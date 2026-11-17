Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information

# Python Syntax Notes

    # Operands `The value or variable to be operated on. e.g. 3, peach`
    # Operators `The function performing the work, such as mathematical`

# Step-by-step execution debug: https://pythontutor.com/index.html

#### Variables ####

    # 'Assignment Statements' '<variable> = <expression>' e.g. side = 3

#### Arithmetic ####
    
    ## Expressions

    # Addition `+`
    # Subtraction `-`
    # Multiplication `*`
    # Division `/`
    # Exponentiation `**`
    # Variable assignment `=`


    # Integer Division/Floor Division/Round Down Division `y // x` `How many times does x go into y without creating decimal`
        # e.g. 5 // 3 = 1
    # Integer Remainder `y % x` `Remainder as result of x into y instead of creating decimal`
        # e.g. 5 % 3 = 2
    ## Booleans

    # Equality `==` `Produces True or False, like saying is equal to`
    # `True` ->(implies) `1`
    # `False` ->(implies) `0`
    # Is less than `<` 
    # Is greater than `>` `>=`
    # Not equal to `!=`

    # `not, and, or` `Used to connect Boolean expressions`

#### Arith Functions ####

    # `input()` `Reads a string from an input, no matter the input!`
    # `range(start, stop, step)` `Returns a range from start up to, but not including stop`
    # `eval()` `Evaluates a numeric string and returns it as a numeric data type`
    
    from math import *

    # Minimum `min()`
    # Maximum `max()`
    # Absolute value `abs()`
    # Round `round()`

    # Convert decimal to binary `bin('n')`
    # Convert n (number) to binary `'{:b}'.format(n)`
    # Convert n (number) to octal `'{:o}'.format(n)`
    # Convert n (number) to hexadecimal `'{:x}'.format(n)`

    # Round up `ceil()`
    # Round down `floor()`
    # Square root `sqrt()`

    # pi `pi`
    # e (Euler's constant) `e`
    # Logarithm (Logarithm of base b) `log(a,b)`
    # Exponential (base e) `exp()`

    from random import randrange

    # Random Within Int Range `randrange(n)` `Integer between at least 0 and less than n`
    # Random Within Int Range Expanded `randrange(n,x,y)` `n = start, x = stop, y = increment`

#### Logic ####

    # Logical constants `True` `False`
    # Logical operators `not` `and` `or`

#### Integers ####

    ## Integer Presentation Types

    # `{:b}.format(n)` `Outputs number n in binary
    # `{:c}.format(n)` `Outputs number n in Unicode
    # `{:d}.format(n)` `Outputs number n in decimal notation
    # `{:o}.format(n)` `Outputs number n in base 8`
    # `{:x}.format(n)` `lowercase x` `Outputs number n in base 16, lowercase letters for digits above 9`
    # `{:X}.format(n)` `uppercase X` `Outputs number n in base 16, uppercase letters for digits above 9`

#### Strings ####

    # Words(Sequences of characters) ####

    # `''` or `""` or `'''_'''` to denote
    # `\n` `Newline`
    # Concatenation `+` `A series of things linked together like links in a chain`
    # Equality `==`
    # ABC..aa..zz.. - starting at 0 and increasing as rightward
    # `input()` `Reads a string from an input, no matter the input!`
    # `range(start, stop, step)` `Returns a range from start up to, but not including stop`
    # `eval()` `Evaluates a numeric string and returns it as a numeric data type`

    # `s[start:up to:step]` `Slicing, starting at index 'start' up to 'up to'` `step, increment size, defaults to one`
    
    ## String Operators
    # `ele in s` `Returns True if string ele is a SUBSTRING of string s, False otherwise`
    # `ele not in s` `Returns False if string ele is a SUBSTRING of string s, True otherwise`
    # `s + t` `Concatenation of string s and string t`
    # `s * n` = `n * s` `Concatenation of n copies of s`
    # `s[i]` `Character at index <i> of string <s>`
    # `len(s)` `Length of string s`
    # 's[::-1]' 'Returns a given string in reverse order'

    ## String Methods
    # `s.capitalize()` `A COPY of string s with the first letter capitalized, if the letter is alphabetic`
    # `s.count(target)` `Returns the number of occurences of substring target in string s`
    # `s.lower()` `Returns a copy of string s converted to lowercase`
    # `s.replace("old","new")` `Returns a copy of string s which every occurence of substring old, is replaced by substring new`
    # `s.split(sep) `Returns a list of substrings of s, separations are marked by substring sep, default is empty space, can`t split a single word into characters - works better on sentences`
    # `s.strip()` `Returns a copy of string s with leading and trailing blank spaces removed`
    # `s.upper()` `Returns a copy of string s converted to uppercase`
    # `s.format(a,b,c)` ``Returns a string with empty {} filled by method parameters, in order. e.g. a then b then c {}{}{}`


    # `s.find(target) `The index of the FIRST OCCURENCE of substring target in string s`

