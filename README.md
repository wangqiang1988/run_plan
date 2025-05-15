# run_plan
### 生成训练计划和页面
说明：跑步计划生成excel，并且页面化excel可进行完成后备注、延期调整。  
可将计划每日推送到微信或其他程序方便查看、并通过页面进行备注、调整训练日期。  
调整训练计划可直接对excel进行调整。  
### 方法
1.使用create_run_plan_excel.py生成跑步计划excel。  
2.使用run_cron.py对跑步计划进行生效，设定开始执行日期。  
3.运行app.py (flask)  
4.打开页面即可看到跑步计划  
### 运行
```
pip3 install pandas openpy openpyxl flask
python3 create_run_plan_excel.py
python3 run_cron.py
python3 app.py
浏览器打开 http://127.0.0.1:5000/
```
