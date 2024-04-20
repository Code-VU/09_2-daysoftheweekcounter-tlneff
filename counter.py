def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    lines = []
    days = {}
    with open(file_name) as file:
        for line in file:
            lines.append(line)
    for line in lines:
        if line[:5] == "From ":
            day = line.split(' ')[2]
            days[day] = days.get(day, 0)+1
    print(days)


# if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
