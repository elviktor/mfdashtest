import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("CFLJ_transparent_logo_2017_edition_PNG.png"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("Full View", id="learn-more-button"),
                        href="/dash-financial-report/full-view",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Center for Law and Justice")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [html.H6("1st Quarter Report")],
                        className="seven columns main-title",
                    )
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "1st Quarter Performance",
                href="/dash-financial-report/qtr-1-performance",
                className="tab",
            ),
            dcc.Link(
                "2nd Quarter Strategy",
                href="/dash-financial-report/qtr-2-strategy",
                className="tab",
            ),
            dcc.Link(
                "Campaign Summaries", href="/dash-financial-report/campaigns", className="tab"
            ),
            dcc.Link(
                "Internal Data",
                href="/dash-financial-report/internal-data",
                className="tab",
            ),
            dcc.Link(
                "External Data",
                href="/dash-financial-report/external-data",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
