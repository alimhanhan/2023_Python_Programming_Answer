phrase = input('문자열을 입력하시오: ')
phrase = phrase.replace("In","")
phrase = phrase.replace("The","")
phrase = phrase.replace("Of","")
phrase = phrase.replace("By","")

acro = ""

for word in phrase.upper().split():
        acro += word[0]

print(acro)