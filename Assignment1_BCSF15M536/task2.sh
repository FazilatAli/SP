#!/bin/bash
fileName=$1
lines=`cat $fileName | wc -l`

touch "even.txt"
touch "odd.txt"
evenFile="even.txt"
oddFile="odd.txt"
i=0
c=1
#reading file
while IFS= read -r line || [[ -n "$line" ]];
do 
	c=`expr $c % 2`
	if [ $c -eq 0 ]
	then
		echo "$line" >> $evenFile
	else
		echo "$line" >> $oddFile
	fi
	c=`expr $c + 1`
done < "$fileName"

echo "Even file: " 

cat "$evenFile"
echo "Odd file: "
cat "$oddFile"

	
