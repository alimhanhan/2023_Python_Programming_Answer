itemprice = int(input("물건값을 입력하시오: "))
note = int(input("1000원 지폐 개수: "))
coin500 = int(input("500원 동전 개수: "))
coin100 = int(input("100원 동전 개수: "))

change = note*1000 + coin500*500 + coin100*100 - itemprice

ncoin500 = change//500
change = change % 500

ncoin100 = change//100
change = change % 100

ncoin10 = change//10
change = change % 10

ncoin1 = change

print("500원: ", ncoin500, "100원: ", ncoin100, "10원: ", ncoin10, "1원: ", ncoin1)