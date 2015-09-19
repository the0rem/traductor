import unittest
import traductor.traductor

class TestTraductor(unittest.TestCase):

  def test_exists(self):
      self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()