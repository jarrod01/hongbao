import random
import numpy as np

def hongbao_select(people, money, minimal=0.01):
    hongbaos = []
    money -= people * minimal
    if money == 0:
        return [minimal]*people
    elif money < 0:
        return []
    for i in range(people):
        average = money / (people - i)
        tmp_count = random.randrange(0, int(average*200), 1)
        tmp_count /= 100
        hongbaos.append(tmp_count)
        money -= tmp_count
    hongbaos = [i + minimal for i in hongbaos]
    return hongbaos


def result_analysis(hongbaos):
    hongbao_array = np.array(hongbaos)
    print('瓜分总金额：' + str(hongbao_array.sum()))
    print('最小值：' + str(hongbao_array.min()))
    print('最大值：' + str(hongbao_array.max()))
    print('平均值：' + str(hongbao_array.mean()))
    print('方差：' + str(hongbao_array.var()))
    print('标准差：' + str(hongbao_array.std()))


if __name__ == '__main__':
    people = int(input('请输入人数：'))
    money = float(input('请输入总金额：'))
    minimal = float(input('请输入每人最小金额：'))
    hongbaos = hongbao_select(people, money, minimal)
    if hongbaos:
        result_analysis(hongbaos)
    else:
        print('输入有误，钱不够分的！')
    # counts = 0
    # for i in range(10000):
    #     people = random.randint(20, 60)
    #     average = random.randint(50, 200)/100
    #     money = people * average
    #     minimal = 0.5
    #     hongbaos = hongbao_select(people, money, minimal)
    #     if hongbaos:
    #         hongbao_array = np.array(hongbaos)
    #         if hongbao_array.max() >= average*2:
    #             counts += 1
    # print(counts)