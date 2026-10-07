# 编程题 2：用户管理器

> **硬性要求：本题必须完成。** 未完成的编程题不进入部门筛选流程。

## 题目描述

实现一个用户管理类，管理用户数据的增删查改，并支持 JSON 文件持久化。

每个用户是一个字典，形如 `{"id": 1, "name": "张三", "age": 18}`。`id` 由管理器自动分配，从 1 开始递增。

## 功能要求

该类需支持以下功能（方法命名、参数设计由你决定，需符合 Python 命名规范）：

- 添加用户（传入姓名和年龄），自动分配 id，返回该用户字典
- 按 id 查询用户，不存在返回 `None`
- 修改指定用户的年龄，成功返回 `True`，用户不存在返回 `False`
- 删除指定用户，成功返回 `True`，用户不存在返回 `False`
- 列出所有用户（按添加顺序）
- 将所有用户保存为 JSON 文件
- 从 JSON 文件加载用户，覆盖当前数据

## 行为示例

```
um = UserManager()
um.add_user("张三", 18)    →  {"id": 1, "name": "张三", "age": 18}
um.add_user("李四", 20)    →  {"id": 2, "name": "李四", "age": 20}
um.get_user(1)            →  {"id": 1, "name": "张三", "age": 18}
um.get_user(99)           →  None
um.update_age(1, 19)      →  True
um.remove_user(2)         →  True
um.remove_user(2)         →  False
um.list_users()           →  [{"id": 1, "name": "张三", "age": 19}]
um.save_to_json("users.json")
um2 = UserManager()
um2.load_from_json("users.json")
um2.list_users()          →  [{"id": 1, "name": "张三", "age": 19}]
```

## 约束与要求

- 语言：Python 3
- 实现文件：`main.py`（本目录下）
- 保存/加载必须使用 `json.dump` / `json.load`
- 文件操作必须指定 `encoding="utf-8"`，`ensure_ascii=False`
- 从文件加载后，后续添加用户的 id 应接续已加载的最大 id
- 不得引入第三方库（标准库 `json`、`os` 可用）
- 如有测试脚本，放在 `test.py` 中（该项作为可选项，如果完成会视测试规范度和完成度有一定的加分）

## 提交要求

- 将代码放在本目录 `q2/` 下
- 必须包含 `main.py`，可执行或可被 import 后调用
- 如有测试脚本，放在 `test.py` 中（该项作为可选项，如果完成会视测试规范度和完成度有一定的加分）
- 保持过程性提交，最终代码需能直接运行
