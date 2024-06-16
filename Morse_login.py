from tkinter import *
import os
import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.font as font
import os
from tkinter import *
import tkinter as ttk
import sys
import os 
import pathlib
import cv2
import numpy as np
import dlib
from math import hypot
import time
import random
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QDesktopWidget, QPushButton, QGridLayout
from morse_converter import MorseConverter as mc
import telepot

global  username1
global username12

bot=telepot.Bot("7059925065:AAFxGEhyzYDTePhXI2NdTEplpRtZLaw4-6M")
ch_id="1374196115"
bot1=telepot.Bot("7059925065:AAFxGEhyzYDTePhXI2NdTEplpRtZLaw4-6M")
ch_id1="1374196115"


# Counters
frames = 0
letter_index = 0
blinking_frames = 0
frames_to_blink = 6
frames_active_letter = 9

# Text and keyboard settings
text = ""
text1=[]
keyboard_selected = "left"
last_keyboard_selected = "left"
select_keyboard_menu = True
keyboard_selection_frames = 0
count=0
pf =[]
scanned=0

class MouseClicksMorse(QWidget):
    global username1
    global username12
    
    def __init__(self):
        super().__init__()
        self.inputArea = InputArea()
        self.initUI()

    def initUI(self):
        self.center()
        self.resize(700, 500)
        self.setWindowTitle('Mouse Clicks - Morse Code Conversion')

        self.inputArea.update_labels.connect(self.updateLabels)
        self.inputArea.clear_labels.connect(self.clearLabels)

        inst = QLabel()
        inst.setText('Instructions:\n Dot (.)\t\t:  Left Click\n Dash (-)\t\t:  Double Left Click\n Next Letter\t:  Right Click\n Next Word\t:  Double Right Click')
        font = QtGui.QFont("MoolBoran", 18)
        font.setStyleHint(QtGui.QFont.TypeWriter)
        inst.setFont(font)

        grid = QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(inst, 1, 3)
        grid.addWidget(self.inputArea, 1, 0, 5, 1)
        grid.addWidget(self.inputArea.outputMorse, 3, 3)
        grid.addWidget(self.inputArea.outputConverted, 4, 3)
        grid.addWidget(self.inputArea.clearButton, 5, 3)

        self.setLayout(grid)

        self.setGeometry(300, 300, 550, 300)
        self.setWindowTitle('Mouse Clicks - Morse Code Conversion')

        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def updateLabels(self):
        self.inputArea.outputMorse.setText('Morse Code: <b>' + self.inputArea.message.replace('*', ' ').replace('.', '·'))
        if self.inputArea.message[-1] == '*':
            self.inputArea.outputConverted.setText('Conv. Text: <b>' + mc._morseToText(self.inputArea.message))    ##outputConvclearLabelserted

    def clearLabels(self):
        self.inputArea.outputMorse.setText('Morse Code: ')
        self.inputArea.outputConverted.setText('Conv. Text: ')
        test1=mc._morseToText(self.inputArea.message).strip('\n').strip('\t').strip(' ')
        print('dffdfddddddddddddddddd')
        print('username ,type {},{}'.format(username1,type(username1)))
        username12=username1 + '.txt'
        print((username12))

        file2 = open(username12, "a")
        
        print(file2)        
        file2.write(username1+ ',' + str(test1))
        
        file2.close()
        self.inputArea.message = ''
        exit()


class InputArea(QWidget):

    update_labels = pyqtSignal()
    clear_labels = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timeout)
        self.click_count = 0
        self.message = ''
        self.temp = ''

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

        self.outputMorse = QLabel()
        self.outputMorse.setText('Morse Code: ')
        self.outputConverted = QLabel()
        self.outputConverted.setText('Conv. Text: ')
        font = QtGui.QFont("Consolas", 10)
        font.setStyleHint(QtGui.QFont.TypeWriter)
        self.outputMorse.setFont(font)
        self.outputConverted.setFont(font)

        self.clearButton = QPushButton('Clear All')
        self.clearButton.clicked.connect(self.sendClearSignal)

    def mousePressEvent(self, event):
        self.click_count += 1
        if event.button() == Qt.LeftButton:
            self.temp = '.'
        if event.button() == Qt.RightButton:
            self.temp = '*'
        if not self.timer.isActive():
            self.timer.start()

    def timeout(self):
        if self.click_count > 1:
            if self.temp == '*':
                self.message += '**'
            else:
                self.message += '-'
        else:
            self.message += self.temp
        self.click_count = 0
        self.update_labels.emit()

    def sendClearSignal(self):
        self.clear_labels.emit()

    def getMessage(self):
        return self.message

    def printMessage(self):
        print(self.message)



