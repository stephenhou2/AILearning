import json
from io import StringIO

d = dict(name='Bob', age=20, score=88)
f = StringIO()

json.dump(d, f)
f.seek(0)
s = f.read()
# s = f.getvalue()
f.close()

print(s)