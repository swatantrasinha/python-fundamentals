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
   Primitive data type - int,float,string   
   
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
   








## web requests

## installing and using packages

