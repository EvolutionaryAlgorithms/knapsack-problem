from app.knapsack import knapsack
from app.read_from_file import ReadFromFile

capacity, amount, values, weights = ReadFromFile.read()

print("Total value =", knapsack(capacity, amount, values, weights))

