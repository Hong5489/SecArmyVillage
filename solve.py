message = [11, 29, 27 ,25 ,10 ,21 ,1 ,0 ,23 ,10 ,17, 12 ,13 ,8]
print(''.join([chr(t^ord('x')) for t in message]))