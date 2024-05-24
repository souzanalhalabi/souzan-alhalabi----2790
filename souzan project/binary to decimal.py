def is_binary(num):
    try:
        int(num, 2)
        return True
    except ValueError:
         return False
def main():
   B = input("Enter a binary number: ")
   if is_binary(B):
      D = 0
      for i in range(len(B)):
          if B[i] == '1':
             D = D + 2**(len(B)-i-1) 
      print("The decimal of the number is",D)
   else:
      print("The enterd number is invalid format,please enter a binary number")

main()

