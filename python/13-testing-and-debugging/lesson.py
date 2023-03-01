# TODO
# Mock objects
# Testing and Debugging

# Unit testing
# Unit testing is a method of testing software by using automated tests performed on units.
# A 'unit' in this context is a portion of your program that is supposed to work independently.
# Unit tests are performed by writing 'test cases', which isolate parts of your program to test.
#
# Integration testing
# Most software will be made up of multiple modules. Integration testing involves testing these
# modules as a group, to ensure they can communicate and share data properly.
# There are several methods of performing integration testing, but it is common to follow a
# 'test plan' which covers every module and outlines the steps and order they should be tested in.
# Integration testing is usually the next step after unit testing.
#
# System testing
# System testing involves testing a completely integrated system to ensure all requirements are met.
# Sometimes, the software you are writing is part of a larger software network or hardware system.
# System testing ensures that the end product meets the required specifications.
# Examples of system testing are:
# - Testing a login page by ensuring clients can enter credentials which takes them to a home page.
# - Conducting quality assurance tests on mobile devices by factory testing hardware and software.
# System testing is often the step after performing integration testing.
#
# Acceptance testing
# The purpose of system testing is to ensure the product does not fail and meets the requirements,
# while the purpose of acceptance testing is to ensure the product meets the demands of the
# clients or end-users.
# One example is User Acceptance Testing (UAT), which is the process of verifying a solution
# through a user ('beta testing').


# 1. Unittest
# Python's built-in module 'unittest' provides a suite for creating and running your own test cases.
import unittest

# Let's write something that we will test with.
def only_positive_integers(int_list):
    if not isinstance(int_list, list):
        return []
    return [x for x in int_list if x >= 0]

# Now on to testing. Create a subclass of the 'unittest.TestCase' class.
class TestExample(unittest.TestCase):

    # Any method of this class will be a test case.
    def test_list(self):
        # AssertEqual and assertNotEqual tests if two arguments are equal or not equal.
        self.assertEqual(only_positive_integers([-1, 0, 1]), [0, 1])

    def test_empty(self):
        # AssertTrue and assertFalse tests if an argument returns True or False.
        # May also provide an additional string to any assert function to display a failure message.
        self.assertTrue(isinstance(only_positive_integers(""), list), "Did not return a list!")

# When writing tests, remember that unit tests should be short and test only a single feature.
# Test cases should be 'atomic': independent, cause no side effects, and may run in any order.


# To run our testing suite:
unittest.main()
# Afterwards, try changing our testing code to see what Python outputs when test cases pass or fail.
