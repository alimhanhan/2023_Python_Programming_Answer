from tkinter import *

# 버튼을 선택할 수 있는지 여부 검사 --> 선택 가능하면 o,x 표시
def checked(i):
    global player
    button = list[i]

    # 사용자가 선택할 수 없는 버튼을 누를 경우 아무 행동도 취하지 않고 리턴
    if button["text"] != "            ":
        return

    button["text"] = "     " + player + "      "
    button["bg"] = "yellow"

    if player == "X":
        button["bg"] = "yellow"
    else:
        button["bg"] = "lightgreen"

    # 승패가 갈렸는지 확인
    if (list[0]["text"] == list[1]["text"] == list[2]["text"] != "            " or
            list[3]["text"] == list[4]["text"] == list[5]["text"] != "            " or
            list[6]["text"] == list[7]["text"] == list[8]["text"] != "            " or
            list[0]["text"] == list[3]["text"] == list[6]["text"] != "            " or
            list[1]["text"] == list[4]["text"] == list[7]["text"] != "            " or
            list[2]["text"] == list[5]["text"] == list[8]["text"] != "            " or
            list[0]["text"] == list[4]["text"] == list[8]["text"] != "            " or
            list[2]["text"] == list[4]["text"] == list[6]["text"] != "            "):
        # 승패가 갈리면 승자 출력
        message = player + " 승리!"
        for b in list:
            b["state"] = "disabled"
        status.config(text=message)
        if player == "X":
            player = "O"
        else:
            player = "X"
    elif all(button["text"] != "            " for button in list):
        # 비긴 경우
        message = "비겼습니다."
        status.config(text=message)
    else:
        # 이제 누구 차례인지 출력
        if player == "X":
            player = "O"
        else:
            player = "X"
        message = player + "의 차례입니다."
        status.config(text=message)

window = Tk()  # 윈도우 생성
player = "X" # 시작 플레이어는 x
list = []

for i in range(9):
    b = Button(window, text="            ", command=lambda k=i: checked(k))
    b.grid(row=i // 3, column=i % 3)
    list.append(b)

status = Label(window, text="x의 차례입니다.", font=("Helvetica", 14))
status.grid(row=3, column=0, columnspan=3)

window.mainloop()