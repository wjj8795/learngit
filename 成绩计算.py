score = float(input())
if score >= 0 and score < 60:
    print ("不及格")
elif score >= 60 and score < 70:
    print ("等级是D")
elif score >= 70 and score < 80:
    print ("等级是C")
elif score >= 80 and score < 90:
    print ("等级是B")
elif score >= 90 and score <= 100:
    print ("等级是A")