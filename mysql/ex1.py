#ATM Use case
while True:
    balance=50000
    print('\t \t \t \twelcome to Indian Bank')
    print('1.check balance\n2.withdraw\n3.deposit\n4.exit')
    try:
        option=int(input('select your option:'))
    except Exception as e:
        print('error',e)
        continue
    if option==1:
        print('your balance is:',balance)
        break
    if option==2:
        print('balance is:',balance)
        withdraw=int(input('enter amount to withdraw:'))
        if withdraw<balance and withdraw>0:
            remainingbalance=(balance-withdraw)
            print('transaction of',withdraw,'is successfull')
            print('remaining balance is:',remainingbalance)
            break
        elif withdraw>balance:
            print('insufficient funds')
            print('enter amount less than',balance)
            break
        else:
            print('no withdraw done')
            break
    if option==3:
        deposit=int(input('enter amount to deposit:'))
        if deposit>0:
            updatedbalance=balance+deposit
            print('your account balance is:',updatedbalance)
            break
        else:
            print('enter positive value')
            break
    if option==4:
        exit()
        break
    if option>4:
        print('enter only 1,2,3 or 4')
        exit()









