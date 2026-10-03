import streamlit as st
from snowflake.snowpark.context import get_active_session

st.title("📦 Supply Chain Anomaly Dashboard")
st.write("Live Inventory Risk & Deficit Monitor")

session = get_active_session()

query = """
SELECT 
    i.product_id, 
    i.warehouse_location, 
    i.current_stock, 
    i.reorder_threshold, 
    (i.reorder_threshold - i.current_stock) as deficit,
    s.supplier_name, 
    s.status as order_status
FROM INVENTORY_LOGS i
LEFT JOIN SUPPLIER_ORDERS s ON i.product_id = s.product_id
WHERE i.current_stock < i.reorder_threshold
"""

df = session.sql(query).to_pandas()

if df.empty:
    st.success("All inventory levels are healthy.")
else:
    st.error(f"🚨 ALERT: {len(df)} products are currently below reorder thresholds.")
    st.dataframe(df)
    st.bar_chart(data=df, x='PRODUCT_ID', y='DEFICIT')
