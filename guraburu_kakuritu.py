'''
10連 : 40% -> 400 (601~1000)
20連 : 40% -> 400 (201~600)
30連 : 18.5% -> 185 (16~200)
100連 : 1.5% -> 15 (1~15)
のガチャを14回した時
11回連続で100連を引けない確率

1回のガチャにおいて
SSR : 6%
その他 : 94%

最終日までにSSRを引く期待値(知りたい)

人数設定 : 40万人

1~3日の間はSSRの確率が6% 4~14の間はSSRの確率が3%
'''
import random

# ガチャの回数抽選
def kaisuu_gacha(day):
    # print(random.randint(1, 1000))
    result = {"10" : 0,
              "20" : 0,
              "30" : 0,
              "100": 0}

    for i in range(day):
        # 最終日前日までの判定
        # 天井であるならば
        if(i == 13 and result['100'] == 0):
            result['100'] = result['100'] + 1

        else:
            tmp = random.randint(1, 1000)
            if(tmp <= 15):
                result['100'] = result['100'] + 1
            elif(tmp >= 16 and tmp <= 200):
                result['30'] = result['30'] + 1
            elif(tmp >= 201 and tmp <= 600):
                result['20'] = result['20'] + 1
            else:
                result['10'] = result['10'] + 1

        if(i == 2):
            gekiatsu_num = result['10'] * 10 + \
                           result['20'] * 20 + \
                           result['30'] * 30 + \
                           result['100'] * 100

    return result, gekiatsu_num

# SSRの抽選関数, geki
def SSR_gacha(r, gekiatsu_num):
    # その人は何回ガチャを引けるか計算
    result = {"atari" : 0,
              "hazure" : 0}
    kaisuu_num = r['10'] * 10 + r['20'] * 20 + r['30'] * 30 + r['100'] * 100

    # ガチャ回数からSSR(3% or 6%)が出るかシミュレート
    for i in range(kaisuu_num):
        tmp = random.randint(1, 100)
        # 確率設定
        if(i < gekiatsu_num):
            kakuritsu = 6
        else:
            kakuritsu = 3

        if(tmp <= kakuritsu):
            result['atari'] = result['atari'] + 1
        else:
            result['hazure'] = result['hazure'] + 1

    # SSRの的中率
    # return result['atari'] / kaisuu_num * 100

    # SSRの出現数
    return result['atari']


## main
day = 14
user_num = 100000
one_kakutiru = 0.0
all_kakuritu = 0.0

for i in range(user_num):
    kaisuu_result, gekiatsu_num = kaisuu_gacha(day)
    one_kakuritu = SSR_gacha(kaisuu_result, gekiatsu_num)
    all_kakuritu = all_kakuritu + one_kakuritu
    one_kakuritu = 0.0

print(all_kakuritu / user_num)
