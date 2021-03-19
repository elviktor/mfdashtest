# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    qtr1Performance,
    qtr2Strategy,
    campaignSummaries,
    internalData,
    externalData,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/qtr-1-performance":
        return qtr1Performance.create_layout(app)
    elif pathname == "/dash-financial-report/qtr-2-strategy":
        return qtr2Strategy.create_layout(app)
    elif pathname == "/dash-financial-report/campaigns":
        return campaignSummaries.create_layout(app)
    elif pathname == "/dash-financial-report/internal-data":
        return internalData.create_layout(app)
    elif pathname == "/dash-financial-report/external-data":
        return externalData.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            qtr1Performance.create_layout(app),
            qtr2Strategy.create_layout(app),
            campaignSummaries.create_layout(app),
            internalData.create_layout(app),
            externalData.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
