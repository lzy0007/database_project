import streamlit as st
import pandas as pd
import numpy as np
from queries import *
from utils import getOne_query, getMany_query

def overview():

    def row_metrics(title, queries):

        columns = st.columns(len(title))

        for t, c, q in zip(title, columns, queries):
            c.metric(t, int( getOne_query(q) ) )

    metric = ["Sales", "Films", "Inventory", "Rental", "Customers"]

    row_metrics( ["Total " + m for m in metric], [  globals()[f"overview_total{m}"]  for m in metric] )

    st.line_chart( getMany_query(overview_salesYear).astype({"sales" : float}), x = "year" )

    