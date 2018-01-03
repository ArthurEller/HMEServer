import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)
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

HMEServer_Server Application v1.0 by ArthurHMES
Twitter: @Thuur1337     Github: https://github.com/ArthurHMES/

""" + '\033[0;0m'


ip = raw_input("Qual IP do servidor?")
porta = raw_input("Qual a porta do servidor?")


try:

    client.connect((ip, int(porta)))
    arqv = raw_input("Onde esta localizado o arquivo que voce quer enviar? ")
    arq = open(arqv, 'r')

    for i in arq.readlines():
        client.send(i)
        print "Arquivo enviado com sucesso"
        server.close
    else:
        print "Tivemos uma falha ao enviar o arquivo."
        server.close

except:
    print "Conexao falhou"
    server.close
    