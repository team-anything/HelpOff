import requests
from bs4 import BeautifulSoup

class sms :
    def __init__(self,username,password):
        #Logging In

        self.url='http://site24.way2sms.com/Login1.action?'
        self.details={'username':username,'password':password}
        self.cook=requests.session()

        #creating spoof
        self.cook.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"

        self.query=self.cook.post(self.url,data=self.details)

        #initaially logged out
        self.Logged =False

        # query returned returned value 200 = True ie logged in
        if self.query.status_code!=200 :
            self.Logged=False
        else :
            self.Logged=True

        #session ids is produced everytime a session starts
        self.id=self.cook.cookies.get_dict()['JSESSIONID'][4:]

    def count(self):
        #count to messages left per day
        self.messages_left='http://site24.way2sms.com/sentSMS?Token='+self.id
        self.query = self.cook.get(self.messages_left)

        #After getting raw data converting to Soup
        self.soup=BeautifulSoup(self.query.text,'html.parser')

        self.data=self.soup.find("div",{"class":"hed"}).h2.text

        self.sent=0

        for self.i in self.data:
            if self.i.isdecimal():
                self.sent=10*self.sent +int(self.i)
        return self.sent

    def send(self,number,message) :
        # sending in queue
        if len(message)>139 or len(number)!=10 or not number.isdecimal():
            return False
        self.payload={
            'ssaction':'ss',
            'Token':self.id,
            'mobile':number,
            'message':message,
            'msglen':129,
        }
        self.message_url='http://site24.way2sms.com/smstoss.action'
        self.query=self.cook.post(self.message_url,data=self.payload)

        if self.query.status_code!=200:
            return False
        return True
    def Logout(self):
        #Logging Out
        self.cook.get('http://site24.way2sms.com/entry?ec=0080&id=dwks')

        # close session
        self.cook.close()
        self.Logged=False

def send_sms(name,event):
    query = sms("9820501130","E6896N") # username is usually Mobile Number (Logging in)
    my_message = "Hi, " + name + "\nYou're successfully registered for :" + event
    query.send("8976339502",my_message) # recipient = receiver's number
    query.Logout()
    print("Message Sent")

#if __name__ == "__main___":
print("YES")
text = input("ENTER:")
send_sms(text,"HACKNCODE")
