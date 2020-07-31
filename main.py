import time
from random import randint
import turtle as t
from turtle import Turtle
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox


objects = []
window = Tk()
window.withdraw()
window.title('Account Manager')


class PopupWindow1(object):
    loop = False
    attempts = 0

    def __init__(self, master):
        opt = self.opt = Toplevel(master)
        opt.title('Modus auswählen')
        opt.geometry('{}x{}'.format(500, 350))
        opt.resizable(width=True, height=True)
        self.l1 = Label(opt, text="Wähle Modul", font=('new times roman', 20), justify=CENTER)
        self.l1.pack()
        self.b1 = Button(opt, text='ACCSaver', command=self.clean1, font=('new times roman', 14))
        self.b1.pack()
        self.b2 = Button(opt, text='TEST', command=self.clean2, font=('new times roman', 14))
        self.b2.pack()
        self.b3 = Button(opt, text='Turtles', command=self.clean3, font=('new times roman', 14))
        self.b3.pack()

    def clean1(self):
        self.loop = True
        PopupWindow(window)
        self.opt.destroy()

    def clean2(self):
        self.loop = True
        Window2(window)
        self.opt.destroy()

    def clean3(self):
        self.loop = TRUE
        Window1(window)
        self.opt.destroy()


class Window1(object):
    loop = False
    attempts = 0

    def __init__(self, master):
        pot2 = self.pot2 = Toplevel(master)
        pot2.title('ZIPencoder')
        pot2.geometry('{}x{}'.format(500, 350))
        pot2.resizable(width=True, height=True)
        self.l2 = Label(pot2, text='Was sollen die Turtles malen', font=('new times roman', 14), justify=CENTER)
        self.l2.pack()
        self.b4 = Button(pot2, text='COLOR BALL', command=self.turtleball, font=('new times roman', 14))
        self.b4.pack()
        self.b5 = Button(pot2, text='COLOR Spirograph', command=self.turtle2, font=('new times roman', 14))
        self.b5.pack()
        self.b6 = Button(pot2, text='3D Spirale' ,command=self.turtle3, font=('new times roman', 14))
        self.b6.pack()
        self.b7 = Button(pot2, text='Turtle Race', command=self.turtle4, font=('new times roman', 14))
        self.b7.pack()
        self.b8 = Button(pot2, text='CLEAR', command=self.clear, font=('new times roman', 14))
        self.b8.pack()

    def turtleball(self):
        self.loop = True
        t.bgcolor('black')
        t.pensize(2)
        t.speed(0)
        t.hideturtle()
        for i in range(6):
            for colours in ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']:
                t.color(colours)
                t.circle(100)
                t.left(10)

    def turtle2(self):
        t.speed(0)
        t.bgcolor('black')
        t.hideturtle()
        for i in range(5):
            for colours in ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']:
                t.color(colours)
                t.pensize(3)
                t.left(12)
                t.forward(200)
                t.left(90)
                t.forward(200)
                t.left(90)
                t.forward(200)
                t.left(90)
                t.forward(200)
                t.left(90)

    def turtle3(self):
        twindow = t.Screen()
        twindow.title('3D Spirale')
        t.shape('turtle')
        t.bgcolor('black')
        x=1
        t.speed(0)
        while x<500:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            t.colormode(255)
            t.color(r, g, b)
            t.forward(5+x)
            t.right(90.99)
            x=x+1

    def turtle4(self):
        window2 = t.Screen()
        window2.title('Turtle Race')
        t.bgcolor('forestgreen')
        t.color('white')
        t.speed(0)
        t.penup()
        t.setpos(-110, 200)
        t.write('Turtle Race', font=('Arial', 30, 'bold'))
        t.penup()
        t.setpos(-400, -180)
        t.color('chocolate')
        t.begin_fill()
        t.pendown()
        t.forward(800)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(800)
        t.right(90)
        t.forward(200)
        t.end_fill()
        stamp_size = 20
        square_size = 15
        finish_line = 200
        t.color('black')
        t.shape('square')
        t.shapesize(square_size / stamp_size)
        t.penup()
        for i in range(10):
            t.setpos(finish_line, (150 - (i * square_size * 2)))
            t.stamp()
        for j in range(10):
            t.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
            t.stamp()
        t.hideturtle()
        turtle1 = Turtle()
        turtle1.speed(0)
        turtle1.color('red')
        turtle1.shape('turtle')
        turtle1.penup()
        turtle1.goto(-250, 100)
        turtle1.pendown()
        turtle2 = Turtle()
        turtle2.speed(0)
        turtle2.color('blue')
        turtle2.shape('turtle')
        turtle2.penup()
        turtle2.goto(-250, 50)
        turtle2.pendown()
        turtle3 = Turtle()
        turtle3.speed(0)
        turtle3.color('yellow')
        turtle3.shape('turtle')
        turtle3.penup()
        turtle3.goto(-250, 0)
        turtle3.pendown()
        turtle4 = Turtle()
        turtle4.speed(0)
        turtle4.color('cyan')
        turtle4.shape('turtle')
        turtle4.penup()
        turtle4.goto(-250, -50)
        turtle4.pendown()
        time.sleep(3)
        for i in range(145):
            turtle1.forward(randint(1, 5))
            turtle2.forward(randint(1, 5))
            turtle3.forward(randint(1, 5))
            turtle4.forward(randint(1, 5))
        t.exitonclick()

    def clear(self):
        print('HELLO')

