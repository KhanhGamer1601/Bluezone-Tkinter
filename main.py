#import library
from tkinter import*
from time import*
from tkinter import messagebox
from tkinter.ttk import*

#main code
class App:
    def __init__(self):
        self.app = Tk()
        self.app.title('Bluzone !')
        self.app.geometry('600x600+300+50')

        self.main_menu = Menu(self.app)
        self.file = Menu(self.main_menu, tearoff = '0')
        self.about = Menu(self.main_menu, tearoff = '0')
        self.main_menu.add_cascade(label = 'File', menu = self.file)
        self.main_menu.add_command(label = 'About', command = self.About)
        self.file.add_command(label = 'Exit', command = self.app.destroy)

        self.app_title = Label(self.app, text = 'Bluezone', font = ('Times', 16)).pack()

        self.Username = Label(self.app, text = 'Username: ').place(x = 150, y = 50)
        self.Username_Data = StringVar()
        self.Username_entry = Entry(self.app, textvariable = self.Username_Data)
        self.Username_entry.place(x = 280, y = 50)

        self.Date_List = [
            i for i in range(1, 32)
        ]
        self.Month_List = [
            i for i in range(1, 13)
        ]
        self.Year_List = [
            i for i in range(1900, 2022)
        ]

        self.Date_Label = Label(self.app, text = 'Date you were born: ').place(x = 150, y = 100)
        self.Month_Label = Label(self.app, text = 'Month you were born: ').place(x = 150, y = 150)
        self.Year_Label = Label(self.app, text = 'Year you were born: ').place(x = 150, y = 200)

        self.Date = Combobox(self.app)
        self.Date['values'] = self.Date_List
        self.Date.place(x = 280, y = 100)

        self.Month = Combobox(self.app)
        self.Month['values'] = self.Month_List
        self.Month.place(x = 280, y = 150)
        self.Month.bind('<<ComboboxSelected>>', self.BornMonth)

        self.Year = Combobox(self.app)
        self.Year['values'] = self.Year_List
        self.Year.place(x = 280, y = 200)
        self.Year.bind('<<ComboboxSelected>>', self.BornYear)

        self.Gender = IntVar()
        self.Male = Radiobutton(self.app, text = 'Male', variable = self.Gender, value = 1).place(x = 150, y = 250)
        self.Female = Radiobutton(self.app, text = 'Female', variable = self.Gender, value = 2).place(x = 230, y = 250)

        self.Show_Datetime = Label(self.app, text = 'Time: ')
        self.Show_Datetime.place(x = 150, y = 300)
        self.UpdateTime()

        self.Countries = [
            'Vietnam',
            'China',
            'America',
            'Japan',
        ]

        self.Nationality_Label = Label(self.app, text = 'Nationality: ').place(x = 150, y = 350)
        self.Nationality = Combobox(self.app)
        self.Nationality['values'] = self.Countries
        self.Nationality.place(x = 280, y = 350)

        self.User_var = StringVar()
        self.User_Target_Var = StringVar()

        self.User_Position_Entry = None
        self.User_Target_Entry = None
        
        self.Cough_Var = StringVar()
        self.Sneeze_Var = StringVar()
        self.Snivel_Var = StringVar()
        self.Shortness_Of_Breath_Var = StringVar()

        self.Next = Button(self.app, text = 'Next', width = 16, command = self.Next).place(x = 150, y = 400)

        self.app.config(menu = self.main_menu)
        self.app.mainloop()

    def Next(self):
        try:
            if self.Username_Data.get() == '':
                return messagebox.showinfo('notification', 'You have forgotten to choose the username !')
            if self.Gender.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the gender !')
            if self.Nationality.get() == '':
                return messagebox.showinfo('notification', 'You have forgotten to choose the nationality !')
            if self.Date.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the date !')
            if self.Month.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the month !')
            if self.Year.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the year !')
            else:
                self.Username_entry.configure(background = 'white')
            Save = open(self.Username_Data.get(), 'a')
            Save.write(self.Username_Data.get() + '\n')
            Save.write(str(self.Date.get()) + '\n')
            Save.write(str(self.Month.get()) + '\n')
            Save.write(str(self.Year.get()) + '\n')
            Save.write(str(self.Gender.get()) + '\n')
            Save.write(self.Nationality.get() + '\n')
        except:
            messagebox.showinfo('Error', 'error')

        page = Toplevel(self.app)
        page.geometry('600x600+0+0')
        page_title = Label(page, text = 'Bluezone', font = ('Times', 16)).pack()

        self.User_Position = Label(page, text = 'Your location: ').place(x = 150, y = 50)
        self.User_Position_Entry = Entry(page, textvariable = self.User_var)
        self.User_Position_Entry.place(x = 270, y = 50)

        self.User_Target = Label(page, text = 'Your place to come: ').place(x = 150, y = 100)
        self.User_Target_Entry = Entry(page, textvariable = self.User_Target_Var)
        self.User_Target_Entry.place(x = 270, y = 100)

        self.User_Health = Label(page, text = 'Your health: ').place(x = 150, y = 150)
        self.Cough = Checkbutton(page, text = 'Cough', variable = self.Cough_Var, onvalue = 'Cough', offvalue = 'None')
        self.Cough.place(x = 150, y = 200)
        self.Sneeze = Checkbutton(page, text = 'Sneeze', variable = self.Sneeze_Var, onvalue = 'Sneeze', offvalue = 'None')
        self.Sneeze.place(x = 150, y = 250)
        self.Snivel = Checkbutton(page, text = 'Snivel', variable = self.Snivel_Var, onvalue = 'Snivel', offvalue = 'None')
        self.Snivel.place(x = 150, y = 300)
        self.Shortness_Of_Breath = Checkbutton(page, text = 'Shortness of breath', variable = self.Shortness_Of_Breath_Var, onvalue = 'Shortness of breath', offvalue = 'None')
        self.Shortness_Of_Breath.place(x = 150, y = 350) 

        Submit = Button(page, text = 'Submit', width = 16, command = self.Bluezone_Submit).place(x = 150, y = 400)

    def Bluezone_Submit(self):
        try:
            if self.User_var.get() == '':
                messagebox.showinfo('notification', 'You have forgotten to choose your current position !')
            if self.User_Target_Var.get() == '':
                messagebox.showinfo('notification', 'You have forgotten to choose the position you want to come !')
            Save = open(self.Username_Data.get(), 'a')
            Save.write(self.User_var.get() + '\n')
            Save.write(self.User_Target_Var.get() + '\n')
            Save.write(self.Cough_Var.get() + '\n')
            Save.write(self.Sneeze_Var.get() + '\n')
            Save.write(self.Snivel_Var.get() + '\n')
            Save.write(self.Shortness_Of_Breath_Var.get() + '\n')
            Save.close()
            messagebox.showinfo('notification', 'Thank you for submiting !')
        except:
            messagebox.showinfo('Error', 'error')

    def UpdateTime(self):
        current_time = strftime('%H:%M:%S')
        self.Show_Datetime.config(text = current_time)
        self.Show_Datetime.after(200, self.UpdateTime)

    def BornMonth(self, event):
        if int(self.Month.get()) == 1 or int(self.Month.get()) == 3 or int(self.Month.get()) == 5 or int(self.Month.get()) == 7 or int(self.Month.get()) == 8 or int(self.Month.get()) == 10 or int(self.Month.get()) == 12:
            self.Date['values'] = self.Date_List
        if int(self.Month.get()) == 4 or int(self.Month.get()) == 6 or int(self.Month.get()) == 9 or int(self.Month.get()) == 11:
            self.Date['values'] = self.Date_List[0:30]
        if int(self.Month.get()) == 2:
            try:
                if int(self.Year.get()) % 4 == 0:
                    self.Date['values'] = self.Date_List[0:29]
                else:
                    self.Date['values'] = self.Date_List[0:28]
            except:
                self.Date['values'] = self.Date_List[0:28]
        self.Date.set(1)

    def BornYear(self, event):
        if int(self.Year.get()) % 4 == 0:
            try:
                if int(self.Month.get()) == 2:
                    self.Date['values'] = self.Date_List[0:29]
                else:
                    self.Date['values'] = self.Date_List[0:28]
            except:
                pass
        else:
            self.BornMonth(event)

    def About(self):
        notification = 'This app has been created because the gornverment need to control your activities when covid-19 is raging !'
        messagebox.showinfo('notification', notification)

main = App()
