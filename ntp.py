import socket
import sys

UDP_PORT=123
message="\xd3\x02\x03\xfa\x00\x01\x00\x00\x00\x01" \
        "\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\x00\x00\x00\x00\x00\x00" \
        "\x00\x00\xde\xad\xbe\xef"

if len(sys.argv)!=2: 
	print ("usage: python ntp.py <ip address>")
	sys.exit()
else:	
    UDP_IP=sys.argv[1]

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(message,(UDP_IP,UDP_PORT))

data,addr=sock.recvfrom(1024)

# transform string into int decimal, use . as seprator,display 2 places 
# you must convert 2xhexa digits into decimal - dont know how to do that

print ("[+] NTP peer of the remote ntp process is")
print '.'.join("{:02d}".format(ord(x)) for x in data[12:16])
