# -*- coding: UTF-8 -*-
#Code By JRay 20230321

import os 
import subprocess
import datetime

#Variable
web_adr = str("www.google.com")
packet_amount = str(input("Packet Amount: "))
packet_size = str(32)
str_amount = str(0)
path = os.getcwd() +"\Log"

#Date
date = datetime.datetime.now()
datetime_format = date.strftime("%Y%m%d_%H%M")

#Log_dir
if not os.path.isdir(path):
    os.makedirs(path, mode=0o777) 

#Export
file_name = "Log_" + datetime_format + ".txt"
file_position = path+ "\\" +file_name

#Log
with open(file_position, "w") as file:
    file.write('---------------------------------------------------------------\n')
    file.write("Date: "+ str(date))
    file.write("\nWeb_address: " + web_adr +
      "\nPacket_amount: "+ packet_amount +
      "\nPacket_size: "+ packet_size +
      "\nStress_amount: "+ str_amount
      )
    file.write('\n---------------------------------------------------------------\n')

#Main
cmd = "ping " + web_adr + " -n " + packet_amount + " -l " + packet_size
context = open(file_position, "a") 
subprocess.run(cmd, stdout=context) 




print(path)
