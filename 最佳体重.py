height = float(input())
weight = float(input())
best = height - 105
if weight > best:
    print ("偏胖")
elif weight == best:
    print ("体重正常")
elif weight < best:
    print ("偏瘦")