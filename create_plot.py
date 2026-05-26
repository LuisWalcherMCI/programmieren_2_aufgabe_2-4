import plotly.express as px


def create_fig(Zone):

    import plotly.graph_objects as go

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=Zone.index,
        y=Zone["HR"].where(Zone["Z1"]),
        mode="lines",
        name="Z1",
        line=dict(color="blue")
    ))

    fig.add_trace(go.Scatter(
        x=Zone.index,
        y=Zone["HR"].where(Zone["Z2"]),
        mode="lines",
        name="Z2",
        line=dict(color="green")
    ))

    fig.add_trace(go.Scatter(
        x=Zone.index,
        y=Zone["HR"].where(Zone["Z3"]),
        mode="lines",
        name="Z3",
        line=dict(color="yellow")
    ))

    fig.add_trace(go.Scatter(
        x=Zone.index,
        y=Zone["HR"].where(Zone["Z4"]),
        mode="lines",
        name="Z4",
        line=dict(color="orange")
    ))

    fig.add_trace(go.Scatter(
        x=Zone.index,
        y=Zone["HR"].where(Zone["Z5"]),
        mode="lines",
        name="Z5",
        line=dict(color="red")
    ))

    fig.update_layout(
        title="Heart Rate nach Zonen",
        xaxis_title="Zeit in Sekunden",
        yaxis_title="HR"
    )

    return fig