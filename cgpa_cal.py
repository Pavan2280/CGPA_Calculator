import tkinter as tk
from tkinter import ttk

l_gpa=[]

def calculate():
    sum_gpa=0
    
    sub1=sub1_var.get()
    sub2=sub2_var.get()
    sub3=sub3_var.get()
    sub4=sub4_var.get()
    sub5=sub5_var.get()
    
    for i in (sub1,sub2,sub3,sub4,sub5):
        
        if i<=9:
            l_gpa.append(1)    
        elif 10<=i and i<=19:
            l_gpa.append(2)
        elif 20<=i and i<=29:
            l_gpa.append(3)
        elif 30<=i and i<=39:
            l_gpa.append(4)
        elif 40<=i and i<=49:
            l_gpa.append(5)
        elif 50<=i and i<=59:
            l_gpa.append(6)
        elif 60<=i and i<=69:
            l_gpa.append(7)
        elif 70<=i and i<=79:
            l_gpa.append(8)
        elif 80<=i and i<=89:
            l_gpa.append(9)        
        elif 90<=i and i<=100:
            l_gpa.append(10)   
        else:
            sub1_error=ttk.label(root,text='Invalid input')
            sub1_error.grid(row=0,column=2)
            sub1_error.configure(foreground='Red')

    for j in l_gpa:
        sum_gpa+=j
        final_cgpa=sum_gpa/5
        
    cgpa.set(final_cgpa)
    cgpa_display=ttk.Entry(root,width=10, textvariable=cgpa, state='disabled')
    
    cgpa_display.grid(row=7,column=4)
    
root = tk.Tk()
cgpa=tk.IntVar()
root.title('GPA CALCULATOR')

sub1 = ttk.Label(root,text='Enter marks of 1st sub:')
sub1.grid(row=0,column=0)
sub1.config(font=('Courier',12))

sub2 = ttk.Label(root,text='Enter marks of 2nd sub:')
sub2.grid(row=1,column=0)
sub2.config(font=('Courier',12))

sub3 = ttk.Label(root,text='Enter marks of 3rd sub:')
sub3.grid(row=2,column=0)
sub3.config(font=('Courier',12))

sub4 = ttk.Label(root,text='Enter marks of 4th sub:')
sub4.grid(row=3,column=0)
sub4.config(font=('Courier',12))

sub5 = ttk.Label(root,text='Enter marks of 5th sub:')
sub5.grid(row=4,column=0)
sub5.config(font=('Courier',12))

sub1_var=tk.IntVar()
sub1_var_entry=ttk.Entry(root,width=10,textvariable=sub1_var)
sub1_var_entry.grid(row=0,column=1)

sub2_var=tk.IntVar()
sub2_var_entry=ttk.Entry(root,width=10,textvariable=sub2_var)
sub2_var_entry.grid(row=1,column=1)

sub3_var=tk.IntVar()
sub3_var_entry=ttk.Entry(root,width=10,textvariable=sub3_var)
sub3_var_entry.grid(row=2,column=1)

sub4_var=tk.IntVar()
sub4_var_entry=ttk.Entry(root,width=10,textvariable=sub4_var)
sub4_var_entry.grid(row=3,column=1)

sub5_var=tk.IntVar()
sub5_var_entry=ttk.Entry(root,width=10,textvariable=sub5_var)
sub5_var_entry.grid(row=4,column=1)

calc=ttk.Button(root,text='Calculate',command=calculate)
calc.grid(row=7,column=0)

quit=ttk.Button(root,text='Quit',command=root.destroy)
quit.grid(row=8,column=0)

root.mainloop()
