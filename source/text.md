title: Testing the blog engine
tags: prueba, markdown, mola
date: 2016-10-05



Esto es una *prueba*, sepa que `markdown` es un formato útil
e interesante.

1. Ejemplo de lista 1
2. Ejemplo de lista 2
3. Ejemplo de lista 3


	
This is the classic "unicode issue". I believe that explaining this is beyond the scope of a StackOverflow answer to completely explain what is happening.

It is well explained here.

In very brief summary, you have passed something that is being interpreted as a string of bytes to something that needs to decode it into Unicode characters, but the default codec (ascii) is failing.

The presentation I pointed you to provides advice for avoiding this. Make your code a "unicode sandwich". In Python 2, the use of "from __future__ import unicode_literals" helps. 
