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


