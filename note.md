# Notes
Dash App is best defined as Componets that are displayed on the page through the **layout**, which interact with each other through the **Callback**

1. Components: Eg; radio button, drop down, calender etc
2. Layout: How components and apps are displayed on the page
3. Callbacks: Allows app to be interactive

-- dcc vs dbc <br>
dcc : dash core components <br>
dbc: dash bootstrap components

Note:
* We import the dcc module (DCC stands for Dash Core Components). This module includes a Graph component called dcc.Graph, which is used to render interactive graphs.
* We import the **dash_ag_grid package (as dag)** to display the data in a table.
* We also import the **plotly.express** library to build the interactive graphs.

-- dcc vs dag <br>
dcc = Dash Core Components (built-in UI components) <br>
dag = Dash AG Grid (a separate, specialized component library for tables)

-- plotly.express (px) vs plotly.graph_objects <br>
1️⃣ Big picture (one sentence) <br>
    plotly.express (px) = quick, high-level, automatic <br>
    plotly.graph_objects (go) = low-level, explicit, fully controllable <br>
    They both produce the same final thing: a Plotly Figure.

2️⃣ Think of it like this (analogy)<br>
    🚗 Driving analogy<br>
    plotly.express → automatic car<br>
    plotly.graph_objects → manual car

Both get you to the destination (a figure), but:<br>
    px makes decisions for you<br>
    go lets you control everything


* Always remember bootstrap canvas has 12 invicible grid or columns.



# Some Links
* [dcc.Dropdown](https://dash.plotly.com/dash-core-components/dropdown)
* [API Reference](https://dash.plotly.com/reference#dash.dash)
* [Example App](https://dash-example-index.herokuapp.com/)
* [Bootstrap](https://www.dash-bootstrap-components.com/docs/)
* [Bootstrap-Components](https://www.dash-bootstrap-components.com/docs/components/)
* [Dash Cheatsheet](https://dash-example-index.herokuapp.com/cheatsheet)
* [Bootstrap 4 Cheat Sheet](https://hackerthemes.com/bootstrap-cheatsheet/)
* [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/)
* [Plotly](https://plotly.com/python/?_gl=1*e9r9hi*_gcl_au*MTM2MDA0MzQ0Mi4xNzY2MDY4MDE0*_ga*MjA2MDY2OTc3NS4xNzY2MDY4MDE1*_ga_6G7EE0JNSC*czE3NjczODE5MDIkbzE4JGcxJHQxNzY3MzgyMTc4JGo0OCRsMCRoMA..)

## YT vide0
* [callbacks](https://www.youtube.com/watch?v=pNMWbY0AUJ0)

# Activate Virtual Environment
source dashenv/bin/activate
