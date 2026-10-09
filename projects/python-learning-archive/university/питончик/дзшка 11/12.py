def sum_decorator(func):
    def wrapper(self):
        return func(self)
    return wrapper


class Class:
    def __init__(self, nums):
        self.nums = nums
        self.solution = []

    def removeDuplicates(self):
        if not self.nums:
            return

        self.solution = [self.nums[0]]
        for i in range(1, len(self.nums)):
            if self.nums[i] != self.nums[i - 1]:
                self.solution.append(self.nums[i])

    def print(self):
        print(self.solution)

    @sum_decorator
    def all_sum(self):
        return sum(self.solution)



a = Class([0, 1, 1, 2, 2, 3, 4])
a.removeDuplicates()
a.print()
print(a.all_sum())



b = Class([0, 1, 1, 3, 3, 4, 4, 4, 4, 5])
b.removeDuplicates()
b.print()          
print(b.all_sum()) 
