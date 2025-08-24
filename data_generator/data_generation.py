"""
Tool name: Generate sample data for practice
Author: GiHwan Jo

Summary
- Consisted by 4 fields(MainOP, Option, Measure1, Measure2)
  - MainOP: String, length: 6~20, RegEx: ^[a-zA-Z0-9]{6,20}$
  - Option: String, Length: 5~10, multiple options up to 10, No duplication, concat by comma, RegEx: ^[a-zA-Z0-9]{5,10}$
  - Measure1: Float, 0~1.00000, decimal point 5
  - Measure2: Float, -1 to 1, decimal point 3
- Generate 1K rows and able to repeate up to 10
- Store to CSV
"""

import csv
import random
import string
import os
import re

# === Value structure RegEx ===
MAINOP_PATTERN = re.compile(r'^[a-zA-Z0-9]{6,20}$')
OPTION_PATTERN = re.compile(r'^[a-zA-Z0-9]{5,10}$')

# === Create random data ===
def generate_mainop():
    while True:
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 20)))
        if MAINOP_PATTERN.match(value):
            return value

def generate_options():
    options = set()
    num_options = random.randint(1, 10)  # up to 10
    while len(options) < num_options:
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
        if OPTION_PATTERN.match(value):
            options.add(value)
    return ",".join(options)  # separating options by comma

def generate_measure1():
    return round(random.uniform(0, 1), 5)

def generate_measure2():
    return round(random.uniform(-1, 1), 3)

# === 데이터 생성 ===
def generate_data_row(existing_data):
    mainop = generate_mainop()
    option = generate_options()
    measure1 = generate_measure1()
    measure2 = generate_measure2()
    return (mainop, option, str(measure1), str(measure2))

# === CSV 관리 ===
def load_existing_data(filename):
    existing_data = set()
    if os.path.exists(filename):
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) == 4:
                    existing_data.add(tuple(row))
    return existing_data

def save_data(filename, data):
    file_exists = os.path.exists(filename)
    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:  # Add header if it is not exist
            writer.writerow(["MainOP", "Option", "Measure1", "Measure2"])
        writer.writerows(data)

# === 메인 로직 ===
def generate_dataset(filename="generated_data.csv", num_rows=1000):
    existing_data = load_existing_data(filename)
    new_data = set()

    while len(new_data) < num_rows:
        row = generate_data_row(existing_data.union(new_data))
        if row not in existing_data and row not in new_data:
            new_data.add(row)

    save_data(filename, new_data)
    print(f"{len(new_data)} rows generated and saved to {filename}")

if __name__ == "__main__":
    # 사용자에게 실행 횟수 입력받기
    try:
        repeat = int(input("How many time repeat to generate sample data? (1~10): ").strip())
        if not (1 <= repeat <= 10):
            raise ValueError("Please input integer number between 1 and 10.")
    except ValueError as e:
        print("❌ Input a wrong number. The ddefault repeat number is 1.")
        repeat = 1

    for i in range(repeat):
        print(f"\n=== Repeat time: {i+1} ===")
        generate_dataset()
