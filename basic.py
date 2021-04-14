import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input,Output
import dash_auth

USERNAME_PASSWORD_PAIRS = [['manish@fecdirect.org','test@123'] , ['sanga','sanga@123']]


app = dash.Dash()

auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)


app.layout = html.Div([
    dcc.Slider(
        id='my-input',
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) for i in range(10)},
        value=8,
    ),
    html.H1(id='my_output')

])

@app.callback(
    Output('my_output','children'),
    [Input('my-input','value')]
)
def dddddd(record):
    return record



if __name__ == '__main__':
    app.run_server()