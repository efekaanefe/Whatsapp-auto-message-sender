# Whatsapp-auto-message-sender
A bot to send the same messages to every number in a csv file, at a given time

# ADDING PHONE NUMBER TO CSV FILE
IF YOU WANT TO OPEN phone_book.csv, OPEN IT WITH A TEXT EDITOR, NOT WITH AN EXCEL-LIKE APP BECAUSE
PHONE NUMBERS MUST BE TEXT AND ADD EXCEL-LIKE APPS MAY CHANGE IT TO BE A NUMBER.
EVEN THOUGH SCRIPT READS THE .CSV FILE COLUMNS AS TEXTS, FORMAT OF THE NUMBER MAY BE CHANGED.
FOR EXAMPLE EXCEL-LIKE APP MAY CHANGE THE NUMBER +123456789123 TO IN SCIENTIFIC NOTATION 123E+9
AND SCRIPT READS THIS AS A TEXT LIKE 123E+9, WHICH NOT THE DESIRED FORMAT FOR A PHONE NUMBER :)

PHONE NUMBERS MUST BE LIKE "+90XXXXXXXXXX" (WITH PLUS SIGN AND COUNTRY CODE IN IT).


# To use this script properly:
You must have pyautogui and pandas libraries installed in your computer.

You must have logged in to whatsapp web in your default web browser (browser doesn´t need to be opened)
And you shouldn´t do anything, once the script started sending messages.
Bot will start sending once the current hour and current minute are equal to starting hour and starting minute.
So if the hour/min input is already passed, bot will send the messages next day.
Also the estimated time for whatsapp web to open cannot be lesser than the actual time it takes to open it.
If it is lesser, bot will not be able to send the messages, but will print that it sended.
Faster your internet connection and computer is, smaller this value must be.


