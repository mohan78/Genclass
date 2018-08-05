# Genclass
A python module for generating class code with out the need to type the boring and repeating lines. Just give the class name and its fields to generate the block of class code right in that file.

## Installation
>pip install Genclass

Usage instruction in the pdf attached.

## Initializing Genclass object
```sh
from Genclass import genclass

obj = genclass.Class_generator(filename) 
```
#'filename' is the filename of the python file in which you want to create class code

for example: Let the filename be test.py. Then the initialization would be:

>obj = genclass.Class_generator(‘test’)

## Methods
### GenerateClass
>GenerateClass(class name,[list of fields],'yes' for creating __str__ (optional),[list of fields for __str__] (optional))
  
  Generates the ‘class’ code in the given file.
  
  Example:
  ```sh
  obj.GenerateClass('Person',['fname','lname','gender','dob'],'yes',['fname','lname'])
  ```
  
  The above code will generate the following code in the test.py file:
  ```sh
  
  class Person:
    
    def __init__(self,fname,lname,gender,dob):
      self.fname = fname
      self.lname = lname
      self.gender = gender
      self.dob = dob
      
    def __str__(self):
      return self.fname + self.lname

  ```
### InheritClass
>InheritClass(Parent class object name without quotes,new class name,[list of fields])
  
  Generates the inherited ‘class’ code in the given file. Caution: Give the parent class name without quotes.
  
  Example:
  ```sh
  obj.InheritClass(Person,’Employee’,[‘emp_id’,’dept’])
  ```
  
  The above code will generate the following code in the test.py fiel:
  ```sh
  class Employee(Person):
    
    def __init__(self,fname,lname,gender,dob,emp_id,dept):
      self.emp_id = emp_id
      self.dept = dept
      Person.__init__(self,fname,lname,gender,dob)
  ```
### tell_params
>tell_params(class object name without quotes)
  
  Retunrs the list of arguments of the supplied class as single string comma seperated argument names.
  
  Example:
  ```sh
  params = obj.tell_params(Person)
  print(params)
  ```
  >Output: fname,lname,gender,dob


```
Thanks,
Mohan Chand Peddapuli
Contact me at: mohanroger63@gmail.com
```
