import streamlit as st
import pandas as pd
import numpy as np
import queries
from overview import overview
from film import film
from customer import customer
from store import store
from staff import staff
from utils import getOne_query, getMany_query

st.write("# Sakila Dashboard")
group = st.expander("Group description")
group.table(pd.DataFrame({"Name": ["NG ZI XING", "LOO ZHI YUAN", "SAM CHIA YUN", "YEW RUI XIANG"], "Matric Code": ["A21EC0213", "A21EC0197", "A21EC0127", "A21EC0149"] }))

overview_tab, film_tab, customer_tab, staff_tab, store_tab = st.tabs(["##### Overview", "##### Film", "##### Customers", "##### Staffs", "##### Store"])

with overview_tab:
    overview()

with film_tab:
    film()

with customer_tab:
    customer()

with staff_tab:
    staff()

with store_tab:
    store()
    
