
from sqlmodel import SQLModel,Field,create_engine,Session,UniqueConstraint
from enum import Enum
import datetime
from typing import Optional

# Enumeration Classes  : 

class GradeLevel(str,Enum) : 
    One = "One"
    Two = "Two"
    Three = "Three" 
    Four = "Four"
    Five = "Five"
    Six = "Six"

    
class AdminORnot(str,Enum) : 
    Yes = "Yes"
    No = "No"
    
    
class DamageStatus(str,Enum):
    Healthy = "Healthy"
    Damaged = "Damaged"
    Half_Damaged = "Half_Damaged"
    
    
class Payment_Method(str,Enum):
    Catch_Receipt = 'Catch_Receipt'
    Cash = 'Cash'
    Bills = 'Bills'
    Bank_Transfer = 'Bank_Transfer'
    
class Returned(str,Enum):
    Yes = "Yes it is returned"
    No = "Not Returned" 
    

class PaidinFullType(str,Enum):
    Yes = "Yes"
    No = "No"
    
class Loan_Type(str,Enum) :
    Work = "For work" 
    Personal = "Personal"
    
class Type_of_Deposit(str,Enum) : 
    Cash = "Cash"
    Bank_Transfer = "Bank_Transfer"

class loginStatus(str,Enum):
    Online = "Online"
    Offline = "Offline"
    

# Data Modeling Classes : 


class Employee (SQLModel,table = True) :
    __tablename__ = "Employees" 
    id: int = Field(default=None,primary_key= True)
    Employee_Number : str 
    Name : str 
    Employee_email : str 
    Department : int = Field(foreign_key="Department.id")
    Grade : str 
    Address : str 
    Phone_Number : str 
    Relative_Number : str 
    IBAN : str 
    Bank : str 
    
class Department(SQLModel, table=True):
    __tablename__ = 'Department'
    id: int = Field(default=None, primary_key=True)
    Department_Name: str 
    Manager_ID : Optional[int] = Field(foreign_key=Employee.id)
    
class Auditor(SQLModel,table = True) :
    __tablename__ = "Auditors"
    id : int = Field(default=None,primary_key=True)
    Employee_ID: int = Field(foreign_key=Employee.id)
    Username : str 
    Password : str
    Login_Status : Optional [loginStatus] = Field(default=loginStatus.Offline)
    Admin : AdminORnot
    
 
class Asset_Inventory(SQLModel, table=True):
    __tablename__ = 'Asset_Inventory'
    id: int = Field(default=None, primary_key=True)
    Object_Name : str
    Description : Optional[str] = Field(default="")
    Serial_Number: str
    Money_Value: int
    Quantity: int
    Location: str
    
    
class Asset_Allocation(SQLModel, table = True):
    __tablename__ = "Asset_Allocations"
    id: int = Field(default = None, primary_key = True)
    Asset_ID : int = Field(foreign_key=Asset_Inventory.id)
    Employee_ID: int = Field(foreign_key=Employee.id)
    Department_ID: Optional[int] = Field(default=None,foreign_key=Department.id)
    Auditor_ID: int = Field(foreign_key=Auditor.id)
    Quantity: int
    Allocation_Date: Optional [datetime.datetime] = Field(default_factory=datetime.datetime.now)
    Is_Returned: Optional[Returned] = Field(default=Returned.No)
    Return_Date: Optional[datetime.datetime] = Field(default_factory= None)
    Suggested_ReturnDate: str
    Given_Status: Optional[DamageStatus] = Field(default=DamageStatus.Healthy)
    Return_Status: Optional[DamageStatus] = Field(default="Not Returned")
    Note:Optional[str] = Field(default="")
    
    
class Financial_Loan(SQLModel,table=True) :
    __tablename__ = "Financial_Loans"
    id : int = Field(default=None,primary_key=True)
    Employee_ID: int = Field(foreign_key=Employee.id)
    Auditor_ID: int = Field(foreign_key=Auditor.id) 
    Amount : int 
    Type_ofDeposit :  str
    LoanType : str
    PaidinFull : Optional[PaidinFullType] = Field(default=PaidinFullType.No.value)
    Allocation_Date: Optional [datetime.datetime] = Field(default_factory=datetime.datetime.now)
    Suggested_ReturnDate: str
    
    

class Loan_Payment(SQLModel, table=True):
    __tablename__ = 'Loan_payments'
    id: int = Field(default=None, primary_key=True)
    Loan_id: int = Field(foreign_key=Financial_Loan.id)
    Auditor_ID: int = Field(foreign_key=Auditor.id)
    Amount: int
    TimeStamp: Optional [datetime.datetime] = Field(default_factory=datetime.datetime.now)
    Payment_method: Payment_Method
    Note:Optional[str] = Field(default="")
 
engine = create_engine("sqlite:///Project_database.db") 
SQLModel.metadata.create_all(engine)
