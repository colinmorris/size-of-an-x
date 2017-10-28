from __future__ import division
import pandas as pd
from collections import defaultdict
from soa_data import data as soa_norms

def load_totalcounts(fiction=False):
  count_fname = 'totalcounts{}.txt'.format('_fiction' if fiction else '')
  f = open(count_fname)

  nugs = f.read().split('\t')
  rows = [map(int, nug.split(',')) for nug in nugs if len(nug) > 1]
  cols = ['year', 'matches', 'pages', 'books']
  cdf = pd.DataFrame(rows, columns=cols)
  cdf.set_index('year', drop=False, inplace=True)
  return cdf

def normalize_sizeofs(ttytc):
  """Normalize by number of 'size of a's per year.
  So the 'counts' per year are the % of 'size of a's with the given ending.
  """
  # 'standard' number of matches per year
  baseline = 10**9
  tc = load_totalcounts()
  yrs = range(1800, 2009)
  norm_per_year = dict(zip(yrs, soa_norms))
  for _, ytc in ttytc.iteritems():
    for yr in ytc:
      n = tc.loc[yr, 'matches']
      n *= norm_per_year[yr]
      ytc[yr] *= 1 / n

def normalize_sigma(ttytc):
  # normalize the data so that the counts for each year add up to this (across tokens)
  baseline = 100
  counts_per_year = defaultdict(int)
  for _, ytc in ttytc.iteritems():
    for yr, count in ytc.iteritems():
      counts_per_year[yr] += count

  for term, ytc in ttytc.iteritems():
    for yr in ytc:
      ytc[yr] *= baseline / counts_per_year[yr]


def normalize_tc(ttytc):
  totalcounts = load_totalcounts()
  # 'standard' number of matches per year
  baseline = 10**9
  for term, ytc in ttytc.iteritems():
    for yr in ytc:
      adj = baseline / totalcounts.loc[yr, 'matches']
      ytc[yr] *= adj

normalize = normalize_tc
