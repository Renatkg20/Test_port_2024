import socket
import time 

def isOpen(ip,port):
   t = time.ctime()
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
       s.connect((ip, int(port)))
       s.shutdown(2)
       return f"Port {port} is open. \nTime: {t}"
   except:
       return f"Port {port} is close. \nTime: {t}"

def send_message():
  print("something is wrong")

# while True:
#   port1 = isOpen("92.62.72.167", "10012")
#   if port1 == "Port 10012 is close":
#       send_message()
#   else:
#     pass
print(isOpen("92.62.72.167", "10012"))
 