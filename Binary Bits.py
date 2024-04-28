## 
 # @author Kashikizu
 # File Creation Date: 28/04/2024 (dd/mm/yyyy)
 # Initial Completion Date: 28/04/2024 
 ##

print("Decimal Numbers with two 1 bits:")
for i in range(5):
    for j in range(5):
        if(i != 0 | j != 0):
            x = pow(2, i)
            y = pow(2, j)
            print(y + x)