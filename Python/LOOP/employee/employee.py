from datetime import datetime


class Employee:

    num_of_emps: int = 0  # static variable
    raise_amnt: int = 1.04

    def __init__(self, first: str, last: str, pay: str) -> None:
        """
        constructor
        """

        assert pay > 0

        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def __repr__(self):
        """
        print the employee's information for debugging
        """
        return "{}('{}', '{}', '{}')".format(self.__class__.__name__, self.first, self.last, self.pay)

    def __str__(self):
        """
        print the employee's information for users
        """
        return "{} - {}".format(self.fullname, self.email)

    def __add__(self, other):
        """
        calculate the sum of two employees' pay
        """
        return self.pay + other.pay

    @property  # getter
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):  # instance method
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name: str):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    def raise_amount(self):  # instance method
        self.pay = int(self.pay * self.raise_amnt)

    @classmethod
    def set_raise_amt(cls, amount: int):  # class method
        cls.raise_amnt = amount

    @classmethod
    def from_string(cls, emp_str: str):  # class method
        first, last, pay = emp_str.split("-")
        return cls(first, last, float(pay))

    @staticmethod
    def is_workday(day: datetime) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
