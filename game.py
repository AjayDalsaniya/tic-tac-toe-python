from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector


root = Tk()
root.title("Tic Tac Toe")


root.configure(bg="Cadet Blue")
root.resizable(0, 0)
root.geometry("1350x750+10+10")

buttons = StringVar()
i = True


def checker(buttons):
    global i
    if buttons['text'] == '':
        if (i):
            i = False
            buttons['text'] = 'X'
            winner()
        else:
            i = True
            buttons['text'] = 'O'
            winner()


def winner():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X'):
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        messagebox.showinfo("Game says", 'X is Winner')


    elif (btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X'):
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        messagebox.showinfo("Game says", 'X is Winner')

    elif (btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X'):
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        messagebox.showinfo("Game says", 'X is Winner')

    elif (btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X'):
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        messagebox.showinfo("Game says", 'X is Winner')

    elif (btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X'):
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        messagebox.showinfo("Game says", 'X is Winner')

    elif (btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        messagebox.showinfo("Game says", 'X is Winner')

    elif (btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X'):
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        messagebox.showinfo("Game says", 'X is Winner')

    elif (btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X'):
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        messagebox.showinfo("Game says", 'X is Winner')




    elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O'):
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        messagebox.showinfo("Game says", 'O is Winner')

    elif (btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O'):
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        messagebox.showinfo("Game says", 'O is Winner')

    elif (btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O'):
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        messagebox.showinfo("Game says", 'O is Winner')
    elif (btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O'):
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        messagebox.showinfo("Game says", 'O is Winner')
    elif (btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O'):
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        messagebox.showinfo("Game says", 'O is Winner')
    elif (btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        messagebox.showinfo("Game says", 'O is Winner')
    elif (btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O'):
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        messagebox.showinfo("Game says", 'O is Winner')
    elif (btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O'):
        n = float(playerO.get())
        score = (n + 1)
        playerO.set(score)
        messagebox.showinfo("Game says", 'O is Winner')

    elif (btn1['text'] != '' and btn2['text'] != '' and btn3['text'] != '' and btn4['text'] != ''
          and btn5['text'] != '' and btn6['text'] != '' and btn7['text'] != '' and btn8['text'] != '' and
          btn1['text'] != ''):
        messagebox.showinfo("Game Says", 'Tied Game')


def Quit():
    msg = messagebox.askquestion("Confirm", "Are you want to Quit? You still have chances!")
    if msg == 'yes':
        root.destroy()


def reset():
    btn1['text'] = ''
    btn2['text'] = ''
    btn3['text'] = ''
    btn4['text'] = ''
    btn5['text'] = ''
    btn6['text'] = ''
    btn7['text'] = ''
    btn8['text'] = ''
    btn9['text'] = ''


def NewGame():
    reset()
    playerX.set(0)
    playerO.set(0)



# frames
Tops = Frame(root, bg="Cadet Blue", pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

MainFrame = Frame(root, bg="Powder Blue", bd=10, height=600, width=1350, relief=RIDGE)
MainFrame.grid(row=1, column=0)

Leftframe = Frame(MainFrame, bg="Powder Blue", bd=10, height=490, width=730, padx=10, pady=2, relief=RIDGE)
Leftframe.pack(side=LEFT)

Rightframe = Frame(MainFrame, bg="Powder Blue", bd=10, height=490, width=750, padx=5, pady=2, relief=RIDGE)
Rightframe.pack(side=RIGHT)

Rightframe1 = Frame(Rightframe, bg="Powder Blue", bd=10, height=300, width=560, padx=35, pady=2, relief=RIDGE)
Rightframe1.grid(row=0, column=0)

Rightframe2 = Frame(Rightframe, bg="Powder Blue", bd=10, height=350, width=600, padx=0, pady=2, relief=RIDGE)
Rightframe2.grid(row=1, column=0)

Rightframe3 = Frame(Rightframe, bg="Powder Blue", bd=10, height=200, width=600,padx=145, pady=2, relief=RIDGE)
Rightframe3.grid(row=2, column=0,)

# design game
lbl=Label(root,text="TIC TAC TOE", font=('times', 35, 'bold','underline','italic'),height=2, width=20,bg='Cadet Blue',fg='white').grid(row=0,column=0)
btn1 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn1))
btn1.grid(row=0, column=0, sticky=S + N + E + W)

btn2 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn2))
btn2.grid(row=0, column=1)

btn3 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn3))
btn3.grid(row=0, column=2)

btn4 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn4))
btn4.grid(row=1, column=0)

btn5 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn5))
btn5.grid(row=1, column=1)

btn6 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn6))
btn6.grid(row=1, column=2)

btn7 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn7))
btn7.grid(row=2, column=0)

btn8 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn8))
btn8.grid(row=2, column=1)

btn9 = Button(Leftframe, text='', font=('times', 26, 'bold'), height=3, width=8, bg='white',
              command=lambda: checker(btn9))
btn9.grid(row=2, column=2)

