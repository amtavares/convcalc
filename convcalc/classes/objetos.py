import pandas as pd
import utils.functions

pd.set_option('display.max_colwidth', -1)

class Conveyor():

    def __init__(self):
        self.capacity = None #Ton/h
        self.lenght = None
        self.deltay = None
        self.puley_quantity = None


class Belt():

    def __init__(self):
        self.manufacturer = None
        self.modelname = None

        # Phisycal properties
        self.mass_per_lenght = None
        self.lenght = None
        self.width = None
        self.width_sm = None

class Material():

    def __init__(self):
        self.name = None
        self.density = None
        self.lumpsize = None
        self.inflamabe = None
        self.mass_per_lenght = None

    @property
    def max_lumpsize(self):
        return max(self.lumpsize)
    


class Table():
    def __init__(self, filename=None):

        self.dataframe = None        
        if filename:
            self.name = filename.split('/')[-1]
            self.load_data(filename)


    def load_data(self, file):
        try:
            self.dataframe = pd.read_csv(file, index_col=0)
            self.dataframe.index = self.dataframe.index.astype(str)
            self.dataframe.columns = self.dataframe.columns.astype(str)
        except Exception as e:
            print('Error loading file {}. {}'.format(file,e))



    def get_value(self, line, column, method='exact'):
        '''Return the value in the specified line and column values
            method: ['exact', 'upper', 'lower']
                exact: Search for the exact values of line and column
                upper: search for the first value grater than the line and/or column
                lower: search for the last value smaller than the line and/or column
        '''

        if method=='exact':
            return self.dataframe.loc[str(line), str(column)]
        elif method=='upper':
            line = functions.findupper(self.dataframe.index.tolist(), line)
            line = functions.findupper(self.dataframe.column.tolist(), line)
            return self.dataframe.loc[str(line), str(column)]
        elif method=='lower':
            line = functions.findlower(self.dataframe.index.tolist(), line)
            line = functions.findlower(self.dataframe.column.tolist(), line)
            return self.dataframe.loc[str(line), str(column)]
            


    def __str__(self):
        return 'Table name: {}\nTable Contents: \n {}'.format(self.name, self.dataframe)

class Idle():
    def __init__(self):
        self.series = None
        self.number_of_rolls = None
        self.rolls_diameter = None
        self.trough_angle = None
        self.scale = None
        self.admissible_load = None




    





