from __future__ import division
import pandas as pd
import sys
import numpy as np
from collections import defaultdict
from special_cases import *
import disambig
import utils

# Whether to merge minor ortho variations described in foo.canonical_formers
# Also merge adj + X -> X (see foo.jjs)
CANONIZE = 1

DISAMBIG = True

NORMALIZE = 1

CENSOR = 1

# If true, measure number of distinct books each comparison appears in, rather 
# than its total uses across books.
COUNT_BOOKS = 0

# Whether to use english fiction dataset (vs. all English books)
if len(sys.argv) > 1:
  assert sys.argv[1] == 'f', 'Unrecognized command line args {}'.format(sys.argv)
  FICTION = 1
else:
  FICTION = 0

MIN_YEAR = 1800

# Year thresholds
THRESHES = [1900, 2000, 2100]
if FICTION:
  # < 1940: 10% of fiction
  # >= 2000: 50% of fiction
  THRESHES = [1940, 2000, 2100]

def make_row(yr_to_count, token, raw_ytc):
  assert len(yr_to_count), "Got no counts for token <{}>".format(token)
  years = yr_to_count.keys()
  counts = yr_to_count.values()
  total = sum(counts)
  raw_total = sum(raw_ytc.values())
  first, last = min(years), max(years)
  maxcount = max(counts)
  modeyrs = [yr for (yr, count) in yr_to_count.iteritems() if count==maxcount]
  # Calculate mean and median years
  yearsum = 0
  countseen = 0
  median_yr = None
  for yr in sorted(yr_to_count.keys()):
    count = yr_to_count[yr]
    yearsum += yr*count
    countseen += count
    if countseen >= total/2 and median_yr is None:
      median_yr = yr
  mean_yr = yearsum / total

  y0, y1, y2 = THRESHES
  total_pre1900 = sum(count for (yr, count) in yr_to_count.iteritems() if yr < y0)
  total_20c = sum(count for (yr, count) in yr_to_count.iteritems() if y0 <= yr < y1)
  total_21c = sum(count for (yr, count) in yr_to_count.iteritems() if y1 <= yr < y2)

  return dict(token=token, total=total, mean_yr=mean_yr, median_yr=median_yr, first_yr=first, 
      last_yr=last, mode_yr=modeyrs[0],
      total_pre1900=total_pre1900, total_20c=total_20c, total_21c=total_21c,
      annual_max=maxcount, raw_total=raw_total,
      )


bucket_phrases = set.union(
    *[
    {headword + ' ' + complement for complement in buckets[headword]}
    for headword in buckets
    ]
)
token_to_year_to_count = defaultdict(lambda : defaultdict(int))
#for grams, fname in [(4, 'sizeof.tsv'), (5, 'sizeof_5.tsv')]:
for grams in (4, 5):
  fname = 'sizeof_{}{}.tsv'.format(
      grams, '_fiction' if FICTION else '')
  f = open(fname)

  for line in f:
    phrase, yr, count, _books = line.split('\t')
    if COUNT_BOOKS:
      count = _books
    yr, count = map(int, [yr, count])
    if yr < MIN_YEAR:
      continue
    # Let's just skip uppercase "Size of a...". Likely to be a book title or something.
    if phrase[0] == 'S':
      continue
    tokens = phrase.split()
    token = ' '.join(tokens[3:])
    if grams == 4 and (token in full_split or token in jjs):
      continue
    if grams == 5:
      first = tokens[3]
      if token in bucket_phrases:
        pass
      elif first in jjs:
        if CANONIZE:
          # Turn something like "small car" into just "car"
          token = tokens[4]
      elif first in full_split:
        pass
      else:
        continue

    token_to_year_to_count[token][yr] += count

  f.close()

ttytc = token_to_year_to_count # ow my fingers
# Adjust bucket headword counts (subtract the headword + complement phrase counts)
for headword, complements in buckets.iteritems():
  hw_counts = ttytc[headword]
  for complement in complements:
    phrase = headword + ' ' + complement
    if phrase not in ttytc:
      print "Warning: No counts found for bucket phrase <{}>".format(phrase)
      continue
    for (yr, count) in ttytc[phrase].iteritems():
      hw_counts[yr] -= count

if CANONIZE:
  for alt, canon in canonical_forms.items():
    if alt not in ttytc:
      print "No counts found for canonicalizable token <{}>".format(alt)
      continue
    alt_counts = ttytc[alt]
    canon_counts = ttytc[canon]
    for (yr, count) in alt_counts.iteritems():
      canon_counts[yr] += count
    del ttytc[alt]

# renames
for orig, renamed in renames.iteritems():
  if orig not in ttytc:
    print "No counts for renamable token <{}>".format(orig)
    continue
  counts = ttytc[orig]
  assert renamed not in ttytc
  ttytc[renamed] = counts
  del ttytc[orig]

if DISAMBIG:
  for phrase in disambig.disambig_phrase_to_fname:
    disambig.disambig(phrase, ttytc)

if CENSOR:
  for token in verboten:
    if token not in ttytc:
      print "Missing censorable token <{}>".format(token)
      continue
    del ttytc[token]

raw_ttytc = {}
for token, ytc in ttytc.iteritems():
  raw_ttytc[token] = ytc.copy()
if NORMALIZE:
  utils.normalize(ttytc)

# Make the dataframe
rows = [make_row(ytc, token, raw_ttytc[token]) for (token, ytc) in ttytc.iteritems()]

#out_fname = '5grams.csv' if '5' in fname else '4grams.csv'
out_fname = 'merged{}{}.csv'.format(
    '_fiction' if FICTION else '',
    '_nocanon' if not CANONIZE else '',
    )
df = pd.DataFrame(rows)
df.to_csv(out_fname, index=False)
