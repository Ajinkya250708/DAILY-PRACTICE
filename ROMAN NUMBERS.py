
n=int(input("Enter a Number:"))



if n<1 or n>3999:
    print("Invalid input")
else:
    th=n//1000
    hun=(n%1000)//100
    ten=(n%100)//10
    one=n%10
    
    ans=""
    
    ans+="M"*th
    
    if hun==9:
        ans+="CM"
    elif hun==4:
        ans+="CD"
    elif hun>=5:
        ans+="D"+"C"*(hun-5)
    else:
        ans+="C"*hun
        
        
    if ten==9:
        ans+="XC"
    elif ten==4:
        ans+="XL"
    elif ten>=5:
        ans+="L"+"X"*(ten-5)
    else:
        ans+="X"*ten
        
        
    if one==9:
        ans+="IX"
    elif one==4:
        ans+="IV"
    elif one>=5:
        ans+="V"+"I"*(one-5)
    else:
        ans+="I"*one
        
    print(ans)
        
    