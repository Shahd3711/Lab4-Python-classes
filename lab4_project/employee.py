from person import Person
import re

class Employee(Person):
    def __init__(self, name, money, id, car, email, salary, distanceToWork):
        super().__init__(name, money)
        self.id = id
        self.car = car
        self.email = email if self.validate_email(email) else "invalid@mail.com"
        self.salary = max(salary, 1000)
        self.distanceToWork = distanceToWork

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, velocity):
        self.car.run(velocity, self.distanceToWork)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)

    def send_mail(self, to, subject, msg, receiver_name):
        with open("email.txt", "w") as f:
            f.write(f"From: {self.email}\n")
            f.write(f"To: {to}\n")
            f.write(f"Subject: {subject}\n\n")
            f.write(f"Hi, {receiver_name}\n")
            f.write(msg + "\n")
            f.write("Thanks\n")
