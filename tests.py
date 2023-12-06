from tkinter import *
from tkinter import messagebox
import ast 
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.iconbitmap('kevin.ico')

def signin():
    username=user.get()
    password=code.get()

    file = open('datasheet.txt', 'r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("Weather_App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        screen.iconbitmap('kevin.ico')

        Label(screen, text='SHERMAN!!!', bg='#fff', font=('Calibry(Body)',20,'bold')).pack()

        tab_control = ttk.Notebook(screen)

        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Личный кабинет')

        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Температура')

        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab3, text='Влажность')

        tab4 = ttk.Frame(tab_control)
        tab_control.add(tab4, text='Осадки')

        tab5 = ttk.Frame(tab_control)
        tab_control.add(tab5, text='Скорость ветра')

        tab_control.pack(expand=1, fill='both')

        lb1=Label(tab1, text='''Username : '''+username+
        '''\nPassword : '''+password, bg='#fff', font=('Calibry(Body)',15,'bold')).place(x=5,y=10)
        lb2=Label(tab2, text='Прогноз на 10 дней', bg='#fff', font=('Calibry(Body)',15,'bold')).place(x=5,y=10)
        lb3=Label(tab3, text='Прогноз на 10 дней', bg='#fff', font=('Calibry(Body)',15,'bold')).place(x=5,y=10)
        lb4=Label(tab4, text='Прогноз на 10 дней', bg='#fff', font=('Calibry(Body)',15,'bold')).place(x=5,y=10)
        lb5=Label(tab5, text='Прогноз на 10 дней', bg='#fff', font=('Calibry(Body)',15,'bold')).place(x=5,y=10)
        
        screen.mainloop()
    
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

##################################################################################################################################################
def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.iconbitmap('kevin.ico')

    def signup():
        username = user.get()
        password = code.get()
        conform_password = conform_code.get()

        if password==conform_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))
            


                messagebox.showinfo('Signup','Successfully sign up')

            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', 'Both passwords should match')

    def sign():
        window.destroy()


    img = PhotoImage(file='login.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)

    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(x=480,y=50)

    heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',24,'bold'))
    heading.place(x=100,y=5)

    #---------------------------------------------------------------------

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0, 'Username')


    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)

    #---------------------------------------------------------------------

    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0, 'Password')

    def toggle_password1():
        if code.cget("show") == "*":
            code.config(show="")
            # Изменить изображение на закрытый глаз
            eye_image = Image.open("closeye.png")
        else:
            code.config(show="*")
            # Изменить изображение на открытый глаз
            eye_image = Image.open("openeye.png")
    
        # Изменить размер изображения
        eye_image = eye_image.resize((20, 20), Image.BICUBIC)
        # Создать объект изображения Tkinter
        eye_photo = ImageTk.PhotoImage(eye_image)
        # Обновить изображение кнопки
        toggle_button.config(image=eye_photo)
        toggle_button.image = eye_photo


    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    closed_eye_image = Image.open("closeye.png")
    open_eye_image = Image.open("openeye.png")

    # Изменить размер изображений
    closed_eye_image = closed_eye_image.resize((20, 20), Image.BICUBIC)
    open_eye_image = open_eye_image.resize((20, 20), Image.BICUBIC)

    # Создать объекты изображений Tkinter
    closed_eye_photo = ImageTk.PhotoImage(closed_eye_image)
    open_eye_photo = ImageTk.PhotoImage(open_eye_image)

    toggle_button = Button(frame, image=open_eye_photo, command=toggle_password1)
    toggle_button.place(x=320,y=150)

    Frame(frame, width=295, height=2, bg='black').place(x=25,y=177)

    #---------------------------------------------------------------------

    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0, 'Conform password')

    def toggle_password2():
        if conform_code.cget("show") == "*":
            conform_code.config(show="")
            # Изменить изображение на закрытый глаз
            eye_image = Image.open("closeye.png")
        else:
            conform_code.config(show="*")
            # Изменить изображение на открытый глаз
            eye_image = Image.open("openeye.png")
    
        # Изменить размер изображения
        eye_image = eye_image.resize((20, 20), Image.BICUBIC)
        # Создать объект изображения Tkinter
        eye_photo = ImageTk.PhotoImage(eye_image)
        # Обновить изображение кнопки
        toggle_button.config(image=eye_photo)
        toggle_button.image = eye_photo


    conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0, 'Conform password')
    conform_code.bind("<FocusIn>", on_enter)
    conform_code.bind("<FocusOut>", on_leave)

    closed_eye_image = Image.open("closeye.png")
    open_eye_image = Image.open("openeye.png")

    # Изменить размер изображений
    closed_eye_image = closed_eye_image.resize((20, 20), Image.BICUBIC)
    open_eye_image = open_eye_image.resize((20, 20), Image.BICUBIC)

    # Создать объекты изображений Tkinter
    closed_eye_photo = ImageTk.PhotoImage(closed_eye_image)
    open_eye_photo = ImageTk.PhotoImage(open_eye_image)

    toggle_button = Button(frame, image=open_eye_photo, command=toggle_password2)
    toggle_button.place(x=320,y=150)

    Frame(frame, width=295, height=2, bg='black').place(x=25,y=247)

    #----------------------------------------------------------------------

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35,y=280)
    label=Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=340)

    signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=200,y=340)

    window.mainloop()

##################################################################################################################################################################

img = PhotoImage(file='login2.png')
Label(root, image=img, bg='white').place(x=50,y=50)

frame = Frame(root, width=350, height=350, bg='#fff')
frame.place(x=480,y=70)

heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#-------------------------------------------------------------------------------------
 
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#-------------------------------------------------------------

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')

def toggle_password():
    if code.cget("show") == "*":
        code.config(show="")
        # Изменить изображение на закрытый глаз
        eye_image = Image.open("closeye.png")
    else:
        code.config(show="*")
        # Изменить изображение на открытый глаз
        eye_image = Image.open("openeye.png")
    
    # Изменить размер изображения
    eye_image = eye_image.resize((20, 20), Image.BICUBIC)
    # Создать объект изображения Tkinter
    eye_photo = ImageTk.PhotoImage(eye_image)
    # Обновить изображение кнопки
    toggle_button.config(image=eye_photo)
    toggle_button.image = eye_photo

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11), show="*")
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

closed_eye_image = Image.open("closeye.png")
open_eye_image = Image.open("openeye.png")

# Изменить размер изображений
closed_eye_image = closed_eye_image.resize((20, 20), Image.BICUBIC)
open_eye_image = open_eye_image.resize((20, 20), Image.BICUBIC)

# Создать объекты изображений Tkinter
closed_eye_photo = ImageTk.PhotoImage(closed_eye_image)
open_eye_photo = ImageTk.PhotoImage(open_eye_image)

toggle_button = Button(frame, image=open_eye_photo, command=toggle_password)
toggle_button.place(x=320,y=150)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#---------------------------------------------------------------

Button(frame,width=39,pady=7,text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account", fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame, width=6,text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=215,y=270)



root.mainloop()
