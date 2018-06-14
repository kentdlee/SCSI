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

Lesson One
-------------
From this lesson we learn how to create a program in Wing IDE 101, save it, run it, and interact with it.

The first program is almost always a hello world application. We'll start that way to keep things very simple. First start Wing IDE 101 and click the
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

Introduction to Types
================================
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
up in when we wrote "Hello". Strings are called the *str* type in Python. String literal values are written inside either double or single quotes.

In the first program we used two *functions*, *input* and *print*. The *input* function gets input from the user and returns a *str* of that input.
The *input* function is passed a prompt string to print when it is executed to so can prompt the user for input.

The *print* function prints the values passed to it to the screen separated by spaces.

We can convert from one type to another by writing the using the name of the type like a function in Python and passing in the value we want to
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

Notice that we added 1 to an integer in this code. Integers and floats support all the common arithmetic operations include +, -, \*, and /. Integers
also support // which represents integer division. So 6//4 would be 1. Integers also support the modulo (i.e. remainder) operator so 6%4 is 2. This
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

Strings, Integers, Floats

Calculate days, minutes, seconds since you were born.
Get input from the user. Convert to the correct type.

Lesson Two
-----------
Calculate change in dollars, quarters, dimes, nickels, and pennies.

Then use the datetime module to compute the days since you were born.



Introduction to Loops and Collections
=======================================
Tuples, Lists, Sets, Dictionaries

Use the random module to put some values in each of these types of collections.
Read words from a file. Add them to a list if they are not in a stop set.


Use a dictionary mapping tuples to integers to represent a tic tac toe board.

Write an evaluation function to find a win in the board.

Have students write an eval function for connect four.

Use datetime to keep track of how fast an item can be looked up.

Lesson Three
--------------
Create a word jumble by mixing up letters of words.

Use a dictionary to keep track of the words. Count the correct answers.  Keep a list of the incorrect answers. Keep track of time to see how fast they find the
answer.





Writing and Calling Functions
==============================

Writing Classes, Making Objects, Calling Methods
=================================================

Code Re-use with Inheritance
===============================

End of session one.

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

  * `Python Types and Operators <https://docs.python.org/3.6/library/stdtypes.html>`_
  * `Arithmetic Operators <https://www.tutorialspoint.com/python/python_basic_operators.htm>`_



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
