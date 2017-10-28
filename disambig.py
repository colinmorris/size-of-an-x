from __future__ import division
from collections import defaultdict

# If true, measure number of distinct books each comparison appears in, rather 
# than its total uses across books.
COUNT_BOOKS = 0

disambig_phrase_to_fname = {
    "man 's": 'asamans.tsv',
    "grain of": 'asagrain.tsv',
}

def make_ttytc(fname):
  f = open(fname)
  token_to_year_to_count = defaultdict(lambda : defaultdict(int))
  ttytc = token_to_year_to_count # ow my fingers

  for line in f:
    phrase, yr, count, _books = line.split('\t')
    if COUNT_BOOKS:
      count = _books
    tokens = phrase.split()
    token = tokens[-1]
    yr, count = map(int, [yr, count])

    token_to_year_to_count[token][yr] += count

  f.close()
  return ttytc

def disambig(phrase, ttytc):
  disam_fname = disambig_phrase_to_fname[phrase]
  subs = make_ttytc(disam_fname)

  totals_per_year = defaultdict(int)
  for sub, sub_ytc in subs.iteritems():
    for yr, count in sub_ytc.iteritems():
      totals_per_year[yr] += count

  base = ttytc[phrase]
  for sub, sub_ytc in subs.iteritems():
    subphrase = phrase +' ' + sub
    for year, base_count in base.iteritems():
      try:
        sub_fraction = sub_ytc[year] / totals_per_year[year]
      except ZeroDivisionError:
        # uh oh
        print '.',
        sub_fraction = 1 / len(subs)
      ttytc[subphrase][year] = base_count * sub_fraction
  del ttytc[phrase]

