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

class GymManager:
    def __init__(self):
        self.customers = []
        self.courses = []
        self.fees = {}

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
        print(new_list1) # display to check, if you're sure about that, then remove it
        arr = np.array(new_list1)
        c = 0
        if n in arr:
            for i in range(0,len(new_list1)):
                c=c+1
                # ['hiep' ,'hieu' ,'hiep']
                if n == new_list1[i]: #hieu = 2
                    print(f"Customer {new_list1[i]} has found")
                    print(f"| {'Customer ID': <10} | {'Customer Name': <20} | {'DOB': <10} | {'Phone:' :<10} | {'Join Date': <10} |")
                    print("-" * 77)
                    print(f"| {new_list2[i]:11} | {new_list1[i]:20} | {new_list3[i]:10} | {new_list4[i]:10} | {new_list5[i]:10} |")
                    
                    for k in range(c,len(new_list1)-1):
                        if n == new_list1[k+1]:
                            print(f"| {new_list2[k+1]:11} | {new_list1[k+1]:20} | {new_list3[k+1]:10} | {new_list4[k+1]:10} | {new_list5[k+1]:10} |")
                    print("-" * 77)
                    break
                    
            print(f"Error! Customer {n} hasn't found")
                

    #show list of customer
    def show_customer(self):
        print("List of customer: ")
        print(f"| {'Customer ID': <10} | {'Customer Name': <20} | {'DOB': <10} | {'Phone' :<10} | {'Join Date' : <10} |")
        print("-" * 77)
        for customer in self.customers:
            print(f"| {customer.customer_id:11} | {customer.name:20} | {customer.dob:10} | {customer.phone:10} | {customer.date:10} |")
        print("-" * 77)

    #show list of course
    def show_course(self):
        print("List of course: ")
        print(f"| {'Course ID:' :<10} | {'Course Name': <20} | {'Fee':<10} |")
        print("-" *50)
        for course in self.courses:
            print(f"| {course.course_id:10} | {course.name:20} | {course.fee:10} |")
        print("-" *50)

    def main(self):
        while(True):
            print("\n")
            print("------------ Gym Management System -------------")
            print("1. Add new customer ")
            print("2. Add the course ")
            print("3. Show all customer ")
            print("4. Show all courses ")
            print("5. Find the customer ")
            print("6. Exit ")

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
                break
gymm = GymManager()
gymm.main()