import diablo2

jane = diablo2.Amazon()        	# jane 여전사 탄생
mary = diablo2.Amazon()       	# mary 여전사 탄생

print(jane.strength)          	# jane 여전사의 강도
print(jane.attack())

eve = diablo2.Amazon()         	# eve 여전사 탄생
eve.exercise()                	# eve 훈련시키기
print(eve.strength)			# eve 강도