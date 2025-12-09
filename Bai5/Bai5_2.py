import datetime as dt

# Định dạng chuỗi thời gian
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển chuỗi thành datetime object
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In ra ngày, tháng, phút, giây
print('Day:', t1.day)        # 12
print('Month:', t1.month)    # 10
print('Minute:', t1.minute)  # 45
print('Second:', t1.second)  # 52

# Thời gian hiện tại
t2 = dt.datetime.now()

# Tính hiệu số thời gian
diff = t2 - t1  # diff là timedelta object

# In số ngày chênh lệch
print('How many days difference?', diff.days)
