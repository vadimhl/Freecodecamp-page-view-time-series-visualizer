import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np
np.float = np.float64
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
# filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value'] >=  df['value'].quantile(0.025)) & (df['value'] <=  df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 8) )
    plt.plot(df)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xticks(rotation=0, ha='center')
    plt.ylabel('Page Views');
    plt.xlabel('Date');

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar = df_bar.groupby(['year', 'month']).agg({'value':'mean'}).round(0)
    df_bar = df_bar.reset_index()
    print(df_bar)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(16, 8) )
    labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # sns.barplot(data=df_bar, x='year', y='value', hue='month', legend="full", palette='bright');
    sns.barplot(data=df_bar, x='year', y='value', hue='month', palette='bright');
    plt.ylabel('Average Page Views');
    plt.xlabel('Years')
    h, l = ax.get_legend_handles_labels()
    ax.legend(h, labels, title="Months")



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(figsize=(16, 8) )



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
