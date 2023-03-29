# 복리 계산기

init_money = int(input("원금을 입력하시오: "))
years = int(input("투자 기간을 입력하시오: "))
interest = float(input("이율을 입력하시오: "))

print("복리로 원리금을 계산한 결과는", init_money*(1+interest)**years, "입니다.")