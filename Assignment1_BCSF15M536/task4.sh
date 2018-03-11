#!/bin/bash
if [ $# = 1 ]
then
	file=$1
	touch "temp.txt"
	file1="temp.txt"
	sort $file | uniq -u >> $file1
	rm $file
	touch $file
	cat $file1 >> $file
	rm $file1

elif [ $# -gt 1 ]
then
	echo "too many arguments"
else
	echo "No argument given"
fi

