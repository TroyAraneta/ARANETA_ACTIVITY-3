# Purchase Amount Input
PA = eval(input("Enter purchase amount: "))
# The 6% Sales Tax Percentage
STP = 0.06
# Sales Tax Percentage multiplied by the Purchase Amount
STV = PA * STP
# Sales Tax Value's Decimal Rounded to 2
TAD = round(STV, 2)
# Output Result
print("Sales tax is", TAD)
