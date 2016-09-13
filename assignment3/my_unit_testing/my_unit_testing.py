#!usr/bin/env python3
import sys

class UnitTest(object):
    def __init__(self, func, args, kwargs, res):    # make test
        self.func=func
        self.args=args
        self.kwargs=kwargs
        self.res=res

    def __call__(self):                             # run test    
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
