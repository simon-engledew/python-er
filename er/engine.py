import random
import sre_parse

random = random.SystemRandom()

def to_tuple(o):
    return tuple(o) if hasattr(o, '__iter__') else (o,)

def flatten(items):
    for item in items:
        if hasattr(item, '__iter__'):
            for child in flatten(item):
                yield child
        else:
            yield item

def shuffle(items):
    items = list(items)
    random.shuffle(items)
    return items

class Enum(object):
    """
        Enforces integrity of enumerated values.
        Allows reverse lookup of enumerated values.

        States = Enum('STOPPED', 'STARTED')

        States.STOPPED
        # => STOPPED

        States.STARTED
        # => STARTED

        States['STARTED'] == States.STARTED
        # => True

        States.STARTED
        # => KeyError: "key STARTED not in Enum(STOPPED=0,STARTED=1)"
    """

    class Value(object):
        def __init__(self, value, name):
            self.value = value
            self.name = name

        def __eq__(self, other):
            return self.value == other

        def __gt__(self, other):
            return self.value > other

        def __lt__(self, other):
            return self.value < other

        def __ge__(self, other):
            return self.value >= other

        def __le__(self, other):
            return self.value <= other

        def __hash__(self, other):
            return hash(self.value)

        def __str__(self):
            return str(self.name)

    def __init__(self, *args):
        self.__keys__ = dict((arg, Enum.Value(i, arg)) for i, arg in enumerate(args))

    def __len__(self):
        return len(self.__keys__)

    def __iter__(self):
        return iter(self.__keys__)

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __getitem__(self, key):
        try:
            return self.__keys__[key]
        except KeyError:
            raise KeyError('key %s not in %s' % (key, self))

    def __str__(self):
        return 'Enum(%s)' % ', '.join(str(o) for o in sorted(self.__keys__.values()))

Position = Enum(
    'at_beginning',
    'at_end'
)

def consume_literal(literal):
    return lambda: ['%c' % literal,]

def consume_range(start, end):
    return lambda: ['%c' % literal for literal in xrange(start, end)]

def consume_branch(unknown, branches):
    return lambda: (choice() for choices in (consume((tokens,)) for tokens in random.choice(branches)) for choice in choices)

def consume_in(*tokens):
    choices = consume(tokens)
    return lambda: random.choice([value for choice in choices for value in choice()])

def consume_at(position):
    return lambda: Position[position]

def consume_max_repeat(start, end, tokens):
    choices = consume(tokens)
    return lambda: [choice() for choice in choices for i in xrange(0, random.randint(start, min(end, 255)))]

def consume_subpattern(id, tokens):
    # print id, tokens
    choices = consume(tokens)
    return lambda: [choice() for choice in choices]

def consume(tokens):
    return [globals()['consume_%s' % name](*to_tuple(args)) for name, args in tokens]

def execute(pattern):
    tokens = sre_parse.parse(pattern)
    return (token() for token in consume(tokens))
