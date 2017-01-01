import collections
import enum
import random
import sre_parse
import sys

random = random.SystemRandom()

def to_tuple(value):
    return tuple(value) if isiterable(value) else (value,)

_chr = unichr if sys.version_info.major == 2 else chr
_str = unicode if sys.version_info.major == 2 else str
_range = xrange if sys.version_info.major == 2 else range

def isiterable(value):
    return (
        isinstance(value, collections.Iterable) and
        not isinstance(value, (bytes, _str))
    )

def flatten(items):
    for item in items:
        if isiterable(item):
            for child in flatten(item):
                yield child
        else:
            yield item

def shuffle(items):
    items = list(items)
    random.shuffle(items)
    return items

@enum.unique
class Position(enum.Enum):
    at_beginning = 1
    at_end = 2

def consume_literal(literal):
    return lambda: [_chr(literal)]

def consume_range(start, end):
    return lambda: [_chr(literal) for literal in _range(start, end)]

def consume_branch(unknown, branches):
    return lambda: (choice() for choices in (consume((tokens,)) for tokens in random.choice(branches)) for choice in choices)

def consume_in(*tokens):
    choices = consume(tokens)
    return lambda: random.choice([value for choice in choices for value in choice()])

def consume_at(position):
    return lambda: Position[str(position).lower()]

def consume_max_repeat(start, end, tokens):
    choices = consume(tokens)
    return lambda: [choice() for choice in choices for i in _range(0, random.randint(start, min(end, 255)))]

def consume_subpattern(id, tokens):
    choices = consume(tokens)
    return lambda: [choice() for choice in choices]

def consume(tokens):
    return [globals()['consume_{}'.format(str(name).lower())](*to_tuple(args)) for name, args in tokens]

def execute(pattern):
    tokens = sre_parse.parse(pattern)
    return (token() for token in consume(tokens))
