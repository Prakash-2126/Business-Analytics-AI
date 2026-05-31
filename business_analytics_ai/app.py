import streamlit as st
from modules.visualization import Visualization
from modules.loader import DataLoader
from modules.profiler import DataProfiler
from modules.descriptive import (
    DescriptiveAnalysis
)
from modules.diagnostic import (
    DiagnosticAnalysis
)
from modules.predictive import (
    PredictiveAnalysis
)
from modules.prescriptive import (
    PrescriptiveAnalysis
)
from modules.report_generator import (
    ReportGenerator
)
from modules.utils import (
    create_directories
)

create_directories()

st.set_page_config(
    page_title="Business Analytics AI",
    layout="wide"
)

st.title(
    "Business Analytics AI Platform"
)

uploaded_file = st.file_uploader(
    "Upload Dataset"
)

if uploaded_file:

    df = DataLoader.load(
        uploaded_file
    )

    st.subheader("Dataset")

    st.dataframe(df.head())

    # ==================================
    # DATA VISUALIZATION SECTION
    # ==================================

    st.subheader("Data Visualizations")

    numeric_columns = (
        df.select_dtypes(
            include=["int64", "float64"]
        )
        .columns
        .tolist()
    )

    categorical_columns = (
        df.select_dtypes(
            include=["object"]
        )
        .columns
        .tolist()
    )

    # Line Chart
    if numeric_columns:

        line_col = st.selectbox(
            "Select Column for Trend Analysis",
            numeric_columns
        )

        st.plotly_chart(
            Visualization.line_chart(
                df,
                line_col
            ),
            use_container_width=True
        )

    # Bar Chart
    if numeric_columns:

        bar_col = st.selectbox(
            "Select Column for Bar Chart",
            numeric_columns,
            key="bar"
        )

        st.plotly_chart(
            Visualization.bar_chart(
                df,
                bar_col
            ),
            use_container_width=True
        )

    # Histogram
    if numeric_columns:

        hist_col = st.selectbox(
            "Select Column for Histogram",
            numeric_columns,
            key="hist"
        )

        st.plotly_chart(
            Visualization.histogram(
                df,
                hist_col
            ),
            use_container_width=True
        )

    # Box Plot
    if numeric_columns:

        box_col = st.selectbox(
            "Select Column for Box Plot",
            numeric_columns,
            key="box"
        )

        st.plotly_chart(
            Visualization.box_plot(
                df,
                box_col
            ),
            use_container_width=True
        )

    # Scatter Plot
    if len(numeric_columns) >= 2:

        x_col = st.selectbox(
            "Scatter X Axis",
            numeric_columns,
            key="scatter_x"
        )

        y_col = st.selectbox(
            "Scatter Y Axis",
            numeric_columns,
            key="scatter_y"
        )

        st.plotly_chart(
            Visualization.scatter_plot(
                df,
                x_col,
                y_col
            ),
            use_container_width=True
        )

    # Pie Chart
    if categorical_columns:

        pie_col = st.selectbox(
            "Select Category Column",
            categorical_columns
        )

        st.plotly_chart(
            Visualization.pie_chart(
                df,
                pie_col
            ),
            use_container_width=True
        )



    profile = DataProfiler.profile(df)

    st.subheader("Profile")

    st.json(profile)

    descriptive = (
        DescriptiveAnalysis.generate(df)
    )

    st.subheader(
        "Descriptive Analysis"
    )

    st.write(descriptive)

    # ==================================
    # DIAGNOSTIC ANALYSIS
    # ==================================

    corr = (
        DiagnosticAnalysis.correlation(df)
    )

    st.subheader(
        "Correlation Matrix"
    )

    st.dataframe(corr)

    # ==================================
    # PRESCRIPTIVE ANALYSIS
    # ==================================

    recommendations = (
        PrescriptiveAnalysis
        .recommendations(df)
    )

    st.subheader(
        "Recommendations"
    )

    st.write(recommendations)

    # ==================================
    # MODEL TRAINING
    # ==================================

    numeric_columns = (
        df.select_dtypes(
            include=["int64", "float64"]
        )
        .columns
        .tolist()
    )

    if numeric_columns:

        target = st.selectbox(
            "Select Target Column",
            numeric_columns,
            key="target_column"
        )

        if st.button(
            "Train Prediction Model"
        ):

            try:

                score, path = (
                    PredictiveAnalysis.train(
                        df,
                        target
                    )
                )

                st.success(
                    f"Model Score: {score:.4f}"
                )

                st.success(
                    f"Model Saved: {path}"
                )

            except Exception as e:

                st.error(
                    f"Training Error: {e}"
                )

    # ==================================
    # PDF REPORT GENERATION
    # ==================================

    if st.button(
        "Generate PDF Report"
    ):

        try:

            ReportGenerator.generate(
                profile,
                descriptive,
                recommendations
            )

            st.success(
                "Report Generated Successfully"
            )

        except Exception as e:

            st.error(
                f"Report Error: {e}"
            )