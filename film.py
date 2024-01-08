import streamlit as st
import pandas as pd
import numpy as np
import queries
from utils import getOne_query, getMany_query

def film():

    #### Metrics
    def row_metrics(title, queries):

        columns = st.columns(len(title))

        for t, c, q in zip(title, columns, queries):
            c.metric(t, str( getOne_query(q) ).capitalize() )
    
    
    row_metrics(["Highest Sales Film", "Highest Sales Category", "Actor with Highest Ratio of Sales and Film"],
                [ getattr(queries, f"film_high{m}") for m in ["SalesFilm", "SalesCat", "RatioSalesNumFilmAct"] ])



    
    ####Films by Group Key
    st.write("## Films by Group Key")
    groupkey = {"Actor" : "Act", "Category" : "Cat", "Language" : "Lang", "Release Year" : "Year"}
    key = st.selectbox("Select the group by Key", groupkey)

    list_columns, chart_columns = st.columns(2)
    
    with list_columns:
        st.dataframe(getMany_query( getattr(queries, f"film_by{groupkey[key]}") ), use_container_width = True)

    with chart_columns:

        st.bar_chart( getMany_query( getattr(queries, f"film_numBy{groupkey[key]}") ).astype({"count" : int}), y = "count", x = key.lower() )



    

    ####Sales by Group Key
    st.write("## Sales by Group Key")
    groupkey = {"Rental Rate" : "Rent", "Rental Duration" : "Dur", "Rating" : "Rat", "Category" : "Cat", "Features" : "Fea"}
    key = st.selectbox("Select the group by Key", groupkey)

    st.bar_chart( getMany_query( getattr(queries, f"film_salesBy{groupkey[key]}") ).astype({"sales" : int}), y = "sales", x = key )
        
    
    
    
    
    