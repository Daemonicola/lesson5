tuple = 2,4,3,5
immutable_var = tuple
print(immutable_var)
 # Если мы хотим изменить элемент кортежа, то мы столкнемся с ошибкой,которая показывает, что кортеж не поддерживает образение по элементам
# Однако, если поставить квадратные скобки и попробовать присудить элементу новое значение, то у нас все получится
tuple = ([2],[9], 15)
print(tuple)
tuple[0][0]=14
print(tuple)
mutable_list = ['soda', 'fruit', 'products']
mutable_list.append('tools')
print(mutable_list)
