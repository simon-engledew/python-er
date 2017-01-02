[![Build Status](https://travis-ci.org/simon-engledew/python-er.svg)](https://travis-ci.org/simon-engledew/python-er)
![Python Versions](https://img.shields.io/pypi/pyversions/er.svg)
![Licence](https://img.shields.io/pypi/l/er.svg)
![Format](https://img.shields.io/pypi/format/er.svg)

```
pip install er
```

A python micro library that generates data matching a given regular expression.

On the command-line:

```
# er 'he?llo there{4,5}'

hllo thereeee
```

or from python:

```
>>> import er

>>> print er.generate('he?llo there{4,5}')

'hello thereeeee'
````
