from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from datetime import timedelta

app = Flask(__name__)
EXCEL_FILE = '/home/ubuntu/github/12周跑步训练计划.xlsx'

def load_plan():
    df = pd.read_excel(EXCEL_FILE, parse_dates=['日期'])
    df.fillna('', inplace=True)
    return df

def save_plan(df):
    df.to_excel(EXCEL_FILE, index=False)

@app.route('/')
def index():
    df = load_plan()
    plans = df.to_dict(orient='records')
    return render_template('index.html', plans=plans)


@app.route('/mark_complete/<int:row_id>', methods=['POST'])
def mark_complete(row_id):
    return render_template('remark.html', row_id=row_id)

@app.route('/submit_remark/<int:row_id>', methods=['POST'])
def submit_remark(row_id):
    remark = request.form['remark']
    df = load_plan()
    if 0 <= row_id < len(df):
        df.at[row_id, '备注'] = remark
        save_plan(df)
    return redirect(url_for('index'))

@app.route('/postpone/<int:row_id>', methods=['POST'])
def postpone(row_id):
    df = load_plan()
    if row_id < 0 or row_id >= len(df):
        return "Invalid record", 404
    
    # 延后当天及之后所有计划日期1天
    for i in range(row_id, len(df)):
        df.at[i, '日期'] += timedelta(days=1)
    save_plan(df)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
