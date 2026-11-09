# W1 练习（2026-11-09 ~ 11-15）

## 本周目标
- Python 安装与 PATH、PyCharm + Python 解释器、venv 虚拟环境；
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
| grade.py | 成绩等级判定 | python grade.py |
| leap_year.py | 闰年判断 | python leap_year.py |
| guess_number.py | 猜数字游戏 | python guess_number.py |

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
- 用时： 0.5 小时

### 11/10 周二
- 完成：circle.py、profile.py、types_demo.py；bmi.py 加了单位和 BMI 输出
- 卡点：input 返回字符串，直接相加报 TypeError
- 解决：用 int() / float() 转换
- 用时：0.5 小时

### 11/11 周三
- 完成：grade.py、leap_year.py、guess_number.py
- 卡点：闰年 1900 一开始判断错了
- 解决：先判断能不能被 400 整除，再判断 100
- 用时：0.5 小时
