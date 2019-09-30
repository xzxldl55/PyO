# -*- coding -*-

from datetime import datetime

now = datetime.now()  # 获取时间,类型为datetime.datetime
dt = datetime(2019, 7, 22, 0, 0, 0)

# 转换为时间戳 --> 11位，小数位是毫秒
ts = dt.timestamp()
fts = datetime.fromtimestamp(ts)  # 将时间戳转换位datetime

# str转换为datetime
st = datetime.strptime('2019-7-22 19:00:00', '%Y-%m-%d %H:%M:%S')
print(st.strftime('%a, %b %d %H:%M'))  # datetime转str
# print(now, '\n', dt, '\n', ts, fts, st)
