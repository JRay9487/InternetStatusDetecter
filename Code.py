# -*- coding: UTF-8 -*-

#import
import os 
import subprocess
import datetime

#Variable
packet_amount = ""
packet_size = ""
str_amount = ""
web_adr = ""
    
#input
def inputvalue(var, text, default):
    var = str(input(text))
    if var == "":
        var = default
    return var

packet_amount = inputvalue(packet_amount,"Packet amount(by default is 1000 packets): ","1000")
packet_size = inputvalue(packet_size,"Packet size(by default is 32 bytes): ","32")
str_amount = inputvalue(str_amount,"Stress System(by default is 0):!!!NOT YET DEVELOP!!!! ","0")
web_adr = inputvalue(web_adr,"Web address or IP(by default is www.google.com): ","www.google.com")

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
