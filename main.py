
file_name = 'covid-19-data/mask-use/mask-use-by-county.csv'

lines = []

def sort(ret, sort_column):
    return sorted(ret, key = lambda x:x[sort_column])

f = open(file_name, 'r')
header = None
for line in f:
    if header is None:
        header = line,
        continue
    A = line.rstrip().split(",")
    lines.append(A)
f.close()

print(sort(lines, 3))
