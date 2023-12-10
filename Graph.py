import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
from  plotly.subplots  import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt



def Display_Sales_category(data):
  fig = make_subplots(rows=1, cols=2)
  fig.add_trace(go.Bar(x=data.index, y=data['Sales']),row=1, col=1)
  fig.add_trace(go.Bar(x=data.index, y=data['Profit']),row=1, col=2)
  fig.update_traces(name='Sales', row=1, col=1)
  fig.update_traces(name='Profit', row=1, col=2)
  fig.update_layout(
      title_text = '<b>Total sales and  profitability of each product category</b>',
      title_font_size = 25,
      title_font_family = "Liberation Serif",
      title_font_color="#5b5b5b",
      xaxis_title = '',
      yaxis_title = '',
      plot_bgcolor= 'white',
      bargap = 0.5,
  )

  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
  
def Display_Sales_cate_year(Data):
  data = Data['sum']['Sales']
  fig4 = px.bar(data, x=data.index, y=data.columns,barmode='group',color_discrete_sequence=['#a1a0a0','#a1a0a0','#03396c'])
  fig4.update_layout(
    title_text = "<b>The annual Sales growth for each product category</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    bargap = 0.5,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)



def Display_Profit_cate_year(Data):
  data = Data['sum']['Profit']
  fig4 = px.bar(data, x=data.index, y=data.columns,barmode='group',color_discrete_sequence=['#a1a0a0','#a1a0a0','#03396c'])
  fig4.update_layout(
    title_text = "<b>The annual profit growth for each product category</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    bargap = 0.5,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)


def DisplayCountry_category(Data, names='United States'):
  data = Data.loc[names]
  fig4 = px.bar(data, x=data.index, y=data.columns)
  fig4.update_layout(
    title_text = f"<b>The yearly sales growth for each product category in the {names}</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    bargap = 0.5,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)
  


def Display_sales_segment(Data):
  data = Data['Sales']['sum']
  fig4 = px.bar(data, x=data.index, y=data.values)
  fig4.update_layout(
    title_text = f"<b>The yearly Sales growth for each segment of customers</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    bargap = 0.6,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)
  
def Display_top_order_sales(Data):
  data = Data.head(30)
  fig4 = px.bar(data, x=data['Customer.ID'], y=data.Sales)
  fig4.update_layout(
    title_text = f"<b>The most customers with the highest order volumes</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    bargap = 0.2,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)
  

def Display_Sales_date_trend(Data,Data2):
  fig4 = make_subplots(rows=1, cols=1)
  fig4.add_trace(go.Line(x=Data.index, y=Data.Sales, line=dict(color='#b3cde0', width=2),name='Original Sales'))
  fig4.add_trace(go.Line(x=Data2.index, y=Data2.Sales, line=dict(color='#ae0001', width=4), name='Resampling Sales average 7 day'))
  fig4.update_layout(
    title_text = f"<b>Trend Sales Overview spanning from the commencement of 2011 to the conclusion of 2014</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    #bargap = 0.5,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)


def Display_Sales_year(Data):
  fig4 = px.line(Data, x=Data.index, y=Data.Sales, color_discrete_sequence=['#6497b1'],text=Data['Sales'].apply(lambda x: f'{x:,}'))
  #text=Data['Sales'].apply(lambda x: f'{x:,}')
  scatter_trace = go.Scatter(x=Data.index, y=Data.Sales, mode='markers', marker=dict(size=8, color='#005b96'), name='Sales',showlegend=False)
  fig4.add_trace(scatter_trace)
  fig4.update_traces(line=dict(width=5),
                    marker=dict(size=8,color='#005b96'),
                     textposition='bottom right')
  fig4.update_layout(
    title_text = f"<b>Yearly Sales Trend</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    #bargap = 0.5,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)
  

def Display_Quantity_sales(Data):
  fig = make_subplots(rows=1, cols=2)
  fig.add_trace(go.Bar(x=Data['Year'], y=Data['Sales']),row=1,col=1)
  fig.add_trace(go.Bar(x=Data['Year'], y=Data['Quantity']),row=1,col=2)
  #fig4 = px.bar(sales_qual_melted, x='Year', y='Value',barmode='group',color='Metric')
  fig.update_traces(name='Sales',row=1,col=1)
  fig.update_traces(name='Quantity',row=1,col=2)
  fig.update_layout(
    title_text = "<b>Total Sales and Quantity over year</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    bargap = 0.5,
  )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  

def Display_month_sales(Data):
  custom_colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
  fig4 = px.bar(Data, x=Data.index, y=Data.Sales,color_discrete_sequence=custom_colors)
  scatter_trace = go.Scatter(x=Data.index, y=Data.Sales, mode='lines+markers', marker=dict(color='#a00000'),showlegend=False)
  fig4.update_traces(marker_line_width=5)
  fig4.add_trace(scatter_trace)
  fig4.update_layout(
    title_text = f"<b>Monthly Sales Overview</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    bargap = 0.3,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)
  

def Display_avg_each_year(Data):
  fig4 = px.line(Data, x=Data.index, y=Data.Sales)
  scatter_trace = go.Scatter(x=Data.index,  y=Data.Sales, mode='markers', marker=dict(size=10, color='#3483ca'), name='Markers',showlegend=False)
  fig4.add_trace(scatter_trace)
  fig4.update_traces(marker_line_width=3)
  fig4.update_layout(
    title_text = f"<b>Trend in Annual Sales Averages</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    #bargap = 0.5,
  )
  fig4.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig4.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig4)
  
  
def Display_market_sale_profit(Data):
  colors1 = ['#a7adba'] * 7
  colors1[0] = '#03396c'
  colors2 = ['#a7adba'] * 7
  colors2[2] = '#03396c'
  fig = make_subplots(rows=1, cols=2)
  fig.add_trace(go.Bar(x=Data.index, y=Data['Sales'], name='Sales', marker=dict(color=colors1)), row=1, col=1)
  fig.add_trace(go.Bar(x=Data.index, y=Data['Profit'], name='Profit',marker=dict(color=colors2)), row=1, col=2)
  #fig4 = px.bar(market_group, x=market_group.index, y=market_group.Sales)
  fig.update_layout(
    title_text = "<b>Average Sales and Profits for Each Regional Market</b>",
    title_font_size = 25,
    title_font_family = "Liberation Serif",
    title_font_color="#5b5b5b",
    xaxis_title = '',
    yaxis_title = '',
    plot_bgcolor= 'white',
    bargap = 0.3,
  )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
  

def display_market_category(Data,names='APAC'):
    colors = ['#a7adba']*3
    colors[2] = '#03396c'
    data = Data.loc[names]
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(go.Bar(x=data.index, y=data['Sales'], name='Sales',marker=dict(color=colors)), row=1, col=1)
    fig.add_trace(go.Bar(x=data.index, y=data['Profit'], name='Profit',marker=dict(color=colors)), row=1, col=2)

    # Update layout
    fig.update_layout(title_text=f'<b>Market Category: {names}</b>',
                      title_font_size = 25,
                      title_font_family = "Liberation Serif",
                      title_font_color="#5b5b5b",
                      xaxis_title='Category',
                      yaxis_title='Value',
                      plot_bgcolor='white')

    # Show the figure
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
    fig.update_xaxes(tickfont=dict(color='gray'))
    st.plotly_chart(fig)
    
    

def Display_Sales_shipMode(Data):
  shipping_modes = Data['Ship.Mode'].unique()

  # Create subplot with multiple columns
  fig = make_subplots(rows=1, cols=len(shipping_modes), subplot_titles=shipping_modes)

  for i, mode in enumerate(shipping_modes):
      mode_data = Data[Data['Ship.Mode'] == mode]

      scatter_trace = go.Scatter(x=mode_data['Shipping.Cost'], y=mode_data['Sales'], mode='markers', name=mode)
      fig.add_trace(scatter_trace, row=1, col=i+1)

  fig.update_layout(title_text='<b>Sales vs Shipping Cost for Different Shipping Modes</b>',
                    title_font_size = 25,
                    title_font_family = "Liberation Serif",
                    title_font_color="#5b5b5b",
                    xaxis_title='Shipping Cost',
                    yaxis_title='Sales')
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))

  st.plotly_chart(fig)
  
  
def Display_profit_shipMode(Data):
  shipping_modes = Data['Ship.Mode'].unique()
  fig = make_subplots(rows=1, cols=len(shipping_modes), subplot_titles=shipping_modes)

  for i , mode in enumerate(shipping_modes):
    mode_data = Data[Data['Ship.Mode'] == mode]
    scatter_trace = go.Scatter(x=mode_data['Shipping.Cost'], y=mode_data['Profit'], mode='markers', name=mode)
    fig.add_trace(scatter_trace, row=1, col=i+1)

    fig.update_layout(title_text='Profit vs Shipping Cost for Different Shipping Modes',
                    title_font_size = 25,
                    title_font_family = "Liberation Serif",
                    title_font_color="#5b5b5b",
                    xaxis_title='Shipping Cost',
                    yaxis_title='Profit')
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))

  st.plotly_chart(fig)
  

def Display_discount_profit(Data):
  fig = go.Figure()
  scatter_trace = go.Scatter(x=Data['Discount'], y=Data['Profit'], mode='markers')
  fig.add_trace(scatter_trace)
  fig.update_layout(title_text='<b>Profit vs Shipping Cost for Different Shipping Modes</b>',
                    title_font_size = 25,
                    title_font_family = "Liberation Serif",
                    title_font_color="#5b5b5b",
                    xaxis_title='Shipping Cost',
                    yaxis_title='Profit')
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))

  st.plotly_chart(fig)
  
  
def market_profit(Data):
  data_profit = Data['Profit']
  fig = px.bar(data_profit , x=data_profit .index, y=data_profit .columns,barmode='group')
  fig.update_layout(
      title_text = "<b>Yearly Total Profit Growth Across Regional Markets</b>",
      title_font_size = 25,
      title_font_family = "Liberation Serif",
      title_font_color="#5b5b5b",
      xaxis_title = '',
      yaxis_title = '',
      plot_bgcolor= 'white',
      bargap = 0.5,
    )
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))
  st.plotly_chart(fig)
  
  

