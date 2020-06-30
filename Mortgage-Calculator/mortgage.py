import math
term = input("How would you like to pay: monthly, weekly, daily, or continually? ")
payment = int(input("What is the initial loan amount? "))
interest = int(input("How much is the interest? "))
nth = int(input("How many years would you like to pay? "))

if term == "monthly":
    math = payment * ((interest * .010) / 12) * (1 + (interest*.010 / 12)) ** (nth * 12) / \
           ((1 + (interest*.010 / 12)) ** (nth * 12) - 1)
    print(str("You will have to pay $") + str(round(math, 2)) + str(" a month to pay off your debt."))
elif term == "weekly":
    math2 = payment * ((interest * .010) / 52) * (1 + (interest*.010 / 52)) ** (nth * 52) / \
            ((1 + (interest*.010 / 52)) ** (nth * 52) - 1)
    print(str("You will have to pay $") + str(round(math2, 2)) + str(" a week to pay off your debt OR a total of $")
          + str(round(math2 * 4.34, 2)) + str(" a month."))
elif term == "daily":
    math3 = payment * ((interest * .010) / 365) * (1 + (interest*.010 / 365)) ** (nth * 365) / \
            ((1 + (interest*.010 / 365)) ** (nth * 365) - 1)
    print(str("You will have to pay $") + str(round(math3, 2)) + str(" a day to pay off your debt OR around $")
          + str(round(math3 * 30.42, 2)) + str(" a month."))
else:
    math4 = payment * math.exp((interest * .010) * (120/12))
    print(str("$") + str(payment) + str(" compounded continuously at a rate of ") + str(interest) + str("% for ")
          + str(nth) + str(" years will yield a final amount of $") + str(round(math4, 2)))
