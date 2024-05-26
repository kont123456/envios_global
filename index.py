import pandas as pd
import dash
import plotly.express as px 
import dash_bootstrap_components as dbc 
from dash import dcc,html,dash_table 
from dash.dependencies import Output,Input 
from app import app 
import lateral,grafico1,grafico2 

server=app.server


app.layout= dbc.Container([
                dbc.Row([
                    dbc.Col([
                        
                             dcc.Location(id="url",pathname="/grafico1"),
                             lateral.layout 
                           
                        
                    ],md=2,style={'position': 'fixed', 'height': '100%', 'overflow': 'auto', 'width': '25%'}),
                     dbc.Col(
                        
                        html.Div(id="graficos",style={'overflow': 'auto', 'width': '100%', 'height': '100vh', 'margin-left': '21.2%'}),
                        
                    md=10)
                        
                ])
                
],fluid=True)
@app.callback(Output("graficos","children"),
              [Input("url","pathname")])

def actualizar_link(url):
    if url=="/" or url=="/grafico1":
       return grafico1.layout
    if url=="/grafico2":
       return grafico2.layout

if __name__=="__main__":
     app.run_server(debug=True)
