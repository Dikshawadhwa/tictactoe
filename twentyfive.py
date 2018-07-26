import tkinter as t
from tkinter import messagebox
root=t.Tk()
global x
x='y'
root.geometry('250x300')
root.title("TIC TACK TOE")
b=t.Button(root,command=lambda:fun(b))
b.grid(row=1,column=1,padx=10,pady=10,ipadx=25,ipady=3)
b1=t.Button(root,command=lambda:fun(b1))
b1.grid(row=2,column=1,padx=10,pady=10,ipadx=25,ipady=3)
b2=t.Button(root,command=lambda:fun(b2))
b2.grid(row=3,column=1,padx=10,pady=10,ipadx=25,ipady=3)
b3=t.Button(root,command=lambda:fun(b3))
b3.grid(row=1,column=2,padx=10,pady=10,ipadx=25,ipady=3)
b4=t.Button(root,command=lambda:fun(b4))
b4.grid(row=1,column=3,padx=10,pady=10,ipadx=25,ipady=3)
b5=t.Button(root,command=lambda:fun(b5))
b5.grid(row=2,column=2,padx=10,pady=10,ipadx=25,ipady=3)
b6=t.Button(root,command=lambda:fun(b6))
b6.grid(row=2,column=3,padx=10,pady=10,ipadx=25,ipady=3)
b7=t.Button(root,command=lambda:fun(b7))
b7.grid(row=3,column=2,padx=10,pady=10,ipadx=25,ipady=3)
b8=t.Button(root,command=lambda:fun(b8))
b8.grid(row=3,column=3,padx=10,pady=10,ipadx=25,ipady=3)
b9=t.Button(root,command=lambda:reset(),text='RESET')
b9.grid(row=4,columnspan=10,padx=10,pady=10,sticky=t.E+t.W)
b10=t.Button(root,command=lambda:exit(),text='EXIT')
b10.grid(row=5,columnspan=10,padx=10,pady=10,sticky=t.E+t.W)
def fun(button):
    global x
    if x is 'y':
        a=button['text']
        if(a==''):
            button['text']='X'
            x='n'
            win()
    elif x is 'n':
        a=button['text']
        if(a==''):
            button['text']='0'
            x='y'
            win()
def reset():
    b['text']=''
    b1['text']=''
    b2['text']=''
    b3['text']=''
    b4['text']=''
    b5['text']=''
    b6['text']=''
    b7['text']=''
    b8['text']=''
def exit():
    root.destroy()
def win():
    if(b['text']==b1['text']==b2['text']=='X'):
       messagebox.showinfo("RESULT","Player X wins")
       reset()
    elif (b['text'] == b1['text'] == b2['text'] == '0'):
        messagebox.showinfo("RESULT", "Player 0 wins")
        reset()
    elif (b3['text'] == b5['text'] == b7['text'] == 'X'):
        messagebox.showinfo("RESULT", "Player X wins")
        reset()
    elif (b3['text'] == b5['text'] == b7['text'] == '0'):
        messagebox.showinfo("RESULT", "Player 0 wins")
        reset()
    elif (b4['text'] == b6['text'] == b8['text'] == 'X'):
        messagebox.showinfo("RESULT", "Player X wins")
        reset()
    elif (b4['text'] == b6['text'] == b8['text'] == '0'):
        messagebox.showinfo("RESULT", "Player 0 wins")
        reset()
    elif (b['text'] == b3['text'] == b4['text'] == 'X'):
        messagebox.showinfo("RESULT", "Player X wins")
        reset()
    elif (b['text'] == b3['text'] == b4['text'] == '0'):
        messagebox.showinfo("RESULT", "Player 0 wins")
        reset()
    elif (b1['text'] == b5['text'] == b6['text'] == 'X'):
        messagebox.showinfo("RESULT", "Player X wins")
        reset()
    elif (b1['text'] == b5['text'] == b6['text'] == '0'):
        messagebox.showinfo("RESULT", "Player 0 wins")
        reset()
    elif (b2['text'] == b7['text'] == b8['text'] == 'X'):
        messagebox.showinfo("RESULT", "Player X wins")
        reset()
    elif (b2['text'] == b7['text'] == b8['text'] == '0'):
        messagebox.showinfo("RESULT", "Player 0 wins")
        reset()
    elif (b['text'] == b5['text'] == b8['text'] == 'X'):
        messagebox.showinfo("RESULT", "Player X wins")
        reset()
    elif (b['text'] == b5['text'] == b8['text'] == '0'):
        messagebox.showinfo("RESULT", "Player 0 wins")
        reset()
    elif (b4['text'] == b5['text'] == b2['text'] == 'X'):
        messagebox.showinfo("RESULT", "Player X wins")
        reset()
    elif (b4['text'] == b5['text'] == b2['text'] == '0'):
        messagebox.showinfo("RESULT", "Player 0 wins")
        reset()
    elif(b['text']!='' and b1['text']!='' and b2['text']!='' and b3['text']!='' and b4['text']!='' and b5['text']!='' and b6['text']!='' and b7['text']!='' and b8['text']!=''):
        messagebox.showinfo("RESULT", "DRAW")
        reset()




root.mainloop()
