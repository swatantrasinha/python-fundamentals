# ![python fundamentals](./Python-logo.jpg "python logo") PYTHON FUNDAMENTALS : [Course Link](https://app.pluralsight.com/ilx/video-courses/clips/9be6a792-b1cb-4fe6-990f-9b746e31f9e6 "Python Pluralsight Course")

---
 ## Chapter 01 - Introduction   
 
  <details>
    <summary>Why Python ?</summary>
      <p>  
        1. **Versatile** programming language.It can be used in :   
          - Data Science
          - Machine Learning
          - Web Development

        2. Strong Community   
          There is a package for everything

        3. Easy to Learn   
          - easy to read
          - concise
          - interpreted language

      </p>
  </details>

---
 ## Chapter 02 - Explore Data Types   
 
 <details>
  <summary>Data Types </summary>
  
  <p>
   Primitive data type - int, float, string, boolean   
   
Python assumes the type of variables based on data types   

```python
amount=10
```
>Python infers that amount is an **int** since its a whole number

---

```python
amount=10.5
```
>Python infers that amount is an **float** since its a decimal number


## writing python programs

```python
tax=0.06
total= amount + amount*tax
print(total) # 10.6

amount=100
total= amount + amount*tax
print(total)  # 106.0
```

### Data Type conversion function   

convert a float to an int
>amount= int(10.6) # 10

convert int to a float   
>amount=float(10) # 10.0

concatenate string

```python
hello="hello"
name="sarah"
greeting= hello + name
print(greeting) # hellosarah
```

### python input function   

```python
my_name= input("what is your name \n")
print("input name is " + my_name) # input name is swat sinha
```


See below codes to understadnd type conversion:   
<details>
  <summary>Decade Calculator</summary>
  <p>
Take input from user and calculate how many decades old 
    
```python
age= input("how old are you \n")
decades= age/10  
```

>TypeError: unsupported operand type(s) for /: 'str' and 'int'


```python
age= int (input("how old are you \n")) # type 34
decades= age/10  
print("you are " + str(decades) + " decades old.") 
# output - you are 3.4 decades old.
```

>But we we want output like "3 decades and 4 years old" then we need quotient and remainder values

```python
user_age= int (input("how old are you \n")) # type 34
user_decades= user_age // 10
user_years=   user_age % 10
print("you are " + str(user_decades) + " decades and " + str(user_years) + " years old") 
# output - you are 3 decades and 4 years old
```

  </p>
</details>

  </p>
 </details>

---
 ## Chapter 03 - Conditionals and Import   
 
<details>
  <summary>Comparators</summary>
  <p>
   
   1. equal to   
      >print(temp == 95)  # True/False based on temp value   

  2. less than   
  >print(temp < 95)  # True/False based on temp value   

  3. less than equal to   
  >print(temp <= 95)  # True/False based on temp value   

4. greater than   
   >print(temp > 95)  # True/False based on temp value  

5. greater than equal to   
   >print(temp >= 95)  # True/False based on temp value   

6. not equal to   
   >print(temp != 95)  # True/False based on temp value   

  </p>
</details>

<details>
  <summary>if - elif - else</summary>
 
  <p>
   
   ```python
# if - elif - else

temperature=55
if temperature > 80 :
    print("Its too hot")
    print("Stay Inside")
elif temperature <60:
    print("Its too cold")
    print("Stay Inside")
else :
    print("Enjoy the outdoors")
# Output below: 
#Its too cold
#Stay Inside

```

  </p>
</details>


<details>
  <summary>Logical Operators</summary>
  <p>
   
   1. and   
   2. or   
   3. not   

   
   'and' , 'or' ->  combine multiple comparisons   
   'not' -> negate a comparison   

   ```python

# combile 'if' with 'or'    
temperature=85    
if temperature > 80 or temperature < 60:
    print("Stay Inside")
else :
    print("Enjoy the outdoors")
# Output : Stay Inside


# combine 'if' with 'and'    
temperature=75  
forcaset='pleasant'

if temperature < 80 and forcaset != 'rainy':
    print("Go Outside")
else :
    print("Stay Inside")
# Output : Go Outside

# not if
forcaset='rainy'
if not forcaset == 'rainy':
    print("Go Outside Inside")
else :
    print("Stay Inside")
# Output: Stay Inside

# not boolean
raining=True
if not raining:
    print("Go Outside")
else:
    print("Stay Inside")
# Output: Stay Inside

```
   
  </p>
  </details>

