numbers = [10, 20, 10, 40, 50, 60, 70]


class Sum_pair:
    def __init__(self, arr):
        for i, num in enumerate(numbers):
            for j, num2 in enumerate(numbers):
                if num+num2 == 50:
                    print(i,",",j)
                    return


sum_pair = Sum_pair(numbers)
