initial_number = 1234

deadline = 0
while(True):

    user_input = int(input("비밀번호 입력: "))

    if user_input == initial_number:
        print("맞았습니다. 현관문이 열렸습니다.")
        break
    else:
        deadline += 1

        if (deadline == 5):
            print("시도 횟수 초과 문 잠김")
            break

        print("틀렸습니다. 다시 입력하세요.")

