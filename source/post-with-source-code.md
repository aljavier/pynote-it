title: Factorial with Python
slug: factorial
tags: insanity, kung-fu
date: 2016-07-07


Just an example Python code:

    :::python
    def factorial(x):
       if x == 0:
          return 1
       else:
          return x * factorial(x - 1)


