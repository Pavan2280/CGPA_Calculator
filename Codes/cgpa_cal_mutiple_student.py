import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

class GPA_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('GPA CALCULATOR')
        
        self.student_index = 0  # Keep track of the current student
        self.students = []  # List to store student data
        
        self.create_student_frame()
        
        self.quit_button = ttk.Button(self.root, text='Quit', command=self.root.destroy)
        self.quit_button.grid(row=7, column=0, pady=10)
        
        self.next_button = ttk.Button(self.root, text='Next', command=self.next_student)
        self.next_button.grid(row=7, column=1, pady=10)
        self.next_button.configure(state='disabled')
        
        self.plot_button = ttk.Button(self.root, text='Plot Graph', command=self.plot_graph)
        self.plot_button.grid(row=7, column=2, pady=10)
        self.plot_button.configure(state='disabled')

    def create_student_frame(self):
        if self.student_index < 5:
            student_frame = ttk.LabelFrame(self.root, text=f'Student {len(self.students) + 1}')
            student_frame.grid(row=0, column=0, padx=10, pady=10)
            
            sub1_label = ttk.Label(student_frame, text='Enter marks of 1st sub:')
            sub1_label.grid(row=0, column=0)
            sub1_label.config(font=('Courier', 12))

            sub2_label = ttk.Label(student_frame, text='Enter marks of 2nd sub:')
            sub2_label.grid(row=1, column=0)
            sub2_label.config(font=('Courier', 12))

            sub3_label = ttk.Label(student_frame, text='Enter marks of 3rd sub:')
            sub3_label.grid(row=2, column=0)
            sub3_label.config(font=('Courier', 12))

            sub4_label = ttk.Label(student_frame, text='Enter marks of 4th sub:')
            sub4_label.grid(row=3, column=0)
            sub4_label.config(font=('Courier', 12))

            sub5_label = ttk.Label(student_frame, text='Enter marks of 5th sub:')
            sub5_label.grid(row=4, column=0)
            sub5_label.config(font=('Courier', 12))

            self.sub1_var = tk.IntVar()
            sub1_var_entry = ttk.Entry(student_frame, width=10, textvariable=self.sub1_var)
            sub1_var_entry.grid(row=0, column=1)

            self.sub2_var = tk.IntVar()
            sub2_var_entry = ttk.Entry(student_frame, width=10, textvariable=self.sub2_var)
            sub2_var_entry.grid(row=1, column=1)

            self.sub3_var = tk.IntVar()
            sub3_var_entry = ttk.Entry(student_frame, width=10, textvariable=self.sub3_var)
            sub3_var_entry.grid(row=2, column=1)

            self.sub4_var = tk.IntVar()
            sub4_var_entry = ttk.Entry(student_frame, width=10, textvariable=self.sub4_var)
            sub4_var_entry.grid(row=3, column=1)

            self.sub5_var = tk.IntVar()
            sub5_var_entry = ttk.Entry(student_frame, width=10, textvariable=self.sub5_var)
            sub5_var_entry.grid(row=4, column=1)

            calc_button = ttk.Button(student_frame, text='Calculate', command=self.calculate)
            calc_button.grid(row=5, column=0, columnspan=2)
            
            cgpa_display = ttk.Entry(student_frame, width=10, state='readonly')
            cgpa_display.grid(row=6, column=0, columnspan=2)
            
            self.students.append({
                'sub1_var': self.sub1_var,
                'sub2_var': self.sub2_var,
                'sub3_var': self.sub3_var,
                'sub4_var': self.sub4_var,
                'sub5_var': self.sub5_var,
                'cgpa_display': cgpa_display,
                'calc_button': calc_button
            })

    def calculate(self):
        student_data = self.students[self.student_index]
        
        sub1 = student_data['sub1_var'].get()
        sub2 = student_data['sub2_var'].get()
        sub3 = student_data['sub3_var'].get()
        sub4 = student_data['sub4_var'].get()
        sub5 = student_data['sub5_var'].get()

        l_gpa = []

        for i in (sub1, sub2, sub3, sub4, sub5):
            if i <= 9:
                l_gpa.append(1)
            elif 10 <= i and i <= 19:
                l_gpa.append(2)
            elif 20 <= i and i <= 29:
                l_gpa.append(3)
            elif 30 <= i and i <= 39:
                l_gpa.append(4)
            elif 40 <= i and i <= 49:
                l_gpa.append(5)
            elif 50 <= i and i <= 59:
                l_gpa.append(6)
            elif 60 <= i and i <= 69:
                l_gpa.append(7)
            elif 70 <= i and i <= 79:
                l_gpa.append(8)
            elif 80 <= i and i <= 89:
                l_gpa.append(9)
            elif 90 <= i and i <= 100:
                l_gpa.append(10)
            else:
                sub1_error = ttk.Label(self.root, text='Invalid input')
                sub1_error.grid(row=0, column=2)
                sub1_error.configure(foreground='Red')

        sum_gpa = sum(l_gpa)
        final_cgpa = sum_gpa / 5

        cgpa_display = student_data['cgpa_display']
        cgpa_display.configure(state='normal')
        cgpa_display.delete(0, tk.END)
        cgpa_display.insert(0, final_cgpa)
        cgpa_display.configure(state='readonly')

        student_data['calc_button'].configure(state='disabled')  # Disable Calculate button for this student
        self.next_button.configure(state='normal')  # Enable Next button
        self.plot_button.configure(state='disabled')  # Disable Plot Graph button

    def next_student(self):
        self.student_index += 1
        if self.student_index < 5:
            self.create_student_frame()
            self.next_button.configure(state='disabled')
            self.plot_button.configure(state='disabled')  # Disable Plot Graph button
        else:
            self.quit_button.configure(state='normal')
            self.next_button.configure(state='disabled')
            self.plot_button.configure(state='normal')  # Enable Plot Graph button for plotting

    def plot_graph(self):
        # Get the CGPA values for all students
        cgpa_values = [float(student['cgpa_display'].get()) for student in self.students]

        # Create a bar graph
        plt.bar(range(1, len(cgpa_values) + 1), cgpa_values)
        plt.xlabel('Student')
        plt.ylabel('CGPA')
        plt.title('CGPA Distribution')

        # Show the graph
        plt.show()

if __name__ == '__main__':
    root = tk.Tk()
    app = GPA_Calculator(root)
    root.mainloop()
