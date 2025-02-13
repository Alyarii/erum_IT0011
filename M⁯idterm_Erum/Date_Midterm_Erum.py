def convert_date(date_string):
    months = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }
    
    month, day, year = date_string.split("/")  
    day = str(int(day))  
    
    return f"{months[month]} {day}, {year}"

date_input = input("Enter the date (mm/dd/yyyy): ")
print("Date Output:", convert_date(date_input))