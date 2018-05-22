# TODO : Clean var ; rem cache
import query_retreive as qr
import retreiveData as rd
import time,pickle
from flask import Flask, jsonify,request 

app = Flask(__name__)

'''

ADD TEMPLATE : 

'''

@app.route('/',methods=["GET"])
def query():
    previous = ""
    file = open("./aipc.pickle","rb")
    placename = pickle.load(file)
    file.close()
    while(1):
        ans,number = qr.response()
        number = str(number)[2:]
        if(ans != previous):
            temp = qr.get_context(ans)
            flag = -1 
            if temp[-1]==0:
                qr.sendSMS(number,temp[0])
                print("SENT :",temp[0])
                print("*"*80)
                response =  [number,temp[0]]
                flag = 0 
            else:
                flag = temp[-1]
                response = temp[:-1] 
            if flag == 2:
                data = rd.google_directions(response[0],response[1],response[2])
                qr.sendSMS(number,data)
                print("SENT :",data)
                print("*"*80)
            elif flag == 3:
                data = rd.process_detail(response[0])
                qr.sendSMS(number,"ADDRESS: \n"+data)
                print("SENT :",data)
                print("*"*80)
            elif flag:
                pincode = response[0]
                query = response[1]
                contact = number
                # pin code conv .
                data = rd.retreive_area(placename[str(pincode)],query)
                if len(data) == 1:
                    qr.sendSMS(number,data)
                    print("SENT :",data)
                    print("*"*80)
                elif data != None:
                    if data[1]!=None:
                        data = data[0]+"\n"+data[1]+"\n"+data[2]
                    else:
                        data = data[0]+"\n"+data[2]
                    print("SENT :",data)
                    print("*"*80)
                    qr.sendSMS(number,data)
            print("Message Sent : app.py")
            previous = ans
        time.sleep(5)

if __name__ == "__main__":
    app.run(debug=True,port=8080)
