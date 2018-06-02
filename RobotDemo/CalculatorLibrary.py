# encoding=utf8
from calculator import Calculator, CalculationError, Cart


class CalculatorLibrary(object):
    """Test library for testing Calculator business logic.

    Interacts with the calculator directly using its `push` method.
    """

    def __init__(self):
        self._calc = Calculator()
        self._cart = Cart()
        self._result = ''

    def push_button(self, button):
        """Pushes the specified `button`.

        The given value is passed to the calculator directly. Valid buttons
        are everything that the calculator accepts.

        Examples:
        | Push Button | 1 |
        | Push Button | C |

        Use `Push Buttons` if you need to input longer expressions.
        """
        self._result = self._calc.push(button)

    def push_buttons(self, buttons):
        """Pushes the specified `buttons`.

        Uses `Push Button` to push all the buttons that must be given as
        a single string. Possible spaces are ignored.

        Example:
        | Push Buttons | 1 + 2 = |
        """
        for button in buttons.replace(' ', ''):
            self.push_button(button)

    def result_should_be(self, expected):
        """Verifies that the current result is `expected`.

        Example:
        | Push Buttons     | 1 + 2 = |
        | Result Should Be | 3       |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))

    def should_cause_error(self, expression):
        """Verifies that calculating the given `expression` causes an error.

        The error message is returned and can be verified using, for example,
        `Should Be Equal` or other keywords in `BuiltIn` library.

        Examples:
        | Should Cause Error | invalid            |                   |
        | ${error} =         | Should Cause Error | 1 / 0             |
        | Should Be Equal    | ${error}           | Division by zero. |
        """
        try:
            self.push_buttons(expression)
        except CalculationError, err:
            return str(err)
        else:
            raise AssertionError("'%s' should caused an error" % expression)

    def add_book_to_cart(self, bookname, price, publisher):
        self._cart.addBook(bookname, price, publisher)

    def configure_delivery_fee(self, city, fee):
        self._cart.setFeeOfCity(city, fee)

    def checkout(self, city):
        self._cart.caculate(city)

    def charge_should_be(self, expected):
        if self._cart.sum != int(expected):
            raise AssertionError('%s != %s' % (self._cart.sum, expected))
        print expected

    def next_state_of_exam_process(self, currentState, nextState):
        states = {u'报名': u'审批', u'审批': u'开考', u'开考': u'交卷'}
        if states[currentState] == nextState:
            return
        raise AssertionError('%s is not next state of %s' % (currentState, nextState))
