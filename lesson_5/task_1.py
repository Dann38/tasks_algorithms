# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
import collections

n = int(input('Введите кол-во предприятий:\n'))
Company = collections.namedtuple('Company', 'name profit1 profit2 profit3 profit4 average')
companies = []
total_profit = 0

for i in range(1, n+1):
    name = input('Введите имя компании:\n')
    profit1 = int(input('Введите прибыль за последние 4 квартала:\n'))
    profit2 = int(input())
    profit3 = int(input())
    profit4 = int(input())
    average = (profit1 + profit2 + profit3 + profit4)/4

    total_profit += average

    companies.append(Company(name, profit1, profit2, profit3, profit4, average))

average_profit = total_profit/n

print(f'\n{average_profit}\n')
companies_min = ''
companies_max = ''

for i in companies:
    if i.average < average_profit:
        companies_min += f'{i.name} ({round(i.average, 2)}) на {round(average_profit - i.average, 2)} ниже среднего\n'

    else:
        companies_max += f'{i.name} ({round(i.average, 2)}) на {round(i.average - average_profit, 2)} выше среднего\n'

print(companies_max, companies_min)
