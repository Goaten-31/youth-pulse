import streamlit as st
from cleaning import *

st.markdown("""
    ## Teen Mental Health, Academic Performance, and Social Media Usage: The links between the three
    ### How can we establish solid predictions to one of them based on the other variables
""")
st.divider()

st.markdown("""
    ### Introduction:
    With this dashboard, consisting currently of the working dataframes and charts.
    
    I aim to provide a clear and concise explanation for how all the parameters in this dataset correlate
    between one another, and which one of them is relevant in which context.
    Then drawing conclusions to help discover methods to improve teen mental health.
""")

st.divider()

st.markdown("""
    ## The working dataframes:
    #### The main dataframe:
    The original dataframe contains 1200 rows, this is a 10 row header is here
    to showcase each of the parameters and their potential values.
""")

st.dataframe(dfc.head(10))

st.markdown("""
    ### Academic Performance by Hours of Sleep:
    The following dataframe and charts showcases the average GPA of students within a specified range
    of hours of sleep
""")

st.dataframe(slpdf)
st.plotly_chart(exp_bar_plot(slpdf))
st.plotly_chart(exp_scatter_plot(slpdf))

st.divider()

st.markdown("""
            ###### Since sleep hours is a dataset containing ranges and not fixed values,
            ###### we use the following formula for each one of the ranges and replace the
            ###### range in question with the value we got:
            """)
st.latex(r'''x_{mid} = \frac{x_{lower} + x_{upper}}{2}''')

st.markdown("""
    Now, we can calculate the correlation coefficient:
""")

st.latex(r'''
r = \frac{n\sum xy - \sum{x} \sum{y}}{\sqrt{[n\sum x^2 - (\sum x)^2] - [n\sum y^2 - (\sum y)^2]}}\\
''')
st.latex(r'''with: \\
n = \ Number \ of \ Elements \ in \ a \ Dataset  \\
x = \ Average \ Hours \ of \ Sleep \\
y = \ Average \ Academic \ Performance \ in \ GPA \\ 
''')

st.markdown("""
    After computing, we find out that the correlation coefficient is approximately 0.
    Aligning perfectly with our graph, and showing that there is no correlation between sleep hours and
    academic performance.
""")

st.divider()

st.markdown("""
    Now that our methodology is clear, 
    we will look into how mental health indices change in relation
    to other parameters
""")

st.divider()

st.markdown("""
    # Sleep In Relation to Mental Health:
""")