
Amount=int(input("Enter your vsishi amount :"))
member=int(input("Enter your number of member for vishi :"))
month=int(input("Enter no. month to do :"))
intrest=float(input("Enter your intrest rate :"))
i=1
per_month_amount=Amount/member
intrest_amount=Amount*intrest/100
deposte_amount=per_month_amount-intrest_amount
add_amount=intrest_amount/(member-2)
while i<=month:
    if i==1:
        print("Deposite amount for 1st month is :",per_month_amount)
    else:
        deposte_amount=deposte_amount+add_amount
        print("You have to deposite amount is ",i," month :",deposte_amount,"Total of this month is :",deposte_amount*member)
        
    i+=1

# Amount=200000
# add_amoumt=(Amount*1.5/100)/8
# deposte_amount=20000-(Amount*1.5/100)
# print(deposte_amount+add_amoumt)
