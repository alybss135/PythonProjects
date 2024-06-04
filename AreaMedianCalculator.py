name_of_user = input("Enter your name: ")

answer = input("Hello " + name_of_user + ", would you like to know how to qualify for affordable housing? Answer with a yes or no ")

if (answer == "No" or answer == "no" or answer == "NO"):
    print("That's okay. You can always visit this site to learn more later: https://oaklandside.org/affordable-housing-guide/#how-do-i-know-if-i-qualify-for-affordable-housing")
else: 
    print("The federal government determines the 'area median income,' or AMI, for the region, including Oakland and Berkeley. When apartments become available, you are given the maximum and sometimes the minimum amount of income you can earn to qualify to live there.")

household_income = float(input("Enter your household income: "))

if (household_income < 31050.00):
    print("Based on your income, you are in the Extremely Low Income Category. You cannot afford a household")
elif (household_income >= 31050.00 and household_income < 35000.00):
    print("Based on your income, you are in the Extremely Low Income Category. You can afford to buy a one person household.")
elif (household_income > 35000.00 and household_income < 39950.00):
    print("Based on your income, you are in the Extremely Low Income Category. You can afford a two person household")
elif (household_income > 44350.00 and household_income < 47900.00):
    print("Based on your household income, you are in the Extremely Low Income category. You can afford to buy a four person household.")
elif (household_income >= 51800.00 and household_income < 59200.00):
    print("Based on your income, you are in the Very Low Income Category. You can afford to pay for a one-person household.")
elif (household_income >= 59200.00 and household_income < 66600.00):
    print("Based on your income, you are in the Very Low Income Category. You can affor to pay for a two person household")
elif (household_income >= 73950.00 and household_income < 79900.00):
    print("Based on your income, you are in the Very Low Income Category. You can afford to buy a four person household")
elif (household_income >= 78550.00 and household_income < 89750.00):
    print("Based on your income, you are in the Low Income Category. You can afford to pay for a one-person household.")
elif (household_income >= 89750.00 and household_income < 100950.00):
    print("Based on your income, you are in the Low Income Category. Youn can afford to pay for a two person household.")
elif (household_income >= 112150.00 and household_income < 118300.00):
    print("Based on your income, you are in the Low Income Category. You can afford to pay for a one or four person household.")
elif (household_income >= 118300.00 and household_income < 121150.00):
    print("Based on your income, you are in the Area Median Income Category. You can afford to pay for a one person household.")
elif (household_income >= 121150.00 and household_income < 133100.00):
    print("Based on your income, you are in the Area Median Income Category. You can afford to pay for a two person household.")
elif (household_income >= 147900.00 and household_income < 159750.00):
    print("Based on your income, you are in the Area Median Income and Moderate Income Category. You can afford to pay for a two or four person household.")
elif (household_income >= 133100.00 and household_income <= 142000.00):
    print("Based on your income, you are in the Moderate Income Category. You can afford to pay for a one-person household.")
elif (household_income >= 177500.00 and household_income < 191700.00):
    print("Based on your income, you are in the Moderate Income Category. You can afford to pay for a four person household.")
else: 
    print("Based on your income, you are in the Above Moderate Income Category.")