reset_btn = Button(Rightframe2, text='Reset', font=('Georgia', 15, 'bold'), height=1, width=10, bg="Orange",fg="white", command=reset,bd=0)
reset_btn.grid(row=1, column=0,pady=10)

exitButton = Button(Rightframe2, text="Quit", font=('Georgia', 15, 'bold'), height=1, width=10, bg="white", command=Quit,bd=0,fg="Blue")
exitButton.grid(row=1, column=1,padx=20)

new_btn = Button(Rightframe2, text='NewGame', font=('Georgia', 15, 'bold'),height=1, width=10,  bg="Green",fg="white", command=NewGame,bd=0)
new_btn.grid(row=1, column=2,padx=10)


playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)




lblplayerX = Label(Rightframe1, font=('arial', 15, 'bold'), bg="Powder Blue", text="Player X:", width=8, height=3,
                   padx=2, pady=2)
lblplayerX.grid(row=0, column=0)
txtplayerX = Entry(Rightframe1, font=('arial', 20, 'bold'), bd=4, fg="Black", textvariable=playerX, width=20,
                   justify=LEFT)
txtplayerX.grid(row=0, column=1)

lblplayerO = Label(Rightframe1, font=('arial', 15, 'bold'), bg="Powder Blue", text="Player O:", width=10, height=2,
                   padx=2, pady=2)
lblplayerO.grid(row=2, column=0)
txtplayerO = Entry(Rightframe1, font=('arial', 20, 'bold'), bd=4, fg="Black", textvariable=playerO, width=20,
                   justify=LEFT)
txtplayerO.grid(row=2, column=1)

reset()

