WechatPy
========

#A python interface to connect wechat public platform

---------------------------------------

##Features

* Easy to install - just import class from python file
* Updating - I will update frequently
* Other function - Please contact me for other functional modules, for example sending message to user without call from wechat.

----------------------------------------

##Usage

Put the file into your application folder, then call the interface according to your app framework. Generally, is you 
get the request XML file you should call the interface like

```Python
from wchooker import wcInfoHandler
handler = wcInfoHandler()
responseMsg = handler.respondMsg(rawStr) #rawStr is the raw xml from wechat platform
```

Then you should modify the file "wcMsgProc.py" as

```Python
#------------------processing---------------------------
      if (wcMsg.msgType == MESSAGE_TEXT):
      response = wcTextResponse()
      response.resContent = wcMsg.msgContent
      log(wcMsg.msgHost)
           
      #add yourselves' handling code here
      #please see "wcData.py" for the structure of the class wcMsg
      #The return content should be set to response.resContent
#------------------------------------------------------
      return response 
```
