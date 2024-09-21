import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("medical_examination.csv")

df_copy=df.copy()
radice=df_copy['height']**2
df_copy['weight']=df_copy['weight'].astype(int)
df_copy['overweight']=df_copy['weight']/radice



df_copy.loc[df_copy['overweight'] < 25, 'overweight'] = 0
df_copy.loc[df_copy['overweight'] > 25, 'overweight'] = 1

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0

plt.clf()


catDF = pd.melt(df_copy, id_vars = "cardio", value_vars = ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

# Write melted Df to a file so we can eyeball it.
catDF.to_csv("CatPlot Meltdown.csv")
# Create the catplot.
plt.clf() 
catPlotObj = sns.catplot(x = "variable", hue = "value", col = "cardio", data = catDF, kind = "count").set_axis_labels("variable", "total")
fig = catPlotObj.fig  # The test requires a figure object not a calPlot object.
# if debugSw == True: # During testing we want to display the plot.
# 	plt.show()      # But this hangs execution until we dismiss the plot.
fig.savefig('catplot.png')  