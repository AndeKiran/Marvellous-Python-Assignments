def ChkPrime(value): #function to check given number is prime or not 
    for a in range(2,value+1):
        if(value%a == 0):
            if((a!=value)):
                #If "Number is not prime"
                return False
                break
            else:
                # If "Number is prime"
                return True
                break
    