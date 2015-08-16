#balance = 3329
#信用卡未支付债务余额
#annuallnterestRate = 0.2
#十进制数的年利率
#monthlyPaymentRate = 0.02
#十进制数的最小月支付比例
month = 0
mininumMonthlyPayment = 0
remainingBalance = balance
'''mininumMonthlyPayment = remainingBalance*monthlyPaymentRate
remainingBalance = remainingBalance - mininumMonthlyPayment
print('Month: 0')
print('Minimum monthly payment: '+str(round(mininumMonthlyPayment,2)))
print('Remaining balance: '+str(round(remainingBalance,2)))'''
low = remainingBalance/12
high = (remainingBalance*((1+annuallnterestRate/12)**12))/12
mininumMonthlyPayment = (low + high)/2
while (high - low)>0.0001:
	month = 0
	print(low,high)
	print(remainingBalance)
	print(mininumMonthlyPayment)
	if remainingBalance>0:
		low = mininumMonthlyPayment
	else:
		high = mininumMonthlyPayment
	mininumMonthlyPayment = (low + high)/2
	remainingBalance = balance
	for month in range(12):
		remainingBalance = remainingBalance - mininumMonthlyPayment
		remainingBalance *=(1+(annuallnterestRate/12))