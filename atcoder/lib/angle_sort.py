from functools import cmp_to_key


def angle_cmp(a, b):
    """a が先なら -1、b が先なら 1、同じ座標なら 0"""
    ax, ay = a
    bx, by = b

    # 前半: 右方向から、上を通って左方向の直前まで
    # 後半: 左方向から、下を通って右方向の直前まで
    a_lower = ay < 0 or (ay == 0 and ax < 0)
    b_lower = by < 0 or (by == 0 and bx < 0)

    if a_lower != b_lower:
        return 1 if a_lower else -1

    # 同じ半分にある場合、外積で角度を比較する
    cross = ax * by - ay * bx

    if cross > 0:
        return -1
    if cross < 0:
        return 1

    # 同じ方向なら、原点に近い点を先にする
    distance_a = ax * ax + ay * ay
    distance_b = bx * bx + by * by

    if distance_a < distance_b:
        return -1
    if distance_a > distance_b:
        return 1

    return 0


def angle_sort(points):
    """
    右方向を始点として、反時計回りに並べる。
    同じ方向なら近い順。原点 (0, 0) は先頭。
    元のリストは変更せず、新しいリストを返す。
    計算量: O(N log N)
    """
    return sorted(points, key=cmp_to_key(angle_cmp))


def is_same_dir(a, b):
    """原点から見て同じ方向か。原点が含まれる場合は False"""
    ax, ay = a
    bx, by = b

    cross = ax * by - ay * bx
    dot = ax * bx + ay * by

    return cross == 0 and dot > 0


import math

if __name__ == "__main__":
    points = [
        (2, 2),
        (0, -1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, 0),
        (1, -1),
        (-1, 1),
        (0, 1),
        (1, 1),
        (3, 0),
    ]

    print("ソート前:")
    print(points)

    sorted_points = angle_sort(points)

    print("\nソート後:")
    print(sorted_points)

    print("\n各点の角度（右方向が 0 度、反時計回り）:")
    for i, (x, y) in enumerate(sorted_points):
        if x == 0 and y == 0:
            print(f"{i}: {(x, y)} → 原点なので角度は未定義")
        else:
            angle = math.degrees(math.atan2(y, x)) % 360
            print(f"{i}: {(x, y)} → {angle:.3f} 度")

    print("\n同じ方向か:")
    print("(1, 1) と (2, 2):", is_same_dir((1, 1), (2, 2)))
    print("(1, 1) と (-1, -1):", is_same_dir((1, 1), (-1, -1)))
