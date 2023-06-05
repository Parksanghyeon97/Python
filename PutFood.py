import Fridge

LG = Fridge.Fridge()
apple = Fridge.Food()
elephant = Fridge.Food()

LG.open()
LG.put(apple)
LG.put(elephant)
LG.close()

print("냉장고 안의 음식 :", LG.foods)