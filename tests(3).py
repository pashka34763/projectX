def toggle_password():
    if code['show'] == '*':
        code.config(show='')
        conform_code.config(show='')
        toggle_button.config(image=open_eye_photo)
    else:
        code.config(show='*')
        conform_code.config(show='*')
        toggle_button.config(image=closed_eye_photo)

def on_enter(e):
    code.delete(0,'end')
    code.config(show='*')
def on_leave(e):
    name1=code.get()
    if name1=='':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
    

Frame(frame, width=295, height=2, bg='black').place(x=25,y=177)

    #---------------------------------------------------------------------

def on_enter(e):
    conform_code.delete(0,'end')
    conform_code.config(show='*')

def on_leave(e):
    name2=conform_code.get()
    if name2=='':
        conform_code.insert(0, 'Conform Password')


conform_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0, 'Conform password')
conform_code.bind("<FocusIn>", on_enter)
conform_code.bind("<FocusOut>", on_leave)

eye_image = Image.open("openeye.png")
closed_eye_image = Image.open("closeye.png")

# Изменить размер изображений
eye_image = eye_image.resize((20, 20), Image.BICUBIC)
closed_eye_image = closed_eye_image.resize((20, 20), Image.BICUBIC)

# Создать объекты изображений Tkinter
open_eye_photo = ImageTk.PhotoImage(eye_image)
closed_eye_photo = ImageTk.PhotoImage(closed_eye_image)

toggle_button = Button(frame, image=closed_eye_photo, command=toggle_password)
toggle_button.pack()

Frame(frame, width=295, height=2, bg='black').place(x=25,y=247)