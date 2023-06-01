import random
import time

def make_list ():
	lotto_nums_lists = []
	for i in range(1, 46):
		lotto_nums_lists.append(i)
	return lotto_nums_lists

def lotto_shuffle_and_pick(nums_lists, s, max):
	print("Pleas wait a minute..")
	My_lotto_nums_lists = nums_lists
	sec = s
	secs = 0
	i = 1
	results = []
	while True:
		random.shuffle(My_lotto_nums_lists)
		time.sleep(sec)
		secs += 2

		if secs % 6 == 0:
			if i > max:
				break
			results.append(My_lotto_nums_lists.pop())
			i += 1

	return results

def print_lotto(lo):
	for i in lo:
		print(i, end=' ')
def lotto_number(max_choice):
	My_lotto_nums_lists = make_list()
	lotto = lotto_shuffle_and_pick(My_lotto_nums_lists, 0.5,max_choice)
	print_lotto(lotto)

def main():
	lotto_number(5)

# 작업할 때 굉장히 편해진다.
if __name__ == '__main__':
	main()



