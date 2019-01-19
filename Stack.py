import random
import copy

class Stack: 
    def __init__(self): 
        self.l = []
        self.r = []
    
    def l_push(self, number):
        self.l.insert(0, number)

    def l_pop(self):
        self.l.pop(0)

    def r_push(self, number):
        self.r.append(number)

    def r_pop(self):
        self.r.pop(len(self.r)-1)

class Unit_Test:
    def __init__(self):
        self.stack = Stack()
        self.test_data = [random.randint(1,20) for i in range(5)]
        

    
    def test_l_push(self):
        print('Test data', self.test_data, ' will be pushed into LStack by order.')
        print('\n')

        for i in range(len(self.test_data)):
            print("Pushing", i, "th data", self.test_data[i])
            self.stack.l_push(self.test_data[i])
            print("LStack should be equal to ", self.test_data[i::-1])
            print("LStack actually is equal to ", self.stack.l)
        
        if (self.stack.l == self.test_data[::-1]):
            print("Test L_Push Passed.")
        else:
            print("Test L_Push Failed. ")
        
        print('\n')

    def test_l_pop(self):
        self.l_stack_data = [random.randint(1,20) for i in range(5)]
        self.stack.l = copy.copy(self.l_stack_data)
        print('Set LStack data to random data', self.l_stack_data)
        print('\n')

        print('Data on the Stack_L', self.stack.l, 'will be removed as FirstInLastOut Order')
        print('\n')

        for i in range(len(self.l_stack_data)):
            print('Removing the', i,  'th Element', self.l_stack_data[i], 'from L_Stack')
            self.stack.l_pop()
            print('Stack should be equal to ', self.l_stack_data[:i+1])
            print('Stack actually is equal to ', self.stack.l)

            if(self.l_stack_data[i+1:] == self.stack.l):
                print("Test L_Pop Passed.")
            else:
                print("Test L_Pop Failed ")
        
        print('\n')


    def test_r_push(self):
        print('Test data', self.test_data, ' will be pushed into RStack by order.')
        print('\n')

        for i in range(len(self.test_data)):
            print("Pushing", i, "th data", self.test_data[i])
            self.stack.r_push(self.test_data[i])
            print("RStack should be equal to ", self.test_data[:i+1])
            print("LStack actually is equal to ", self.stack.r)
        
        if (self.stack.r == self.test_data):
            print("Test R_Push Passed.")
        else:
            print("Test R_Push Failed. ")
        
        print('\n')
        
    def test_r_pop(self):
        self.r_stack_data = [random.randint(1,20) for i in range(5)]
        self.stack.r = copy.copy(self.r_stack_data)
        print('Set RStack data to random data', self.r_stack_data)
        print('\n')

        print('Data on the Stack_R', self.stack.r, 'will be removed as FirstInLastOut Order')
        print('\n')

        for i in range(len(self.r_stack_data)):
            print('Removing the', i,  'th Element', self.r_stack_data[len(self.r_stack_data)-i-1], 'from R_Stack')
            self.stack.r_pop()
            print('Stack should be equal to ', self.r_stack_data[:len(self.r_stack_data)-i-1])
            print('Stack actually is equal to ', self.stack.r)

            if(self.r_stack_data[:len(self.r_stack_data)-i-1] == self.stack.r):
                print("Test R_Pop Passed.")
            else:
                print("Test R_Pop Failed ")
        
        print('\n')


    

test = Unit_Test()
test.test_r_push()
test.test_r_pop()

test.test_l_push()
test.test_l_pop()










