#ask monthly salary
#calculate ideal saving amount 20%
#calculate maximum monthly expense 80%

name = str(input ("Enter your name"))
monthly_salary = float (input ("Enter your monthly salary"))

monthly_idealsaving = (monthly_salary * (0.2))
monthly_maximumexpense =( monthly_salary * (0.8))
ideal_dailyexpensebudget = monthly_maximumexpense / 31
total_expenses = 0

print("Monthly Salary:",monthly_salary)
print("Monthly Ideal Saving Amount:", monthly_idealsaving)
print("Monthly Maximum Expense:", monthly_maximumexpense)
print("Ideal Maximum Daily Budget:", ideal_dailyexpensebudget)



#ask for daily expense every day of the month. Loop for 31 days. How to do that the loop will stop if MM
for day in range (1,32):
  print("\nDay",day)
  
  ideal_dailyexpensebudget=float(input("Enter your expense for  the day:"))
  total_expenses += ideal_dailyexpensebudget
  
  if total_expenses >= monthly_maximumexpense:
    print ("You have spend your maximum budget this month")

    break  
  
  if total_expenses >= monthly_maximumexpense * 0.8:
    print("Warning: You have used up to 80% of your maximum expense budget!")

#it is adding the daily spending amount, however the ideal daily expense budget is not doing what I wanted. Total expenses is functioning well
# warnings are operating well too
  
  print ("Total Expenses:", total_expenses)

remaining_budget=monthly_maximumexpense - total_expenses
print ("\nMonthly Summary:")
print ("Monthly Salary:", monthly_salary)
print ("Monthly Ideal Saving:", monthly_idealsaving)
print ("Monthly Maximum Expense:", monthly_maximumexpense)
print ("Total Expenses:", total_expenses)
print ("Remaining Budget:", remaining_budget)

#summary is running well

#closing statement
if remaining_budget >= 0:
  print ("Well done, you have spend less than your montly maximum spend budget. You may want so save this extra amount for a special project in the future:", name)
if remaining_budget <= 0:
  print ("Watch out on your expenses, this month you did not save enough. Perhaps you would like to review your daily expenses:", name)

