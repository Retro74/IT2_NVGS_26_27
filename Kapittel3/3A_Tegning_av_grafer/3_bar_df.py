import matplotlib.pyplot as plt, pandas as pd

data = {"Bynavn": ["Oslo", "Bergen", "Trondheim", "Harstad"],
        "Innbyggertall": [681067, 280216, 171322, 26431]}

by_innb_df = pd.DataFrame(data)

farger = plt.cm.autumn([i/(len(by_innb_df)-1) for i in range(len(by_innb_df))])

#print(by_innb_df)
plt.bar(by_innb_df["Bynavn"], by_innb_df["Innbyggertall"], color=farger)
plt.show()