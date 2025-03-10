number = int(input())
reshte = input( )
s1, s2, s3 = "", "", ""
for i in reshte : 
    if i=='0' :
        s1+="***"
        s2+= "*.*"
        s3+="***"

    elif i=='1':
        s1+= ".*."
        s2+= ".*."
        s3+= ".*."
    
print(s1)
print(s2)
print(s3)