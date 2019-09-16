# 1. Variables for calculating savings
annual_salary = int(input("Enter the starting salary: "))
monthly_salary = annual_salary / 12
semi_annual_raise = 0.07
annual_return = 0.04
down_payment = 250000
current_savings = 0
# 2. Variables for bisection search
num_steps = 0
low = 0
high = 10000
portion_saved = (high + low) // 2
# 3. Variables for conditions
epsilon = 100
possible = True
while abs(current_savings - down_payment) > epsilon and possible == True:
    current_savings = 0
    monthly_salary = annual_salary / 12 # clear salary from raises
    for months_count in range(0, 36): # loop for calculating 3-year-savings
        current_savings += current_savings * annual_return / 12
        current_savings += monthly_salary * (portion_saved / 10000)
        if months_count != 0 and months_count % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    if current_savings < down_payment: #bisection search
       low = portion_saved
    else:
       high = portion_saved
    # this works because the new portion is set *after* this check,
    # so if we run another iteration after this the 99.99% savings rate
    # was not enough
    if portion_saved == 9999:
        print("It is not possible to pay the down payment in three years.")
        # stop the while loop if impossible to save for down payment, even if
        # 99.99% of salary are saved for 3 years
        possible = False
    portion_saved = (high + low) // 2
    num_steps += 1

if possible == True:
    best_savings_rate = portion_saved / 10000 # output should be a decimal
    print("Best savings rate: ", best_savings_rate)
    print("Steps in bisection search: ", num_steps)
