import matplotlib.pyplot as plt
from counting_values import CalculationOfTheFactorialOfNumber, LinearComplexityCalculation, QuadraticComplexityCalculation, CalculationOfTheComplexityConstant, LogarithmicComplexityCalculation

class MainDraw:
    def __init__(self, number_of_element) -> None:
        self.number_of_element = number_of_element
    
    def drawing_a_graph(self):
        factorial = CalculationOfTheFactorialOfNumber(self.number_of_element)
        linear = LinearComplexityCalculation(self.number_of_element)
        quadratic = QuadraticComplexityCalculation(self.number_of_element)
        log = LogarithmicComplexityCalculation(self.number_of_element)
        const = CalculationOfTheComplexityConstant(self.number_of_element)
        
        x_values = list(range(1, self.number_of_element + 1))
        
        plt.plot(x_values, factorial.calculate_factorial_complexity(), 
                 label="Факториальная сложность")
        
        plt.plot(x_values, linear.calculate_linear_complexity(), 
                 label="Линейная сложность")
        
        plt.plot(x_values, quadratic.calculate_quadratic_complexity(), 
                 label="Квадратичная сложность")
        
        plt.plot(x_values, log.calculate_logarithmic_complexity(), 
                 label="Логарифмическая сложность")
        
        plt.plot(x_values, const.calculate_constant_complexity(), 
                 label="Константная сложность")
        
        plt.legend()
        
        plt.show()