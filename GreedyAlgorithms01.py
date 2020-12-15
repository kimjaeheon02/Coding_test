total_money = int(input('거스름돈 : '))
exchange = [500, 100, 50, 10]


for i in exchange:
    count = int(total_money / i)
    print(i, '원 : ', count, '개')
    total_money = total_money % i