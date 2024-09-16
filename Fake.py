
from faker import Faker
import time

f = Faker()

f.name()
f.email()
f.password()

print ("\n"+"Successful Operation !! "+"\n"+"......""\n"+"")
 

name = f.name()
Email = f.email()
password = f.password()

print("name : "+ name +"\n"+"Email : "+ Email +"\n"+"Password : "+ password +"\n"+"......."+"\n"+"\n"+"BD-Dedsec""\n")

time.sleep(1)

           