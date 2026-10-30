def calculte_change(paid,price):
    change=paid - price
    return change
snack_price=25
print("vending machine")
print(f"this snack costs {snack_price} units")
print("accepted coins:1,5,10,25\n")
total_inserted=0
coins_inserted=0
while True:
    coin=int(input("insert a coin(1,5,10,25:)"))
    if coin!=1 and coin!=5 and coin!=10 and coin!=25:
        print("invalid coin,try again\n")
        continue
    total_inserted+=coin
    coins_inserted+=1
    print(f"inserted {coin} .total so far:{total_inserted}\n")
    if total_inserted>=snack_price:
          print("enough money inserted\n")
          break