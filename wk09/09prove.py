f = open("census.txt", "r")
census = {}

# This was is probably even easier
for line in f:  # gets one line at a time from the file
    # print(line)  # we can print it or do anything else we want with it here
    words = line.split(",")
    education = words[3]
    #  print(education)
    if education not in census:
        census[education] = 1
    else:
        census[education] += 1

for k,v in census.items():
    print(v, k)
    