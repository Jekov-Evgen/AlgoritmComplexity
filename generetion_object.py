from tkinter import *
from tkinter import ttk
from drawing import QuadraticComplexity, LogarithmicComplexity, LinearComplexity, FactorialComplexity, ConstantComplexity
from main_drawing import MainDraw


TEXT = "Получить график!"


class GenerationNameComplexity:
    def __init__(self) -> None:
        self.list_name_o_big = ["Квадратическая сложность(O(n^2))", 
                           "Логарифмическая сложность(O(log(n)))",
                           "Линейная сложность(O(n))",
                           "Факториальная сложность(O(n!))",
                           "Постоянная сложность(O(1))"]
        
        
    def generation_label(self):
        count_list = [i for i in range(0, 5)]
        
        for i in range(0, len(self.list_name_o_big)):
            ttk.Label(text=f'{self.list_name_o_big[i]}').grid(row=0, column=count_list[i], 
                                                              padx=20)


        

class GenerationEntryAndButton:
    def field_generation(self):
        self.quadratic = ttk.Entry()
        self.logarithmic = ttk.Entry()
        self.linear = ttk.Entry()
        self.factorial = ttk.Entry()
        self.constant = ttk.Entry()
        
        self.quadratic.grid(row=1, column=0, padx=20, pady=10)
        self.logarithmic.grid(row=1, column=1, padx=20, pady=10)
        self.linear.grid(row=1, column=2, padx=20, pady=10)
        self.factorial.grid(row=1, column=3, padx=20, pady=10)
        self.constant.grid(row=1, column=4, padx=20, pady=10)
        
        ttk.Button(text=f"{TEXT}", command=self.calling_func_quad).grid(row=2, column=0, 
                                                                          padx=20, pady=10)
        ttk.Button(text=f"{TEXT}", command=self.calling_func_log).grid(row=2, column=1, 
                                                                       padx=20, pady=10)
        ttk.Button(text=f"{TEXT}", command=self.calling_func_lin).grid(row=2, column=2, 
                                                                       padx=20, pady=10)
        ttk.Button(text=f"{TEXT}",command=self.calling_func_fact).grid(row=2, column=3, 
                                                                       padx=20, pady=10)
        ttk.Button(text=f"{TEXT}", command=self.calling_func_const).grid(row=2, column=4,
                                                                         padx=20, pady=10)
    
    
    def calling_func_quad(self):
        value = int(self.quadratic.get())
        graph = QuadraticComplexity(value)
        
        graph.drawing_a_graph()
        
        
    def calling_func_log(self):
        value = int(self.logarithmic.get())
        graph = LogarithmicComplexity(value)
        
        graph.drawing_a_graph()
        
        
    def calling_func_lin(self):
        value = int(self.linear.get())
        graph = LinearComplexity(value)
        
        graph.drawing_a_graph()
       
        
    def calling_func_fact(self):
        value = int(self.factorial.get())
        graph = FactorialComplexity(value)
        
        graph.drawing_a_graph()
        
        
    def calling_func_const(self):
        value = int(self.constant.get())
        graph = ConstantComplexity(value)
        
        graph.drawing_a_graph()
            
class GenerationMainGraph:
    def generating_the_main_graph(self):
        self.main_graph = ttk.Entry()
        self.main_graph.grid(row=3, column=0, padx=20, pady=10, columnspan=5, sticky="ew")
        
        ttk.Button(text="Получить общий график!", command=self.calling_main_draw).grid(row=4, column=0, 
                                                       columnspan=5, padx=20, pady=20, 
                                                       sticky="ew")
     
        
    def calling_main_draw(self):
        value = int(self.main_graph.get())
        graph = MainDraw(value)
            
        graph.drawing_a_graph()