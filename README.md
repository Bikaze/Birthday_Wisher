# Birthday Email Sender(Birthday Wisher)

This Python script checks if today matches a birthday in the birthdays.csv file and sends a birthday email if there is a match. It also sends a notification to another email.

## Overview
The script uses pandas to read birthday data from a CSV file, the datetime library to get the current day and month, and smtplib to send birthday emails. If there is a birthday today, a random letter template is chosen and sent to the celebrant. A notification email is also sent to another email address.

## How to Use
1. Ensure that you have the necessary dependencies installed, including pandas, datetime, and smtplib.
2. Update the birthdays.csv file with the relevant birthday data.
3. Add the letter templates in the letter_templates directory.
4. Update the sender's email and password in the script.
5. Update the notification email address in the script.

## Code Overview
The main components of the code include:
- Reading birthday data from a CSV file using pandas and the datetime library to match the current date.
- Sending birthday emails using the smtplib library.
- Choosing a random letter template and customizing it with the celebrant's name.
- Sending a notification email to another email address.

The script provides a simple way to automate the process of sending birthday wishes via email and notifying another email address.
