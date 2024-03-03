import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import html
import plotly.express as px
import pandas as pd
import dash_table

app = dash.Dash(__name__)


df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
})


styles = {
    'sidebar': {
        'width': '150px',
        'height': '100%',
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'backgroundColor': '#343a40',  
        'paddingTop': '20px',
        'paddingLeft': '10px',
        'color': 'white',
    },
    'sidebar-button': {
        'backgroundColor': 'transparent',
        'border': 'none',
        'color': 'white',
        'marginBottom': '10px',
        'fontSize': '16px',
        'display': 'block',
        'text-align': 'left',
        'padding': '10px',
        'text-decoration': 'none',
        'width': '100%',  
        'cursor': 'pointer', 
    },
    'content-rectangle': {
        'marginLeft': '150px',
        'padding': '20px',
        'backgroundColor': '#f8f9fa', 
        'border': '1px solid #dee2e6',  
        'margin-top': '80px',  
        'min-height': 'calc(100vh - 80px)', 
    },
    'app-bar': {
        'height': '60px',
        'backgroundColor': '#007BFF', 
        'padding': '10px',
        'color': 'white',
        'display': 'flex',
        'justifyContent': 'space-between',
        'alignItems': 'center',
        'position': 'fixed',
        'top': 0,
        'width': '100%',
        'zIndex': 1,  
    },
    'button-container': {
        'padding': '10px',
        'border': '1px solid #dee2e6',
        'border-radius': '5px',
        'margin-top': '20px', 
        'background-color': '#ffffff', 
    },
}

app.layout = html.Div(
    children=[
        html.Div(
            id='sidebar',
            children=[
                html.H2('SECURIUM SOLUTIONS', style={'margin': 0}),
                html.Button('Analytics', id='btn-analytics', n_clicks=0, style=styles['sidebar-button']),
                html.Button('Home', id='btn-home', n_clicks=0, style=styles['sidebar-button']),
                html.Button('Video', id='btn-new-page', n_clicks=0, style=styles['sidebar-button']),
                
                html.Button('Analytics', id='btn-analytics-appbar', n_clicks=0, style={'display': 'none'}),
            ],
            style=styles['sidebar']
        ),
        html.Div(
            children=[
                html.Div(
                    id='page-content',
                    style=styles['content-rectangle'],
                    children=[
                        html.Div(
                            id='button-container',
                            children=[
                                html.Button('Button Inside Rectangle', id='btn-inside', n_clicks=0, style=styles['sidebar-button']),
                            ],
                            style=styles['button-container']
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.H2('SECURIUM SOLUTIONS', style={'margin': 0}),
    
                    ],
                    style=styles['app-bar']
                ),
            ]
        ),
    ]
)


@app.callback(Output('page-content', 'children'),
              [Input('btn-home', 'n_clicks'),
               Input('btn-analytics', 'n_clicks'),
               Input('btn-analytics-appbar', 'n_clicks'),
               Input('btn-new-page', 'n_clicks'),
               Input('btn-inside', 'n_clicks')],
              prevent_initial_call=True)  
def display_page(btn_home, btn_analytics, btn_analytics_appbar, btn_new_page, btn_inside):
    ctx = dash.callback_context
    if not ctx.triggered_id:
        button_id = 'btn-home'
    else:
        button_id = ctx.triggered_id.split('.')[0]

    if button_id == 'btn-home':
       data = [
            {'Name': 'John', 'CV_SCORE': 25, 'Sale': 'Happend'},
            {'Name': 'Alice', 'CV_SCORE': 30, 'Sale': 'Not happend'},
            {'Name': 'Bob', 'CV_SCORE': 28, 'Sale': 'Happend'},
            {'Name': 'John', 'CV_SCORE': 25, 'Sale': 'Happend'},
            {'Name': 'Alice', 'CV_Score': 30, 'Sale': 'No'},
            {'Name': 'Bob', 'CV_SCORE': 28, 'Sale': 'Happened'},
            {'Name': 'John', 'CV_SCORE': 25, 'Sale': 'Happend'},
            {'Name': 'Alice', 'CV_SCORE': 30, 'Sale': 'No'},
            {'Name': 'Bob', 'CV_SCORE': 28, 'Sale': 'No'},
        ]

        
       columns = [{'name': col, 'id': col} for col in data[0].keys()]
       table = dash_table.DataTable(
            columns=columns,
            data=data,
            style_table={'height': '300px', 'overflowY': 'auto'},  
        )
       df_scatter = pd.DataFrame({
            'x': [1, 2, 3, 4, 5],
            'y': [10, 11, 12, 13, 14]
        })
       scatter_plot = [
            html.H1('Analytics Content - Panda Graph Placeholder'),
            dcc.Graph(
                id='panda-plot',
                figure=px.scatter(df_scatter, x='x', y='y', title='Sample Panda Scatter Plot')
            )
        ]
       return table
    elif button_id == 'btn-analytics' or button_id == 'btn-analytics-appbar':
        df_scatter = pd.DataFrame({
            'x': [1, 2, 3, 4, 5],
            'y': [10, 11, 12, 13, 14]
        })

        scatter_plot = [
            html.H1('Analytics Content - Simple plot'),
            dcc.Graph(
                id='panda-plot',
                figure=px.scatter(df_scatter, x='x', y='y', title='Sample Panda Scatter Plot')
            )
        ]

        return  scatter_plot
        
  
    elif button_id == 'btn-analytics' or button_id == 'btn-analytics-appbar':
        return [
            html.H1('Analytics Content - Panda Graph Placeholder'),
            dcc.Graph(
                id='panda-plot',
                figure=px.scatter(df, x='x', y='y', title='Sample Panda Scatter Plot')
            )
        ]
    elif button_id == 'btn-inside':
        return html.H1('New Button Content')
    elif button_id == 'btn-new-page':
        video_url = 'https://www.youtube.com/watch?v=f4q61AWv8pA&list=PPSV'
        return [
            html.H1('Video Content'),
            html.Iframe(src=video_url, width='560', height='315', style={'border': '0'}),
            html.Iframe(src=video_url, width='560', height='315', style={'border': '0'}),
            html.Iframe(src=video_url, width='560', height='315', style={'border': '0'}),
            html.Iframe(src=video_url, width='560', height='315', style={'border': '0'}),
            dbc.Button("YES", outline=True, color="primary", className="me-1"),
        dbc.Button(
            "NO", outline=True, color="secondary", className="me-1"
        ),
            
        ]



if __name__ == '__main__':
    app.run_server(debug=False, port=8092)



