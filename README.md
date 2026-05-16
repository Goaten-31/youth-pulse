# YouthPulse: an analysis of teen mental health and potentially related factors
***
## Purpose:
The goal of this project is to provide an easy-to-comprehend data visualization
and analysis dashboard to study teen mental health and its correlation with
other factors such as:
- Academic Performance
- Sleep Hours
- Social Media Usage
***
## Stack:
- ### Languages:
1. **Python (3.12+)**
2. **SQL**
- ### Framework/Libs:
1. **Pandas**
2. **NumPy**
3. **Plotly**
4. **SQLalchemy**
- ### Technologies:
1. **Streamlit**
2. **PostgreSQL**
***
## Implementation:
### Requirements:
To run this on your local machine, you must have the aforementioned stack
and the following datasets:
 - **CSV:**
   - [Teen_Mental_Health_Dataset.csv]() 
 - **SQL:**
   - [Check this repo]() 
### Running:
To actually run it, open your terminal in the correct directory and run:
```bash
streamlit run main.py
# replace 'main' with the appropriate file name
```
***
## Limitations:
The working dataset (Teen_Mental_Health_Dataset.csv) didn't control for
things such as financial status, substance usage and diet habits; with 
missing variables such as these, it becomes harder to assert causation 
and draw clear conclusions; this is a study on correlation only.