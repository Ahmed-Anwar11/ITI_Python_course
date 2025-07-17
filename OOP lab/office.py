class Office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        employees = [] 

    def get_all_employees(self):
        return self.employees

    
    def get_employee(self, empid):
        self.empid = empid
        if empid in self.employees:
            return self.employees[empid]
        else:
            return None
               
    
    def hire(self, employee):
        self.employee = employee
        self.employees.append(employee)
    
    def fire(self, employee):
        self.employee = employee
        self.employees.pop(employee)
            
      
    def deduct(self, empid, deduction):
        self.empid = empid
        self.deduction = deduction
        employee = self.get_employee(empid)
        employee.salary -= deduction
            
    def reward(self, empid, reward):
        self.empid = empid
        self.reward = reward
        employee = self.get_employee(empid)
        employee.salary += reward


    

