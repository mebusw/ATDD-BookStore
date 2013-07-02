#!/usr/bin/python
# -*- coding: utf-8 -*-  

class Calculator(object):
    BUTTONS = '1234567890+-*/C='

    def __init__(self):
        self._expression = ''

    def push(self, button):
        if button not in self.BUTTONS:
            raise CalculationError("Invalid button '%s'." % button)
        if button == '=':
            self._expression = self._calculate(self._expression)
        elif button == 'C':
            self._expression = ''
        else:
            self._expression += button
        return self._expression

    def _calculate(self, expression):
        try:
            return str(eval(expression))
        except SyntaxError:
            raise CalculationError('Invalid expression.')
        except ZeroDivisionError:
            raise CalculationError('Division by zero.')


class CalculationError(Exception):
    pass

class Cart(object):
    """docstring for Cart"""
    def __init__(self):
        self.sum = 0
        self._fees = {}
        self._books = []

    def addBook(self, bookname, price, publisher):
        self._books.append({'name': bookname, 'price': price, 'publisher': publisher})

    def setFeeOfCity(self, city, fee):
        self._fees[city] = int(fee)

    def caculate(self, city):
        #self.sum = sum(map(lambda book: int(book['price']), self._books))
        self.sum = reduce(lambda x, book: int(book['price']) + x, self._books, 0)
	print self._books, city
        if not (city == u'上海' and len([x for x in self._books if x['publisher'] == u'清华']) > 0):
            self.sum += self._fees[city]

        
