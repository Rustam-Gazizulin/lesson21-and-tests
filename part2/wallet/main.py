# У нас есть класс кошелек, в котором есть поля – 
# золотые, серебряные и бронзовые монеты.

#  Одна золотая монета ровна десять серебряных
#  Одна серебряная монета ровна сто бронзовых

# Реализовать методы сравнения двух экземпляров
# класса кошелёк, заполненных такими монетами.
 

class Wallet:
    def __init__(self, gold=0, silver=0, bronze=0):
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def get_count(self):
        gold = 0
        silver = 0
        if self.gold:
            gold = self.gold * 1000
        if self.silver:
            silver = self.silver * 100
        return self.bronze + gold + silver

    def __repr__(self):
        return f'З: {self.gold}, С: {self.silver}, Б: {self.bronze}'

    def __eq__(self, other):
        return self.get_count() == other.get_count()

    def __ne__(self, other):
        return self.get_count() != other.get_count()

    def __gt__(self, other):
        return self.get_count() > other.get_count()

    def __ge__(self, other):
        return self.get_count() >= other.get_count()

    def __lt__(self, other):
        return self.get_count() < other.get_count()

    def __le__(self, other):
        return self.get_count() <= other.get_count()


# Здесь код для самопроверки, 
# если в терминале хотя бы один пункт ложь, тогда ищите ошибку в коде,
if __name__ == '__main__':
    big_wallet = Wallet(
        gold=5
    )
    
    medium_wallet = Wallet(
        gold=2,
        silver=7,
        bronze=72
    )
    
    small_wallet = Wallet(
        bronze=100
    )

    small_silver_wallet = Wallet(
        silver=1
    )

    big_silver_wallet = Wallet(
        silver=50
    )


    def true_lie(assertion):
        if assertion:
            return "Правда"
        return "Ложь"
    
    
    print(
        f" {big_wallet} == {big_silver_wallet}", 
        true_lie(big_wallet == big_silver_wallet))
    print(
        f" {small_silver_wallet} == {big_silver_wallet}",
        true_lie(small_silver_wallet != big_silver_wallet))
    print(
        f" {medium_wallet} > {small_wallet}", 
        true_lie(medium_wallet > small_wallet)
    )
    print(
        f" {small_silver_wallet} < {big_silver_wallet}", 
        true_lie(small_silver_wallet < big_silver_wallet)
    )
    print(
        f" {big_wallet} <= {big_silver_wallet}", 
        true_lie(big_wallet <= big_wallet)
    )
    print(
        f" {small_wallet} <= {big_wallet}", 
        true_lie(small_wallet <= big_wallet)
    )
    print(
        f" {big_wallet} >= {big_silver_wallet}", 
        true_lie(big_wallet >= big_silver_wallet)
    )
    print(
        f" {big_wallet} >= {medium_wallet}", 
        true_lie(big_wallet >= medium_wallet)
    )
