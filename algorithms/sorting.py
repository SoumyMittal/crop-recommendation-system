class Sorting:

    @staticmethod
    def bubble_sort_descending(arr):

        n = len(arr)

        for i in range(n):

            for j in range(0, n - i - 1):

                if arr[j][1] < arr[j + 1][1]:

                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr