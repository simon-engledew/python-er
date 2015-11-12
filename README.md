```
pip install er
```

A python 2.7.x micro library that generates data matching a given regular expression.

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