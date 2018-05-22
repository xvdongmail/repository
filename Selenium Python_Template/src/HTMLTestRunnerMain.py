from unittest import TestLoader,TestSuite
from HtmlTestRunner import  HTMLTestRunner
import os
import sys
sys.path.append("./test/")
from MyTestCase import MyTestCase
from MyTestCase1 import MyTestCase1

example_tests = TestLoader().loadTestsFromTestCase(MyTestCase)
example_tests1 = TestLoader().loadTestsFromTestCase(MyTestCase1)

suite = TestSuite([example_tests,example_tests1])

filename = r'template/report_template.html'

runner = HTMLTestRunner(template=filename,output='example_suite')

runner.run(suite)