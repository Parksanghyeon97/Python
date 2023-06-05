class Elevator:
    def __init__(self, total_floors):
        self.total_floors = total_floors
        self.current_floor = 1
        self.direction = "정지"

    def call_elevator(self, floor):
        # 호출된 층과 현재 층을 비교하여 이동 방향을 결정합니다.
        if floor == self.current_floor:
            print("이미 해당 층에 있습니다.")
        elif not 1 <= floor <= self.total_floors:
            print("존재하지 않는 층입니다.")
        else:
            self.direction = "상승" if floor > self.current_floor else "하강"
            print(f"{floor}층으로 이동 중...")
            # 현재 층과 호출된 층이 같을 때까지 이동합니다.
            while self.current_floor != floor:
                self.move()
            print("도착했습니다.")

    def move(self):
        # 이동 방향에 따라 현재 층을 증가 또는 감소시킵니다.
        self.current_floor += 1 if self.direction == "상승" else -1
        print(f"현재 {self.current_floor}층, {self.direction} 이동 중...")

    def display_properties(self):
        # 엘리베이터의 속성을 출력합니다.
        print("=== 엘리베이터 속성 ===")
        print(f"전체 층 수: {self.total_floors}")
        print(f"현재 층: {self.current_floor}")
        print(f"이동 방향: {self.direction}")
        print("=====================")


# 엘리베이터 객체 생성
elevator = Elevator(10)

# 엘리베이터 사용 예시
while True:
    elevator.display_properties()
    # 사용자로부터 이동할 층을 입력받습니다.
    user_want = input("몇 층으로 가시겠습니까? (종료하려면 'finish' 입력) ")
    if user_want == "finish":
        print("프로그램을 종료합니다.")
        break
    try:
        user_want = int(user_want)
        elevator.call_elevator(user_want)
    except ValueError:
        print("유효한 숫자를 입력해주세요.")
    print("=="*30)  # 구분선 추가