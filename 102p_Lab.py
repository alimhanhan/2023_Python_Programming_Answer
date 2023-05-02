rain = input("현재 비가 오고 있나요?: ")
umbrella = input("우산을 가지고 있나요?: ")

if rain == 'yes':
    if umbrella == 'yes':
        print("외출할 수 있습니다.\n")
    else:
        print("잠시 기다리십시오.\n")
else:
    print("외출할 수 있습니다.\n")