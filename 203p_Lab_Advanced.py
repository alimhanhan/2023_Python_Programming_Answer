def is_prime():
    prime_list = []

    for i in range(2, 101):
        for a in range(2, i + 1):
            if a == i:
                prime_list.append(i)
            if i % a == 0:
                break
                
    print(prime_list)

print('1부터 100 사이의 소수는 아래와 같습니다.')
is_prime()