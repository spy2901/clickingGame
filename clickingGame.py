import tkinter as tk

win = tk.Tk()

win.title('Clicking Game')
win.configure(background="#cc7f47")
win.geometry("500x500")

max_amount = 0
label1 = None #just so it is defined

def fun():
    global max_amount, label1
    max_amount +=1
    label1.configure(text='Cookies:' + str(max_amount))

btn = tk.Button(win,text = 'Change', command = fun,fg='black', font=("Helvetica", 20),bg="#cc7f47")
btn.place(x=200,y=240)

t1 =str(max_amount)
label1 = tk.Label(win,text = 'Balance:' + t1,fg='Black', font=("Helvetica", 30),bg="#cc7f47")
label1.place(x=170,y=150)

win.mainloop()
print("radi")
