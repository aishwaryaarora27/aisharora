import heapq #importing heap queue
from collections import defaultdict,OrderedDict #importing the defaultdict and OrderedDict from collections module
class Car:
  def __init__(self,registration_number,age): #Constructor of class Car used to initialize variables
    self.registration_number=registration_number
    self.age=age
  def __str__(self): #returnable function returning Registration number and age of class Car
    return "Car [registration_number="+self.registration_number+",age="+self.age+"]"
class ParkingLot:
  def __init__(self):  #Constructor of class Parkinglot
    self.registration_slot_mapping=dict()
    self.age_registration_mapping=defaultdict(list)
    self.slot_car_mapping=OrderedDict()
    self.available_parking_lots=[]
  def create_parking_lot(self,total_slots):  #Function creating Parking Lot
    print("Created parking of {} slots".format(total_slots))
    for i in range(1,total_slots+1):
      heapq.heappush(self.available_parking_lots,i)  #Inserting value of i in heapq,namely, available_parking_lots
    return True
  def get_nearest_slot(self):  #function to allot the slot nearest to entry gate for parking
    return heapq.heappop(self.available_parking_lots) if self.available_parking_lots else None
  def leave(self,slot_to_be_freed):  #function to free up the parking slot after departure of any car
    found = None
    for registration_no, slot in self.registration_slot_mapping.items(): #for loop to browse through the dictionary
      if slot==slot_to_be_freed:
        found=registration_no
    if found:
      heapq.heappush(self.available_parking_lots, slot_to_be_freed)
      del self.registration_slot_mapping[found]
      car_to_leave=self.slot_car_mapping[slot_to_be_freed]
      self.age_registration_mapping[car_to_leave.age].remove(found)
      del self.slot_car_mapping[slot_to_be_freed]
      print('''Slot number {} vacated, the car with vehicle registration number "{}" left the space, the driver of the car was of age {}'''.format(slot_to_be_freed,found,car_to_leave.age))
  def park(self,car):  #function to perform parking of cars
    slot_no=self.get_nearest_slot()
    print('''Car with vehicle registration number "{}" has been parked at slot number {}'''.format(car.registration_number,slot_no))
    self.slot_car_mapping[slot_no]=car
    self.registration_slot_mapping[car.registration_number]=slot_no
    self.age_registration_mapping[car.age].append(car.registration_number)
    return slot_no
  def registration_numbers_for_cars_with_age(self,age): #this function is printing the registration numbers of cars whose drivers possess the given age
    print(self.age_registration_mapping[age])
  def slot_numbers_for_cars_with_age(self,age): # function printing the slot numbers for cars whose drivers are of given age
    l=list(self.registration_slot_mapping[reg_no] for reg_no in self.age_registration_mapping[age])
    s=""
    for i in l:
      s=s+str(i)+","
    print(s[:len(s)-1])
  def slot_number_for_registration_number(self,registration_number): #printing slot numbers for given registration numbers of vehicles
    slot_number=None
    if registration_number in self.registration_slot_mapping:
      slot_number=self.registration_slot_mapping[registration_number]
      print(slot_number)
      return slot_number
    else:
      print("Not Found")
      return slot_number
   