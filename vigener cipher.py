message=input("enter the message:")
letters='abcdefghijklmnopqrstuvwxyz'
k=input("enter the value:")
ct=''
n=0
x=len(message)
y=len(k)
for i in range(0,x):
    temp=message[i]
    p=k[i]
    if(temp==" " and p==" "):
        ct=ct+" "
    elif(temp.isupper() and p.isupper()):
        ct+=chr((ord(temp)+ord(p)-65)%26+65)
    else:
        ct+=chr((ord(temp)+ord(p)-97)%26+97)
print("cipher text of given message is:"+ct)
    
            
