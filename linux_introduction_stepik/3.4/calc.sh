#!/bin/bash
#functio
cal () { let "res=$1 $2 $3"; echo "$res"; }

while [[ "yes" == "yes" ]]
do
	read x y z
	if [[ $x == "exit" ]]
	then
		echo "bye"
		exit
	elif [[ -n $x || -n $y || -n $z ]]
	then
		case $y in
			"+")
				cal $x "$y" $z;;
			"-")
				cal $x "$y" $z;;
			"*")
				cal $x "$y" $z;;
			"/")
				cal $x "$y" $z;;
			"%")
				cal $x "$y" $z;;
			"**")
				cal $x "$y" $z;;
			*)
				echo "error"
				exit
		esac
	fi
done
