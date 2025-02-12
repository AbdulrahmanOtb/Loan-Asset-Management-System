
from sqlmodel import Session
import datetime
from enum import Enum
import hashlib
from Data_Modeling import Employee,GradeLevel,engine,Asset_Allocation,Financial_Loan,Payment_Method,Loan_Payment,PaidinFullType,Loan_Type,Type_of_Deposit,Auditor,loginStatus,AdminORnot,Department,Asset_Inventory


class Employees:
    
    @staticmethod
    def add (employee_number: str, name: str, employee_email: str, department:int, grade:str, address: str, phone_number: str, relative_number: str, iban: str, bank: str)  :

        EmployeeObj = Employee(Employee_Number = employee_number,Name = name ,Employee_email= employee_email,Department= department,Grade= grade,Address=address,Phone_Number = phone_number,Relative_Number= relative_number,IBAN= iban,Bank= bank)

        with Session (engine) as session :
            Employee_number_check = session.query(Employee).filter_by(Employee_Number = employee_number).first()
            
            if not employee_number.strip() or not name.strip() or not employee_email.strip()  or not address.strip() or not phone_number.strip() or not relative_number.strip() or not iban.strip() or not bank.strip():
                return "Error: Some Inputs Are Empty!"
            
            elif Employee_number_check:
                return "Error: Employee Number Already taken"
            
            elif len(phone_number) & len(relative_number) != 10:
                return "Error: Phone Number must be in 10 digits"
            
            elif phone_number == relative_number:
                    return "Error: Phone Number and Relative Number must be different"
            
            else:
                session.add(EmployeeObj)
                session.commit()
                return True

    @staticmethod
    def delete (id:int) :
        
        with Session (engine) as session:
            AssetsCheck = session.query(Asset_Allocation).filter_by(Employee_ID = id).first()
            LoansCheck = session.query(Financial_Loan).filter_by(Employee_ID = id).first()
            AuditorCheck = session.query(Auditor).filter_by(Employee_ID = id).first()
            EmployeeCheck = session.query(Employee).filter_by(id = id).first()
            DepartmentCheck = session.query(Department).filter_by(Manager_ID = EmployeeCheck.Employee_Number).first()
            if not AuditorCheck:
                if not LoansCheck:
                    if not AssetsCheck:
                        if not DepartmentCheck:
                            EmployeeObj = session.get(Employee,id) 
                            session.delete(EmployeeObj)
                            session.commit()
                            return True
    
    @staticmethod 
    def update (id:int,updates:dict):
        
        with Session(engine) as session :
            EmployeeObj = session.get(Employee,id) 
            ManagerCheck = session.query(Department).filter_by(Manager_ID = id).first()
          
        for key,value in updates.items() :
            if key == "Department":
                if ManagerCheck:
                    if value != ManagerCheck.id:
                        return False
            setattr(EmployeeObj,key,value)  
        session.add(EmployeeObj)
        session.commit()
        return True
       
    @staticmethod
    def check(key):
        with Session(engine) as session:
            employeeNumberCheck = session.query(Employee).filter_by(Employee_Number=key).first()
            
            employeeNameCheck = session.query(Employee).filter_by(Name=key).first()

            if employeeNumberCheck:
                return employeeNumberCheck.id
            elif not employeeNumberCheck:
                if employeeNameCheck:
                    return employeeNameCheck.id
                elif not employeeNameCheck:
                    return False

