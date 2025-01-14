# Morse Code Based Authentication System
This is my 8th semester project, which implements a novel authentication system using Morse code recognition. 
It utilizes computer vision and machine learning techniques to verify user authentication based on their Morse code input.

Features:

Registration Process:

Create User: Users start by creating an account with a username and password.
Face Enrollment: The system captures the user's facial data for future recognition. 
Success/Failure: If the face enrollment is successful, the user is registered. If not, the registration fails, and the user is notified.

Login Process:

User Authentication: The user enters their username and password.

Face Detection: The system attempts to recognize the user's face. If face detection fails, an alert message is sent via a Telegram bot. If face detection is successful, the user proceeds to the next step. 

Morse Code Authentication: The user enters Morse code by blinking, using a virtual keyboard. 
The system interprets the blinks into Morse code and verifies it. 
If Morse code authentication is successful, the user is logged in. 
If Morse code authentication fails, the login is unsuccessful, and the user may be prompted to answer a security question to reset their Morse code password.

Alerts:

Telegram Notifications: Alerts are sent via a Telegram bot for events such as failed face detection attempts. 
Key Components :
Facial Recognition: Uses OpenCV for capturing and recognizing the user's face. 
Morse Code Input: Interprets user blinks into Morse code using a virtual keyboard. 
Telegram Bot: Sends alert messages to the user in case of failed authentication attempts.



Installation and usage procedure:

1. Download and install Python version 3.11 from the following link : 
https://www.python.org/downloads/release/python-3110/
Add the path of the “Python.exe” file to the “Path” folder in System 
environment variables.

2. Open command prompt and install the following libraries

   • pillow

   • numpy

   • PyQt5

   • telepot

   • dlib

   • opencv
 
   • pandas

   • opencv-contrib

Use the following command in command prompt to install the 
libraries : 
pip install library_name.py

3. Ensure proper installation of the libraries

4. Open command prompt in the project folder and run the following command :
   python Morse_login.py

Regsitration Process

5. Begin the registration process by clicling the “REGISTER” button.
   
6. Enter the details which will be used later in the login process, such as:
• Username.
• Password.
• Morse password.
(Give any 2 digit number for which you know the morse code 
conversion. 
Eg : The Morse code for 00 is 10 dashes ie _ _ _ _ _ _ _ _ _ _).
• Nickname ( for password reset).
• Re-enter Nickname.

7. Enter the follwing registration details to train the Facial Recognition 
dataset:
• Id no.
• Name.

8. The Camera application is opened and 121 images of the User’s face is 
captured.
Note: Make sure to use a high quality webcam and sit in a well lit room.

9. After the completion of capturing 121 images, click on the “Quit” button 
of the face id registration window (window with Green background).

10. Close the User details regsitration window ( window with Blue
background).

11. Also close the small pop-up window which shows the message reading 
“Registration Successful”.


LOGIN PROCESS

12. Click on the “LOGIN” button on the Welcome screen.
The user’s face is recognised if it is a registered user and his/her name is 
displayed along with a pop-up which says “ Logged in Successfully”.
OR
If it is an unknown user a mail is sent to a telegram chat bot containing 
the image of the unknown user .

13. Close the pop up , camera application and the welcome screen .
    
14. Enter the Username and Password which was previously entered in the 
Registration process.
In case the user has forgetten the password, petname entered during 
Registraion process can be used to reset it.

15. The Morse Code based authentication starts and the morse password is 
entered through eye blinks.


For example , if the user had entered 00 as their morse password, 
Blink when the cursor is on the “ _” symbol of the virtual keyboard.
The user has to blink 10 times to enter the 10 dashes 
ie “ _ _ _ _ _ _ _ _ _ _”.

Note: refer the command prompt window to see the characters which 
have been entered as input.

16. Any wrong input can be deleted by blinking when the cursor is on “<” 
symbol (Backspace).

17. After the completion of Morse code authentication , a final message 
screen opens, indicating successful authentication.
