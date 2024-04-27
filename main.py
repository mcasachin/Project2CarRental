import datetime
import Classes.Cars as instntCar
import Classes.Rental as instntRental
import Classes.Customer as instntCustomer

car1 = {
    "id": "BM1",
    "brand": "BMW",
    "model": "X1",
    "perhourrent": 1000,
    "starttime": datetime.datetime.now()
}
car2 = {
    "id": "NG1",
    "brand": "Nissan",
    "model": "GTR",
    "perhourrent": 1500,
    "starttime": datetime.datetime.now()
}
car3 = {
    "id": "AQ1",
    "brand": "Audi",
    "model": "Q1",
    "perhourrent": 5000,
    "starttime": datetime.datetime.now()
}

def back(thislist,thisrentedlist,cur_Cus):
    input('\nPress ENTER to return to main menu...')
    menu(thislist,thisrentedlist,cur_Cus)

def menu(thislist: list, thisRentedlist : list,cur_Cus : str):

    # print('Enter Customer Name                5')
    print('\nDisplay all Available Cars         1')
    print('Rent a Car                         2')
    print('Return the Car and Pay Bill        3')
    print('Exit                               4')
    try:
        choice = int(input('\nChoose your options: '))
    except Exception as e:
        print("\nInvalid choice.",e)
        back(thislist, thisrentedlist,cur_Cus)
    else:
        if choice == 1:
            try:
                cur_Car= instntCar.Cars(thislist)
                thislist=cur_Car.displayCars()
            except Exception as e:
                print("\n1 Invalid choice.", e)
            back(thislist,thisrentedlist,cur_Cus)
        elif choice == 2:
            try:
                cur_Rental = instntRental.Rental(thislist, thisRentedlist)
                idc2 = input('\nEnter Car Number : ')
                thislist = cur_Rental.IntitateRental(idc2,cur_Cus);
            except Exception as e:
                print("\n2 Invalid choice.", e)
            back(thislist, thisrentedlist,cur_Cus)
        elif choice == 3:
            try:
                cur_Rental = instntRental.Rental(thislist, thisRentedlist)
                idc3 = input('\nEnter Car Number : ')
                thislist = cur_Rental.CalculateRent(idc3);
            except Exception as e:
                print("\n3 Invalid choice.", e)
            back(thislist,thisrentedlist,cur_Cus)
        elif choice == 4:
            print('\nThanks for using Car Rental System. Bye!')
            return
        else:
            print('\n4 Invalid choice.')
            back(thislist,thisrentedlist,cur_Cus)

if __name__ == '__main__':
    thislist = [car1, car2, car3]
    thisrentedlist=[]
    print('\nWelcome to Star Car Rental')
    name= input('\nEnter Customer  Name : ')
    print(        '\nHi ' + name + ', Below is the Car Rental Menu-Please press the number to selct from menu  ')
    cur_Cus = instntCustomer.Customer(name)
    menu(thislist,thisrentedlist,cur_Cus)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

