import wfdb

ann = wfdb.rdann("data/210", "atr")

print("Number of annotations:", len(ann.sample))

print("\nFirst 20 beat labels:")
print(ann.symbol[:20])

print("\nFirst 20 sample positions:")
print(ann.sample[:20])