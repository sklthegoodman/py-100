'''
百钱百鸡
    公鸡单价：5
    母鸡：3
    小计：1/3
'''

def chicken(female=5,male=3,chick=1/3,price=100,quantity=100):
    for f in range(1,int(quantity/female)):
        for m in range(1,int(quantity/male)):
            if female * f + male * m + (quantity-f-m) * chick == price:
                print((f,m,(quantity-f-m)))

# 百前百鸡
chicken()

# 千元千鸡
print('千元千鸡')
options = {
    "price":1000,
    "quantity":1000
}
chicken(**options)