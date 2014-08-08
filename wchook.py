import xml.dom.minidom 
from utilities import *
from models import WCMsg,WCUser
from wcData import * 
from wcMsgProc import wcMsgProccessor            

class wcInfoHandler:
    """A simple handler for wechat message"""
    
    def respondMsg(self,rawStr):
        """main method handling message"""
        #logging.info(rawStr)

        msg = self.retrieveMsgContent(rawStr)
        user = self.validateUser(msg.msgFromCryptID);
        msg.saveToDB(user)
        
        proccessor = wcMsgProccessor()
        response = proccessor.parseMsg(msg,user)
        
        return self.compResponseMsg(response, msg)
        
    
    def getTagContent(self,root,tag):
        return root.getElementsByTagName(tag)[0].firstChild.nodeValue
    
    def retrieveMsgContent(self,rawStr):
        dom = xml.dom.minidom.parseString(rawStr)
        root = dom.documentElement
        
        #toUser = self.getTagContent(root, 'ToUserName')
        fromUser = self.getTagContent(root, 'FromUserName')
        timeStamp = self.getTagContent(root, 'CreateTime')
        msgHost = self.getTagContent(root, 'ToUserName')
        msgType = self.getTagContent(root,'MsgType')
        msgID = self.getTagContent(root,'MsgId')
        log(msgType)
        
        if (msgType=='text'):
            msg = wcTextMsg(MESSAGE_TEXT,fromUser,timeStamp,msgID,msgHost)
            msg.msgContent = self.getTagContent(root, 'Content')
            return msg
        elif(msgType=='location'):
            msg = wcLocMsg(MESSAGE_LOC,fromUser,timeStamp,msgID,msgHost)
            msg.lat = self.getTagContent(root, 'Location_X')
            #log(msg.msgType)
            msg.lon = self.getTagContent(root, 'Location_Y')
            return msg
    
    def validateUser(self,crptID):
        try:
            user = WCUser.objects.get(crptID__iexact=crptID)
            return user
        except:
            user = WCUser()
            user.crptID = crptID
            user.msgCount = 0
            user.save()
            return user
    
    def compResponseMsg(self,response,msg):
        impl = xml.dom.minidom.getDOMImplementation()
        dom = impl.createDocument(None, 'xml', None)
        root = dom.documentElement
        root.appendChild(self.buildXMLnode(dom, 'ToUserName', msg.msgFromCryptID, 'cdata'))
        root.appendChild(self.buildXMLnode(dom, 'FromUserName', msg.msgHost, 'cdata'))
        root.appendChild(self.buildXMLnode(dom, 'CreateTime', msg.msgTimeStamp, 'text'))
        root.appendChild(self.buildXMLnode(dom, 'MsgType', 'text', 'cdata'))
        
        #add content
        if(response.resType==RESPONSE_TEXT):
            content = response.resContent
            root.appendChild(self.buildXMLnode(dom, 'Content', content, 'cdata'))
 

        
        root.appendChild(self.buildXMLnode(dom, 'FuncFlag', '0', 'text'))
            #output
        return root.toxml()
        
        
    def buildXMLnode(self,dom,tag,content,type):
        node = dom.createElement(tag)
        if (type == 'cdata'):
            value = dom.createCDATASection(content)
        elif(type == 'text'):
            value = dom.createTextNode(content)
        
        node.appendChild(value)
        return node
            
        

        
    
