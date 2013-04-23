#coding:UTF-8
from wcData import *
from utilities import *
import urllib, urllib2, cookielib

class wcMsgProccessor:
    def parseMsg(self,wcMsg, WCUser):
    """Put your message processing code here"""
        
        #------------------processing---------------------------
        if (wcMsg.msgType == MESSAGE_TEXT):
            response = wcTextResponse()
            response.resContent = wcMsg.msgContent
            log(wcMsg.msgHost)
           
        
        #------------------------------------------------------
        return response #a string containing return string
