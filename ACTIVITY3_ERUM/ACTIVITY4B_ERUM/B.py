import csv

def load_currency_data(file_path="currency.csv"):
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ISO-8859-1']
    
    for encoding in encodings:
        try:
            currencies = {}
            with open(file_path, 'r', encoding=encoding) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    code = row['code'].strip().upper()
                    name = row['name'].strip()
                    rate = float(row['rate'].strip())
                    currencies[code] = {'name': name, 'rate': rate}
            print(f"Successfully loaded using {encoding} encoding")
            return currencies
        except UnicodeDecodeError:
            print(f"Failed to load with {encoding}, trying next...")
        except FileNotFoundError:
            print("Error: The file 'currency.csv' was not found.")
            return None
        except Exception as e:
            print(f"Error reading the file: {e}")
            return None

    print(" Could not decode the file with any of the attempted encodings.")
    return None

def convert_currency(amount, target_currency, currencies):
    if target_currency in currencies:
        rate = currencies[target_currency]['rate']
        return amount * rate
    else:
        print("Error: Invalid currency code.")
        return None

def main():
    currencies = load_currency_data()
    if not currencies:
        return  

    try:
        amount = float(input("Enter amount in USD: "))
        target_currency = input("Enter target currency code (e.g., PHP, EUR): ").upper()

        result = convert_currency(amount, target_currency, currencies)

        if result is not None:
            print(f"\n{amount:.2f}USD is equal to {result:.2f} {target_currency}")
    except ValueError:
        print("Invalid input! Please enter a number for the amount.")

if __name__ == "__main__":
    main()
