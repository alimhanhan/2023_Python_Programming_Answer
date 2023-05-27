import time

now = time.localtime()
if (now.tm_mon >= 12) or (now.tm_mon <=2 ):
    print('추운 겨울입니다.')
elif now.tm_mon >= 9:
    print('청명한 가을입니다.')
elif now.tm_mon >= 6:
    print('무더운 여름입니다.')
elif now.tm_mon >= 3:
    print('산뜻한 봄입니다.')