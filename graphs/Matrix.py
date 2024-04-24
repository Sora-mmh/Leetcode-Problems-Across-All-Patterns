def find_lvl_combinations(lvl):
    l1, l2 = [e for e in range(lvl)], [e for e in range(lvl)]
    l1.append(lvl)
    l2.append(lvl)
    combinations = [(e1, e2) for e1 in l1 for e2 in l2 if e1 + e2 == lvl]
    return combinations


def get_levels(mat):
    import numpy as np

    m, n = len(mat), len(mat[0])
    updated_mat = []
    lvl = 1

    neighbors_per_lvl = find_lvl_combinations(lvl)
    for i in range(m):
        for j in range(n):
            lvl_neighbors_indices = [
                (i + ii, j + jj)
                for (ii, jj) in neighbors_per_lvl
                if (i + ii >= 0 and i + ii < m) and (j + jj >= 0 and j + jj < n)
            ]
            lvl_neighbors = [
                mat[i + ii][j + jj]
                for (ii, jj) in neighbors_per_lvl
                if (i + ii >= 0 and i + ii < m) and (j + jj >= 0 and j + jj < n)
            ]
            print(f"{i,j}", lvl_neighbors_indices)
            # if 0 in lvl_neighbors:
            #     updated_mat.append(lvl)
            # else:
            #     while 0 not in lvl_neighbors:
            #         lvl =+ 1
            #         neighbors_per_lvl = find_lvl_combinations(lvl)
            #     updated_mat.append(0)
    print(updated_mat)
