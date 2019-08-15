"""
map(関数, イテラブル): すべての要素に処理を行う.
filter(関数, イテラブル): 条件に合う要素だけを抜き出す.
"""


# map関数 -------------------------------------------------------- #
def double(x):
    return x * 2


nums = [4, 3, 7, 6, 2, 1]

# ラムダ式を使わない場合
nums2 = list(map(double, nums))
print(nums2)

# ラムダ式を使う場合
nums2 = list(map(lambda x: x * 2, nums))
print(nums2)

# リスト内包表記でも書ける
nums2 = [double(num) for num in nums]
print(nums2)


# filter関数 -------------------------------------------------------- #
nums = [4, -3, 9, 1, -2, -4, 5]

# ラムダ式を使う場合
nums2 = list(filter(lambda x: x > 0, nums))
print(nums2)

# リスト内包表記でも書ける
nums2 = [num for num in nums if num > 0]
print(nums2)