#### Lists ####

    # `help(list)` `All list documentation`
    
    ### List Mutation

        ## List operators and functions

            #  `list[i] = value` `Sets element at index i to value`
            # `object in list` `Returns True if object is in list, false otherwise`
            # `x not in list` `False if object is in list, true otherwise`
            # `listA + listB` `Concatenation of lists listA and listB`
            # `list[i]` `Item at index i of list`
            # `len(list)` `non-zero-based length of list`
            # `min(list)` `Returns smallest item in list`
            # `max(list)` `Returns largest item`
            # `sum(list)` `Sum of elements in list` 
            # `list * n` = `n * list` `Concatenation of n copies of list`
            # `list[::-1]` `Returns a list in reverse order of list`

        ## List Methods

            # `list.append(element)` `adds element to the END of list`
            # `list.count(element)` `RETURNS the number of occurences of element in list`
            # `list.index(element)` `RETURNS the index of the FIRST OCCURENCE of element in list`
            # `list.insert(index, element)` `Inserts element before targeting index`
            # `list.pop()` `Removes and returns LAST element in the list`
            # `list.remove(element)` `Removes the FIRST OCCURENCE of element in the list`
            # `list.reverse()` `Reverses the order of elements in the list`
            # `list.sort()` `Sorts the list` 

#### Tuples ####
    # behave like lists in many ways except immutable, and uses parentheses () instead of brackets []

#### If/elif/else ####

    # Elif: Exactly one of the code blocks (if, elif*n, else) will execute
    # meaning the order matters

#### Execution Control Structures ####

    # Decision Control

        # `if` statements

            # One-Way Decision
                # if <condition>: 
                    # <indented code block>
                # <non-indented block>

            # Two-Way Decision
                # if <condition>:
                    # <indented code block 1>
                # else:
                    # <indented code block 2>
                # <non-indented code block>

            # Multi-Way Decision
                # the FIRST condition that evaluates True will execute; order matters

                # if <condition 1>:
                    # <indented code block 1>
                # elif <condition 2>:
                    # <indented code block 2>
                # elif <condition 3>:
                    # <indented code block 3>
                # else:
                    # <indented code block last>
                # <non-indented code block>

    # Iterative Control
        # `Basic For Loop`

            # for <variable> in <sequence>:
                # <indented code block>
            # <non-indented statement>

        # Iteration Loop
            # Iterating through an explicit sequence of values and performing an action on each value

        # Counter Loop - Indexed Iteration
            # Iterating over a sequence of integers specified by range
                # for <i> in <range()>
                    # print(i)

            # Iterating over a sequence by index instead of value
                # for <i> in <range(len(<sequence>))>:
                    # print(<sequence>[<i>])

                # Range only evaluates integers, which some sequences aren't
                # Adding <len()> gives a integer count of the sequence
                # <range(len())> Together these create zero-based index, each <variable> in <sequence> has it's own index
                # You can then use this <i> for <sequence>[<i>], since it's the exact length of the sequence

                # When comparing indexes, may have to start at offset: len(range(1,_)) or len(range(_-1)) or len(range(1,_,-1))

        # Accumulator Loop
            # <accumulator> = <empty sequence>
                # for <i> in <sequence>:
                    # <code block>
                    # <accumulator> = <accumulator> + <i>

        # Nested Loop
            # for <i> in <sequence1>: 
                # for <j> in <sequence2>: 
            # kind of turns <sequence1> into a counter
            # for each individual item in <sequence1>, iterate through <sequence2>
            # iterates through <sequence2> entirely for each item in <sequence1>

            # def f(x,y): >>> f('str','fs')
            #   for i in x:
            #       for j in y:
            #           print(j)
            
            # iterates through y entirely for each item in x
            # so it would iterate through u three times because len(x) is 3 

        # While Loop
            # while <condition>:
                # <indented code block> (executed as long as condition is true)
            # <non-indented statement> (execution jumps once condition is false)

            # Infinite loop (runs forever)
                # while True:
                    # <indented code block>

            # Loop and a Half (repeats until a flag is reached)
                # while True:
                    # <indented code block>
                # if <variable> == <flag value> (This is the strategy, will stop the loop, and effectively "half" will execute")
                    # <indented code block>
                # <non-indented code block>

        # Additionals

            # break
                # if <condition>
                    # <break> (In a nested loop, terminates the inner loop only, not the outer loop)
            # continue
                # if <condition>
                    # <continue> (In a nested loop, terminates only the current iteration within a loop, moves on to next iteration)
            # pass
                # if <condition>
                    # <pass> (Does nothing, useful for when code hasn't been implemented)


