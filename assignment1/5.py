s = input()

vowels = "aeiou"
count = 0

for char in s.lower():
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
