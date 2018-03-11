#!/bin/bash
arr=(`find . -type f| perl -ne 'print $1 if m/\.([^.\/]+)$/' |sort -u`) #file extensions
arr1=(`ls -f`)
count=${#arr[*]}
count=`expr $count - 1`
if [ $count -eq 0 ]
then
	echo "no file found"
else
	for file in ${arr[*]}
	do
		mkdir "/home/fazilatali/$file files"  #createing directories
	done
		
	for file1 in ${arr1[*]}
	do
		for file in ${arr[*]}
		do
			if [ "${file1##*.}" = "$file" ]
			then
			`mv "$file1" "/home/fazilatali/$file files/"` #moving files to appropriate folder
			fi
		done
		count=`expr $count - 1`
	done
fi