#This method is for Registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.configure(background ='#2283a1')
    register_screen.geometry("1000x750")
    global username
    global password
    global morse_password
    global username_entry
    global password_entry
    global question,question1,question2
    username = StringVar()
    password = StringVar()
    morse_password = StringVar()
    question1 = StringVar()
    question2 = StringVar()

    Label(register_screen, text="Please enter details below",font=("impact", 25), bg="#2283a1").pack()


    username_lable = Label(register_screen, text="Username",font=("impact", 18),bg="#2283a1")
    username_lable.place(x = 250,y = 100)
    username_entry = Entry(register_screen, textvariable=username,font=("impact", 18))
    username_entry.place(x = 600,y = 100)

    password_lable = Label(register_screen, text="Password",font=("impact", 18),bg="#2283a1")
    password_lable.place(x = 250,y = 180)
    password_entry = Entry(register_screen, textvariable=password, show='*',font=("times", 18))
    password_entry.place(x = 600,y = 180)

    password_lable = Label(register_screen, text="Morse Password",font=("impact", 18),bg="#2283a1")
    password_lable.place(x = 250,y = 260)
    morse_password = Entry(register_screen, textvariable=morse_password, show='*',font=("times", 18))
    morse_password.place(x = 600,y = 260)

    question = Label(register_screen, text="Rescue Key",font=("impact", 18),bg="#2283a1")
    question.place(x = 250,y = 340)
    question1 = Entry(register_screen, textvariable=question1, show='*',font=("impact", 18))
    question1.place(x = 600,y = 340)

    question = Label(register_screen, text="Renter Rescue Key",font=("impact", 18),bg="#2283a1")
    question.place(x = 250,y = 420)
    question2 = Entry(register_screen, textvariable=question2, show='*',font=("impact", 18))
    question2.place(x = 600,y = 420)
    Button(register_screen, text="Register", width=10, height=2,font=("impact", 15), bg="#a12b56", command = register_user).place(x = 425,y = 520)



#This method is for login
def login():
    from PIL import ImageTk, Image #imports

    global login_screen,result_det

    result_det=0
    result_det=log_check() #Control goes to log_check() method [0 if successful else 1]
    login_screen = Tk()#Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1500x750")
    #login_screen.configure(background ='#295a63')
    login_screen.configure(background ='#21d6ff')
    #Label(login_screen, text="Please enter details below to login",font=("times", 25,"bold"),background="#2d2366").place(x = 150,y = 10)
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    # Calculate the center position for the elements
    center_x = login_screen.winfo_screenwidth() // 2
    entry_width = 300  # Adjust this value as needed

    Label(login_screen, text="Please enter details below to login",font=("times", 25,"bold"),background="#21d6ff").place(x = center_x - entry_width,y = 50)

    # Place the Username label and entry
    Label(login_screen, text="Username: ", font=("times", 25, "bold"), background="#295a63").place(x=center_x - entry_width, y=150)
    username_login_entry = Entry(login_screen, textvariable=username_verify, font=("times", 25, "bold"))
    username_login_entry.place(x=center_x, y=150)

    # Place the Password label and entry
    Label(login_screen, text="Password: ", font=("times", 25, "bold"), background="#295a63").place(x=center_x - entry_width, y=250)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*', font=("times", 25, "bold"))
    password_login_entry.place(x=center_x, y=250)

    # Place the LOGIN button
    Button(login_screen, 
           text="LOGIN", 
           width=6, 
           height=1, 
           command=login_verify, 
           font=("conneqt", 20, "bold")).place(x=center_x - entry_width, y=460)
    print("before entered")
    if result_det==1:
        login_screen.destroy()
    elif result_det==0:
        print("entered")



