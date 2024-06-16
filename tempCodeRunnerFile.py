main_screen = Tk() #main_screen's Tk object is created
main_screen.title("Registration Page") #Title of the main page
img =Image.open('startpage.jpg') #Image for the Registration screen
screen_width = main_screen.winfo_screenwidth() #Gets the width of the current screen from the windows
screen_height = main_screen.winfo_screenheight() #Gets the width of the current screen from the windows
img = img.resize((screen_width, screen_height)) #Resizes the image according to the screen's size
bg = ImageTk.PhotoImage(img) #Converts the image to Tkinter compatible format

label = Label(main_screen, image=bg) #Creates a Tkinter label widget (Label) and associates it with the main Tkinter window (main_screen) 
label.place(x = 0,y = 0)

main_screen.geometry("1200x650") #Size of the main screen