class Assets_Inventory : 
    
    @staticmethod
    def add (object_name : str,serial_Number: str , money_Value: int , quantity: int ,  location: str, description : str) : 
        
        AssetObj = Asset_Inventory (Object_Name=object_name,Serial_Number=serial_Number,Money_Value=money_Value,Quantity=quantity,Location=location,Description=description) 
        
        with Session (engine) as session : 
                if not object_name.strip() or not serial_Number.strip() or not money_Value.strip() or not quantity.strip() or not location.strip():
                    return False
                else :
                    session.add(AssetObj)
                    session.commit()
                    return True
    
    @staticmethod            
    def delete (asset_id : int) : 
        
        with Session (engine) as session :
            InventoryCheck = session.query(Asset_Inventory).filter_by(id = asset_id).first()
            AssetsCheck = session.query(Asset_Allocation).filter_by(Asset_ID = InventoryCheck.Object_Name).first()
            if not AssetsCheck:
                AssetObj = session.get(Asset_Inventory,asset_id) 
                session.delete(AssetObj)
                session.commit()
                return True
    
    @staticmethod        
    def update (id : int ,updates : dict) : 
        
         with Session (engine) as session :
             
            AssetObj = session.get(Asset_Inventory,id) 

            for key,value in updates.items() : 
                setattr(AssetObj,key,value)  
                session.add(AssetObj)
                session.commit()

    @staticmethod
    def check(object_name):
        with Session(engine) as session:
            asset_id = session.query(Asset_Inventory).filter_by(Object_Name=object_name).first()
            if asset_id:
                return asset_id.id
            else:
                return None

class Assets_Allocations :
    
    @staticmethod 
    def add(employee_id : int,asset_id :int,auditor_id : int ,department_id : str ,quantity : int, suggested_returndate: str, note: str) :
        
        AssetAllocationObj = Asset_Allocation(Employee_ID=employee_id,Asset_ID=asset_id,Auditor_ID=auditor_id,Department_ID=department_id,Quantity=quantity,Suggested_ReturnDate=suggested_returndate, Note= note)
        if note == "Personal":
            with Session (engine) as session : 
                EmployeeCheck = session.query(Employee).filter_by(id = employee_id).first()
                AssetCheck = session.query(Asset_Inventory).filter_by(id = asset_id).first()
                departmentcheck = session.query(Department).filter_by(id=department_id).first()

            Quantity = int(quantity)
            if not quantity.strip():
                return False
            elif AssetAllocationObj:
                if EmployeeCheck and AssetCheck :
                    if AssetCheck.Quantity == 0 :
                        return "Error: There is No Asset in Inventory maybe its Finished"
                    elif Quantity > AssetCheck.Quantity : 
                        return "Error: The Quantity Entered is Higher than the Asset Quantity in Inventory."
                    else:
                        AssetCheck.Quantity -= Quantity
                        setattr(AssetAllocationObj,"Department_ID","")
                        setattr(AssetCheck,"Quantity",AssetCheck.Quantity)
                        session.add(AssetAllocationObj)
                        session.add(AssetCheck)
                        session.commit()
                        return True
            
        elif note == "Department":
            with Session (engine) as session : 
                AssetCheck = session.query(Asset_Inventory).filter_by(id = asset_id).first()
                departmentcheck = session.query(Department).filter_by(id=department_id).first()
            
            Quantity = int(quantity)
            if not quantity.strip():
                return False
            elif AssetAllocationObj:
                if departmentcheck and AssetCheck :
                    if AssetCheck.Quantity == 0 :
                        return "Error: There is No Asset in Inventory maybe its Finished"
                    elif Quantity > AssetCheck.Quantity : 
                        return "Error: The Quantity Entered is Higher than the Asset Quantity in Inventory."
                    else:
                        AssetCheck.Quantity -= Quantity
                        setattr(AssetCheck,"Quantity",AssetCheck.Quantity)
                        session.add(AssetAllocationObj)
                        session.add(AssetCheck)
                        session.commit()
                        return True
            
    @staticmethod
    def update (id:int,updates:dict) :
        
        with Session(engine) as session:
            ReturnedAsset = session.query(Asset_Allocation).filter_by(id = id).first()
            InventoryAccess = session.query(Asset_Inventory).filter_by(id = ReturnedAsset.Asset_ID).first()
        
            InventoryAccess.Quantity += ReturnedAsset.Quantity
            setattr(InventoryAccess,"Quantity",InventoryAccess.Quantity)
            for key,value in updates.items() :
                setattr(ReturnedAsset,key,value)
            setattr(InventoryAccess,"Quantity",InventoryAccess.Quantity)
            session.add(InventoryAccess)
            session.add(ReturnedAsset)
            session.commit()