#This method checks wheather a registered user is trying to login and returns result_det
def log_check():
    import tkinter.font as font
    import cv2
    import time
    import datetime
    import csv
    from csv import DictReader
    import pandas as pd
    import time

    recognizer = cv2.face_LBPHFaceRecognizer.create() #Initialize the LBPH (Local Binary Patterns Histograms) Face Recognizer
    recognizer.read('trainer.yml') #load the trained model (trainer.yml) for face recognition

    #These lines load the Haar cascade classifier XML file for face detection.
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX #This line sets the font type for displaying text on the image
    df=pd.read_csv("UserDetails.csv") #This line reads the user details from a CSV file named "UserDetails.csv" using pandas
    cam = cv2.VideoCapture(0) #This line initializes the video capture object for accessing the webcam (index 0)
    global result_det
    result_det=0
    flag = []
    count=0
    count1=0
    count2=0
    count3=0
    sample =0
    lecture=0
    mon=0
    var1=0
    var2=0
    var=0
    t=0

    def successful(): #Defines the method for successful login
        # import tkinter.messagebox as mbox
        # mbox.showinfo("Success", "Face Authentication Success") #Shows a message box 
        root=Tk()
        root.geometry('250x150')
        root.configure(background ='#a2f59f')
        root.title("Successful")
        lbl=Label(root, text="Logged In Successfully")
        print("Login Successful1111")   
        lbl.pack()
        root.mainloop()
        

    def unsuccessful(): #Defines the method for successful login
        root=Tk()
        root.geometry('250x50')
        root.title("Unsuccessful")
        root.configure(background ='#e3684f')
        lbl=Label(root, text="Logged In UnSuccessful",bg ='#e3684f')
        print("Login unSuccessful") 
        lbl.pack()
        root.mainloop()

    while True:
        now = datetime.datetime.now() #retrieves the current date and time using the datetime.datetime.now() function and assigns it to the variable now
        ret, im =cam.read() #Returns two values: ret, which indicates whether the frame was successfully captured, and im, which contains the captured frame
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #Converts the captured frame (im) from BGR (Blue-Green-Red) color space to grayscale as they are easier to process
        faces = faceCascade.detectMultiScale(gray, 1.2,5) #Detects faces in the grayscale frame (gray) using the Haar cascade classifier (faceCascade). It returns a list of rectangles representing the bounding boxes of detected faces.
        if t==1:
            t=0
            break
        
        for(x,y,w,h) in faces: #Iterates over each detected face, represented by the coordinates (x, y, w, h) of the bounding box.
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4) #Draws a green rectangle around each detected face in the original color frame (im). The rectangle's position and size are determined by the coordinates (x-20, y-20) and (x+w+20, y+h+20), respectively
            Id,i = recognizer.predict(gray[y:y+h,x:x+w]) #It uses the LBPH face recognizer to predict the identity (Id) and confidence (i) of the detected face.gray[y:y+h, x:x+w] extracts the region of interest (ROI) corresponding to the detected face from the grayscale frame.
            print(i)#if the face is detected

            if i < 55:
                aa=df.loc[df['Id'] == Id]['name'].values
                tt=str(Id)+"-"+aa
                Id = df.loc[df['Id']== Id] ['name'].values
                var1=1
            else:
                count=count+1
                Id = "unknown"

                if count > 10:
                    count=0
                Id="unknown"
                print("unknown")
                cv2.imwrite("frame.png",im)
                print("mail Sent")
                time.sleep(5)
                mon=0
                var2=1
        
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

        cv2.imshow('im',im)
        
        if var2==1 and count > 5: #This line of code executes if an unknown person tries to login
            var2=0
            print("unsuccess")
            unsuccessful()
            t=1
            bot.sendMessage(ch_id,str("UNKNOWN DETECTED"))
            bot.sendPhoto(ch_id,photo=open("frame.png",'rb')) #A frame image of the unknown user is takes
            bot1.sendMessage(ch_id1,str("UNKNOWN DETECTED")) 
            bot1.sendPhoto(ch_id1,photo=open("frame.png",'rb')) #The frame is sent to the telegram bot
            cam.release()
            cv2.destroyAllWindows()
            result_det=1
            break

        elif var1==1: #If a registered member tries to login
            var1=0
            print("Success")
            successful()
            t=1
            cam.release()
            cv2.destroyAllWindows()
            result_det=0
            break

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return result_det #Returns 0 if a successful login else 1



