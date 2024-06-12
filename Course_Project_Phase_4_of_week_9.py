from datetime import datetime

def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetUserName():
    UserName = input("Enter user name or 'End' to quit: ")
    return UserName

def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ")
            

def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
           break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("user Name: ", username, " Password ", userpassword, " Role: ", userrole)
       
def Login():
     UserFile = open("Users.txt", "r")
     UserList = []
     UserName = input("Enter User Name: ")
     UserPwd = input("Enter Password: ")
     UserRole = "None"
     while True:
         UserDetail = UserFile.readline()
         if not UserDetail:
            return UserRole, UserName, UserPwd
         UserDetail = UserDetail.replace("\n", "")
         
         UserList = UserDetail.split("|")
         if UserName == UserList[0] and UserPwd == UserList[1]:
             UserRole = UserList[2] 
             return UserRole, UserName      
     return UserRole, UserName
      
def GetEmpname():
    empname = input("Enter employee name: ")
    return empname
     
def GetDatesWorked():
    fromdate = input("Enter start date (mm/dd/yyyy): ")
    todate = input("Enter End date (mm/dd/yyyy): ")
    return fromdate, todate
 
def GetHoursWorked():
    hours = float(input("Enter amount of hours worked: "))
    return hours
 
def GetHourlyrate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate
 
def GettaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate 
 
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
 
def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrosspay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    EmpFile = open("Employees.txt", "r")
    while True:
        rundate = input("Enter start date for report (mm/dd/yyyy) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%y")
            break
        except ValueError:
            print("invalid date format. Try again.")
            print()
            continue    
    while True:
         EmpDetail = EmpFile.readline()
         if not EmpDetail:
             break
         EmpDetail = EmpDetail.replace("\n", "")
         
         EmpList = EmpDetail.split("|")
         fromdate = EmpList[0]
         if (str(rundate).upper() != "ALL"):
             checkdate = datetime.strptime(fromdate, "%m/%d/%y")
             if (checkdate < rundate):
                 continue 
             todate = EmpList[1]
             empname = EmpList[2]
             hours = float(EmpList[3])
             hourlyrate = float(EmpList [4])
             taxrate = float(EmpList[5])
             grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)  
             print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
             TotEmployees += 1
             Tothours += hours
             TotGrossPay += grosspay 
             TotTax += incometax
             Totneypay += netpay 
             EmpTotals["TotEmp"] = TotEmployees
             EmpTotals["Tothrs"] = TotHours
             EmpTotals["TotGrossPay"] = TotGrossPay
             EmpTotals["TotTax"] = TotTax
             EmpTotals["TotNetPay"] = TotNetPay
             DetailsPrinted = True
         if (DetailsPrinted):
             PrintTotals(EmpTotals)
         else:
             print("No detail information to print")
              
def PrintTotals(EmpTotals):
    print()
    print(f'Total number of employees: {EmpTotals["TotEmp"]}')
    print(f'Total hours worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total gross pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total income tax: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total net pay: {EmpTotals["TotNetPay"]:,.2f}')
     
if __name__ == "__main__":
    CreateUsers()
    print()
    print("Data Entry")
    UserRole, username = Login()
    DetailsPrinted = False
    EmpTotals = {}
    if (UserRole.upper() == "NONE"):
        print(username, "is invalid.")
        
    else:   
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("Employees.txt", "a+")
            while True:
                empname = GetEmpname()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = GetDatesWorked()
                hours = GetHoursWorked()
                hourlyrate = GetHourlyrate()
                taxrate = GettaxRate()
                EmpDetail = fromdate + "|" + todate + "|" + empname + "|" + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
                EmpFile.write(EmpDetail)
            EmpFile.close()   
        printinfo(DetailsPrinted)
        
        

             
         


     
 
                   
                 
                      
                      
   
            
            
