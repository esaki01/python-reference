"""
クロージャ（関数閉包）: 関数の中の関数のこと.
"""


def circle_area_func(pi):

    def circle_area(radius):
        return pi * radius * radius

    return circle_area


cal = circle_area_func(3.14)
print(cal)
print(cal(10))
