import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df[(df['value']>=df['value'].quantile(0.025)) & 
           (df['value']<=df['value'].quantile(0.975))]
df['date']=pd.to_datetime(df['date'])
df.set_index('date',inplace=True)

def draw_line_plot():
    # Draw line plot
  
    fig1 =df.plot(xlabel='Date',ylabel='Page Views',title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019').figure
    # Save image and return fig (don't change this part)
    fig1.savefig('line_plot.png')
    return fig1

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
   
    df['month']=df.index.month
    df['year']=df.index.year
    df_bar = df.groupby(['year','month'])['value'].mean()
    df_bar = df_bar.unstack()
  # Draw bar plot
    fig2 = df_bar.plot(legend=True,kind='bar',xlabel='Years',ylabel='Average Page Views').figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig2.savefig('bar_plot.png')
    return fig2

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_a=df_box.sort_values('month')[['month','value']]
    df_b=df_box.sort_values('year')[['year','value']]
    # Draw box plots (using Seaborn)
    fig3, axes = plt.subplots(1, 2)
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(ax=axes[1],x='month',y='value',data=df_a,order=month_order)
    sns.boxplot(ax=axes[0],x='year',y='value',data=df_b)
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig3.savefig('box_plot.png')
    return fig3
