import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df["weight"]/((df["height"]/100)**2)).apply(lambda x : 1 if x>25 else 0)

df.loc[df['overweight'] < 25, 'overweight'] = 0
df.loc[df['overweight'] > 25, 'overweight'] = 1
# 3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = 'cardio', value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    #df_cat = None
    

    # 7
    catPlotfig = sns.catplot(data = df_cat, x="variable", hue = "value", kind = "count").set_axis_labels("variable", "total")


    # 8
    fig = catPlotfig.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # Clean the data
    
    df_heat = df.loc[(df.ap_lo <= df.ap_hi)
                 & (df.height >= df.height.quantile(0.025))
                 & (df.height <= df.height.quantile(0.975))
                 & (df.weight >= df.weight.quantile(0.025))
                 & (df.weight <= df.weight.quantile(0.975)), :]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots()
    sns.heatmap(
    corr.applymap(lambda x: 0 if abs(x) < 1e-8 else x),  # Elimina diferencias pequeñas
    annot=True,
    square=True,
    mask=mask,
    fmt=".1f",  # Asegura que los valores estén redondeados a un decimal
    cbar_kws={"shrink": 0.5}
    )

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig