from car import Car
from employee import Employee
from office import Office

car1 = Car("Fiat 128", fuelRate=100, velocity=60)

emp1 = Employee(
    name="Samy",
    money=5000,
    id=1,
    car=car1,
    email="samy@mail.com",
    salary=5000,
    distanceToWork=20
)

office = Office("ITI")

office.hire(emp1)

emp1.sleep(7)
emp1.eat(3)
emp1.work(8)

emp1.drive(60)

office.check_lateness(emp1.id, moveHour=8)

print("Employees:", [e.name for e in office.get_all_employees()])
print("Salary:", emp1.salary)
