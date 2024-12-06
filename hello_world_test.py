# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/hello-world/canonical-data.json
# File last updated on 2023-07-19

import unittest

try:
    from hello_world import (
        hello,
    )

except ImportError as import_fail:
    message = import_fail.args[0].split("(", maxsplit=1)
    item_name = import_fail.args[0].split()[3]

    item_name = item_name[:-1] + "()'"

    # pylint: disable=raise-missing-from
    raise ImportError(
        "\n\nMISSING FUNCTION --> In your 'hello_world.py' file, we can not find or import the"
        f" function named {item_name}. \nThe tests for this first exercise expect a function that"
        f' returns the string "Hello, World!"'
        f'\n\nDid you use print("Hello, World!") instead?'
    ) from None


class HelloWorldTest(unittest.TestCase):
    def test_say_hi(self):
        msg = "Hello, World!"
        self.assertEqual(hello(), "Hello, World!", msg=msg)

    def test_say_with_invalid_name(self):
        msg = "Hello, World!"
        self.assertEqual(hello("123"), "Hello, World!", msg=msg)

    def test_say_with_name(self):
        msg = "Hello, Arlen"
        self.assertEqual(hello("Arlen"), "Hello, Arlen!", msg=msg)

    def test_say_with_name_with_space(self):
        msg = "Hello, María Jose"
        self.assertEqual(hello("María Jose"), "Hello, María Jose!", msg=msg)
    
    def test_say_with_numbers(self):
        msg = "Hello, World!"
        self.assertEqual(hello(123), "Hello, World!", msg=msg)

    def test_say_hello_with_space_white(self):
        msg = "Hello, Arlen!"
        self.assertEqual(hello(" Arlen "), "Hello, Arlen!", msg=msg)
    
    def test_say_hello_with_number_and_string(self):
        msg = "Hello, World!"
        self.assertEqual(hello("Arlen545"), "Hello, World!", msg=msg)

    def test_say_hello_with_special_caracters(self):
        msg = "Hello, World!"
        self.assertEqual(hello("%&#/"), "Hello, World!", msg=msg)