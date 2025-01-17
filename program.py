
import pandas as pd
import matplotlib.pyplot as plt
import csv

def create_csv(filename,headers,rows):
    with open (filename,mode='a',newline='')as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
        print(f"csv file '{filename}' created successfully")


filename = "expense.csv"
headers = ["category", "Amount", "date"]
rows = []

print("1. Log expense")
print("2. Analyse data")
print("3. Visualize data")
print("4. Exit")

def Log_expense():
    Category = input("Enter the category (e.g. Food, Travel): ")
    Amount = float(input("Enter the amount: "))
    Date = input("Enter the date (dd_mm_yy): ")
    row = [Category, Amount, Date]
    create_csv(filename, headers, [row]) 

def Analyze_data():
    df = pd.read_csv(filename)  
    print("\nExpense Data:")
    print(df)

    total_amount = df["Amount"].sum()
    print("\nTotal Amount Spent:", total_amount)

def visualize_data():
    df = pd.read_csv(filename) 

    print("\nVisualizing data...")
    grouped_data = df.groupby('category')['Amount'].sum()
    grouped_data.plot(kind='bar', color='skyblue', figsize=(8, 5))
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

while True:
    ch = input("\nEnter your choice:")
    if ch == '1':
        Log_expense()
    elif ch == '2':
        Analyze_data()
    elif ch == '3':
        visualize_data()
    elif ch == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
