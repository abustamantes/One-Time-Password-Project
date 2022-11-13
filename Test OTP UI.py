from argparse import _MutuallyExclusiveGroup
from tkinter import *
import hmac
import hashlib
import base64

root = Tk()
root.title("Server")
root.geometry("400x150")
e = Entry(root, width=50, bg="white", fg="black")
e.pack()
key = "800070FF00FF08012"
key = bytes(key, 'utf-8')
x = 1
def myClick():
    global x
    global key
    print(f'This is the current counter: {x}')
    input = e.get()
    msg = bytes(f'{x}', 'utf-8')
    digest = hmac.new(key, msg, "sha256").digest()
    code = base64.b64encode(digest).decode('utf-8')
    code = code[:6]
    if (code == input):
        myLabel.config(text="Access granted!")
        x=x+1
        key = key.replace(key, digest)
    else:
        key2 = key
        for i in range(x,x+11):
            msg2 = bytes(f'{i}', 'utf-8')
            digest2 = hmac.new(key2, msg2, "sha256").digest()
            code2 = base64.b64encode(digest2).decode('utf-8')
            code2 = code2[:6]
            if (code2==input):
                myLabel.config(text="")
                myLabel.config(text="Access granted!- Soft synchronization was done.")
                x=i+1
                key = key.replace(key, digest2)
                break
            else:
                myLabel.config(text="Denied, try again or synchronize your token!")
            key2=key2.replace(key2, digest2)
def sy():
    global x
    global key
    x1=x
    key1=key
    input = e.get()
    while True:
        msg = bytes(f'{x1}', 'utf-8')
        digest = hmac.new(key1, msg, "sha256").digest()
        code = base64.b64encode(digest).decode('utf-8')
        code = code[:6]
        x1 = x1 + 1
        key1 = key1.replace(key1, digest)
        if (code == input):
            myLabel.config(text="It is synchronized, use the next OTP")
            x=x1
            key=key1
            print(f'This the synchronized counter: {x}')
            print(f'This is the code that you inserted:{code}')
            break
myButton = Button(root, text="Enter the OTP", command=myClick, padx=10, pady=5, fg="black", bg="white")
myButton.pack()
syn=Button(root,text="Synchronize",command=sy, padx=10, pady=5, fg="black", bg="white")
syn.pack()
myLabel=Label(root)
myLabel.pack()
root.mainloop()



