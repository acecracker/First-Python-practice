from cgitb import text
from tkinter import *

root = Tk()
root.title("CKM_TestProject")
root.geometry("300x300-100+100") # 가로 * 세로

root.resizable(False,False)  #  화면 크기변경 Disable

photo = PhotoImage(file="gui_basic/img.png")

label1 = Label(root, text = " 안녕하세요")
label1.pack()

label2 = Label(root, image = photo)
label2.pack()


def btncmd():
    print("버튼이 클릭되었어용")

def change():
    label1.config(text="또 만나요")

def change1():
    label1.config(text="처음으로")


txt = Text(root, width = 30, height =5)
txt.pack()
txt.insert(END,"여러줄을 입력할수 있지")

entry = Entry(root, width=30)
entry.pack()
entry.insert(0,"한줄만 입력해요")

btn3 = Button(root,  width=10, height= 5, text = "버튼3", command=change1)
btn3.pack()


btn6 = Button(root, image=photo, command= change)
btn6.pack()

btn7 = Button(root, text ="동작하는 버튼", command=btncmd)
btn7.pack()



root.mainloop()


