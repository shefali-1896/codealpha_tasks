# Stock Portfolio Tracker Project

# Display welcome message
print("Welcome to Stock Portfolio Tracker")

# Create a dictionary to store stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

# Display available stocks
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "=", "$" + str(price))

# Create a variable to store total investment value
total_value = 0

# Keep taking stock details until the user enters 'done'
while True:

    # Ask the user to enter the stock name
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    # Stop taking input if the user enters 'done'
    if stock == "DONE":
        break

    # Check if the stock exists in the dictionary
    if stock in stock_prices:

        # Ask the user to enter the quantity
        quantity = int(input("Enter quantity: "))

        # Calculate the investment value
        investment = stock_prices[stock] * quantity

        # Add it to the total value
        total_value += investment

        # Display the investment for this stock
        print(stock, "=", quantity, "x", "$" + str(stock_prices[stock]), "=", "$" + str(investment))

    else:
        # Display a message if the stock name is invalid
        print("Stock not found!")

# Display the total investment value
print("\n----- Portfolio Summary -----")
print("Total Investment Value = $" + str(total_value))

# Thank the user
print("Thank you for using Stock Portfolio Tracker!")
