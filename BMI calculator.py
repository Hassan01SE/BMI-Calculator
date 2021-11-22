from tkinter import *
from tkinter import messagebox

#program outlook
m=Tk()
m.geometry("1000x670")
m.maxsize(1000,900)
m.minsize(500,300)
m.title("Body Mass Index calculator by Hassan Sohail")

#functions
def measure():
    a=float(e4.get())
    b=float(e5.get())
    if a==0 or b==0:
        messagebox.showerror("Error","Invalid Entry!")

    c=a/100
    d=c*c
    y=b/d
    healthyweight=25*d
    bmi.config(text="Your BMI is: " + str(y),font=('aeriel', 20, 'bold'))
    if y > 25:
        Remark.config(text="You're overweight ;(",font=('aeriel', 20, 'bold'),bg="red",fg="black")
        messagebox.showinfo("Lose weight to: ",healthyweight)
    elif y < 18.5:
        Remark.config(text="You're underweight :(", font=('aeriel', 20, 'bold'),bg="yellow")
        messagebox.showinfo("Gain weight up to: ", healthyweight)
    else:
        Remark.config(text="You're healthy :D", font=('aeriel', 20, 'bold'),bg="green",fg="black")



def cal():
    p=float(e1.get())
    q=float(e2.get())
    weight=float(e3.get())
    if p==0 or weight==0:
        messagebox.showerror("ERROR","Invalid entry!")
    r=p*12
    s=r+q
    t=s*0.0254
    u=t*t
    x=weight/u
    healthyweight=25*u
    bmi.config(text="Your BMI is: " + str(x), font=('aeriel', 20, 'bold'))
    if x > 25:
        Remark.config(text="You're overweight ;(",font=('aeriel', 20, 'bold'),bg="red",fg="black")
        messagebox.showinfo("Lose weight to: ", healthyweight)
    elif x < 18.5:
        Remark.config(text="You're underweight :(", font=('aeriel', 20, 'bold'),bg="yellow")
        messagebox.showinfo("Gain weight to: ", healthyweight)
    else:
        Remark.config(text="You're healthy :D", font=('aeriel', 20, 'bold'),bg="green",fg="black")






f1=Frame(m,bg='dark grey')
f1.place(width=1000,height=50)
l1=Label(f1,text="Body Mass Index Calculator", font=('Times New Roman', 34),fg='maroon',bg='dark grey')
l1.pack(fill=X)

f2=Frame(m)
f2.place(x=90,y=75, width=310, height=75)
f3=Frame(m)
f3.place(x=650,y=75,width=310,height=75)

l2=Label(f2, text="Standard", font=("cambria", 25, "bold"),bg="purple",borderwidth=15,relief=RAISED,width=30).pack(pady=5,side=TOP)
l3=Label(f3, text="Metric", font=("cambria", 25, "bold"),bg="purple",borderwidth=15,relief=RAISED,width=30).pack(padx=5,side=TOP)

f4=Frame(m)
f4.place(x=60,y=145,width=510,height=375)
f5=Frame(m)
f5.place(x=650,y=145,width=510,height=375)

height=Label(f4,text="Your Height:",font=(12))
height.grid(pady=10,row=0,column=0)

e1=Entry(f4)
e1.grid(pady=10,row=0,column=1)
e2=Entry(f4)
e2.grid(padx=3,pady=10,row=0,column=2)

feet=Label(f4,text="(Feet)").grid(row=1,column=1)
inch=Label(f4,text="(Inches)").grid(padx=3,row=1,column=2)

w1=Label(f4,text="Your Weight:",font=12).grid(pady=10,row=2,column=0)
e3=Entry(f4)
e3.grid(row=2,column=1)
kg=Label(f4,text="(Kilogram)").grid(row=3,column=1)

button=Button(f4,text="Compute BMI",font=(20),borderwidth=10,relief=SUNKEN,width=13,bg="silver",activeforeground="red",command=cal).grid(pady=30,row=4,column=1)
button1=Button(f5,text="Compute BMI",font=(20),borderwidth=10,relief=SUNKEN,width=13,bg="silver",activeforeground="red",command=measure).grid(pady=40,row=4,column=1)

#for Metric
h1=Label(f5,text="Your Height:",font=12).grid(pady=10,row=0,column=0)
e4=Entry(f5)
e4.grid(row=0,column=1)
centi=Label(f5,text="(Centimeters)").grid(row=1,column=1)
w2=Label(f5,text="Your Weight:",font=12).grid(row=2,column=0)
e5=Entry(f5)
e5.grid(row=2,column=1)
kkg=Label(f5,text=("(Kilogram)")).grid(row=3,column=1)


f10=Frame(m)
f10.place(x=250,y=360, width=560,height=500)

bmi=Label(f10,height=2,width=560,text="Your BMI is:",font=('aeriel', 35, 'bold'),borderwidth=15,relief=SUNKEN,fg="brown",bg="white")
bmi.pack()
Remark=Label(f10,height=2,width=560,text="Remarks",font=('aeriel', 25, 'bold'),borderwidth=15,relief=SUNKEN,fg="brown",bg="white")
Remark.pack(pady=5)


m.mainloop()
