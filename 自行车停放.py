import numpy as np
import pandas as pd
from scipy.spatial import distance_matrix

# 假设停放点的位置数据
parking_points = np.array([[0, 0], [1, 2], [2, 1], [3, 3], [4, 1]])

# 计算停放点之间的距离矩阵
dist_matrix = distance_matrix(parking_points, parking_points)

# 转换为DataFrame以便于查看
df_dist = pd.DataFrame(dist_matrix, columns=['Point'+str(i) for i in range(len(parking_points))],
                       index=['Point'+str(i) for i in range(len(parking_points))])

print("停车点之间的距离矩阵：")
print(df_dist)

# 计算平均距离和方差等指标
avg_distance = np.mean(dist_matrix[np.triu_indices(len(parking_points), k=1)])
var_distance = np.var(dist_matrix[np.triu_indices(len(parking_points), k=1)])

print("\n平均距离：", avg_distance)
print("距离方差：", var_distance)

# 进一步的分析和建模可以根据具体需求进行扩展