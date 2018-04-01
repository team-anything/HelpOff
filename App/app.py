import query_retreive as qr
import retreiveData as rd
import send_sms 
import time

if __name__=="__main__":
    previous = []
    while(1):
        response = qr.response()
        if(response != previous):
            print(response,previous)
            pincode = response[0]
            search_type = response[1]
            query = response[2]
            contact = response[3]   
            # pin code conv .
            placename = "Dahisar,Mumbai" # 
            data = rd.retreive_area(placename,query)
            print(data)
            if data != None:
                text = data[0]+"\n"+data[1]+"\n"+data[0]
                send_sms.send_data_sms(text,str(contact)[2:])

        previous  = response    
        time.sleep(5)