# Implementing event on register button
def register_user():
    
    username_info = username.get()
    password_info = password.get()
    morse_pas = morse_password.get()
    question_info1 = question1.get()
    question_info2 = question2.get()
    if len(morse_pas)!=2:
        lbl=Label(register_screen,text="Morse Pass Want to be in 2 digit",font=("impact", 25),bg="#2283a1")
        lbl.place(x=600,y=500)
    if str(question_info1)!=str(question_info2):
        lbl=Label(register_screen,text="Rescue Key Not Match",font=("impact", 25),bg="#2283a1")
        lbl.place(x=600,y=500)
    else:
        lbl=Label(register_screen,text="Rescue Key Matched",font=("impact", 25),bg="#2283a1")
        lbl.place(x=600,y=500)
        username_info1=username_info+'.txt'
        file = open(username_info1, "w")
        #file.write(username_info + "\n")
        file.write(username_info + ",")
        file.write(password_info + ",")
        file.write(morse_pas + ",")
        file.close()
        username_info_p=username_info+'_p' + '.txt'
        file = open(username_info_p, "w")
        file.write(question_info2)
        file.close()

    

        username_entry.delete(0, END)
        password_entry.delete(0, END)
        os.system('python Register.py')
        print("Registration Success")

        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 20)).pack()

# Implementing event on login button 
def listToString(s):  
    
    # initialize an empty string 
    str1 = "" 
    
    # return string   
    return (str1.join(s))

def listToString1(s):  
    
    # initialize an empty string 
    str2 = "" 
    
    # return string   
    return (''.join(str(e) for e in list))

def Convert(string): 
    li = list(string.split("")) 
    return li     


