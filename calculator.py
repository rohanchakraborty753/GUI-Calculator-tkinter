from tkinter import *

flag = True

root = Tk()
root.title("Calculator App")
root.geometry("285x340")
root.resizable(False, False)
root.iconbitmap("calc.ico")
root.configure(background="#f7a707")

font1 = "{Arial} 15 bold"

def Calc(event):
    global flag
    if flag == False:
        allCLear()
        flag = True
    global numEvent
    numEvent = event.widget
    text = numEvent['text']
    
    if text == "x":
        calcScreen.insert(INSERT,"*")
        return
        
    calcScreen.insert(INSERT, text)
           

def evaluate():
    global flag
    expression = calcScreen.get()
    try:
        result = eval(expression)
        if result == float(result):
            result = round(result, 3)
        calcScreen.delete(0, END)
        calcScreen.insert(INSERT,result)
        flag = False  
    except:
       calcScreen.delete(0, END)
       calcScreen.insert(INSERT,"Error!")
       flag = False     

def allCLear():
    calcScreen.delete(0, END)

def clear():
    expression= calcScreen.get()
    expression = expression[0:len(expression)-1]
    calcScreen.delete(0, END)
    calcScreen.insert(INSERT,expression)

calcScreen = Entry(root, width = 19, font="{Arial} 25 bold", justify=RIGHT, borderwidth=0, border=1, bg= "black", fg= "white")
calcScreen.grid(row=0, column=0, columnspan=5, pady= 10, padx=4)


num = 1
for i in range(1,4):
    for j in range(0,3):
        btn = Button(root, text=num, width=3, height=2, bg= "orange", fg= "green", font=font1)
        btn.grid(row=i, column=j, pady=5,padx=4, sticky="w")
        num += 1
        btn.bind("<Button-1>", Calc)

btn1 = Button(root, text="+", width=3, height=2, bg= "grey", fg= "green", font=font1)
btn1.grid(row=1, column=3, pady=5,padx=4, sticky="w")
btn1.bind("<Button-1>", Calc)

btn2 = Button(root, text="-", width=3, height=2, bg= "grey", fg= "green", font=font1)
btn2.grid(row=2, column=3, pady=5,padx=4, sticky="w")
btn2.bind("<Button-1>", Calc)

btn3 = Button(root, text="x", width=3, height=2, bg= "grey", fg= "green", font=font1)
btn3.grid(row=3, column=3, pady=5,padx=4, sticky="w")
btn3.bind("<Button-1>", Calc)

btn5 = Button(root, text="0", width=3, height=2, bg= "grey", fg= "green", font=font1)
btn5.grid(row=4, column=1, pady=5,padx=4, sticky="w")
btn5.bind("<Button-1>", Calc)

btn4 = Button(root, text="AC", width=3, height=2, command=allCLear, bg= "grey", fg= "green", font=font1)
btn4.grid(row=5, column=0, pady=5,padx=4, sticky="w")

btn9 = Button(root, text="C", width=3, height=2, command=clear, bg= "grey", fg= "green", font=font1)
btn9.grid(row=4, column=0, pady=5,padx=4, sticky="w")

btn6 = Button(root, text=".", width=3, height=2, bg= "grey", fg= "green", font=font1)
btn6.grid(row=4, column=2, pady=5,padx=4, sticky="w")
btn6.bind("<Button-1>", Calc)

btn7 = Button(root, text="/", width=3, height=2, bg= "grey", fg= "green", font=font1)
btn7.grid(row=4, column=3, pady=5,padx=4, sticky="w")
btn7.bind("<Button-1>", Calc)

btn8 = Button(root, text="=", width=19, height=2,borderwidth=0,border=1, command=evaluate, bg= "grey", fg= "green", font=font1)
btn8.grid(row=5, column= 1, columnspan=3, pady=5,padx=4, sticky="w")


root.mainloop()