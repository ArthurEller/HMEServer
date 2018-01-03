import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print '\033[0;32m'+"""\n                                                             
____    ______       ____________   ____                                              
`MM'    `MM`MMb     dMM`MMMMMMMMM  6MMMMb\                                            
 MM      MM MMM.   ,PMM MM      \ 6M'    `                                            
 MM      MM M`Mb   d'MM MM        MM         ____  ___  __ ____    ___  ____  ___  __ 
 MM      MM M YM. ,P MM MM    ,   YM.       6MMMMb `MM 6MM `MM(    )M' 6MMMMb `MM 6MM 
 MMMMMMMMMM M `Mb d' MM MMMMMMM    YMMMMb  6M'  `Mb MM69 "  `Mb    d' 6M'  `Mb MM69 " 
 MM      MM M  YM.P  MM MM    `        `Mb MM    MM MM'      YM.  ,P  MM    MM MM'    
 MM      MM M  `Mb'  MM MM              MM MMMMMMMM MM        MM  M   MMMMMMMM MM     
 MM      MM M   YP   MM MM              MM MM       MM        `Mbd'   MM       MM     
 MM      MM M   `'   MM MM      / L    ,M9 YM    d9 MM         YMP    YM    d9 MM     
_MM_    _MM_M_      _MM_MMMMMMMMM MYMMMM9   YMMMM9 _MM_         M      YMMMM9 _MM_    v1.0

HMEServer_Hosting Application v1.0 by ArthurHMES
Twitter: @Thuur1337     Github: https://github.com/ArthurHMES/

""" + '\033 [0;0m'

ip = "0.0.0.0"
porta = raw_input("Porta para criar o servidor: ")
s = server.bind((ip,int(porta) ))


try:

    server.listen (5)
    print "Listening in: " +ip+":"+str(porta)

    (client_socket, adress) = server.accept()

    print "Received from: " + adress[0]

    while True:
        data = client_socket.recv(1024)
        arq = open(raw_input("Okay, arquivo recebido, salvar como: "), 'w')
        server.close


        if not data:
            break
        arq.write(data)
        server.close


except Exception as Error:
    print str(Error)
    server.close()
