import time
from datetime import datetime as dt

host_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites_list=[]

# input for names of website name to block
n=int(input("No. of website you want to ban="))
for a in range(n):
    website=input()
    websites_list.append(website)

# input for woking works
starttime=str(input("start time in HH Mm format- "))
endtime=str(input("end time in HH Mm format- "))

start_time=[int(b) for b in starttime.split()]
end_time=[int(b) for b in endtime.split()]

while True:
    #setting working hours
    if dt(dt.now().year,dt.now().month,dt.now().day,start_time[0],start_time[1])<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,end_time[0],end_time[1]):
        print("Working Hours ....")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    # writing the block website in host file
                    file.write(redirect+" "+website+"\n")
        time.sleep(10)
    else:
        print("Fun Hours......")
        with open(host_path,'r') as file:
            content=file.readline()
        # remove the block website from the host file
        with open(host_path,'w') as file:
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
        time.sleep(10)
    