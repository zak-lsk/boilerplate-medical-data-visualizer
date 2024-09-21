import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = df['weight'] / ((df['height'] / 100) **2)
df_copy=df.copy()
radice=df_copy['height']**2
df_copy['weight']=df_copy['weight'].astype(int)
df_copy['overweight']=df_copy['weight']/radice

df_copy.loc[df_copy['overweight'] < 25, 'overweight'] = 0
df_copy.loc[df_copy['overweight'] > 25, 'overweight'] = 1
# 3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0

# 4
def draw_cat_plot():
    # 5
    df_cat = None


    # 6
    df_cat = None
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
