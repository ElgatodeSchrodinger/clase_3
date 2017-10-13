import socket

sc=socket.socket()

sc.bind(("localhost",9999))
sc.listen(2)
sc2 , addr=sc.accept()
recibido=sc2.recv(1024)

f=open("holder.jpg","wb")
f.write(recibido)
f.close()
