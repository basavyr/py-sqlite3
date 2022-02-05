from random import uniform, randrange


class Data:
    """
    - generate random data as a list of arrays
    - Predefined values:
        * seed
        * number of random arrays within the final list of random data
        * the smallest possible length for an (individual/component) array 
        * the largest possbile length for an array
    """

    DEFAULT_SEED = 1
    N_DATA_SETS = 10

    def __init__(self):
        self.seed = Data.DEFAULT_SEED
        self.left_limit = 1
        self.right_limit = 10
        self.dataSets = Data.N_DATA_SETS

    def CreateRandomArray(self):
        """
        - generate an array with random elements
        - elements are given from a uniform data distribution
        - elements are confined within [-seed, seed] interval 
        - size of the array is given by a random integer 
        """
        give_rd_number = lambda: uniform(-self.seed, self.seed)
        rd_arr_size = randrange(self.left_limit, self.right_limit)
        rd_arr = [give_rd_number() for _ in range(rd_arr_size)]

        return rd_arr

    def GiveRandomData(self):
        """
        - declare an emptry array which will be updated with a bunch of random arrays
        - the number of random arrays within the data is given by the n argument
        """
        random_data = []

        for _ in range(self.N_DATA_SETS):
            rd_array = self.CreateRandomArray()
            random_data.append(rd_array)

        return random_data
