from time import sleep
from threading import*
value=input("enter the string")
i=0
upper=0
lower=0

class hello (Thread):
    def run (self):
        
        for i in range(len(value)):
            if value[i]>='A' and value[i]<='Z':
                i+=1 
                print("upper")
            elif value[i]>='a' and value[i]<='z':
                i+=1
                print("lower")
                
            
class hi(Thread):
    def run (self):
        
        for i in range(len(value)):
            if value[i]>='A' and value[i]<='Z':
                i+=1 
                print("upper")
            elif value[i]>='a' and value[i]<='z':
                i+=1
                print("lower")
                                
                


t1=hello()
t2=hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()


print("bye")
            
