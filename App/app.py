import query_retreive as qr
import retreiveData as rd
import time,pickle

if __name__=="__main__":
    previous = []
    file = open("./aipc.pickle","rb")
    placename = pickle.load(file)
    file.close()
    while(1):
        response = qr.response()
        if(response != previous):
            print(response,previous)
            pincode = response[0]
            search_type = response[1]
            query = response[2]
            contact = response[3]   
            # pin code conv .
            print(placename[str(pincode)])
            data = rd.retreive_area(placename[str(pincode)],query)
            print(data)
            if data != None:
                text = data[0]+"\n"+data[1]+"\n"+data[2]
                #qr.sendSMS(str(contact)[2:],text)
                print("Message Sent : app.py")
        previous  = response    
        time.sleep(5)
