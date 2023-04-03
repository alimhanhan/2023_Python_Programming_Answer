init_book = 28000  #원가 2만 8000원
dis = 10/100  # 10% 할인

final_book = init_book - init_book*dis  # 할인 적용된 가격
number = 10  # 책 개수

total = final_book * number + 3000 + (number - 1) * 500  # 총 금액(배송비 포함)
print("총 비용은", total, "원 입니다.")
