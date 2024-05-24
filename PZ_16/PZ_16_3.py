# Для задачи из блока 1 создать две функции, save_def и
# load_def, которые позволяют сохранять информацию из экземпляров класса (3
# шт.) в файл и загружать ее обратно. Использовать модуль pickle для
# сериализации и десериализации объектов Python в бинарном формате."""
import pickle


class Bank:
    def __init__(self, amount, rate):
        self.amount = amount
        self.rate = rate

    def rate_calculation(self):
        interest_rate = self.amount * (self.rate / 100)
        return f'Процентные начисления{interest_rate: .2f} рублей процентов.'

    def replenishment_money(self, amount):
        self.amount += amount
        return f'Вам начислено {amount} рублей. На вашем счёте {self.amount} рублей.'

    def withdraw_money(self, amount):
        if (amount <= self.amount):
            self.amount -= amount
            return f'Вы сняли {amount} рублей. Остаток на счёте {self.amount} рублей.'
        else:
            return 'Недостаточно средств на счёте.'


def save_def(banks, filename):
    with open(filename, 'wb') as f:
        pickle.dump(banks, f)


def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


Bank1 = Bank(2500, 7)
Bank2 = Bank(50000, 10)
Bank3 = Bank(120000, 12)

banks = [Bank1, Bank2, Bank3]
save_def(banks, 'banks.pkl')

loaded_banks = load_def('banks.pkl')

for bank in loaded_banks:
    print(f'На вашем счете {bank.amount} рублей. Процентная ставка {bank.rate} %.')
    print(bank.withdraw_money(1000))
    print(bank.rate_calculation())
    print(bank.replenishment_money(17000))
    print(bank.rate_calculation())
    print()
