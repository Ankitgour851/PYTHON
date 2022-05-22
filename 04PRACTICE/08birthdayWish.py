import pandas as pd
import datetime
import smtplib
import os

os.chdir(r"C:\Users\ASUS\Desktop\practice prob in python\7birthdaywish")
# os.mkdir("Testing")

GMAIL_ID = ''
GMAIL_PSWD = ''

def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject:{sub}\n\n{msg}")
    s.quit()

if __name__ == "__main__":
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()

    df = pd.read_excel("data.xlsx")
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(type(today))
    writeInt= []

    for index,item in df.iterrows():
        # print(index,item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'],"Happy Birthday",item['Dialogue'])
            writeInt.append(index)

    # print(writeInt)
    for i in writeInt:
        yr = df.loc[i,'Year']
        # print(yr)
        df.loc[i,'Year'] = str(yr) + ','+ str(yearNow)
        # print(df.loc[i,'Year'])

    # print(df)
    df.to_excel('data.xlsx',index=False)