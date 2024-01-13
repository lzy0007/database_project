import streamlit as st
import pandas as pd
import numpy as np
import queries
from utils import getOne_query, getMany_query

def staff():

    #### Metrics

    def row_metrics(title, queries):
        columns = st.columns(len(title))

        for t, c, q in zip(title, columns, queries):
            c.metric(t, str( getOne_query(q) ).capitalize())

    row_metrics(["Number of Active Staff", "Staff ID with Most Sales"],
                [getattr(queries, f"staff_{m}") for m in ["active", "MostSales"]])

    #### Staff Over City
    st.write("## Distribution of Staff over City")
    st.bar_chart(getMany_query(getattr(queries, 'staff_DistributionOverCity')), y="staff_count", x="city")

    #### Ratio of Number of Rental with Number of Serviced Customer Over Staff
    #### Ratio of Sales with Number of Rental Over Staff
    st.write("## Ratio by Group Key over Staff")
    groupkey = {"Number of Rental with Number of Serviced Customer" : "RatioRental_NumServicedCustomerOverStaff", "Sales with Number of Rental" : "RatioSales_NumRentalOverStaff"}
    column = {"Number of Rental with Number of Serviced Customer": "rental_customer_ratio", "Sales with Number of Rental": "sales_rental_ratio"}
    key = st.selectbox("Select Ratio", groupkey)

    st.bar_chart( getMany_query( getattr(queries, f"staff_{groupkey[key]}") ).astype({column[key] : float}), y = column[key], x = "staff_id" )