#### Files ####

    ## File mode

    # `r` `Reading mode (default)`
    # `w` `Writing mode; if the file already exists, all content is wiped`
    # `a` `Append mode; writes are appended to the end of the file`
    # `t` `Text mode`
    # `b` `Binary mode`

    ## File methods
    
    # `infile.read(n)` `Read n characters from file infile or until the end of the file, RETURN characters read as a string`
    # `infile.read()` `Read characters from file infile until the end of the file, RETURN characters read as a string`
    # `infile.readline()` `Read file infile until new line character or end of file, RETURN characters read as a string`
    # `infile.readlines()` `Read file infile until the end of the file, RETURN the characters read as a list`
    # `outfile.write(s)` `Write string s to file outfile`
    # `file.close()` `Close the file, should always do this'

#### Input and Output ####

    # `F-Strings` `Embeds outside previously set values inside a string` `e.g. var = 'a' print(f'The letter {var})`
    # `s.format(a,b,c)` ``Returns a string with empty {} filled by method parameters, in order. e.g. a then b then c {}{}{}`
    # `print(arg1,argN,..., sep ='', end= '\n')`
    # `input()` `Receives information from user and returns user response as string`
        # e.g. variable = input('displayed message')

    # `eval()` `Converts a str to a number`

#### Indexed Iteration ####
    
    # Looping through a collection while keeping track of the exact position of each item

    # `range(len('string'))` `Returns the indices of  string`
    # `Sequence of Index numbers` `for ele in range(len('string'))`
    #                                 `print(ele, 'string'[ele])`

    # `len('string')` `Returns an integer of the amount of characters in the inputted string`
    # `range(len('string'))` `Returns a zero-based sequence, that ends before the character amount of the string`
    # `for i in range(len('string')): print(ele)` `Prints each element on per line of the sequence created by range`
    # `for i in range(len('string')): print('string'[i])` `Loops through the inputted string and prints the character at index`
        # `print('string'[i+1])` `Removes the former 0 index and character, starts at the second character: string to tring`
        # `print('string'[i-1])` `Moves the last character in the sequence to the front and doesn't change length: string to gstrin`

#### Dictionaries/Maps ####

    # General
        # An unordered container which stores values via specific keys
        # A container that stores items that are accessible uding user-specified indexes

        # `General anatomy` `<variable> = { <key 1>:<value 1> , <key 2>:<value 2>, ..., <key i>:<value i:>}`
        # e.g. `employee = {'987-65-4321':['Yu', 'Tsun']}`

        # To access: `<dict var>[<key>]`

        # (key, value) pairs are separated by commas, enclosed by curly braces <{}>
        # Key and value separated by colon <:>, key to the left of colon, value to the right of colon
        # <key> must be IMMUTABLE
        # <value> can be any data type, mutable or immutable

    # Dictionary Opertators
        # `Indexing to access a value` `<variable>[<key>]`
        # `Return the value of a key` `<variable><.get(<key>)>`

        # `Add a (key, value) pair` `<variable>[<new key>] = <new value>`
        # `Modify an existing key` `<variable>[<existing key>] = <new value>`
        # `Remove a (key,value) pair` `<variable><.pop(<existing key>)>`
        # `Update/merge/overwrite a dict with another dict` `<variable><.update(<variable2>)>`

        # `Return a view of keys` `<vairable><.keys()>`
        # `Return a view of values` `<variable><.values()>`

        # `Return tuple pair objects from dict` `<variable><.items`

        # `Length of dictionary - number of (key, val) pairs` `len(<variable>)`
        # `Boolean key check` `<key> in <variable>` `<key> not in <variable>`
        # `Remove a (key,value) pair` `<variable><.pop(<existing key>)>`

