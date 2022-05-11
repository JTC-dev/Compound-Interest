principal = 200 # Starting amount
compounds = 0 

while True:

    if compounds < 365: #stops the program after 1 year of compounding

        daily_interest = 0.02 # Amount earned in the day

        profit = daily_interest * principal

        principal = principal + profit

        print(principal,'compounds:', compounds)
        compounds = compounds + 1
