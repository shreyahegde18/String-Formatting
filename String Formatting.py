def print_formatted(number):
    # your code goes here
    n=number
    w=len(bin(n)[2:])
    
    for i in range(1,n+1):
        d = f'{i}' #typecasting
        print(d.rjust(w)+oct(i)[2:].rjust(w+1)+hex(i)[2:].rjust(w+1).upper()+bin(i)[2:].rjust(w+1))
        
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)