#### Sets ####

    # General

        # An unordered sequence of items separated by commas and enclosed in curly braces

        # `Remove duplicates from a list` `<listvar> = list(set(<listvar>))`
            # Listvar is the variable assignment name of the list object
            # Converts the inital list to a set using the <set> operator, converts back to list using <list> operator, reassigns using the initial <listvar>
        
        # `Create an empty set object` `<assignvar> = <set()>` 
            # `e.g. s = set()`
    
    # Set Operators

        # `Boolean Check` `<object> in <set_assignvar>` `<object> not in <set_assignvar>`

        # `Return size of a set` `len(<set_assignvar>)`

        # `Check if two sets contain same elements` <set_assignvar1> == <set_assignvar2>
        # `Check if two sets don't contain same elements` `<set_assignvar1> != <set_assignvar2>`
        # `True if var1 is a subset of var2` `<set_assignvar1> <= <set_assignvar2>`
        # `True if var1 subset of var2 and sets do not contain same elements` `<set_assignvar1> < <set_assignvar2>`
        # `Returns union of two sets` `<set_assignvar1> | <set_assignvar2>`
        # `Returns intersection of two sets` `<set_assignvar1> & <set_assignvar2>`
        # `Returns difference between two sets` `<set_assignvar1> - <set_assignvar2>`
        # `Returns symmetric difference of two sets` `<set_assignvar1> ^ <set_assignvar2>`
            # `Symmetric difference: set of elements in either set, but not both`

    # Set Methods
        
        # `Add an item to a set` `<set_assignvar>.add(<item>)`
        # `Remove an item from a set` `<set_assignvar>.remove(<item>)`
        # `Empty a set` `<set_assignvar>.clear()`

#### Random Module ####

    # What most computer programs use to generate numbers - fake - pseudorandom

    # start with <import random>

    # `A random integer between two numbers` `<random>.randrange(start, up-to-stop)`
        # e.g. random.range(1,7)

    # `A random float between numbers` `<random>.uniform(start, up-to-stop)`
        # e.g. random.uniform(2,4)

    # `Shuffle the order of a mutable sequence` `<var_assign> = <random>.shuffle(<mutable_seq>)`
        # e.g. random.shuffle([1,2,3])

    # `Return a random item of a sequence` `<random>.choice(<sequence>)`

    # `Return a random list of items in a sequence` `<random>.sample(<sequence>, <sample size>)`

#### Namespaces ####

    # Every name (variable, function, type) has a scope (the namespace where it lives). Outside of this scope, it's invisible
    
    # `Local scope` `Names assigned inside the body of a function`
    # `Global scope` `Names assigned outside of any function` `Namespace is associated with the shell or entire module`
    # `Global variables` `Any variable defined in the module outside of any function`
        # e.g. say you had variable 'a' LOCALLY defined in function(), and global variable 'a' outside of the function
        # because of namespaces, these wouldn't interfere with eachother because they each have their own namespace

    # Encapsulation
        # Modularizes implementation details to keep code clear

        # Rough Example:

        # def function(a, b, c)
        #   a.method()
        #   a.method2()
        #   function2(a,b,c)

        # Code Reuse
            # Often repeated actions can be implemented in reusable ways for shorter code and easier maintainability
        
        # Modularity
            # Complexity is dealt with by breaking down the program into smaller, simpler, self-contained pieces
            # Each smaller piece can be designed, implemented, tested, debugged independently

        # Local Variables
            # Variables assigned inside a function should be invisible to the outer calling program
            
            # e.g. Outside of the double(), x has no assignment/invisible. If double were apart of a larger program, x can be used within without creating verbosity
            # def double(y):
            #   x = 2
            #   print('x = {}')

        # Program Stacks

            # Contains a stack frame, used to store variables local to the respective funcion call
            # Stack frame is also used to storoe the line number/memory address of where execution should resume after the function terminates
    
    # Error objects are called exceptions

    # Try/Except
    
            # try (executed first)
                # <indented code block 1>
            # except: # (executed only if an exception is raised while try block runs) # (if the try code works, the except block is ignored)
                # <indented code block 2>
            # <non-indented statement>
    
            # idented code block is attempted first
            # if it goes through without exceptions: code block 2 is ignored
            # if there is an exception, wherever it is excepted, remaining statements do not run
            # then, indented code block runs to completion without a new exception raised
    

    # Catching Specific Exceptions
    
            # try:
                # <indented code block 1>
            # except <TypeError1>: e.g. ValueError # executed only if the specific TypeError occurs, in this case a ValueError
                # <indented code block 2>
            # except <TypeError(n)>:
                # <indented code block (n)>
            # except: # executed if exception other than specific errors
                # <indented code block>
            # <non-indented code block>

    # Classes as Namespaces
            # Behind the scenes, a Python class is essentially a namespace e.g. list class
            # The class <list> is in a namespace called <list>, which contains methods and operators of the <list> class
    
            # e.g. lst = [1,2,3]
            # When execute: lst.sort()
            # Python first translates the statement to: list.sort(lst)
            # lst here is just an instance of the list class
    
            # Generally
            # <instance><.method(arg1,arg2,...)>
    
            # Python Translation:
            # <class><.method(instance, arg1, arg2,...)>
    
            # More e.g.
            # lst.append(9) on lst 9 == list.append(lst,9)
            # d.keys() == dict.keys(d)
    
            # Every implementation of EVERY class method must include an additional input argument, correspond to the instance calling the method)

