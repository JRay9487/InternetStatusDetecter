import datetime

date = datetime.datetime.now()
datetime_format = date.strftime("%Y%m%d_%H%M")
file_name = "Log_" + datetime_format

print(file_name)
