for a in range(1,101):
    if(a == 7 or a % 7 == 0 or a // 10 == 0):
        continue
    else:
        print(a)
