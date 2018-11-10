width=input('please enter width: ')
price_width=10
item_width=int(width)-price_width
header_format='%-*s%*s'
format       ='%-*s%*.2f'
print('=' *int(width))
print(header_format % (item_width,'item',price_width,'price'))
print('-' *int(width))
print(format % (item_width,'Apples',price_width,0.4))
print(format % (item_width,'Pears',price_width,0.5))
input()