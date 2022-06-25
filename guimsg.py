from tkinter import *
from tkinter import messagebox
import requests
def send(num, msg):

    api = "NGvXHmZieywAF81ThBnqCuRrIPfdo4Ubg6WlOS2QDsKV0Etj939xQT4b2IpUCNS83frPZitGklXOVhED0"
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {'authorization':f"{api}",
            "sender_id":"FSTSMS",
            "message":msg,
            "language":"english",
            "route":"p",
            "numbers":num}
    response=requests.get(url, params=params)
    dic=response.json()
    print(dic)
    if dic['message']==['SMS sent successfully.']:
        messagebox.showinfo("Succesful", "msg sent")

        msgbox.delete("1.0", "end")

def run1():
    msgValue = msgbox.get("1.0", "end-1c")
    numb=sm.get()
    send(numb, msgValue)
root=Tk()
root.title("send messsage")
root.config(bg="orange")
root.geometry("650x800")
root.minsize(650, 800)
root.maxsize(650, 800)
frame=Frame(root, borderwidth=4, bg="blue", width=35)
frame.grid(row=0, column=2)
Name=Label(frame, text="vishesh message box", font="helvetica 12 bold", fg="red", width=25)
Name.grid(row=0, column=2)
st=StringVar()
sm=StringVar()

# creating a label for password
passw_label = Label(root, text='Number', font=('calibre', 12, 'bold'), fg="blue")
passw_label.grid(column=0, row=4, pady=10)

# creating a entry for password
passw_entry =Entry(root, textvariable=sm, font=('calibre', 10, 'normal'), borderwidth=6, relief='groove')
passw_entry.grid(column=2, row=4, pady=10)




passw_label = Label(root, text='Type Your msg', font=('calibre', 12, 'bold'), fg="blue")
passw_label.grid(column=0, row=10)


msgbox = Text(root,
                   height=10,
                   width=55,
               borderwidth=5,
               relief=GROOVE,
              bg="#79975A",
              fg="white",
              font="helvetica 12 bold")


msgbox.grid(row=10, column=2, pady=20)
# # print(st.get())
# print(textbox.get("1.0","end-1c"))
print()

Button(root, text="Send", command=run1, font="hislerim 15 bold", fg="blue", borderwidth=5, relief='sunken').grid(row=11, column=2)
root.mainloop()
