import streamlit as st
import pandas as pd
import numpy as np
import queries
from utils import getOne_query, getMany_query

def store():

    def row_metrics(title, queries):

        columns = st.columns(len(title))

        for t, c, q in zip(title, columns, queries):
            c.metric(t, str( getOne_query(q) ).capitalize() )
        

    row_metrics(["Total Number of Store", "Highest Sales Store ID", "Highest Rental Store ID"],
                    [ getattr(queries, f"store_{m}") for m in ["totalStore", "highSalesStore", "highRentalStore"] ])
    
    
    st.write("## List of Staff in Each Store")
    st.dataframe(getMany_query( getattr(queries, "store_listStaffStore") ), use_container_width = True)


    st.write("## Details for each store")
    details = {"Number of staff" : "numStaff", "Number of inventory" : "numInventory", 
    "Number of rental" : "numRental", "Number of sales" : "numSales", "Number of customer" : "numCustomer"}
    column_y = {"Number of staff" : "no_of_staff", "Number of inventory" : "no_of_inventory", 
    "Number of rental" : "no_of_rental", "Number of sales" : "no_of_sales", "Number of customer" : "no_of_customer"}
    key = st.selectbox("Select details", details)

    st.bar_chart( getMany_query( getattr(queries, f"store_{details[key]}EachStore") ), y = column_y[key], x = "store_id" )

