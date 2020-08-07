#starter code for gui application using tkinter
# import tkinter
# or 
import tkinter as tk
from tkinter import ttk  # import ttk lib that is more attractive  than tk lib for creating widgets
win=tk.Tk()
win.title('NIKKU GUI')
#create labels
# widgets >>>labels, buttons,radio buttons  --- tk,ttk
name_label=ttk.Label(win,text='enter name : ')
name_label.grid(row=0, column=0, sticky=tk.W)
#for setting labes in window we use pack ,grid >>>pack makes it in center while in grid in we can put row column details
email_label=ttk.Label(win,text='enter email :')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='enter age :')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='Select your gender :')
gender_label.grid(row=3,column=0,sticky=tk.W)

# create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus() #makes the cursor default in this box at start of app

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)


#create combobox
gender_var=tk.StringVar()
gender_combobox= ttk.Combobox(win,width=13,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Others')
gender_combobox.current(0) # it makes the combox fill with the 0th position index in tuple by default :like male is already showing in combobox by default
gender_combobox.grid(row=3,column=1)


# radio button
usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtn2.grid(row=4,column=1)

#check button
checkbtn_var=tk.IntVar()
checkbtn =ttk.Checkbutton(win,text='check if you want to subscribe to our newsletter',variable=checkbtn_var )
checkbtn.grid(row=5,columnspan=3)  #columnspan is used to use to more columns for a task





# # create a button
def action():
    username=name_var.get()
    userage=age_entrybox.get()
    useremail=email_var.get()
    print(f"{username} {userage} old {useremail}")
    usergender=gender_var.get()
    user_type=usertype.get()
    if checkbtn_var.get()==0:
        subscribe='NO'
    else:
        subscribe='YES'
    print(usergender,user_type,subscribe)

    with open('fileproject1.txt','a') as f:
        f.write(f'{username},{userage},{useremail},{usergender},{user_type},{subscribe}\n')
    
    
    #here below method is used to clear the entry box after submitting 
    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    #change color
    name_label.configure(foreground='#b388ff') # you can use your own color  >>hexavalue of colour

    #submit_button.configure(foreground='Red') # change color of the button

submit_button=tk.Button(win,text='submit',command=action)
submit_button.grid(row=6,column=0)







win.mainloop()


