import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col=['date'])

# Clean data
df = df[df['value'].between(df['value'].quantile(.025), df['value'].quantile(.975))]
months = ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November','December']

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,6))
    ax.plot(df, color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)
    df_pivot = pd.pivot_table(df_bar, values='value', index='year', columns='month',aggfunc=sum)

    # Draw bar plot
    ax = df_pivot.plot(kind='bar',figsize=(10,8))
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    fig = ax.get_figure()





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
    df_box['month_number'] = df.index.month
    df_box = df_box.sort_values('month_number')
    fig, ax = plt.subplots(1,2, figsize=(15,6))
    sns.boxplot(data=df_box, x='year', y ='value', ax = ax[0], palette='bright').set_title('Year-wise Box Plot (Trend)')
    ax[0].set(xlabel='Year',ylabel='Page Views')
    sns.boxplot(data=df_box, x='month', y ='value', ax = ax[1], palette='pastel').set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set(xlabel='Month',ylabel='Page Views')
    


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
