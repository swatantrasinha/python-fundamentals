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
    



