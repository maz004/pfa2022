import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("maz003.kali@gmail.com", "ABC123654789m#")

# sent the mail
yag.send(
    to="ali.messoudi99@gmail.com",
    subject="Liste d'absence", # email subject
    contents="Ci-joint la liste d'absence pour le " + date + "\n ce message est envoyer automatiquement",  # email body
    attachments= filename  # file attached
)
print("Email Sent!")
