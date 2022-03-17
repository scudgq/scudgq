'''
给定利率，求翻倍需要多少年
'''
base = 100000
interest = 0.0325
year = 0
while base <= 200000:
    year +=1
    base+= base * interest
    print(year ,base)