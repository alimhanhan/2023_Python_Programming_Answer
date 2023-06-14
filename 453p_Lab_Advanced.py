from tkinter import *
import random

answer = random.randint(1, 100)
tries = 0
max_tries = 10

def guessing():
    global tries
    guess = int(guessField.get())

    if guess > answer:
        msg = "높음!"
    elif guess < answer:
        msg = "낮음!"
    else:
        msg = "정답!"

    tries += 1
    if tries >= max_tries:
        msg = "\n게임 종료! 시도 횟수를 초과했습니다."
        tryButton.config(state=DISABLED)
    triesLabel["text"] = f"시도 횟수: {tries}/{max_tries}"
    resultLabel["text"] = msg
    guessField.delete(0, 5)

def reset():
    global answer, tries
    answer = random.randint(1, 100)
    tries = 0
    triesLabel["text"] = f"시도 횟수: {tries}/{max_tries}"
    resultLabel["text"] = "1부터 100사이의 숫자를 입력하시오."
    tryButton.config(state=NORMAL)

window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요!")
window.geometry("500x120")

titleLabel = Label(window, text="숫자 게임에 오신 것을 환영합니다!", bg="white")
titleLabel.pack()

guessField = Entry(window)
guessField.pack(side="left")
tryButton = Button(window, text="시도", fg="green", bg="white", command=guessing)
tryButton.pack(side="left")

resetButton = Button(window, text="초기화", fg="red", bg="white", command=reset)
resetButton.pack(side="left")

triesLabel = Label(window, text=f"시도 횟수: {tries}/{max_tries}", bg="white")
triesLabel.pack(side="left")

resultLabel = Label(window, text="1부터 100사이의 숫자를 입력하시오.", bg="white")
resultLabel.pack(side="left")

window.mainloop()