#kreis academy file操作

import string

s = """\

私の名前は $name です。
歳は　$age です。

"""

template = string.Template(s)
contents = template.substitute(name='近藤',age='20')
print(contents)