import xml.dom.minidom 
from utilities import *
from models import WCMsg,WCUser

class wcMsg:
    """Base Class for WeChat Message"""
    #__datastr = u''
    msgID = u''
    msgTimeStamp = u''
    msgFromCryptID = u''
    msgFromFakeID = u''
    msgType = MESSAGE_NULL
    msgHost = u''
    #msgText = u'' #default as text msg
    def __init__(self,msgType, msgFromCryptID,msgTimeStamp,msgID,msgHost):
        self.msgType = msgType
        self.msgFromCryptID = msgFromCryptID
        self.msgTimeStamp = msgTimeStamp
        self.msgID = msgID
        self.msgHost = msgHost
    
    def buildDbMsg(self):
        p = WCMsg()
        p.msgType = self.msgType
        p.msgFakeID = self.msgFromFakeID
        
        p.msgCrptID = self.msgFromCryptID
        p.msgTimestamp = self.msgTimeStamp
        p.msgID = self.msgID
        
        return p
        
class wcTextMsg(wcMsg):
    msgContent = ''
    def saveToDB(self,user):
        p = self.buildDbMsg()
        p.msgContent = self.msgContent
        p.msgFrom = user
        p.save()
        user.msgCount+=1
        user.save()
        
class wcLocMsg(wcMsg):
    lat = 0
    lon = 0
    def saveToDB(self,user):
        p = self.buildDbMsg()
        p.msgContent = 'lat=%s lon=%s'%(self.lat,self.lon)
        log(p.msgContent)
        p.msgFrom = user
        p.save()
        user.msgCount+=1
        user.save()
        
class wcRepsonse():
    resType = RESPONSE_NULL
    
class wcTextResponse():
    resContent = ''
    def __init__(self):
        self.resType = RESPONSE_TEXT