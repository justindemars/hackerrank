height, width = input().split()
height = int(height)
width = int(width) - 2

halfheight = height // 2

filler = '-'
design = '.|.'

# print(".|.".center(width, filler))

for i in range(halfheight):
    print((design*i).rjust(width//2, filler) + design + (design*i).ljust(width//2, filler))

print("WELCOME".center(width+2, filler))

for k in range(halfheight):
    print((design*(halfheight-k-1)).rjust(width//2, filler) + design + (design*(halfheight-k-1)).ljust(width//2, filler))