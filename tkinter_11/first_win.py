from tkinter import *
win = Tk()
win.title('Login System')
win.geometry('500x500')
win.resizable(False, False)
win.config(background='#D5DBDB')
win.iconbitmap('C:\\imgs\\LoginPeople-150x150.png')
# ---- title : العنوان -------
title = Label(win, text='Login System', font=('Courier', 15), bg='black', fg='white')
title.pack(fill = X)

# ---- frame -----
fr1 = Frame(win, width='300', height='350', bg = 'whitesmoke')
fr1.pack(pady=30)

#-----image صورة -----
photo = PhotoImage(file='C:\\imgs\\logo22.png',
                    width=250, height=150)
panel = Label(win, image = photo)
panel.place(x = 120, y = 30)
# --------------------- label -------------------------
lbl = Label(fr1, text = 'User Name ', font = ('Courier', 15), bg = 'whitesmoke')
lb2 = Label(fr1, text = 'Password ', font = ('Courier', 15), bg = 'whitesmoke')
lbl.place(x = 10, y = 140)
lb2.place(x = 10, y = 180)
# ---- Entry Fields -----
en1 = Entry(fr1)
en1.place(x = 134, y = 145)

en1 = Entry(fr1)
en1.place(x = 134, y = 185)

# ----- Button ------

# ----- Button ------
bt1 = Button(fr1, text = 'Login', font = ('Courier', 15), bg='#76D7C4', width = '12')
bt1.place(x = 15, y = 260)
bt2 = Button(fr1, text = 'Signin', font = ('Courier', 15), bg='#CD6155', width = '11')
bt2.place(x = 150, y = 260)


# ---- checkbox ----
c1 = Checkbutton(fr1, text = 'Forget Password !', font = ('Courier', 15), bg = 'whitesmoke')
c1.place(x=40, y=220)
pw = Label(fr1, text='Developed by Yahia Momtaz@2023', font = ('Courier',9), bg='whitesmoke')
pw.place(x=40, y=330)
win.mainloop()