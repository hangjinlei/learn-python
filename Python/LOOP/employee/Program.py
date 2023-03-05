"""
类
    magic methods
        https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
        __init__ # 构造函数
        __repr__ # 用于调试
        __str__ # 用于用户
        __dict__ # 用于查看对象变量: 根据调用者的不用, 分为类级别或实例级别

    重载运算符
        __add__ # +

    静态变量: num_of_emps, raise_amnt
        在类中访问时最好使用self, 以便于实例重新赋值 (best practice)

    校验数据: assert

    构造函数: __init__
        实例变量: first, last, pay, email
    实例方法: fullname, raise_amount
    类方法: set_raise_amt, from_string
    静态方法: is_workday

继承
    新增方法: __init__, add_emp, remove_emp, print_emps
"""

from datetime import datetime
from employee import Employee
from developer import Developer
from manager import Manager

emp_1 = Developer("Corey", "Schafer", 50000, "C#")
emp_2 = Developer("Test", "User", 60000, "Python")

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

print(Employee.num_of_emps)

print(Employee.raise_amnt)
Employee.set_raise_amt(1.05)
print(Employee.raise_amnt)

emp_3 = Employee.from_string(emp_str_1)
print(emp_3.email)
emp_3.fullname = "John Smith"
print(emp_3.fullname)


day = datetime(year=2023, month=3, day=4)
print(Employee.is_workday(day))

mgr_1 = Manager("bill", "gates", 90000, [emp_1])
mgr_1.add_emp(emp_2)
mgr_1.remove_emp(emp_1)
mgr_1.print_emps()

print(repr(emp_1))
print(repr(mgr_1))
print(str(mgr_1))

print(emp_1 + emp_2)
