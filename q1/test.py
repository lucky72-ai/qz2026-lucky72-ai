from main import analyze_log
with open("app.jsonl", "w", encoding="utf-8") as f:
    f.write('{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "用户登录成功", "user": "张三"}\n')
    f.write('{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "数据库连接失败", "user": "李四"}\n')
    f.write('{"timestamp": "2026-10-01 10:25:12", "level": "INFO", "message": "用户登出", "user": "张三"}\n')
    f.write('{"timestamp": "2026-10-01 10:26:30", "level": "ERROR", "message": "超时", "user": "李四"}\n')
    f.write('{"timestamp": "2026-10-01 10:27:00", "level": "INFO", "message": "任务完成", "user": "王五"}\n')
result = analyze_log("app.jsonl")
print("运行结果：")
print(result)