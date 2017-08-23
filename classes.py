import pandas as pd

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
        self.weight_specific = None
        self.lenght = None
        self.width = None
        self.width_sm = None

class Material():

    def __init__(self):
        self.name = None
        self.density = None
        self.lumpsize = None
        self.inflamabe = None

    @property
    def max_lumpsize(self):
        return max(self.lumpsize)
    


class Table():
    def __init__(self, filename=None):

        self.dataframe = None
        self.name = None
        if filename:
            self.load_data(filename)


    def load_data(self, file):
        try:
            self.dataframe = pd.read_csv(file, index_col=1)
        except Exception as e:
            print('Error loading file {}. {}'.format(file,e))



    def get_value(self, line, column, precise=True):
        return None






