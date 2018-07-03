.. Game Development with Python master file, created by
   sphinx-quickstart on Wed May 30 21:12:53 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Game Development with Python!
=============================================================================



.. toctree::
   :maxdepth: 2

The goal of this camp is to open new worlds and possibilities to you in the area of computer programming. In this week we'll motivate learning to program
by exploring gaming. Today's video games are complex masterpieces and are programmed by teams of programmers, artists, and writers. Yet, video game
programming remains a very elite area with a huge amount of competition. So, my goal is not to teach you to be a video game programmer, but to teach
you to be a programmer by learning about video games and how they are constructed. More importantly, the skills and knowledge you learn by studying Computer Science
will open the door to a profession full of creativity, opportunities for life-long learning, and the skills needed to help many people.

There are a few basic things you need to learn to become a computer programmer. In the early lessons this week we'll study the Python programming language
and learn some of the basics.
Just as importantly there are
also skills we need to learn to find problems in our code. We almost never write code correctly the first time. We have to debug our programs until
they are correct. Don't worry if your program doesn't run the first time you run it. It probably won't. Programs working the first time they are run is the exception, not
the rule. Try the code you have written. When it doesn't work, try to figure out why. If you have spent a few minutes with the code and you are not sure
of the problem, then ask for help. There is no problem in asking questions.

In Computer Science, we never write anything ourselves from scratch. Instead, we
build on the shoulders of the giants that have come before us. Writing programs is a creative process and the design and coding of new creations (our programs) can
be very rewarding, both emotionally and monetarily. But we all must acknowledge as programmers we don't write things from scratch. Instead, we
build new things by using code that others have written before in new and creative ways.
Much of what we do as programmers relies on libraries of code that others have already written to make our job easier. So, an important part of
computer programming is reading, trying out libraries of code, and figuring out how to use it in building something new.

As programmers we use our creativity and ingenuity to take code from libraries and combine these libraries along with code
we write, to solve problems that impact the lives of those around us in some manner, hopefully for the good of humanity. We're very excited to have
you begin this journey, so let's get started!





Getting Started
===============================


.. container:: figboxright

  .. _guido:

  .. figure:: guido.jpg


  We are going to learn to program using a very popular programming language called Python. The language is named Python after Monty Python. It was first
  created by Guido Van Rossum, a programmer who worked for Google for a while and now works for Dropbox. Python is a language that is used by many
  websites to access data on web servers. It is also a language that will let you quickly learn to program. You can write a one line program in Python.

  Python is a high-level language, meaning that we can do a lot with very few statements and instructions to the computer. For instance, we can build a list
  of values from a file with one line of code. But, to accomplish these high-level tasks, we need a program to help us. Python is an interpreted language
  and that means that a special program, called the Python interpreter, translates the high-level statements that we write into the low-level commands
  understood by a computer.

  The figure below has the interpreter represented in Pink/Red. The internals of the interpreter (i.e. the stuff inside the Pink box) is not important
  to us. What is important is the source program which is interpreted by the Python interpreter, which is a program that understands how to run your
  source program using the operating system and the computer hardware. So, to run a Python program we must run it with a Python interpreter.


.. container:: figboxcenter

   .. _interpretfig:

   .. figure:: interpretation.png

Configuring Python
---------------------
To run Python programs you must have a Python interpreter installed. There are two versions of Python, version 2 and version 3.
We'll be using Python version 3 for our programming.

We'll download a version of Python that has lots of modules which provide code for us to use. Anaconda is a large distribution of Python with lots
of great modules available to use. We first bring up a web browser and go to http://anaconda.com. Then download version 3 of the anaconda distribution.
Install the anaconda distribution on the computer. Usually it is just installed in your home directory. Then we can add the anaconda *bin* directory
to your path. How to do this depends on your operating system. If you are using Windows, you edit the PATH environment variable using the Windows
method of modifying the path. If you are using Mac OS X then you must edit the PATH environment variable by editing the *.bashrc* file in your home
directory.

After installing anaconda, several other packages must be installed. First install keras. To do this you execute this command from a command prompt
on the system.

.. code-block:: text

    conda install keras==2.1.2

Then *pydot* and *graphviz* must be installed. For our purposes later it is probably best to have pydot version 1.2.4 installed and graphviz version 2.40.1.
Both *pydot* and *graphviz* are available as add-ons to the anaconda distribution of Python.

.. code-block:: text

    conda install pydot
    conda install graphviz

Finally, we need to install the pygame module so we can use it while building some games. Pygame is not available as an add-on to the anaconda distribution
but is available as part of Python so we use the *pip* command instead which is the Python install program (i.e. pip).

.. code-block:: text

    pip install pygame

This concludes installing all the Python software we'll need for this camp. Next we'll configure a tool for writing software to play games.

Configuring the IDE
--------------------

To write our Python programs we'll use an Integrated Development Environment, or IDE, that runs the interpreter by providing it with your source program.
Wing IDE 101 is our development environment.

Start up the Wing IDE 101 program. The first time you run it you must accept the license (it is free to use) and then configure it to run our distribution
of Python. To configure Wing IDE 101 choose Edit -> Configure Python... and then pick the
right Python interpreter. In our case we'll choose *pythonw* because this Python 3 interpreter will capture the keystrokes on the keyboard correctly
to interact with games developed with *pygame*.

.. container:: figboxcenter

   .. _configide:

   .. figure:: pythonconfig.png
      :scale: 50 %

Press OK to accept *pythonw* as the interpreter. Wing 101 will ask if you want to restart the *shell* which is just another
name for the Python interpreter. You can respond by clicking the *restart shell* button.

This is a one-time only configuration. Now, let's write our first program.

Lesson 1
-------------
From this lesson we learn how to create a program in Wing IDE 101, save it, run it, and interact with it.

The first program is almost always a hello world application. We'll start that way to keep things very simple, but with just a little extra.
First start Wing IDE 101 and click the
new program button. Then type the code from the figure below into the "untitled" pane. Once you are done typing it you can run it by clicking the
*bug* icon. This icon is used to run and debug your program.

