balance = 5000#信用卡未支付债务余额
annuallnterestRate = 18#十进制数的年利率
monthlyPaymentRate = 0.02#十进制数的最小月支付比例

month = 0
mininumMonthlyPayment = 0
remainingBalance = balance
mininumMonthlyPayment = remainingBalance*monthlyPaymentRate
remainingBalance = remainingBalance - mininumMonthlyPayment
print('Month: 0')
print('Minimum monthly payment: '+str(round(mininumMonthlyPayment)))
print('Month: 0'+str(round(remainingBalance)))
for month in range(12):
	remainingBalance *=(1+annuallnterestRate/12)
	mininumMonthlyPayment = remainingBalance*monthlyPaymentRate
	remainingBalance = remainingBalance - mininumMonthlyPayment
	print('Month: '+str(month+1)
    print('Minimum monthly payment: '+str(round(mininumMonthlyPayment)))
	print('Month: 0'+str(round(remainingBalance)))