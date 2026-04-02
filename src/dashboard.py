import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def plot_class_distribution(df, target_col):
    counts = df[target_col].value_counts().reset_index()
    counts.columns = [target_col, 'Count']
    fig = px.pie(counts, values='Count', names=target_col, title='Resistance Class Distribution',
                 color=target_col, color_discrete_map={'Resistant':'#ef4444', 'Susceptible':'#22c55e', 'Intermediate':'#eab308'})
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return fig

def plot_antibiotic_resistance(df, antibiotic_col='Antibiotic_Tested', target_col='Susceptibility'):
    if antibiotic_col in df.columns:
        counts = df.groupby([antibiotic_col, target_col]).size().reset_index(name='Count')
        fig = px.bar(counts, x=antibiotic_col, y='Count', color=target_col, 
                     title='Resistance by Antibiotic', barmode='stack',
                     color_discrete_map={'Resistant':'#ef4444', 'Susceptible':'#22c55e', 'Intermediate':'#eab308'})
        fig.update_layout(template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        return fig
    return None

def plot_feature_importance(fi_df):
    if fi_df is not None:
        fig = px.bar(fi_df.head(10), x='Importance', y='Feature', orientation='h',
                     title='Top 10 Feature Importances',
                     color='Importance', color_continuous_scale='Viridis')
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, template='plotly_dark',
                          paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        return fig
    return None
