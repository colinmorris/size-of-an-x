Looking at the changing frequencies of different size analogies in Google Books ngram data. For more context, check out my [blog post](http://colinmorris.github.io/blog/size-of-things).

`sizeofthings.csv` has a processed version of the data if you don't want to download several gb of raw ngram data and run the various munging scripts. The `raw_total` column is just the raw number of times `size of $token` appeared in books from 1800-2008 (it is occasionally fractional because of some trigram hacks described in the appendix of the blog post). The `total` column (and per-century total columns) are normalized by number of words scanned per year.

Code is pretty messy. Happy to explain/document it on request. If you're interested in extending/reusing some of this work, just drop me a line.

Rough steps for end-to-end repro:

- Download 'si' 4grams and 5grams files and unzip
  - also, downloaded "as" 5grams, grepped for "as a man 's X" and "as a grain of X" to asamans.tsv and asagrain.tsv. Which are used in disambig.py called by make_df.py. 
- Make sizeof.tsv and sizeof_5.tsv by grepping for '^size of an\? ' (grep.sh)
- run make_df.py
- do stuff with the resulting dataframe/csv thing (see ipython notebooks)


