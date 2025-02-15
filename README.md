# Loan-Asset-Management-System


## Overview
Loan-Asset-Management-System is a PyQt5-based application for managing assets, loans, and employee records. It supports multiple languages and includes features for adding, editing, and searching records.

## Features
- **Employee Management**: Add, edit, and remove employee records.
- **Asset Allocation and Inventory Management**: Manage asset allocation and inventory.
- **Loan Management**: Manage loans and payments.
- **Multi-language Support**: Supports English and Arabic.
- ### **Asset & Loan Status Indicator**  
The system uses a **color-coded status** to track the condition of assets and loan payments:  
- 🟢 **Green** – Paid loan / Healthy asset  
- 🔴 **Red** – Unpaid & late loan / Damaged asset  
- 🟡 **Yellow** – Paid but late loan / Half-damaged asset  
- ⚪ **White** – Unpaid & not late loan / Asset currently with the employee  

## Screenshots of Application Pages : 

### Login Page
![Login Page]( https://github.com/AbdulrahmanOtb/Loan-Asset-Management-System/blob/main/Loan-Asset-Management-System/LoginPage.jpg )
  
### Employees Management Page
![Employees Management](https://github.com/AbdulrahmanOtb/Loan-Asset-Management-System/blob/main/Loan-Asset-Management-System/EmployeesPage.png)
### Asset Inventory Management
![Asset_Inventory](https://github.com/AbdulrahmanOtb/Loan-Asset-Management-System/blob/main/Loan-Asset-Management-System/AssetInventoryPage.png)

### Departments Management
![Departments](https://github.com/AbdulrahmanOtb/Loan-Asset-Management-System/blob/main/Loan-Asset-Management-System/DepartmentPage.png)

### Users Management
![Users](https://github.com/AbdulrahmanOtb/Loan-Asset-Management-System/blob/main/Loan-Asset-Management-System/UsersPage.png)

### Financial Loan & Loan Payments Management
![Financial](https://github.com/AbdulrahmanOtb/Loan-Asset-Management-System/blob/main/Loan-Asset-Management-System/FinancialAndLoanPayments_Page.png)

### Asset Allocation Management
![Financial](https://github.com/AbdulrahmanOtb/Loan-Asset-Management-System/blob/main/Loan-Asset-Management-System/AssetAllocationPage.png)


## Getting Started

### Prerequisites
- Python 3.7+
- PyQt5
- SQLModel

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Loan-Asset-Management-System.git
    cd Loan-Asset-Management-System
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application
1. Run the application:
    ```sh
    python MainApp.py
    ```
    

## Usage
1. Launch the application.
2. Log in using your credentials. If you don't have an account, contact the administrator to create one for you.
3. Use the various tabs to manage employees, assets, loans, and payments.

## Project Structure
- **MainApp.py**: Entry point of the application.
- **MainWindow.py**: Handles the login page UI and functionality.
- **SecondMainWindow.py**: Main window of the application.
- **Translation_list.py**: Contains translation data and functions.
- **Data_operations.py**: Contains data operation classes and methods.
- **Data_modeling.py**: Contains database models and schema definitions.
- **There is many python files to handle the operations in the windows like add,return,edit, and UI files designed by PyQt**

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
