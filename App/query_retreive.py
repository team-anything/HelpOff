import urllib.request
import urllib.parse
import codecs
import json,re
import apiai

Access_token = "fbef6a5e857a475d89cccbdb61804ba8"
client=apiai.ApiAI(Access_token)

def get_context(message):
    req=client.text_request()
    req.lang="de"
    req.session_id="<SESSION ID, UNIQUE FOR EACH USER>"
    req.query=message
    response=json.loads(req.getresponse().read().decode('utf-8'))
    responseStatus = response['status']['code']
    if responseStatus==200 :
        text = response['result']['fulfillment']['speech']
    else:
        text="No Match Found"
    result=response["result"]
    param=result["parameters"]
    if len(param.keys())==0:
        return [text,0]
    if "number" in param.keys():
        pin=param["number"]
    if "tof" in param.keys():
        tof=param["tof"]
    if "type" in param.keys():
        typ=param["type"]
        if typ=="routes":
            message=message.split("\n")
            if(len(message)>3):
                mod=message[3]
            else:
                mod='transit'
            return [message[1],message[2],mod,2]
        elif typ=="nearby":
            return [pin,tof,typ,1]

def getInboxes(apikey):
    data =  urllib.parse.urlencode({'apikey': apikey})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/get_inboxes/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)


def getMessages(apikey, inboxID):
    data =  urllib.parse.urlencode({'apikey': apikey, 'inbox_id' : inboxID})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/get_messages/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

def sendSMS(number, message):
    apikey= 'lY0QfNF6OU8-treTNMuE2I05MdjqKZK0yHDlhsjIX2'
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': number,
        'message' : message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    print("MESSAGE SENT")

def response():
    resp = getMessages('lY0QfNF6OU8-treTNMuE2I05MdjqKZK0yHDlhsjIX2', '10')
    ans = json.loads(resp.decode('ASCII'))
    #print(get_context(ans["messages"][-1]["message"][6:])+[ans["messages"][-1]["number"]])
    x = ans["messages"][-1]["message"][6:]
    y = ans["messages"][-1]["number"]
    return x,y
    #
    
