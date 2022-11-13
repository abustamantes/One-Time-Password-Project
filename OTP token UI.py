# Cliente code:
from tkinter import *
import hmac
import hashlib
import base64

root=Tk()
root.title("Client")
root.geometry("200x100")
key="800070FF00FF08012"
key=bytes(key,'utf-8')
x=0
def button_click():  
    global x
    global key
    x +=1
    msg=bytes(f'{x}','utf-8')
    digest = hmac.new(key, msg,"sha256").digest() #
    key=key.replace(key,digest)
    code=base64.b64encode(digest)    
    code=code[:6]
    myLabel.config(text=code)
    print(x)
OTP=Button(root,text="Generate OTP",padx=20,pady=10,command=button_click,fg="black", bg="white")
OTP.pack()
myLabel=Label(root)
myLabel.pack()
root.mainloop()