# Problem Set 1 C
# Name: Rafael Ederli
# Time Spend: 0:00

# Part C: Choosing an Interest Rate
initial_deposit = float(input("Enter the initial deposit: "))

cost_of_dream_home = 800000
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment

if initial_deposit >= down_payment - 100:
    print("Best savings rate:", 0.0)
    print("Steps in bisection search:", 0)
else:
    # Limits
    low = 0.0
    high = 1.0
    steps = 0
    r = None

    while low <= high:
        mid = (low + high) / 2
        amount_saved = initial_deposit * (1 + mid / 12) ** 36
        if abs(amount_saved - down_payment) < 100:
            r = mid
            break
        elif amount_saved < down_payment:
            low = mid
        else:
            high = mid

        steps = steps + 1

        if high - low < 1e-9:
            break
    
    if r is None:
        print("Best savings rate: None")
    else:
        print("Best savings rate:", round(r, 4))
        print("Steps in bisection search:", steps)