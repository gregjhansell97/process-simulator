from NextFit import *

testProc = NextFit(256)
print(testProc)

testProc.add('A', 20)
print(testProc)
testProc.add('B', 15)
print(testProc)
testProc.remove('A')
print(testProc)
testProc.add('C', 21)
print(testProc)