def login_verify():
    
    global  username1,username12
    username1 = username_verify.get()
    username12=username1+'.txt'
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    global inputpassword
    global username_info1_p
    list_of_files = os.listdir()

    if username12 in list_of_files:
        file1 = open(username12, "r")
        #verify = file1.read().splitlines()
        verify = file1.read().split(',')
        check=list(verify)
        print('check {},,type {}'.format(check,type(check)))
        if password1 in verify:
            print('test {},{}'.format(password1,type(verify[1])))
            inputpassword = listToString(verify[1])
            print(inputpassword)
            print(type(inputpassword))
            global morse_pass
            morse_pass = listToString(verify[2])
            print(morse_pass)
            print(type(morse_pass))
            
            cap = cv2.VideoCapture(0)
            board = np.zeros((300, 700), np.uint8)
            board[:] = 255

            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
           # gaze()
            global frames 
            global letter_index 
            global blinking_frames
            global frames_to_blink 
            global frames_active_letter

            global text 
            global text1
            global keyboard_selected 
            global last_keyboard_selected 
            global select_keyboard_menu 
            global keyboard_selection_frames
            global count
            pf =[]

            keyboard = np.zeros((300, 600, 3), np.uint8)


            keys_set_1 = {0: "-", 1: ".",
              2: "<",3:'D'}

            def draw_letters(letter_index, text, letter_light):

                if letter_index == 0:
                    x = 0
                    y = 0
                elif letter_index == 1:
                    x = 200
                    y = 0
                elif letter_index == 2:
                    x = 400
                    y = 0
                elif letter_index == 3:
                    x = 600
                    y = 0
               
                width = 200
                height = 200
                th = 3 # thickness

                # Text settings
                font_letter = cv2.FONT_HERSHEY_PLAIN
                font_scale = 9
                font_th = 4
                text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
                width_text, height_text = text_size[0], text_size[1]
                text_x = int((width - width_text) / 2) + x
                text_y = int((height + height_text) / 2) + y

                if letter_light is True:
                    cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 255, 255), -1)
                    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (51, 51, 51), font_th)
                else:
                    cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (51, 51, 51), -1)
                    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 255, 255), font_th)

            def draw_menu():
                rows, cols, _ = keyboard.shape
                th_lines = 4 # thickness lines


            def midpoint(p1 ,p2):
                return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

            font = cv2.FONT_HERSHEY_PLAIN

            def get_blinking_ratio(eye_points, facial_landmarks):
                left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
                right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
                center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
                center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))



                hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
                ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

                ratio = hor_line_lenght / ver_line_lenght
                return ratio

            def eyes_contour_points(facial_landmarks):
                left_eye = []
                right_eye = []
                for n in range(36, 42):
                    x = facial_landmarks.part(n).x
                    y = facial_landmarks.part(n).y
                    left_eye.append([x, y])
                for n in range(42, 48):
                    x = facial_landmarks.part(n).x
                    y = facial_landmarks.part(n).y
                    right_eye.append([x, y])
                left_eye = np.array(left_eye, np.int32)
                right_eye = np.array(right_eye, np.int32)
                return left_eye, right_eye

            def get_gaze_ratio(eye_points, facial_landmarks):
                    left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                                                (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                                                (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                                                (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                                                (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                                                (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)
                    # cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)

                    height, width, _ = frame.shape
                    mask = np.zeros((height, width), np.uint8)
                    cv2.polylines(mask, [left_eye_region], True, 255, 2)
                    cv2.fillPoly(mask, [left_eye_region], 255)
                    eye = cv2.bitwise_and(gray, gray, mask=mask)

                    min_x = np.min(left_eye_region[:, 0])
                    max_x = np.max(left_eye_region[:, 0])
                    min_y = np.min(left_eye_region[:, 1])
                    max_y = np.max(left_eye_region[:, 1])

                    gray_eye = eye[min_y: max_y, min_x: max_x]
                    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
                    height, width = threshold_eye.shape
                    left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
                    left_side_white = cv2.countNonZero(left_side_threshold)

                    right_side_threshold = threshold_eye[0: height, int(width / 2): width]
                    right_side_white = cv2.countNonZero(right_side_threshold)

                    if left_side_white == 0:
                        gaze_ratio = 1
                    elif right_side_white == 0:
                        gaze_ratio = 5
                    else:
                        gaze_ratio = left_side_white / right_side_white
                    return gaze_ratio

            scanned=0
            once=1
            scanned =1
           # pf =['1','5']
            one=['.','-','-','-','-']
            two=['.','.','-','-','-']
            thrid=['.','.','.','-','-']
            four=['.','.','.','.','-']

            five=['.','.','.','.','.']
            six=['-','.','.','.','.']
            seven=['-','-','.','.','.']
            eight=['-','-','-','.','.']

            nine=['-','-','-','-','.']
            zero=['-','-','-','-','-']

            paswword =[0,0,0]
            char=[]
            while True:
                
                ret, frame = cap.read()
                rows, cols, _ = frame.shape
                keyboard[:] = (26, 26, 26)
                frames += 1
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Draw a white space for loading bar
                frame[rows - 50: rows, 0: cols] = (255, 255, 255)

                if select_keyboard_menu is True:
                    draw_menu()

                # Keyboard selected
                if keyboard_selected == "left":
                    keys_set = keys_set_1

                active_letter = keys_set[letter_index]

                # Face detection
                faces = detector(gray)
                for face in faces:
                    landmarks = predictor(gray, face)

                    left_eye, right_eye = eyes_contour_points(landmarks)

                    # Detect blinking
                    left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
                    right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
                    blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

                    # Eyes color
                    cv2.polylines(frame, [left_eye], True, (0, 0, 255), 2)
                    cv2.polylines(frame, [right_eye], True, (0, 0, 255), 2)


                    if select_keyboard_menu is True:
                        # Detecting gaze to select Left or Right keybaord
                        gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
                        gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
                        gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2
                        print(gaze_ratio)

                        if gaze_ratio <= 5:
                            keyboard_selected = "right"
                            keyboard_selection_frames += 1
                            # If Kept gaze on one side more than 15 frames, move to keyboard
                            if keyboard_selection_frames == 15:
                                select_keyboard_menu = False
            ##                    right_sound.play()
                                # Set frames count to 0 when keyboard selected
                                frames = 0
                                keyboard_selection_frames = 0
                            if keyboard_selected != last_keyboard_selected:
                                last_keyboard_selected = keyboard_selected
                                keyboard_selection_frames = 0

                    else:
                        # Detect the blinking to select the key that is lighting up
                        if blinking_ratio > 5:
                            # cv2.putText(frame, "BLINKING", (50, 150), font, 4, (255, 0, 0), thickness=3)
                            blinking_frames += 1
                            frames -= 1

                            # Show green eyes when closed
                            cv2.polylines(frame, [left_eye], True, (0, 255, 0), 2)
                            cv2.polylines(frame, [right_eye], True, (0, 255, 0), 2)

                            # Typing letter
                            if blinking_frames == frames_to_blink:
                                if active_letter != "E" and active_letter != "C":
                                    count=count+1
                                    text += active_letter
                                    text1.append(active_letter)
                                    print('text1 {}'.format(text1))
                                if active_letter == "<" or active_letter == "D" :
                                    try:
                                        text += " "
                                        count=count-1
                                        text1.pop(count)
                                        count=count-1
                                        text1.pop(count)                        
                                        print('del {}'.format(text1))
                                    except:
                                        pass
                                            
                                text += " "
                                #print("text {}".format(text))
                                
                                if len(text1) == 5 :
                                    print('Selection of Single no is completd ')
                                    print(type(str(text1)))
                                    
                                    

                                    if text1 == one:
                                        print('Selected no {}'.format(one))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('1')
                                        

                                    if text1 == two:
                                        print('Selected no {}'.format(two))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('2')

                                    if text1 == thrid:
                                        print('Selected no {}'.format(thrid))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('3')

                                    if text1 == four:
                                        print('Selected no {}'.format(four))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('4')
                                    if text1 == five:
                                        print('Selected no {}'.format(five))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('5')
                                    if text1 == six:
                                        print('Selected no {}'.format(six))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('6')

                                    if text1 == seven:
                                        print('Selected no {}'.format(seven))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('7')

                                    if text1 == eight:
                                        print('Selected no {}'.format(eight))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('8')

                                    if text1 == nine:
                                        print('Selected no {}'.format(nine))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('9')
                                    if text1 == zero:
                                        print('Selected no {}'.format(zero))
                                        text1=[]
                                        count=0
                                        once =1
                                        char.append('0')

                                    else:
                                        #print('not ,matched ')
                                        text1=[]
                                        count=0
                                        #print('Not MAtched char {}'.format(str(char)))
                                    print('paswword {}'.format(str(char)))
                                select_keyboard_menu = True
                                # time.sleep(1)

                        else:
                            blinking_frames = 0


            # Display letters on the keyboard
                if select_keyboard_menu is False:
                    if frames == frames_active_letter:
                        time.sleep(0.45)
                        letter_index += 1
                        frames = 0
                    if letter_index == 3:
                        letter_index = 0
                    for i in range(3):
                        if i == letter_index:
                            light = True
                        else:
                            light = False
                        draw_letters(i, keys_set[i], light)

                # Show the text we're writing on the board
                cv2.putText(board, str(text1), (80, 100), font, 9, 0, 3)

                # Blinking loading bar
                percentage_blinking = blinking_frames / frames_to_blink
                loading_x = int(cols * percentage_blinking)
                cv2.rectangle(frame, (0, rows - 50), (loading_x, rows), (51, 51, 51), -1)
                pwd=''
                ''
                if len(char) > 1 :
                    pwd=listToString(char)
                    print ('Got the password and i  {} ,{}'.format(pwd,morse_pass))
                    print ('Type the xhar password and i  {} ,{}'.format(type(pwd),type(morse_pass)))
                    #lis=[]
                    
                    start=0
##                    break

                    if str(pwd) == str(morse_pass) : #password
                        print('Password matches ')
                        os.system("python msg.py")
                        lis=[]
                        break
                    else:
                        
                        Label(login_screen, text="Rescue Key * ",font=("times", 25,"bold"),background="#295a63").place(x = 200,y = 350)
                        global petname_login_entry
                        petname_login_entry = Entry(login_screen, text="",font=("times", 25,"bold"))
                        petname_login_entry.place(x = 400,y = 360)
                        btn = Button(login_screen, text="Submit \n Pet Name",font=("times", 25,"bold"),command=check_pet)
                        btn.place(x = 550,y = 460)

                cv2.imshow("Frame", frame)
                cv2.imshow("Virtual keyboard", keyboard)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()

        else:
            #password_not_recognised()
            file1.close()

            center_x = login_screen.winfo_screenwidth() // 2
            entry_width = 300  # Adjust this value as needed
            Label(login_screen, text="Rescue Key: ",font=("times", 25,"bold"),background="#295a63").place(x = center_x - entry_width,y = 350)
            petname_login_entry = Entry(login_screen, text="",font=("times", 25,"bold"))
            petname_login_entry.place(x = center_x,y = 350)
            btn = Button(login_screen, text="SUBMIT \n RESCUE KEY",font=("conneqt", 18,"bold"),command=check_pet)
            btn.place(x = center_x,y = 460)
            
    else:
        user_not_found()

# Designing popup for login success
def check_pet():
    check=petname_login_entry.get()
    check=str(check)
    print(check)
    username_info1_p=username1+'_p' + '.txt'
    file = open(username_info1_p, "r")
    print(file)
    if check in file:
        os.remove(username12)
        print('Found the security question in database{}'.format(check))
        app = QApplication(sys.argv)
        ex = MouseClicksMorse()
    # print(ex.message)
        sys.exit(app.exec_())
    else:
        print('Not found in database ')
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.configure(background ='#295a63')
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    #Button(login_success_screen, text="Start", command=programs).pack()
# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.configure(background ='#295a63')
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.configure(background ='#295a63')
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def gaze():
    os.system("python gaze.py")


# Designing Main(first) window
from PIL import ImageTk, Image 

global main_screen #main_screen is declared as a global variable
  
# main_screen = Tk() #main_screen's Tk object is created
# main_screen.title("Registration Page") #Title of the main page
# img =Image.open('login-cen.jpg') #Image for the Registration screen
# screen_width = main_screen.winfo_screenwidth() #Gets the width of the current screen from the windows
# screen_height = main_screen.winfo_screenheight() #Gets the width of the current screen from the windows
# img = img.resize((screen_width, screen_height)) #Resizes the image according to the screen's size
# bg = ImageTk.PhotoImage(img) #Converts the image to Tkinter compatible format

# label = Label(main_screen, image=bg) #Creates a Tkinter label widget (Label) and associates it with the main Tkinter window (main_screen) 
# label.place(x = 0,y = 0)

# main_screen.geometry("1200x650") #Size of the main screen


main_screen = Tk()
main_screen.title("Registration Page")

# Open video file
cap = cv2.VideoCapture('start1.mp4')

# Function to update the video frame
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Resize frame to fit screen
        frame = cv2.resize(frame, (screen_width, screen_height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        label.config(image=frame)
        label.image = frame
        label.after(10, update_frame)  # Update every 10 milliseconds
    else:
        cap.release()

# Get screen width and height
screen_width = main_screen.winfo_screenwidth()
screen_height = main_screen.winfo_screenheight()
# Size and position of the video widget
label = Label(main_screen)
label.place(x=0, y=0, relwidth=1, relheight=1)
# Start updating the video frame
update_frame()
# Size of the main screen
main_screen.geometry("1200x650")

img2 =Image.open('loginbut.jpg') #Image for the button
#width, height =290, 185  #Sets the height and width of the image
width, height =270, 185
img2 = img2.resize((width, height)) #Resize the image
bt0 = ImageTk.PhotoImage(img2)
btnStart = Button( #Creates a button
    main_screen,
    image = bt0,
    height="35",
    width="150",
    relief = FLAT,
    border = 0,
    command = login, #When the button is pressed the method 'login' will be called
)
btnStart.place(x = 520,y = 280) #Sets the place for the button

img3 =Image.open('registerbut.jpg') #Image for the button
#width, height = 250, 125  #Sets the height and width of the image
width, height = 270, 205
img3 = img3.resize((width, height)) #Resize the image
bt = ImageTk.PhotoImage(img3)
btnStart1 = Button( #Creates a button
    main_screen,
    image = bt,
    height="42",
    width="170",
    relief = FLAT,
    border = 0,
    command = register, #When the button is pressed the method 'register' will be called
)
btnStart1.place(x = 510,y = 360) #Sets the place for the button

main_screen.mainloop() #Tkinter window (represented by main_screen) will be displayed, and the program will wait for user interactions.