#### Implementing classes and OOP ####

    # A class statement defines a new <type> and gives the type a name
    # A class is defined by its attributes i.e. the methods/functions within the class

    # Creating a class - composition
        # class <ClassName()>:
            # <indented codeblock>

    # Create an instance object of a class type - composition
        # <var_assign> = <ClassName()> <instance> = <ClassName() == constructor of ClassName>

    # Assign a attribute value to instance object of a class
        # <class_instance><.var_assign> = <var_value>
        # e.g. point.x = 3 # of Point() type



    # How a class method works
        # class <ClassName()>:
            # <def funct(instance, arg1, arg2)>
            #
    
    # General Class Definition

        # class <Class Name>:
            # <class variable1> = <value>
            # <class variable2> = <value>

            # def <class method 1>(self, arg11, arg12, ...):
                # <implementation of class method 1>
            # def <class method 2>(self, arg21, arg22, ...):
                # <implementation of class method 2>

#### BOUND VERSUS UNBOUND FOR CLASSES!


### new

# Namespaces

    # Error objects are called exceptions
        # 


    # Try/Except

        # try (executed first)
            # <indented code block 1>
        # except: # (executed only if an exception is raised while try block runs) # (if the try code works, the except block is ignored)
            # <indented code block 2>
        # <non-indented statement>

        # idented code block is attempted first
        # if it goes through without exceptions: code block 2 is ignored
        # if there is an exception, wherever it is excepted, remaining statements do not run
        # then, indented code block runs to completion without a new exception raised

    # Catching Specific Exceptions

        # try:
            # <indented code block 1>
        # except <TypeError1>: e.g. ValueError # executed only if the specific TypeError occurs, in this case a ValueError
            # <indented code block 2>
        # except <TypeError(n)>:
            # <indented code block (n)>
        # except: # executed if exception other than specific errors
            # <indented code block>
        # <non-indented code block>

    # Classes as Namespaces
        # Behind the scenes, a Python class is essentially a namespace e.g. list class
        # The class <list> is in a namespace called <list>, which contains methods and operators of the <list> class

        # e.g. lst = [1,2,3]
        # When execute: lst.sort()
        # Python first translates the statement to: list.sort(lst)
        # lst here is just an instance of the list class

        # Generally
        # <instance><.method(arg1,arg2,...)>33

        # <class><.method(instance, arg1, arg2,...)>

        # More e.g.
        # lst.append(9) on lst 9 == list.append(lst,9)
        # d.keys() == dict.keys(d)3

        # Every implementation of EVERY class method must include an additional input argument, correspond to the instance calling the method)

    # Implementing classes and OOP
        # 


# Class is a user-defined data type

# help(<object>) - returns a glossary of object's methods

# In OOP: parentheses/() instantiates a new instance/object/calls in memory
# Parentheses() calls a new object into instantiation and memory, saving to a variable determines instance-level memory or class-level memory

# Defining a Class Object by Composition - class <class_name> or class <class_name>():
    # no attributes or methods defined


# Defining a Class Object by Inheritance - class <class_name>(<parent_class_name>):
    # <class_name> inherits attributes and methods from <parent_class_name>

