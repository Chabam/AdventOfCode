print("Enter the spreadsheet then press ctrl-c :\n")

spreadSheet = []

# A loop to get all the spread sheet even with the "\n"
while True:
    try:
        spreadSheetRow = input()
        # This rather scary line basically splits the string into a list converted to int
        spreadSheet.append(list(map(int, spreadSheetRow.split())))
    except KeyboardInterrupt:
        break

checksum = 0

# We check each row summing the minimum and maximum value
for row in spreadSheet:
    checksum += int(max(row)) - int(min(row))

print(checksum)