#a program that asks a user to in

def isnumberpositive(number):
    if number>0:
        return False
    number=int(input("enter the positive number"))
    
    def isprimenumber(prime):
        if prime<=number:
            for i in range(2,int(number**0.5)+1):
                if number%i==0:
                    return i
     
          
        
    

    
    
    