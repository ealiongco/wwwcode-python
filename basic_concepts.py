""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

total_bill = input('How much is your total bill?: ')
payment = input('How much is your payment?: ')
change = int(total_bill) - int(payment)

print('Hi! Your change is ' + str(change))