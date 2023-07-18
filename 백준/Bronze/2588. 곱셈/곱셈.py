A = int(input())
B = int(input())

result1 = A * (B % 10)   
result2 = A * ((B // 10) % 10) 
result3 = A * (B // 100)  
result4 = A * B 

print(result1)
print(result2)
print(result3)
print(result4)