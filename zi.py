N = 5

# children[v]: 頂点 v の子の一覧
children = [[1, 2], [3, 4], [], [], []]

tin = [0] * N
tout = [0] * N
tour = []


def dfs(v):
    tin[v] = len(tour)
    tour.append(v)
    print(f"入る v={v}: tin[{v}]={tin[v]}, tour={tour}")

    for w in children[v]:
        dfs(w)

    tout[v] = len(tour)
    print(f"出る v={v}: tout[{v}]={tout[v]}, tour={tour}")


dfs(0)

print("tin  =", tin)
print("tout =", tout)
print("tour =", tour)
