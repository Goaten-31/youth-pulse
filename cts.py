import csv

with open('Teen_Mental_Health_Dataset.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)

    f = open("test.sql", "a")

    for row in reader:
        f.write(f"INSERT INTO teen_mental_health VALUES ({' '.join(row)});\n")

    f.close()