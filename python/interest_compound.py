"""Calculate compound interest for Paulik."""

import math

princ_amount = float(input("Please enter the princiapal amount: "))
rate_of_int = float(input("Please enter the rate of interest: "))
time_period = float(input("Please enter time period in years: "))

ci_future = princ_amount * (math.pow((1 + rate_of_int / 100), time_period))
compound_int = ci_future - princ_amount
print("Future compound interest for principal amount {0} = {1}".format(princ_amount, ci_future))
print("Compound interest for principal amount{0} = {1}".format(princ_amount, compound_int))
