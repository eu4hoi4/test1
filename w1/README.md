# W1 练习（2026-11-09 ~ 11-15）

## 本周目标
- Python 安装与 PATH、VS Code + Python 扩展、venv 虚拟环境；
- 变量、数据类型、条件判断、while/for 循环、函数定义与参数；
- Git 安装与 init/add/commit/log。

## 文件说明
| 文件 | 作用 | 运行方式 |
|---|---|---|
| hello.py | 输入名字并问候 | python hello.py |
| temperature.py | 摄氏转华氏 | python temperature.py |
| bmi.py | 计算 BMI 并分类 | python bmi.py |
| circle.py | 圆面积与周长 | python circle.py |
| profile.py | 个人名片 | python profile.py |
| types_demo.py | 类型与转换演示 | python types_demo.py |
## 运行方法
1. 打开 PyCharm 底部的 Terminal（Alt+F12）
2. 进入 w1 目录：cd w1
3. 运行：python hello.py
（如果终端前面没有 (.venv)，先在项目根目录执行 .\.venv\Scripts\activate）

## 每日记录
### 11/09 周一
- 完成：环境验证、venv、hello、温度转换、BMI、首次 commit
- 卡点：PowerShell 激活 venv 报错
- 解决：执行 Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
- 用时：2 小时

### 11/10 周二
- 完成：circle.py、profile.py、types_demo.py；bmi.py 加了单位和 BMI 输出
- 卡点：input 返回字符串，直接相加报 TypeError
- 解决：用 int() / float() 转换
- 用时：2 小时

## 还不懂
- if __name__ == "__main__" 是什么意思
- 解释：只有当我直接运行这个文件时，才执行 main()；如果我是被别的文件 import 的，就不执行。
- git add 和 git commit 的区别
- 解释：git add：把工作区的改动放入暂存区（staging area）——"我要提交这些文件"；git commit：把暂存区的内容正式记录到仓库历史——"生成一个版本快照"。

## 明日计划
- 学变量与类型；写温度、BMI、圆面积三个小程序