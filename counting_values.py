from math import log2


class CalculationOfTheFactorialOfNumber:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
        
    def calculate_factorial_complexity(self):
        if self.number_of_element == 0:
            return 1
        elif self.number_of_element < 0:
            raise(ValueError)
        
        result = 1
        ready_list_factorial = []
        
        for i in range(1, self.number_of_element + 1):
            result *= i
            ready_list_factorial.append(result)
            
        return ready_list_factorial
    
    
class LinearComplexityCalculation:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
        
    def calculate_linear_complexity(self):
        if self.number_of_element <= 0:
            raise(ValueError)
        
        list_of_elements = [i for i in range(1, self.number_of_element + 1)]
        
        return list_of_elements
    
    
class QuadraticComplexityCalculation:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
        
    def calculate_quadratic_complexity(self):
        if self.number_of_element <= 0:
            raise(ValueError)
        
        list_of_elements = [i ** 2 for i in range(1, self.number_of_element + 1)]
        
        return list_of_elements
    
    
class CalculationOfTheComplexityConstant:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
        
    def calculate_constant_complexity(self):
        if self.number_of_element < 0:
            raise(ValueError)
        
        list_of_elements = []
        
        for i in range(1, self.number_of_element + 1):
            list_of_elements.append(1)
            
        return list_of_elements
           
            
class LogarithmicComplexityCalculation:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
        
    def calculate_logarithmic_complexity(self):
        if self.number_of_element <= 0:
            raise(ValueError)
        
        list_of_elements = []
        
        for i in range(1 ,self.number_of_element + 1):
            list_of_elements.append(int(log2(i)))
            
        return list_of_elements