.. container:: figboxcenter

   .. _helloworld:

   .. figure:: helloworld.png
      :scale: 50 %

When you first run it you will be asked to save it. Save it to your Desktop folder and call it helloworld.py with no spaces and no capital letters.

The program will wait for input from you. You have to type your name in the *Debug I/O* pane. Then it will finish printing its output.

Next, let's run it by stepping into it. Click the *step into* arrow on the right side. Then click the *step over* button to watch the Python interpreter
execute each of the two statements.

By clicking in the gray strip just to the right of the line numbers you can also set breakpoints. A breakpoint looks like a stop light. When a breakpoint
is encountered during execution of the program the program stops just before the statement is executed.

Try using step into, step over, and setting a breakpoint to make sure you know how they work.

Introduction to Types and Calling Functions
==============================================

Python supports doing math involving two different types. There are *integers* and *floats* in Python. We're familiar with integers. Floats are floating
point numbers which are the computer's version of Real numbers.

We can assign a *variable* a *value*. So for instance,

.. code-block:: python

    x = 6

This assigns the variable *x* the value *6*. The *6* has a type which is an integer, or *int* in the Python language. The *x* is a variable which is a *reference* to the value. A *reference* is a
pointer to a *value*. A *value* is also known as an *object*. So *6* is an integer object.

.. container:: figboxcenter

   .. _reference:

   .. figure:: reference.png

There are other types of values in Python. For instance, writing

.. code-block:: python

    y = 6.0

creates a variable reference *y* that points to a *float* object. Writing a decimal point in a number makes it a *float* instead of an *int*.

There are other types of values as well in Python. Strings are another example. In the first program above we have a string literal value show
up when we wrote "Hello". Strings are called the *str* type in Python. String literal values are written inside either double or single quotes.

The first program we wrote above calls two functions, the *input* function and the *print* function. A function is given a value or values and returns a value. The values
given to the function are written inside the parens. If there is more than one, they are separated by commas. You *call* a function by writing its
name. When a function is called you go to that function's code (which you might not see) and execute its code. When the function is done executing
it *returns*. A function always returns a value. Sometimes we care about the value the function returns. Other times we might not.

The *input* function gets input from the user and returns a *str* of that input.
The *input* function is passed a prompt string to print when it is executed. The prompt is printed to the screen and then the program stops and waits
for *enter* to be pressed. Any input typed before *enter* is pressed is returned from the *input* function as the value of the input.
In the program above the *input* function is given the string literal value "What is your name? " and it returns the input entered by the user.

The *print* function is given
the two strings to print. The first string is the string literal "Hello", the second string to print is the value entered by the user.
The *print* function prints the values passed to it to the screen separated by spaces. Notice that more than one value can be passed to some functions,
like *print*. When more than one value is passed to a function, we separate the values by commas. The *print* function
returns a special value called *None* which we don't care about so we don't bother writing

.. code-block:: python

    val = print("Hello",name)

because *val* would just refer to the value *None* anyway and we don't need that value in our program.


Converting Between Types
------------------------

We can convert from one type to another by writing the name of the type like a function in Python and passing in the value we want to
convert to a new type of value. For instance, consider getting the age of a person from the user.

.. code-block:: python

    name = input("What is your name? ")
    myAgeStr = input("What is your age? ")
    myAgeInt = int(myAgeStr)
    print(name, "next year you will be ", myAgeInt+1)

Examine the code above closely. The *myAgeStr* is a string because that's what *input* returns. The *myAgeInt* is an integer because we call the *int*
type conversion function on the string.

Normally we might simplify the code above to look something like this.

.. code-block:: python

    name = input("What is your name? ")
    myAge = int(input("What is your age? "))
    nextYearsAge = myAge+1
    print(name, "next year you will be ", nextYearsAge)

The code above has an *assignment statement* that assigns the value computed from *myAge+1* to the variable *nextYearsAge*. Alternatively, you can
increment the age. So you could write the code like this as well.

.. code-block:: python

    name = input("What is your name? ")
    age = int(input("What is your age? "))
    age = age+1
    print(name, "next year you will be ", age)

This code demonstrates that you can re-use the same variable and increment it in the program. Re-using the same variable works well when you want to
keep track of some accumulating value.

Arithmetic Operations
----------------------

Notice that we added 1 to an integer in the code in the previous section. Integers and floats support all the common arithmetic operations include +, -, \*, and /. Integers
support // which represents integer division. So 6//4 would be 1. Integers also support the modulo (i.e. remainder) operator so 6%4 is 2. This
is division like you learned in grade school. When you divide 6 by 4 you get 1 with a remainder of 2.

Strings support a few arithmetic operators as well like +, which is used for string concatenation. The * operator can be used with an integer to get
string repetition. Here are some sample operations with strings.

