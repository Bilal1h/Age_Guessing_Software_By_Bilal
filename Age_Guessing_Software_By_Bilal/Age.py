from tkinter import * 
import tkinter.messagebox as tmsg
import subprocess
from tkinter import ttk

root = Tk()
root.state("zoomed")
root.wm_iconbitmap("1.ico")
root.title('Age Calculator')
def exits():
    root.destroy()
def play():
    global ans
    calculator = tmsg.askyesno("Calculator","Do You Want A Calculator To Perform These Calculations")
    if calculator:
        subprocess.Popen('C:\Windows\system32\calc.exe')
    else:
        pass
    ans = tmsg.askokcancel("Step 1","First Multiply the First Digit OF your Age by 5 ")
    if ans:
       pass
    else:
         tmsg.askokcancel("Step 1","Try Again | Multiply the First Digit OF your Age by 5 ")
    ans1 = tmsg.askokcancel("Step 2","Then Add 4 to your Answer ")
    if ans1:
       pass
    else:
         ans1 = tmsg.askokcancel("Step 2","Try Again | Then Add 4 to your Answer ")
    ans2 = tmsg.askokcancel("Step 3","Then Multiply Your Answer by 2")
    if ans2:
       pass
    else:
         ans2 = tmsg.askokcancel("Step 3","Try Again | Multiply Your Answer by 2")
    ans3 = tmsg.askokcancel("Step 4","Then Add The Second Digit Of Your Age To The Answer")
    if ans3:
       pass
    else:
         ans3 = tmsg.askokcancel("Step 4","Try Again | Add The Second Digit Of Your Age To The Answer")
    Label(root,text="Enter The Final Answer You Get : ",font="lucida 20").pack()
    ans = Entry(root,font="Nexa 20 bold")
    ans.pack()
    def finalans():
        age = int(ans.get())
        if age > 100:
            tmsg.showinfo("Error","Please Enter A Valid Answer")
            
        else:
            ageans = age-8
            f = tmsg.askyesno("Age",f"Your Age Is : {ageans}")
        if f:
            pass
        else:
            tmsg.showinfo("Error Handling","Check that You Had Done Every Step Carefully")
    
        

    
    Button(root,text="Check Answer",command=finalans,font="Nexa 20 bold").pack()
    
Label(text="Age Calculator",font="Roboto 60 bold").pack()


Button(text="Play",font="Nexa 30 bold",command=play).pack(pady=50)
Button(text="Exit",font="Nexa 30 bold",command=exits).pack()





root.mainloop()


