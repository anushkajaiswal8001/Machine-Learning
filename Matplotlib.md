# Matplotlib — Quick Reference

## Introduction
- Python library for creating charts and graphs.
- Commonly used with NumPy and Pandas.

## Importing
- `matplotlib.pyplot` — plotting functions.
- Alias: `plt`.

## Basic Plotting
- `plot()` — create a line chart.
- `show()` — display the chart.
- X and Y values should have matching lengths.

## Plot Customization
- `marker` — customize data point markers.
- `markersize` — change marker size.
- `color` — set line or marker color.
- `linestyle` — change line style.
- `linewidth` — change line thickness.
- `markerfacecolor` / `markeredgecolor` — customize markers.

## Labels and Ticks
- `title()` — set chart title.
- `xlabel()` / `ylabel()` — label axes.
- `xticks()` — set x-axis tick positions.
- `tick_params()` — customize tick appearance.

## Grid Lines
- `grid()` — display grid lines.
- Customize axis, color, line style and width.


## Chart Functions 

### Line Chart
- `plt.plot()` — Create a line chart.
- `marker` — Customize data point markers.
- `linestyle` — Customize line style.
- `linewidth` — Set line thickness.
- `color` — Set line color.

### Bar Chart
- `plt.bar()` — Vertical bar chart.
- `plt.barh()` — Horizontal bar chart.

### Pie Chart
- `plt.pie()` — Create a pie chart.
- `labels` — Set category names.
- `autopct` — Display percentage values.
- `explode` — Separate selected slices.
- `startangle` — Rotate the chart.

### Scatter Plot
- `plt.scatter()` — Show relationships between two numerical variables.
- `s` — Set marker size.
- `c` — Set marker colors.
- `alpha` — Control transparency.

### Histogram
- `plt.hist()` — Show numerical data distribution.
- `bins` — Set the number of intervals.
- `edgecolor` — Set bar border color.

### Labels and Appearance
- `plt.title()` — Set chart title.
- `plt.xlabel()` / `plt.ylabel()` — Label axes.
- `plt.xticks()` / `plt.yticks()` — Customize tick positions and labels.
- `plt.grid()` — Display grid lines.
- `plt.legend()` — Display labels for plotted data.
- `plt.xlim()` / `plt.ylim()` — Set axis limits.

### Multiple Plots
- `plt.subplots()` — Create a figure and one or more axes.
- `plt.tight_layout()` — Adjust spacing to prevent overlap.
- `plt.show()` — Display the figure.
- `plt.savefig()` — Save the figure to a file.


## Pandas + Matplotlib
- `pd.read_csv()` — load data from a CSV file.
- `value_counts()` — count occurrences of each category.
- Use DataFrame or Series data to create visualizations.


