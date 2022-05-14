p = float(input())#процентная ставка
x = int(input())#money"вклад"
#y = int(input())
money_before = 100 * x
money_after = int(money_before * (100 + p) / 100)
print(money_after // 100, money_after % 100)
