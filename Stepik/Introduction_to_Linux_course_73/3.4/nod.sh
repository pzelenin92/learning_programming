#!/bin/bash

#gcd function
gcd ()
{
	if [[ $1 -eq $2 ]]
	then
		i=$1
		return
	elif [[ $1 -gt $2 ]]
	then
		local x=$1
		local y=$2
	else
		local x=$2
		local y=$1
	fi
	local z=$x

#2nd var
	while [[ "yes" == "yes" ]]
	do
		let "z=$x%$y"
		if [[ $z -ne 0 ]]
		then
			i=$z
			local x=$y
			local y=$z
		else
			break
		fi
	done	
}

#main
while [[ "yes" == "yes" ]]
do
	read M N
	if [[ -z $M ]]
	then
		echo "bye"
		break
	else
		gcd $M $N
		echo "GCD is $i"
	fi
done
