class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is", self.name)


p = Person("Jack")
# p.say_hi()
#前面两行同样可以写作
# Person("Michael").say_hi()


class Robot:
    """类的文档字符串"""
    population = 0


    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):
        """方法的文档字符串"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))


# r1 = Robot("r1")
# r1.say_hi()
# Robot.how_many()
#
# r2 = Robot("r2")
# r2.say_hi()
# Robot.how_many()
#
# r1.die()
# r2.die()
# Robot.how_many()
#
# print(Robot.__doc__)
# print(Robot.say_hi.__doc__)

class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized schoolmember: {})".format(self.name))

    def tell(self):
        print("Name:\"{}\" Age:\"{}\"".format(self.name, self.age))


class Techer(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("(Initialized techer: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("(Initialized student: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Techer("jack", 40, 60000)
s = Student("michael", 22, 88)
members = [t,s]
# for member in members:
#     member.tell()


