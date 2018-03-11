#!/bin/bash
Is_lower()
{
	string="$@"
	lower=$(tr '[A-Z]' '[a-z]'<<<"${string}")
	echo $lower
}
Is_root()
{
	true=1
	false=0
	if [ `id -u` -eq 0 ]
	then
		return $true
	else
		return $false
	fi
}
Is_user_exist()
{
	true=1
	false=0
	u=`id -u -n`
	file="/etc/passwd"
	dd=`grep "$u" $file`
	if [ -z "$dd" ]
	then
		echo "user does not exist"
	else
		echo "user exist"
	fi
	
}
Is_lower $@
if [ Is_root = 1 ]
then 
	echo "root user"
else
	echo "Not a root user"
fi 

Is_user_exist



