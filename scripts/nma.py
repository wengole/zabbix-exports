#!/bin/env python2
import sys
import requests
import logging


logger = logging.getLogger('Zabbix NMA script')
logFile = logging.FileHandler('/tmp/nma-script.log')
logger.addHandler(logFile)

apikey = sys.argv[1]
subject =sys.argv[2]
message = sys.argv[3]

params = {
    'apikey': apikey,
    'application': 'Zabbix',
    'event': subject,
    'description': message,
    'priority': 0,
}
r = requests.post('https://www.notifymyandroid.com/publicapi/notify')

logger.info(subject)
logger.info(message)
logger.info(r.status_code)