#!/usr/bin/avr python
# -*- coding: utf-8 -*-

#Info:
# program: simple resolv name/IP  and create or save in the file
# types IP and  argunment
# mathoian


#use argument name = sys.argv[1]

import sys
import socket


name = sys.argv[1]
print(sys.argv[1], " )))))) ", socket.gethostbyname(sys.argv[1]))
arq = open('resolved.txt', 'w')
texto = []
texto.append('# List name resolved # \n')
texto.append("name -> " + sys.argv[1])
texto.append(socket.gethostbyname(sys.argv[1]))
arq.writelines(texto)
arq.close()
