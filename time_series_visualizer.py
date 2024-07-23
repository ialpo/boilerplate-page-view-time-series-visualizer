import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv ( 'fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'] )

# Clean data
df = df.loc [ ( df['value'] >= df['value'].quantile(0.025) ) &
              ( df['value'] <= df['value'].quantile(0.975) ) ]

def draw_line_plot():
    fig, ax = plt.subplots( figsize=(10,5) )

    ax.plot ( df.index, df['value'], 'r', linewidth = 1 )

    ax.set_title ( 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019' )
    ax.set_xlabel ( 'Date' )
    ax.set_ylabel ( 'Page Views' )

    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df['Month'] = df.index.month
    df['Year']  = df.index.year

    df_bar = df.groupby( ['Year', 'Month'] )['value'].mean()
    df_bar = df_bar.unstack()

    fig = df_bar.plot.bar ( legend=True, figsize=(7,7) ) 

    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xticks()
    plt.yticks()

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month-num'] = df_box['date'].dt.month

    df_box = df_box.sort_values ( 'month-num' )

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots ( nrows= 1, ncols = 2, figsize = (12,6) )
    
    ax[0]= sns.boxplot(x=df_box['year'], y=df_box['value'], ax = ax[0])
    ax[1]= sns.boxplot(x=df_box['month'], y=df_box['value'], ax = ax[1])    
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')    
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()