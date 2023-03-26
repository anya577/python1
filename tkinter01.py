from tkinter import *
root = Tk()

hello = Label(root, text='Hello Anna!')
goodbye = Label(root, text='good bye my learning')

myButton = Button(root, text='test button')

root.title('my first GUI program')  
root.geometry('500x400')
root.minsize(200,100)
             

# hello.pack() 
hello.grid(row=0, column=0)
goodbye.grid(row=1,column=3)


root.mainloop()