import binascii
from machine import Pin
def convertTuple(tup):
    st = ''.join(map(str, tup))
    return st

# Python code to convert from Binary
# to Hexadecimal using int() and hex()
def binToHexa(n):
   
    # convert binary to int
    num = int(n, 2)
     
    # convert int to hexadecimal
    hex_num = hex(num)
    return(hex_num)
# Driver code
D0 = Pin(13,Pin.IN)
D1 = Pin(12,Pin.IN)
D2 = Pin(14,Pin.IN)
D3 = Pin(27,Pin.IN)
D4 = Pin(26,Pin.IN)
D5 = Pin(25,Pin.IN)
D6 = Pin(33,Pin.IN)
D7 = Pin(35,Pin.IN)
CLK = Pin(15, Pin.OUT)
ADDR = 0
romsize = 32*1024
while ADDR < romsize:
    CLK.value(0)
    data = (D0.value(),D1.value(),D2.value(),D3.value(),D4.value(),D5.value(),D6.value(),D7.value())
    
    bindata = convertTuple(data)
    hexdata = binToHexa((convertTuple(data)))
    #asciidata = binascii.unhexlify(hexdata[2:])
    print('Address:     Data:')
    print(hex(ADDR),'      ',hexdata) 
   
    #print('Address:', hex(ADDR))
    #print('bin:',bindata)
    #print('hex:',hexdata)
    
    #print('ascii:', asciidata)
    CLK.value(1)
    ADDR +=1

