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
<details>

chapter 05 is done

</p>
</details>
 
    

## web requests

## installing and using packages

