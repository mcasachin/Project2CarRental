class Rental():

    def __init__(self,thislist: list, thisRentedlist:list):
        self.thislist = thislist
        self.thisRentedlist = thisRentedlist

    def IntitateRental(self,idc2,cur_Cus) -> list:
        from datetime import datetime
        try:
            if (len(self.thislist) == 0):
                print("\nNo Inventory Avaiable, Kindly check later.")
            else:
                for i in range(len(self.thislist)):
                    if (self.thislist[i]["id"] == idc2):
                        print("\n **** Rent Agreement created for "+cur_Cus.displayName()+" , Below are the details ****")
                        print("\nCar Number", self.thislist[i]["id"])
                        print("Car Brand and Model", self.thislist[i]["brand"],self.thislist[i]["model"])
                        print("Rent per Miniute for Car is",self.thislist[i]["perhourrent"]," and Rent Start Time is ", datetime.now())
                        self.thislist[i]["starttime"]=datetime.now()
                        self.thisRentedlist.append(self.thislist[i])
                        del self.thislist[i]
                        break
                    elif (i == len(self.thislist) - 1):
                       print("Car Number not found, Please check Car Number again")
            return self.thislist
        except Exception as e:
            print("\n Error in IntitateRental", e)

    def CalculateRent(self,carId,) -> list:
        from datetime import datetime
        try:
            if(len(self.thisRentedlist)==0):
                print("Car Number not found, Please check Car Number again")
            for i in range(len(self.thisRentedlist)):
                if (self.thisRentedlist[i]["id"] == carId):
                    currentTime = datetime.now()
                    inputTime = self.thisRentedlist[i]["starttime"]
                    # inputTime = datetime.strptime(inputdTime, '%Y %m %d %H %M %S')
                    DateDiff = currentTime - inputTime
                    # DateDiffHours = int(DateDiff.total_seconds())
                    DateDiffHours = int(DateDiff.total_seconds() / 60)
                    print('\n ****  Rent Slip for car Usage *****')
                    print("\nStart Time of Car usage is", str(inputTime))
                    print("End Time Usage of car in Mins is", str(currentTime))
                    print("Total Time Usage of car in Mins is", str(DateDiffHours))
                    print("Rent per Miniute for Car Number", carId, 'is', self.thisRentedlist[i]["perhourrent"])
                    print("\nTotal Rent for Car Number", carId, 'is', int(self.thisRentedlist[i]["perhourrent"]) * DateDiffHours)
                    self.thislist.append(self.thisRentedlist[i])
                    del self.thisRentedlist[i]
                    break
                elif (i == len(self.thisRentedlist) - 1):
                    print("Car Number not found, Please check Car Number again")
            return self.thislist
        except Exception as e:
            print("\n Error in CalculateRent", e)