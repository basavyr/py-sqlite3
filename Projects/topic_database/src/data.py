from random import uniform, randrange


class Data:
    """
    - generate random data as a list of arrays
    - Predefined values:
        * seed
        * number of random arrays within the final list of random data -> N_RANDOM_ARRAYS
        * the smallest possible length for an (individual/component) array 
        * the largest possbile length for an array
    """

    DEFAULT_SEED = 1
    N_RANDOM_ARRAYS = 10
    LEFT_LIMIT = 1
    RIGHT_LIMIT = 10

    def __init__(self):
        self.seed = Data.DEFAULT_SEED
        self.left_limit = Data.LEFT_LIMIT
        self.right_limit = Data.RIGHT_LIMIT
        self.dataSets = Data.N_RANDOM_ARRAYS

    def CreateRandomArray(self):
        """
        - generate an array with random elements
        - elements are given from a uniform data distribution
        - elements are confined within [-seed, seed] interval 
        - size of the array is given by a random integer 
        """

        rd_number = lambda: uniform(-self.seed, self.seed)
        rd_array_size = randrange(self.left_limit, self.right_limit)
        rd_array = [rd_number() for _ in range(rd_array_size)]

        return rd_array

    def GiveRandomData(self):
        """
        - Returns a bunch of random arrays (fixed number of arrays to be added within the final list)
        - the number of random arrays within the output data is given by the N_RANDOM_ARRAYS argument
        """
        random_data = []

        for data_idx in range(self.dataSets):
            rd_array = self.CreateRandomArray()
            random_data.append(rd_array)

        return random_data
