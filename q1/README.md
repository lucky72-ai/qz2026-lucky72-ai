# 编程题 1：JSON 日志管道

> **硬性要求：本题必须完成。** 未完成的编程题不进入部门筛选流程。

## 题目描述

生产环境的日志通常是 **JSON Lines** 格式（每行一个 JSON 对象），例如 `app.jsonl`：

```jsonl
{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "用户登录成功", "user": "张三"}
{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "数据库连接失败", "user": "李四"}
{"timestamp": "2026-10-01 10:25:12", "level": "INFO", "message": "用户登出", "user": "张三"}
{"timestamp": "2026-10-01 10:26:30", "level": "ERROR", "message": "超时", "user": "李四"}
{"timestamp": "2026-10-01 10:27:00", "level": "INFO", "message": "任务完成", "user": "王五"}
```

请写一个函数 `analyze_log(filepath)`，接收一个 `.jsonl` 文件路径，返回一个统计字典。

## 返回格式

```python
{
    "total": 5,                    # 成功解析的日志总条数
    "by_level": {                 # 按 level 统计条数
        "INFO": 3,
        "ERROR": 2,
    },
    "by_user": {                  # 按 user 统计条数
        "张三": 2,
        "李四": 2,
        "王五": 1,
    },
    "last_error": "超时",          # 最后一条 level 为 ERROR 的 message；无 ERROR 则为 None
}
```

## 示例

### 示例 1

输入文件 `app.jsonl`（内容如上）：

```python
result = analyze_log("app.jsonl")
print(result["total"])        # 5
print(result["by_level"])     # {'INFO': 3, 'ERROR': 2}
print(result["by_user"])      # {'张三': 2, '李四': 2, '王五': 1}
print(result["last_error"])   # 超时
```

### 示例 2：文件不存在

```python
result = analyze_log("not_exist.jsonl")
print(result)
# {'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
```

### 示例 3：空文件

```python
# 文件存在但内容为空
result = analyze_log("empty.jsonl")
print(result)
# {'total': 0, 'by_level': {}, 'by_user': {}, 'last_error': None}
```

### 示例 4：含格式错误的行

文件内容：

```jsonl
{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "ok", "user": "张三"}
这不是合法的 JSON
{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "失败", "user": "李四"}
```

```python
result = analyze_log("bad.jsonl")
print(result["total"])      # 2（跳过格式错误行）
print(result["by_level"])    # {'INFO': 1, 'ERROR': 1}
print(result["last_error"])  # 失败
```

## 约束与要求

- 语言：Python 3
- 实现文件：`main.py`（本目录下）
- 函数签名：`def analyze_log(filepath: str) -> dict:`
- 文件操作必须指定 `encoding="utf-8"`
- 文件不存在时返回空结果字典，**不得抛异常**
- 某行 `json.loads` 失败时跳过该行，**不得中断整个解析**
- 空文件返回空结果字典
- 每行 JSON 保证包含 `timestamp`、`level`、`message`、`user` 四个键（格式正确的行）
- 不得引入第三方库（标准库 `json`、`os` 可用）
- 如有测试脚本，放在 `test.py` 中（该项作为可选项，如果完成会视测试规范度和完成度有一定的加分）

## 提交要求

- 将代码放在本目录 `q1/` 下
- 必须包含 `main.py`，可执行或可被 import 后调用
- 如有测试脚本，放在 `test.py` 中（该项作为可选项，如果完成会视测试规范度和完成度有一定的加分）
- 保持过程性提交，最终代码需能直接运行
