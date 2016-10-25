# Koara-py [![Build Status](https://travis-ci.org/koara/koara-py.svg?branch=master)](https://travis-ci.org/koara/koara-py)
Koara-py is a [koara](http://www.koara.io) parser, written in Python.  Koara-py passes the [koara compliancy test](https://github.com/koara/koara-java/tree/master/src/test/resources/tests).

## Installation
Via Pip:
```
pip install koara
```
Via Easy Install:
```
easy_install -U koara
```
Or download [koara.py](https://github.com/koara/koara-py/blob/master/koara.py)

## Usage
```python
import koara

parser = koara.Koara()
print parser.parse('This text will be converted to HTML')

# Extensions can be enabled during construction:
parser2 = koara.Koara(['autolinks', 'tables'])
print parser2.parse('This text will be converted to HTML')
```

## Community
Koara is released under version 2.0 of the Apache License. We love any contribution!

* [Github](http://github.com/koara)
* [Twitter](http://twitter.com/koaralang)


