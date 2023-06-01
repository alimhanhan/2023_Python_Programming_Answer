year = 0
bal = 1000
interest = float(input('이자율: '))

while bal < 2000:
    year = year + 1
    final_inter = bal * interest
    bal = bal + final_inter

print('기간: ', year)
print('총액: ', bal)