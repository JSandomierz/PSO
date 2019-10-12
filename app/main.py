import plotly.graph_objs as go
import time
import random

def genData(data):
    tmp = list(data)
    tmp[-1] = random.randint(1,10)
    return tmp

def genChart():
    cat_a = go.Bar(y=[2,1,3])
    fig = go.Figure(
        data=[cat_a],
        layout_title_text="A figure"
    )
    fig.plot(renderer="firefox")
    time.sleep(1)
    cat_a = go.Bar(y=[3,3,3])

    fig.plot(renderer="firefox")


def __main__():
    genChart()
__main__()