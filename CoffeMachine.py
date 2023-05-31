remain_coffee = 10 #남은 커피양
remain_money=10000 #남은 거스름돈
coffee_fee=300     #커피 한개 가격

user_input_money=0 #사용자가 지불한 돈
user_want_count=0  #사용자가 원하는 양
real_user_receive=0#사용자가 진짜 가져간 양

return_money=0     #거스름

while(remain_coffee >= 0):
    #커피 자판기 상태 출력
    print("="*30)
    print("자판기 거스름 돈 여유분", remain_money)
    print("커피 남은 개수", remain_coffee)
    print("=" * 30)
    print("")
    print("")

    user_input_money = int(input("돈을 넣으세요. : "))
    user_want_count = int(input("커피 개수를 입력하세요.: "))



    if user_input_money < 300:
        print("당신은 한개도 못삽니다. 돌아가세요.")
        continue

    #(해당 과정을 통해 분수에 맞게 살 수 있도록 조정됨)
    while(user_input_money - (coffee_fee * user_want_count) < 0):
        user_want_count -= 1

    #(팔다가 커피가 다 떨어질 수 있으니까 하나씩 빼주면서 체크)
    real_user_receive = 0
    while(user_want_count > 0):
        real_user_receive += 1
        user_want_count -=1
        remain_coffee -= 1


        if remain_coffee == 0:
            return_money = user_input_money - (300 * real_user_receive)
            print("%d 개의 커피를 드립니다. 거스름 돈은 %d 원 입니다." % (real_user_receive, return_money))
            print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
            break

    if remain_coffee == 0:
        break

    #(거스름돈을 계산하자)
    return_money = user_input_money - (300 * real_user_receive)
    print("%d 개의 커피를 드립니다. 거스름 돈은 %d 원 입니다." %(real_user_receive,return_money))

    #(빠져나간 만큼 업데이트 해주기)
    remain_money -= return_money
