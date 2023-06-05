class Fridge:
	isOpened = False		# 냉장고 문이 열렸는지 닫혔는지를 나타내는 값(처음은 닫혀 있다.)
	foods = []			# 냉장고 안의 음식(처음은 비어 있다.)

	def open(self):		# 냉장고 문 열기
		self.isOpened = True
		print('냉장고 문을 열었어요')

	def put(self, thing):	# 냉장고에 음식 넣기
		if self.isOpened:
			self.foods.append(thing)
			print(f'냉장고 속에 {thing} 음식이 들어 갔네요')
		else:
			print('냉장고 문이 닫혀 있어서 못 넣겠네요')

	def close(self):		# 냉장고 문 닫기
		self.isOpened = False
		print('냉장고 문을 닫았어요')


class Food:
	pass	               # 아무런 동작을 하지 않는다.