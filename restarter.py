# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 10:38:25 2016

@author: Steve
"""

"""
Check to see if an process is running. If not, restart.
Run this in a cron job
"""
import os, time, datetime
process_name= "YOUR_SCRIPT.py" # change this to the name of your process

while True:
    time.sleep(60)
    try:
        tmp = os.popen("ps -Af").read()
        #restart process if crashed
        if process_name not in tmp[:]:
            newprocess="nohup python %s &" % (process_name)
            os.system(newprocess)
            print "Restarted stream."
            print datetime.datetime.now()
    except:
        continue
  