# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Scalene and Right','3,4,5 is a Right and scalene triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene and Right','5,3,4 is a Right and scalene triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(13,14,9), 'Scalene', '13,14,9 should be scalene')

    def testIsoscelesTrainglesA(self):
        self.assertEqual(classifyTriangle(3,3,4), 'Isosceles', '3,3,4 should be isosceles')

    def testIsoscelesTrainglesB(self):
        self.assertEqual(classifyTriangle(3,4,3), 'Isosceles', '3,4,3 should be isosceles')

    def testIsoscelesTrainglesC(self):
        self.assertEqual(classifyTriangle(4,3,3), 'Isosceles', '4,3,3 should be isosceles')

    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(2,-1,3), 'InvalidInput', '-1,2,3 is not valid input')

    def testZeroInput(self):
        self.assertEqual(classifyTriangle(0,2,3), 'InvalidInput', '0,2,3 is not valid input')

    def testOutsideOfRange(self):
        self.assertEqual(classifyTriangle(1,1,201), 'InvalidInput', '1,1,201 is not valid input')

    def testInsideOfRange(self):
        self.assertNotEqual(classifyTriangle(200,200,200), 'InvalidInput', '200,200,200 is a valid input')
        
    def testNonIntegerInputA(self):
        self.assertEqual(classifyTriangle(1,1.5,4), 'InvalidInput', '1,1.5,4 is not valid input')

    def testNonIntegerInputB(self):
        self.assertEqual(classifyTriangle(1.0,1,2), 'InvalidInput', '1.0,1,2 is not valid input')

    def testNonIntegerInputC(self):
        self.assertEqual(classifyTriangle('a','b','c'), 'InvalidInput', 'a,b,c is not valid input')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,1,3), 'NotATriangle', '1,1,3 is not a triangle')

    def testNotATriangleB(self):
        self.assertNotEqual(classifyTriangle(3,3,4), 'NotATriangle', '3,3,4 is a triangle')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

