"""
not None == not False == not "" == not 0 == not [] == not {} == not ()

None != False (False是0，是int类型)
None != ""
None != 0
None != []
None != {}
None != ()

if not x，在变量为0、字符串为空、列表/字典/元组为空的时候都能使用。
if x is not None,只有在x为None的时候使用。
"""
# x = None
# x = False
x = ""
# x = 0
# x = []
# x = {}
# x = ()

# if not x，在变量为0、列表/字典/元组为空的时候都能使用。
if not x:  # None、False、""、0、[]、{}、()都行
    print("aaa")
else:
    print("-aaa")

# if x is None,只有在x为None的时候使用。
if x is not None:  # None
    print("bbb")
else:
    print("-bbb")
