#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.

    NOTE:
    Your function should be only a single line long.
    You may not use any loops when implementing this function;
    you must use either the map and filter functions or list comprehensions.

    >>> evens(10)
    [0, 2, 4, 6, 8, 10]
    >>> evens(11)
    [0, 2, 4, 6, 8, 10]
    >>> evens(0)
    [0]
    >>> evens(1)
    [0]
    >>> evens(-1)
    []
    '''


def threes(n):
    '''
    Returns a list of all numbers from 0 to n inclusive that contain the digit 3.

    NOTE:
    Your function should be only a single line long.
    You may not use any loops when implementing this function;
    you must use either the map and filter functions or list comprehensions.

    >>> threes([2])
    []
    >>> threes([3])
    [3]
    >>> threes([10])
    [3]
    >>> threes([20])
    [3, 13]
    >>> threes([50])
    [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43]
    '''


def small_words(text):
    '''
    Returns a list of all words in the input text that are less than 4 characters long.

    NOTE:
    Your function should be only a single line long.
    You may not use any loops when implementing this function;
    you must use either the map and filter functions or list comprehensions.

    >>> small_words('this is a simple test case')
    ['this', 'is', 'a', 'test', 'case']
    >>> small_words('really enormous words')
    []
    >>> small_words('')
    []
    >>> small_words('a big word is bad')
    ['a', 'big', 'word', 'is', 'bad']
    '''


def squares(n):
    '''
    Returns a list of all square number between 1 and n inclusive.
    Recall that the nth square number is defined to be n*n.

    NOTE:
    Your function should be only a single line long.
    You may not use any loops when implementing this function;
    you must use either the map and filter functions or list comprehensions.

    >>> squares(1)
    [1]
    >>> squares(2)
    [1, 4]
    >>> squares(3)
    [1, 4, 9]
    >>> squares(10)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    '''


def lengths(strings):
    '''
    Given a list of strings, returns a list of the lengths of the corresponding strings.

    NOTE:
    Your function should be only a single line long.
    You may not use any loops when implementing this function;
    you must use either the map and filter functions or list comprehensions.

    >>> lengths([])
    []
    >>> lengths(['test'])
    [4]
    >>> lengths(['this','is','a','test'])
    [4,2,1,4]
    '''


def capital_lengths(strings):
    '''
    Given a list of strings, returns a list of the lengths of the corresponding strings that start with capital letters.

    NOTE:
    Your function should be only a single line long.
    You may not use any loops when implementing this function;
    you must use either the map and filter functions or list comprehensions.

    >>> lengths([])
    []
    >>> lengths(['test'])
    []
    >>> lengths(['this','is','a','test'])
    []
    >>> lengths(['This','Is','a','Test'])
    [4, 2, 4]
    >>> lengths(['tHIS','Is','a','Test'])
    [2, 4]
    '''
