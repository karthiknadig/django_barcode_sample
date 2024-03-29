import re

data = [
    'M331.371,210.239',
    'c0,0.56-0.114,1.084-0.342,1.575',
    'c-0.229,0.49-0.57,0.919-1.025,1.287',
    'c-0.456,0.367-1.029,0.657-1.72,0.868',
    's-1.494,0.317-2.412,0.317',
    'c-0.509,0-0.964-0.015-1.368-0.043',
    'c-0.403-0.029-0.781-0.066-1.133-0.113',
    'v-1.531',
    'c0.403,0.07,0.83,0.124,1.279,0.162',
    'c0.448,0.038,0.907,0.057,1.376,0.057',
    'c0.638,0,1.183-0.057,1.636-0.171',
    'c0.452-0.114,0.821-0.278,1.107-0.493',
    'c0.287-0.215,0.495-0.476,0.625-0.781',
    's0.195-0.651,0.195-1.035',
    'c0-0.351-0.078-0.657-0.234-0.917',
    'c-0.156-0.261-0.376-0.479-0.659-0.654',
    's-0.621-0.307-1.015-0.395',
    'c-0.395-0.088-0.825-0.132-1.293-0.132',
    'h-1.455',
    'v-1.391',
    'h1.479',
    'c0.386,0,0.736-0.05,1.054-0.152',
    'c0.316-0.101,0.588-0.247,0.813-0.436',
    'c0.226-0.189,0.398-0.423,0.52-0.701',
    'c0.121-0.277,0.182-0.593,0.182-0.945',
    'c0-0.686-0.209-1.186-0.627-1.499',
    'c-0.417-0.313-1.03-0.47-1.84-0.47',
    'c-0.43,0-0.874,0.043-1.331,0.129',
    'c-0.456,0.086-0.946,0.215-1.468,0.387',
    'v-1.484',
    'c0.222-0.079,0.457-0.149,0.709-0.21',
    'c0.25-0.063,0.501-0.115,0.752-0.157',
    's0.5-0.075,0.748-0.098',
    'c0.247-0.023,0.485-0.035,0.713-0.035',
    'c0.678,0,1.274,0.074,1.789,0.22',
    's0.945,0.356,1.29,0.63',
    's0.606,0.606,0.782,0.997',
    'c0.176,0.392,0.264,0.831,0.264,1.32',
    'c0,0.73-0.188,1.342-0.563,1.837',
    's-0.889,0.89-1.54,1.183',
    'c0.331,0.052,0.658,0.156,0.98,0.313',
    'c0.321,0.156,0.611,0.355,0.868,0.6',
    'c0.257,0.243,0.465,0.531,0.624,0.862',
    'C331.291,209.469,331.371,209.836,331.371,210.239',
    'z',
    ]


regex = r"[-]?[0-9]+[\.]?[0-9]*"

x_min = 1000.000
y_min = 1000.000
y_max = -1000.00
x_max = -1000.00
(x, y) = list(float(s) for s in re.findall(regex, data[0]))

for d in data[1:]:
    if d[0] in ['Z', 'z']:
        continue
    nums = list(float(s) for s in re.findall(regex, d))
    if d[0] in ['M', 'S', 'C', 'Q', 'L', 'T']:
        nums = nums[-2:]
        x, y = nums

    if d[0] in ['m', 's', 'c', 'q', 'l', 't']:
        nums = nums[-2:]
        x1, y1 = nums
        x += x1
        y += y1

    if d[0] == 'v':
        y += nums[0]

    if d[0] == 'V':
        y = nums[0]

    if d[0] == 'h':
        x += nums[0]

    if d[0] == 'H':
        x = nums[0]

    x_min = x if x < x_min else x_min
    y_min = y if y < y_min else y_min
    x_max = x if x > x_max else x_max
    y_max = y if y > y_max else y_max

print([(x_min, y_min), (x_max, y_max)])
print((x_max-x_min, y_max-y_min))

for d in data:
    if d[0] in ['Z', 'z']:
        continue
    nums = list(float(s) for s in re.findall(regex, d))
    if d[0] in ['M', 'T', 'L']:
        x, y = nums
        v = [str(x-x_min), str(y-y_min)]
        print('%s%s' % (d[0], ','.join(v)))
    if d[0] in ['S', 'Q']:
        x2, y2, x, y = nums
        v = [str(x2-x_min), str(y2-y_min), str(x-x_min), str(y-y_min)]
        print('%s%s' % (d[0], ','.join(v)))
    if d[0] in ['C']:
        x1, y1, x2, y2, x, y = nums
        v = [str(x1-x_min), str(y1-y_min), str(x2-x_min), str(y2-y_min), str(x-x_min), str(y-y_min)]
        print('%s%s' % (d[0], ','.join(v)))
    if d[0] in ['V']:
        y = nums[0]
        print('%s%s' % (d[0], str(y-y_min)))
    if d[0] in ['H']:
        x = nums[0]
        print('%s%s' % (d[0], str(x-x_min)))
