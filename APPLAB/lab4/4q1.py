from tkinter import *
import sqlite3
conn=sqlite3.connect('lab4ques1.sqlite')
curs=conn.cursor()
strng='create table Loan(annual_rate int, number_of_payments int, loan int,Monthlypayment int,remaining int)'
curs.execute(strng)
root=Tk()
root.config(bg='grey')
root.geometry("300x160")
annuallabel=Label(text="Annual Rate:",bg='grey',pady=3).grid(row=1,column=0 )
Numberofpaymentlabel=Label(text="Number of Payments:",bg='grey',pady=3).grid(row=2,column=0 )
loanlabel=Label(text="Loan Principle:",bg='grey',pady=3).grid(row=3,column=0 )
monthlylabel=Label(text="Monthly Payment:",bg='grey',pady=3).grid(row=4,column=0 )
remainingloanlabel=Label(text="Remaining Loan:",bg='grey',pady=3).grid(row=5,column=0 )
e1=Entry(root,width=25)
e1.grid(row=1,column=2, columnspan=2)
e2=Entry(root,width=25)
e2.grid(row=2,column=2, columnspan=2)
e3=Entry(root,width=25)
e3.grid(row=3,column=2, columnspan=2)
e4=Entry(root,width=25)
e4.grid(row=4,column=2, columnspan=2)
e5=Entry(root,width=25)
e5.grid(row=5,column=2, columnspan=2)
def func1():
    strng="insert into Loan values(?,?,?,?,?)"
    curs.execute(strng,(e1.get(),e2.get(),e3.get(),e4.get(),int(e3.get())-(int(e1.get())*int(e4.get()))))
    conn.commit()
def func2():
    curs.execute("update Loan SET Monthlypayment==?",(e4.get(),))
    conn.commit()
def func3():
    root.destroy()
btn1=Button(root,text="Final Balance",bg='grey',highlightbackground="black",highlightthickness=1,command=func1).grid(row=6,column=0)
btn2=Button(root,text="Monthly Payment",bg='grey',highlightbackground="black",highlightthickness=1,command=func2).grid(row=6,column=1,columnspan=2)
btn3=Button(root,text="Quit",bg='grey',highlightbackground="black",highlightthickness=1,command=func3).grid(row=6,column=3 )
root.mainloop()