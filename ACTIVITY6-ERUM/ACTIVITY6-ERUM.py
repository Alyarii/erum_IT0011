class Item:
    def __init__(item, id, name, description, price):
        item.id = id
        item.name = name
        item.description = description
        item.price = price

class ItemManager:
    def __init__(item):
        item.items = {}
    
    def create_item(item, id, name, description, price):
        try:
            if not isinstance(id, str) or not id.strip():
                raise ValueError("ID cannot be empty and must be a string")
            
            if id in item.items:
                raise ValueError(f"Item with ID {id} already exists")
                
            if not isinstance(name, str) or not name.strip():
                raise ValueError("Name cannot be empty and must be a string")
                
            if not isinstance(description, str):
                raise ValueError("Description must be a string")
                
            if not isinstance(price, (int, float)) or price < 0:
                raise ValueError("Price must be a positive number")
            
            new_item = Item(id, name, description, price)
            item.items[id] = new_item
            return f"Item {id} created successfully"
            
        except ValueError as e:
            return f"Error creating item: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def read_item(item, id):
        try:
            if not id or id not in item.items:
                raise ValueError(f"Item with ID {id} not found")
                
            found_item = item.items[id]
            return {
                "ID": found_item.id,
                "Name": found_item.name,
                "Description": found_item.description,
                "Price": found_item.price
            }
            
        except ValueError as e:
            return f"Error reading item: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def read_all_items(item):
        try:
            if not item.items:
                return "No items found"
                
            result = []
            for id, found_item in item.items.items():
                result.append({
                    "ID": found_item.id,
                    "Name": found_item.name,
                    "Description": found_item.description,
                    "Price": found_item.price
                })
            return result
            
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def update_item(item, id, name=None, description=None, price=None):
        try:
            if not id or id not in item.items:
                raise ValueError(f"Item with ID {id} not found")
                
            found_item = item.items[id]
            
            if name is not None:
                if not isinstance(name, str) or not name.strip():
                    raise ValueError("Name cannot be empty and must be a string")
                found_item.name = name
                
            if description is not None:
                if not isinstance(description, str):
                    raise ValueError("Description must be a string")
                found_item.description = description
                
            if price is not None:
                if not isinstance(price, (int, float)) or price < 0:
                    raise ValueError("Price must be a positive number")
                found_item.price = price
                
            return f"Item {id} updated successfully"
            
        except ValueError as e:
            return f"Error updating item: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
    
    def delete_item(item, id):
        try:
            if not id or id not in item.items:
                raise ValueError(f"Item with ID {id} not found")
                
            del item.items[id]
            return f"Item {id} deleted successfully"
            
        except ValueError as e:
            return f"Error deleting item: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"


def display_menu():
    print("\n===== ITEM MANAGEMENT SYSTEM =====")
    print("1. Add a new item")
    print("2. View an item")
    print("3. View all items")
    print("4. Update an item")
    print("5. Delete an item")
    print("6. Exit")
    print("==================================")
    return input("Enter your choice (1-6): ")


def main():
    item_manager = ItemManager()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            print("\n----- Add New Item -----")
            id = input("Enter ID: ")
            name = input("Enter name: ")
            description = input("Enter description: ")
            try:
                price = float(input("Enter price: "))
                print(item_manager.create_item(id, name, description, price))
            except ValueError:
                print("Error: Price must be a valid number")
                
        elif choice == "2":
            print("\n----- View Item -----")
            id = input("Enter ID of item to view: ")
            result = item_manager.read_item(id)
            print(result)
                
        elif choice == "3":
            print("\n----- All Items -----")
            print(item_manager.read_all_items())
                
        elif choice == "4":
            print("\n----- Update Item -----")
            id = input("Enter ID of item to update: ")
            print("Leave blank for fields you don't want to update")
            name = input("Enter new name (or press Enter to skip): ") or None
            description = input("Enter new description (or press Enter to skip): ") or None
            
            price = None
            price_str = input("Enter new price (or press Enter to skip): ")
            if price_str:
                try:
                    price = float(price_str)
                except ValueError:
                    print("Error: Price must be a valid number")
                    continue
            
            print(item_manager.update_item(id, name, description, price))
                
        elif choice == "5":
            print("\n----- Delete Item -----")
            id = input("Enter ID of item to delete: ")
            print(item_manager.delete_item(id))
                
        elif choice == "6":
            print("\nThank you for using the Item Management System! Exiting the program.")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()