class Window2(object):
    loop = False
    attempts = 0

    def __init__(self, master):
        pot = self.pot = Toplevel(master)
        pot.title('TEST')
        pot.geometry('{}x{}'.format(500, 350))
        pot.resizable(width=True, height=True)
        self.m = Label(pot, text='Hier könnte deine Idee sein', font=('new times roman', 14), justify=CENTER)
        self.m.pack()
        self.e1 = Entry(pot, width=20)
        self.e1.pack(pady=7)
        self.n1 = Button(pot, text='Starten', font=('new times roman', 14))
        self.n1.pack()


class PopupWindow(object):
    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Master Passwort eingeben')
        top.geometry('{}x{}'.format(500, 350))
        top.resizable(width=False, height=False)
        self.y = Label(top, text="Master Passwort: ", font=('new times roman', 14), justify=CENTER)
        self.y.pack()
        self.e = Entry(top, show='*', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='OK', command=self.cleanup, font=('Courier', 14))
        self.b.pack()

    def cleanup(self):
        # noinspection PyAttributeOutsideInit
        self.value = self.e.get()
        access = 'enrico'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.e.delete(0, 'end')
            messagebox.showerror('Falsches Passwort',
                                 'Falsches Passwort, Verbleibene Versuche: {0}'.format(str(4 - self.attempts)))


class EntityAdd:
    def __init__(self, master, n, u, e, p):
        self.name = n
        self.username = u
        self.email = e
        self.password = p
        self.window = master

    def write(self):
        f = open('emails.txt', "a")
        n = self.name
        u = self.username
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedU = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in u:
            if letter == ' ':
                encryptedU += ' '
            else:
                encryptedU += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedU + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()


class EntityDisplay:

    def __init__(self, master, n, u, e, p, i):
        self.name = n
        self.username = u
        self.email = e
        self.password = p
        self.window = master
        self.i = i

        dencryptedN = ""
        dencryptedU = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.username:
            if letter == ' ':
                dencryptedU += ' '
            else:
                dencryptedU += chr(ord(letter) - 5)

        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.label_name = Label(self.window, text=dencryptedN, font=('Courier', 14))
        self.label_username = Label(self.window, text=dencryptedU, font=('Courier', 14))
        self.label_email = Label(self.window, text=dencryptedE, font=('Courier', 14))
        self.label_pass = Label(self.window, text=dencryptedP, font=('Courier', 14))
        self.deleteButton = Button(self.window, text='X', fg='red', command=self.delete)

    def display(self):
        self.label_name.grid(row=7 + self.i, sticky=W)
        self.label_username.grid(row=7 + self.i, column=1)
        self.label_email.grid(row=7 + self.i, column=2)
        self.label_pass.grid(row=7 + self.i, column=3, sticky=E)
        self.deleteButton.grid(row=7 + self.i, column=4, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Löschen',
                                                'Bist du dir Sicher, den Account aus der Liste zu nehmen?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_username.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()


def onsubmit():
    p = password.get()
    g = email.get()
    u = username.get()
    n = name.get()
    e = EntityAdd(window, n, u, g, p)
    e.write()
    name.delete(0, 'end')
    username.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('OK', 'Erfolgreich Hinzugefügt, \n' + 'Name: ' + n + '\nBenutzername: ' + u +
                        '\nEmail: ' + g + '\nPasswort: ' + p)
    readfile()


def clearfile():
    f = open('emails.txt', "w")
    f.close()


def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = EntityDisplay(window, entityList[0], entityList[1], entityList[2], entityList[3], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()


c = PopupWindow1(window)

entity_label = Label(window, text='Account Daten eingeben', font=('Courier', 18))
name_label = Label(window, text='Plattform/Webseite: ', font=('Courier', 14))
username_label = Label(window, text='Benutzername: ', font=('Courier', 14))
email_label = Label(window, text='Email: ', font=('Courier', 14))
pass_label = Label(window, text='Passwort: ', font=('Courier', 14))
name = Entry(window, font=('Courier', 14))
username = Entry(window, font=('Courier', 14))
email = Entry(window, font=('Courier', 14))
password = Entry(window, show='*', font=('Courier', 14))
submit = Button(window, fg='black', bg='green', text='Hinzufügen', command=onsubmit, font=('Courier', 14))

entity_label.grid(columnspan=4, row=0)
name_label.grid(row=1, sticky=E, padx=3)
username_label.grid(row=2, sticky=E, padx=3)
email_label.grid(row=3, sticky=E, padx=3)
pass_label.grid(row=4, sticky=E, padx=3)

name.grid(columnspan=4, row=1, column=1, padx=2, pady=2, sticky=W)
username.grid(columnspan=4, row=2, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=4, row=3, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=4, row=4, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=4, pady=4)

name_label2 = Label(window, text='Plattform/Webseite: ', font=('Courier', 14))
username_label2 = Label(window, text='Benutzername: ', font=('Courier', 14))
email_label2 = Label(window, text='Email: ', font=('Courier', 14))
pass_label2 = Label(window, text='Passwort: ', font=('Courier', 14))

name_label2.grid(row=6)
username_label2.grid(row=6, column=1)
email_label2.grid(row=6, column=2)
pass_label2.grid(row=6, column=3)


readfile()

window.mainloop()
