from tkinter import *
from tkinter import ttk
from generetion_object import GenerationNameComplexity, GenerationEntryAndButton, GenerationMainGraph

class MainWindow:
    def __init__(self) -> None:
        self.name = GenerationNameComplexity()
        self.functional_objects = GenerationEntryAndButton()
        self.main_button = GenerationMainGraph()
        
    def draw_main(self):
        root = Tk()
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()
        
        self.name.generation_label()
        self.functional_objects.field_generation()
        self.main_button.generating_the_main_graph()
        
        root.mainloop()