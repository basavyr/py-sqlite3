from random import randrange, uniform
from datetime import datetime


class Room_Temp:
    """
    - generate a sequence of temperatures based on a uniform data distribution
    - the class initializes with a seed, representing the base value
    - another value representing the maximal variation between the base value is given at init time
    """

    MAX_TEMP_NUMBER = 100
    """
    number  of temperatures that are generated on a single list
    """

    def __init__(self, temp_seed, max_variation):
        self.seed = temp_seed
        self.delta = max_variation

    def giveRoomTemp(self):
        base_temp = self.seed

        rd_temp = uniform(self.seed - self.delta, self.seed + self.delta)
        return rd_temp

    def generateRoomTemps(self):
        temps = []

        for temp_id in range(Room_Temp.MAX_TEMP_NUMBER):
            random_temp = self.giveRoomTemp()
            temps.append(random_temp)

        return temps

    @staticmethod
    def generateDBEntry(idx, temp, topic):
        temp_tuple = (float(idx), float(temp), str(
            datetime.utcnow()), str(topic))
        return temp_tuple
