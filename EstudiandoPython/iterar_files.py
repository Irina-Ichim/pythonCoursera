# with open("lucky.txt") as file:
#      for line in file:
#           print(line.upper())
        
# with open("lucky.txt") as file:
#     for line in file:
#         cleaned_line = line.strip().upper()
#         print(cleaned_line)
        
file = open("lucky.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
