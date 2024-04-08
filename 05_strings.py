# Immutability of strings
fact = "The moon has no atmosphere."
fact + "No sound can be heard on the moon."
print(fact)

two_fact = fact + "No sound can be heard on the moon."
print(two_fact)

# Multiline text
multiline = "Fatcs about the moon:\n There is no atmosphere.\n There is no sound"
print(multiline)

multiline = """Fatcs about the Moon:
  There is no atmosphere.
  There is no sound"""

print(multiline)



# String methods in Python

# 1) the method .title() returns the string in initial caps and can be used with a string directly:

print("temperature and facts about the moon".title()) 

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)


# 2) A common string method is .split(). Without arguments, the method will separate the string at every space.
temperature = "Daylight: 260 F Nighttime: -280 F"
temperature_list = temperature.split()
print(temperature_list)

temperature = "Daylight: 260 F\n Nighttime: -280 F"
temperature_list = temperature.split('\n')
print(temperature_list)


# 3) Search for a string
print("Moon" in "This text will describe facts and challenges with space travel")

print("Moon" in "This text will describe facts about the Moon")

temp = """Saturn has a daytime temp of -170 degrees celsius, while Mars has -28 Celsius"""
print(temp.find("Moon")) #The .find() method returns a -1 when the word isn't found, or it returns the index (the number representing the place in the string). This is how it would behave if you're searching for the word Mars:

print(temp.find("Mars"))

# Another way to search for content is to use the .count() method, which returns the total number of occurrences of a certain word in a string:

print(temp.count("Mars"))
print(temp.count("Moon"))


# 4) To do a case-insensitive comparison, you can convert a string to all lowercase letters by using the .lower() method:

print("The Moon And The Earth".lower())

print("The moon and the earth".upper())


# Check content

temp = "Mars Avg temp: -60 C"
parts = temp.split(':')
print(parts)
print(parts[-1])
print(len(parts))


# printing numeric value using for loop and "isnumeric()" function
mars_temp = "The highest temperature on Mars is about 30 C"
for i in mars_temp.split():
    if i.isnumeric():
        print(i)

# It might be surprising to learn that "-70".isnumeric() would return False. This is because all characters in the string would need to be numeric, and the dash (-) isn't numeric. If you need to check negative numbers in a string, the .isnumeric() method wouldn't work.

print("-60".startswith('-'))

if "30 C".endswith("C"):
    print("This temp is in celsius")


# Transform text

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))


text = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius"
print("Saturn" in text)
print("saturn" in text.lower())


moon_facts = ["The moon is drifting away from the Earth.", "On avg, the Moon is moving about 4cm every year."]
print('      '.join(moon_facts))