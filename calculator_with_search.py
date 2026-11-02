# Seth Pearson
# Calculator with search Function
# 11/1/2026
def calculate(first_number, operator, second_number):
	if operator == "+":
		return first_number + second_number
	if operator == "-":
		return first_number - second_number
	if operator == "*":
		return first_number * second_number
	if operator == "/":
		if second_number == 0:
			raise ZeroDivisionError("Cannot divide by zero")
		return first_number / second_number
	raise ValueError(f"Unsupported operator: {operator}")

def basic_calculate():
	try:
		first_number = float(input("Enter the first number: "))
		operator = input("Enter an operator (+, -, *, /): ")
		second_number = float(input("Enter the second number: "))
		result = calculate(first_number, operator, second_number)
		print(result)
	except (ValueError, ZeroDivisionError) as error:
		print(f"Error: {error}")

def brute_force_search(a, b, c):
	closest_x = -100
	closest_difference = float("inf")
	for step in range(2001):
		x = -100 + step * 0.1
		difference = abs((a * x + b) - c)
		if difference < closest_difference:
			closest_x = x
			closest_difference = difference
	return closest_x

def equation_solver_menu():
	try:
		a = float(input("Enter value for a: "))
		b = float(input("Enter value for b: "))
		c = float(input("Enter value for c: "))
		x = brute_force_search(a, b, c)
		print(f"Approximate value of x: {x}")
	except ValueError as error:
		print(f"Error: {error}")

def visualize_search():
	try:
		a = float(input("Enter value for a: "))
		b = float(input("Enter value for b: "))
		c = float(input("Enter value for c: "))
		closest_x = -100
		closest_difference = float("inf")
		closest_result = None
		for step in range(2001):
			x = -100 + step * 0.1
			result = a * x + b
			difference = abs(result - c)
			print(f"Testing x = {x:.1f}: ax + b = {result}, distance from c = {difference}")
			if difference < closest_difference:
				closest_x = x
				closest_difference = difference
				closest_result = result
		print(f"Closest solution: x = {closest_x:.1f}, ax + b = {closest_result}, distance from c = {closest_difference}")
	except ValueError as error:
		print(f"Error: {error}")

def explain_search_algorithms():
	print("Brute force search checks possible values one at a time until it finds the closest answer.")
	print("Brute force is very slow since it has to check lots of values one at a time.")
	print("Binary search is a better approach because it repeatedly cuts the search space in half making the attempts to find the solution much lower.")
	print("Which makes it better since it doesnt have to check every value one at a time, and that allows for way faster and more accurate results.")
	
def main_menu():
	while True:
		print("\nMain Menu")
		print("1. Basic calculator")
		print("2. Equation solver")
		print("3. Visualize search")
		print("4. Explain search algorithms")
		print("5. Exit")
		choice = input("Choose an option: ")

		if choice == "1":
			basic_calculate()
		elif choice == "2":
			equation_solver_menu()
		elif choice == "3":
			visualize_search()
		elif choice == "4":
			explain_search_algorithms()
		elif choice == "5":
			print("Goodbye!")
			break
		else:
			print("Error: Invalid choice. Please choose an option from 1 to 5.")

if __name__ == "__main__":
	main_menu()
