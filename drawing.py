import matplotlib.pyplot as plt
from counting_values import CalculationOfTheFactorialOfNumber, LinearComplexityCalculation, CalculationOfTheComplexityConstant, QuadraticComplexityCalculation, LogarithmicComplexityCalculation


class FactorialComplexity:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
    def drawing_a_graph(self):
        data = CalculationOfTheFactorialOfNumber()
        x_values = list(range(1, self.number_of_element + 1))
        
        plt.plot(data.calculate_factorial_complexity(self.number_of_element))
        plt.xticks(x_values)
        
        plt.show()
        
class LinearComplexity:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
    def drawing_a_graph(self):
        data = LinearComplexityCalculation(self.number_of_element)
        x_value = [i for i in range(1, self.number_of_element + 1)]
        
        plt.plot(data.calculate_linear_complexity())
        plt.xticks(x_value)
        plt.yticks(x_value)
        
        plt.show()
        
class ConstantComplexity:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
    def drawing_a_graph(self):
        data = CalculationOfTheComplexityConstant(self.number_of_element)
        x_value = [i for i in range(1, self.number_of_element + 1)]
        
        plt.plot(data.calculate_constant_complexity())
        plt.xticks(x_value)
        plt.yticks(x_value)
        
        plt.show()
        
class QuadraticComplexity:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
    def drawing_a_graph(self):
        data = QuadraticComplexityCalculation(self.number_of_element)
        x_value = [i for i in range(1, self.number_of_element + 1)]
        
        plt.plot(data.calculate_quadratic_complexity())
        plt.xticks(x_value)
        
        plt.show()
        
class LogarithmicComplexity:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
        
    def drawing_a_graph(self):
        data = LogarithmicComplexityCalculation(self.number_of_element)
        x_value = [i for i in range(1, self.number_of_element + 1)]
        
        plt.plot(data.calculate_logarithmic_complexity())
        plt.xticks(x_value)
        
        plt.show()