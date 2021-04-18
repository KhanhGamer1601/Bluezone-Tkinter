#import library
from tkinter import*
from time import*
from tkinter import messagebox

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
        self.Username_entry.place(x = 270, y = 50)

        self.Date_List = [
            i for i in range(1, 32)
        ]
        self.Month_List = [
            i for i in range(1, 13)
        ]
        self.Year_List = [
            i for i in range(1900, 2022)
        ]

        self.Date_Var = IntVar()
        self.Month_Var = IntVar()
        self.Year_Var = IntVar()

        self.Date_Label = Label(self.app, text = 'Date you were born: ').place(x = 150, y = 100)
        self.Month_Label = Label(self.app, text = 'Month you were born: ').place(x = 150, y = 150)
        self.Year_Label = Label(self.app, text = 'Year you were born: ').place(x = 150, y = 200)

        self.Date = OptionMenu(self.app, self.Date_Var, *self.Date_List).place(x = 280, y = 100)
        self.Month = OptionMenu(self.app, self.Month_Var, *self.Month_List).place(x = 280, y = 150)
        self.Year = OptionMenu(self.app, self.Year_Var, *self.Year_List).place(x = 280, y = 200)

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

        self.Nationality_var = StringVar()
        self.Nationality_Label = Label(self.app, text = 'Nationality: ').place(x = 150, y = 350)
        self.Nationality = OptionMenu(self.app, self.Nationality_var, *self.Countries)
        self.Nationality.place(x = 270, y = 350)

        self.User_var = StringVar()
        self.User_Target_Var = StringVar()
        self.User_Health_Var = StringVar()

        self.User_Position_Entry = None
        self.User_Target_Entry = None
        self.User_Health_Entry = None
        
        self.Health_List = [
            'cough',
            'sneeze',
            'snivel',
            'shortness of breath',
        ]

        self.Next = Button(self.app, text = 'Next', width = 16, command = self.Next).place(x = 150, y = 400)

        self.app.config(menu = self.main_menu)
        self.app.mainloop()

    def Next(self):
        try:
            self.HandleUsername = [self.Username_entry, self.Username_Data]

            if self.HandleUsername[1].get() == '':
                self.HandleUsername[0].configure(bg = 'red')
            if self.Gender.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the gender !')
            if self.Nationality_var.get() == '':
                return messagebox.showinfo('notification', 'You have forgotten to choose the nationality !')
            if self.Date_Var.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the date !')
            if self.Month_Var.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the month !')
            if self.Date_Var.get() == 30 or self.Date_Var.get() == 31 and self.Month_Var.get() == 2:
                return messagebox.showinfo('notification', 'Does not exist !')
            if self.Year_Var.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the year !')
            else:
                self.HandleUsername[0].configure(bg = 'white')
            Save = open(self.Username_Data.get(), 'a')
            Save.write(self.Username_Data.get() + '\n')
            Save.write(str(self.Date_Var.get()) + '\n')
            Save.write(str(self.Month_Var.get()) + '\n')
            Save.write(str(self.Year_Var.get()) + '\n')
            Save.write(str(self.Gender.get()) + '\n')
            Save.write(self.Nationality_var.get() + '\n')
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
        self.User_Health_Entry = OptionMenu(page, self.User_Health_Var, *self.Health_List)
        self.User_Health_Entry.place(x = 270, y = 150)

        Submit = Button(page, text = 'Submit', width = 16, command = self.Bluezone_Submit).place(x = 150, y = 200)

    def Bluezone_Submit(self):
        self.entrylist = [
            [self.User_Position_Entry, self.User_var], 
            [self.User_Target_Entry, self.User_Target_Var], 
            [self.User_Health_Entry, self.User_Health_Var],
        ]

        try:
            errorcount = 0
            for i in self.entrylist:
                if i[1].get() == '':
                    i[0].configure(bg='red')
                    errorcount += 1
                else:
                    i[0].configure(bg='white')
            if errorcount != 0:    
                return messagebox.showwarning('notification', 'Missing Infomation!')
            Save = open(self.Username_Data.get(), 'a')
            Save.write(self.User_var.get() + '\n')
            Save.write(self.User_Target_Var.get() + '\n')
            Save.write(self.User_Health_Var.get() + '\n')
            Save.close()
            messagebox.showinfo('notification', 'Thank you for submiting !')
        except:
            messagebox.showinfo('Error','error')

    def UpdateTime(self):
        current_time = strftime('%H:%M:%S')
        self.Show_Datetime.config(text = current_time)
        self.Show_Datetime.after(200, self.UpdateTime)

    def About(self):
        notification = 'This app has been created because the gornverment need to control your activities when covid-19 is raging !'
        messagebox.showinfo('notification', notification)

main = App()
