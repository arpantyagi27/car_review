import tkinter as t
#root =t.Tk()
l=t.Label(None,text="Grade")
l1=t.Label(None,text="M1")
l2=t.Label(None,text="M2")

e1=t.Entry(None)
e2=t.Entry(None)
def calc():
    s=(int(e1.get())+int(e2.get()))/2
    l.config(text=str(s))
b=t.Button(None,text="Grade", command=calc)
l.grid(row=5,column=7)
l1.grid(row=10,column=5)
l2.grid(row=15,column=5)
e1.grid(row=10,column=7)
e2.grid(row=15,column=7)
b.grid(row=20,column=7)
t.mainloop()