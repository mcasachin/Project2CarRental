
class Cars():
    def __init__(self,thislist :list):
        self.thislist=thislist

    def displayCars(self) -> list:
        try:
            if (len(self.thislist) == 0):
                print("\nNo Inventory Avaiable, Kindly check later.")
            else:
                print("Please find below is aviable Inventory of Cars with Brand Model details.\n ")
                for x in self.thislist:
                    print("Car Number", x["id"], "is", x["brand"], x["model"], "and per hour rent is", x["perhourrent"])
            return self.thislist;
        except Exception as e:
            print("\n Error in displayCars", e)