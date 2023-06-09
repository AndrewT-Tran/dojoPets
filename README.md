

Assignment: Dojo Pets
=====================

Objectives
----------

*   More practice with OOP and class association.

* * *

Ninja Class
-----------

**Attributes**

*   first\_name
*   last\_name
*   pet
*   treats
*   pet\_food

**Methods**

*   walk()
*   feed()
*   bathe()
```
class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
        	
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method

```
Pet Class
---------

**Attributes**

*   name
*   type
*   tricks
*   health
*   energy

**Methods**

*   sleep()
*   eat()
*   play()
*   noise()
```
class Pet:
    # implement __init__( name , type , tricks ):
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound

```
![image](https://github.com/AndrewT-Tran/dojoPets/assets/112746783/adb55296-72f0-434f-9a41-d6844ff1c173)

*   Create a Ninja class with the ninja attributes listed above.
    
*   Create a Pet class with the pet attributes listed above.
    
*   Implement walk(), feed(), bathe() on the ninja class.
    
*   Implement sleep(), eat(), play(), noise() methods on the pet class.
    
*   Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
    
*   Have the Ninja feed, walk , and bathe their pet.
    
*   NINJA BONUS: Use modules to separate out the classes into different files.
    
*   SENSEI BONUS: Use Inheritance to create sub classes of pets.
    
*   Compress or zip up assignment and upload it.
