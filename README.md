Looking at the changing frequencies of different size analogies in Google Books ngram data. 

Code is pretty messy. Happy to explain/document it on request. If you're interested in extending/reusing some of this work, just drop me a line.

Repro steps:

- Download 'si' 4grams and 5grams files and unzip
  - also, downloaded "as" 5grams, grepped for "as a man 's X" and "as a grain of X" to asamans.tsv and asagrain.tsv. Which are used in disambig.py called by make_df.py. 
- Make sizeof.tsv and sizeof_5.tsv by grepping for '^size of an\? ' (grep.sh)
- run make_df.py
- do stuff with the resulting dataframe/csv thing (see ipython notebooks)


