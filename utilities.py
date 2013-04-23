import os
import sys
import re

def log(str):
    if 'SERVER_SOFTWARE' in os.environ:
        from bae.api import logging
        logging.info(str)
    else:
        print str
        
MESSAGE_TEXT = 1
MESSAGE_IMG =2
MESSAGE_SOUND =3
MESSAGE_NULL =0

RESPONSE_NULL=0
RESPONSE_TEXT=1

def matchStr(input,regexp):
    match = re.search(regexp, input)
    if match:
        return match.group(0)
    else:
        return ''
