#!/bin/bash

# env:parsearg
#
#     the root folder of the package, e.g. the top level of the package structure 
#     as this script lives at the root level, it is just the pwd
#
#     bash$ tree -d $parsearg --charset=ascii | grep -v __pycache 
#
#        /home/tharte/dot/py/python/parsearg
#        |-- build
#        |-- dist
#        |-- doc
#        |   |-- examples
#        |   |-- img
#        |-- install
#        |   |-- bin
#        |   |-- include
#        |   |-- lib
#        |-- src
#        |   |-- parsearg
#        `-- tests
# parsearg=/path/to/top/level/package/source/parsearg
parsearg=$(pwd)

# env:PYTHONPATH
#
# explicitly declare the location of the source code: if the source changes
# then pytest can pick up the change; otherwise pytest may use an /installed/
# version of parsearg (which will not reflect the change in source code)
PYTHONPATH=$parsearg/src

pytest -v $parsearg/tests
