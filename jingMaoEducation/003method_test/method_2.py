# 导入模块测试

# 导入模块出现红线的解决方法：
# 右击文件夹，"Mark Directory As" --> "Sources Root"

# from method_1 import print_hello
#
# print_hello()
#
# ####################################################
#
# import method_1
#
# method_1.print_hello()
# method_1.print_i()


# 直接导入整个模块
import method_1
method_1.print_hello()
method_1.print_i()

# 导入模块中的具体函数
from method_1 import print_hello as hello
from method_1 import print_i
hello()
print_i()













