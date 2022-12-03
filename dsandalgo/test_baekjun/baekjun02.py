# d = divmod(30,7)
# print(d)

#백준 2525번

# hour, minute = map(int, input().split())
# required_time = int(input())

# hour += required_time // 60
# minute += required_time % 60

# if minute >= 60:
#     hour += 1
#     minute -= 60
# if hour >= 24:
#     hour -= 24

# print(hour, minute)

#백준 2884 번

hour, minute = map(int, input().split())

minute -= 45

if minute < 0:
    minute = 60 + minute
    hour -= 1
    if hour < 0:
        hour = 24+ hour

print(hour, minute)