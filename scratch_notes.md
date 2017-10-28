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


'pair of cards' is an old/regional way of saying deck. FASCINATING.

OED: A set of separate things or parts collectively forming a whole, as a set of clothes, a pack of cards, a chest of drawers, etc. Now chiefly Brit. regional and Irish English (north.)

1801   J. Strutt Glig-gamena Angel-ðeod iv. ii. 291   The pack or set of cards, in the old plays, is continually called a pair of cards.
1530   J. Palsgrave Lesclarcissement 182   Vnes cartes, a payre of cardes to playe with.


Deck OED gloss:
 a. ‘A pack of cards piled regularly on each other’ (Johnson); also the portion of the pack left, in some games, after the hands have been dealt. Since 17th c. dial. and in U.S.

 1594   1st Pt. Raigne Selimus sig. F4v   If I chance but once to get the decke, To deale about and shufle as I would.
 1594   R. Barnfield Shepheard Content viii. sig. Eiij   Pride deales the Deck whilst Chance doth choose the Card.
 1595   Shakespeare Henry VI, Pt. 3 v. i. 44   But whilst he sought to steale the single ten, The king was finelie fingerd from the decke.
 1609   R. Armin Hist. Two Maids More-clacke sig. D1v   Ile deale the cards and cut ye from the decke.
 1701   N. Grew Cosmol. Sacra i. iii. §21   The Selenites [have the shape], of Parallel Plates, as in a Deck of Cards.
 1777   J. Brand Observ. Pop. Antiq. (1849) II. 449   In some parts of the North of England a pack of cards is called to this day..a deck of cards.
 1860   in J. R. Bartlett Dict. Americanisms (ed. 3)   
 1882   B. Harte Gentl. La Porte in Flip 135   I reckon the other fifty-one of the deck ez as pooty.
 1884   R. Holland Gloss. Words County of Chester (1886)    Deck o' cards, a pack of cards.
 1885   Cent. Mag. 29 548/1   An old ratty deck of cards.

Shakespeare's King Henry VI has 'But, whiles he thought to steal the single ten, The king was slily finger'd from the deck!'
In an 1826 edition of said play, the editor actually puts an asterisk next to deck and notes:
  A pack of cards was anciently termed *a deck of cards*, or *a pair of cards*, and this is still in use in some parts.
Deck of cards was in currency in Shakespeare's time, but considered archaic in 1826! FASCINATING.
Similar note in an 1864 ed'n
Also in A Glossary of Obscure Words and Phrases in the Writings of Shakspeare (1887)

