
import streamlit as st
import pandas as pd

# Title
st.title("Clothes Shop Data Analysis")

# Read CSV file
df = pd.read_csv("clothes.csv")

# Sidebar filters
st.sidebar.header("Filters")

section = st.sidebar.selectbox(
    "Select Section",
    ["All", "Male", "Female"]
)

clothes = st.sidebar.selectbox(
    "Select Clothes",
    ["All"] + sorted(df["clothes"].unique())
)

size = st.sidebar.selectbox(
    "Select Size",
    ["All"] + sorted(df["size"].unique())
)

# Apply filters
if section != "All":
    df = df[df["section"] == section]

if clothes != "All":
    df = df[df["clothes"] == clothes]

if size != "All":
    df = df[df["size"] == size]

# Display clothes
st.subheader("Clothes Details")

if len(df) > 0:

    st.dataframe(df)

    # Basic analysis
    st.subheader("Data Analysis")

    st.write("Total Stock:", df["quantity"].sum())

    st.write("Average Price:", round(df["price"].mean(), 2))

    st.write("Highest Price:", df["price"].max())

    st.write("Lowest Price:", df["price"].min())

    # Most available clothes
    st.subheader("Most Available Clothes")

    best = df.loc[df["quantity"].idxmax()]

    st.write(best["clothes"])

    # Low stock
    st.subheader("Low Stock Alert")

    low_stock = df[df["quantity"] < 11]

    if len(low_stock) > 0:
        st.warning("Low stock available!")
        st.dataframe(low_stock)
    else:
        st.success("Stock is available!")

    # Clothes chart
    st.subheader("Clothes Quantity Chart")

    st.bar_chart(df.set_index("clothes")["quantity"])

    # Size analysis
    st.subheader("Size-wise Analysis")

    size_data = df.groupby("size")["quantity"].sum()

    st.bar_chart(size_data)

else:
    st.warning("No data found!")
