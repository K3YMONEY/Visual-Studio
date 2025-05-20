#create a dictionary of an employee with first name, last name,ID,email and organisation.
Employee_info = {
    'first_name' : 'Robert',
    'last_name' : 'muiruri',
    'ID' : 12345678,
    'Email' : 'rober32@gmail.com',
    'Organisation' : 'KMD'
}
print(Employee_info)
print(Employee_info['last_name'])
Employee_info['position'] = 'Manager'
print(Employee_info)
del Employee_info['last_name']
print(Employee_info)
Employee_info.clear()
print(Employee_info)