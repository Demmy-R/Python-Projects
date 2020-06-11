adult = int(input("How many adults are riding this train? "))
adult_train = adult * 12
adult_miles = int(input("How many miles are the adults riding in total? "))
adult_total = adult_train * adult_miles
print("There are " + str(adult) + " adults riding this train, each riding " + str(adult_miles)
      + " mile(s), and the total cost is $" + str(adult_total) + "\n")

kids = int(input("How many kids are riding this train? "))
kids_train = kids * 7.5
kids_miles = int(input("How many miles are the kids riding in total? "))
kids_total = kids_train * kids_miles
print("There are " + str(kids) + " kids riding this train, each riding " + str(kids_miles)
      + " mile(s), and the total cost is $" + str(kids_total) + "\n")

kids_adults = kids_total + adult_total
print("The total amount earned today is $" + str(kids_adults))
