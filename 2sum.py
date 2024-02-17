#2.	Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690


n=5
series_sum=1
term=2

for i in range(n):
    series_sum+=term
    term=term*10+2

print(series_sum)