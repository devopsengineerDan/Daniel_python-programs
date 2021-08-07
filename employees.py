def add_employee(emp, emp_list=[]): 
    emp_list.append(emp)
    print(emp_list)
    
emps = ['John', 'Jane']

add_employee('Dan', emps)
add_employee('Otieno', emps)
add_employee('Kevin', emps)
