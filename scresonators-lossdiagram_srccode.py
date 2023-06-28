#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import pandas for Creation of DataFrame
import pandas as pd
# Import plotly for creation of graph object
import plotly.express as px
# Import numpy to use np.arange()
import numpy as np
# Import plotly io for html generation
import plotly.io as pio
#import chart studio to push graph to plotly and generate an iframe 
import chart_studio
import chart_studio.tools as tls
# Read in excel file in .xlsx format
data = pd.read_excel('graph_data_revised.xlsx')

# Create a pandas dataframe and label each column
df= pd.DataFrame(data, columns=['SC', 'Reference', 'Dep.', 'Substrate', 'δLP (×10**−6)','Fδ0TLS (×10**−6)','g','δLP','Fδ0TLS'])

# create a symbol array specifying which symbols to use
symbols=['circle', 'square', 'diamond', 'cross', 'x', 'triangle-up', 'pentagon', 'star']


# Create scatter plot figure using plotly express as px.scatter
fig = px.scatter(
           df, 
           x='g', 
           y=['δLP (×10**−6)','Fδ0TLS (×10**−6)'],
           color='Reference', 
           color_discrete_sequence=px.colors.qualitative.Alphabet,
           symbol='SC',
           symbol_sequence= symbols,
           labels={'SC' : 'Superconductor', 'Reference' : 'Source', 'Dep.' : 'Depostion', 'g' : 'g (μm)'},
           hover_name='Reference',
           hover_data={'Dep.': True, 'SC':True, 'Substrate': True,'g' : False, 'value' : False, 'Reference': False},
           log_x=True, log_y=True)


# Create diagonal lines using Numpy range, and a loop to itereate over each constant and generate an (x,y) coordinate line trace
x = np.arange(0.1, 40, 0.1)
constants = [0.25E-6, 0.5E-6, 1.0E-6, 2.0E-6, 4.0E-6, 8.0E-6, 16.0E-6, 32.0E-6, 
             64.0E-6, 128.0E-6, 256.0E-6, 512.0E-6, 1014.0E-6, 2018.0E-6]
for constant in constants:
    y = (1/x) * constant
    fig.add_scatter(x=x,y=y,mode='lines',showlegend=False,line_color='black',hoverinfo='skip',opacity=.1)


# Update the labels of the X and Y axis, the attriubutes of the graph title, and the background and paper color of the plot
fig.update_layout(xaxis_title= "g (μm)", 
                  yaxis_title= "δLP , Fδ0TLS",
                  title_font_color="black", 
                  title_font_family="Droid sans", 
                  title_font_size=38,
                  plot_bgcolor="#b4bac2",
                  paper_bgcolor="rgba(0,0,0,0)",showlegend=False)

# # update the stylization of the legend 
# fig.update_layout(legend_bgcolor="rgba(0,0,0,0)",
#                   legend_bordercolor="rgba(0,0,0,0)",
#                   legend_borderwidth=2,
#                   legend=dict(
#                   orientation="h",
#                   yanchor= "auto",
#                   font=dict(size=5)))

# Format stylization of Y axis
fig.update_yaxes(exponentformat="power", 
                 gridcolor="white", 
                 linecolor="black", 
                 zeroline=True,
                showgrid=False,
                showticklabels=True,
                ticks='inside',
                mirror=True,
                range=[-6.8,-4.2])

# Format stylization of X axis
fig.update_xaxes(exponentformat="power", 
                 linecolor="black",
                 showgrid=False,
                showticklabels=True,
                ticks='inside',
                mirror=True,
                range=[-.05,1.55])

# Add annotation to show correlation of plotted data 
fig.add_annotation(x=0.9, y=-5.2,
            text="Decreasing Interface Loss",
            font=dict(family="Droid sans", size= 15),
            showarrow=True,
            arrowwidth=2.5,
            arrowhead=3,
                  ay=-50,
                  ax=70)
#Sets anchoring of legend to be visible below the plot
fig.update_layout(legend={'x':-0.3,'y':-0.70})

#Change username and API key to push to your chart studio plotly account
username = 'dylanblevins49'
api_key='xzY9yy6Z7WNySh5P5PNy'
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

#This will push to your account 
import chart_studio.plotly as py
py.plot(fig, filename = 'index.html', auto_open=True)

#This will generate your iframe, chang url to the url where you graph is hosted on chart studio plotly. ADD   ?link=false   at the end of url to eliminate "Edit Chart" button
import chart_studio.tools as tls
tls.get_embed('https://plotly.com/~dylanblevins49/3/') 

#Use these if you just want and html file
# pio.write_html(fig, file='index.html', auto_open=True)
# fig.write_html("scatter_plot_final.html") 


# In[ ]:




