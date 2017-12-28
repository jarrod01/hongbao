import random
import matplotlib.pyplot as plt
import numpy as np

def count_select(people, money):
    counts = []
    for i in range(people):
        average = money / (people - i + 1)
        tmp_count = random.randrange(1, int(average*200), 1)
        tmp_count /= 100
        counts.append(tmp_count)
        money -= tmp_count
    return counts

if __name__ == '__main__':
    people = 5000
    money = 1000
    counts = count_select(people, money)
    nums = list(set(counts))
    nums.sort()
    nums_count = []
    for num in nums:
        nums_count.append(counts.count(num))
    print('mean: ' + str(sum(counts)/people))
    plt.title('各红包值的次数')
    plt.xlabel('红包值')
    plt.ylabel('次数')
    plt.plot(nums, nums_count)
    plt.show()