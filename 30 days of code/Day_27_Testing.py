

from random import randint, shuffle

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        # complete this function

        arr = [14,76,34,5,37,7,64,6,25,41,4,3,56,35,2]
        return arr


    @staticmethod
    def get_expected_result():
        # complete this function
        arr = [14,76,34,5,37,7,64,6,25,41,4,3,56,35,2]
        return arr.index(min(arr))

class TestDataExactlyTwoDifferentMinimums():

    @staticmethod
    def get_array():
        # complete this function
        arr = [5,7,2,45,7,2,4,6,2,2,6,7,2,23,4,7,3,7,1,6,1]
        return arr

    @staticmethod
    def get_expected_result():
        # complete this function
        arr = [5,7,2,45,7,2,4,6,2,2,6,7,2,23,4,7,3,7,1,6,1]
        return arr.index(min(arr))

