balance = float(input('balance = '))
annuallnterestRate = float(input('annuallnterestRate = '))
a = annuallnterestRate/12
monthlyPaymentRate = 0.02
mininumMonthlyPayment = (balance*((a+1)**11)*(a))/(((a+1)**12)-1)
print('mininumMonthlyPayment: '+str(round(mininumMonthlyPayment,2)))
#print(a)