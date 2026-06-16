class Searching:

    @staticmethod
    def linear_search(crop_list, target):
        for i in range(len(crop_list)):
            if crop_list[i] == target:
                return i
        return -1