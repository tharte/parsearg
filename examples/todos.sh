#!/bin/bash

#python todos purge users
#python todos purge todos

python todos.py create user foo -e foo@foo.com -p 212-555-1234
python todos.py create user bar -e bar@bar.com
python todos.py create user qux -p 212-123-5555

exit

python todos.py create todo foo title1 -c description1 -d 2020-11-30
python todos.py create todo foo title2 -c description2 --due-date=2020-12-31
python todos.py create todo qux todo-1 --description=Christmas-party -d 2020-11-30
python todos.py create todo qux todo-2 --description=New-Year-party

python todos.py update user email qux qux@quxbar.com
python todos.py update user phone bar 203-555-1212

python todos.py update todo title 4 most-important
python todos.py update todo description 4 2021-party
