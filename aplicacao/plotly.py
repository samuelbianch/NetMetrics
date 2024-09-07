import plotly.express as px
import plotly.graph_objects as go

class Gerar_Grafico():
    def generate_chart(names, values):
        df = "Media Trans"
        fig = px.pie(df, values=values, names=names, hole=.3)

        return fig
    

    def gerar_donut(label, value, arq):

        colors = ['rgb(255, 255, 255)', 'rgb(0, 181, 30)', 'rgb(0, 0, 255)']
        if value < 0:
            colors = ['rgb(255, 255, 255)',  'rgb(250, 0, 0)', 'rgb(0, 0, 255)']
            value = value * (-1)
        labels = ['', label]
        values = [1 - value, value]

        
        # Use `hole` to create a donut-like pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, marker_colors=colors)])
        fig.update(layout_showlegend=False)
        fig.update_traces(hoverinfo='label+percent+name', textinfo='none')
        fig.update({'layout': {
            'xaxis' : {
                'color': 'green'
                },
            'height': 300,
            'width': 300,
            }
            
        })

        html = fig.to_html()

        with open('templates/partials/_grafico_' + arq + '.html', 'w', encoding="utf-8") as arquivo:
            arquivo.write(html)
            arquivo.close()