class Loan_payment:
    
    @staticmethod 
    def add(loan_id:int,auditor_id: int, amount: int, PaymentMethod: Payment_Method):
        timestamp = datetime.datetime.now()
        Payed = Loan_Payment(Loan_id=loan_id, Auditor_ID=auditor_id, Amount=amount, Payment_method=PaymentMethod, TimeStamp=timestamp)
        
        with Session(engine) as session:
            LoanCheck = session.query(Financial_Loan).filter_by(id = loan_id).first()
            
            if not loan_id.strip() or not auditor_id.strip() or not amount.strip():
                return False

            elif LoanCheck:
                loan = session.get(Financial_Loan,loan_id)
                Amount = int(amount)
                if Amount > loan.Amount :
                    return "Error: The payment amount is greater than the remaining amount of the loan."
                
                loan.Amount-= Amount
                setattr(loan,"Amount",loan.Amount)
                if loan.Amount == 0 : 
                    setattr(loan,"PaidinFull",PaidinFullType.Yes)
                    session.add(loan)
                    session.add(Payed)
                    session.commit()
                    return "Success: The loan has been paid in full."
                else:
                    session.add(loan)
                    session.add(Payed)
                    session.commit()
                return "The Loan has been add"
            
    @staticmethod 
    def update (id:int,updates:dict) :
        
        with Session(engine) as session : 
          PaymentObj = session.query(Loan_Payment).filter(Loan_Payment.id == id )
          AmountObj = session.query(Financial_Loan).filter(Financial_Loan.id == PaymentObj.Loan_id)
          
          AmountObj.Amount += PaymentObj.Amount
          setattr(AmountObj,"Amount", AmountObj.Amount)
        session.add(AmountObj)
        session.commit()
                
class Financial_Loans:
        
        @staticmethod
        def add(employee_id: int,auditor_id: int, amount: int ,type_of_deposit: Type_of_Deposit, loan_type: Loan_Type,suggested_ReturnDate= str) :
            
         FinancialObj = Financial_Loan(Employee_ID = employee_id,Auditor_ID = auditor_id,Amount= amount,Type_ofDeposit= type_of_deposit,LoanType= loan_type, Suggested_ReturnDate= suggested_ReturnDate)
        
         with Session (engine) as session : 
            EmployeeCheck = session.query(Employee).filter_by(id = employee_id).first()
            if not employee_id.strip() or not auditor_id.strip() or not amount.strip():
                return False
            elif EmployeeCheck:
                session.add(FinancialObj)
                session.commit()
                return True

class Auditors:
    
    @staticmethod
    def add (employee_id:int,username:str,password: str, admin : AdminORnot) :
        
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()
        
        AuditorObj = Auditor(Employee_ID=employee_id,Username=username,Password = hashed_password , Admin = admin)
        
        with Session (engine) as session : 
            EmployeeCheck = session.query(Employee).filter_by(id = employee_id).first()

            if not username.strip() or not password.strip():
                return False

            elif EmployeeCheck:
                session.add(AuditorObj)
                session.commit()
                return True
            
    @staticmethod
    def delete (id:int) :
        
        with Session (engine) as session :
            AuditorObj = session.get(Auditor,id) 
            session.delete(AuditorObj)
            session.commit()
    
    @staticmethod 
    def update (id:int,updates:dict) :
        
        with Session(engine) as session : 
          AuditorObj = session.get(Auditor,id) 
          
        for key,value in updates.items() : 
                setattr(AuditorObj,key,value)  
        session.add(AuditorObj)
        session.commit()

    @staticmethod 
    def login(Username: str,Password : str):
        with Session(engine) as session:
            auditorLogin = session.query(Auditor).filter_by(Username=Username).first()
            if auditorLogin:
                stored_password = auditorLogin.Password
                hash_object = hashlib.sha256(Password.encode())
                hashed_password = hash_object.hexdigest()
                
                if hashed_password == stored_password:
                    auditorLogin.Login_Status = loginStatus.Online
                    session.add(auditorLogin)
                    session.commit()
                    if auditorLogin.Admin == 'Yes':
                            return auditorLogin.Admin
                    else:
                            return auditorLogin.Admin
                else:
                    return False

    @staticmethod
    def logout(Username:str):

        with Session(engine) as session:

            auditorLogout: Auditor = session.query(Auditor).filter_by(Username=Username).first()


            if auditorLogout:
                auditorLogout.Login_Status = loginStatus.Offline
                setattr(auditorLogout,"Login_Status",loginStatus.Offline)
                session.add(auditorLogout)
                session.commit()

