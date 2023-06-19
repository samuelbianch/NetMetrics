import plotly.express as px
import plotly.graph_objects as go

class Gerar_Grafico():
    def generate_chart(names, values):
        df = "Media Trans"
        fig = px.pie(df, values=values, names=names, hole=.3)

        return fig
    

    def gerar_donut(label, value, arq):

        labels = ['', label]
        values = [1 - value, value]

        # Use `hole` to create a donut-like pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update(layout_showlegend=False)
        fig.update({'layout': {'xaxis' : {'color': '#229954'}}})

        html = fig.to_html()

        with open('templates/partials/_grafico_' + arq + '.html', 'w', encoding="utf-8") as arquivo:
            arquivo.write(html)
            arquivo.close()
