import matplotlib.pyplot as plt

labels = ['Non-offensive', 'Offensive']
counts = [500, 477]

plt.figure(figsize=(6,6))
plt.pie(counts, labels=labels, autopct='%1.1f%%')
plt.title("Dataset Distribution")
plt.savefig("outputs/figures/dataset_distribution.png", dpi=300)

