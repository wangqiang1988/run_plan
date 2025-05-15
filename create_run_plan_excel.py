import pandas as pd

# 训练计划数据列表（只列出了前2周样例，后面按规律延续）
data = []
weeks = 12
weekdays = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

for week in range(1, weeks+1):
    data.append([week, '周一', '轻松跑', 5, '7:30 - 8:00', '126-150', '', ''])
    data.append([week, '周二', '休息/力量训练', '', '', '', '', ''])
    data.append([week, '周三', '节奏跑', 4, '6:10 - 6:40', '160-175', '', '心率偏高'])
    data.append([week, '周四', '轻松跑', 5, '7:30 - 8:00', '126-150', '', ''])
    data.append([week, '周五', '休息', '', '', '', '', ''])
    data.append([week, '周六', '长距离慢跑', 7 + (week - 1) * 0.5, '7:40 - 8:10', '135-155', '', ''])
    data.append([week, '周日', '休息', '', '', '', '', ''])

df_plan = pd.DataFrame(data, columns=['周数', '星期', '训练内容', '距离(公里)', '配速（分/公里）', '心率区间', '日期', '备注'])

# 保存成Excel文件
file_path = '/home/ubuntu/github/12周跑步训练计划.xlsx'
df_plan.to_excel(file_path, index=False)
file_path

