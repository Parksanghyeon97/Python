milk_orders = {'101': {'milk': 1, 'yogurt': 5},
               '102': {'milk': 2},
               '103': {'milk': 1, 'yogurt': 10},
               '104': {'yogurt': 15}}

for k,v in milk_orders.items():
    if 'milk' in v:
        print("%s 호 milk : %s 개" %(k,milk_orders.get(k).get('milk')))
