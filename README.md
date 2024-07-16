# python-pandas-graph

Download the TSLA stock price from https://query1.finance.yahoo.com/v7/finance/download/TSLA?period1=1667246938&period2=1698782938&interval=1d&events=history&includeAdjustedClose=true 

Open the python3 interpreter and type in the following commands:

```python
>>> import pandas
>>> # change the path_to_plot to your web directory
>>> path_to_plot = "tsla.png"
>>> df = pandas.read_csv('TSLA.csv')
>>> # Here we pick the columns we like to plot
>>> df[ ['Date', 'Close'] ].plot().get_figure().savefig(path_to_plot)
```

You can now access the plot as a png file

Using the above knowledge, create a script called `graph.py`, stock_plot.py 
that takes one argument, the stock ticker symbol, and outputs an image called stock.png 
to your web directory.  i.e.

```console
$ ls
graph.py  README.md
$ python3 graph.py asdf
Error in receiving stock symbol
$ python3 graph.py MSFT
$ ls
graph.py  MSFT.png  README.md
$ 
```

HINT: if you choose to write a pure python script, but you still want to call some shell commands, following this link: https://ioflood.com/blog/python-run-shell-command/  

Read the documentation on DataFrame.plot
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
and 
matplotlib (the library that pandas use to create graphs)
https://matplotlib.org/stable/api/figure_api.html
so that the graph is properly labeled (i.e. proper title, axis labels, etc.)

Here's an example:

![Example graph for nvida](example.png)

