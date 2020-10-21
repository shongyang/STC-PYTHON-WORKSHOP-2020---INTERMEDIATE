import csv

# Method A

try:
    with open("breakfast.csv", "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["index no", "food", "ounces"])
        wr.writerow(["", "bread", "5 ounces"])
        wr.writerow(["", "pancakes", "15 ounces"])
        wr.writerow(["", "nettle tea", "10 ounces"])
except:
    print("Alamak")
else:
    print("WooHooHoo!")

# Method B

try:
    with open("breakfast.csv", "w", newline="") as csvfile:
        fieldnames = ["index no", "food", "ounces"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({"index no": "", "food": "bread", "ounces": "5 ounces"})
        writer.writerow({"index no": "", "food": "pancakes", "ounces": "15 ounces"})
        writer.writerow({"index no": "", "food": "nettle tea", "ounces": "10 ounces"})
except:
    print("Alamak")

else:
    print("WooHooHoo!")