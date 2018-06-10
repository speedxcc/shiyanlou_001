import socket,sys
from getopt import getopt


def judge_host(host):
    point = 0
    for x in host:
        if x == ".":
            point +=1
        elif x not in ['1','2','3','4','5','6','7','8','9','0']:
            print("Parameter Error1")
            sys.exit()
    if point != 3:
    	print("Parameter Error2")
    	sys.exit()
    return host

def judge_port(port):
    new_port = [port]
    for i,x in enumerate(port):
        if x == "-":
            start = int(port[:i])
            end = int(port[i+1:])
            new_port = list(range(start,end+1))
            break
        elif x.isdigit() == False:
            print("Parameter Error")
            sys.exit() 
  #  print(new_port)
    return new_port

if len(sys.argv) != 5:
	print('Parameter Error5')
	sys.exit()
try:
	opts,args = getopt(sys.argv[1:],"",["host=","port="])
except:
	print("Parameter Error6")
	sys.exit()


for a,b in opts:
	if a in ['--host']:
		host = judge_host(b)
	if a in ['--port']:
		port = judge_port(b)
   
#print(host,port)

sock = socket.socket()
sock.settimeout(0.05)

for port in port:
    try:
	    sock.connect((host,int(port)))
	    print(port,'open')
    except:
        print(port,'close')




#