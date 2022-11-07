import database

MENU_PROMPT = """
Please choose the following options:
1) Add a new restaurant
2) see all restaurants
3) find a restaurant by Name
4) Return restaurant names where employees greater than the number entered
5) Exit

Your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            name = input("Enter the restaurant name: ")
            id = int(input("Enter the restaurant id: "))
            cuisine = input("Enter the restaurant cuisine: ")
            no_of_emp = int(input("Enter the number of employees: "))
            database.add_restaurant(connection, name, id, cuisine, no_of_emp)

            
        elif user_input == "2":
            restaurants = database.get_all_restaurants(connection)
            for restaurant in restaurants:
                print(restaurant)
            
        elif user_input == "3":
            name = input("Enter the restaurant name: ")
            restaurants = database.get_restaurant_by_name(connection, name)
            for restaurant in restaurants:
                print(restaurant)
        
        elif user_input == "4":
            employee_count = input("Enter the number of employees: ")
            restaurants = database.get_restaurant_by_employeecount(connection, employee_count)
            for restaurant in restaurants:
                print(restaurant)

        else:
            print("Invalid option, please try again.")

menu()
