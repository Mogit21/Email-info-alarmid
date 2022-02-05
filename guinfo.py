import tkinter as tk
import smtplib
from email.message import EmailMessage
from okrunfunctions import queryidtable, datalisted, datatext, queryregiontable


def okrun():
    """query information from table id in db for NE ID input by the user
    and fills in the to, cc , subject and body text widgets with the correct output
    containing the corresponding information of the NE collected from the sqlite query.
    """
    
    try:
        idinput = neid.get("1.0",'end-1c')
        data = queryidtable(idinput)            #function 1
        listnames = datalisted(data,1)            #function 2
        listipaddresses = datalisted(data,2)
        listoffices = datalisted(data,3)
        textnames = datatext(listnames)         #function 3
        textipaddresses= datatext(listipaddresses)
        distinctoffices = datatext(list(set(listoffices)))  #To have unique values
        offices=tuple(distinctoffices.split(","))           # To be used in region table sql query
        
        text = f"Link to NE {textnames} are down"
        message = f"""Hello, 
        To inform you that the link to {textnames} are down.
        IP address:{textipaddresses}
        Office:{distinctoffices}
        Best regards.
        Signature"""
        
        rgresult = queryregiontable(offices)            #function 4
        listowners = datalisted(rgresult,2) 
        owners= list(set(listowners))           #to have distinct values of owners
        owners= (';').join(owners)
        
        to.insert(tk.END, "recipient1@email.com, recipient2@email.com, recipient3@email.com")
        cc.insert(tk.END, owners +", recipient4@email.com, recipient5@email.com")
        subject.insert(tk.END, text)
        body.insert(tk.END, message)
    except Exception as e:
        print (e)

def sendemail():
    """All arguments need to be of string type
    This function will send an email and return sending result message"""

    msg = EmailMessage()
    msg['Subject'] = subject.get("1.0",'end-1c') 
    msg['From'] = sender.get("1.0",'end-1c') 
    msg['To'] = to.get("1.0",'end-1c')
    msg['Cc'] = cc.get("1.0",'end-1c')
    msg.set_content(body.get("1.0",'end-1c'))
    sender_email = str(sender.get("1.0",'end-1c'))
    sender_pwd = str(password.get("1.0",'end-1c'))
    server = smtplib.SMTP_SSL(host='your_mail_server', port=465)   # put in your email server and port for sending email
    try:
        server.login(sender_email, sender_pwd)
        server.send_message(msg)
        res = "email sent successfully!"  
        result.insert(tk.END, res)
    except Exception as e:
        res = e
        result.insert(tk.END, e)
    finally:
        server.quit()


root = tk.Tk()
root.title("Title")

canvas = tk.Canvas(root, width=800, height=650)
canvas.grid(columnspan=4,rowspan=9)
frame = tk.Frame(root, width=800, height=650,bg="blue")
frame.grid(columnspan=4, rowspan=8, column=0, row=0)
# Asking input
asking = tk.Label(root, text="Please enter NE ID, multiple NE IDs must be separated by commas ( , ):")
asking.grid(columnspan=2, column=0, row=0)
# Descriptions
senderdesc = tk.Label(root, text="Sender email (Company name)")
senderdesc.grid(columnspan=1, column=0, row=1)
passwordesc = tk.Label(root, text="Enter password")
passwordesc.grid(columnspan=1, column=2, row=1)
todesc = tk.Label(root, text="TO")
todesc.grid(columnspan=1, column=0, row=2)
ccdesc = tk.Label(root, text="CC")
ccdesc.grid(columnspan=1, column=0, row=3)
subjectdesc = tk.Label(root, text="Subject")
subjectdesc.grid(columnspan=1, column=0, row=4)
bodydesc = tk.Label(root, text="Message")
bodydesc.grid(columnspan=1, column=0, row=5)
dbadmindesc = tk.Label(root, text="DB admin")
dbadmindesc.grid(columnspan=1, column=0, row=7)
# Text widgets
neid = tk.Text(root, width=25, height=1)
neid.grid(columnspan=1, column=2, row=0)
sender = tk.Text(root, width=25, height=1)
sender.grid(columnspan=1, column=1, row=1)
password = tk.Text(root, width=15, height=1)
password.grid(columnspan=1, column=3, row=1)
to = tk.Text(root, width=65, height=2)
to.grid(columnspan=3, column=1, row=2)
cc = tk.Text(root, width=65, height=2)
cc.grid(columnspan=3, column=1, row=3)
subject = tk.Text(root, width=65, height=1)
subject.grid(columnspan=3, column=1, row=4)
body = tk.Text(root, width=65, height=10)
body.grid(columnspan=3, column=1, row=5)
result = tk.Text(root, width=40, height=1)
result.grid(columnspan=2, column=2, row=6)
admin = tk.Text(root, width=65, height=1)
admin.grid(columnspan=3, column=1, row=7)
# Button widgets
ok = tk.Button(root, text="OK", width=10, height=1, command = okrun)
ok.grid(columnspan=1, column=3, row=0)
send = tk.Button(root, text="Send", width=10, height=1, command = sendemail)
send.grid(columnspan=1, column=1, row=6)

root.mainloop()

