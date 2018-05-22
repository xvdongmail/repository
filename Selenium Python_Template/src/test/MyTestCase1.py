import HtmlTestRunner
import unittest


class MyTestCase1(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\test\\1\\sdfs.html'))
