from counting_values import CalculationOfTheFactorialOfNumber, LinearComplexityCalculation, QuadraticComplexityCalculation, CalculationOfTheComplexityConstant, LogarithmicComplexityCalculation
import pytest


@pytest.mark.parametrize("number_of_elements, result", [(5, [1, 2, 6, 24, 120]), (0, 1)])
def test_factoral(number_of_elements, result):
    factorial = CalculationOfTheFactorialOfNumber(number_of_elements)
    
    assert factorial.calculate_factorial_complexity() == result


def test_neg_fact():
    with pytest.raises(ValueError):
        factorial1 = CalculationOfTheFactorialOfNumber(-6)
        factorial1.calculate_factorial_complexity()
        
        
@pytest.mark.parametrize("number_of_elements, result", [(10, [i for i in range(1, 11)])])
def test_lin(number_of_elements, result):
    linear = LinearComplexityCalculation(number_of_elements)
    
    linear.calculate_linear_complexity() == result
    
    
def test_neg_lin():
    with pytest.raises(ValueError):
        linear = LinearComplexityCalculation(-2)
        linear.calculate_linear_complexity()
        
        
@pytest.mark.parametrize("number_of_element, result", [(2, [1, 4]), (6, [1, 4, 9, 16, 25, 36])])
def test_quadra(number_of_element, result):
    quadratic = QuadraticComplexityCalculation(number_of_element)
    
    assert quadratic.calculate_quadratic_complexity() == result
    
    
def test_neg_quadra():
    with pytest.raises(ValueError):
        quadratic = QuadraticComplexityCalculation(-3)
        quadratic.calculate_quadratic_complexity()
     
        
@pytest.mark.parametrize("number_of_element, result", [(5, [1, 1, 1, 1, 1]), (0, [])])
def test_const(number_of_element, result):
    const = CalculationOfTheComplexityConstant(number_of_element)
    assert const.calculate_constant_complexity() == result


def test_neg_const():
    with pytest.raises(ValueError):
        const = CalculationOfTheComplexityConstant(-4)
        const.calculate_constant_complexity()

  
@pytest.mark.parametrize("number_of_element, result", [(5, [0, 1, 1, 2, 2])])
def test_log(number_of_element, result):
    log = LogarithmicComplexityCalculation(number_of_element)
    assert log.calculate_logarithmic_complexity() == result

    
def test_neg_log():
    with pytest.raises(ValueError):
        log = LogarithmicComplexityCalculation(-2)
        log.calculate_logarithmic_complexity()