# Function-Performance-Comparison
In this repository you can find a function that can be used to compare the run time of different functions 
The function takes in a list of functions and a list of numeric inputs of varying lengths. It will output both a summary table showing max, min, average runtime as well as difference between fastest and slowest run time. It also returns a table that shows the run time for all inputs for each function

**Example Input:** 

```python
inputs=[341,121234143121,12421391934431212414124112412323234343333333332111243412412424]

def my_solution(n): #define first test function
lst=[]
for letter in str(n):
lst.append(int(letter))
return sum(lst)

def code_wars_solution(n): #define second test function
return sum(map(int, str(n)))

def slow_solution(n): #define third test function
sum = 0
while n>9:
sum += n%10
n //= 10
return sum + n

def even_slower(n):
return n if n<9 else n%10 + digit_sum(n//10)

functions=[my_solution,code_wars_solution,slow_solution] 
