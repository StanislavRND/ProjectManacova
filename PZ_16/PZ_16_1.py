# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег

class Bank:
    def __init__(self, amount, rate):
        self.amount = amount
        self.rate = rate  

    def rate_calculation(self):
        interest_rate = self.amount * (self.rate / 100)
        print(f'Процентные начисления {interest_rate: .2f} рублей процентов.')

    def replenishment_money(self, amount):
        self.amount += amount
        print(f'Вам начислено {amount} рублей. На вашем счёте {self.amount} рублей.')

    def withdraw_money(self, amount):
        if (amount <= self.amount):
            self.amount -= amount
            print(f'Вы сняли {amount} рублей. Остаток на счёте {self.amount} рублей.')
        else:
            print('Недостаточно средст на счёте.')

bank1 = Bank(50000, 10)
print(f'На вашем счете {bank1.amount} рублей. Процентная ставка {bank1.rate} %.\n')
bank1.withdraw_money(4000)
bank1.rate_calculation()
bank1.replenishment_money(17000)
bank1.rate_calculation()


