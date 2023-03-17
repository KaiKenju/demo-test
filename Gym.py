import numpy as np
class Customer:
    def __init__(self, customer_id, name, dob, phone, date):
        self.customer_id = customer_id
        self.name = name
        self.dob = dob
        self.phone = phone
        self.date = date

class Course:
    def __init__(self,course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee

class FeeManager:
    def __init__(self, customer_id, customer_name, course_id, fee, pay, pay_amount):
        self.customer_id = customer_id
        self.customer_name=customer_name
        self.course_id=course_id
        self.fee=fee
        self.pay=pay
        self.pay_amount=pay_amount

class GymManager:
    def __init__(self):
        self.customers = []
        self.courses = []
        self.fees = []
        self.pay1 = []

    #data customer
    def input_customer_infor(self):
        print(f"---------- Customer ---------")
        customer_id = int(input("Enter the customer ID: "))
        customer_name = input("Enter customer name: ")
        customer_dob = input("Enter customer date of birth (DD-MM-YYYY): ")
        customer_phone = int(input("Enter customer phone: "))
        customer_date = input("Enter the JoinDate: ")
        customer = Customer(customer_id,customer_name,customer_dob, customer_phone, customer_date)
        self.customers.append(customer)
        

    #data course
    def input_course_infor(self):
        course_id = int(input("Enter the course ID: "))
        course_name = input("Enter the course name: ")
        course_fee = int(input("Enter the fee of course: "))
        course = Course(course_id,course_name,course_fee)
        self.courses.append(course)

    #find information of customer
    def find_customer(self):
        new_list1 = []
        new_list2 = []
        new_list3 = []
        new_list4 = []
        new_list5 = []
        n = input("Enter the name of customer: ")
        for customer in self.customers:
            new_list1.append(customer.name)
            new_list2.append(customer.customer_id)
            new_list3.append(customer.dob)
            new_list4.append(customer.phone)
            new_list5.append(customer.date)

        arr = np.array(new_list1)
        if n in arr:
            print(f"| {'Customer ID': <10} | {'Customer Name': <20} | {'DOB': <10} | {'Phone:' :<10} | {'Join Date': <10} |")
            print("-" * 77)
            for i in range(0,len(new_list1)):
                # ['hiep' ,'hieu' ,'hiep']
                if n == new_list1[i]: #hieu = 2
                    print(f"| {new_list2[i]:11} | {new_list1[i]:20} | {new_list3[i]:10} | {new_list4[i]:10} | {new_list5[i]:10} |")    
        else:           
            print(f"Error! Customer {n} hasn't found")

    # def to calculate money
    def cal_fee(self):
        fee_list1  = [] #contains cus_id
        fee_list2  = [] #contains cus_name
        fee_list3 = [] # contains course id [12 23 45]
        customer_id = int(input("Enter the customer ID: "))
        customer_name = input("Enter customer name: ")
        for customer in self.customers:
            fee_list1.append(customer.customer_id)
            fee_list2.append(customer.name)
        for course in self.courses:
            fee_list3.append(course.course_id) 
            self.fees.append(course.fee) # fee of course sever [150 250]
        
        arr1 = np.array(fee_list3) # [111 222]
        arr2 = np.array(self.fees) # fee of course sever [150 250]
        k = 0
        if customer_id in fee_list1 and customer_name in fee_list2:
            x = int(input("Enter the  course id  to pay the fee: "))
            #check course id in arr1 yes or not!
            if x in arr1:
                for j in range(0,len(arr1)): # j-> 0 , 1 ; arr1 = [1 2]
                     
                    if x == arr1[j]: #location:1  
                        y = int(input("Enter the fee of the course: "))
                        for i in range(0, len(arr2)): # , range(0,2) ;fees = [150 250]
                            if i==j:
                                k = arr2[i] - y
                                      
                print(f"| {'Customer ID': <10} | {'Customer name': <20} | {'Course ID': <10} | {'Fee (USD)': <10} | {'Pay (USD)': <10} | {'Amount owed': <10} |")
                print("-" * 91)
                print(f"| {customer_id:11} | {customer_name:20} | {x:10} | {arr2[i]:10} | {y:10} | {k:11} |")
                self.pay1.append(FeeManager(customer_id,customer_name,x,arr2[i],y,k))# error
                
            else:
                print(f"Something wrong! The customer {customer_name} or the customer id {customer_id} have not exits.")
    
        else:
            print("Error! Customer has not found")
    
    #show customer have not pay
    def show_customer_unpaid(self):
        print(f"| {'No':5} | {'Customer ID': <10} | {'Customer name': <10} | {'Course ID': <10} | {'Fee (USD)': <10} | {'Pay (USD)': <10} | {'Amount owed': <10} |")
        print("-" * 92)
        for index,feepay in enumerate(self.pay1):
            print(f"| {index:5} | {feepay.customer_id:10} | {feepay.customer_name:14} | {feepay.course_id:10} | {feepay.fee:10} | {feepay.pay:10} | {feepay.pay_amount:11} |")
        print("-" * 92)

    #show list of customer
    def show_customer(self):
        print("List of customer: ")
        print(f"| {'No':<5} | {'Customer ID': <10} | {'Customer Name': <20} | {'DOB': <10} | {'Phone' :<10} | {'Join Date' : <10} |")
        print("-" * 85)
        for index,customer in enumerate(self.customers):
            print(f"| {index:5} | {customer.customer_id:11} | {customer.name:20} | {customer.dob:10} | {customer.phone:10} | {customer.date:10} |")
        print("-" * 85)

    #show list of course
    def show_course(self):
        print("List of course: ")
        print(f"| {'No': <5} | {'Course ID' :<10} | {'Course Name': <20} | {'Cost':<10} |")
        print("-" *58)
        for index,course in enumerate(self.courses):
            print(f"| {index:5} |{course.course_id:11} | {course.name:20} | {course.fee:10} |")
        print("-" *58)

    #main
    def main(self):
        while(True):
            print("\n")
            print("------------ Gym Management System -------------")
            print("1. Add new customer ")
            print("2. Add the course ")
            print("3. Show all customer ")
            print("4. Show all courses ")
            print("5. Find the customer ")
            print("6. Input fee of customer ")
            print("7. Show customer unpaid ")
            print("0. Exit ")
            
            temp = int(input("Your option: "))
            if temp == 1:
                self.input_customer_infor()
            elif temp == 2:
                self.input_course_infor()
            elif temp == 3:
                self.show_customer()
            elif temp == 5:
                self.find_customer()
            elif temp == 4:
                self.show_course()
            elif temp == 6:
                self.cal_fee()
            elif temp == 0:
                break
            elif temp == 7:
                self.show_customer_unpaid()
            else:
                print("Invalid choice! ")
gymm = GymManager()
gymm.main()