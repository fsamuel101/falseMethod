while True:
    from tabulate import tabulate
    import math

    table_data = [['Iteration', 'Xl', 'Xr', 'Yl', 'Yr', 'Xn', 'Yn', 'Error']]

    equation = input("Enter the function: ")
    Xl = float(input("Enter the Xl: "))
    Xr = float(input("Enter the Xr: "))
    i = int(input("Enter the number of Iteration you want: "))

    def false_position(func, a, b, i):
        xLeft = a
        xRight = b
        err = ''
        xN = 0
        iteration = 1

        while i >= iteration:

            yLeft = func(xLeft)
            yRight = func(xRight)
            old = xN
            try:
                xN = xLeft + (xRight - xLeft) * (yLeft / (yLeft - yRight))
            except ZeroDivisionError:
                print("Error: Division by zero. Please choose different Xl and Xr values.")
                return

            yN = func(xN)

            # this is for the error
            if iteration != 1 and xN != 0:  # Check if xN is not zero
                err = ((xN - old) / xN) * 100

            table_data.append([iteration, xLeft, xRight, yLeft, yRight, xN, yN, err])

            if abs(yRight - 0) > abs(yN - 0):
                xLeft = xRight
                xRight = xN
            else:
                xLeft = xN
                xRight = xRight

            iteration += 1

    def user_function(x):
        try:
            result = eval(equation.replace('^', '**'), {"math": math, "x": x})
            return result
        except Exception as e:
            print(f"Error in evaluating the function: {e}")
            return float('nan')

    false_position(user_function, Xl, Xr, i)

    print(tabulate(table_data, headers='firstrow', tablefmt="fancy_grid"))

    # Ask the user if they want to try again or exit
    choice = input("Do you want to try again? (y/n): ").lower()
    if choice != 'y':
        break
