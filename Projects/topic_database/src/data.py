from random import uniform, randrange


class Data:
    DEFAULT_SEED = 1
    N_DATA_SETS = 100

    def __init__(self):
        self.seed = Data.DEFAULT_SEED
        self.left_limit = 1
        self.right_limit = 10
        self.dataSets = Data.N_DATA_SETS

    def CreateArray(self):
        """
        - generate an array with random elements
        - elements are given from a uniform data distribution
        - elements are confined within [-seed, seed] interval 
        - size of the array is given by a random integer 
        """
        rd = lambda: uniform(-self.seed, self.seed)
        rd_arr_size = randrange(self.left_limit, self.right_limit)
        rd_arr = [rd() for _ in range(rd_arr_size)]

        return rd_arr

    def GiveData(self):
        # declare an emptry array which will be updated with a bunch of random arrays
        # the number of random arrays within the data is given by the n argument
        data_sets = []

        for idx in range(self.N_DATA_SETS):
            arr_idx = self.CreateArray()
            data_sets.append(arr_idx)

        return data_sets


def main():
    data = Data()
    arrays = data.GiveData()
    for arr in arrays:
        print(arr)


if __name__ == '__main__':
    main()
