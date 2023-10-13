# Test 1
# import binascii
# from tkinter import filedialog

# file_path = filedialog.askopenfilename()

# x = ""
# with open(file_path, 'rb') as f:
#     for chunk in iter(lambda: f.read(32), b''):
#         x += str(binascii.hexlify(chunk)).replace("b","").replace("'","")
# b = bin(int(x, 16)).replace('b','')
# g = [b[i:i+2] for i in range(0, len(b), 2)]
# dna = ""
# for i in g:
#     if i == "00":
#         dna += "A"
#     elif i == "01":
#         dna += "T"
#     elif i == "10":
#         dna += "G"
#     elif i == "11":
#         dna += "C"
# print(x) #hexdump
# print(b) #converted to binary
# print(dna) #converted to "DNA"

#Test 2
# import math
# #"make a long test string"
# import numpy as np
# s=''.join((str(x) for x in np.random.randint(4,size=33)))\
#     .replace('0','A').replace('1','T').replace('2','G').replace('3','C')

# def store_(s):
#     size=len(s) #size will changed to fit 8*integer so remember true value of it and store with data
#     s2=s.replace('A','0').replace('T','0').replace('G','1').replace('C','1')\
#         .ljust( int(math.ceil(size/8.)*8),'0') #add '0' to 8xInt to the right
#     a=(hex( eval('0b'+s2[i*8:i*8+8]) )[2:].rjust(2,'0') for i in xrange(len(s2)/8))
#     return ''.join(a),size

# yourDataAsHexInText,sizeToStore=store_(s)
# print yourDataAsHexInText,sizeToStore


# def restore_(s,size=None):
#     if size==None: size=len(s)/2
#     a=( bin(eval('0x'+s[i*2:i*2+2]))[2:].rjust(8,'0') for i in xrange(len(s)/2))
#     #you loose information, remember?, so it`s only A or G
#     return (''.join(a).replace('1','G').replace('0','A') )[:size]

# restore_(yourDataAsHexInText,sizeToStore)


# print "so check it"
# print s ,"(input)"
# print store_(s)
# print s.replace('C','G').replace('T','A') ,"to compare with information loss"
# print restore_(*store_(s)),"restored"
# print s.replace('C','G').replace('T','A') == restore_(*store_(s))