import unittest
from . import traductor

def helloWorld(input):
	return "Hello, " + input + "!"

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(helloWorld("Docker"), "Hello, Docker!")



if __name__ == '__main__':
	unittest.main();