from __future__ import print_function

import argparse
from . import engine

def shuffle_pattern(items):
    items = list(items)
    fixed = [None, None]
    shuffled = []

    for offset, position in ((0, engine.Position.at_beginning), (-1, engine.Position.at_end)):
        if items:
            if items[offset] == position:
                items.pop(offset)
                if items:
                    fixed[offset] = items.pop(offset)

    head, tail = fixed

    if head:
        shuffled.append(head)

    if items:
        shuffled.extend(engine.shuffle(items))

    if tail:
        shuffled.append(tail)

    for item in shuffled:
        if engine.isiterable(item):
            for child in shuffle_pattern(item):
                yield child
        else:
            yield item

def generate(regex, shuffle=False):
    output = engine.execute(regex)
    output = (o for o in (shuffle_pattern if shuffle else engine.flatten)(output) if not isinstance(o, engine.Position))

    return ''.join(map(str, output))

def main():
    parser = argparse.ArgumentParser(description='datagenerator: create test data')
    parser.add_argument('regex', metavar='REGEX', type=engine._str, help='a regular expression pattern for the data to conform to')
    parser.add_argument('--shuffle', action='store_true', default=False, help="randomize the output (for passwords)")

    args = parser.parse_args()

    print(generate(args.regex, args.shuffle))

if __name__ == "__main__":
    main()
