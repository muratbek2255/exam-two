# list_worker = [
#     {'name': 'Барсбек Канаткулов', 'work': 'manager', 'ZP': '45000', 'work_on_week': '18 hours', 'id': '1'},
#     {'name': 'Алымкул Тилекбаев', 'work': 'secretary', 'ZP': '20000', 'work_on_week': '38', 'id': '2'},
#     {'name': 'Айпери Шалымбекова', 'work': 'salesman', 'ZP': '20000',  'work_on_week': '38', 'id': '3'},
#     {'name': ' Бакыт Рустамов', 'work': 'shop worker',  'work_on_week': '25', 'id': '4'},
#     {'name': 'Алтынай Ширинбаева', 'work': 'shop worker',  'work_on_week': '40', 'id': '5'},
#     {'name': ' Жанар Рыскулов', 'work': 'secretary', 'ZP': '20000', 'work_on_week': '33', 'id': '6'}
# ]
# summa = 0
#
#
# # while True:
# #     manager = float(input(f'Vvedite summu: '))
# #     secretary = float(input(f'Vvedite summu: '))
# #     saleswoman = float(input('Количеество продаж: '))
# #     shop_worker = float(input('Введите часовой оклад: '))
# #     summa += 1
# #
# #     saleswoman_summa = 50 * saleswoman
# #     secretary_summa = secretary * 2
# #     shopworker_summa = shop_worker * 100
# #
# #
# #     if summa > 0:
# #         print(manager+secretary_summa+saleswoman_summa+shopworker_summa)
# #         break
# #
#
#
# product = []
# noproduct = []
#
# for i in list_worker:
#     if i['work_on_week'] == '38':
#         product.append(i["name"])
#     elif i['work_on_week'] == '40':
#         product.append(i["name"])
#     else:
#         noproduct.append(i["name"])
#
#
# print(f'Продуктивные: {product}'
#       f'Непродуктивные: {noproduct}')

# class Office:
#     def __init__(self, name, id, time):
#         self.name = name
#         self.id = id
#         self.time = time
#
#     def salary(self):
#         pass
#
#     def summa(self):
#         pass
#
#     def KPD(self):
#         self.time*100/40
#
#
# class Manager(Office):
#     def init(self, name, id, time, money):
#         super().__init__(name, id, time)
#         self.money = money
#
#     def salary(self):
#         return self.money
#
# class Secretary(Office):
#     def init(self, name, id, time, salary):
#         super().__init__(name, id, time)
#         self.salary = salary
#
#     def salary(self):
#         return self.salary
#
# class SalesMan(Office):
#     def init(self, name, id, time, salary, prodaja) -> None:
#         super().__init__(name, id, time)
#         self.salary = salary
#         self.prodaja = prodaja
#
#     def salary(self):
#         return self.salary + (self.prodaja*50)
#
# class ShopWorker(Office):
#     def init(self, name, id, time, salary, hour):
#         super().__init__(name, id, time)
#         self.salary = salary
#         self.hour = hour
#
#     def salary(self):
#         return self.hour * 100
#
# class SecretaryReplacement(Office):
#     def init(self, name, id, time, salary, hour):
#         super().__init__(name, id, time)
#         self.salary = salary
#         self.hour = hour
#
#     def salary(self):
#         return self.hour * 100
#
#
# manager = Manager("Барсбек Канаткулов", 1, 18, 45000)
# secretary = Secretary("Алымкул Тилекбаев",2,38, 20, 20000)
# sales_person = SalesMan("Айпери Шалымбекова", 3, 38)
# cex = ShopWorker("Бакыт Рустамов",4,25)
# cex2 = ShopWorker("Алтынай Ширинбаева",5,40)
# zamena = SecretaryReplacement("Жанар Рыскулов",6,33)
# personal = []
# def office_money():
#     total_money = sum([
#         person.salary() for person in personal
#         ])
#     return f"Общий заработок персонала - {total_money}"
# def vyvod():
#     total = office_money()
#     for worker in personal:
#         print(f'ID - {worker.id}, Name - {worker.name} Salary - {worker.salary} Perfomance - {worker.KPD()}')
#     return total
# vyvod()


