import query_retreive as qr
import time

if __name__=="__main__":
	x=[]
	while(1):
		tp=qr.response()
		if(tp!=x):
			x=tp
		time.sleep(15)