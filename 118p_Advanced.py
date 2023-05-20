score = int(input('성적: '))

if score >= 95:
    print('성적: A+')
elif score >= 90 and score < 95:
    print('성적: A0')
elif score >= 80 and score < 90:
    print('성적: B')
elif score >= 70 and score < 80:
    print('성적: C')
elif score >= 60 and score < 70:
    print('성적: D')
else:
    print('성적: F')