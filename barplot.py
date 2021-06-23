import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# dict ={'skill':['Python','Pandas','Numpy','Machine Learning','Deep Learning','NLP','Hadoop','Pyspark','Flask','AWS'],
       # 'expertise':[7,9,8,8,7,4,5,6,4,4]}

df=pd.read_csv("skill.csv")

sns.set_theme(style="darkgrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 5))


# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(y="Skill", x="Score", data=df,
            label="Technical skill", color="b")

ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 10), ylabel="",
       xlabel="Technical Skill")

sns.despine(left=True, bottom=True)
plt.savefig(r'images\barplot.png')
