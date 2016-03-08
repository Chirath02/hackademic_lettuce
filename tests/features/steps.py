from lettuce import world, steps


@steps
class FactorialSteps(object):
    """Methods in exclude or starting with _ will not be considered as step"""

    exclude = ['set_number', 'get_number']

    def __init__(self, environs):
        self.environs = environs

    def set_number(self, value):
        self.environs.number = int(value)

    def get_number(self):
        return self.environs.number

    def _assert_number_is(self, expected, msg="Got %d"):
        number = self.get_number()
        assert number == expected, msg % number

    def have_the_number(self, step, number):
        '''Given I have the number (\d+)'''
        self.set_number(number)

    def i_compute_its_factorial(self, step):
        number = self.get_number()
        self.set_number(factorial(number))

    def check_number(self, step, expected):
        '''Then I see the number (\d+)'''
        self._assert_number_is(int(expected))

# Important!
# Steps are added only when you instanciate the "@steps" decorated class
# Internally decorator "@steps" build a closure with __init__

FactorialSteps(world)


def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number-1)