# login from design
def datalogin():
    Top = Toplevel()
    Top.title("Log In ")
    # Set the window size
    # Here 0,0 represents the starting point of the window
    Top.geometry("1280x800+0+0")
    Top.config(bg="white")

    # ============================================================================
    # ==============================DESIGN PART===================================
    # ============================================================================

    frame1 = Frame(Top, bg='red')
    frame1.place(x=0, y=0, width=450, relheight=1)

    label1 = Label(Top, text="TIC", font=("times new roman", 28, "bold"), bg="red", fg="white").place(x=100, y=300)
    label2 = Label(Top, text=" TAC ", font=("times new roman", 30, "bold"), bg="red", fg="white").place(x=162,y=300)

    label3 = Label(Top, text=" TOE", font=("times new roman", 30, "bold"), bg="red", fg="white").place(x=255,y=300)

    label4 = Label(Top, text="LOGIN...", font=("times new roman", 20, "bold"), bg="red",
                   fg="Blue").place(x=100, y=360)

    # =============Entry Field & Buttons============

    frame2 = Frame(Top, bg="gray95")
    frame2.place(x=450, y=0, relwidth=1, relheight=1)

    frame3 = Frame(frame2, bg="white",bd=10,relief=RIDGE)
    frame3.place(x=140, y=150, width=500, height=450)

    label1 = Label(frame2, text="Login", font=("times new roman", 28, "bold"), fg="red").place(x=300, y=75)

    email_label = Label(frame3, text="Email Address", font=("helvetica", 20, "bold"), bg="white", fg="gray").place(x=50,
                                                                                                                   y=40)
    email_entry = Entry(frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray",textvariable=emaillogin,bd=5,relief=RIDGE)
    email_entry.place(x=50, y=80, width=300)

    password_label = Label(frame3, text="Password", font=("helvetica", 20, "bold"), bg="white", fg="gray").place(x=50,
                                                                                                                 y=120)
    password_entry = Entry(frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray", show="*",textvariable=passwordlogin,bd=5,relief=RIDGE)
    password_entry.place(x=50, y=160, width=300)

    login_button = Button(frame3, text="Log In",command=login_func, font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="blue",
                          fg="white").place(x=50, y=250, width=300)
passwordlogin = StringVar()
emaillogin = StringVar()
def login_func():
    if emaillogin.get() == "" or passwordlogin.get() == "":
        messagebox.showerror("Error!", "All fields are required")
    else:
        try:
            connection = mysql.connector.connect(host='localhost', user='root', password='', port='3378', database='tic-tac-toe')

            cur = connection.cursor()
            cur.execute("select * from register where email=%s and password=%s",(emaillogin.get(), passwordlogin.get()))

            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error!", "Invalid USERNAME & PASSWORD")
            else:
                # connection = mysql.connector.connect(host='localhost', user='root', password='', port='3378', database='tic-tac-toe')
                # cur = connection.cursor()
                # cur.execute("select firstname, lastname from register where email=%s and password=%s",(emaillogin.get(), passwordlogin.get()))
                # frow = cur.fetchone()

                # fatch_lbl.config("Login",text=frow)



                # messagebox.showinfo("Success", "Wellcome to the PySeek family")
                # Clear all the entries



                first_name, last_name = row[1], row[2]
                full_name = f"{first_name} {last_name}"
                
                # Update the label's text with the full name
                fatch_lbl.config(text=full_name)

                messagebox.showinfo("Success", "Welcome to the PySeek family")
            connection.close()

        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}")


fname =StringVar()
lname =StringVar()
email =StringVar()
npassword =StringVar()
password =StringVar()
age =StringVar()


# registration data form
def data():
    Top = Toplevel()
    Top.geometry("1280x800+0+0")
    Top.title("Registration")

    #frame = Frame(Top, bg="white")
    #frame.place(x=100,y=50,width=500,height=550)


    frame1 = Frame(Top, bg="Blue")
    frame1.place(x=0, y=0, width=450, relheight = 1)

    frame2 = Frame(Top, bg="gray100")
    frame2.place(x=450,y=0,relwidth=1, relheight=1)

    frame3 = Frame(frame2, bg="white",relief=RIDGE,bd=10)
    frame3.place(x=140,y=150,width=500,height=450)

    label1 = Label(frame1, text="TIC", font=("helvetica", 30, "bold"), bg="Blue", fg="white").place(x=100, y=300)
    label2 = Label(frame1, text=" TAC TOE", font=("helvetica", 30, "bold"), bg="Blue", fg="white").place(x=162,y=300)
    label3 = Label(frame1, text="Register...", font=("helvetica", 20, "bold"), bg="Blue",fg="Green2").place(x=100, y=360)




    title1 = Label(frame3, text="Sign Up", font=("times new roman",25,"bold"),bg="white",fg="Blue").place(x=20, y=10)
    title2 = Label(frame3, text="Join with us", font=("times new roman",13),bg="white", fg="red").place(x=20, y=50)
    
    f_name_l = Label(frame3, text="First name", font=("helvetica",15,"bold"),bg="white",fg="Blue").place(x=20, y=100)
    l_name_l = Label(frame3, text="Last name", font=("helvetica",15,"bold"),bg="white",fg="Blue").place(x=240, y=100)

    fname_txt = Entry(frame3,font=("arial"),textvariable=fname,bd=4,fg='red',relief=RIDGE)
    fname_txt.place(x=20, y=130, width=200)

    lname_txt = Entry(frame3,font=("arial"),textvariable=lname,bd=4,fg='red',relief=RIDGE)
    lname_txt.place(x=240, y=130, width=200)

    email_l = Label(frame3, text="Email", font=("helvetica",15,"bold"),bg="white",fg="Blue").place(x=20, y=180)

    email_txt = Entry(frame3,font=("arial"),textvariable=email,bd=4,fg='red',relief=RIDGE)
    email_txt.place(x=20, y=210, width=420)

    

    

    password_l = Label(frame3, text="Password", font=("helvetica", 15, "bold"), bg="white",fg="Blue").place(x=200, y=260)

    password_txt = Entry(frame3, font=("arial"),show="*",textvariable=password,bd=4,fg='red',relief=RIDGE)
    password_txt.place(x=150, y=300, width=200)

    

    signup = Button(frame3,text="Sign Up",font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="Blue",command=registor).place(x=150,y=380,width=220)


    

# insert data store in database
def registor():
    #if fname.get()=="" or lname.get()=="" or email.get()==""  or password.get()=="" :
       #messagebox.showerror("Error!","Sorry!, All fields are required")

    if fname.get()=="":
        messagebox.showinfo("Alert", "Enter your name first")

    elif lname.get()=="":
        messagebox.showinfo("Alert", "Enter your name Last")

    elif email.get()=="":
        messagebox.showinfo("Alert", "Enter Email")

    elif password.get()=="":
        messagebox.showinfo("Alert", "Enter Password")
        
        
    else:
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="",port='3378', database="tic-tac-toe")
            cur = connection.cursor()

            cur.execute("select email from register where email=('email.get()')")

            row=cur.fetchone()


            # Check if th entered email id is already exists or not.
            if row != None:
                messagebox.showerror("Error!","The email id is already exists, please try again with another email id")
            else:
                cur.execute("insert into register (firstname,lastname,email,password) values(%s,%s,%s,%s)",
                (fname.get(),lname.get(),email.get(),password.get()))
                                
                connection.commit()
                connection.close()
                messagebox.showinfo("Congratulations!","Register Successful")
                
        except Exception as es:
            messagebox.showerror("Error!",f"Error due to{str(es)}")




btn_register = Button(Rightframe3, text="Register", font=('Georgia', 15, 'bold'),fg="Blue",bg="Powder Blue",bd=0,
                      command=data)  # button registration command through registration from(data)
btn_register.grid(row=0, column=0,pady=10)

btn_login = Button(Rightframe3, text="Login", font=('Georgia', 15, 'bold'), bg="Powder Blue",bd=0,fg="Red",
                   command=datalogin)  # button login command through login from(datalogin)
btn_login.grid(row=0, column=1,padx=20)



fatch_lbl = Label(Rightframe3,font=("Georgia",15,'bold'),bg="Powder Blue",fg='Green')
fatch_lbl.place()
fatch_lbl.grid(row=1,column=0,pady=8)




root.mainloop()


class SignUp:
    pass
