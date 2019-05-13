def turnOnBits(no,pos,noofbits):
   x = 2**noofbits - 1
   x = x << (pos - noofbits)
   return no | x

def toggleOnBits(no,pos,noofbits):
   x = 2**noofbits - 1
   x = x << (pos - noofbits)
   return no ^ x

def turnOffBits(no,pos,noofbits):
   x = 2**noofbits - 1
   x = x << (pos - noofbits)
   x = ~x
   return no & x

def main():
   no = eval(input("Enter no: "))
   pos = eval(input("Enter the bit position from which to turn off bits: "))
   bits = eval(input("Enter Number of bits to turn off: "))
   result = turnOffBits(no, pos, bits)
   print(result)

if __name__ == '__main__':
   main()
