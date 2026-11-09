Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information

# Python Syntax Notes

# Operands `The value or variable to be operated on. e.g. 3, peach`
# Operators `The function performing the work, such as mathematical`

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
    # Integer Remainder `y % x` `Remainder as result of x into y instead of creating decimal`

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

        # `<variable> = { <key 1>:<value 1> , <key 2>:<value 2>, ..., <key i>:<value i:>}`
        # e.g. `employee = {'987-65-4321':['Yu', 'Tsun']}`

        # To access: `<dict var>[<key>]`

        # (key, value) pairs are separated by commas, enclosed by curly braces <{}>
        # Key and value separated by colon <:>, key to the left of colon, value to the right of colon
        # <key> must be IMMUTABLE
        # <value> can be any data type

    # Dictionary Opertators
        # `Indexing to access a value` `<variable>[<key>]`
        # `Add a (key, value) pair` `<variable>[<new key>] = <new value>`
        # `Modify an existing key` `<variable>[<existing key>] = <new value>`
        # `Length of dictionary - number of (key, val) pairs` `len(<variable>)`
        #  `Boolean key check` `<key> in <variable>` `<key> not in <variable>`

