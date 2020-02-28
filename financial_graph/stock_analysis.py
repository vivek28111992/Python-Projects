from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

start = datetime.datetime(2018, 6, 19)
end = datetime.datetime(2019, 12, 18)

df = data.DataReader(name = "HDFCAMC.NS", data_source="yahoo", start=start, end=end)
df['Status'] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df['Middle'] = (df.Open+df.Close)/2
df['Height'] = abs(df.Open-df.Close)

# print(df.Open, df.Close)

p = figure(x_axis_type='datetime', width=1000, height=400, sizing_mode="scale_width")
p.title.text = "Candlestick Chart"
p.grid.grid_line_alpha = 0.3

hours_12 = 12 * 60 * 60 * 1000

p.segment(df.index, df.High, df.index, df.Low, color="Black")

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"], fill_color="green", line_color="black")

p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"], fill_color="red", line_color="black")

# output_file("CS.html")
# show(p)

script1, div1 = components(p)
cdn_js = CDN.js_files
cdn_css = CDN.css_files

print(cdn_js)
