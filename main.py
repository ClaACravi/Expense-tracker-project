#ask monthly salary
#calculate ideal saving amount 20%
#calculate maximum monthly expense 80%

name = str(input ("Enter your name"))
monthly_salary = float (input ("Enter your monthly salary"))

monthly_idealsaving = (monthly_salary * (0.2))
monthly_maximumexpense =( monthly_salary * (0.8))
ideal_dailyexpensebudget = round(monthly_maximumexpense / 31, 2)
total_expenses = 0

print("Monthly Salary:",monthly_salary)
print("Monthly Ideal Saving Amount:", monthly_idealsaving)
print("Monthly Maximum Expense:", monthly_maximumexpense)
print("Ideal Maximum Daily Budget:", ideal_dailyexpensebudget)



#ask for daily expense every day of the month. Loop for 31 da
for day in range (1,32):
  print("\nDay",day)
  
  current_dailyexpense=float(input("Enter your expense for  the day:"))
  if current_dailyexpense > ideal_dailyexpensebudget:
    print("You are spending too much today")
  total_expenses += current_dailyexpense
  
  if total_expenses >= monthly_maximumexpense:
    print ("You have spend your maximum budget this month")

    break  
  
  if total_expenses >= monthly_maximumexpense * 0.8:
    print("Warning: You have used up to 80% of your maximum expense budget!")

#it is adding the daily spending amount
  #Total expenses is functioning well
# warnings are operating well too
  
  print ("Total Expenses:", total_expenses)

remaining_budget=monthly_maximumexpense - total_expenses
print ("\nHello",name)
print ("Monthly Summary:")
print ("Monthly Salary:", monthly_salary)
print ("Monthly Ideal Saving:", monthly_idealsaving)
print ("Monthly Maximum Expense:", monthly_maximumexpense)
print ("Total Expenses:", total_expenses)
print ("Remaining Budget:", remaining_budget)

#summary is running well

#closing statement

if remaining_budget > 0:
  print ("Well done, you have spend less than your montly maximum spend budget. You may want so save this extra amount for a special project in the:")
if remaining_budget < 0:
  print ("Watch out on your expenses, this month you did not save enough. Perhaps you would like to review your daily expenses to avoid over spending:")
if remaining_budget == 0:
  print ("Good job, you have just spend the right amount:")
