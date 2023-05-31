user_num = int(input("구구단: "))

for i in range(1,10):
    if i % 2 == 0:
        continue
    else:
        print("%d x %d = %d" %(user_num,i,user_num*i))