class Departments:
    
    @staticmethod
    def add(department_name: str,manager_id : int):
        
        DepartmentObj = Department(Department_Name=department_name)
        

        with Session (engine) as session:    
            DepartmentCheck = session.query(Department).filter_by(Department_Name=department_name,Manager_ID =manager_id).first()

            if not department_name.strip():
                return False
            elif DepartmentCheck:
                return "Error: The department Already Added"
            else:
                session.add(DepartmentObj)
                session.commit()
                return True
    
    @staticmethod
    def delete (id:int) :
        
        with Session (engine) as session :
            EmployeeCheck = session.query(Employee).filter_by(Department = id).first()
            AssetsCheck = session.query(Asset_Allocation).filter_by(Department_ID = id).first()
            if not EmployeeCheck:
                if not AssetsCheck:
                    DepartmentObj = session.get(Department,id) 
                    session.delete(DepartmentObj)
                    session.commit()
                    return True
            
    @staticmethod 
    def update (id:int,updates:dict) :
        
        with Session(engine) as session :
            DepartmentObj = session.get(Department,id) 

        for key,value in updates.items():
            setattr(DepartmentObj,key,value)
        session.add(DepartmentObj)
        session.commit()

    @staticmethod
    def check(key):
        with Session(engine) as session:
            department_id = session.query(Department).filter_by(Department_Name=key).first()

            if department_id:
                return department_id.id
        

#### TEST AREA ####


# Employees.add(employee_number="212222",name="Ammar",employee_email="Am@gmail.com",department=1,grade=GradeLevel.Five,address="Jeddah,ALmurjan",relative_number="0555555555",iban="11111111",bank="ALrajhi Bank",phone_number="0444444444")
# Employees.delete(id=2)
# Employees.update(id= 1,updates= {"Name":"Ammar" , "Department": DepartmentType.Research_and_development})
# print(Employees.Employee_Loans(employee_id=1))

# Auditors.add(employee_id= 4,username="bb",password = "11",admin = AdminORnot.No.value) 
# Auditors.delete(id=2)
# Auditors.update(id= 1,updates= {"Password":"11223344" , "Admin": AdminORnot.Yes})
#Auditors.update(id= 1,updates={"Password":"44444"})
# Auditors.login('AbdullahZh','000000')
# Auditors.login('AbdulrahmanOtb','44444')
# Auditors.logout('AbdulrahmanOtb')

# Assets_Allocations.add(employee_id= 3,auditor_id=1,department_id=1,asset_id=3,quantity=10,suggested_returndate=5 )         
#Assets_Allocations.update(id=1,auditor_id=2,returnstatus=Returned.Yes.value,return_date=datetime.datetime.now(),damage_status=DamageStatus.Half_Damaged.value)


# Financial_Loans.add(employee_id=1,auditor_id =2,amount= 80000,type_of_deposit= Type_of_Deposit.Bank,loan_type= Loan_Type.Personal,suggested_ReturnDate= datetime.datetime(2024,1,1))
# Loan_payment.add(loan_id=2,auditor_id=2,amount=10000,PaymentMethod=Payment_Method.Cash)
# Departments.add(department_name="Accounting and finance")
