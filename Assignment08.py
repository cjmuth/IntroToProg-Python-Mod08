# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CMuth,12/4/2022,Modified code to complete assignment 8
# CMuth,12/5/2022,Added error handlers to read_data_from_file, add_data_to_list, and print_current_list_items
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
bln_changes = None

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:

    """
    # TODO: Add Code for Product class (Constructor, Properties, & Methods)
    # -- Constructor --
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price

    # -- Properties --
    @property
    def product_name(self):
        return str(self.__product_name).title()

    # Ensure the product name contains at least one non-numeric character
    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception('Names must contain at least one non-numeric character.')

    @property
    def product_price(self):
        return str(self.__product_price)

    # Verify the price was given as a numeric value
    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except:
            raise Exception('Prices must be numeric.')

    # -- Methods --
    def to_string(self):
        ''' Returns object data in a comma separated string of values

        :return: (string) CSV data
        '''
        product_data_csv = self.product_name + ', $' + self.product_price
        return product_data_csv

    def __str__(self):
        ''' Overrides Python's built-in method to
        return object data in a comma separated string of values

        :return: (string) CSV data
        '''
        return self.to_string()

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_products):
        """ Reads data from a file into a list of objects

        :param file_name: (string) with name of file:
        :param list_of_products: (list) you want filled with file data:
        :return: (list) of products
        """
        try:
            list_of_products.clear()  # clear current data
            file = open(file_name, "r")
            for line in file:
                name, price = line.split(",")
                product = Product(name, price)
                list_of_products.append(product)
            file.close()
            return list_of_products
        except:
            print('\n*********************')
            print('File ' + file_name + ' was not found. No existing data loaded.')
            print('*********************')

    # TODO: Add Code to process data to a file
    @staticmethod
    def write_data_to_file(file_name, list_of_products, bln_changes):
        """ Writes data from a list of objects to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of products
        """
        if bln_changes:
            try:
                # Open the file in write mode
                objFile = open(file_name, 'w')
                # Loop through objects in table list
                for product in list_of_products:
                    # Extract values, concatenate as string, write to text file
                    objFile.write(product.product_name + ',' + product.product_price + '\n')
                # Close text file
                objFile.close()
                print('\nData has been saved.')
                bln_changes = False
            except:
                print('\nData was not saved.')
                bln_changes = True
            return bln_changes
        else:
            print('\nNo changes found.  Data was not saved.')

class DataProcessor:

    @staticmethod
    def add_data_to_list(product_name, product_price, list_of_products):
        """ Adds data to a list of objects

        :param product_name: (string) with name of a product:
        :param product_price: (string) with price of a product:
        :param list_of_products: (list) you want filled with file data:
        :return: (list) of products
        """
        if not list_of_products:
            list_of_products = []
        try:
            name = str(product_name).strip()
            price = str(product_price).strip().replace('$','')
            product = Product(name, price)
            list_of_products.append(product)
            bln_changes = True
        except Exception as e:
            print('\n*********************')
            print('Invalid entry: ' + str(e))
            print('*********************')
            bln_changes = False
        # Pass the updated product list back to the main program
        return list_of_products, bln_changes

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

        input_product_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """
    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_list_items(list_of_products):
        try:
            for product in list_of_products:
                print(product)
        except:
            print('\n*********************')
            print('No existing data to display.')
            print('*********************')

    # TODO: Add code to get product data from user
    @staticmethod
    def input_product_data():
        """  Gets product name and price values to be added to the list

        :return: (string, string) with task and priority
        """
        # Get new proiduct name from user
        name = input('What is the product name? ')
        # Get price of new product from user
        price = input('What is the price? ')
        # Pass the user given values back to the main program
        return name, price


# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while True:
    # Show user a menu of options
    IO.print_menu_items()
    # Get user's menu option choice
    choice_str = IO.input_menu_choice()
    if choice_str.strip() == '1':
        # Show user current data in the list of product objects
        IO.print_current_list_items(lstOfProductObjects)
    elif choice_str.strip() == '2':
        # Let user add data to the list of product objects
        name, price = IO.input_product_data()
        lstOfProductObjects, bln_changes = DataProcessor.add_data_to_list(name, price, lstOfProductObjects)
    elif choice_str.strip() == '3':
        # Let user save current data to file and exit program
        bln_changes = FileProcessor.write_data_to_file(strFileName, lstOfProductObjects, bln_changes)
    elif choice_str.strip() == '4':
        if bln_changes:
            print('You have unsaved changes.')
            choice_str = input('Do you wish to save them? (y/n) ')
            if choice_str.lower() == 'y':
                FileProcessor.write_data_to_file(strFileName, lstOfProductObjects, bln_changes)
            else:
                print('\nData was not saved.')
        input('\nGoodbye.\n\nPress enter to close window.')
        break
    else:
        print('\n*********************')
        print('Invalid selection: Please choose from 1-4.')
        print('*********************')
# Main Body of Script  ---------------------------------------------------- #