# e.g. class dog: or class dog(str): or class dog(object):

# Inspect a class object - <class_name> : returns data type, origin, and which class <class '__definitionOrigin__.<class_name>'> 
    # <class ...> : <what data type the class is>
    # <__dunderscore__> : <__where the class is defined__>
    # <.class_name>: <the exact recalled name and proof of definiton by that name's existence>


# Create an unsaved instance of a class - <classname>() : construction call, instantiates/creates an instance of the <class_name> data type, not stored in memory
    # without being assigned to a variable `ivie = dog()`, instance created but not saved


# Create an instance of a class - <var> = <class_name>() : instantiates/creates instance of <class_name> class and assigns to variable <var>
    # <ivie = dog()> : instantiates/creates instance of <dog> class and assigns to variable <ivie>
    # new instance of <dog> class is created and assigned to variable <ivie>
    # think of it like a soul or spirit assigned to a now named and defined entity in computer memory
    # each time this is executed it creates an instance of <dog> class and assigns it to variable <ivie> at a new address in memory, overwriting any duplicates
    # Saying <ivie> is a <Dog()> object


# Create an alias for a class - <var> = <class_name> : <var> now points to the <class_name> object, can even be used to create new instances of the <class_name> class, like an alias
    # e.g. <canine> = <dog>: <canine> now points to the <dog> class object, can be used to create new instances of the <dog> class


# Create a function method for a class
    # def <method_name>(<which instance is calling the method>, <args/params>, <args/params>, ...)
        # class Point()
        #   def function(self, xcoord):
        #       self.x = xcoord


# Create a variable and associated value inside of a class
    # <class_name>.<value_variable> = <value>

# Returns a class's namespace, dictionary of attribute and method names and mappings
    # <class_name>.__dict__


# Assign a variable and value inside of an instance
    # <instance_name>.<variable> = <value>
    # e.g. <point.x = 3> <ivie.color = 'white'> 
    #                                   No parentheses because it would instantiate an unsaved (no variable) instance of the class, basically pointless, would create the instance, assign the value, then destroy the instance

# Assign a variable and value inside of a class
    # <class_name>.<variable> = <value>
    #                                   No parentheses because it would instantiate an unsaved (no variable) instance of the class, basically pointless, would create the instance, assign the value, then destroy the instance

# Use a defined class method on an instance - <instance_name>.<method_name>(<parameters>) : <Class_name>.<method_name>(<instance>, <parameters>)
    # <instance_name>.<method_name>(<parameters>) 
    # Python translation: <Class_name>.<method_name>(<instance>, <parameters>)

    # Notice how when bounding by the instance name you do not need to reinstate the instance, it automatically is recognized as the referenced instance

# Every method needs a (self) signature, otherwise it won't know which instance to point to

# Dunderscore Instantiation __init__
    # Allows class constructor use/instance creation with input arguments, requires input arguments
    # <def __init__(self, parameter, parameter...)>
    
    # <def __init__(self, parameter, parameter...)>
    #   self.<var_assign> = <parameter>
    #   self.<var_assign> = <parameter2>

    # Instantiate with default inputs - default constructors
        # <def __init__(self, param1 = 0, param2 = '', param3 = [])
        #   self.<var_assign> = <param1>
        #   self.<var_assign> = <param2>
        #   self.<var_assign> = <param3>


# Return a dictionary of variables for a instance - <instance_name><.__dict__>
    # e.g. ivie.color = 'brown' -> ivie.__dict__ : {'color': 'brown'}

# Return a dictionary of variables for a class - <class_name><.__dict__>
    # e.g. class Dog:/class Dog(): -> Dog.__dict__

# Return instance variable values - <instance>.<variable>

# Change instance variable - <instance>.<variable> = <new_value>

# Access class attribute from instance namespace
    # <instance>.<method_name>

# point.setx(3)
# Python Translation: Point.setx(point,3)



# <class dog>
# <dog = dog()>
# creates an instance of dog class and names it dog, renders class object uncallable

# once created <ivie> lives at a specific address in mem, 
    # if <ivie> is assigned to another variable, e.g. <fido = ivie>, both variables point to the same instance of the <dog> class in memory
    # if <ivie> is assigned to a new instance of the <dog> class, e.g. <ivie = dog()>, the original instance of the <dog> class is still in memory, but <ivie> now points to a new instance of the <dog> class in memory