import json

if __name__ == '__main__':

    chinese_numbers = {
        "one": "一",
        "two": "二",
        "three": "三",
        "four": "四",
        "five": "五",
        "six": "六",
        "seven": "七",
        "eight": "八",
        "nine": "九",
        "ten": "十"
    }

    print("Let's print chinese FIVE")
    print(chinese_numbers["five"])
    print("Time for all numbers 1-10:")
    print(json.dumps(chinese_numbers))