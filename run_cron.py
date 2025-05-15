import pandas as pd
from datetime import datetime, timedelta

FILE_PATH = '/home/ubuntu/github/12周跑步训练计划.xlsx'

def load_plan():
    df = pd.read_excel(FILE_PATH)
    return df

def save_plan(df):
    df.to_excel(FILE_PATH, index=False)

def assign_dates(df, start_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    # 找到周一对应日期
    # 训练计划默认周一顺序，从周一开始往下排
    day_of_week_map = {'周一':0, '周二':1, '周三':2, '周四':3, '周五':4, '周六':5, '周日':6}
    
    # 给每条训练计算日期
    dates = []
    for _, row in df.iterrows():
        week = row['周数']
        weekday = row['星期']
        base_date = start_date + timedelta(days=(week-1)*7)
        offset = day_of_week_map[weekday]
        day_date = base_date + timedelta(days=offset)
        dates.append(day_date.strftime("%Y-%m-%d"))
    df['日期'] = dates
    return df

def get_today_plan(df, today_str):
    today_plan = df[df['日期'] == today_str]
    if today_plan.empty:
        print(f"{today_str} 今天没有训练任务。")
        return None
    else:
        print(f"{today_str} 的训练计划：")
        for _, row in today_plan.iterrows():
            print(f"- {row['星期']}：{row['训练内容']}，距离 {row['距离(公里)']} 公里，配速 {row['配速（分/公里）']}, 心率 {row['心率区间']}")
        return today_plan

def postpone_plan(df, today_str):
    # 今天没完成，所有日期 >= 今天的都推迟一天
    df['日期'] = pd.to_datetime(df['日期'])
    today_date = datetime.strptime(today_str, "%Y-%m-%d")
    df.loc[df['日期'] >= today_date, '日期'] = df.loc[df['日期'] >= today_date, '日期'] + timedelta(days=1)
    df['日期'] = df['日期'].dt.strftime("%Y-%m-%d")
    print("训练计划已顺延一天。")
    return df

def main():
    df = load_plan()

    # 如果第一次运行没有日期，先让用户输入开始日期
    if df['日期'].isnull().all():
        start_date = input("请输入训练计划开始日期（格式：YYYY-MM-DD）：")
        df = assign_dates(df, start_date)
        save_plan(df)
        print("日期分配完成，已保存。")

    today_str = datetime.now().strftime("%Y-%m-%d")
    today_plan = get_today_plan(df, today_str)
    if today_plan is None:
        return

    #completed = input("今天训练完成了吗？（y/n）：").strip().lower()
    #if completed == 'y':
    #    print("继续加油！")
    #else:
    #    df = postpone_plan(df, today_str)
    #    save_plan(df)

if __name__ == "__main__":
    main()

