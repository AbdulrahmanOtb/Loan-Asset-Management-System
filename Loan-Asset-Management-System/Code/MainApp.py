
import sys
import os

from sqlmodel import Session
from datetime import date,datetime
from PyQt5 import QtWidgets, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableView, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QIntValidator, QKeySequence , QIcon,QPixmap
from PyQt5.QtCore import Qt,QLocale
import hashlib

from MainWindow import MainWindow
from SecondMainWindow import SecondMainWindow
from AddLoanWindow import AddLoanWindow
from AddPaymentWindow import AddPaymentWindow
from ReturnAssetWindow import ReturnAssetWindow
from AddEmployeeWindow import AddEmployeeWindow
from UpdateEmployeeWindow import UpdateEmployeeWindow
from AddUserWindow import AddUserWindow
from UpdateUserWindow import UpdateUserWindow
from AddAssetAllocationWindow import AddAssetAllocationWindow
from AssetDepartmentAllocationWindow import AssetDepartmentAllocationWindow
from AddAssetInventory import AddAssetInventory
from EditAssetInventory import EditAssetInventory
from AddDepartmentWindow import AddDepartmentWindow
from EditDepartmentWindow import EditDepartmentWindow
from Translation_list import Translate

from Data_Operations import Auditors , Employees, Assets_Allocations, Loan_payment, Financial_Loans,Departments,Assets_Inventory
from Data_Modeling import Employee,engine,Auditor,Financial_Loan,Asset_Allocation,Loan_Payment,Department,Asset_Inventory, Payment_Method,Loan_Type,AdminORnot,Returned,GradeLevel,DamageStatus,Type_of_Deposit,loginStatus

import IconsForWindows


