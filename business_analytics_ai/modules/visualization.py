import plotly.express as px
import pandas as pd


class Visualization:

    @staticmethod
    def line_chart(df, column):

        fig = px.line(
            df,
            y=column,
            title=f"{column} Trend Analysis"
        )

        return fig

    @staticmethod
    def bar_chart(df, column):

        fig = px.bar(
            df,
            y=column,
            title=f"{column} Distribution"
        )

        return fig

    @staticmethod
    def histogram(df, column):

        fig = px.histogram(
            df,
            x=column,
            nbins=30,
            title=f"{column} Histogram"
        )

        return fig

    @staticmethod
    def box_plot(df, column):

        fig = px.box(
            df,
            y=column,
            title=f"{column} Outlier Analysis"
        )

        return fig

    @staticmethod
    def scatter_plot(df, x_col, y_col):

        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            title=f"{x_col} vs {y_col}"
        )

        return fig

    @staticmethod
    def pie_chart(df, column):

        counts = df[column].value_counts()

        fig = px.pie(
            values=counts.values,
            names=counts.index,
            title=f"{column} Distribution"
        )

        return fig