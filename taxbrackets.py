"""
This shows an example of the "fivethirtyeight" styling, which
tries to replicate the styles from FiveThirtyEight.com.
"""
from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl

print(mpl.__version__)

def marginal_to_average(tax_structure, income):
    cumulative_bracket_max = 0
    total_tax = 0
    residual_income = income
    for (bracket_max, tax_rate) in tax_structure:
        cumulative_bracket_max += bracket_max
        exceeds_bracket = income > cumulative_bracket_max
        if exceeds_bracket: # tax total amount in bracket
            total_tax += tax_rate * bracket_max
            residual_income -= bracket_max 
        else:
            total_tax += tax_rate * residual_income
            break
    return total_tax

def marginal_tax(tax_structure, income):
    """ Returns marginal tax rate given an income """
    cumulative_bracket_max = 0
    residual_income = income
    for (bracket_max, tax_rate) in tax_structure:
        cumulative_bracket_max += bracket_max
        exceeds_bracket = income > cumulative_bracket_max
        if not exceeds_bracket: 
            return tax_rate
    print('Error: income higher than highest tax bracket')
    return -1

def marginal_to_average_list(tax_structure, income):
    marginal_taxes = [marginal_tax(tax_structure, i) for i in range(income)]
    dollars = [ i+1 for i in range(income)]
    average_tax = np.cumsum(marginal_taxes) / dollars
    # average_tax = np.cumsum(marginal_taxes)
    return average_tax
        


max_gross_income = 150000

marginal_tax_canada = [
    (44701, 15.0/100),
    (44700, 22.0/100),
    (49185, 26.0/100),
    (max_gross_income, 29.0/100) 
    ]
marginal_tax_ontario = [
    (40922, 5.05/100),
    (40925, 9.15/100),
    (68153, 11.16/100),
    (70000, 12.16/100),
    (max_gross_income, 13.16/100) 
    ]
marginal_tax_bc = [
    (37869, 5.06/100),
    (37871, 7.7/100),
    (11218, 10.5/100),
    (18634, 12.19/100),
    (45458, 14.7/100),
    (max_gross_income, 13.16/100) 
    ]
marginal_tax_alberta = [
    (max_gross_income, 10.0/100) 
    ]
marginal_tax_usa = [
    (9075, 10.0/100),
    (36900-9075, 15.0/100),
    (89350-36900, 25.0/100),
    (186350-89350, 28.0/100),
    (405100-186350, 33.0/100),
    (406750-405100, 35.0/100),
    (max_gross_income, 39.6/100) 
    ]
marginal_tax_cali = [
    (7749, 1.0/100),
    (18371-7749, 2.0/100),
    (28995-18371, 4.0/100),
    (40250-28995, 6.0/100),
    (50869-40250, 8.0/100),
    (259844-50869, 9.3/100),
    (311812-259844, 10.3/100),
    (519687-311812, 11.3/100),
    (max_gross_income, 12.3/100) 
    ]

avg_tax_canada = marginal_to_average_list(marginal_tax_canada, max_gross_income)
avg_tax_ontario = marginal_to_average_list(marginal_tax_ontario, max_gross_income)
avg_tax_bc = marginal_to_average_list(marginal_tax_bc, max_gross_income)
avg_tax_alberta = marginal_to_average_list(marginal_tax_alberta, max_gross_income)
avg_tax_usa = marginal_to_average_list(marginal_tax_usa, max_gross_income)
avg_tax_cali = marginal_to_average_list(marginal_tax_cali, max_gross_income)

min_gross_income = 10000
income_range = range(min_gross_income, max_gross_income)

plt.style.use('fivethirtyeight')
tax_ontario = avg_tax_canada + avg_tax_ontario
tax_bc = avg_tax_canada + avg_tax_bc
tax_cali = avg_tax_usa + avg_tax_cali

handle_on = plt.plot(income_range, tax_ontario[min_gross_income:max_gross_income], label='Ontario')
handle_bc = plt.plot(income_range, tax_bc[min_gross_income:max_gross_income], label='British Columbia')
handle_cali = plt.plot(income_range, tax_cali[min_gross_income:max_gross_income], label='California')
handle_us = plt.plot(income_range, avg_tax_usa[min_gross_income:max_gross_income], label='Washington')
# handle_ab = plt.plot(income_range, avg_tax_canada + avg_tax_alberta, label='Alberta')
# handle_on = plt.plot(income_range, avg_tax_canada, label='Canada')
plt.xlabel('Income ($)')
plt.ylabel('Effective Tax Rate (%)')
# plt.ylabel('Tax ($)')
plt.legend(loc=4)
plt.show()
