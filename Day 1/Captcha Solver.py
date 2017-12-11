captcha = input("Captcha ? ")

sum = 0
prevDigit = ''

# Loop trough all the digit in the captcha
for digit in captcha:
    # If the previous digit is equal to the currentDigit
    if prevDigit == digit:
        # We add the value of this digit to the sum
        sum += int(digit)
    # Then we assign the value of the current digit to the previous for the next "Current digit"
    prevDigit = digit

# Finally we check if the first digit equals the last, we add it to the sum (circular list)
if (captcha[0] == captcha[len(captcha) - 1]):
    sum += int(captcha[0])

print(sum)