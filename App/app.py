import query_retreive as qr
import retreiveData as rd
import time,pickle

if __name__=="__main__":
    previous = ""
    file = open("./aipc.pickle","rb")
    placename = pickle.load(file)
    file.close()
    while(1):
        ans,number = qr.response()
        if(ans != previous):
            temp = qr.get_context(ans)
            flag = -1 
            if temp[-1]==0:
                #sendSMS(number,temp[0])
                response =  [number,temp[0]]
                flag = 0 
            else:
                flag = temp[-1]
                response = temp[:-1] 
            print(response,flag)
            if not flag :
                # qr.sendSMS(number,response[0])
                print(response)
            elif flag == 2:
                data = rd.google_directions(response[0],response[1],response[2])
                # qr.sendSMS(number,data)
                print(data,"HERE")
            else:
                print(response,previous)
                pincode = response[0]
                query = response[1]
                search_type = response[2]
                contact = number
                # pin code conv .
                print(placename[str(pincode)])
                data = rd.retreive_area(placename[str(pincode)],query)
                print(data)
                if len(data)==1:
                    # qr.sendSMS(str(contact)[2:],data)
                    print("Message Sent : app.py")
                elif data != None:
                    if data[1]!=None:
                        text = data[0]+"\n"+data[1]+"\n"+data[2]
                    else:
                        text = data[0]+"\n"+data[2]
                    #qr.sendSMS(str(contact)[2:],text)
                    print("Message Sent : app.py")
            previous = ans
        time.sleep(5)
