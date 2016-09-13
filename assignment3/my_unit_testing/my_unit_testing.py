#!usr/bin/env python3
# my_unit_testing.py: A simple module for making and executing tests.

import sys

class UnitTest(object):
    def __init__(self, func, args, kwargs, res):
        """Constructor-like function; prepares test.
           Can be used like this 'testname=UnitTest(func, args, kwargs, res)'
        
        Args:
            func (function): Function to test.
            args (argument list): List of standard arguments to use as input to func.
            kwargs (keyword argument list): Keyword arguments to input to func.
            res (any var): varibable to test the result of func against.

        Returns:
            <none>
        """
        self.func=func
        self.args=args
        self.kwargs=kwargs
        self.res=res

    def __call__(self):
        """Function that executes test.
           Ex. of use: 'testname()'

        Args:
            <none>
        Returns:
            bool: The return value. True for successful test. False otherwise.
        """
        try:
            testresult=self.func(*self.args, **self.kwargs)
        except:
            # print("Test failed.", sys.exc_info()[0])
            return False;

        if str(testresult) == str(self.res):
            # print("Test passed. Result: "+str(testresult)+" is the same as "+str(self.res))
            return True

        # print("Test failed. Result: "+str(testresult)+" should have been "+str(self.res))
        return False;
