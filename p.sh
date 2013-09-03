#! /bin/sh
echo $#, $1, $2
echo $*
./pre-commit.py $*

echo $?

#git last | grep -q aaa && echo $?
