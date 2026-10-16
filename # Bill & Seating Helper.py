# Bill & Seating Helper

# Function to calculate a restaurant bill using positional arguments
def calculate_bill(food_cost, drinks_cost, tax):
    total = food_cost + drinks_cost + tax
    return total


# Function to calculate seating arrangements using recursion
def seating_arrangements(n):
    """
    Calculate the number of ways to arrange n people in seats using recursion.
    """
    if n <= 1:
        return 1
    return n * seating_arrangements(n - 1)


# Calculate the restaurant bill
bill = calculate_bill(5000, 2000, 500)
print("Restaurant Bill: ₦", bill)


# Access and display the function's docstring
print("\nFunction Docstring:")
print(seating_arrangements.__doc__)


# Calculate seating arrangements
people = 4
print("\nNumber of people:", people)
print("Possible seating arrangements:", seating_arrangements(people))n