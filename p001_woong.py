list = range(1000)
print sum(list[::3] + list[::5]) - sum(list[::15])
