def saveData():
    f=open("Data.csv","r")
    l=len(f.readlines())-1
    f.seek(0,0)
    a=True
    d=[]
    while(l!=0):
       st=f.readline().split(",")
       string="IP Header: "+st[0]+"\nTTL: "+st[1]+"\nProtocol: "+st[2]+"\nSource IP Address: "+st[3]+"\nDestination IP Address: "+st[4]+"\nSource Port: "+st[5]+"\nDestination Port: "+st[6]+"\nSequence: "+st[7]+"\nAcknowlewdge no: "+st[8]+"\nTCP Header: "+st[9]
       d.append(string)
       print(string)
       l-=1
    '''f.write('IP Header Length,')
    f.write('TTL,')
    f.write('Protocol,')
    f.write("Source IP Address,")
    f.write('Destination IP Address,')
    f.write("Source Port,")
    f.write("Destination Port,")
    f.write('Sequence,')
    f.write('Acknowledge,')
    f.write('TCP Header Length')
    f.write("\n")
    '''
#print("Version: {} IP Header Length: {} TTL: {} Protocol: {} \nSource Address: {} Dest. Address: {}".format(version,ihl,ttl,protocol,s_addr,d_addr))
#print("Source Port: {} Dest Port: {} Sequence: {} Acknowledge: {} TCP Header Length: {}".format(source_port,dest_port,sequence,acknowledgement,tcph_length))
saveData()