.. code-block:: python

    Kent's Mac> python3
    Python 3.6.5 |Anaconda, Inc.| (default, Apr 26 2018, 08:42:37)
    [GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 6 + 5
    11
    >>> "hi"*6
    'hihihihihihi'
    >>> "hi " + "there"
    'hi there'
    >>>

In the code example above I wanted to try out something in Python. You can do this in two ways. You can open a terminal window and try it there.
To do this go to the search icon at the top of the window, and type *terminal*. Then you can type *python3* to start the interpreter. Once you have
tried out what you see here you can type *ctl-d* to get out of the interpreter or just close the window.

The other way to try something out quickly is in Wing IDE 101. Click on the *Python Shell* pane and then you can try it right in that pane. You DON'T
need to type *ctl-d* inside Wing IDE 101 to get out when you are done using the Python Shell in Wing.

You can get more help with arithmetic operators in `Python by going to this page <https://www.tutorialspoint.com/python/python_basic_operators.htm>`_.

Lesson 2
------------------

Write a program that calculates the number of years since the Declaration of Independence was signed in 1776. Interacting with the program should look
exactly like this.

.. code-block:: text

    What year is it? 2021
    It has been 245 years since the Declaration of Independence was signed.


Once you have completed your solution, you can `check it here <_static/lesson2.py>`_.

String Operations
====================

Strings are another built-in type in Python. String objects have a number of *functions* that we can call on them. When a function is associated with
an object the function is called a *method*. To call the method we write the reference to the object first, followed by a dot, followed by the method
name. For instance, there is a method called *lower* that returns a new string with all the characters of the object lower cased.

So if we execute this code...

.. code-block:: python

    s = "Hello WORLD!"
    t = s.lower()
    print(t)

it prints the string "hello world!" to the screen. There are many other methods that work on strings as well.
They are listed `in the String documentation <https://docs.python.org/3.6/library/stdtypes.html#text-sequence-type-str>`_.

Lesson 3
---------------

Write a program that asks the user to type a sentence and then prints all the lower case characters as upper case and all the upper case characters
as lower case. So interacting with it should look like this...

.. code-block:: text

    Please type a sentence: Hello WORLD!
    Here is the new sentence: hELLO world!

Once you have completed your solution, you can `check it here <_static/lesson3.py>`_.

If Statements
================

There is another type in Python for true or false. Boolean values, called the *bool* type in Python, are *True* and *False*. Using Python we can compare
two values and get a boolean value as a result. Then we can execute one block
of code or another based on that result. The *then part* is executed if the boolean value is *True* in an *if* statement, and the *else part* is executed
if the value is *False* in an if statement.

For instance, consider this code.

.. code-block:: python

    dogName = input("What is your dog's name? ")
    if dogName == "Fido":
      print("That's not very original.")
    else:
      print(dogName, "is a cool name!")



We can also compare values for less than or greater than, less than or equal and greater than or equal.

.. code-block:: python

    age = int(input("Please enter your age: "))
    if age < 1:
        print("No your not!")
    else:
        print(age,"is a good age!")

    if age < 1:
        print("Younger than the first year, really?")
    elif age < 13:
        print("Those are great years!")
    elif age <= 19:
        print("You are a teenager! Oh boy!")
    elif age < 26:
        print("Your brain is still growing until you are 26. Did you know that?")
    else:
        print("Congratulations!")

    if age >= 8:
        print("You are ready to start learning to program!")



Lesson 4
-------------
Write a game that asks the user to think of a number between 1 and 100 (inclusive). Then check to see if the number is 50 or not and if it is, print that
it guessed right. So running the program would look like this if the user thought of 50.

.. code-block:: text

    Pick a number between 1 and 100.
    Is your number 50? Yes
    I guessed correctly!

And, if the number was not 50 then it should run like this.

.. code-block:: text

    Pick a number between 1 and 100.
    Is your number 50? No
    I guessed incorrectly!

This seems like a silly exercise. But it will get you writing some code with an if statement. You can compare strings with == and !=
for equals and not equals. However, strings are either lower case or upper case. If you have a string named *s* and you want to lower
case it you can write *s.lower()* to lowercase the string.

Once you have completed your solution, you can `check it here <_static/lesson4.py>`_.

Introduction to While Loops
=======================================

We can make the guessing game in the last lesson more interesting if we allow the program to repeatedly guess numbers to find the
correct answer. A *while* loop is just the trick. A while loop has a *loop body* which is a sequence of statements that will be executed
as long as the condition of the while loop evaluates to *True*. Here is an example of a while loop.

.. code-block:: python

    count = 0
    while count < 10:
      print(count)
      count = count + 1 # you can abbreviate this as count += 1

Run this code to see that it repeats the *print* and the *assignment statement* 10 times, printing 0 through 9 to the screen.

Lesson 5
------------

We can improve the guessing game by keeping track of two values a *low* and a *high* integer. Then each time through the loop we'll
guess the integer average of the *low* and *high* value. If we are wrong we should ask if the number is lower or higher. If it is lower then we can adjust the
*high* value. If it is higher than the average, then we can adjust the *low* value. In this way we keep repeating the body of the loop until the value
is found.

We can start the program by setting up the loop as follows.

.. code-block:: python

    ...
    found = False
    while not Found:
      # This is the body of the loop where we guess and then adjust low and high as
      # appropriate.

You fill in the blanks in this code so interacting with the program works like this.

.. code-block:: text

    Pick a number between 1 and 100
    Is your number 50? no
    Is it higher or lower? higher
    Is your number 75? no
    Is it higher or lower? lower
    Is your number 62? yes
    I guessed correctly in 3 tries.

Once you have completed your solution, you can `check it here <_static/lesson5.py>`_.

Two Container Types
====================

There are several types built into Python for containing other values. These types are called container
types or container classes. Tuples, lists, sets, and dictionaries are four of the common container types
available in Python.

We want to learn about these container types because we are going to write programs that often have more than one value
that we must keep track of. When we do, we want to use one of these containers if possible. For each of the containers we need
to know how to create a container object, how to put things in it, and how to get things back out of it. The *things* we put in containers are
called *elements* because containers are written so that practically any kind of element may be added to a container.

Tuples
--------

There are four different kinds of collections that are important for us as
computer programmers. We will first look at tuples. A *tuple* is a sequence
of values that cannot be changed once the tuple is created. For instance (4,3) is a
tuple of two integers. Here is some code that works with tuples.

.. code-block:: python
    :linenos:

    x = (4,3.0)
    y = x[0]
    z = x[1]
    print("x =",x)
    print("y =",y)
    print("z =",z)
    a,b = x
    print("a =",a)
    print("b =",b)
    c = (a,b,x)
    print("c =",c)

Running this code produces the following output.

.. code-block:: text

    x = (4, 3.0)
    y = 4
    z = 3.0
    a = 4
    b = 3.0
    c = (4, 3.0, (4, 3.0))

The tuple (4,3) is assigned to *x* on the first line. The second line takes the zeroth element of the tuple and assigns it to *y*. Tuples are immutable
sequences. Tuples being immutable means we can't change the elements of the sequence once the tuple has been created. Elements of sequences,
like tuples, are given index positions starting at 0. So *x[0]* is the first element of the tuple. Then *x[1]* is the second element of the tuple.

Using Python you can assign variables to each element of a tuple by separating by commas. Line 7 of the code above assigns *a* and *b* to the individual
elements of x. Finally, line 10 shows that a tuple may contain other tuples.

You can read more about `tuples by clicking here <https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences>`_.

Lists
------

Lists are similar to tuples, except that we use a slightly different syntax for creating a list and lists are *mutable* while tuples are *immutable*.
This means that lists can be modified once they are created. Consider this code.

.. code-block:: python
    :linenos:

    lst = []
    lst.append("hi")
    lst.append("there")
    print(lst)
    y = lst[0]
    x = lst[1]
    print(x)
    print(y)
    lst[1] = "Bob"
    print(lst)
    s = "Hello World\tHow,\tare\nyou?"
    print(s)
    sList = s.split()
    print(sList)

Line 1 of the code above creates an empty list. Lines 2 and 3 add to elements to the list, mutating it so it is no longer empty. Line 4 prints
the list. Take a look at the first line of output below to see what a list looks like when printed. Like tuples you can access individual elements of a
list as shown on lines 5 and 6. Take note of the fact that the indices into a list start at 0 and go to 1 less than the length of the list.
Line 9 shows how an element of a list may be mutated to hold a new value.

Line 13 shows how a string can be split by calling the *split* method which
returns a list of the white space separated values in the string. White space are any blanks, tabs, or newline characters found in the string. Take
note of how the tab character (i.e. \\t) and the newline character (i.e. \\n) are encoded in the string and how they affect the output coming from the
program.

.. code-block:: text

    ['hi', 'there']
    there
    hi
    ['hi', 'Bob']
    Hello World	  How,	are
    you?
    ['Hello', 'World', 'How,', 'are', 'you?']

More information on using `lists can be found here <https://docs.python.org/3/tutorial/datastructures.html>`_.

Patterns of Computation
=========================

In the following sections we'll learn about several patterns for computing things involving lists of elements. These patterns are used over and
over again in writing code. Each section will introduce one of these patterns through an example. You should take a moment in each section
to understand how these patterns can be applied to lots of different situations.

For Loops for Lists
--------------------

Lists are collections of elements. We keep elements in a list when the elements are all alike in some way. We might have a list of integers, or a list
of strings. We can even have lists of more complicated values like employees or students. For now, we'll limit our discussion to lists of strings and integers.

When we have a list of elements we may want to do something with each element of the list. This is where a *for loop* comes in handy. A *for loop*
iterates (i.e. repeats) once for each element of a list. Here is a loop that prints the elements of a list.

.. code-block:: python
    :linenos:

    s = "Hello World\tHow,\tare\nyou?"
    print(s)
    sList = s.split()
    print(sList)
    for element in sList:
      print(element)

This for loop prints each of the elements of the list.

Each list, like tuples, has index values that can be used to get individual elements of the list. Consider this code.

.. code-block:: python
    :linenos:

    s = "Hello World\tHow,\tare\nyou?"
    print(s)
    sList = s.split()
    print(sList[0])
    print(sList[1])

So *sList[0]* is the first element of the list. There is a *len* function that can be used to get the length of a list. There is also a *range*
function that will generate a list of integers, which can be used as the indices into a list. So this code will work to print the elements of a
list as well.

.. code-block:: python
    :linenos:

    s = "Hello World\tHow,\tare\nyou?"
    print(s)
    sList = s.split()
    print(sList)
    for i in range(len(sList)):
      print(sList[i])

The *range* function can be given three arguments. It can be called as *range(start,stop,increment)* and it generates a list of integers from *start*
to *stop-1* that goes up by *increment* each time. So *range(0,10,2)* would generate the list of integers *[0,2,4,6,8]* but not *10* because *range*
only goes to *stop-1* which would be *9* in this case.

We can also generate ranges that go backwards. So, *range(9,-1,-1)* would generate the list *[9,8,7,6,5,4,3,2,1,0]*. This can be used to build a
more flexible for loop for going through elements of a list. For instance, if we want to use a for loop to go backwards through a list we can write
the following.

.. code-block:: python
    :linenos:

    s = "Hello World\tHow,\tare\nyou?"
    print(s)
    sList = s.split()
    print(sList)
    for i in range(len(sList)-1,-1,-1):
      print(sList[i])

The code above will print *you?* first and *Hello* last.

Importing Modules
--------------------

A module is code that someone else wrote and that we can use. It is frequently useful to use code that others have already written so we
don't have to start from scratch for each program we write. We also know when we import a module that the module has been debugged
and should work as described. We import a module by writing

.. code-block:: python

    import module_name

where *module_name* is the module to be imported. Many, many modules are already written for Python. Included among them is the
`random <https://docs.python.org/3/library/random.html>`_ module.

If we import the *random* module we can use code in it to build a random permutation of a list of integers. Here is
some code that can be used to build a random permutation of a list of integers.

.. code-block:: python
    :linenos:

    import random
    rng = range(10)
    print(random.sample(rng,len(rng)))

To call the *sample* function from the *range* module, we write *random.sample(arguments)* to call it. To know what
is in the random module, you have to read the `random module documentation <https://docs.python.org/3/library/random.html>`_. Go there now to read
about the *sample* function and what it does.

The Accumulator Pattern
-------------------------

The *accumulator pattern* is a pattern of statements that is frequently used for accumulating a value calculated from the values in a list. The
general format of the pattern looks like this.

.. code-block:: python
    :linenos:

    accumulator = identity_value

    for element in list:
      accumulator = accumulator op element

    # use the accumulated value in the accumulator.

For instance, if we want to add all the values in a list together we might write something like this.

.. code-block:: python
    :linenos:

    total = 0

    for x in lst:
      total = total + x

    print("The total of the values in the list is", total)

This gives us the total numeric value. But, the same pattern might apply to concatenating all the strings in a list by writing this.

.. code-block:: python
    :linenos:

    sentence = ""

    for s in sList:
      sentence = sentence + s + " "

    print("The sentence is", sentence)

The blank is added to put spaces between the words that are concatenated to the string.

There are many uses of this pattern. It can be used to find the product of a bunch of numbers. Sums and concatenations are the example
given here. We can also use it in computing averages where we need the sum of the items and the number of items being averaged.

Lesson 6
------------

Let's use what we have learned to create a jumble of a word. For instance, if we have a word like "truck" then a jumble of it is "curtk".
Write a program that asks the user to enter a word and then prints a jumble of that word. Your program interaction should look like this.

.. code-block:: text

    Please enter a word: truck
    A jumble is curtk.

You should make sure that your output is identical to this, except that you might have a different jumble.

The solution to this involves using a for loop and the accumulator pattern so this
exercise brings a lot of things together that you just learned. To begin, write a program that prints out the same word that you type in. Then start
expanding on it. Write a little bit, try it, then write a little bit more. This is called incremental programming.

Once you have completed your solution, you can `check it here <_static/lesson6.py>`_.

The Guess and Check Pattern
-----------------------------

There is another useful pattern that shows up in many computer programs. The guess and check pattern is often used when dealing with a list of elements.
If you need to know if a certain condition holds for some element of a list, then you want to use the guess and check pattern.
The general pattern look like this.

.. code-block:: python

    guess = False
    for element in lst:
      if p(element):
        guess = True

    # after the for loop we know of p(element) was true for some element of lst

There are many variations of this pattern. For instance, if we want to know if an even
number appears in a list we might write something like this.

.. code-block:: python

    lst = [7,5,4,3,1]
    evenNumberExists = False

    for element in lst:
      if element % 2 == 0:
        evenNumberExists = True

    if evenNumberExists:
      print("There was an even number in the list.")
    else:
      print("There were no even numbers in the list.")

Again, there are many different versions of this guess and check pattern.

Reading a File
---------------------

It is sometimes useful to read from a file using Python. There are several ways to do this. Since a file consists of many lines of text, you can use
a while loop to read from a file. You may also use a for loop to read from a file. Consider reading from a file like the `wordsEn.txt <_static/wordsEn.txt>`_ file.
You can save this file by right-clicking on it and selecting *Save Link As...*. Save it to a file called *wordsEn.txt*. Then you can read this file
by writing this. The file and the program must be saved in the same directory for this code to work.

.. code-block:: python

    file = open("wordsEn.txt", "r")
    words = []
    for line in file:
      words.append(line.strip())

The code above builds a list called *words* that contains all the words found in the file. The call to *strip* removes any white space appearing
before or after the word. You can achieve the same result by using this alternative code.

.. code-block:: python

    file = open("wordsEn.txt","r")
    words = [x.strip() for x in file.readlines()]

This code relies on what is called a *list comprehension* to loop over the lines in the file and strip each line. The *file.readlines()* reads all the lines
of a file and places them into a list of strings. The *x.strip() for x in file.readlines()* takes each element of the list and *strips* the whitespace
which includes a newline character for each line of the file before it is stripped and removes those newlines. We end up with just a list of
all the words in the file.

Word Permutations
-------------------

Jumbles are permutations of words. A permutation is simply a rearranging of the elements of a list. In the case of jumbles, it is a rearranging of the
letters of the string. Permutations are something that can be useful and someone has written a module for doing this. The *itertools* module helps
in building permutations. For instance, to get all the permutations of the string "hello" we can use the following code.

.. code-block:: python

    import itertools

    s = "hello"
    lst = ["".join(x) for x in itertools.permutations(s)]
    print(lst)

This code uses the *itertools* *permutations* function to get all the permutations of a string. However, calling the *permutations* function
returns an object that when iterated over returns the permutations as tuples of characters like *('h','e','l','l','o')* instead of as strings.
So, the expression *"".join(x)* takes a tuple of characters and joins them all together into a string. So, the list comprehension above returns
the following list of values, which is the output from this code.

.. code-block:: text

    ['hello', 'helol', 'hello', 'helol', 'heoll', ...]

Many of the permutations are omitted here since there are 5x4x3x2x1=120 permutations.


Lesson 7
--------------

Jumbles often appear in newspapers and on websites. In this lesson you'll write a program that helps you solve jumbles. Ask the user to enter a jumbled
word. Then print possible solutions to each jumbled word that is entered. For instance, interacting with the program should work like this.

.. code-block:: text

    What is the jumbled word? ipnut
    Possible solutions are:
      input

You can write this code by using the wordsEn.txt file, reading it into a list, and then checking each of the permutations of the jumbled word to see
if they are in the list.

You can try these jumbles as well with your program: yamof, warely, and deonlo. One of them doesn't behave quite right. Why is that? Form a theory and
then check it out to see if you were right.

Once you have completed your solution, you can `check it here <_static/lesson7.py>`_.

Two More Container Types
=========================

Because of their importance to efficiency there are two more built-in types that we'll cover, sets and dictionaries. These two collections are important
because membership within them can be determined in constant time. That means that no matter how big the set or dictionary is, the amount of time needed
to determine if an element is in a set or dictionary does not increase. You may have noticed in lesson seven that it took a considerable amount of time
to determine what the jumbled word should be in some cases. This is because of the number of words in wordsEn.txt. As the size of the list of words
grows, so does the time it takes to look up a word. One solution to this is to use a set.

Sets
-------
A set is a collection of elements
where there are no duplicates and where there is no ordering of them. Sets are simply collections of unique elements. Python has two different set types.
The *frozenset* type is a set that cannot be altered after it is created. A *set* is a mutable (i.e. alterable) set of elements. Documentation on how
to use `both types of sets can be found here <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_.

If we wanted to build a *frozenset* of all the words in the *wordsEn.txt* file all we have to do is add a *frozenset* type conversion to our list
comprehension that builds the list of words.

.. code-block:: python

    file = open("wordsEn.txt","r")
    words = frozenset([x.strip() for x in file.readlines()])

This gives us a frozen set. If we replaced the *frozenset* with *set* then we would have a *set* type of value. The need for the distinction between
*sets* and *frozensets* will be clearer after reading about dictionaries.

Both set types support set operations like *intersection*, and *union*, and *difference*. There are mutating methods for the *set* type that also
support mutating set operations like *intersection_update*, *update*, and *difference_update*. To learn more about these operations you can read the set
documentation.

You can test for set membership using the *in* operator.
So, the following code can be executed for a set of integers.

.. code-block:: python

    mySet = frozenset(range(10))

    x = 6
    if x in mySet:
      print("Yes")
    else:
      print("No")

This code will print *Yes* when executed. If *x=10* it would print *No*. As an example of computing the intersection of two sets consider
this code.

.. code-block:: python

    firstSet = frozenset(range(10))
    secondSet = frozenset(range(5,20))

    thirdSet = firstSet.intersection(secondSet)

    print(thirdSet)

When executed, this code prints *frozenset({5, 6, 7, 8, 9})* as the result.

Lesson 8
--------------
Redo the jumble code from lesson seven to use frozensets instead of lists whenever possible. Make sure you have the same output as before. You should
notice a significant speed up in finding the correct answers. Again, you can try out ipnut, yamof, warely, and deonlo. The interaction with the program
should look like this.

.. code-block:: text

    What is the jumbled word? ipnut
    Possible solutions are:
      input

Once you have completed your solution, you can `check it here <_static/lesson8.py>`_.


Dictionaries
--------------

A *dictionary*, sometimes called a *map* or a *hashtable*, is a mapping of *keys* to *values*. A *set* is like a dictionary with only the *keys* being
in a set. The dictionary, or *dict* type in Python, is used to map a *key* to a *value* for some set of keys. Here is an example of creating
and using a dictionary in Python.

.. code-block:: python

    stateCapitals = {}
    stateCapitals["MN"] = "St. Paul"
    stateCapitals["IA"] = "Des Moines"
    stateCapitals["WI"] = "Madison"

    for state in stateCapitals:
      print(state,stateCapitals[state])

    if "ND" in stateCapitals:
      print(stateCapitals["ND"])
    else:
      print("ND is not in the stateCapitals map")

The code above shows us that we can iterate over the keys in the dictionary by using a for loop. We can also use the subscript operator to
get the *value* that goes with the *key* by writing *stateCapitals[state]* where *state* is that key.

The cool thing about a dictionary is that the keys can be virtually any value that is not mutable and can be compared for equality. So the key
can be a tuple, a string, a frozenset, or an integer, or other immutable values. A key to a dictionary cannot be a set, or a list, or another dictioinary
because these are mutable values.

Lesson 9
-------------

Create a dictionary that maps tuples of (row,col) to values of "X" or "O". Then write two nested for loops that print a tic tac toe board. You should
get the contents of the board from the user. So, interacting with the program should look like this.

.. code-block:: text

    Please enter the first row of the board : X O X
    Please enter the second row of the board: X _ X
    Please enter the third row of the board : _ O _

    The board is currently this:
    | X | O | X |
    -------------
    | X |   | X |
    -------------
    |   | O |   |

When printing, if you don't want to print a newline character at the end of a print, you can call print like this:

.. code-block:: python

    print("Hello World", end="")

and it will not print a newline at the end. In addition, if you want to print a newline someplace other than the end of a print, you can
include the newline in the string like this.

.. code-block:: python

    print("Hello\nWorld")

These two hints may help in solving this problem.

Make sure you use two nested for loops to print the board back out once you have created the board dictionary. It will be helpful if you treat
the first row as row 0 and the first column as column 0 so that *board[(0,0)]* is the upper left corner of the tic tac toe board.

Once you have completed your solution, you can `check it here <_static/lesson9.py>`_.

Writing and Calling Functions
==============================

As our programs get bigger we want to organize them and one of the major organizational tools in Python is the ability to define functions.
A function has a name and is given arguments. The function returns a value. We call a function, which is a sequence of statements that are
executed using the arguments provided to it. When the sequence of statements finishes, we return to where we called the function. Consider this code.

.. code-block:: python

    # This is a predicate function that takes an integer as an argument and
    # returns true if the integer is even and false otherwise.
    def isEven(x):
      if x % 2 == 0:
        return True

      return False

    # This function takes a list of numbers and multiplies all of them together
    # and returns the product of those numbers.
    def product(lst):
      product = 1
      for x in lst:
        product = product * x

      return product

    # This is the start of code that is not in either function. This is the module level code.
    evens = []

    for x in range(1, 100):
      if isEven(x):
        evens.append(x)

    evensProduct = product(evens)

    print("The product of the even numbers between 1 and 99 is", evensProduct)

This code above is used to find the product of all the even numbers between 1 and 99.

Typically Python programs have a main function that is defined. The *main* function is defined to contain the top-level code of our program. It
typically is not very complicated. If it gets too complicated we will usually figure out how to organize the program better to keep the main
function simpler. Here is the general format for writing a main function and calling it using the above example again.

.. code-block:: python
    :linenos:

    # import any modules at the beginning

    def isEven(anInt):
      x = anInt % 2
      if x == 0:
        return True

      return False

    def product(lst):
      product = 1
      for x in lst:
        product = product * x

      return product

    # Typically Python programs have a main function someplace which is where
    # the program begins execution (because of the call to it shown below.)
    def main():

      # This is the code in the main function of this program.
      evens = []

      for x in range(1, 100):
        if isEven(x):
          evens.append(x)

      evensProduct = product(evens)

      print("The product of the even numbers between 1 and 99 is", evensProduct)

    # This if statement is at the module level. It is the only
    # code that is at the module level in this program.
    # By writing this if statement, if the program is run
    # by itself then main() is called to run the program.
    # If this module were imported into another program
    # the following condition would be false and so
    # the main function defined above would not be called.
    if __name__ == "__main__":
      main()

There is another important concept to understand in regard to functions. A variable
defined inside a function is only available in that function and not outside it. So for instance,
the variable *x*, defined on line 4 in the *isEven* function, is not available outside of that function.
The variable *x* that appears on line 24 in the *main* function is a different x. So when *isEven* is called
on line 24 and then assigns a value to *x* on line 4, this is a different *x* than is being assigned a value
on line 24 in the program. In this way, we don't have to worry about what the names of variables are outside
the function that we are writing. We know that anything we define inside a function is only defined inside
the function and not elsewhere.

Lesson 10
-----------
Let's take the code from the last lesson and modify it so that X's are represented with 1's and O's are
represented with -1's. Zero can represent a blank spot. So, we can write code at the module level to
be used as constants in our code. Take a look at this code below.

.. code-block:: python
    :linenos:

    X = 1
    O = -1
    tokenToChar = {}
    tokenToChar[X] = "X"
    tokenToChar[O] = "O"
    tokenToChar[0] = " "

    def printBoard(board):
        for i in range(3):
            print("|",end="")
            for j in range(3):
                print(tokenToChar[board[(i,j)]]+"|",end="")
            print('\n-------')


    def main():
        row1 = "X _ O".split() #input("Please enter the first row of the board : ").split()
        row2 = "X X O".split() #input("Please enter the second row of the board: ").split()
        row3 = "O O X".split() #input("Please enter the third row of the board : ").split()
        board = {}

        for i in range(len(row1)):
            if row1[i] == "X":
                board[(0,i)] = X
            elif row1[i] == "O":
                board[(0,i)] = O
            else:
                board[(0,i)] = 0

        for i in range(len(row2)):
            if row2[i] == "X":
                board[(1,i)] = X
            elif row2[i] == "O":
                board[(1,i)] = O
            else:
                board[(1,i)] = 0

        for i in range(len(row3)):
            if row3[i] == "X":
                board[(2,i)] = X
            elif row3[i] == "O":
                board[(2,i)] = O
            else:
                board[(2,i)] = 0

        printBoard(board)
        #print(evalBoard(board))


    if __name__ == "__main__":
        main()


Take a look at the printBoard code and see how it works. Now, define another function called *evalBoard* which when it is called
will return 1 if X wins, -1 if Y wins, and 0 if nobody wins or if there is no winner yet. Be sure to call your *evalBoard* function
to try it out.

Once you have completed your solution, you can `check it here <_static/lesson10.py>`_.

Writing Classes, Making Objects, Calling Methods
=================================================

As programs get even bigger, there needs to be even more organization to them. For instance, in the previous lesson we have developed two functions
that both operate on a Tic Tac Toe board. It would be nice to group these functions together by tying them to a class of data. *Classes* are the
means a programmer can describe a new *type* to Python and the operations that are allowed on that new *type*. Consider this code.

.. code-block:: python
    :linenos:

    # This is the name of the new type (i.e. class).

    class Kitty:
      # Inside the class is anything indented inside it. This class
      # extends to the "def main" below.

      # This method name is the one given to the constructor. It exists
      # so objects can be created as shown on lines 31 and 48 below.
      # The constructor stores values in the object which is referred to
      # by self.
      def __init__(self, name):
        self.name = name

      # This is a method that has a side-effect. It returns None.
      def speak(self):
        print(self.name,'says meow')

      # This is an accessor method since it access the name
      # field of the object referred to by self.
      def getName(self):
        return self.name

      # This is a mutator method since it changes the name
      # field of the object referred to by self.
      def setName(self,newName):
        self.name = newName

    def main():
      # Here we create an object by writing the type's class
      # name in this expression.
      helloKitty = Kitty("Tigger")

      # Here is how a method is called. We write the
      # object . method ( arguments )
      # to call a method. In this case there are no
      # arguments because self is supplied by writing
      # helloKitty on the left side of the dot.
      helloKitty.speak()

      # Here is a call to an accessor method. Notice we
      # write helloKitty.getName() to call getName on
      # the helloKitty object.
      catName = helloKitty.getName()
      print(catName)
      helloKitty.setName("Curious")

      # This creates a second Kitty object.
      secondKitty = Kitty("Mother")

      # Notice the two calls to speak. One
      # on helloKitty's object and one on
      # secondKitty's object.
      helloKitty.speak()
      secondKitty.speak()



    if __name__ == "__main__":
      main()

The comments in the code above are important to review here. Take the time to review
each line to see what it does and to familiarize yourself with the syntax. Then use
the debugger to step into and over the entire program to watch how it executes. Check
out the *Stack Data* pane in Wing IDE 101 so you can watch the objects as they are
created and manipulated.

Operator Overloading
======================

Because of its importance to understanding how some code works in Python, we'll briefly go over
operator overloading. Python allows certain operators to be overloaded like +, -, \*, /, //, %, *in*, and
many other `operators that are covered here <https://docs.python.org/3.6/library/operator.html>`_.

These operators are actually implemented as methods with special names in Python. For instance the __setitem__ and __getitem__ methods
can be implemented to allow the subscript operator to be used on an object.

.. code-block:: python

    x = [1,2,3]
    # Here is an example of __setitem__ being called on a list.
    x[0] = 4

    # Here is an example of __getitem__ being called on a list.
    print(x[2])

The overloaded method is called when the operator is used in an expression.

The Tic Tac Toe board dictionary that we used in previous code could be implemented by writing a new class called TicTacToeBoard. But, we might still
want to be able to set and get items from the dictionary as we did in the past. To do this we could write code like this.

.. code-block:: python
    :linenos:

    X = 1
    O = -1
    tokenToChar = {}
    tokenToChar[X] = "X"
    tokenToChar[O] = "O"
    tokenToChar[0] = " "

    class TicTacToeBoard:
        # The TicTacToeBoard contains a dictionary which is called data. This encapsulates
        # the board into the TicTacToeBoard object and hides the details from those using
        # the object.
        def __init__(self):
            self.data = {}

        # Here is the set item magic method for the set item operator
        def __setitem__(self,key,val):
            self.data[key] = val

        # And here is the get item method.
        def __getitem__(self,key):
            return self.data[key]



    def main():
        row1 = "X _ O".split() #input("Please enter the first row of the board : ").split()
        row2 = "X X O".split() #input("Please enter the second row of the board: ").split()
        row3 = "O O X".split() #input("Please enter the third row of the board : ").split()

        # Notice that the board is created differently now.
        board = TicTacToeBoard()

        # __setitem__ is used in the code below.
        for i in range(len(row1)):
            if row1[i] == "X":
                board[(0,i)] = X
            elif row1[i] == "O":
                board[(0,i)] = O
            else:
                board[(0,i)] = 0

        for i in range(len(row2)):
            if row2[i] == "X":
                board[(1,i)] = X
            elif row2[i] == "O":
                board[(1,i)] = O
            else:
                board[(1,i)] = 0

        for i in range(len(row3)):
            if row3[i] == "X":
                board[(2,i)] = X
            elif row3[i] == "O":
                board[(2,i)] = O
            else:
                board[(2,i)] = 0

        # check out how the two methods below are now called. They
        # are no longer functions. They are methods which are a part
        # of the TicTacToeBoard class.
        board.print()
        print(board.eval())


    if __name__ == "__main__":
        main()


Lesson 11
------------

The code above shows us how we might define and use a new TicTacToeBoard class. It won't work as it stands. To get the code
above to work you must write the *print* and the *eval* methods of the TicTacToeBoard class. Complete this lesson by implementing
these methods.

Once you have completed your solution, you can `check it here <_static/lesson11.py>`_.


Code Re-use with Inheritance
===============================

Inheritance is something we can use when writing classes so that we can re-use code that was written
before. In some languages inheritance plays another role as well, but with Python the only reason
for inheritance is code reuse.

Using our previous exercise as an example, the code below now inherits from *dict* instead of
encapsulating a *dict* called *data* as in the last example. So, TicTacToeBoard is a dictionary
and therefore does not need to have __getitem__ and __setitem__ written for it. This is the code re-use
in this case. We automatically get these two methods because we are using inheritance. But, we still have
to write the *print* and *eval* methods.

.. code-block:: python
    :linenos:

    X = 1
    O = -1
    tokenToChar = {}
    tokenToChar[X] = "X"
    tokenToChar[O] = "O"
    tokenToChar[0] = " "

    class TicTacToeBoard(dict):
        # In this version, the TicTacToeBoard inherits from dict which means that
        # TicTacToeBoard is a dictionary and does not need the __getitem__ and __setitem__
        # methods because they are already defined. In addtion, the constructor below
        # doesn't do anything except call the super constructor which should always be
        # the first thing you do in an inherited constructor so you call the original
        # super class constructor to do whatever it needs to do. Sometimes you might write
        # additional code after the call to super().__init__()
        def __init__(self):
            super().__init__()


    def main():
        row1 = "X _ O".split() #input("Please enter the first row of the board : ").split()
        row2 = "X X O".split() #input("Please enter the second row of the board: ").split()
        row3 = "O O X".split() #input("Please enter the third row of the board : ").split()

        # Notice that the board is created differently now.
        board = TicTacToeBoard()

        # __setitem__ is used in the code below.
        for i in range(len(row1)):
            if row1[i] == "X":
                board[(0,i)] = X
            elif row1[i] == "O":
                board[(0,i)] = O
            else:
                board[(0,i)] = 0

        for i in range(len(row2)):
            if row2[i] == "X":
                board[(1,i)] = X
            elif row2[i] == "O":
                board[(1,i)] = O
            else:
                board[(1,i)] = 0

        for i in range(len(row3)):
            if row3[i] == "X":
                board[(2,i)] = X
            elif row3[i] == "O":
                board[(2,i)] = O
            else:
                board[(2,i)] = 0

        # check out how the two methods below are now called. They
        # are no longer functions. They are methods which are a part
        # of the TicTacToeBoard class.
        board.print()
        print(board.eval())


    if __name__ == "__main__":
        main()

Lesson 12
------------

The code above shows us how we might define and use a TicTacToeBoard class that inherits from *dict*. It won't work as it stands. To get the code
above to work you must write the *print* and the *eval* methods of the TicTacToeBoard class. Complete this lesson by implementing
these methods.

Once you have completed your solution, you can `check it here <_static/lesson12.py>`_.

Introduction to Animation
===========================

Frames and Double Buffering

How does PyGame do it?

Translation, Rotation, and Scaling
====================================
Always relative to origin.

How does PyGame do it?

Building a Video Game
======================
Missile Command? Angry Birds?

End of session two.

Composite Shapes
=================
Animating.

Detecting Collisions
====================

End of Session 3.

Games of Perfect Information
============================
Tic Tac Toe

Minimax

Connect Four

Machine Learning Opponents
============================
Building an AlphaZero opponent for Connect Four.

Python Quick Reference Links
==============================

  * `Types and Operators <https://docs.python.org/3.6/library/stdtypes.html>`_
  * `Arithmetic Operators <https://www.tutorialspoint.com/python/python_basic_operators.htm>`_
  * `Built-in Types <https://docs.python.org/3.6/library/stdtypes.html>`_
  * `String Operations <https://docs.python.org/3.6/library/stdtypes.html#text-sequence-type-str>`_
  * `Tuples and Sequences <https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences>`_
  * `Lists <https://docs.python.org/3/tutorial/datastructures.html>`_
  * `Sets <https://docs.python.org/3/tutorial/datastructures.html#sets>`_
  * `Dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
  * `Random module <https://docs.python.org/3/library/random.html>`_
  * `Itertools module <https://docs.python.org/3.6/library/itertools.html>`_
  * `Operator Overloading in Python <https://docs.python.org/3.6/library/operator.html>`_



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
