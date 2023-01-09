# import plotly.express as px
# import plotly.graph_objects as go
#
# df = px.data.gapminder().query("year==2007")
#
# fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
#                      size="pop", hover_name="country",
#                      title="Population by Country and Continent",
#                      size_max=60)
#
# # Add pie chart markers
# pie_chart_data = [go.Scattergeo(
#     lon = df[df['continent'] == cont]['longitude'],
#     lat = df[df['continent'] == cont]['latitude'],
#     text = df[df['continent'] == cont]['country'],
#     mode = 'markers+text',
#     textposition = 'bottom center',
#     marker = {
#         'size': df[df['continent'] == cont]['pop']/1e6,
#         'sizemode': 'area',
#         'sizeref': 2.*max(df[df['continent'] == cont]['pop']/1e6)/(100.**2),
#         'sizemin': 4
#     },
#     name = cont
# ) for cont in df.continent.unique()]
#
# fig.update_traces(pie_chart_data, selector=dict(type='scattergeo'))
# fig.show()

