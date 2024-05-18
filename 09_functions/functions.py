def hello_world():
  pass
  
hello_world()

def hello_world1():
  print('-------------')
  print("Hello World from (1)")

hello_world1()

def hello_world2():
  return "hello humanity from (2)"

print(hello_world2())

def hello_world3(name = 'My friend'):
  return (f'Hello {name} from (3)')

print(hello_world3('Shubham'))

def hello_world4(greeting, name = 'My friend'):
  return (f'{greeting}, {name} from (4)')

print(hello_world4('Hi', 'Shubham'))
print(hello_world4('Shubham', 'Hi'))
print(hello_world4(name = 'Shubham', greeting = 'Hi'))


def student_info(*args, **kwargs):
  print(args) # returns tuple ('args' are Non-Keyword arguments)
  print(kwargs) # returns dictionary ('kwargs' are Keyword arguments) 

student_info('Maths', 'Art', name = 'Shubham', age = 21)

student_info('Math', 'Science', 'Art', name = 'Shubham', age = 21)



def myFuc(*args):
  for arg in args:
    print(arg)

myFuc(1,2,3,4,5)


def myFun(arg1, *args):
  print(arg1)
  for i in args:
    print("Next argument through *args: ", i)

myFun('Hello','Welcome', 'to', 'Python')


def myFun(**kwargs):
  for key, value in kwargs.items():
    print("%s == %s" % (key, value))

myFun(first = 'Inter', mid = 'Stellar', last = 'Hans Zimmar')

def myFun(**kwargs):
  for key, value in kwargs.items():
    print(f"The {key} == {value}")

myFun(first = 'Inter', mid = 'Stellar', last = 'Hans Zimmar')


def myFun(arg1,arg2, **kwargs):
  print(arg1)
  print(arg2)
  for i,j in kwargs.items():
    print(f"{i} == {j}")

myFun('-----------------------','Hello', first = 'Inter', mid = 'Stellar', last = 'Hans Z')


courses = ['Maths', 'Science', 'Art', 'History']
info = {'Name':'Siddhesh', 'Age':21, 'Gender':'Male'} 

def func(*args, **kwargs):
  print('-------------')
  print(args)
  print(kwargs)

func(courses, info)
func(*courses, **info)



month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]


def is_leap(year):

  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) 


def days_in_month(year, month):

  if not 1 <= month <= 12:
    return 'Invalid Month'

  if month == 2 and is_leap(year):
    return 29

  return month_days[month]


print(days_in_month(2024,3))
print(days_in_month(2024,13))
print(days_in_month(2024,2))