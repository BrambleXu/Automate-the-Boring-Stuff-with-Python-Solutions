"""
测试文件
---
Lists of books
Lists of 100 best books
Lists of banned books
Lists of The New York Times Fiction Best Sellers
Lists of The New York Times Non-Fiction Best Sellers
Publishers Weekly lists of bestselling novels in the United States
---

bulletPointAdder.py脚本将从剪贴板中取得文本，在每一行开始处加上星号和空格，然后将这段新的文本贴回到剪贴板。

你希望bulletPointAdder.py程序完成下列事情：

1．从剪贴板粘贴文本；

2．对它做一些处理；

3．将新的文本复制到剪贴板。

---
程序运行错误，搞懂原因了。
用print (line)查看输出的时候，发现
* Lists of books
* Lists of 100 best books
* Lists of banned books
* Lists of The New York Times Fiction Best Sellers
* Lists of The New York Times Non-Fiction Best Sellers
* Publishers Weekly lists of bestselling novels in the United States
每一句前面都有星号。但最后在记事本里paste的时候，发现前面还是没有星号。

因为我用的是line = '* ' + line, 这个语句是把新的*line复制给了line
并没有对原先的list里的每一个单项产生改变。也就是之前的是否会改变list自身的问题。
所以说这里不能用for line in lines.
必须得用for i in range(len(lines)),
对list里的每一个单项lines[i]+‘*’，才能把list更新
"""

# bulletPointAdder.py - Add Wikipedia bullet points to the start
# of each line of test on the clipboard

import pyperclip

text = pyperclip.paste()

# TODO: Separate lines and add stars.
lines = text.split('\n')
for line in lines:
    line = '* ' + line
    print (line)
text = '\n'.join(lines)

pyperclip.copy(text)
