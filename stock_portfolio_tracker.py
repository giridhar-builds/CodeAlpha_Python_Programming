# =====================================================================
# TASK 2: STOCK PORTFOLIO TRACKER
# =====================================================================
def track_portfolio():
    # Hardcoded dictionary defining stock prices
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOG": 175.0,
        "MSFT": 420.0,
        "AMZN": 185.0
    }
    
    portfolio = {}
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks in system:", ", ".join(stock_prices.keys()))
    
    # Input collection loop
    while True:
        symbol = input("\nEnter stock symbol to add (or type 'done' to calculate): ").strip().upper()
        if symbol == 'DONE':
            break
            
        if symbol not in stock_prices:
            print(f"Stock symbol '{symbol}' not found in the price registry. Please try again.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            continue
            
        # Add or update stock quantity in portfolio
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} shares of {symbol} to your portfolio.")

    # Calculations and Display Results
    print("\n==========================================")
    print("           PORTFOLIO SUMMARY              ")
    print("==========================================")
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<12}{'Total Value':<12}")
    print("-" * 46)
    
    total_portfolio_value = 0.0
    report_lines = []
    
    for symbol, qty in portfolio.items():
        price = stock_prices[symbol]
        investment_value = qty * price
        total_portfolio_value += investment_value
        
        line = f"{symbol:<10}{qty:<10}${price:<11.2f}${investment_value:<11.2f}"
        print(line)
        report_lines.append(line)
        
    print("-" * 46)
    print(f"Total Portfolio Investment Value: ${total_portfolio_value:.2f}")
    print("==========================================")
    
    
    try:
        with open("portfolio_summary.txt", "w") as file:
            file.write("==========================================\n")
            file.write("           PORTFOLIO SUMMARY              \n")
            file.write("==========================================\n")
            file.write(f"{'Stock':<10}{'Quantity':<10}{'Price':<12}{'Total Value':<12}\n")
            file.write("-" * 46 + "\n")
            for line in report_lines:
                file.write(line + "\n")
            file.write("-" * 46 + "\n")
            file.write(f"Total Portfolio Investment Value: ${total_portfolio_value:.2f}\n")
            file.write("==========================================\n")
        print("\nPortfolio summary successfully saved to 'portfolio_summary.txt'")
    except IOError:
        print("\nError: Could not save portfolio summary to file.")

if __name__ == "__main__":
    track_portfolio()
