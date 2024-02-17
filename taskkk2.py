MIN_SENIORS = 10
MAX_SENIORS = 36
MIN_CARERS = 2
ADDITIONAL_CARERS_THRESHOLD = 24
HIRE_OF_COACH = {range(12, 17): 150, range(17, 27): 190, range(27, 40): 225}
COST_OF_MEAL = {range(12, 17): 14.00, range(17, 27): 13.50, range(27, 40): 13.00}
COST_OF_THEATRE_TICKET = {range(12, 17): 21.00, range(17, 27): 20.00, range(27, 40): 19.00}

def calculate_total_cost(num_seniors):
    if not MIN_SENIORS <= num_seniors <= MAX_SENIORS:
        return "Error: Invalid number of seniors. Please enter a number between 2 and 36."

    num_carers = MIN_CARERS + (1 if num_seniors > ADDITIONAL_CARERS_THRESHOLD else 0)
    total_cost = sum(HIRE_OF_COACH[range(MIN_SENIORS, min(MAX_SENIORS, i + 12))] * num_seniors for i in range(3)) + \
                  sum(COST_OF_MEAL[range(MIN_SENIORS, min(MAX_SENIORS, i + 12))] * (num_seniors + num_carers) for i in range(3)) + \
                  sum(COST_OF_THEATRE_TICKET[range(MIN_SENIORS, min(MAX_SENIORS, i + 12))] * num_seniors for i in range(3))

    cost_per_person = total_cost / (num_seniors + num_carers)
    return f"Total cost: ${total_cost:.2f}\nCost per person: ${cost_per_person:.2f}"

# Task 2
people_on_outing = []
amount_paid = []
def record_outing():
    num_seniors = int(input("Enter the number of seniors interested in the outing: "))
    for i in range(num_seniors):
        name = input(f"Enter the name of senior {i+1}: ")
        people_on_outing.append(name)
        payment = float(input(f"Enter the amount paid by {name}: ").replace('$', ''))
        amount_paid.append(payment)

    num_carers = int(input("Enter the number of carers on the outing: "))
    for i in range(num_carers):
        name = input(f"Enter the name of carer {i+1}: ")
        people_on_outing.append(name)
        payment = float(input(f"Enter the amount paid by {name}: ").replace('$', ''))
        amount_paid.append(payment)
# task 3
    total_collected = sum(amount_paid)
    print("\nList of people on the outing and amount paid:")
    for i in range(len(people_on_outing)):
        print(f"{people_on_outing[i]} - ${amount_paid[i]:.2f}")
    print(f"\nTotal amount collected: ${total_collected:.2f}")

    estimated_cost = float(calculate_total_cost(num_seniors).split(':')[1].split()[0])
    profit_or_loss = total_collected - estimated_cost
    if profit_or_loss == 0:
        print("The outing has broken even.")
    elif profit_or_loss > 0:
        print(f"The outing has made a profit of ${profit_or_loss:.2f}.")
    else:
        print(f"The outing has incurred a loss of ${abs(profit_or_loss):.2f}.")

record_outing()