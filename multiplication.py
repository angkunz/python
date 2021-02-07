import tkinter as tk

def show_output() :
    number = int(student_number.get())
    number2 = int(student_point.get())
    
    output = ''
    for x in range(1,number2+1) :
        output += str(number) + ' x ' + str(x) + " = " + str(number*x) + "\n"

    output_labal.configure(text=output)



window = tk.Tk()
window.option_add("*Font", "time 24 bold")
window.title('โปรแกรมสูตรคูณ')
window.minsize(width=400,height=400)

title_label = tk.Label(master=window, text="โปรแกรมสูตรคูณ",bg="deep sky blue")
title_label.pack()

student_label = tk.Label(master=window, text="กรุณากรอกแม่สตรคูณ",pady=10)
student_label.pack()

student_number = tk.Entry(master=window,)
student_number.pack()

point_label = tk.Label(master=window, text="กรุณากรอกจำนวนครั้งที่จะคูณ",pady=10)
point_label.pack()

student_point = tk.Entry(master=window)
student_point.pack()

go_button = tk.Button(master=window, text='ตกลง', width=5,height=1,bd=5,command=show_output)
go_button.pack()

output_labal = tk.Label(master=window,font='time 15')
output_labal.pack()



window.mainloop()