class MainApp:
    
    def __init__(self) -> None:
        self.App = QtWidgets.QApplication(sys.argv)
        logo = QPixmap(":/AppIcon/AppIcon.png")
        self.app_icon = QIcon(logo)
        self.Window = MainWindow()
        self.Window.setWindowIcon(self.app_icon)
        self.SecondWindow = SecondMainWindow()
        self.SecondWindow.setWindowIcon(self.app_icon)
        self.AddLoanWindow = AddLoanWindow()
        self.AddLoanWindow.setWindowIcon(self.app_icon)
        self.AddPaymentWindow = AddPaymentWindow()
        self.AddPaymentWindow.setWindowIcon(self.app_icon)
        self.ReturnAssetWindow = ReturnAssetWindow()
        self.ReturnAssetWindow.setWindowIcon(self.app_icon)
        self.AddEmployeeWindow = AddEmployeeWindow()
        self.AddEmployeeWindow.setWindowIcon(self.app_icon)
        self.UpdateEmployeeWindow = UpdateEmployeeWindow()
        self.UpdateEmployeeWindow.setWindowIcon(self.app_icon)
        self.AddUserWindow = AddUserWindow()
        self.AddUserWindow.setWindowIcon(self.app_icon)
        self.UpdateUserWindow = UpdateUserWindow()
        self.UpdateUserWindow.setWindowIcon(self.app_icon)
        self.AddAssetAllocationWindow = AddAssetAllocationWindow()
        self.AddAssetAllocationWindow.setWindowIcon(self.app_icon)
        self.AddAssetInventoryWindow = AddAssetInventory()
        self.AddAssetInventoryWindow.setWindowIcon(self.app_icon)
        self.EditAssetInventoryWindow = EditAssetInventory()
        self.EditAssetInventoryWindow.setWindowIcon(self.app_icon)
        self.AddDepartmentWindow = AddDepartmentWindow()
        self.AddDepartmentWindow.setWindowIcon(self.app_icon)
        self.EditDepartmentWindow = EditDepartmentWindow()
        self.EditDepartmentWindow.setWindowIcon(self.app_icon)
        self.AssetDepartmentAllocationWindow = AssetDepartmentAllocationWindow()
        self.AssetDepartmentAllocationWindow.setWindowIcon(self.app_icon)
        self.IntType = QIntValidator()
        self.Actions()
        self.get_all_department_names()
        self.get_all_object_names_ToComboBox()
        self.Data_Vaidation()
        self.Row_Selection()
        self.translation(0)
        self.loadData()



    ### Language ###     
    def translation(self,lang):
     
     ## Login Page ##
     self.Window.Program_Title.setText(Translate('Asset management', lang))
     self.Window.Username_Input.setPlaceholderText(Translate('Username_Input', lang))
     self.Window.Password_Input.setPlaceholderText(Translate('Password_Input', lang))
     self.Window.Login_Pushbutton.setText(Translate('Login_Pushbutton', lang))
     
     ## Main Page ##
     self.SecondWindow.Add_Employee_Button.setText(Translate('Add_Employee_Button', lang))
     self.SecondWindow.Edit_Employee_Button.setText(Translate('Edit_Employee_Button', lang))
     self.SecondWindow.Delete_Employee_Button.setText(Translate('Delete_Employee_Button', lang))
     self.SecondWindow.Employees_TitleOf_Table_2.setText(Translate('Employees_TitleOf_Table_2', lang))
     self.SecondWindow.SearchEmployee_title_3.setText(Translate('SearchEmployee_title_3', lang))
     self.SecondWindow.Add_Auditor_Button.setText(Translate('Add_Auditor_Button', lang))
     self.SecondWindow.Delete_Assets_Inventory_TitleOf_Table_4.setText(Translate('Delete_Assets_Inventory_TitleOf_Table_4', lang))
     self.SecondWindow.Add_Department_Button_3.setText(Translate('Add_Department_Button_3', lang))
     self.SecondWindow.Edit_Department_Button_3.setText(Translate('Edit_Department_Button_3', lang))
     self.SecondWindow.Delete_Department_Button_3.setText(Translate('Delete_Department_Button_3', lang))
     self.SecondWindow.Delete_Assets_Inventory_TitleOf_Table_3.setText(Translate('Delete_Assets_Inventory_TitleOf_Table_3', lang))
     self.SecondWindow.SearchDepartment_title_5.setText(Translate('SearchDepartment_title_5', lang))
     self.SecondWindow.Add_Assets_Inventory_Button_2.setText(Translate('Add_Assets_Inventory_Button_2', lang))
     self.SecondWindow.Edit_Assets_Inventory_Button_2.setText(Translate('Edit_Assets_Inventory_Button_2', lang))
     self.SecondWindow.Delete_Assets_Inventory_Button_2.setText(Translate('Delete_Assets_Inventory_Button_2', lang))
     self.SecondWindow.SearchAssets_Inventory_title_3.setText(Translate('SearchAssets_Inventory_title_3', lang))
     self.SecondWindow.Auditors_TitleOf_Table_2.setText(Translate('Auditors_TitleOf_Table_2', lang))
     self.SecondWindow.Edit_Auditor_Button.setText(Translate('Edit_Auditor_Button', lang))
     self.SecondWindow.Delete_Auditor_Button.setText(Translate('Delete_Auditor_Button', lang))
     self.SecondWindow.SearchAuditors_title_2.setText(Translate('SearchAuditors_title_2', lang))
     self.SecondWindow.Add_FinanciaLoan_Button_6.setText(Translate('Add_FinanciaLoan_Button_6', lang))
     self.SecondWindow.FinancialLoans_TitleOf_Table_7.setText(Translate('FinancialLoans_TitleOf_Table_7', lang))
     self.SecondWindow.LoanPayments_TitleOf_Table_8.setText(Translate('LoanPayments_TitleOf_Table_8', lang))
     self.SecondWindow.AssetAllocations_TitleOf_Table_4.setText(Translate('AssetAllocations_TitleOf_Table_4', lang))
     self.SecondWindow.Add_Asset_Button_3.setText(Translate('Add_Asset_Button_3', lang))
     self.SecondWindow.Return_Asset_Button_3.setText(Translate('Return_Asset_Button_3', lang))
     self.SecondWindow.SearchAsset_title_4.setText(Translate('SearchAsset_title_4', lang))
     self.SecondWindow.Logout_button.setText(Translate('Logout_button', lang))
     self.SecondWindow.Refresh_Button.setText(Translate('Refresh_Button', lang))
     self.SecondWindow.Add_Payment_Button_5.setText(Translate('Add_Payment_Button_5', lang))
     self.SecondWindow.AddDepartmentAsset_Button.setText(Translate('AddDepartmentAsset_Button', lang))
     self.SecondWindow.Employees_And_Auditors_Tab.setTabText(0,Translate('EmployeesTab', lang))
     self.SecondWindow.Employees_And_Auditors_Tab.setTabText(1,Translate('Assets_inventory_Tab', lang))
     self.SecondWindow.Employees_And_Auditors_Tab.setTabText(2,Translate('DepartmentTab', lang))
     self.SecondWindow.Employees_And_Auditors_Tab.setTabText(3,Translate('Auditors', lang))
     self.SecondWindow.Financial_OR_Assest_Tab.setTabText(0,Translate('Financial_Tab_2', lang))
     self.SecondWindow.Financial_OR_Assest_Tab.setTabText(1,Translate('AssetAllocations_Tab_2', lang))
     
     ## Asset Pages ##
     self.AddAssetAllocationWindow.AddAsset_Title_3.setText(Translate('AddAsset_Title_3', lang))
     self.AddAssetAllocationWindow.TitleOfEmployeeID_AddAsset_3.setText(Translate('TitleOfEmployeeID_AddAsset_3', lang))
     self.AddAssetAllocationWindow.TitleOf_ObjectName_AddAsset_3.setText(Translate('TitleOf_ObjectName_AddAsset_3', lang))
     self.AddAssetAllocationWindow.TitleOfQuantity_AddAsset_3.setText(Translate('TitleOfQuantity_AddAsset_3', lang))
     self.AddAssetAllocationWindow.TitleOfAuditorID_AddAsset_3.setText(Translate('TitleOfAuditorID_AddAsset_3', lang))
     self.AddAssetAllocationWindow.SuggestedReturnDate_Title_AddAsset_3.setText(Translate('SuggestedReturnDate_Title_AddAsset_3', lang))
     self.AddAssetAllocationWindow.Save_AddAsset_Button_3.setText(Translate('Save_AddAsset_Button_3', lang))
     self.AddAssetAllocationWindow.Cancel_AddAsset_Button_3.setText(Translate('Cancel_AddAsset_Button_3', lang))
     self.ReturnAssetWindow.Auditors_TitleOf_Table_2.setText(Translate('Return Asset', lang))
     self.ReturnAssetWindow.SearchLoans_title_6.setText(Translate('SearchLoans_title_6', lang))
     self.ReturnAssetWindow.TitleOf_DamageStatus_ReturnedAsset_3.setText(Translate('TitleOf_DamageStatus_ReturnedAsset_3', lang))
     self.ReturnAssetWindow.TitleOf_Notes_ReturnedAsset_4.setText(Translate('TitleOf_Notes_ReturnedAsset_4', lang))
     self.ReturnAssetWindow.TitleOf_Returned_ReturnedAsset_3.setText(Translate('TitleOf_Returned_ReturnedAsset_3', lang))
     self.ReturnAssetWindow.Save_ReturnedAsset_Button_5.setText(Translate('Save_ReturnedAsset_Button_5', lang))
     self.ReturnAssetWindow.Cancel_ReturnedAsset_Button_5.setText(Translate('Cancel_ReturnedAsset_Button_5', lang))
     self.AssetDepartmentAllocationWindow.AddAsset_Title_3.setText(Translate('AddAsset_Title_3', lang))
     self.AssetDepartmentAllocationWindow.TitleOfEmployeeID_AddAsset_3.setText(Translate('Department Name', lang))
     self.AssetDepartmentAllocationWindow.TitleOf_ObjectName_AddAsset_3.setText(Translate('Object Name', lang))
     self.AssetDepartmentAllocationWindow.TitleOfQuantity_AddAsset_3.setText(Translate('Quantity', lang))
     self.AssetDepartmentAllocationWindow.TitleOfAuditorID_AddAsset_3.setText(Translate('TitleOfAuditorID_AddAsset_3', lang))
     self.AssetDepartmentAllocationWindow.SuggestedReturnDate_Title_AddAsset_3.setText(Translate('SuggestedReturnDate_Title_AddAsset_3', lang))
     self.AssetDepartmentAllocationWindow.Save_AddAsset_Button_3.setText(Translate('Add', lang))
     self.AssetDepartmentAllocationWindow.Cancel_AddAsset_Button_3.setText(Translate('Cancel', lang))
     self.AddAssetInventoryWindow.Add_Assets_Inventory_Title_3.setText(Translate('Add_Assets_Inventory_Title_3', lang))
     self.AddAssetInventoryWindow.TitleOf_ObjectName_AddAsset_4.setText(Translate('TitleOf_ObjectName_AddAsset_4', lang))
     self.AddAssetInventoryWindow.TitleOf_SerialNumber_AddAsset_4.setText(Translate('TitleOf_SerialNumber_AddAsset_4', lang))
     self.AddAssetInventoryWindow.TitleOfQuantity_AddAsset_4.setText(Translate('TitleOfQuantity_AddAsset_4', lang))
     self.AddAssetInventoryWindow.TitleOf_MoneyValue_AddAsset_4.setText(Translate('TitleOf_MoneyValue_AddAsset_4', lang))
     self.AddAssetInventoryWindow.TitleOf_Location_AddAsset_5.setText(Translate('TitleOf_Location_AddAsset_5', lang))
     self.AddAssetInventoryWindow.TitleOfdescription_AddAsset_4.setText(Translate('TitleOfdescription_AddAsset_4', lang))
     self.AddAssetInventoryWindow.Save_AddAssets_Inventory_Button_4.setText(Translate('Save_AddAssets_Inventory_Button_4', lang))
     self.AddAssetInventoryWindow.Cancel_AddAssets_Inventory_Button_4.setText(Translate('Cancel_AddAssets_Inventory_Button_4', lang))
     self.EditAssetInventoryWindow.Add_Assets_Inventory_Title_4.setText(Translate('Add_Assets_Inventory_Title_4', lang))
     self.EditAssetInventoryWindow.TitleOf_ObjectName_EditAsset_5.setText(Translate('TitleOf_ObjectName_EditAsset_5', lang))
     self.EditAssetInventoryWindow.TitleOf_SerialNumber_EditAsset_5.setText(Translate('TitleOf_SerialNumber_EditAsset_5', lang))
     self.EditAssetInventoryWindow.TitleOfQuantity_EditAsset_5.setText(Translate('TitleOfQuantity_EditAsset_5', lang))
     self.EditAssetInventoryWindow.TitleOf_MoneyValue_EditAsset_5.setText(Translate('TitleOf_MoneyValue_EditAsset_5', lang))
     self.EditAssetInventoryWindow.TitleOf_Location_EditAsset_6.setText(Translate('TitleOf_Location_EditAsset_6', lang))
     self.EditAssetInventoryWindow.TitleOfdescription_EditAsset_5.setText(Translate('TitleOfdescription_EditAsset_5', lang))
     self.EditAssetInventoryWindow.Save_UpdateAssets_Inventory_Button_3.setText(Translate('Save_UpdateAssets_Inventory_Button_3', lang))
     self.EditAssetInventoryWindow.Cancel_UpdateAssets_Inventory_Button_3.setText(Translate('Cancel_UpdateAssets_Inventory_Button_3', lang))

     ## Department Pages ##
     self.AddDepartmentWindow.Add_Department_TitleOf_Table_4.setText(Translate('Add_Department_TitleOf_Table_4', lang))
     self.AddDepartmentWindow.TitleOf_DepartmentName_AddDepartment_7.setText(Translate('Name', lang))
     self.AddDepartmentWindow.TitleOfManagerID_AddDepartment_2.setText(Translate('Manager ID', lang))
     self.AddDepartmentWindow.Save_AddDepartment_Button_3.setText(Translate('Add', lang))
     self.AddDepartmentWindow.Cancel_AddDepartment_Button_3.setText(Translate('Cancel', lang))
     self.EditDepartmentWindow.Add_Department_TitleOf_Table_4.setText(Translate('Add_Department_TitleOf_Table_4', lang))
     self.EditDepartmentWindow.TitleOf_DepartmentName_EditDepartment_7.setText(Translate('Name', lang))
     self.EditDepartmentWindow.TitleOfManagerID_AddDepartment_2.setText(Translate('Manager ID', lang))
     self.EditDepartmentWindow.Save_EditDepartment_Button_3.setText(Translate('Update', lang))
     self.EditDepartmentWindow.Cancel_EditDepartment_Button_3.setText(Translate('Cancel', lang))

     #Finanical Pages ##
     self.AddLoanWindow.AddLoan_Title_4.setText(Translate('AddLoan_Title_4', lang))
     self.AddLoanWindow.TitleOfEmployeeID_AddLoan_4.setText(Translate('TitleOfEmployeeID_AddLoan_4', lang))
     self.AddLoanWindow.TitleOfAmount_AddLoan_4.setText(Translate('TitleOfAmount_AddLoan_4', lang))
     self.AddLoanWindow.TitleOfAuditorID_AddLoan_4.setText(Translate('TitleOfAuditorID_AddLoan_4', lang))
     self.AddLoanWindow.TypeofDeposit_title_4.setText(Translate('TypeofDeposit_title_4', lang))
     self.AddLoanWindow.LoanType_title_4.setText(Translate('LoanType_title_4', lang))
     self.AddLoanWindow.SuggestedReturnDate_Title_AddLoan_4.setText(Translate('SuggestedReturnDate_Title_AddLoan_4', lang))
     self.AddLoanWindow.Save_AddLoan_Button_4.setText(Translate('Save_AddLoan_Button_4', lang))
     self.AddLoanWindow.Cancel_AddLoan_Button_4.setText(Translate('Cancel_AddLoan_Button_4', lang))
     self.AddPaymentWindow.AddPayment_Title_2.setText(Translate('AddPayment_Title_2', lang))
     self.AddPaymentWindow.TitleOfLoanID_AddPayment_2.setText(Translate('TitleOfLoanID_AddPayment_2', lang))
     self.AddPaymentWindow.TitleOfAmount_AddPayment_2.setText(Translate('TitleOfAmount_AddPayment_2', lang))
     self.AddPaymentWindow.TitleOfAuditorID_AddPayment_2.setText(Translate('TitleOfAuditorID_AddPayment_2', lang))
     self.AddPaymentWindow.PaymentMethod_title_2.setText(Translate('PaymentMethod_title_2', lang))
     self.AddPaymentWindow.Save_AddPayment_Button_3.setText(Translate('Save_AddPayment_Button_3', lang))
     self.AddPaymentWindow.Cancel_AddPayment_Button_3.setText(Translate('Cancel_AddPayment_Button_3', lang))

     ## Employee Pages ##
     self.AddEmployeeWindow.AddEmployee_Title_2.setText(Translate('AddEmployee_Title_2', lang))
     self.AddEmployeeWindow.TitleOfEmployeeID_AddEmployee_2.setText(Translate('TitleOfEmployeeID_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOfEmployeeName_AddEmployee_2.setText(Translate('TitleOfEmployeeName_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOfEmployeeEmail_AddEmployee_2.setText(Translate('TitleOfEmployeeEmail_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOf_EmployeePhoneNumber_AddEmployee_2.setText(Translate('TitleOf_EmployeePhoneNumber_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOf_EmployeeAddress_AddEmployee_2.setText(Translate('TitleOf_EmployeeAddress_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOf_EmployeeRelativeNumber_AddEmployee_2.setText(Translate('TitleOf_EmployeeRelativeNumber_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOf_EmployeeIBAN_AddEmployee_2.setText(Translate('TitleOf_EmployeeIBAN_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOf_EmployeeBank_AddEmployee_2.setText(Translate('TitleOf_EmployeeBank_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOf_EmployeeDepartment_AddEmployee_2.setText(Translate('TitleOf_EmployeeDepartment_AddEmployee_2', lang))
     self.AddEmployeeWindow.TitleOf_EmployeeGrade_AddEmployee_2.setText(Translate('TitleOf_EmployeeGrade_AddEmployee_2', lang))
     self.AddEmployeeWindow.Save_AddEmployee_Button.setText(Translate('Save_AddEmployee_Button', lang))
     self.AddEmployeeWindow.Cancel_AddEmployee_Button.setText(Translate('Cancel_AddEmployee_Button', lang))
     self.UpdateEmployeeWindow.UpdateEmployee_Title_2.setText(Translate('UpdateEmployee_Title_2', lang))
     self.UpdateEmployeeWindow.TitleOfEmployeeID_UpdateEmployee_2.setText(Translate('TitleOfEmployeeID_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.TitleOfEmployeeName_UpdateEmployee_3.setText(Translate('TitleOfEmployeeName_UpdateEmployee_3', lang))
     self.UpdateEmployeeWindow.TitleOfEmployeeEmail_UpdateEmployee_2.setText(Translate('TitleOfEmployeeEmail_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.TitleOf_EmployeePhoneNumber_UpdateEmployee_2.setText(Translate('TitleOf_EmployeePhoneNumber_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.TitleOf_EmployeeAddress_UpdateEmployee_2.setText(Translate('TitleOf_EmployeeAddress_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.TitleOf_EmployeeRelativeNumber_UpdateEmployee_2.setText(Translate('TitleOf_EmployeeRelativeNumber_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.TitleOf_EmployeeIBAN_UpdateEmployee_2.setText(Translate('TitleOf_EmployeeIBAN_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.TitleOf_EmployeeBank_UpdateEmployee_3.setText(Translate('TitleOf_EmployeeBank_UpdateEmployee_3', lang))
     self.UpdateEmployeeWindow.TitleOf_EmployeeIBAN_UpdateEmployee_2.setText(Translate('TitleOf_EmployeeIBAN_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.TitleOf_EmployeeDepartment_UpdateEmployee_2.setText(Translate('TitleOf_EmployeeDepartment_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.TitleOf_EmployeeGrade_UpdateEmployee_2.setText(Translate('TitleOf_EmployeeGrade_UpdateEmployee_2', lang))
     self.UpdateEmployeeWindow.Save_UpdateEmployee_Button_3.setText(Translate('Save_UpdateEmployee_Button_3', lang))
     
     ## User Pages ##
     self.AddUserWindow.AddAuditor_Title_2.setText(Translate('AddAuditor_Title_2', lang))
     self.AddUserWindow.TitleOfEmployeeID_AddAuditor_2.setText(Translate('TitleOfEmployeeID_AddAuditor_2', lang))
     self.AddUserWindow.TitleOfUsername_AddAuditor_2.setText(Translate('TitleOfUsername_AddAuditor_2', lang))
     self.AddUserWindow.TitleOfPassword_AddAuditor_2.setText(Translate('TitleOfPassword_AddAuditor_2', lang))
     self.AddUserWindow.TitleOfAdmin_AddAuditor_2.setText(Translate('TitleOfAdmin_AddAuditor_2', lang))
     self.AddUserWindow.Save_AddAuditor_Button.setText(Translate('Save_AddAuditor_Button', lang))
     self.AddUserWindow.Cancel_AddAuditor_Button.setText(Translate('Cancel_AddAuditor_Button', lang))
     self.UpdateUserWindow.UpdateAuditor_Title_2.setText(Translate('UpdateAuditor_Title_2', lang))
     self.UpdateUserWindow.TitleOfEmployeeID_UpdateAuditor_2.setText(Translate('TitleOfEmployeeID_UpdateAuditor_2', lang))
     self.UpdateUserWindow.TitleOfUsername_UpdateAuditor_2.setText(Translate('TitleOfUsername_UpdateAuditor_2', lang))
     self.UpdateUserWindow.TitleOfPassword_UpdateAuditor_2.setText(Translate('TitleOfPassword_UpdateAuditor_2', lang))
     self.UpdateUserWindow.TitleOfAdmin_UpdateAuditor_2.setText(Translate('TitleOfAdmin_UpdateAuditor_2', lang))
     self.UpdateUserWindow.UpdateAuditor_Button.setText(Translate('UpdateAuditor_Button', lang))
     self.UpdateUserWindow.Cancel_UpdateAuditor_Button.setText(Translate('Cancel_UpdateAuditor_Button', lang))

     ## Error Messages ##
     self.success_msg = Translate('Success', lang)
     self.edited_msg = Translate('The Data has been edited!', lang)
     self.success_msg = Translate('Success', lang)
     self.edited_msg = Translate('The Data has been edited!', lang)
     self.error_msg=Translate('Error',lang)
     self.Emptyinputs_msg= Translate('Some Inputs Are Empty!',lang)
     self.Add_msg= Translate('Added', lang)
     self.LoginSecAdmin_msg=Translate('Login successful! + You are Admin',lang)
     self.LoginSecNotAdmin_msg=Translate('Login successful! + You are Not Admin',lang)
     self.warning_msg=Translate('Warning',lang)
     self.failedLogin_msg=Translate('Wrong Login',lang)
     self.EmployeeNumbererror_msg=Translate('Employee Number Already taken',lang)
     self.EmployeePhoneNumError_msg=Translate('Phone Number must be in 10 digits',lang)
     self.EmployeeRelativeError_msg=Translate('Phone Number and Relative Number must be different',lang)
     self.NoAsset=Translate('There is No Asset in the Inventory',lang)
     self.EmployeeDepError_msg=Translate('This employee is a manager in a department!',lang)
     self.EmployeeSelectError_msg=Translate('Please Select an Employee to Edit the information',lang)
     self.DeletedEmployee_msg=Translate('The Employee has been Deleted!',lang)
     self.cantDeleteEmployee_msg=Translate('Employee Can not be deleted',lang)
     self.WrongEmployeenumber_msg=Translate('wrong employee number',lang)
     self.AlreadyUser_msg=Translate('Employee already a user',lang)
     self.selectusererror_msg=Translate('Please Select a user',lang)
     self.QuantityHigher_msg=Translate('The Quantity Entered is Higher than the Asset Quantity in Inventory.',lang)
     self.assetAlready_msg=Translate('Asset Already returned',lang)
     self.Returnassetselect_msg=Translate('Please Select The Asset to Return it',lang)
     self.RetunedAsset_msg=Translate('The Asset has been Returned!',lang)
     self.signedEmployeedDepartment_msg=Translate('There is an employee signed to this department',lang)
     self.selectDepartment_msg=Translate('Please Select a Department',lang)
     self.DepartmentAdded_msg=Translate('The Department Already Added',lang)
     self.higherAmount_msg=Translate('The Payment Amount Is Higher Than The Remaining Amount Of The Loan',lang)
     self.addPaymentmsg = Translate('Please Select a Loan',lang)
     self.PaidFullmsg = Translate('The loan is paid in full',lang)
     

     ## Headers Of the Tables ##
     Employeecolumn_labels = ['id','Employee number', 'Name', 'Email', 'Department', 'Grade', 'Address', 'Phone number', 'Relative number', 'IBAN', 'Bank']
     for col, label in enumerate(Employeecolumn_labels):
            header_item = QtWidgets.QTableWidgetItem(Translate(label, lang))
            self.SecondWindow.Employees_Table_2.setHorizontalHeaderItem(col, header_item)

     AssetsInvwntory_column_labels = ['id','Object Name', 'Description', 'Serial Number', 'Money value', 'Quantity', 'Location']
     for col, label in enumerate(AssetsInvwntory_column_labels):
            Assetheader_item = QtWidgets.QTableWidgetItem(Translate(label, lang))
            self.SecondWindow.Assets_Inventory_Table.setHorizontalHeaderItem(col, Assetheader_item)

     Department_column_labels = ['id','Name', 'Manager ID']
     for col, label in enumerate(Department_column_labels):
            Departmentheader_item = QtWidgets.QTableWidgetItem(Translate(label, lang))
            self.SecondWindow.Assets_Inventory_Table_2.setHorizontalHeaderItem(col, Departmentheader_item)

     Users_column_labels = ['id','Employee Name', 'Employee number','Username','Password','Login status','Admin']
     for col, label in enumerate(Users_column_labels):
            User_item = QtWidgets.QTableWidgetItem(Translate(label, lang))
            self.SecondWindow.Auditors_Table_2.setHorizontalHeaderItem(col, User_item)

     FinancialLoans_column_labels = ['id','Employee Name', 'Employee number','Department','Auditor ID','Amount','Type of deposit','Loan type','Paid in full','Allocation date','Suggested ReturnDate']
     for col, label in enumerate(FinancialLoans_column_labels):
            FinancialLoansheader_item = QtWidgets.QTableWidgetItem(Translate(label, lang))
            self.SecondWindow.FinancialLoans_Table_4.setHorizontalHeaderItem(col, FinancialLoansheader_item)
     
     LoanPayment_column_labels = ['id','Loan ID', 'Auditor Name','Amount','Timestamp','PaymentMethod']
     for col, label in enumerate(LoanPayment_column_labels):
            LoanPaymentheader_item = QtWidgets.QTableWidgetItem(Translate(label, lang))
            self.SecondWindow.LoanPayments_Table_5.setHorizontalHeaderItem(col, LoanPaymentheader_item)
     AssetAllocation_column_labels = ['id','Employee Name','Department', 'Auditor Name','Object Name','Quantity','Allocation date','ReturnDate','Given Status','Is Returned ','Suggested ReturnDate','Returned status','Serial Number','Money value','Notes']
     for col, label in enumerate(AssetAllocation_column_labels):
            AssetAllocationheader_item = QtWidgets.QTableWidgetItem(Translate(label, lang))
            self.SecondWindow.AssetAllocations_Table_3.setHorizontalHeaderItem(col, AssetAllocationheader_item)
     
     ## Combo Boxes ##
     grade_levels = [Translate(grade_level.name,lang) for grade_level in GradeLevel]
     self.AddEmployeeWindow.EmployeeGrade_Enum_AddEmployee_2.clear()
     self.UpdateEmployeeWindow.EmployeeGrade_Enum_UpdateEmployee_2.clear()
     self.AddEmployeeWindow.EmployeeGrade_Enum_AddEmployee_2.addItems(grade_levels)
     self.UpdateEmployeeWindow.EmployeeGrade_Enum_UpdateEmployee_2.addItems(grade_levels)

     Admin_or_not = [Translate(admin_or_not.name,lang) for admin_or_not in AdminORnot]
     self.AddUserWindow.Admin_Enum_AddAudtior_2.clear()
     self.UpdateUserWindow.Admin_Enum_UpdateAudtior_2.clear()
     self.AddUserWindow.Admin_Enum_AddAudtior_2.addItems(Admin_or_not)
     self.UpdateUserWindow.Admin_Enum_UpdateAudtior_2.addItems(Admin_or_not)
     
     
     Damage_status = [Translate(damage_status.name,lang) for damage_status in DamageStatus]
     self.ReturnAssetWindow.DamageStatus_Enum_3.clear()
     self.ReturnAssetWindow.DamageStatus_Enum_3.addItems(Damage_status)

     Payment_methods = [Translate(payment_method.name,lang) for payment_method in Payment_Method]
     self.AddPaymentWindow.PaymentMethod_Enum_2.clear()
     self.AddPaymentWindow.PaymentMethod_Enum_2.addItems(Payment_methods)

     Return_status = [Translate(return_status.name,lang) for return_status in Returned]
     self.ReturnAssetWindow.Returned_Enum_3.clear()
     self.ReturnAssetWindow.Returned_Enum_3.addItems(Return_status)
    
     loan_type = [Translate(loantype.name,lang) for loantype in Loan_Type]
     self.AddLoanWindow.LoanType_Enum_4.clear()
     self.AddLoanWindow.LoanType_Enum_4.addItems(loan_type)

     Deposit_type = [Translate(Deposit.name,lang) for Deposit in Type_of_Deposit]
     self.AddLoanWindow.TypeofDeposit_Enum_4.clear()
     self.AddLoanWindow.TypeofDeposit_Enum_4.addItems(Deposit_type)
     
     ## App Direction ##  
     if lang == 1 :
        self.SecondWindow.setLayoutDirection(Qt.RightToLeft)
        self.Window.setWindowTitle(Translate('Asset management',1))
        self.SecondWindow.setWindowTitle(Translate('Asset management',1))
        self.AddEmployeeWindow.setWindowTitle(Translate('Add Employee',1))
        self.UpdateEmployeeWindow.setWindowTitle(Translate('Edit Employee',1))
        self.AddUserWindow.setWindowTitle(Translate('Add User',1))
        self.AddLoanWindow.setWindowTitle(Translate('Add Loan',1))
        self.AddPaymentWindow.setWindowTitle(Translate('Add Payment',1))
        self.ReturnAssetWindow.setWindowTitle(Translate("Return Asset",1))
        self.UpdateUserWindow.setWindowTitle(Translate("Edit User",1))
        self.AddAssetAllocationWindow.setWindowTitle(Translate("Add Asset Allocation",1))
        self.AssetDepartmentAllocationWindow.setWindowTitle(Translate("Add Asset Allocation",1))
        self.AddAssetInventoryWindow.setWindowTitle(Translate("Add Asset In Inventory",1))
        self.EditAssetInventoryWindow.setWindowTitle(Translate("Edit Asset In Inventory",1))
        self.AddDepartmentWindow.setWindowTitle(Translate("Add Department",1))
        self.EditDepartmentWindow.setWindowTitle(Translate("Edit Department",1))
        self.lang = 1
        self.ShortcutForButtons()
     elif lang == 0 : 
         self.SecondWindow.setLayoutDirection(Qt.LeftToRight)
         self.Window.setWindowTitle("Asset Management")
         self.SecondWindow.setWindowTitle("Asset Management")
         self.AddEmployeeWindow.setWindowTitle("Add Employee")
         self.UpdateEmployeeWindow.setWindowTitle("Edit Employee")
         self.AddUserWindow.setWindowTitle("Add User")
         self.AddLoanWindow.setWindowTitle("Add Loan")
         self.AddPaymentWindow.setWindowTitle("Add Payment")
         self.ReturnAssetWindow.setWindowTitle("Return Asset")
         self.UpdateUserWindow.setWindowTitle("Edit User")
         self.AddAssetAllocationWindow.setWindowTitle("Add Asset Allocation")
         self.AssetDepartmentAllocationWindow.setWindowTitle("Add Asset Allocation")
         self.AddAssetInventoryWindow.setWindowTitle("Add Asset In Inventory")
         self.EditAssetInventoryWindow.setWindowTitle("Edit Asset In Inventory")
         self.AddDepartmentWindow.setWindowTitle("Add Department")
         self.EditDepartmentWindow.setWindowTitle("Edit Department")
         self.ShortcutForButtons()
         self.lang = 0


    ### Operations ###
    def Show_Message_Box(self,title,message) :
        
        MesaageBox = QtWidgets.QMessageBox()
        MesaageBox.setWindowTitle(title)
        MesaageBox.setText(message)
        MesaageBox.setWindowIcon(self.app_icon)
        MesaageBox.exec_()

    def LoginInfoCheck(self):
        username_input = self.Window.Username_Input.text()
        password_input = self.Window.Password_Input.text()

        checkinfo = Auditors.login(Username=username_input,Password=password_input)

        with Session(engine) as session:
                auditor_obj = session.query(Auditor).filter_by(Username=username_input).first()
        if checkinfo == 'Yes':
            self.UsernameLogout = username_input
            self.AuditorID = auditor_obj.id
            self.Show_Message_Box(self.success_msg, self.LoginSecAdmin_msg)
            self.Window.hide()
            self.SecondWindow.show()
        elif checkinfo == 'No':
            self.UsernameLogout = username_input
            self.AuditorID = auditor_obj.id
            self.Show_Message_Box(self.success_msg, self.LoginSecNotAdmin_msg)
            self.SecondWindow.Add_Auditor_Button.setVisible(False)
            self.SecondWindow.Add_Assets_Inventory_Button_2.setVisible(False)
            self.SecondWindow.Delete_Assets_Inventory_Button_2.setVisible(False)
            self.SecondWindow.Edit_Assets_Inventory_Button_2.setVisible(False)
            self.SecondWindow.Employees_And_Auditors_Tab.setTabVisible(3, False)
            self.SecondWindow.Add_Department_Button_3.setVisible(False)
            self.SecondWindow.Edit_Department_Button_3.setVisible(False)
            self.SecondWindow.Delete_Department_Button_3.setVisible(False)
            self.Window.hide()
            self.SecondWindow.show()
        else:
            self.Show_Message_Box(self.warning_msg, self.failedLogin_msg)


    def UserLogout(self):
        Auditors.logout(self.UsernameLogout)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def get_all_department_names(self):
        self.AddEmployeeWindow.EmployeeDepartment_Enum_AddEmployee_2.clear()
        self.UpdateEmployeeWindow.EmployeeDepartment_Enum_UpdateEmployee_3.clear()
        with Session(engine) as session:
            departments = session.query(Department.Department_Name).all()
            department_names = [department.Department_Name for department in departments]
        for department_name in department_names:
            self.AddEmployeeWindow.EmployeeDepartment_Enum_AddEmployee_2.addItem(department_name)
            self.UpdateEmployeeWindow.EmployeeDepartment_Enum_UpdateEmployee_3.addItem(department_name)

    def get_all_object_names_ToComboBox(self):
        self.AssetDepartmentAllocationWindow.ObjectName_Enum.clear()
        self.AddAssetAllocationWindow.ObjectName_Enum.clear()
        with Session(engine) as session:
            objects = session.query(Asset_Inventory.Object_Name).all()
            object_names = [Object.Object_Name for Object in objects]
        for object_name in object_names:
            self.AddAssetAllocationWindow.ObjectName_Enum.addItem(object_name)
            self.AssetDepartmentAllocationWindow.ObjectName_Enum.addItem(object_name)

    def AddEmployee (self):
        employee_number_input = self.AddEmployeeWindow.EmployeeID_input_AddEmployee_2.text()
        name_input = self.AddEmployeeWindow.EmployeeName_input_AddEmployee_2.text()
        employee_email_input = self.AddEmployeeWindow.EmployeeEmail_input_AddEmployee_2.text()
        department_input = self.AddEmployeeWindow.EmployeeDepartment_Enum_AddEmployee_2.currentText()
        grade_input = self.AddEmployeeWindow.EmployeeGrade_Enum_AddEmployee_2.currentText()
        address_input = self.AddEmployeeWindow.EmployeeAddress_input_AddEmployee_2.text()
        phone_number_input = self.AddEmployeeWindow.EmployeePhoneNumber_input_AddEmployee_2.text()
        relative_number_input = self.AddEmployeeWindow.EmployeeRelativeNumber_input_AddEmployee_2.text()
        iban_input = self.AddEmployeeWindow.EmployeeIBAN_input_AddEmployee_2.text()
        bank_input =  self.AddEmployeeWindow.EmployeeBank_input_AddEmployee_2.text()


        department_id = Departments.check(department_input)
        if self.lang == 1:
            grade_input = Translate(grade_input,0) # This variable set the grade in engilsh language in database 
        Employeeinfo = Employees.add(employee_number = employee_number_input,name = name_input ,employee_email= employee_email_input, department = department_id, grade = grade_input ,address=address_input,phone_number = phone_number_input,relative_number= relative_number_input,iban= iban_input,bank= bank_input)
        
        if Employeeinfo == "Error: Some Inputs Are Empty!":
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)

        elif Employeeinfo == "Error: Employee Number Already taken":
            self.Show_Message_Box(self.error_msg,self.EmployeeNumbererror_msg)

        elif Employeeinfo == "Error: Phone Number must be in 10 digits":
            self.Show_Message_Box(self.error_msg,self.EmployeePhoneNumError_msg)

        elif Employeeinfo == "Error: Phone Number and Relative Number must be different":
            self.Show_Message_Box(self.error_msg,self.EmployeeRelativeError_msg)

        elif Employeeinfo == True :
            self.Show_Message_Box(self.success_msg, self.Add_msg)
            self.EmployeesList()
            self.loadData()
            self.AddEmployeeWindow.hide()
            self.AddEmployeeWindow.EmployeeID_input_AddEmployee_2.clear()
            self.AddEmployeeWindow.EmployeeName_input_AddEmployee_2.clear()
            self.AddEmployeeWindow.EmployeeEmail_input_AddEmployee_2.clear()
            self.AddEmployeeWindow.EmployeeDepartment_Enum_AddEmployee_2.setCurrentIndex(0)
            self.AddEmployeeWindow.EmployeeGrade_Enum_AddEmployee_2.setCurrentIndex(0)
            self.AddEmployeeWindow.EmployeeAddress_input_AddEmployee_2.clear()
            self.AddEmployeeWindow.EmployeePhoneNumber_input_AddEmployee_2.clear()
            self.AddEmployeeWindow.EmployeeRelativeNumber_input_AddEmployee_2.clear()
            self.AddEmployeeWindow.EmployeeIBAN_input_AddEmployee_2.clear()
            self.AddEmployeeWindow.EmployeeBank_input_AddEmployee_2.clear()
        
    def EditEmployee(self):
        selected_row = self.SecondWindow.Employees_Table_2.currentRow()
        if selected_row >= 0:
            self.UpdateEmployeeWindow.show()
            id = self.SecondWindow.Employees_Table_2.item(selected_row,0).text()
            name = self.SecondWindow.Employees_Table_2.item(selected_row,2).text()
            email = self.SecondWindow.Employees_Table_2.item(selected_row,3).text()
            department = self.SecondWindow.Employees_Table_2.item(selected_row,4).text()
            grade = self.SecondWindow.Employees_Table_2.item(selected_row,5).text()
            address = self.SecondWindow.Employees_Table_2.item(selected_row,6).text()
            phone_number = self.SecondWindow.Employees_Table_2.item(selected_row,7).text()
            relative_number = self.SecondWindow.Employees_Table_2.item(selected_row,8).text()
            iban = self.SecondWindow.Employees_Table_2.item(selected_row,9).text()
            bank = self.SecondWindow.Employees_Table_2.item(selected_row,10).text()

    
            self.UpdateEmployeeWindow.EmployeeID_input_UpdateEmployee_2.setText(id)
            self.UpdateEmployeeWindow.EmployeeName_input_UpdateEmployee_2.setText(name)
            self.UpdateEmployeeWindow.EmployeeEmail_input_UpdateEmployee_2.setText(email)
            self.UpdateEmployeeWindow.EmployeeDepartment_Enum_UpdateEmployee_3.setCurrentText(department)
            self.UpdateEmployeeWindow.EmployeeGrade_Enum_UpdateEmployee_2.setCurrentText(grade)
            self.UpdateEmployeeWindow.EmployeeAddress_input_UpdateEmployee_2.setText(address)
            self.UpdateEmployeeWindow.EmployeePhoneNumber_input_UpdateEmployee_2.setText(phone_number)
            self.UpdateEmployeeWindow.EmployeeRelativeNumber_input_UpdateEmployee_2.setText(relative_number)
            self.UpdateEmployeeWindow.EmployeeIBAN_input_UpdateEmployee_2.setText(iban)
            self.UpdateEmployeeWindow.EmployeeBank_input_UpdateEmployee_3.setText(bank)
        else:
            self.Show_Message_Box(self.error_msg,self.EmployeeSelectError_msg)

    def ExcuteEmployeeEdit(self):
        id = self.UpdateEmployeeWindow.EmployeeID_input_UpdateEmployee_2.text()
        name_input = self.UpdateEmployeeWindow.EmployeeName_input_UpdateEmployee_2.text()
        employee_email_input = self.UpdateEmployeeWindow.EmployeeEmail_input_UpdateEmployee_2.text()
        department_input = self.UpdateEmployeeWindow.EmployeeDepartment_Enum_UpdateEmployee_3.currentText()
        grade_input = self.UpdateEmployeeWindow.EmployeeGrade_Enum_UpdateEmployee_2.currentText()
        address_input = self.UpdateEmployeeWindow.EmployeeAddress_input_UpdateEmployee_2.text()
        phone_number_input = self.UpdateEmployeeWindow.EmployeePhoneNumber_input_UpdateEmployee_2.text()
        relative_number_input = self.UpdateEmployeeWindow.EmployeeRelativeNumber_input_UpdateEmployee_2.text()
        iban_input = self.UpdateEmployeeWindow.EmployeeIBAN_input_UpdateEmployee_2.text()
        bank_input =  self.UpdateEmployeeWindow.EmployeeBank_input_UpdateEmployee_3.text()

        departmentCheck = Departments.check(department_input)
        
        if self.lang == 1:
            grade_input = Translate(grade_input,0) # This variable set the grade in engilsh language in database 
        EmployeeEditCheck = Employees.update(id= id,updates= {"Name":name_input, "Employee_email": employee_email_input, "Department": departmentCheck, "Grade":grade_input, "Address": address_input, "Phone_Number": phone_number_input, "Relative_Number": relative_number_input, "IBAN": iban_input, "Bank": bank_input})
        
        if not id.strip() or not name_input.strip() or not employee_email_input.strip() or not address_input.strip() or not phone_number_input.strip() or not relative_number_input.strip() or not iban_input.strip() or not bank_input.strip():
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)
        
        elif EmployeeEditCheck == True:
            self.Show_Message_Box(self.success_msg, self.edited_msg)
            self.EmployeesList()
            self.loadData()
            self.UpdateEmployeeWindow.hide()
            self.UpdateEmployeeWindow.EmployeeID_input_UpdateEmployee_2.clear()
            self.UpdateEmployeeWindow.EmployeeName_input_UpdateEmployee_2.clear()
            self.UpdateEmployeeWindow.EmployeeEmail_input_UpdateEmployee_2.clear()
            self.UpdateEmployeeWindow.EmployeeDepartment_Enum_UpdateEmployee_3.setCurrentIndex(0)
            self.UpdateEmployeeWindow.EmployeeGrade_Enum_UpdateEmployee_2.setCurrentIndex(0)
            self.UpdateEmployeeWindow.EmployeeAddress_input_UpdateEmployee_2.clear()
            self.UpdateEmployeeWindow.EmployeePhoneNumber_input_UpdateEmployee_2.clear()
            self.UpdateEmployeeWindow.EmployeeRelativeNumber_input_UpdateEmployee_2.clear()
            self.UpdateEmployeeWindow.EmployeeIBAN_input_UpdateEmployee_2.clear()
            self.UpdateEmployeeWindow.EmployeeBank_input_UpdateEmployee_3.clear()
        else:
            self.Show_Message_Box(self.error_msg,self.EmployeeDepError_msg)

    def DeleteEmployee (self):
        selected_row = self.SecondWindow.Employees_Table_2.currentRow()
        if selected_row >= 0 :
            id = self.SecondWindow.Employees_Table_2.item(selected_row,0).text()
            self.loadData()
            EmployeeCheck = Employees.delete(id = id)
            if EmployeeCheck == True:
                self.Show_Message_Box(self.success_msg, self.DeletedEmployee_msg)
                self.loadData()
            else:
                self.Show_Message_Box(self.error_msg,self.cantDeleteEmployee_msg)
        else:
            self.Show_Message_Box(self.error_msg,self.EmployeeSelectError_msg)

    def AddAuditor_AuditorID(self):
        selected_row = self.SecondWindow.Employees_Table_2.currentRow()
        if selected_row >= 0:
            id = self.SecondWindow.Employees_Table_2.item(selected_row,0).text()
            with Session (engine) as session: 
                Employee_number_check_Auditor = session.query(Auditor).filter_by(Employee_ID = id).first()
            if not Employee_number_check_Auditor:
                self.AddUserWindow.EmployeeID_input_AddAudtior_2.setText(id)
                self.AddUserWindow.show()
            else:
                self.Show_Message_Box(self.error_msg,self.AlreadyUser_msg)

        else:
            self.Show_Message_Box(self.error_msg,self.EmployeeSelectError_msg)

    def AddAuditors(self):

        employee_id_input = self.AddUserWindow.EmployeeID_input_AddAudtior_2.text()
        username_input = self.AddUserWindow.Username_input_AddAudtior_2.text()
        password_input = self.AddUserWindow.Password_input_AddAudtior_2.text()
        admin_input = self.AddUserWindow.Admin_Enum_AddAudtior_2.currentText()
        
        if self.lang == 1:
            admin_input = Translate(admin_input,0) # This variable set the admin status in engilsh language in database
             
        Auditorsinfo = Auditors.add(employee_id = employee_id_input,username = username_input,password = password_input,admin = admin_input)
 
        if Auditorsinfo == True :
            self.Show_Message_Box(self.success_msg, self.Add_msg)
            self.AuditorsList()
            self.loadData()
            self.AddUserWindow.hide()
            self.AddUserWindow.EmployeeID_input_AddAudtior_2.clear()
            self.AddUserWindow.Username_input_AddAudtior_2.clear()
            self.AddUserWindow.Password_input_AddAudtior_2.clear()
            self.AddUserWindow.Admin_Enum_AddAudtior_2.setCurrentIndex(0)
        else:
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)
            
    def EditAuditors(self):
        selected_row = self.SecondWindow.Auditors_Table_2.currentRow()
        if selected_row >= 0:
            self.UpdateUserWindow.show()
            id = self.SecondWindow.Auditors_Table_2.item(selected_row,0).text()
            username = self.SecondWindow.Auditors_Table_2.item(selected_row,3).text()
            password = self.SecondWindow.Auditors_Table_2.item(selected_row,4).text()
            admin = self.SecondWindow.Auditors_Table_2.item(selected_row,6).text()

            self.UpdateUserWindow.EmployeeID_input_UpdateAudtior_2.setText(id)
            self.UpdateUserWindow.Username_input_UpdateAudtior_2.setText(username)
            self.UpdateUserWindow.Password_input_UpdateAudtior_2.setText(password)
            self.UpdateUserWindow.Admin_Enum_UpdateAudtior_2.setCurrentText(admin)
        else:
            self.Show_Message_Box(self.error_msg,self.selectusererror_msg)

    def ExcuteAuditorsEdit(self):
        id = self.UpdateUserWindow.EmployeeID_input_UpdateAudtior_2.text()
        username = self.UpdateUserWindow.Username_input_UpdateAudtior_2.text()
        password = self.UpdateUserWindow.Password_input_UpdateAudtior_2.text()
        admin = self.UpdateUserWindow.Admin_Enum_UpdateAudtior_2.currentText()
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()
        if self.lang == 1:
            admin = Translate(admin,0) # This variable set the admin status in engilsh language in database 
        if not id.strip() or not username.strip() or not password.strip():
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)
        else:
            Auditors.update(id= id,updates= {"Username":username, "Password": hashed_password, "Admin":admin})
            self.Show_Message_Box(self.success_msg, self.edited_msg)
            self.AuditorsList()
            self.loadData()
            self.UpdateUserWindow.hide()
            self.UpdateUserWindow.EmployeeID_input_UpdateAudtior_2.clear()
            self.UpdateUserWindow.Username_input_UpdateAudtior_2.clear()
            self.UpdateUserWindow.Password_input_UpdateAudtior_2.clear()
            self.UpdateUserWindow.Admin_Enum_UpdateAudtior_2.setCurrentIndex(0)

    def DeleteAuditor (self):
        selected_row = self.SecondWindow.Auditors_Table_2.currentRow()
        if selected_row >= 0:
            id = self.SecondWindow.Auditors_Table_2.item(selected_row,0).text()
            self.loadData()
            Auditors.delete(id = id)
            self.Show_Message_Box(self.success_msg, self.DeletedEmployee_msg)
            self.loadData()
        else:
            self.Show_Message_Box(self.error_msg,self.selectusererror_msg)

    def AddAssetAllocationPersonal_AuditorID(self):
        selectedrow = self.SecondWindow.Employees_Table_2.currentRow()
        if selectedrow >=0:
            self.AssetCheck = "Personal"
            id = self.SecondWindow.Employees_Table_2.item(selectedrow,0).text()
            self.Employee_department = self.SecondWindow.Employees_Table_2.item(selectedrow,4).text()
            self.AddAssetAllocationWindow.EmployeeID_input_AddAsset_3.setText(id)
            self.AddAssetAllocationWindow.AuditorID_Input_AddAssest_3.setText(str(self.AuditorID))
            self.AddAssetAllocationWindow.show()
        else:
            self.Show_Message_Box(self.error_msg,self.EmployeeSelectError_msg)

    def AddAssetAllocationDepartment_AuditorID(self):
        selectedrow = self.SecondWindow.Employees_Table_2.currentRow()
        if selectedrow >=0:
            self.AssetCheck = "Department"
            self.EmployeeID_AssetCheck = self.SecondWindow.Employees_Table_2.item(selectedrow,0).text()
            department = self.SecondWindow.Employees_Table_2.item(selectedrow,4).text()
            self.AssetDepartmentAllocationWindow.EmployeeID_input_AddAsset_3.setText(department)
            self.AssetDepartmentAllocationWindow.AuditorID_Input_AddAssest_3.setText(str(self.AuditorID))
            self.AssetDepartmentAllocationWindow.show()
        else:
            self.Show_Message_Box(self.error_msg,self.EmployeeSelectError_msg)

    def AddAssetAllocation(self):
        if self.AssetCheck == "Personal":
            employee_id_input = self.AddAssetAllocationWindow.EmployeeID_input_AddAsset_3.text()
            auditor_id_input = self.AddAssetAllocationWindow.AuditorID_Input_AddAssest_3.text()
            object_name_input = self.AddAssetAllocationWindow.ObjectName_Enum.currentText()
            quantity_input = self.AddAssetAllocationWindow.Quantity_input_AddAsset_3.text()
            suggested_returndate_input = self.AddAssetAllocationWindow.SuggestedReturnDate_Input_AddAsset_3.date().toString("yyyy-MM-dd")
            department_input = self.Employee_department
            asset_type = "Personal"
            
            object_id = Assets_Inventory.check(object_name_input)
            department_id = Departments.check(department_input)
            Assetinfo = Assets_Allocations.add(employee_id=employee_id_input, auditor_id=auditor_id_input, asset_id=object_id, department_id=department_id, quantity=quantity_input, suggested_returndate=suggested_returndate_input, note = asset_type)
            
            if Assetinfo == True:
                self.Show_Message_Box(self.success_msg, self.Add_msg)
                self.AssetAllocationList()
                self.loadData()
                self.AddAssetAllocationWindow.hide()
                self.AddAssetAllocationWindow.EmployeeID_input_AddAsset_3.clear()
                self.AddAssetAllocationWindow.AuditorID_Input_AddAssest_3.clear()
                self.AddAssetAllocationWindow.ObjectName_Enum.setCurrentIndex(0)
                self.AddAssetAllocationWindow.Quantity_input_AddAsset_3.clear()
            elif Assetinfo == "Error: There is No Asset in Inventory maybe its Finished":
                self.Show_Message_Box(self.error_msg, self.NoAsset)
            elif Assetinfo == "Error: The Quantity Entered is Higher than the Asset Quantity in Inventory.":
                self.Show_Message_Box(self.error_msg, self.QuantityHigher_msg)
            else:
                self.Show_Message_Box(self.error_msg, self.Emptyinputs_msg)
       
        elif self.AssetCheck == "Department":
            employee_id_input = self.EmployeeID_AssetCheck
            auditor_id_input = self.AssetDepartmentAllocationWindow.AuditorID_Input_AddAssest_3.text()
            object_name_input = self.AssetDepartmentAllocationWindow.ObjectName_Enum.currentText()
            department_input = self.AssetDepartmentAllocationWindow.EmployeeID_input_AddAsset_3.text()
            quantity_input = self.AssetDepartmentAllocationWindow.Quantity_input_AddAsset_3.text()
            suggested_returndate_input = self.AssetDepartmentAllocationWindow.SuggestedReturnDate_Input_AddAsset_3.date().toString("yyyy-MM-dd")
            asset_type = "Department"


            object_id = Assets_Inventory.check(object_name_input)
            department_id = Departments.check(department_input)
            Assetinfo = Assets_Allocations.add(employee_id=employee_id_input, auditor_id=auditor_id_input, asset_id=object_id, department_id=department_id, quantity=quantity_input, suggested_returndate=suggested_returndate_input, note = asset_type)
            
            if Assetinfo == True:
                self.Show_Message_Box(self.success_msg, self.Add_msg)
                self.AssetAllocationList()
                self.loadData()
                self.AssetDepartmentAllocationWindow.hide()
                self.AssetDepartmentAllocationWindow.EmployeeID_input_AddAsset_3.clear()
                self.AssetDepartmentAllocationWindow.AuditorID_Input_AddAssest_3.clear()
                self.AssetDepartmentAllocationWindow.ObjectName_Enum.setCurrentIndex(0)
                self.AssetDepartmentAllocationWindow.Quantity_input_AddAsset_3.clear()
            elif Assetinfo == "Error: There is No Asset in Inventory maybe its Finished":
                self.Show_Message_Box(self.error_msg, self.NoAsset)
            elif Assetinfo == "Error: The Quantity Entered is Higher than the Asset Quantity in Inventory.":
                self.Show_Message_Box(self.error_msg, self.QuantityHigher_msg)
            else:
                self.Show_Message_Box(self.error_msg, self.Emptyinputs_msg)
                
    def ReturnAsset(self):
        selected_row = self.SecondWindow.AssetAllocations_Table_3.currentRow()
        if selected_row >= 0:
            id = self.SecondWindow.AssetAllocations_Table_3.item(selected_row,0).text()
            note = self.SecondWindow.AssetAllocations_Table_3.item(selected_row,14).text()
            with Session (engine) as session:  
                AssetCheck = session.query(Asset_Allocation).filter_by(id = id).first()
            if AssetCheck.Is_Returned != "Yes is returned":
                self.ReturnAssetWindow.AssetID_returnAsset_2.setText(id)
                self.ReturnAssetWindow.Notes_Returned_Input_3.setText(note)
                self.ReturnAssetWindow.show()
            else:
                self.Show_Message_Box(self.error_msg,self.assetAlready_msg)
        else:
            self.Show_Message_Box(self.error_msg,self.Returnassetselect_msg)

    def ExcuteReturnAsset(self):
        id = self.ReturnAssetWindow.AssetID_returnAsset_2.text()
        return_status = self.ReturnAssetWindow.Returned_Enum_3.currentText()
        damage_status = self.ReturnAssetWindow.DamageStatus_Enum_3.currentText()
        note = self.ReturnAssetWindow.Notes_Returned_Input_3.toPlainText()
        
        if self.lang == 1:
            damage_status = Translate(damage_status,0) # This variable set the return status in engilsh language in database 
            return_status = Translate(return_status,0) # This variable set the damage status in engilsh language in database 
        if not id.strip():
            self.Show_Message_Box(self.error_msg,"Something went wrong. Please try again!")
        else:
            Assets_Allocations.update(id= id,updates= {"Is_Returned":return_status, "Return_Status":damage_status, "Note": note, "Return_Date": datetime.now()})
            self.Show_Message_Box(self.success_msg, self.RetunedAsset_msg)
            self.ReturnAssetWindow.hide()
            self.loadData()
            self.ReturnAssetWindow.AssetID_returnAsset_2.clear()
            self.ReturnAssetWindow.Returned_Enum_3.setCurrentIndex(0)
            self.ReturnAssetWindow.DamageStatus_Enum_3.setCurrentIndex(0)
            self.ReturnAssetWindow.Notes_Returned_Input_3.clear()

    def AddPayment_AuditorID(self):
        selected_row = self.SecondWindow.FinancialLoans_Table_4.currentRow()
        if selected_row >= 0:
            id = self.SecondWindow.FinancialLoans_Table_4.item(selected_row,0).text()
            PaidinFull_or_not = self.SecondWindow.FinancialLoans_Table_4.item(selected_row,8).text()
            if PaidinFull_or_not == "No":
                self.AddPaymentWindow.LoanID_Input_AddPayment_2.setText(id)
                self.AddPaymentWindow.AuditorID_Input_AddPayment_2.setText(str(self.AuditorID))
                self.AddPaymentWindow.show()
            elif PaidinFull_or_not == "Yes":
                self.Show_Message_Box(self.error_msg,self.PaidFullmsg)
        else:
            self.Show_Message_Box(self.error_msg,self.addPaymentmsg)

    def AddPayment(self):
        self.selected_row = self.SecondWindow.FinancialLoans_Table_4.currentRow()
        loan_id_input = self.AddPaymentWindow.LoanID_Input_AddPayment_2.text()
        auditor_id_input = self.AddPaymentWindow.AuditorID_Input_AddPayment_2.text()
        amount_input = self.AddPaymentWindow.PaymentAmount_Input_2.text()
        PaymentMethod_input = self.AddPaymentWindow.PaymentMethod_Enum_2.currentText()
        
        if self.lang == 1:
            PaymentMethod_input = Translate(PaymentMethod_input,0) # This variable set the payment method in engilsh language in database 
        Paymentinfo = Loan_payment.add(loan_id=loan_id_input,auditor_id=auditor_id_input,amount=amount_input,PaymentMethod=PaymentMethod_input)
        if Paymentinfo == "Success: The loan has been paid in full." : 
                self.Show_Message_Box(self.success_msg, self.Add_msg)
                self.loadData()
                self.AddPaymentWindow.hide()
                self.AddPaymentWindow.LoanID_Input_AddPayment_2.clear()
                self.AddPaymentWindow.AuditorID_Input_AddPayment_2.clear()
                self.AddPaymentWindow.PaymentAmount_Input_2.clear()
                self.AddPaymentWindow.PaymentMethod_Enum_2.setCurrentIndex(0)

        elif Paymentinfo == "The Loan has been add" :
                self.Show_Message_Box(self.success_msg, self.Add_msg)
                self.loadData()
                self.AddPaymentWindow.hide()
                self.AddPaymentWindow.LoanID_Input_AddPayment_2.clear()
                self.AddPaymentWindow.AuditorID_Input_AddPayment_2.clear()
                self.AddPaymentWindow.PaymentAmount_Input_2.clear()
                self.AddPaymentWindow.PaymentMethod_Enum_2.setCurrentIndex(0)
                
        elif Paymentinfo == "Error: The payment amount is greater than the remaining amount of the loan." :
                self.Show_Message_Box(self.error_msg,self.higherAmount_msg)
        else:
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)             

    def AddLoan_AuditorID(self):
        selected_row = self.SecondWindow.Employees_Table_2.currentRow()
        if selected_row >= 0:
            id = self.SecondWindow.Employees_Table_2.item(selected_row,0).text()
            self.AddLoanWindow.EmployeeID_input_AddLoan_4.setText(id)
            self.AddLoanWindow.AuditorID_Input_AddLoan_4.setText(str(self.AuditorID))
            self.AddLoanWindow.show()
        else:
            self.Show_Message_Box(self.error_msg,self.EmployeeSelectError_msg)
              
    def AddLoans(self):
        employee_id_input = self.AddLoanWindow.EmployeeID_input_AddLoan_4.text()
        auditor_id_input = self.AddLoanWindow.AuditorID_Input_AddLoan_4.text()
        amount_input = self.AddLoanWindow.LoanAmount_Input_4.text()
        type_of_deposit_input = self.AddLoanWindow.TypeofDeposit_Enum_4.currentText()
        loan_type_input = self.AddLoanWindow.LoanType_Enum_4.currentText() 
        suggested_ReturnDate = self.AddLoanWindow.SuggestedReturnDate_Input_AddLoan_4.date().toString("yyyy-MM-dd")
        if self.lang == 1:
            loan_type_input = Translate(loan_type_input,0) # This variable set the loan type in engilsh language in database 
            type_of_deposit_input = Translate(type_of_deposit_input,0) # This variable set the deposit type in engilsh language in database 
        checkinfo = Financial_Loans.add(employee_id=employee_id_input,auditor_id =auditor_id_input,amount= amount_input,suggested_ReturnDate= suggested_ReturnDate, loan_type=loan_type_input, type_of_deposit=type_of_deposit_input)
        if checkinfo == True :
            self.AddLoanWindow.EmployeeID_input_AddLoan_4.clear()
            self.AddLoanWindow.AuditorID_Input_AddLoan_4.clear()
            self.AddLoanWindow.LoanAmount_Input_4.clear()
            self.AddLoanWindow.TypeofDeposit_Enum_4.setCurrentIndex(0)
            self.AddLoanWindow.LoanType_Enum_4.setCurrentIndex(0)
            self.Show_Message_Box(self.success_msg, self.Add_msg)
            self.loadData()
            self.AddLoanWindow.hide()
        else:
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)

    def AddDepartment(self) : 
        
        department_name_Input = self.AddDepartmentWindow.Name_input_AddDepartment_7.text()
        manager_id_input = self.AddDepartmentWindow.ManagerID_Input_2.text()
        
        if not manager_id_input.strip():
            employee_id = None
        else:
            employee_id = Employees.check(manager_id_input)
        
        if employee_id == False:
            self.Show_Message_Box(self.error_msg,self.WrongEmployeenumber_msg)
        else:
            DepartmentInfo = Departments.add(department_name=department_name_Input,manager_id=employee_id)
            if DepartmentInfo == True :
                self.Show_Message_Box(self.success_msg, self.Add_msg)
                self.loadData()
                self.AddDepartmentWindow.hide()
                self.AddDepartmentWindow.Name_input_AddDepartment_7.clear()
                self.AddDepartmentWindow.ManagerID_Input_2.clear()
            elif DepartmentInfo == "Error: The department Already Added":
                self.Show_Message_Box(self.error_msg,self.DepartmentAdded_msg)
            else:
                self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)

    def EditDepartment(self) : 
        selected_row = self.SecondWindow.Assets_Inventory_Table_2.currentRow()
        if selected_row >= 0:
            self.EditDepartmentWindow.show()
            self.departmentId_Check = self.SecondWindow.Assets_Inventory_Table_2.item(selected_row,0).text()
            name = self.SecondWindow.Assets_Inventory_Table_2.item(selected_row,1).text()
            manager_id = self.SecondWindow.Assets_Inventory_Table_2.item(selected_row,2).text()
            
            self.EditDepartmentWindow.Name_input_EditDepartment_7.setText(name)
            self.EditDepartmentWindow.EditManagerID_Input_2.setText(manager_id)
        else:
             self.Show_Message_Box(self.error_msg,self.selectDepartment_msg)
            
    def ExcuteEditDepartment(self):
        
        id = self.departmentId_Check
        Name = self.EditDepartmentWindow.Name_input_EditDepartment_7.text()
        ManagerID = self.EditDepartmentWindow.EditManagerID_Input_2.text()

        if not Name.strip():
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)
        
        if not ManagerID.strip():
            employee_id = None
        else:
            employee_id = Employees.check(ManagerID)
        
        if employee_id == False:
             self.Show_Message_Box(self.error_msg,self.WrongEmployeenumber_msg)
        else:
                Departments.update(id= id,updates= {"Department_Name":Name, "Manager_ID": employee_id})
                self.Show_Message_Box(self.success_msg, self.edited_msg)
                self.loadData()
                self.EditDepartmentWindow.hide()
                self.EditDepartmentWindow.Name_input_EditDepartment_7.clear()
                self.EditDepartmentWindow.EditManagerID_Input_2.clear()

    def DeleteDepartment (self):
        
        selected_row = self.SecondWindow.Assets_Inventory_Table_2.currentRow()
        if selected_row >= 0 :
            id = self.SecondWindow.Assets_Inventory_Table_2.item(selected_row,0).text()
            self.loadData()
            DepartmentCheck = Departments.delete(id = id)
            if DepartmentCheck == True:
                self.Show_Message_Box(self.success_msg, self.DeletedEmployee_msg)
                self.loadData()
            else:
                self.Show_Message_Box(self.error_msg,self.signedEmployeedDepartment_msg)
        else:
            self.Show_Message_Box(self.error_msg,self.selectDepartment_msg)

    def AddAssetInventory(self):
        
        object_name_input = self.AddAssetInventoryWindow.ObjectName_input_AddAssets_Inventory_4.text()
        SerialNumber_input = self.AddAssetInventoryWindow.SerialNumber_input_AddAssets_Inventory_4.text()
        quantity_input = self.AddAssetInventoryWindow.Quantity_input_AddAssets_Inventory_4.text()
        MoneyValue_input = self.AddAssetInventoryWindow.MoneyValue_input_AddAssets_Inventory_4.text()
        Location_input = self.AddAssetInventoryWindow.Location_input_AddAssets_Inventory_5.text()
        Description_input = self.AddAssetInventoryWindow.description_Input_AddAssets_Inventory_4.text()

        Assetinfo = Assets_Inventory.add(object_name=object_name_input,serial_Number=SerialNumber_input,money_Value=MoneyValue_input,quantity= quantity_input,location=Location_input,description = Description_input)
        if Assetinfo == True :
            self.Show_Message_Box(self.success_msg, self.Add_msg)
            self.loadData()
            self.AddAssetInventoryWindow.hide()
            self.AddAssetInventoryWindow.ObjectName_input_AddAssets_Inventory_4.clear()
            self.AddAssetInventoryWindow.SerialNumber_input_AddAssets_Inventory_4.clear()
            self.AddAssetInventoryWindow.Quantity_input_AddAssets_Inventory_4.clear()
            self.AddAssetInventoryWindow.MoneyValue_input_AddAssets_Inventory_4.clear()
            self.AddAssetInventoryWindow.Location_input_AddAssets_Inventory_5.clear()
            self.AddAssetInventoryWindow.description_Input_AddAssets_Inventory_4.clear()
        else:
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)

    def EditAssetInventory(self) : 
        
        selected_row = self.SecondWindow.Assets_Inventory_Table.currentRow()
        if selected_row >= 0:
            self.EditAssetInventoryWindow.show()
            self.AssetIdCheck = self.SecondWindow.Assets_Inventory_Table.item(selected_row,0).text()
            object_name = self.SecondWindow.Assets_Inventory_Table.item(selected_row,1).text()
            description = self.SecondWindow.Assets_Inventory_Table.item(selected_row,2).text()
            serial_number = self.SecondWindow.Assets_Inventory_Table.item(selected_row,3).text()
            money_value = self.SecondWindow.Assets_Inventory_Table.item(selected_row,4).text()
            quantity = self.SecondWindow.Assets_Inventory_Table.item(selected_row,5).text()
            location = self.SecondWindow.Assets_Inventory_Table.item(selected_row,6).text()
            
            self.EditAssetInventoryWindow.ObjectName_input_EditAssets_Inventory_5.setText(object_name)
            self.EditAssetInventoryWindow.description_Input_EditAssets_Inventory_5.setText(description)
            self.EditAssetInventoryWindow.SerialNumber_input_EditAssets_Inventory_5.setText(serial_number)
            self.EditAssetInventoryWindow.MoneyValue_input_EditAssets_Inventory_5.setText(money_value)
            self.EditAssetInventoryWindow.Quantity_input_EditAssets_Inventory_5.setText(quantity)
            self.EditAssetInventoryWindow.Location_input_EditAssets_Inventory_6.setText(location)
        else:
            self.Show_Message_Box(self.error_msg,self.Returnassetselect_msg)

    def ExcuteEditAssetInventory(self):
        id = self.AssetIdCheck
        object_name = self.EditAssetInventoryWindow.ObjectName_input_EditAssets_Inventory_5.text()
        Description = self.EditAssetInventoryWindow.description_Input_EditAssets_Inventory_5.text()
        SerialNumber = self.EditAssetInventoryWindow.SerialNumber_input_EditAssets_Inventory_5.text()
        MoneyValue = self.EditAssetInventoryWindow.MoneyValue_input_EditAssets_Inventory_5.text()
        quantity = self.EditAssetInventoryWindow.Quantity_input_EditAssets_Inventory_5.text()
        Location = self.EditAssetInventoryWindow.Location_input_EditAssets_Inventory_6.text()


        if not id.strip() or not object_name.strip() or not SerialNumber.strip() or not quantity.strip() or not MoneyValue.strip() or not Location.strip():
            self.Show_Message_Box(self.error_msg,self.Emptyinputs_msg)
        else:
            Assets_Inventory.update(id= id,updates= {"Object_Name":object_name, "Serial_Number": SerialNumber, "Quantity": quantity, "Money_Value": MoneyValue, "Location": Location,"Description": Description})
            self.Show_Message_Box(self.success_msg, self.edited_msg)
            self.loadData()
            self.EditAssetInventoryWindow.hide()
            self.EditAssetInventoryWindow.ObjectName_input_EditAssets_Inventory_5.clear()
            self.EditAssetInventoryWindow.description_Input_EditAssets_Inventory_5.clear()
            self.EditAssetInventoryWindow.SerialNumber_input_EditAssets_Inventory_5.clear()
            self.EditAssetInventoryWindow.MoneyValue_input_EditAssets_Inventory_5.clear()
            self.EditAssetInventoryWindow.Quantity_input_EditAssets_Inventory_5.clear()
            self.EditAssetInventoryWindow.Location_input_EditAssets_Inventory_6.clear()

    def DeleteAsset (self):
        
        selected_row = self.SecondWindow.Assets_Inventory_Table.currentRow()
        if selected_row >= 0 :
            id = self.SecondWindow.Assets_Inventory_Table.item(selected_row,0).text()
            self.loadData()
            AssetsCheck = Assets_Inventory.delete(asset_id = id)
            if AssetsCheck == True:
                self.Show_Message_Box(self.success_msg, self.DeletedEmployee_msg)
                self.loadData()
            else:
                self.Show_Message_Box(self.error_msg,self.cantDeleteEmployee_msg)
        else:
            self.Show_Message_Box(self.error_msg,self.Returnassetselect_msg)


    ### Windows or Tabs ###
    def WindowofAddEmployee(self):
        self.AddEmployeeWindow.show()
           
    def WindowOfAddLoan(self):
        self.AddLoanWindow.show()

    def WindowOfAddPayment(self):
        self.AddPaymentWindow.show()

    def WindowOf_AddAssetInventory(self):
        self.AddAssetInventoryWindow.show()

    def WindowOf_AddAssetAllocation(self):
        self.AddAssetAllocationWindow.show()
    
    def EmployeesList(self):
        self.SecondWindow.Employees_And_Auditors_Tab.setCurrentIndex(0)
        
    def DepartmentsList(self):
        self.SecondWindow.Employees_And_Auditors_Tab.setCurrentIndex(1)
    
    def AuditorsList(self):
        self.SecondWindow.Employees_And_Auditors_Tab.setCurrentIndex(3)
        
    def AssetInventoryList(self):
        self.SecondWindow.Employees_And_Auditors_Tab.setCurrentIndex(3)
        
    def Loans_and_Payments_List(self):
        self.SecondWindow.Financial_OR_Assest_Tab.setCurrentIndex(0)

    def AssetAllocationList(self):
        self.SecondWindow.Financial_OR_Assest_Tab.setCurrentIndex(1)
        
    def WindowOf_AddDepartment(self):
        self.AddDepartmentWindow.show()


    ### Buttons ###
    def Actions(self) :
        ## Languages buttons ## 
        self.Window.English_Button.setChecked(True)
        self.Window.English_Button.clicked.connect(lambda: self.translation(0)) 
        self.Window.Arabic_Button.clicked.connect(lambda: self.translation(1)) 
        ## Refresh##
        self.SecondWindow.Refresh_Button.clicked.connect(self.loadData)

        ## Login ##
        self.Window.Login_Pushbutton.clicked.connect(self.LoginInfoCheck)
        self.SecondWindow.Logout_button.clicked.connect(self.UserLogout)
        
        ## Employees ##
        self.SecondWindow.Add_Employee_Button.clicked.connect(self.WindowofAddEmployee)
        self.AddEmployeeWindow.Save_AddEmployee_Button.clicked.connect(self.AddEmployee)
        self.AddEmployeeWindow.Cancel_AddEmployee_Button.clicked.connect(self.AddEmployeeCancel)
        self.SecondWindow.Edit_Employee_Button.clicked.connect(self.EditEmployee)
        self.UpdateEmployeeWindow.Save_UpdateEmployee_Button_3.clicked.connect(self.ExcuteEmployeeEdit)
        self.UpdateEmployeeWindow.Cancel_UpdateEmployee_Button_3.clicked.connect(self.EditEmployeeCancel)
        self.SecondWindow.Delete_Employee_Button.clicked.connect(self.DeleteEmployee)

        ## Users ##
        self.SecondWindow.Add_Auditor_Button.clicked.connect(self.AddAuditor_AuditorID)
        self.AddUserWindow.Save_AddAuditor_Button.clicked.connect(self.AddAuditors)
        self.AddUserWindow.Cancel_AddAuditor_Button.clicked.connect(self.AddAuditorCancel)
        self.SecondWindow.Edit_Auditor_Button.clicked.connect(self.EditAuditors)
        self.UpdateUserWindow.UpdateAuditor_Button.clicked.connect(self.ExcuteAuditorsEdit)
        self.UpdateUserWindow.Cancel_UpdateAuditor_Button.clicked.connect(self.EditAuditorsCancel)
        self.SecondWindow.Delete_Auditor_Button.clicked.connect(self.DeleteAuditor)

        ## Loans ##
        self.SecondWindow.Add_FinanciaLoan_Button_6.clicked.connect(self.AddLoan_AuditorID)
        self.AddLoanWindow.Save_AddLoan_Button_4.clicked.connect(self.AddLoans)
        self.AddLoanWindow.Cancel_AddLoan_Button_4.clicked.connect(self.AddLoansCancel)

        ## Payment ##
        self.SecondWindow.Add_Payment_Button_5.clicked.connect(self.AddPayment_AuditorID)
        self.AddPaymentWindow.Save_AddPayment_Button_3.clicked.connect(self.AddPayment)
        self.AddPaymentWindow.Cancel_AddPayment_Button_3.clicked.connect(self.AddPaymentCancel)

        ## Department ##
        self.SecondWindow.Add_Department_Button_3.clicked.connect(self.WindowOf_AddDepartment)
        self.AddDepartmentWindow.Save_AddDepartment_Button_3.clicked.connect(self.AddDepartment)
        self.AddDepartmentWindow.Cancel_AddDepartment_Button_3.clicked.connect(self.AddDepartmentCancel)
        self.SecondWindow.Edit_Department_Button_3.clicked.connect(self.EditDepartment)
        self.EditDepartmentWindow.Save_EditDepartment_Button_3.clicked.connect(self.ExcuteEditDepartment)
        self.EditDepartmentWindow.Cancel_EditDepartment_Button_3.clicked.connect(self.EditDepartmentCancel)
        self.SecondWindow.Delete_Department_Button_3.clicked.connect(self.DeleteDepartment)

        ## Asset Inventory ##
        self.SecondWindow.Add_Assets_Inventory_Button_2.clicked.connect(self.WindowOf_AddAssetInventory)    
        self.AddAssetInventoryWindow.Save_AddAssets_Inventory_Button_4.clicked.connect(self.AddAssetInventory)
        self.AddAssetInventoryWindow.Cancel_AddAssets_Inventory_Button_4.clicked.connect(self.AddAssetInventoryCancel)
        self.SecondWindow.Edit_Assets_Inventory_Button_2.clicked.connect(self.EditAssetInventory)
        self.EditAssetInventoryWindow.Save_UpdateAssets_Inventory_Button_3.clicked.connect(self.ExcuteEditAssetInventory)
        self.EditAssetInventoryWindow.Cancel_UpdateAssets_Inventory_Button_3.clicked.connect(self.EditAssetInventoryCancel)
        self.SecondWindow.Delete_Assets_Inventory_Button_2.clicked.connect(self.DeleteAsset)

        ## Asset ##
        self.SecondWindow.Add_Asset_Button_3.clicked.connect(self.AddAssetAllocationPersonal_AuditorID)
        self.SecondWindow.AddDepartmentAsset_Button.clicked.connect(self.AddAssetAllocationDepartment_AuditorID)
        self.AddAssetAllocationWindow.Save_AddAsset_Button_3.clicked.connect(self.AddAssetAllocation)
        self.AddAssetAllocationWindow.Cancel_AddAsset_Button_3.clicked.connect(self.AddAssetAllocationCancel)
        self.AssetDepartmentAllocationWindow.Save_AddAsset_Button_3.clicked.connect(self.AddAssetAllocation)
        self.AssetDepartmentAllocationWindow.Cancel_AddAsset_Button_3.clicked.connect(self.AddAssetAllocationCancel)
        self.SecondWindow.Return_Asset_Button_3.clicked.connect(self.ReturnAsset)
        self.ReturnAssetWindow.Save_ReturnedAsset_Button_5.clicked.connect(self.ExcuteReturnAsset)
        self.ReturnAssetWindow.Cancel_ReturnedAsset_Button_5.clicked.connect(self.ReturnAssetCancel)
        
        ## Filters Selection Connect ##
        self.SecondWindow.Employees_Table_2.itemSelectionChanged.connect(self.Filter_SearchEmployee_Asset)
        self.SecondWindow.FinancialLoans_Table_4.itemSelectionChanged.connect(self.Filter_SearchLoan_Payment)
        self.SecondWindow.Assets_Inventory_Table_2.itemSelectionChanged.connect(self.Filter_SearchEmployeeAsset_Department)
        self.SecondWindow.Assets_Inventory_Table.itemSelectionChanged.connect(self.Filter_SearchAsset_AssetAllocation)
        

    ### ShortCutButtons ###
    def ShortcutForButtons(self) :
        self.Window.Login_Pushbutton.setShortcut(QKeySequence(Qt.Key_Return))
        self.ReturnAssetWindow.Save_ReturnedAsset_Button_5.setShortcut(QKeySequence(Qt.Key_Return))
        self.ReturnAssetWindow.Cancel_ReturnedAsset_Button_5.setShortcut(QKeySequence(Qt.Key_Escape))
        self.AddAssetAllocationWindow.Save_AddAsset_Button_3.setShortcut(QKeySequence(Qt.Key_Return))
        self.AddAssetAllocationWindow.Cancel_AddAsset_Button_3.setShortcut(QKeySequence(Qt.Key_Escape))
        self.AssetDepartmentAllocationWindow.Save_AddAsset_Button_3.setShortcut(QKeySequence(Qt.Key_Return))
        self.AssetDepartmentAllocationWindow.Cancel_AddAsset_Button_3.setShortcut(QKeySequence(Qt.Key_Escape))
        self.EditAssetInventoryWindow.Save_UpdateAssets_Inventory_Button_3.setShortcut(QKeySequence(Qt.Key_Return))
        self.EditAssetInventoryWindow.Cancel_UpdateAssets_Inventory_Button_3.setShortcut(QKeySequence(Qt.Key_Escape))
        self.AddAssetInventoryWindow.Save_AddAssets_Inventory_Button_4.setShortcut(QKeySequence(Qt.Key_Return))
        self.AddAssetInventoryWindow.Cancel_AddAssets_Inventory_Button_4.setShortcut(QKeySequence(Qt.Key_Escape))
        self.EditDepartmentWindow.Save_EditDepartment_Button_3.setShortcut(QKeySequence(Qt.Key_Return))
        self.EditDepartmentWindow.Cancel_EditDepartment_Button_3.setShortcut(QKeySequence(Qt.Key_Escape))
        self.AddDepartmentWindow.Save_AddDepartment_Button_3.setShortcut(QKeySequence(Qt.Key_Return))
        self.AddDepartmentWindow.Cancel_AddDepartment_Button_3.setShortcut(QKeySequence(Qt.Key_Escape))
        self.AddPaymentWindow.Save_AddPayment_Button_3.setShortcut(QKeySequence(Qt.Key_Return))
        self.AddPaymentWindow.Cancel_AddPayment_Button_3.setShortcut(QKeySequence(Qt.Key_Escape))
        self.AddLoanWindow.Save_AddLoan_Button_4.setShortcut(QKeySequence(Qt.Key_Return))
        self.AddLoanWindow.Cancel_AddLoan_Button_4.setShortcut(QKeySequence(Qt.Key_Escape))
        self.UpdateUserWindow.UpdateAuditor_Button.setShortcut(QKeySequence(Qt.Key_Return))
        self.UpdateUserWindow.Cancel_UpdateAuditor_Button.setShortcut(QKeySequence(Qt.Key_Escape))
        self.AddUserWindow.Save_AddAuditor_Button.setShortcut(QKeySequence(Qt.Key_Return))
        self.AddUserWindow.Cancel_AddAuditor_Button.setShortcut(QKeySequence(Qt.Key_Escape))
        self.UpdateEmployeeWindow.Save_UpdateEmployee_Button_3.setShortcut(QKeySequence(Qt.Key_Return))
        self.UpdateEmployeeWindow.Cancel_UpdateEmployee_Button_3.setShortcut(QKeySequence(Qt.Key_Escape))
        self.AddEmployeeWindow.Save_AddEmployee_Button.setShortcut(QKeySequence(Qt.Key_Return))
        self.AddEmployeeWindow.Cancel_AddEmployee_Button.setShortcut(QKeySequence(Qt.Key_Escape))
        self.SecondWindow.Refresh_Button.setShortcut(QKeySequence(Qt.Key_Escape))


    ### Tables ###
    def loadData (self) : 
        
        self.EmployeesData = []
        self.FinancialLoansData = []
        self.AssetAllocationsData = []
        self.AuditorsData = []
        self.LoansPayment = []
        self.AssetInventoryData = []
        self.DepartmentData = []

        self.get_all_department_names()
        self.get_all_object_names_ToComboBox()

        with Session(engine) as session : 
            EmployeesList = session.query(Employee).all()
            AuditorsList = session.query(Auditor).all()
            FinancialLoansList = session.query(Financial_Loan).all()
            AssestAllocationsList = session.query(Asset_Allocation).all()
            PaymentsList = session.query(Loan_Payment).all()
            AssetsList = session.query(Asset_Inventory).all()
            DepartmentList = session.query(Department).all()

            
            for employee in EmployeesList : 
                departmentcheck = session.query(Department).filter_by(id = employee.Department).first()
                Employee_Data = [employee.id,employee.Employee_Number,employee.Name,employee.Employee_email,departmentcheck.Department_Name,employee.Grade,employee.Address,employee.Phone_Number,employee.Relative_Number,employee.IBAN,employee.Bank]
                self.EmployeesData.append(Employee_Data)
            self.refresh_EmployeesTable(self.EmployeesData)
                

            for Loan in FinancialLoansList : 
                employeeinfo = session.query(Employee).filter(Employee.id == Loan.Employee_ID ).first()
                auditorinfo = session.query(Auditor).filter(Auditor.id == Loan.Auditor_ID).first()
                auditor_name = session.query(Employee).filter(Employee.id==auditorinfo.Employee_ID).first()
                FinancialLoans_Data = [Loan.id,employeeinfo.Name,employeeinfo.Employee_Number,employeeinfo.Department,auditor_name.Name,Loan.Amount,Loan.Type_ofDeposit,Loan.LoanType,Loan.PaidinFull,Loan.Allocation_Date,Loan.Suggested_ReturnDate]
                self.FinancialLoansData.append(FinancialLoans_Data)
            self.refresh_FinancialLoanTable(self.FinancialLoansData)
             
                
            for AssetAllocation in AssestAllocationsList :
                    if AssetAllocation.Note == "Personal":
                        employeeinfo = session.query(Employee).filter(Employee.id == AssetAllocation.Employee_ID).first()
                        auditorinfo = session.query(Auditor).filter(Auditor.id == AssetAllocation.Auditor_ID).first()
                        auditor_name = session.query(Employee).filter(Employee.id == auditorinfo.Employee_ID).first()
                        assetINFO = session.query(Asset_Inventory).filter_by(id = AssetAllocation.Asset_ID).first()
                        AssetAllocations_Data = [AssetAllocation.id,employeeinfo.Name,AssetAllocation.Department_ID,auditor_name.Name,assetINFO.Object_Name,AssetAllocation.Quantity,AssetAllocation.Allocation_Date,AssetAllocation.Return_Date,AssetAllocation.Given_Status,AssetAllocation.Is_Returned,AssetAllocation.Suggested_ReturnDate,AssetAllocation.Return_Status,assetINFO.Serial_Number,assetINFO.Money_Value,AssetAllocation.Note]
                        self.AssetAllocationsData.append(AssetAllocations_Data)

                    elif AssetAllocation.Note == "Department":
                        auditorinfo = session.query(Auditor).filter(Auditor.id == AssetAllocation.Auditor_ID).first()
                        auditor_name = session.query(Employee).filter(Employee.id==auditorinfo.Employee_ID).first()
                        assetINFO = session.query(Asset_Inventory).filter_by(id = AssetAllocation.Asset_ID).first()
                        departmentcheck = session.query(Department).filter_by(id = AssetAllocation.Department_ID).first()
                        employeeinfo = session.query(Employee).filter_by(id = AssetAllocation.Employee_ID).first()
                        AssetAllocations_Data = [AssetAllocation.id,employeeinfo.Name,departmentcheck.Department_Name,auditor_name.Name,assetINFO.Object_Name,AssetAllocation.Quantity,AssetAllocation.Allocation_Date,AssetAllocation.Return_Date,AssetAllocation.Given_Status,AssetAllocation.Is_Returned,AssetAllocation.Suggested_ReturnDate,AssetAllocation.Return_Status,assetINFO.Serial_Number,assetINFO.Money_Value,AssetAllocation.Note]
                        self.AssetAllocationsData.append(AssetAllocations_Data)
            self.refresh_AssestAllocationsTable(self.AssetAllocationsData)
           
            for auditor in AuditorsList :
                    employeeinfo = session.query(Employee).filter(Employee.id == auditor.Employee_ID ).first()
                    Auditors_Data = [auditor.id,employeeinfo.Name,employeeinfo.Employee_Number,auditor.Username,auditor.Password,auditor.Login_Status,auditor.Admin]
                    self.AuditorsData.append(Auditors_Data)
            self.refresh_AuditorsTable(self.AuditorsData)
            

            for Payment in PaymentsList:
                auditorinfo = session.query(Auditor).filter(Auditor.id == Payment.Auditor_ID).first()
                auditor_name = session.query(Employee).filter(Employee.id==auditorinfo.Employee_ID).first()
                Loan_Payments_Data = [Payment.id, Payment.Loan_id, auditor_name.Name,Payment.Amount, Payment.TimeStamp, Payment.Payment_method]
                self.LoansPayment.append(Loan_Payments_Data)
            self.refresh_LoanPaymentTable(self.LoansPayment)
            

            for Asset in AssetsList:
                AssetsInventoryData = [Asset.id,Asset.Object_Name,Asset.Description,Asset.Serial_Number,Asset.Money_Value,Asset.Quantity,Asset.Location]
                self.AssetInventoryData.append(AssetsInventoryData)
            self.refresh_AssetInventoryTable(self.AssetInventoryData)


            for Dep in DepartmentList:
                if Dep.Manager_ID == None:
                    DepartmentsData = [Dep.id, Dep.Department_Name, ""]
                else:
                    employeeinfo = session.query(Employee).filter_by(id = Dep.Manager_ID).first()
                    DepartmentsData = [Dep.id, Dep.Department_Name, employeeinfo.Name]
                self.DepartmentData.append(DepartmentsData)

            self.refresh_DepartmentTable(self.DepartmentData)
    
    
    ### RefreshTables ###
    def refresh_EmployeesTable(self,EmployeesList) :

        self.SecondWindow.Employees_Table_2.setRowCount(0)
        self.SecondWindow.Employees_Table_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.SecondWindow.Employees_Table_2.setColumnHidden(0, True)
        self.EmployeesData = []

        for row,employee in enumerate(EmployeesList) :
            self.SecondWindow.Employees_Table_2.insertRow(row)
            
            for col, data in enumerate(employee):
                item = QTableWidgetItem(str(data))
                self.SecondWindow.Employees_Table_2.setItem(row, col, item)
        
        ### SEARCH ###
        self.SecondWindow.EmployeeID_SearchEmployee_Input_3.textChanged.connect(self.Filter_Employee_Table)
        ### SEARCH ###
    
    def refresh_FinancialLoanTable(self,FinancialLoansList) :

        self.SecondWindow.FinancialLoans_Table_4.setRowCount(0)
        self.SecondWindow.FinancialLoans_Table_4.setColumnHidden(0, True)
        self.FinancialLoansData = []
    
        for row,Loan in enumerate(FinancialLoansList) :
            self.SecondWindow.FinancialLoans_Table_4.insertRow(row)
            for col, data in enumerate(Loan):
                item = QTableWidgetItem(str(data))
                self.SecondWindow.FinancialLoans_Table_4.setItem(row, col, item)
        
        ### Color ###
        with Session(engine) as session:

            for row in FinancialLoansList:
                financial_loan = session.query(Financial_Loan).filter_by(id=row[0]).first()
                allocation_date = financial_loan.Allocation_Date.date()
                suggested_return_date = datetime.strptime(financial_loan.Suggested_ReturnDate, "%Y-%m-%d").date()
                todaydate = date.today()
                
                if financial_loan.PaidinFull == "Yes":
                    if suggested_return_date >= allocation_date:
                        for column in range(self.SecondWindow.FinancialLoans_Table_4.columnCount()):
                            item = self.SecondWindow.FinancialLoans_Table_4.item((financial_loan.id-1), column)
                            if item is not None:
                                item.setBackground(QtGui.QColor("#90EE90"))#green
                    elif suggested_return_date < allocation_date:
                        for column in range(self.SecondWindow.FinancialLoans_Table_4.columnCount()):
                            item = self.SecondWindow.FinancialLoans_Table_4.item((financial_loan.id-1), column)
                            if item is not None:
                                item.setBackground(QtGui.QColor("#E4D00A"))#orange
                elif financial_loan.PaidinFull == "No":
                    if suggested_return_date < todaydate:
                        for column in range(self.SecondWindow.FinancialLoans_Table_4.columnCount()):
                            item = self.SecondWindow.FinancialLoans_Table_4.item((financial_loan.id-1), column)
                            if item is not None:
                                item.setBackground(QtGui.QColor("#C70039"))#Red



        ### SEARCH ###
        self.SecondWindow.EmployeeID_SearchAsset_Input_4.textChanged.connect(self.Filter_Loan_Table)
        ### SEARCH ###
        
    def refresh_AssestAllocationsTable(self,AssestAllocationsList) :
        
        self.SecondWindow.AssetAllocations_Table_3.setRowCount(0)
        self.SecondWindow.AssetAllocations_Table_3.setColumnHidden(0, True)
        self.AssetAllocationsData = []
        for row,Asset in enumerate(AssestAllocationsList) :
            self.SecondWindow.AssetAllocations_Table_3.insertRow(row)
            
            for col, data in enumerate(Asset):
                item = QTableWidgetItem(str(data))
                self.SecondWindow.AssetAllocations_Table_3.setItem(row, col, item)  

        ### Color ###
        with Session(engine) as session:
            for row in AssestAllocationsList:
                asset = session.query(Asset_Allocation).filter_by(id=row[0]).first()
                if asset.Is_Returned == "Yes":
                    if asset.Return_Status == "Healthy":
                        for column in range(self.SecondWindow.AssetAllocations_Table_3.columnCount()):
                            item = self.SecondWindow.AssetAllocations_Table_3.item((asset.id-1), column)
                            if item is not None:
                                item.setBackground(QtGui.QColor("#90EE90"))
                    elif asset.Return_Status == "Half_Damaged":
                            for column in range(self.SecondWindow.AssetAllocations_Table_3.columnCount()):
                                item = self.SecondWindow.AssetAllocations_Table_3.item((asset.id-1), column)
                                if item is not None:
                                    item.setBackground(QtGui.QColor("#E4D00A"))
                    elif asset.Return_Status == "Damaged":
                            for column in range(self.SecondWindow.AssetAllocations_Table_3.columnCount()):
                                item = self.SecondWindow.AssetAllocations_Table_3.item((asset.id-1), column)
                                if item is not None:
                                    item.setBackground(QtGui.QColor("#C70039"))


        ### SEARCH ###
        self.SecondWindow.EmployeeID_SearchAsset_Input_4.textChanged.connect(self.Filter_Asset_Table)
        ### SEARCH ###

    def refresh_AuditorsTable(self,AuditorsList) :
        
        self.SecondWindow.Auditors_Table_2.setRowCount(0)
        self.SecondWindow.Auditors_Table_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.SecondWindow.Auditors_Table_2.setColumnHidden(0, True)
        self.AuditorsData = []

        for row,auditor in enumerate(AuditorsList) :
            self.SecondWindow.Auditors_Table_2.insertRow(row)
            
            for col, data in enumerate(auditor):
                item = QTableWidgetItem(str(data))
                self.SecondWindow.Auditors_Table_2.setItem(row, col, item) 

        ### SEARCH ###
        self.SecondWindow.EmployeeID_SearchAuditor_Input_2.textChanged.connect(self.Filter_Auditor_Table)
        ### SEARCH ###   

    def refresh_LoanPaymentTable(self,PaymentsList) :
        
        self.SecondWindow.LoanPayments_Table_5.setRowCount(0)
        self.SecondWindow.LoanPayments_Table_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.SecondWindow.LoanPayments_Table_5.setColumnHidden(0, True)
        self.LoansPayment = []

        for row,Payment in enumerate(PaymentsList) :
            self.SecondWindow.LoanPayments_Table_5.insertRow(row)
            
            for col, data in enumerate(Payment):
                item = QTableWidgetItem(str(data))
                self.SecondWindow.LoanPayments_Table_5.setItem(row, col, item)  

        ### SEARCH ###
        self.SecondWindow.EmployeeID_SearchAsset_Input_4.textChanged.connect(self.Filter_Payment_Table)
        ### SEARCH ###
    
    def refresh_DepartmentTable(self,DepartmentList) :
        
        self.SecondWindow.Assets_Inventory_Table_2.setRowCount(0)
        self.SecondWindow.Assets_Inventory_Table_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.SecondWindow.Assets_Inventory_Table_2.setColumnHidden(0, True)
        self.DepartmentData = []
        for row,Dep in enumerate(DepartmentList) :
            self.SecondWindow.Assets_Inventory_Table_2.insertRow(row)
            
            for col, data in enumerate(Dep):
                item = QTableWidgetItem(str(data))
                self.SecondWindow.Assets_Inventory_Table_2.setItem(row, col, item)  

        ### SEARCH ###
        self.SecondWindow.SearchDepartment_Input_5.textChanged.connect(self.Filter_Department_Table)
        ### SEARCH ###

    def refresh_AssetInventoryTable(self,AssetsList) :
        
        self.SecondWindow.Assets_Inventory_Table.setRowCount(0)
        self.SecondWindow.Assets_Inventory_Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.SecondWindow.Assets_Inventory_Table.setColumnHidden(0, True)
        self.AssetInventoryData = []
        for row,Asset in enumerate(AssetsList) :
            self.SecondWindow.Assets_Inventory_Table.insertRow(row)
            
            for col, data in enumerate(Asset):
                item = QTableWidgetItem(str(data))
                self.SecondWindow.Assets_Inventory_Table.setItem(row, col, item)
                
        self.SecondWindow.EmployeeID_SearchAssets_Inventory_Input_3.textChanged.connect(self.Filter_AssetInventory_Table)


    ### Row Selection ###
    def Row_Selection(self):
        self.SecondWindow.Employees_Table_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SecondWindow.FinancialLoans_Table_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SecondWindow.LoanPayments_Table_5.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SecondWindow.AssetAllocations_Table_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SecondWindow.Auditors_Table_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SecondWindow.Assets_Inventory_Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SecondWindow.Assets_Inventory_Table_2.setSelectionBehavior(QAbstractItemView.SelectRows)## Department table


    ### Vaidation ###        
    def Data_Vaidation (self) : 
        self.AddEmployeeWindow.EmployeeID_input_AddEmployee_2.setValidator(self.IntType)
        self.UpdateEmployeeWindow.EmployeeID_input_UpdateEmployee_2.setValidator(self.IntType)
        self.AddUserWindow.EmployeeID_input_AddAudtior_2.setValidator(self.IntType)
        self.UpdateUserWindow.EmployeeID_input_UpdateAudtior_2.setValidator(self.IntType)
        self.AddAssetAllocationWindow.EmployeeID_input_AddAsset_3.setValidator(self.IntType)
        self.AddLoanWindow.EmployeeID_input_AddLoan_4.setValidator(self.IntType)
        self.AddLoanWindow.LoanAmount_Input_4.setValidator(self.IntType)
        self.AddPaymentWindow.LoanID_Input_AddPayment_2.setValidator(self.IntType)
        self.AddAssetAllocationWindow.AuditorID_Input_AddAssest_3.setValidator(self.IntType)
        self.AddLoanWindow.AuditorID_Input_AddLoan_4.setValidator(self.IntType)
        self.AddPaymentWindow.AuditorID_Input_AddPayment_2.setValidator(self.IntType)
        self.AddPaymentWindow.PaymentAmount_Input_2.setValidator(self.IntType)
        self.AddEmployeeWindow.EmployeePhoneNumber_input_AddEmployee_2.setValidator(self.IntType)
        self.UpdateEmployeeWindow.EmployeePhoneNumber_input_UpdateEmployee_2.setValidator(self.IntType)
        self.AddEmployeeWindow.EmployeeRelativeNumber_input_AddEmployee_2.setValidator(self.IntType)
        self.UpdateEmployeeWindow.EmployeeRelativeNumber_input_UpdateEmployee_2.setValidator(self.IntType)
        self.AddAssetInventoryWindow.MoneyValue_input_AddAssets_Inventory_4.setValidator(self.IntType)
        self.AddAssetAllocationWindow.Quantity_input_AddAsset_3.setValidator(self.IntType)
        self.AddAssetInventoryWindow.Quantity_input_AddAssets_Inventory_4.setValidator(self.IntType)
        self.AddDepartmentWindow.ManagerID_Input_2.setValidator(self.IntType)
        self.UpdateEmployeeWindow.EmployeeID_input_UpdateEmployee_2.setReadOnly(True)
        self.UpdateUserWindow.EmployeeID_input_UpdateAudtior_2.setReadOnly(True)
        self.ReturnAssetWindow.AssetID_returnAsset_2.setReadOnly(True)
        self.AddAssetAllocationWindow.AuditorID_Input_AddAssest_3.setReadOnly(True)
        self.AddPaymentWindow.AuditorID_Input_AddPayment_2.setReadOnly(True)
        self.AddPaymentWindow.LoanID_Input_AddPayment_2.setReadOnly(True)
        self.AddLoanWindow.EmployeeID_input_AddLoan_4.setReadOnly(True) 
        self.AddLoanWindow.AuditorID_Input_AddLoan_4.setReadOnly(True) 
        self.AddAssetAllocationWindow.EmployeeID_input_AddAsset_3.setReadOnly(True)
        self.AddUserWindow.EmployeeID_input_AddAudtior_2.setReadOnly(True)
        self.AssetDepartmentAllocationWindow.EmployeeID_input_AddAsset_3.setReadOnly(True)
        self.AssetDepartmentAllocationWindow.AuditorID_Input_AddAssest_3.setReadOnly(True)
        self.AssetDepartmentAllocationWindow.Quantity_input_AddAsset_3.setValidator(self.IntType)
        self.SecondWindow.Employees_Table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SecondWindow.FinancialLoans_Table_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SecondWindow.AssetAllocations_Table_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SecondWindow.LoanPayments_Table_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SecondWindow.Auditors_Table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SecondWindow.Assets_Inventory_Table_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SecondWindow.Assets_Inventory_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.AddLoanWindow.SuggestedReturnDate_Input_AddLoan_4.setLocale(QLocale(QLocale.English))
        self.AddLoanWindow.SuggestedReturnDate_Input_AddLoan_4.setDate(date.today())
        self.AddAssetAllocationWindow.SuggestedReturnDate_Input_AddAsset_3.setDate(date.today())
        self.AssetDepartmentAllocationWindow.SuggestedReturnDate_Input_AddAsset_3.setDate(date.today())

    ### Filters ###
    def Filter_SearchEmployee_Asset(self):
        selected_row = self.SecondWindow.Employees_Table_2.currentRow()
        if selected_row >= 0:
            search_query_loan = self.SecondWindow.Employees_Table_2.item(selected_row,1).text()
            search_query_asset = self.SecondWindow.Employees_Table_2.item(selected_row,2).text()
            search_query_payment = self.SecondWindow.Employees_Table_2.item(selected_row,3).text()
            self.Filter_Asset_Table(search_query_asset)
            self.Filter_Loan_Table(search_query_loan)
            self.Filter_Payment_Table(search_query_payment)
        else : 
            self.loadData()

    def Filter_SearchLoan_Payment(self):
        selected_row = self.SecondWindow.FinancialLoans_Table_4.currentRow()
        if selected_row >= 0:
            self.id = self.SecondWindow.FinancialLoans_Table_4.item(selected_row,0).text()
            search_query = self.SecondWindow.FinancialLoans_Table_4.item(selected_row,0).text()
            self.Filter_Payment_Table(search_query)
        else : 
            self.loadData()

    def Filter_SearchEmployeeAsset_Department(self):
        selected_row = self.SecondWindow.Assets_Inventory_Table_2.currentRow()
        if selected_row >= 0:
            search_query = self.SecondWindow.Assets_Inventory_Table_2.item(selected_row,1).text()
            self.Filter_Employee_Table(search_query)
            self.Filter_Asset_Table(search_query)
        else : 
            self.loadData()

    def Filter_SearchAsset_AssetAllocation(self):
        selected_row = self.SecondWindow.Assets_Inventory_Table.currentRow()
        if selected_row >= 0:
            search_query = self.SecondWindow.Assets_Inventory_Table.item(selected_row,1).text()
            self.Filter_Asset_Table(search_query)
        else : 
            self.loadData()

    def Filter_Employee_Table(self, search_query):
        num_rows = self.SecondWindow.Employees_Table_2.rowCount()
        for row in range(num_rows):
            hide_row = True
            for column in range(5):
                if column == 3:
                    continue
                item = self.SecondWindow.Employees_Table_2.item(row, column)
                if item and search_query.lower() in item.text().lower():
                    hide_row = False
                    break
            self.SecondWindow.Employees_Table_2.setRowHidden(row, hide_row)

    def Filter_Loan_Table(self, search_query):

        num_rows = self.SecondWindow.FinancialLoans_Table_4.rowCount()
        for row in range(num_rows):
            hide_row = True
            for column in range(3):
                if column == 0:
                    continue
                item = self.SecondWindow.FinancialLoans_Table_4.item(row, column)
                if item and search_query.lower() in item.text().lower():
                    hide_row = False
                    break
            self.SecondWindow.FinancialLoans_Table_4.setRowHidden(row, hide_row)

    def Filter_Asset_Table(self, search_query):
        num_rows = self.SecondWindow.AssetAllocations_Table_3.rowCount()
        for row in range(num_rows):
            hide_row = True
            for column in range(5):
                if column == 0:
                    continue
                
                elif column == 3:
                    continue
                item = self.SecondWindow.AssetAllocations_Table_3.item(row, column)
                if item and search_query.lower() in item.text().lower():
                    hide_row = False
                    break
            self.SecondWindow.AssetAllocations_Table_3.setRowHidden(row, hide_row)

    def Filter_Payment_Table(self, search_query):
        num_rows = self.SecondWindow.LoanPayments_Table_5.rowCount()
        for row in range(num_rows):
            hide_row = True
            for column in range(2):
                if column == 0:
                    continue
                item = self.SecondWindow.LoanPayments_Table_5.item(row, column)
                if item and search_query.lower() in item.text().lower():
                    hide_row = False
                    break
            self.SecondWindow.LoanPayments_Table_5.setRowHidden(row, hide_row)

    def Filter_Auditor_Table(self, search_query):
        num_rows = self.SecondWindow.Auditors_Table_2.rowCount()
        for row in range(num_rows):
            hide_row = True
            for column in range(3):
                item = self.SecondWindow.Auditors_Table_2.item(row, column)
                if item and search_query.lower() in item.text().lower():
                    hide_row = False
                    break
            self.SecondWindow.Auditors_Table_2.setRowHidden(row, hide_row)

    def Filter_Department_Table(self, search_query):
        num_rows = self.SecondWindow.Assets_Inventory_Table_2.rowCount()
        for row in range(num_rows):
            hide_row = True
            for column in range(3):
                if column == 0:
                    continue
                item = self.SecondWindow.Assets_Inventory_Table_2.item(row, column)
                if item and search_query.lower() in item.text().lower():
                    hide_row = False
                    break
            self.SecondWindow.Assets_Inventory_Table_2.setRowHidden(row, hide_row)

    def Filter_AssetInventory_Table(self, search_query):
        num_rows = self.SecondWindow.Assets_Inventory_Table.rowCount()
        for row in range(num_rows):
            hide_row = True
            for column in range(2):
                if column == 0:
                    continue
                item = self.SecondWindow.Assets_Inventory_Table.item(row, column)
                if item and search_query.lower() in item.text().lower():
                    hide_row = False
                    break
            self.SecondWindow.Assets_Inventory_Table.setRowHidden(row, hide_row)

        
    ### Cancel Functions ###
    def AddEmployeeCancel(self):
        self.AddEmployeeWindow.hide()
        self.AddEmployeeWindow.EmployeeID_input_AddEmployee_2.clear()
        self.AddEmployeeWindow.EmployeeName_input_AddEmployee_2.clear()
        self.AddEmployeeWindow.EmployeeEmail_input_AddEmployee_2.clear()
        self.AddEmployeeWindow.EmployeeDepartment_Enum_AddEmployee_2.setCurrentIndex(0)
        self.AddEmployeeWindow.EmployeeGrade_Enum_AddEmployee_2.setCurrentIndex(0)
        self.AddEmployeeWindow.EmployeeAddress_input_AddEmployee_2.clear()
        self.AddEmployeeWindow.EmployeePhoneNumber_input_AddEmployee_2.clear()
        self.AddEmployeeWindow.EmployeeRelativeNumber_input_AddEmployee_2.clear()
        self.AddEmployeeWindow.EmployeeIBAN_input_AddEmployee_2.clear()
        self.AddEmployeeWindow.EmployeeBank_input_AddEmployee_2.clear()

    def EditEmployeeCancel(self):
        self.UpdateEmployeeWindow.hide()
        self.UpdateEmployeeWindow.EmployeeID_input_UpdateEmployee_2.clear()
        self.UpdateEmployeeWindow.EmployeeName_input_UpdateEmployee_2.clear()
        self.UpdateEmployeeWindow.EmployeeEmail_input_UpdateEmployee_2.clear()
        self.UpdateEmployeeWindow.EmployeeDepartment_Enum_UpdateEmployee_3.setCurrentIndex(0)
        self.UpdateEmployeeWindow.EmployeeGrade_Enum_UpdateEmployee_2.setCurrentIndex(0)
        self.UpdateEmployeeWindow.EmployeeAddress_input_UpdateEmployee_2.clear()
        self.UpdateEmployeeWindow.EmployeePhoneNumber_input_UpdateEmployee_2.clear()
        self.UpdateEmployeeWindow.EmployeeRelativeNumber_input_UpdateEmployee_2.clear()
        self.UpdateEmployeeWindow.EmployeeIBAN_input_UpdateEmployee_2.clear()
        self.UpdateEmployeeWindow.EmployeeBank_input_UpdateEmployee_3.clear()

    def AddAuditorCancel(self):
        self.AddUserWindow.hide()
        self.AddUserWindow.EmployeeID_input_AddAudtior_2.clear()
        self.AddUserWindow.Username_input_AddAudtior_2.clear()
        self.AddUserWindow.Password_input_AddAudtior_2.clear()
        self.AddUserWindow.Admin_Enum_AddAudtior_2.setCurrentIndex(0)
    
    def EditAuditorsCancel(self):
        self.UpdateUserWindow.hide()
        self.UpdateUserWindow.EmployeeID_input_UpdateAudtior_2.clear()
        self.UpdateUserWindow.Username_input_UpdateAudtior_2.clear()
        self.UpdateUserWindow.Password_input_UpdateAudtior_2.clear()
        self.UpdateUserWindow.Admin_Enum_UpdateAudtior_2.setCurrentIndex(0)

    def AddLoansCancel(self):
        self.AddLoanWindow.hide()
        self.AddLoanWindow.EmployeeID_input_AddLoan_4.clear()
        self.AddLoanWindow.AuditorID_Input_AddLoan_4.clear()
        self.AddLoanWindow.LoanAmount_Input_4.clear()
        self.AddLoanWindow.TypeofDeposit_Enum_4.setCurrentIndex(0)
        self.AddLoanWindow.LoanType_Enum_4.setCurrentIndex(0)

    def AddPaymentCancel(self):
        self.AddPaymentWindow.hide()
        self.Loans_and_Payments_List()
        self.AddPaymentWindow.LoanID_Input_AddPayment_2.clear()
        self.AddPaymentWindow.AuditorID_Input_AddPayment_2.clear()
        self.AddPaymentWindow.PaymentAmount_Input_2.clear()
        self.AddPaymentWindow.PaymentMethod_Enum_2.setCurrentIndex(0)

    def AddAssetAllocationCancel(self):
        self.AddAssetAllocationWindow.hide()
        self.AddAssetAllocationWindow.EmployeeID_input_AddAsset_3.clear()
        self.AddAssetAllocationWindow.AuditorID_Input_AddAssest_3.clear()
        self.AddAssetAllocationWindow.ObjectName_Enum.setCurrentIndex(0)
        self.AddAssetAllocationWindow.Quantity_input_AddAsset_3.clear()
        self.AssetDepartmentAllocationWindow.hide()
        self.AssetDepartmentAllocationWindow.EmployeeID_input_AddAsset_3.clear()
        self.AssetDepartmentAllocationWindow.AuditorID_Input_AddAssest_3.clear()
        self.AssetDepartmentAllocationWindow.ObjectName_Enum.setCurrentIndex(0)
        self.AssetDepartmentAllocationWindow.Quantity_input_AddAsset_3.clear()
    
    def AddAssetInventoryCancel (self) : 
            self.AddAssetInventoryWindow.hide()
            self.AddAssetInventoryWindow.ObjectName_input_AddAssets_Inventory_4.clear()
            self.AddAssetInventoryWindow.SerialNumber_input_AddAssets_Inventory_4.clear()
            self.AddAssetInventoryWindow.Quantity_input_AddAssets_Inventory_4.clear()
            self.AddAssetInventoryWindow.MoneyValue_input_AddAssets_Inventory_4.clear()
            self.AddAssetInventoryWindow.Location_input_AddAssets_Inventory_5.clear()
            self.AddAssetInventoryWindow.description_Input_AddAssets_Inventory_4.clear()
        
    def EditAssetInventoryCancel(self):
        self.EditAssetInventoryWindow.hide()
        self.EditAssetInventoryWindow.ObjectName_input_EditAssets_Inventory_5.clear()
        self.EditAssetInventoryWindow.description_Input_EditAssets_Inventory_5.clear()
        self.EditAssetInventoryWindow.SerialNumber_input_EditAssets_Inventory_5.clear()
        self.EditAssetInventoryWindow.MoneyValue_input_EditAssets_Inventory_5.clear()
        self.EditAssetInventoryWindow.Quantity_input_EditAssets_Inventory_5.clear()
        self.EditAssetInventoryWindow.Location_input_EditAssets_Inventory_6.clear()

    def AddDepartmentCancel(self):
            self.AddDepartmentWindow.hide()
            self.AddDepartmentWindow.Name_input_AddDepartment_7.clear()
            self.AddDepartmentWindow.ManagerID_Input_2.clear()
            
    def EditDepartmentCancel(self):
            self.EditDepartmentWindow.hide()
            self.EditDepartmentWindow.Name_input_EditDepartment_7.clear()
            self.EditDepartmentWindow.EditManagerID_Input_2.clear()

    def ReturnAssetCancel(self):
            self.ReturnAssetWindow.hide()
            self.ReturnAssetWindow.AssetID_returnAsset_2.clear()
            self.ReturnAssetWindow.Returned_Enum_3.setCurrentIndex(0)
            self.ReturnAssetWindow.DamageStatus_Enum_3.setCurrentIndex(0)
            self.ReturnAssetWindow.Notes_Returned_Input_3.clear()



    def run(self) :
        self.Window.show()
        self.App.exec()

App= MainApp()
App.run()