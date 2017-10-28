jjs = {
    'small', 'large', 'ordinary', 'single',
    'average', 'common', 'middling',
    'packaged', 'considerable',
    'moderate', 'normal', 'individual',
    'regular', 'small', 'typical',
    'particular', 'little', 'medium',
    'standard', 'fine',
}


# These have no meaning by themselves
full_split = {
    'half', 'silver',
    'tennis', 'golf', 
    'digital', 'Web',
    'magnetic',
    'soccer',
    'good',
    'pocket',
    'bowling',
    'ten', 'five', 'fifty', 'twenty', 'hundred', 'three', 'one', 'six',
    'beach',
    'very',
    'coffee',
    'soup',
    'tea',
    'living',
    'swimming',
    'mustard',
    'water',
    'real',
    'grown',
    'walking',
    'walk',
    'actual',
    'entire',
    'few',
    'given',
    'English',
    'split',
    'modern',
    'domestic',
    'black',
    'millet',
    'tame',
    'writing',
    'bread',
}

# Each of the keys here makes a separate phrase. The rest of the 4gram count
# after subtracting these phrases should go with the head word.
# TODO: "'s" pretty much makes sense after everything.
buckets = {
    'man': ["'s"],
    'boy': ["'s"],
    'child': ["'s",],

    'pin': ["'s", 'head', 'prick', '-'],
    'egg': ['cup', 'yolk'],
    'football': ['field', 'pitch', 'player', 'stadium'],
    'baseball': ['bat', 'card', 'diamond', 'field', 'glove',
                'infield', 'mitt', 'stadium'],
    'basketball': ['court'],
    'hen': ['egg', 'turkey', "'s"],

    'quarter': ['dollar', "-"],
    'dollar': ['bill', 'coin', 'piece',],

    'orange': ['crate',],
    'pigeon': ["'s", "egg"],
    'ostrich': ["'s", "egg"],
    'duck': ["'s", "egg"],
    'robin': ["'s", 'egg'],
    'grain': ['of'],
    'house': ['fly', 'cat', 'brick', 'mouse', 'rat', 'sparrow',
              'trailer', 'lot'],
    'city': ['block', 'bus', 'lot', 'square'],
    'human': ['baby', 'body', 'brain', 'cell', 'eye','face',
              'finger', 'fist', 'foot', 'hair', 'hand', 'head',
              'heart', 'palm', 'skull', 'thumb', "'s",
              ],
    'cherry': ['pit', 'stone', 'tomato', 'tree'],
    'goose': ['egg', 'quill', "'s"],
    'family': ['Bible', 'car', 'farm',],
    'soda': ['can', 'straw'],
    'pea': ['-'],
    'dinner': ['napkin', 'plate', '-'],
    'crown': ['piece', '-'],
    'horse': ['bean', 'blanket', 'chestnut', "'s"],
    'dog': ['house', 'kennel', "'s"],
    'cat': ["'s"],
    'cricket': ['ball', "-",],
    'phone': ['book', 'booth',],
    'lead': ['pencil', '-', '--'],
}

verboten = {
    'object', 'image', 'population', 'tax', 'partition', 'IP',
    # mostly 'treatment effect'. Appears in medical/scientific literature.
    'treatment',
    # size of an Ethernet frame
    'Ethernet',
    'network', 'array',
    'message',
    # I guess file cabinet is legit
    'file',
    'group',
    'city', 'country',
    'atom',
    # should probably split like man's/grain of
    "child 's",
    "room",
    # NB: house is pretty problematic in terms of non-figurative use (I briefly tallied
    # on my fingers while browsing google books, and it seemed like at least 25% of instances
    # were non-figurative. Might want to actually handwave some factors to penalize such terms
    # by to account for mixed use.
    'farm',
    'family',
}

canonical_forms = {
    "pin 's": "pinhead",
    "pin head": "pinhead",
    "pin -": "pinhead",
    "hazel": "hazelnut",
    "goosequill": "goose quill",
    "goose 's": "goose egg",
    "pea -": "peanut",
    "dinnerplate": "dinner plate",
    "crown -": "crown piece", 
    "beach ball": "beachball",
    "beach -": "beachball",
    "pigeon egg": "pigeon 's",
    "lead -": "lead pencil",
    "lead --": "lead pencil",
    "millet -": "millet seed",
    "millet --": "millet seed",
    "milletseed": "millet seed",
    "hen egg": "hen 's",
    "pigeon egg": "pigeon 's",
    "bread box": "breadbox",
    "bread -": "breadbox",
}
_balls = ['golf', 'foot', 'basket', 'base', 'tennis']
for ball in _balls:
  # yukyuk
  canonball = ball + (' ' if ball in ('golf', 'tennis') else '') + 'ball'
  alt1 = ball + ' ball'
  if alt1 != canonball:
    canonical_forms[alt1] = canonball
  alt2 = ball + 'ball'
  if alt2 != canonball:
    canonical_forms[alt2] = canonball
  # might be over promiscuous
  canonical_forms[ball + ' -'] = canonball

# Basically the same as canonical_forms, except in the latter case the phrase
# being mapped to is assumed to already exist in ttytc. In this case, it is 
# assumed not to exist (and this is verified at runtime).
renames = {
    "hen 's": "hen's egg",
    "pigeon 's": "pigeon's egg",
    "marrowfat": "marrowfat pea",
    "credit": "credit card",
    "deck": "deck of cards",
    "knitting": "knitting needle",
    "hickory": "hickory nut",
    "postage": "postage stamp",
}

cats = dict(
    nuts = {
      'walnut', 'hazelnut', 'peanut', 'almond',
      },
    body_parts = {
      'fist', "man 's", "child 's", 'thumb',
    },
    fruit = {
      'orange', 'apple', 'plum', 'grapefruit', 'cherry',
      },
    vegetables = {
      'pea', 'bean',
      },
    eggs = {
      'egg', "hen 's", "pigeon 's",
      },
    coins = {
      'quarter', 'dime', 'penny', 'nickel', 'sixpence', 'crown piece', 'shilling',
      'cent', 'cent piece', 'silver dollar'
    },
    balls = {
      'soccer ball',
    }.union({ball+'ball' for ball in _balls}),
    other_sports = {
      'football field',
    },
    animals = {
      'dog', 'horse', 'cat', 'pigeon',
    },
)

"""
bp      bodyparts
pe      person
ve      vegetable/grain
co      coin
nu      nut
eg      egg
sp      sports
fr      fruit
ba      ball
an      animal
hh      household
ar      architectural features
bu      building
ge      geographic features
tr      transportation
fo      food not otherwise specified
"""
