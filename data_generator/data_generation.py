import csv
import random
import string
import os
import re

# === Define MainOP and Option pattern data structures using RegEX ===
MAINOP_PATTERN = re.compile(r'^[A-Za-z0-9]{3}-[A-Za-z0-9]{5}$')
OPTION_PATTERN = re.compile(r'^[a-zA-Z0-9]{5,10}$')

# === Generate ramdom MainOP ===
def generate_mainop():
    # Create a random MainOP string. This can be duplicated but the check will be performed when data stored.
    part1 = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
    part2 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    value = f"{part1}-{part2}"
    return value if MAINOP_PATTERN.match(value) else generate_mainop()

def generate_options():
    options = set()
    # Option data can be generated up to 10
    num_options = random.randint(1, 10)
    while len(options) < num_options:
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
        if OPTION_PATTERN.match(value):
            options.add(value)
    # Generated Options are merged by comma
    return ",".join(options)

def generate_measure1():
    return round(random.uniform(0, 1), 5)

def generate_measure2():
    return round(random.uniform(-1, 1), 3)

# === Generate data ===
def generate_data_row():
    mainop = generate_mainop()
    option = generate_options()
    measure1 = generate_measure1()
    measure2 = generate_measure2()
    return (mainop, option, str(measure1), str(measure2))

# === Create and add data to CSV ===
def load_existing_data(filename):
    existing_data = set()
    existing_mainops = set()
    if os.path.exists(filename):
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) == 4:
                    existing_data.add(tuple(row))
                    #If MainOP exists in CSV file, handle it separately
                    existing_mainops.add(row[0])
    return existing_data, existing_mainops

def save_data(filename, data):
    file_exists = os.path.exists(filename)
    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # If newly create a CSV file and there is no header, create header
        if not file_exists:
            writer.writerow(["MainOP", "Option", "Measure1", "Measure2"])
        writer.writerows(data)

# === Main Logic. Default creation is 1000 ===
def generate_dataset(filename="generated_data.csv", num_rows=1000):
    existing_data, existing_mainops = load_existing_data(filename)
    new_data = set()

    while len(new_data) < num_rows:
        row = generate_data_row()
        mainop = row[0]
        # Exclude data if MainOp exists
        if mainop in existing_mainops:
            continue
        if row not in existing_data and row not in new_data:
            new_data.add(row)

    save_data(filename, new_data)
    print(f"{len(new_data)} rows generated and saved to {filename}")

if __name__ == "__main__":
    # Input generate data repeat times
    try:
        repeat = int(input("How many time repeat the data creation? (1~10): ").strip())
        if not (1 <= repeat <= 10):
            raise ValueError("Please input an integer between 1 and 10.")
    except ValueError:
        print("Entered a wrong number. This will execute onece because it is a default value")
        repeat = 1

    for i in range(repeat):
        print(f"\n=== Execute {i+1}time(s) ===")
        generate_dataset()