<details>
  <summary>Import Python Module</summary>
  <p>
   When we install python in computer we get :   

   - python interpreter: python's built-in functionality   

   - python standard library: we need something extra e.g math,datetime,random then we can import from this Python Standard Library   
  
   [Python Standard Library Link](https://docs.python.org/3/library/index.html "Python Standard Linrary")   


   ```python
import random

guess = int(input("Guess the dice roll : \n "))
print('user answered : ' + str(guess))

roll= random.randint(1,6) # function will return a random number between 1 and 6
print("the computer rolled a " + str(roll))

if guess== roll:
    print("Correct: you won !!!")
else:
    print("Wrong guess ... ")

```
  </p>
</details>

 ## Chapter 04 - Lists and Loops   
<details>
  <summary>initialize a list  </summary>
  <p>
    
 ```python
## LIST

# initialize list
acronyms=[]
print(acronyms) # []

acronyms=['LOL', 'IDK', 'SMH']
print( acronyms) # ['LOL', 'IDK', 'SMH']
```

  </p>
</details>

<details>
  <summary>append/remove/del --> add and remove item in list </summary>
  <p>
   
```python
acronyms.append('TBH') 
acronyms.append('BFN') 
print( acronyms) # ['LOL', 'IDK', 'SMH', 'TBH', 'BFN']

# remove ->  remove element by value
acronyms.remove("TBH")
print( acronyms) # ['LOL', 'IDK', 'SMH', 'BFN']

# del ->  remove element by index
del acronyms[2]
print( acronyms) # ['LOL', 'IDK', 'BFN']

# Error Cases
'''
acronyms.remove("ABC") # ValueError: list.remove(x): x not in list
del acronyms[3] # IndexError: list assignment index out of range
'''
```
  </p>
</details>

 <details>
  <summary> check if element exists in list</summary>
  <p>
   
   ```python
if 1 in [1,2,3,4,5]:
    print("true")
    
word= "TBH"
if word in acronyms:
    print(word + " is in the list")
else:
    print(word + " is not in the list")
   ```
  </p>
 </details>


 <details>
  <summary> in-built function sum </summary>
  <p>
   
 ```python
myexpenses = [1,2,3,4,5]
total= sum(myexpenses)
print("total expense is : " , total) # total expense is :  15
```

</p>
</details>


 <details>
  <summary> calculate sum using for loop and use of sep parameter in print </summary>
  <p>

```python

expenses= [10.50, 8, 5, 15, 20, 5, 3]
sum=0 # note: as a practice - we should npt keep variable name as some prefedined keyword
for x in expenses:
    sum= sum + x

print("you spent $" , sum)   # you spent $ 66.5 -> space after $ is added by default 

# sep parameter in print
print("you spent $" , sum, sep='') # you spent $66.5
print("you spent $" , sum, sep='---') # you spent $---66.5
```

</p>
</details>


 <details>
  <summary> loop with range </summary>
  <p>
   syntax for range is below   
   
   ```python

# range(num)  -> means 0 to num   
# range(7) means -> 0 to 6 : 0,1,2,3,4,5,6      

# range(start, stop, step)   
# range(0,7,1) --> 0,1,2,3,4,5,6   

# range(2,14,2) --> 2,4,6,8,10,12   
  

for i in range(2,14,2):
    print(i)

  ```
  
  we will now use range with for loop:
   
```python
total=0
expenses=[]

num_expenses = int(input("Enter number of expenses : "))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense :  \n")))

total= sum(expenses)
print("You spent $", total, sep='')
```

<details>
  <summary> Demo: Loan Calculator</summary>
  <p> 

```python
# get details of loan

money_owed= float(input("how much money do you owe in dollars ? \n")) # $50,000

apr= float(input("what is annual roi ? \n")) # 3%

payment= float(input("how much you will pay off each month in dollars ? \n")) # $1000

months= int(input("how many months do you want to see the results for ? \n")) # 54

monthly_rate= apr/100/12

for i in range(months):
    # calculate interest to pay
    interest_paid = money_owed * monthly_rate

    # add in interest
    money_owed= money_owed + interest_paid
    
    if(money_owed - payment <= 0):
        print("last payment is ", money_owed)
        print("you paid off the loan in ", i+1 , " months ")
        break
    
    # make payment
    money_owed= money_owed - payment

    print("Paid : ", payment, "of which ", interest_paid, " was the interest", end=' ')
    print("Now I owe ", money_owed)
```
</p>
</details>

</p>
</details>


 ## Chapter 05 - Dictionaries, JSON and Pip   

 <details>
    <summary> Dictionaries  </summary>
    <p>
     
   <details>
    <summary> Need for Dictionary </summary>
    <p>
    lets say we want to store a list of acronyms and their translations.   
    We can use 2 lists as below :   
  
   ```python
       acronyms=['LOL', 'IDK' , 'TBH']
       translations=['laugh out loud', 'i dont know', 'to be honest']
   ```

But the problem here is if we add to one list then we need to add to other.      
Similarly, if we remove an item from one list we need to remove from other list as well.   


To solve this we can use ***Dictionary***   

A Dictionary maps key to value. Here the acronym can be key and translation can be value.   
To look up a value in dictionary we need to send key(instead of index)   


```python

acronyms= { 'LOL': 'laugh out loud', 'IDK': "i don't know", 'TBH': 'to be honest'}
print(acronyms['LOL']) # laugh out loud

```

## Dictionary like list can hold anything   

```python

menu= {'Soup' : 5, 'Salad': 6} # valid
print("menu is : " , menu)

my_dict= {10: 'hello', 2: 6.5} # valid
print("my_dict is : " , my_dict)

randon_dict= {10: 'hello', 'name': 6.5, 4.2: 'got it'} # valid
print("randon_dict is : " , randon_dict) # {10: 'hello', 'name': 6.5, 4.2: 'got it'}
print(randon_dict[10]) # hello
print(randon_dict['name']) # 6.5
print(randon_dict[4.2]) # got it
```

  </p>
</details>
    
 
 <details>
        <summary> CRUD in Dictionary </summary>
        <p>
         #### Create Dictionary   
   
We can initialize an empty dictionary and then add key/value to it   

```python

acronyms={}
acronyms['LOL'] = 'laugh out loud'
acronyms['IDK'] = "i don't know"
acronyms['TBH'] = 'to be honest'
print(acronyms) # acronyms  {'LOL': 'laugh out loud', 'IDK': "i don't know", 'TBH': 'to be honest'}
```

#### Updating value in Dictionary

```python
acronyms={}
acronyms['LOL'] = 'laugh out loud'
acronyms['IDK'] = "i don't know"
acronyms['TBH'] = 'to be honest'

print(acronyms['TBH'])  # to be honest

acronyms['TBH']= 'honestly'
print(acronyms['TBH']) # honestly
```



#### delete value in Dictionary   

To delete a value - use del with key   
 
```python
acronyms={}
acronyms['LOL'] = 'laugh out loud'
acronyms['IDK'] = "i don't know"
acronyms['TBH'] = 'to be honest'
print("acronyms : ", acronyms)
del acronyms['IDK']
print("acronyms : ", acronyms)
```

if we use del for a key not present   

```python
# del acronyms['ABC'] # KeyError
```

To avoid this we should use get   

```python
acronyms= { 'LOL': 'laugh out loud', 'IDK': "i don't know", 'TBH': 'to be honest'}
definition= acronyms.get('ABC')
print(definition) # if key is not there it will return None type (None - absence of a value)

if definition:
    del acronyms['ABC'] 
else:
    print("key does not exist")
```

 </p>
 </details>



Below is sample code using dictionary for movie schedule   

<details>
  <summary> Movie Schedule </summary>
  <p> 

```python

current_movies= {
    'The Grinch': '11:00 AM',
    'Rudolph': '1:00 PM',
    'Frosty the Snowman': '3:00 PM',
    'Christmas Vacation': '5:00 PM'
}

print("We are showing the following movies: ")
for key in current_movies:
    print(key)

movie= input("what movie would you like the show time for?  \n ")
showtime= current_movies.get(movie)

if showtime == None:
    print("Requested movie is not playing")
else:
    print(movie, " is playing at : ", showtime) 
```
</p>
</details>

<details>
  <summary> Combining Lists and Dictionaries </summary>
  
 <p> 
 We saw how to use Dictionaries, lets see more complex situations where we need to combine lists with dictionaries   
 
Lets say we have three different menu lists- breakfast, lunch and dinner   
```python

breakfast=["corn flakes", "idly" , "noodles"]   
lunch= ["rice meal", "roti meal", "dosa"]   
dinner= ["curd rice", "oats" , "milk"]

# now to combime these into one list we can use :

menus= [
       ["corn flakes", "idly" , "noodles"],
       ["rice meal", "roti meal", "fruits"], 
       ["curd rice", "oats" , "milk"]]
       
print("Breakfast Menu \t ", menus[0]) # ['corn flakes', 'idly', 'noodles']
print("Lunch Menu \t ", menus[1]) # ['rice meal', 'roti meal', 'fruits']
print("Dinner Menu \t ", menus[2]) # ['curd rice', 'oats', 'milk']

# To get individual item from inner list
print("Breakfast Menu second item \t ", menus[0][1]) # idly

```
Instead of using list of lists as above, we canm also use dictionary   

```python
menus =  {
          'breakfast' : ["corn flakes", "idly" , "noodles"],
          'lunch': ["rice meal", "roti meal", "fruits"], 
          'dinner' : ["curd rice", "oats" , "milk"]
         };
print("Breakfast Menu \t ", menus['breakfast']) # ['corn flakes', 'idly', 'noodles']
print("Lunch Menu \t ", menus['lunch']) # ['rice meal', 'roti meal', 'fruits']
print("Dinner Menu \t ", menus['dinner']) # ['curd rice', 'oats', 'milk']
```

the above code works well but what if we have many more menus- we may need to type each key then   
lets try using for loop instead   
Note: By default for loop in dictionary returns key which won'y help us as we want values   
so we will use items method

```python
menus =  {
          'breakfast' : ["corn flakes", "idly" , "noodles"],
          'lunch': ["rice meal", "roti meal", "fruits"], 
          'dinner' : ["curd rice", "oats" , "milk"]
         };

for menuName,menuValue in menus.items():
    print (menuName , ':' ,  menuValue)

```

We can also use dictionary to represent object   

```python
person= {
    'name': 'Sarah Smith',
    'city': 'Orlando',
    'age': 100
}
print(person.get('name') , "is " , person.get('age') , "years old ") # Sarah Smith is  100 years old 
```


<details>
  <summary> Print all emails </summary>
  
 <p> 
  
```python
contacts= {
    'number': 4,
    'students': [
        {'name': 'Sarah Holderness', 'email': "sarah@example.com" },
        {'name': 'Harry Potter ', 'email': "harry@example.com" },
        {'name': 'Ron Weasley', 'email': "ron@example.com" }
    ]
}

print("Student Emails \n")
for student in contacts['students']:
    print(student['email'])
```
 
 </p>
 </details>

 </p>
</details>


</p>
</details>

 <details>
  <summary> JSON and PIP </summary>
  <p> 

we will now see requesting data from internet using **request** package and we will see how to install this package using **pip**   

## HTTP request in python   
The ***request*** library let us do HTTP request   

***pip*** - used to install any package from python package index   

### to check if pip is installed 
> pip3 --version

### install the required package by 
> pip3 install requests   


We will make request to api - **http://api.open-notify.org/astros.json**   
It would return json response in format:   

```javascript
{
  "message": "success",
  "number": NUMBER_OF_PEOPLE_IN_SPACE,
  "people": [
    {"name": NAME, "craft": SPACECRAFT_NAME},
    ...
  ]
}
```

We will now write code in python for ***people currently in space***   

```python
import requests

response= requests.get('http://api.open-notify.org/astros.json')
json= response.json()


print("The people currently in space are: \n")

for person in json['people']:
    print(person['name'])

```

<details>
 <summary>Creating Python Virtual Environment</summary>
 <p>
  The command we gave earlier:   
  
  > pip3 install requests

installed requests package globally   
But in case one project need version A and other project version B then it will cause problem.   
For this we need ***Python Virtual Environment***   

Details: https://docs.python.org/3/library/venv.html   

Lets create it   

1. uninstall existing requests package(so that we can show request package in new virtual environment)      
> pip3 uninstall requests   

2. create virtual environment with name say ***venv***
> python3 -m venv venv   

this will create directory venv   
and inside this venv there would be bin folder ***activate*** script and version of ***python*** and ***pip***   

<img width="1119" alt="image" src="https://github.com/user-attachments/assets/da69f6c9-19d4-40b6-9113-b887b1e9e58a" />




4. To use package inside this virtual environment(venv), we need to activate it   
source dir_name/bin/activate

> source venv/bin/activate   

Once activated we can see the name in parenthesis (highlighted in red below) which indicated its activated      
<img width="1119" alt="image" src="https://github.com/user-attachments/assets/c7e394dd-d603-4642-b0d4-13fc34246931" />

5. now if we give command to install ***requests*** it will install locally inside the virtual environment   

> pip3 install requests

6. Now to use it VS code does know to run python with our new virtual environment.   
It do prompt us to select the venv when we create it but in case it does not prompt we can select manually by   

View --> Command Palette --> type ***search interpreter*** --> scroll and select python version and venv (see below)
<img width="1064" alt="image" src="https://github.com/user-attachments/assets/36eb86b5-ad43-4b62-902d-cd52c1fd034f" />

now if we open the file and run play button it will execute the program and show output in terminal
 
7. To deactivate virtual environment we just need to type   

> deactivate

<details>
 <summary>Weather API using key</summary>
 <p>
  We will use weather api
go to https://www.weatherapi.com/  -> click on pricing   -> free   --> signup --> verify email --> login   
we will be able to see API key -> copy and save it (1385a520dfdb4dfeb0f192814250203)   

now go to home page(click on home icon) -> then go to API Explorer
https://www.weatherapi.com/api-explorer.aspx   
and paste key
<img width="1515" alt="image" src="https://github.com/user-attachments/assets/17e1e7db-13f8-4762-bc23-44e4dad171a4" />

If we now click on show response, it will create utl to be used in code   
and also complete data in response   
<img width="666" alt="image" src="https://github.com/user-attachments/assets/703a4cc6-1538-4c55-8462-6e9a3402e67b" />

We will write code to use url highlighted above and also extract highligted data from the complete response   

```python

import requests

city= "London"
url = "http://api.weatherapi.com/v1/current.json?key=1385a520dfdb4dfeb0f192814250203&q=" + city + "&aqi=no"
response= requests.get(url)
weather_json= response.json()

'''the below line is also working 
print(weather_json['current']['temp_f']) # working
'''

temp = weather_json.get('current').get('temp_f')
print(temp) # 39.4

description = weather_json.get('current').get('condition').get('text')
print(description) # clear

print("Today's weather in " + city + " is " + description + " and temperature is " + str(temp) + " degrees ")

```


 </p>
</details>

 </p>
</details>

   
</p>

</details>


 ## Chapter 06 - Functions   

 sample python functions

  <details>
  <summary>greeting</summary>
  <p>

```python
def greeting(name):
    print("Hello " + name)

input_name= input("Enter your name \n")
greeting(input_name)
```

***Local scope*** : variable created inside a function and can only be used inside that function. Here name is location variable inside function greeting   

  </p>
  </details>





 <details>
  <summary>addition</summary>
  <p>
   
   ```python
   def addition(a,b):
    return a + b

num1= float(input("Enter your first number \n"))
num2= float(input("Enter your second number \n"))
result= addition(num1, num2)
print("result of addition is : ", result)

```



***Note***: We can use function to organize code as well . 
So the other way to write code for above function is :   


```python

def addition(a,b):
    return a+b

def main():
    num1= float(input("Enter your first number \n"))
    num2= float(input("Enter your second number \n"))
    result= addition(num1 , num2)
    print("result of addition is : ", result)
    
main()

```
</p>
</details>

 
 <details>
  <summary>Dice Rolling Game</summary>
  <p>
   
   Basic dice game where two users will roll a pair of dice to see who wins   

  ```python

import random

def roll_dice():
    dice_total= random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1= input("Enter Player 1 name \n")
    player2= input("Enter Player 2 name \n")
    roll1= roll_dice()
    roll2= roll_dice()
    print(player1 , "rolled : ", roll1)
    print(player2 , "rolled : ", roll2)
    
    if(roll1 > roll2):
        print(player1 , "wins")
    elif(roll2 > roll1):
        print(player2 , "wins")
    else:
        print("its a tie")

main()

  ```
  </p>
 </details>

  ## Chapter 07 - Classes and Objects   
  
<details>
  <summary>Sample Program: </summary>
 
```python

class Robot_Dog:
    def __init__(self, name, breed):
        self.name= name
        self.breed= breed
        
    def bark(self):
        print("Woof Woof !!!")

# Main Program
my_dog= Robot_Dog('Spot', 'Chihuaha')
print(my_dog.name)
print(my_dog.breed)
my_dog.bark() 


'''
Output is:
Spot
Chihuaha
Woof Woof !!!
'''
```

</details>


<details>
 <summary>Price Formatting</summary>   

 This price formatting will be useful in below Company Payroll demo   

 
 ```python
print('hello','world') # hello world
print('hello', 'world', sep='') # helloworld
print('----------------')

salary= 50000
paycheck= salary/52
print('paycheck ', paycheck) # paycheck  961.5384615384615

# rounding `n` to 2 decimal places
paycheckRoundOff = round(paycheck, 2) 

print('paycheckRoundOff : ', paycheckRoundOff)  # paycheckRoundOff:  961.54
print('paycheckRoundOff with dollar : $',paycheckRoundOff)  # paycheckRoundOff with dollar :$ 961.54 (note: there is space after dollar)
print('paycheck with dollar formatted: ', '$',paycheckRoundOff, sep='') # paycheck with dollar formatted:$961.54


print('----------------')

print('Alternative method is below : ')
formatted_price = f"${paycheckRoundOff:.2f}"
print('formatted_price :' , formatted_price)

print(f'Pay Check:  ${paycheck:,.2f}')
 ```

</details>



<details>
 <summary>Demo : Company Payroll </summary>

employee.py   
```python

class Employee:
    def __init__(self, fname, lname, salary):
        self.fname= fname
        self.lname= lname
        self.salary= salary
    
    def calculate_paycheck(self):
        return self.salary/52
```

company.py   


```python
from employee import Employee

class Company:
    def __init__(self):
        self.employees=[]
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        print('Current Employees are: ')
        for i in self.employees:
            print(i.fname, i.lname)
        print('----------------')
    
    def pay_employees(self):
        print('Paying Employees : ')
        for i in self.employees:
            print('Paycheck for : ', i.fname , i.lname)
            print(f'Amount:  ${i.calculate_paycheck():,.2f}')
            print('---------------------')
            
        
        

def main():
    my_company= Company()
    employee1= Employee('Sarah', 'Hess', 50000)
    my_company.add_employee(employee1)
    employee2= Employee('Lee', 'Smith', 25000)
    my_company.add_employee(employee2)
    employee3= Employee('Bob', 'Brown', 60000)
    my_company.add_employee(employee3)
    
    # print(my_company.employees)
    '''
    Output: [<employee.Employee object at 0x100acea50>, <employee.Employee object at 0x100c10a50>, <employee.Employee object at 0x100c10b90>]
    '''
    
    my_company.display_employees()
    
    my_company.pay_employees()
    
    

main()



```
Outout is below:   
 
<img width="282" alt="image" src="https://github.com/user-attachments/assets/0d8623a2-4d85-4049-81be-67fde238c2cd" />


</details>

<details>
 <summary>Inheritance</summary>
 <p>
  Relationships in Object Oriented Programming   

1.  has a relationship:   
  - A company has employees   
  - A robot has a battery   

2. is a relationship:   
  - A robot dog is a robot
  - A robot cats is a robot   

Note: is-a-relationship is also called **inheritance**   

<details>
 <summary>Inheritance Demo</summary>
 <p>
  
```python
class Robot:
    def __init__(self, name):
        self.name= name
        self.position=[0,0]
        print("My name is : ", self.name)
    
    def walk(self,x):
        self.position[0]=self.position[0] + x
        print("New position: ", self.position)
    
    def eat(self):
        print("I am hungry !!")
        
class Robot_Dog(Robot):  # inheriting parent class
    def make_noise(self):
        print("Woof Woof !!!")
    
    def eat(self):    # Method Overiding
        super().eat() # calling parent class eat() method
        print("I like Bacon!!!")
        
my_robot_dog= Robot_Dog('Bud') 
my_robot_dog.walk(20)
my_robot_dog.make_noise() 
my_robot_dog.eat()

```
   

Output:   

<img width="568" alt="image" src="https://github.com/user-attachments/assets/95e5f585-5352-4d82-beca-d61d8326c11e" />   


 </p>
</details>

Benefits of Inheritance:   
1. lets us model real world relationships   
2. let is reuse code   

<details>
 <summary>Company Payroll With Inheritance</summary>
 <p>
 Now we are going to use inheritance to add different types of Employee class   

Unlike in Company Payroll demo above, the company not only has employees that earn a salary but also hourly and commission employee   
   
So lets create a general Employee class for below three three types of employee to inherit from   
   
1. SalariedEmployee   
2. HourlyEmployee   
3. CommissionEmployee   

***employee.py***   

```python
class Employee:
    def __init__(self, fname, lname):
        self.fname= fname
        self.lname= lname
 
    


class SalariedEmployee(Employee):
    def __init__(self,fname, lname, salary):
        super().__init__(fname, lname)
        self.salary= salary
    
    def calculate_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self,fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours= weekly_hours
        self.hourly_rate= hourly_rate
    
    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate

class CommissionEmployee(SalariedEmployee):
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate
    
    def calculate_paycheck(self):
        regular_salary= super().calculate_paycheck()
        total_commission= self.sales_num * self.com_rate
        return regular_salary + total_commission

```

***company.py***      

```python
from employee import SalariedEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees=[]
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        print('Current Employees are: ')
        for i in self.employees:
            print(i.fname, i.lname)
        print('----------------')

    def pay_employees(self):
        print('Paying Employees : ')
        for i in self.employees:
            print('Paycheck for : ', i.fname , i.lname)
            print(f'Amount:  ${i.calculate_paycheck():,.2f}')
            print('---------------------')
            
  
def main():
    my_company= Company()
    employee1= SalariedEmployee('Sarah', 'Hess', 50000)
    my_company.add_employee(employee1)
    
    employee2= HourlyEmployee('Lee', 'Smith', 25, 50)
    my_company.add_employee(employee2)
    
    employee3= CommissionEmployee('Bob', 'Brown', 30000, 5, 200)
    my_company.add_employee(employee3)
    
    my_company.display_employees()
    my_company.pay_employees()
    

main()


```
  
Outout is below:   

<img width="502" alt="image" src="https://github.com/user-attachments/assets/55a3fbde-6896-4631-add0-c4c2da89a6c4" />


 </p>
</details>


 </p>
</details>


## Chapter 08 - Working With Files   
  

<details>
  <summary>Exceptions </summary>
  <p>
 
**Without Exception**   

```python
acronyms= {
    'LOL' : 'laugh out loud',
    'IDK': "I dont't know",
    'TBH': "To Be Honest"
    }
acronym = 'TBH'

definition = acronyms[acronym]
print('Definition of ', acronym , ' is ' , definition)
print('The program keeps going on ...') 
```
Output:   

![image](https://github.com/user-attachments/assets/b80ef799-b4bb-407b-b25f-7843e76a2995)



**With Exception**

```python
acronyms= {
    'LOL' : 'laugh out loud',
    'IDK': "I dont't know",
    'TBH': "To Be Honest"
    }
acronym = 'BTW'

definition = acronyms[acronym]
print('Definition of ', acronym , ' is ' , definition)
print('The program keeps going on ...') 
```

Output:   
![image](https://github.com/user-attachments/assets/f48cd619-4d24-4f1c-8362-185f98591968)



To Handle this we use try/except   
 <img width="599" alt="image" src="https://github.com/user-attachments/assets/b78b7817-5e99-4c02-ab5d-1cfeb7773c10" />

```python
acronyms= {
    'LOL' : 'laugh out loud',
    'IDK': "I dont't know",
    'TBH': "To Be Honest"
    }
acronym = 'BTW'

try:
    definition = acronyms[acronym]
    print('Definition of ', acronyms , ' is ' , definition)
except:
    print('The acronym ', acronym, 'does not exist')

print('The program keeps going on ...')
```

Output:   
![image](https://github.com/user-attachments/assets/fa15d819-826a-45ff-ae5a-a5314e8c812e)

**finally** - to execute code after try/except block.
The code in *finally* block will execute whether there is error or not  

<details>
 <summary>raising exception</summary>
 As a python developer we can raise/throw an exception if a certain condition occurs   
e.g: In the above example where BTW does not exist we decided to raise KeyError exception   

<details>
 <summary>raise pre-defined exception</summary>

 ```python
 def remainder_division(a,b):
    if b == 0:
        raise ZeroDivisionError
    
    result= a//b
    remainder= a%b
    print(a, "/" , b , "is ", result, " and remainder is : ", remainder)
    
# Main Program
remainder_division(10,0)
 ```
Output:   
![image](https://github.com/user-attachments/assets/04c31c5a-ab7f-4e58-b7c0-99c298d9d868)

</details>

<details>
 <summary>raise custom exception</summary>
 
 ```python
 
 def remainder_division(a,b):
    if b == 0:
        raise Exception("Divisor cannot be zero")
    
    result= a//b
    remainder= a%b
    print(a, "/" , b , "is ", result, " and remainder is : ", remainder)
    
# Main Program
remainder_division(10,0)
 ```
Output:   
![image](https://github.com/user-attachments/assets/8559b7b4-334a-4773-9185-2138b08dc726)

</details>
</details>



 </p>
</details>



  <details>
  <summary>Reading Files </summary>
    <p>   

  **Task** :  Finding acronym in a text file   
 
1. Ask user what acronym they are looking for   
2. Open the file   
3. Loop and read each line of file   
4. Check if current acronym matches with what the user is looking for   
5. print the definition

Lets say we have file acronyms.txt
```javascript
'LOL' - 'laugh out loud',
'IDK' -  "I dont't know",
'TBH' -  "To Be Honest"
```

**Ways to read a file**

   <details>
    <summary>read method</summary>
    <p>
*read* method returns the whole file as a string by default or it will return the specificed number of bytes   

     
   ```python
    
    file=open('acronyms.txt')
    try:
     # file operations
     result= file.read()
     print(result)
    finally: 
     file.close()
   ```
   

   Output:   
![image](https://github.com/user-attachments/assets/85533195-6286-4a04-8d56-0a44810f69b6)

 </p>
   </details>

<details>
    <summary>readline method</summary>
 <p>
  *readline* method returns the next line of the file as a string

  ```python
file=open('acronyms.txt')
try:
    # file operations
    result= file.readline()
    print(result)
finally: 
    file.close()
```
Output:   
![image](https://github.com/user-attachments/assets/63628eda-2145-4f47-80ec-7608e0e1f029)

 </p>
</details>


<details>
    <summary>readlines method</summary>
    <p>
    *readlines* returns the list of strings of all of the lines in the file
     
   ```python
     file=open('acronyms.txt')
     try:
      # file operations
      result= file.readlines()
      print(result)
    finally: 
      file.close()
   ```

    Output:    
![image](https://github.com/user-attachments/assets/f03c7c19-51f1-4b82-950a-23c83cee8476)

Since it returns a list ee can loop over and print each line   

```python
file=open('acronyms.txt')
try:
    # file operations
    result= file.readlines()
    # print(result)
    for line in result:
        print(line)
    
finally: 
    file.close()
```
Output:   
![image](https://github.com/user-attachments/assets/41053aa5-454f-44b8-b4cf-6ad5f11aa10d)

This type of loop for reading file is used so often hence there is shortcut 
```python
file=open('acronyms.txt')
try:
    # file operations
    #result= file.readlines()
    for line in file:
        print(line)
    
finally: 
    file.close()
```
Output:   
![image](https://github.com/user-attachments/assets/7b2a5c77-9df1-43cc-b640-abfe4ecd19dd)
   </p>
</details>

<details>
 <summary>find acronym in file</summary>
 <p>
  
  ```python
  look_up= input("what acronym would you like to look up \n")
found= False

with open('acronyms.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            fount=True
            break

if not found:
    print('acronym doesnot exist in file')
 ```
Output:   

![image](https://github.com/user-attachments/assets/bff1665f-f425-4ac4-b7f2-57881805af58)

 </p>
</details>

 </p>
</details>

<details>
  <summary>Write File </summary>
Say we have file acronyms.txt with below contents:   
 
```javascript
 BY - Bye World
GA - Good Afternoon
 ```
 
 <p>
  1. Ask user what acronym they want to add   
  2. ask user for the definition   
  3. open the file   
  4. write new acronym and its definition to the file   

```python
acronym= input("what acronym do you want to add ? \n")
definition= input("what acronym do you want to add for above acronym \n") 

# with open('acronyms.txt', 'w') as file:
'''
w is for write mode but it deletes all previous content and then writes freshly
to apend new text at end we will use append - 'a' as below : 
'''
with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')
```
Output:   
![image](https://github.com/user-attachments/assets/8d3cf964-31cb-4feb-a4d8-e36e63d128a9)

Now acronyms.txt is changed to :   
```javascript
BY - Bye World
GA - Good Afternoon
GN - good night
```
 </p>
**Note**: With write or append mode if file does not exist it will create new file with it
However with read mode if file does not exist it will throw error

</details>

<details>
  <summary>Read and Write In File </summary>
  <p>

 ```python
def find_acronym():
    look_up= input("what acronym would you like to look up \n")
    found= False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found=True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return
        

    if not found:
        print('acronym doesnot exist in file')

def add_acronym():
    acronym= input("what acronym do you want to add ? \n")
    definition= input("what definition do you want to add for above acronym \n") 

    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    choice= input("Do you want to find(F) or add(A) an acronym? \n")
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()   
 ```
   
  </p>
  
 </p>
</details>

<details>
  <summary>File Manipulation </summary>
 
 <p>
Python has some built-in modules for handling files.   
  
 </p>
 </details>

 













    



