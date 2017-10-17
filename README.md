Repro steps:

- Download 'si' 4grams and 5grams files and unzip
- Make sizeof.tsv and sizeof_5.tsv by grepping for '^size of an\? ' (grep.sh)
- make_df.py on each of those tsv files to make csvs
- merge_dfs.py
- ipynb

(Also, at some point did some manual editing of sizeof.tsv to put 'a hen' and 'an hen' next to each other...)

- actually, nvm steps 3 and 4 above. Just run make_df2.py. Which seems to work.

Misc ideas possibly worth trying:
- merge orthographic variations? golf ball, golfball, golf-ball, etc.
  - maybe worth recording the 'raw' form, and also making another df with canonical/deduped forms merged together. Because changes in content and orthography over time can both be kind of interesting. (Though the former probably more so.)
  - same question with modified objects. 'car' vs. 'small car' (both of which have >1000 appearances), etc.
- instead of/in addition to counting total occurrences, count number of books appeared in. 
  - tried this. Seemed to have very little effect on the top 10-20 per era.
- just use fiction ngrams (gets rid of a lot of the non-figurative 'size of a X' phrases).

Some notes on particular phrases/tokens:

Partial phrases with basically unambiguous completions:
- hen's -> egg
- pin's -> head
- pigeon's -> egg (weird!)
- hazel -> nut (specifically, "hazel nut" and "hazel-nut", the latter of which gets split into 3 tokens)
- hemp -> seed (as above)
- millet -> grain/seed
- marrowfat -> pea
- deck -> of cards
- credit -> card

More ambiguous completions:
- grain of -> {rice, salt, sand, millet, wheat, dust...}
- man's -> {hand, fist, head, forefinger, leg, fingernail...}
- child's -> similar to man's
- pepper -> mostly corn/'- corn', but also pepper-box, pepper seed, pepper-shaker

  
Looking at 5grams for "of a man 's X" will produce too many fposes on other phrases. Stages of a man's life. The women of a man's family. Part of a man's life. etc.
- I guess maybe this just becomes an asterisk. :(
- Hm, I guess you could do some kind of manual estimation of the ratio of different man parts (fist, head, etc.), and break the counts up that way. For the purposes of looking at the top 10 or 20, it'll probably just be like 0-3 parts that chart. But won't be able to tell how different parts vary differentially over time.

Ideas about how to organize/present the data:
- Overall top n
- Most archaic / recent. Show with line chart per term?
- Top n per century (and try to show movement in some elegant way)
- Top n restricted to some certain domain? Coins, nuts, fruits, sports balls, animals, etc. I think grouping is a fruitful idea. Could also do...
  - Within a group, look at how each member's popularity has changed over time.
  - Look at the popularity of different groups as a whole (+ over time)

