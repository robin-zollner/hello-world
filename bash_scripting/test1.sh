#!/bin/bash

# Working iwth strings

year=$(date +%Y)
birthyear=1997

my_name=Robin
declare -i my_age=year-birthyear

echo "Hello $my_name, you are $my_age years old"
echo $my_age
echo Do you have a nickname?
read NickName
echo Hello $NickName

zenity --info --title="Test Message" --text="Press Ok" --no-wrap
zenity --warning --title="Test Warning" --text="Press Ok" --no-wrap
zenity --error --title="Test Error" --text=-"Press OK"

if zenity --question --title="Test Question" --text="Press Yes or No" --no-wrap
	then
		zenity --info --title="Yes" --text="You pressed Yes" --no-wrap
	else 
		zenity --info --title="No" --text="You pressed No" --no-wrap
fi

I=$(zenity --calendar)
zenity --info --text="Selected date: $I" --no-wrap