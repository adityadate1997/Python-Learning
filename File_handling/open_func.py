# Read a file
with open('./data.txt', 'r') as f:
    data = f.read()
    print(data)

# Write to file
# Overwrites the complete file
with open('./data.txt', 'w') as f:
    data = '4. Added some with py'
    f.write(data)
    print(data)