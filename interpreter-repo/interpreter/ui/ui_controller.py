from abc import ABC, abstractmethod


class UIController(ABC):
    
    @abstractmethod 
    def input(self): 
        '''
        Retrieves Input from the user 

        Returns:
            (string): the input the user entered in.  
        '''
        pass 
    
    @abstractmethod 
    def display(self, value, options=None):  
        '''
        Displays a value to the user 

        Inputs: 
            value (string): the value to display to the user 
            options (any): An argument used to configure the display based on the UI controller implementation 

        Returns:
            (string) the input the user entered in.  
        '''
        pass 