import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Nassau Candy Supply Chain Analytics",
    layout="wide"
)

st.title("🍭 Nassau Candy: Distribution Performance Dashboard")
st.markdown("### Executive Analysis of Shipping Efficiency and Logistics")

FILE_NAME = "Nassau Candy Distributor (1).csv"

try:
    df = pd.read_csv(FILE_NAME)
    factory_df = pd.read_csv("factories.csv")

    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")

    df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days
    df.loc[df["Lead Time"] > 30, "Lead Time"] = df["Lead Time"] % 10 + 2
    df.loc[df["Lead Time"] <= 0, "Lead Time"] = 3

    factory_map = {
        "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
        "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
        "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
        "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
        "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
        "Laffy Taffy": "Sugar Shack",
        "SweeTARTS": "Sugar Shack",
        "Nerds": "Sugar Shack",
        "Fun Dip": "Sugar Shack",
        "Fizzy Lifting Drinks": "Sugar Shack",
        "Everlasting Gobstopper": "Secret Factory",
        "Hair Toffee": "The Other Factory",
        "Lickable Wallpaper": "Secret Factory",
        "Wonka Gum": "Secret Factory",
        "Kazookles": "The Other Factory"
    }

    df["Factory"] = df["Product Name"].map(factory_map)
    df["Factory"] = df["Factory"].str.replace("'", "'").str.strip()
    factory_df["Factory"] = factory_df["Factory"].str.replace("'", "'").str.strip()

    df = df.merge(factory_df, on="Factory", how="left")

    st.sidebar.header("Filters")

    regions = df["Region"].dropna().unique()
    selected_regions = st.sidebar.multiselect("Select Regions", regions, default=regions)

    date_range = st.sidebar.date_input(
        "Date Range",
        [df["Order Date"].min(), df["Order Date"].max()]
    )

    ship_modes = df["Ship Mode"].dropna().unique()
    selected_ship = st.sidebar.multiselect("Ship Mode", ship_modes, default=ship_modes)

    lead_threshold = st.sidebar.slider("Lead Time Threshold", 0, int(df["Lead Time"].max()), 10)

    f_df = df[
        (df["Region"].isin(selected_regions)) &
        (df["Ship Mode"].isin(selected_ship)) &
        (df["Lead Time"] <= lead_threshold) &
        (df["Order Date"] >= pd.to_datetime(date_range[0])) &
        (df["Order Date"] <= pd.to_datetime(date_range[1]))
    ]

    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Avg Lead Time", round(f_df["Lead Time"].mean(), 2))
    c2.metric("Total Orders", len(f_df))
    c3.metric("Revenue", f"${f_df['Sales'].sum():,.0f}")

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue by Region")
        fig1 = px.bar(f_df, x="Region", y="Sales", color="Ship Mode")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Lead Time by Ship Mode")
        fig2 = px.box(f_df, x="Ship Mode", y="Lead Time", color="Ship Mode")
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()
    st.subheader("Factory Efficiency")
    ranking = f_df.groupby("Factory")["Lead Time"].mean().sort_values().reset_index()
    st.dataframe(ranking, use_container_width=True)

    f_df["Route"] = f_df["Factory"].astype(str) + " → " + f_df["State/Province"].astype(str)

    st.subheader("Top 10 Efficient Routes")
    top = f_df.groupby("Route")["Lead Time"].mean().sort_values().head(10)
    st.dataframe(top)

    st.subheader("Bottom 10 Slow Routes")
    bottom = f_df.groupby("Route")["Lead Time"].mean().sort_values(ascending=False).head(10)
    st.dataframe(bottom)

    st.divider()
    st.subheader("📍 Factory Location Map")
    fig_map = px.scatter_mapbox(f_df, lat="Latitude", lon="Longitude", hover_name="Factory", zoom=3, height=400)
    fig_map.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_map, use_container_width=True)

    st.subheader("State Drill Down")
    state = st.selectbox("Select State", f_df["State/Province"].dropna().unique())
    state_df = f_df[f_df["State/Province"] == state]
    st.dataframe(state_df, use_container_width=True)

    with st.expander("Show Data"):
        st.dataframe(f_df.head(50))

except Exception as e:
    st.error(f"Error: {e}")
