import math
# User instructions
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan")
calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Calculate the investment in simple or compound interest
if calculator_type.upper() == 'INVESTMENT':
    deposit = int(input("Please enter your deposit: "))
    interest_rate = int(input("Please enter your interest rate (as a percentage) without %: "))
    invest_period = int(input("Please enter your number of years on investing: "))
    interest = input("Please choose 'simple' or 'compound' interest: ")
    if interest == 'simple':
        result = deposit * (1 + interest_rate/100 * invest_period)
        print(f"The {interest} is {result}")
    elif interest == 'compound':
        result = deposit * math.pow((1 + interest_rate/100), invest_period)
        print(f"The {interest} is {result}")
    else:
        raise Exception("Invalid interest calculation. Only 'simple' or 'compound' interest can be calculated")
# Calculate the bond repayment
elif calculator_type.upper() == "BOND":
    pv = int(input("Please enter the present value of the house: "))
    interest_rate = int(input("Please enter your interest rate (as a percentage) without %: "))
    n = int(input("Please enter the number of months you plan to take to repay the bond: "))
    monthly_interest = (interest_rate/100) / 12
    repayment = (monthly_interest * pv) / (1 - (1 + monthly_interest) ** (-n))
    print(f"The monthly repayment is {repayment}")
else:
    raise Exception("Invalid input of the calculator!")