def Display_growth_ratio(Data):
  column_names = Data.iloc[:, 4:8].columns

  legend_names = [name[6:] for name in column_names]
  fig = px.bar(Data,
              y=Data.index,
              x=column_names,
              barmode='stack',
              color_discrete_sequence=['#03396c', '#005b96', '#6497b1', '#4c4b57'],
              labels={'x': 'Years'},
              title='<b>The Top 5 APAC Countries with Market Share Growth from 2011 to 2014</b>',text_auto=True
              )

  for i, col in enumerate(column_names):
      fig.data[i].name = legend_names[i]

  fig.update_layout(legend_title_text='Legend', legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),title_font_size = 25,
        title_font_family = "Liberation Serif",
        title_font_color="#5b5b5b",
        xaxis_title = '',
        yaxis_title = '',
        plot_bgcolor= 'white')
  fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'))
  fig.update_xaxes(tickfont=dict(color='gray'))

  st.plotly_chart(fig)
  
  
def Display_ratio_slope(Data):
  colors = ['#aec7c8']*5
  colors[0] = '#03396c'
  country_growth_sorted = Data.sort_values('growth',ascending=False).head()

  melted_df = pd.melt(country_growth_sorted.reset_index(), id_vars=['Country'], value_vars=['ratio_2011', 'ratio_2014'],
                      var_name='Year', value_name='Sales Ratio')

  melted_df['Year'] = pd.Categorical(melted_df['Year'], categories=['ratio_2011', 'ratio_2014'], ordered=True)

  fig = px.line(melted_df, x='Year', y='Sales Ratio', color='Country',
                labels={'Sales Ratio': 'Sales Ratio'},
                title='<b>Slope Graph of Sales Ratios (2011 and 2014) for APAC Countries</b>',markers=True,color_discrete_sequence=colors,text=melted_df['Sales Ratio'].apply(lambda x:f'<b>{x:.2f}%</b>'))

  fig.update_layout(xaxis=dict(tickmode='array', tickvals=[0, 1], ticktext=['2011', '2014']),title_font_family = "Liberation Serif",
          title_font_color="#5b5b5b",
          title_font_size = 25,
          xaxis_title = '',
          yaxis_title = '',
          plot_bgcolor= 'white')
  fig.update_yaxes(showgrid=False, gridwidth=0.5, gridcolor='lightgray', griddash='dot', tickfont=dict(color='gray'),ticksuffix='%')
  fig.update_xaxes(tickfont=dict(color='gray'))
  fig.update_traces(line=dict(width=13),
                    marker=dict(size=20),
                    textposition='top right',
                    )

  st.plotly_chart(fig)
