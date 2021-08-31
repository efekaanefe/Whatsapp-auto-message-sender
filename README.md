# Whatsapp-auto-message-sender
A bot to send the same messages to every number in a csv file, at a given time

# ADDING PHONE NUMBER TO CSV FILE
If you want to open phone_book.csv, open it with a text editor, not with an excel-like app because
Phone numbers must be text and add excel-like apps may change it to be a number.
Even though script reads the .csv file columns as texts, format of the number may be changed.
For example excel-like app may change the number +123456789123 to in scientific notation 123e+9
And script reads this as a text like 123e+9, which not the desired format for a phone number :)

Phone number format is like "+90xxxxxxxxxx" (with plus sign and country code in it).


# To use this script properly:
You must have pyautogui and pandas libraries installed in your computer.

You must have logged in to whatsapp web in your default web browser (browser doesn´t need to be opened)
And you shouldn´t do anything, once the script started sending messages.
Bot will start sending once the current hour and current minute are equal to starting hour and starting minute.
So if the hour/min input is already passed, bot will send the messages next day.
Also the estimated time for whatsapp web to open cannot be lesser than the actual time it takes to open it.
If it is lesser, bot will not be able to send the messages, but will print that it sended.
Faster your internet connection and computer is, smaller this value must be.


