# -*- coding: UTF-8 -*-

import os 
import subprocess
import datetime

#Variable
web_adr = str(input("Web address or IP(by default is www.google.com): "))
if web_adr == "":
    web_adr = "www.google.com"

packet_amount = str(input("Packet amount(by default is 1000 packets): "))
if packet_amount == "":
    packet_amount = str(1000)

packet_size  = str(input("Packet size(by default is 32 bytes): "))
if packet_size  == "":
    packet_size  = str(32)

str_amount  = str(input("Stress System(by default is 0): "))
if str_amount  == "":
    str_amount  = str(0)

#Date
date = datetime.datetime.now()
datetime_format = date.strftime("%Y%m%d_%H%M%S")

#Log_dir
log_path = os.getcwd() +"\Log"
if not os.path.isdir(log_path):
    os.makedirs(log_path, mode=0o777) 

#Export
file_name = "Log_" + datetime_format + ".txt"
file_position = log_path+ "\\" +file_name


#Log
with open(file_position, "a") as file:
    file.write('---------------------------------------------------------------\n')
    file.write("Date: "+ str(date))
    file.write("\nWeb_address: " + web_adr +
      "\nPacket_amount: "+ packet_amount +
      "\nPacket_size: "+ packet_size +
      "\nStress_amount: "+ str_amount
      )
    file.write('\n---------------------------------------------------------------\n')
    file.close()

#Stress_System
for i in range(int(str_amount)):
    os.system("ping " + web_adr + " -n " + packet_amount)

#Main_System
cmd = "ping " + web_adr + " -n " + packet_amount + " -l " + packet_size
context = open(file_position, "a") 
subprocess.run(cmd, stdout=context) 

#Log_modify
log = open(file_position)
lines = log.readlines()
del lines[7:-5]


#Wait
print(file_position)
