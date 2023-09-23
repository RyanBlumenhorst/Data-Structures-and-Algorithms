def MakeChange(cost, paid):
    amount = paid - cost
    amount = round(amount, 2)

    hundreds = 0
    fifties = 0
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    while amount >= 100:
        hundreds += 1
        amount = round(amount - 100, 2)
    while amount >= 50:
        fifties += 1
        amount = round(amount - 50, 2)
    while amount >= 20:
        twenties += 1
        amount = round(amount - 20, 2)
    while amount >= 10:
        tens += 1
        amount = round(amount - 10, 2)
    while amount >= 5:
        fives += 1
        amount = round(amount - 5, 2)
    while amount >= 1:
        ones += 1
        amount = round(amount - 1, 2)
    while amount >= 0.25:
        quarters += 1
        amount = round(amount - 0.25, 2)
    while amount >= 0.10:
        dimes += 1
        amount = round(amount - 0.10, 2)
    while amount >= 0.05:
        nickles += 1
        amount = round(amount - 0.05, 2)
    while amount >= 0.01:
        pennies += 1
        amount = round(amount - 0.01, 2)
    print('Your change:')
    if hundreds > 0:
        if hundreds == 1:
            print ("1 Hundred Dollar Bill")
        else:
            print('%d Hundred Dollar Bills' % hundreds)
    if fifties > 0:
        if fifties == 1:
            print("1 Fifty Dollar Bill")
        else:
            print('%d Fifty Dollar Bills' % fifties)
    if twenties > 0:
        if twenties == 1:
            print("1 Twenty Dollar Bill")
        else:
            print('%d Twenty Dollar Bills' % twenties)
    if tens > 0:
        if tens == 1:
            print("1 Ten Dollar Bill")
        else:
            print('%d Ten Dollar Bills' % tens)
    if fives > 0:
        if fives == 1:
            print("1 Five Dollar Bill")
        else:
            print('%d Five Dollar Bills' % fives)
    if ones > 0:
        if ones == 1:
            print("1 One Dollar Bill")
        else:
            print('%d One Dollar Bills' % ones)
    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print('%d Quarters' % quarters)
    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print('%d Dimes' % dimes)
    if nickles > 0:
        if nickles == 1:
            print("1 Nickle")
        else:
            print('%d Nickles' % nickles)
    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print('%d Pennies' % pennies)


cost = round(float(input('Enter the cost: ')), 2)
paid = round(float(input('Enter the amount paid: ')), 2)
MakeChange(cost, paid)
