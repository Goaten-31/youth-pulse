import os
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine


def bar_plot(df, x, y):
    fig, ax = plt.subplots()
    ax.bar(df[x], df[y])
    ax.set_ylim(0, 4)

    ax.axhline(y=max(df[y]), color='red', linestyle='--', linewidth=0.5)
    ax.axhline(y=min(df[y]), color='green', linestyle='--', linewidth=0.5)

    plt.title(f'{y} by {x}')
    return fig

def exp_bar_plot(df):
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df['Sleep Hours'],
        y=df['Weakest GPA'],
        name='Lowest GPA',
        marker_color='cyan',
        customdata = df['Weakest GPA'],
        hovertemplate = 'Min GPA: %{customdata}',
        opacity = 0.4
    ))

    fig.add_trace(go.Bar(
        x=df['Sleep Hours'],
        y=df['Academic Performance'],
        name='Average GPA',
        marker_color='lightblue',
        customdata=df['Academic Performance'],
        hovertemplate='Average GPA: %{customdata}',
        opacity = 0.6
    ))

    fig.add_trace(go.Bar(
        x=df['Sleep Hours'],
        y=df['Strongest GPA'],
        name='Highest GPA',
        marker_color='blue',
        customdata=df['Strongest GPA'],
        hovertemplate='Max GPA: %{customdata}',
        opacity = 0.4
    ))
    fig.update_layout(
        barmode='overlay',
        title='Average GPA by Sleep Hours',
        xaxis_title='Hours of Sleep',
        yaxis_title='Academic Performance in GPA',
        yaxis_range=(0, 4),
        showlegend=False
    )
    return fig

def exp_scatter_plot(df):
    fig = px.scatter(df, x='Sleep Hours',
                     y='Academic Performance',
                     size='Academic Performance',
                     hover_name='Academic Performance')

    fig.update_layout(yaxis_range=(0, 4),
                      title='Average GPA by Sleep Hours (Scatter Plot)')

    return fig

def correct_title(title : str):
    title = title.split('_')
    title = list(map(str.capitalize, title))
    title = ' '.join(title)
    return title

def get_engine():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db = os.getenv('DB_NAME')

    url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    engine = create_engine(url)
    return engine