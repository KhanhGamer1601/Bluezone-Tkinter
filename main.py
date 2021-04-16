#import library
from tkinter import*
from datetime import*
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

        self.Gender = IntVar()
        self.Male = Radiobutton(self.app, text = 'Male', variable = self.Gender, value = 1).place(x = 150, y = 100)
        self.Female = Radiobutton(self.app, text = 'Female', variable = self.Gender, value = 2).place(x = 230, y = 100)

        self.Now = datetime.now()
        self.Datetime = self.Now.strftime('%H hours %M minutes %S seconds')
        self.Show_Datetime = Label(self.app, text = 'Time: ' + self.Datetime).place(x = 150, y = 150)

        self.Countries = [
            'Vietnam',
            'China',
            'America',
            'Japan',
        ]

        self.Nationality_var = StringVar()
        self.Nationality = OptionMenu(self.app, self.Nationality_var, *self.Countries)
        self.Nationality.place(x = 150, y = 200)

        self.User_var = StringVar()
        self.User_Position = Label(self.app, text = 'Your location: ').place(x = 150, y = 250)
        self.User_Position_Entry = Entry(self.app, textvariable = self.User_var)
        self.User_Position_Entry.place(x = 270, y = 250)

        self.User_Target_Var = StringVar()
        self.User_Target = Label(self.app, text = 'Your place to come: ').place(x = 150, y = 300)
        self.User_Target_Entry = Entry(self.app, textvariable = self.User_Target_Var)
        self.User_Target_Entry.place(x = 270, y = 300)

        self.User_Health_Var = StringVar()
        self.User_Health = Label(self.app, text = 'Your health: ').place(x = 150, y = 350)
        self.User_Health_Entry = Entry(self.app, textvariable = self.User_Health_Var)
        self.User_Health_Entry.place(x = 270, y = 350)

        self.entrylist = [
            [self.Username_entry, self.Username_Data], 
            [self.User_Position_Entry, self.User_var], 
            [self.User_Target_Entry, self.User_Target_Var], 
            [self.User_Health_Entry, self.User_Health_Var],
        ]

        self.Submit = Button(self.app, text = 'Submit', width = 16, command = self.Bluezone_Submit).place(x = 150, y = 400)

        self.app.config(menu = self.main_menu)
        self.app.mainloop()

    def Bluezone_Submit(self):
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
            if self.Gender.get() == 0:
                return messagebox.showinfo('notification', 'You have forgotten to choose the gender !')
            if self.Nationality_var.get() == '':
                return messagebox.showinfo('notification', 'You have forgotten to choose the nationality !')
            Save = open(self.Username_Data.get(), 'a')
            Save.write(self.Username_Data.get() + '\n')
            Save.write(str(self.Gender.get()) + '\n')
            Save.write(self.Nationality_var.get() + '\n')
            Save.write(self.User_var.get() + '\n')
            Save.write(self.User_Target_Var.get() + '\n')
            Save.write(self.User_Health_Var.get() + '\n')
            Save.close()
            messagebox.showinfo('notification', 'Thank you for submiting !')
        except:
            messagebox.showinfo('Error','error')


    def About(self):
        notification = 'This app has been created because the gornverment need to control your activities when covid-19 is raging !'
        messagebox.showinfo('notification', notification)

main = App()
