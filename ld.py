# Lists - Задание 1
numbers = [3, 5, 7, 9, 10.5]
print(numbers)
numbers.append("Python")
#print(numbers)
print(len(numbers))

# Lists - Задание 2
print(numbers[0])
print(numbers[-1])
print(numbers[2:5])
numbers.remove("Python")
#print(numbers)

# Dictionaries - Задание 1
city_temp = {"city": "Москва", "temperature": "20"}
print(city_temp["city"])
city_temp["temperature"] = int(city_temp["temperature"]) - 5
city_temp["temperature"] = str(city_temp["temperature"])
print(city_temp)

# Dictionaries - Задание 2
city_temp.get("country")
city_temp.get("country", "Россия")
city_temp["date"] = "27.05.2019"
#print(city_temp)
print(len(city_temp))