class Coffee:
    def __init__(self):
        self.total_amount = 10
        self.total_amount_price = 5000
        self.coffee_price = 300
        self.put_price = 0
        self.req_coffee_nums = 0
        self.remaining_price = 0

    def request(self):
        self.put_price = int(input("돈을 넣으세요: "))
        self.req_coffee_nums = int(input("커피 개수를 입력하세요: "))

    def get(self):
        if self.put_price < self.coffee_price:
            print("당신은 한 개도 못삽니다. 돌아가세요.")
            return

        user_want_count = self.put_price // self.coffee_price

        if user_want_count > self.req_coffee_nums:
            user_want_count = self.req_coffee_nums

        if user_want_count > self.total_amount:
            user_want_count = self.total_amount

        self.remaining_price = self.put_price - (self.coffee_price * user_want_count)
        self.total_amount -= user_want_count

        if self.total_amount == 0:
            print(f"{user_want_count} 개의 커피를 드립니다. 거스름 돈은 {self.remaining_price} 원 입니다.")
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            exit()
        else:
            print(f"{user_want_count} 개의 커피를 드립니다. 거스름 돈은 {self.remaining_price} 원 입니다.")
            self.total_amount_price -= self.remaining_price

    def info(self):
        print("==" * 15)
        print("자판기 거스름돈 여유분:", self.total_amount_price, "원")
        print("커피 남은 개수:", self.total_amount, "개")
        print("==" * 15)

    def check_amount(self):
        if self.total_amount_price < 0:
            print("자판기 작동 중입니다.")
            print("거스름돈이 없습니다. 판매를 중지합니다.")
            exit()
        elif self.total_amount == 0:
            print("자판기 작동 중입니다.")
            print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
            exit()
        else:
            print("자판기 작동 중입니다.")


# 테스트 코드
coffee_machine = Coffee()

while True:
    coffee_machine.info()
    coffee_machine.request()
    coffee_machine.get()
    coffee_machine.check_amount()
