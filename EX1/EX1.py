import tkinter as tk
from tkinter import ttk

def sum_phone(phone_number) :
    total = 0
    for x in phone_number :
        total += int(x)
        return total

print(sum_phone('0807946386'))
#def interpret(number) :


'''
root = tk.Tk()
root.option_add('*Font','time 20')
root.title('โปรแกรมตรวจเบอร์มือถือ')
root.minsize(width=400,height=400)

ttk.Style().configure("enter.TButton", font=("Times", "10", "bold"), anchor="e")
ttk.Style().configure("cancel.TButton", font=("Times", "10", "italic"), anchor="w")

tk.Label(root,text='เบอร์มือถือมหามงคล', bg='yellow',fg='blue',font='time 20 bold').pack()
tel_number = tk.Entry(root)
tel_number.pack()

ok_button = tk.Button(root,text='ตกลง')
ok_button.pack()

root.mainloop()
'''