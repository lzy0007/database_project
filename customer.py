import streamlit as st
import pandas as pd
import numpy as np
import queries
from utils import getOne_query, getMany_query

def customer():

    

    #### Metrics
    def row_metrics(title, queries):

        columns = st.columns(len(title))

        for t, c, q in zip(title, columns, queries):
            c.metric(t, str( getOne_query(q) ).capitalize() )
    
    
    row_metrics(["Top Spending Customer", "Customer With Most Inventory"],
                [ getattr(queries, f"customer_most{m}") for m in ["InPrice", "InInventory"] ])


    ####Customer/Customer Sales by Group Key
    st.write("### Distribution of Customer/Customer Sales in Each City")
    groupkey = {"Customer" : "CustomersCity", "Customer Sales" : "CustomerSalesCity"}
    key = st.selectbox("Select The Attribute by Key", groupkey)

    if(groupkey[key] == "CustomersCity"):
        st.bar_chart( getMany_query( getattr(queries, f"customer_distribution{groupkey[key]}") ).astype({"customer_count" : "int"}), x = "district", y = "customer_count" )
    else:
        st.bar_chart( getMany_query( getattr(queries, f"customer_distribution{groupkey[key]}") ).astype({"total_sales" : "float"}), x = "district", y = "total_sales" )


    ####Sales by Group Key
    st.write("## Customer Over Payment")

    st.line_chart( getMany_query( getattr(queries, "customer_overPaymentYears") ), y = "customer_count", x = "payment_year" )
    


