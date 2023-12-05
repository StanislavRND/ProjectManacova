# Дан список A размера N. Сформировать новый список B того же размера по
# следующему правилу: элемент BK равен сумме элементов списка A с номерами от 1
# до K.

import random

def form_new_list(N):
    A = [random.randint(1, 100) for i in range(N)]
    B = [sum(A[:i+1]) for i in range(N)]
    return A, B

N = 5
A, B = form_new_list(N)
print("Список A:", A)
print("Список B:", B)