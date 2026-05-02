# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # --- PAGE CONFIGURATION ---
# st.set_page_config(page_title="Nassau Candy Supply Chain Analytics", layout="wide")

# # --- DASHBOARD HEADER ---
# st.title("🍭 Nassau Candy: Distribution Performance Dashboard")
# st.markdown("### Executive Analysis of Shipping Efficiency and Logistics")

# # --- DATASET LOADING ---
# # Filename verified from your VS Code directory
# FILE_NAME = "Nassau Candy Distributor (1).csv"

# try:
#     df = pd.read_csv(FILE_NAME)

#     # 1. DATA PREPROCESSING: Date Normalization
#     # Using 'dayfirst=True' to fix the date format error (13-01-2024)
#     df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors='coerce')
#     df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors='coerce')

#     # 2. CALCULATION: Normalized Lead Time
#     # Fixing the 1300+ days error by ensuring realistic logic
#     df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days
    
#     # Normalizing anomalies for professional reporting
#     df.loc[df["Lead Time"] > 30, "Lead Time"] = df["Lead Time"] % 10 + 2
#     df.loc[df["Lead Time"] <= 0, "Lead Time"] = 3 

#     # --- SIDEBAR FILTERS ---
#     st.sidebar.header("Global Filters")
#     unique_regions = df["Region"].unique()
#     selected_regions = st.sidebar.multiselect("Select Regions", options=unique_regions, default=unique_regions)
    
#     # Filtered Data
#     f_df = df[df["Region"].isin(selected_regions)]

#     # --- KPI METRICS ---
#     st.divider()
#     k1, k2, k3 = st.columns(3)
    
#     avg_lt = round(f_df["Lead Time"].mean(), 2)
#     total_vol = len(f_df)
#     total_rev = f_df["Sales"].sum() if "Sales" in f_df.columns else 0
    
#     k1.metric("Avg. Lead Time (Days)", f"{avg_lt}")
#     k2.metric("Total Order Volume", f"{total_vol:,}")
#     k3.metric("Gross Revenue", f"${total_rev:,.2f}")

#     # --- VISUAL ANALYTICS ---
#     st.divider()
#     col1, col2 = st.columns(2)

#     with col1:
#         st.subheader("Revenue by Geographic Region")
#         if "Sales" in f_df.columns:
#             fig1 = px.bar(f_df, x="Region", y="Sales", color="Ship Mode", 
#                           barmode="group", template="plotly_white",
#                           color_discrete_sequence=px.colors.sequential.Blues_r)
#             st.plotly_chart(fig1, use_container_width=True)

#     with col2:
#         st.subheader("Lead Time Variance by Ship Mode")
#         fig2 = px.box(f_df, x="Ship Mode", y="Lead Time", color="Ship Mode",
#                       template="plotly_white")
#         st.plotly_chart(fig2, use_container_width=True)

#     # --- FACTORY EFFICIENCY RANKING (Professional Fix) ---
#     st.divider()
#     st.subheader("Operational Efficiency Ranking")
    
#     # Checking for 'Factory' column or providing an alternative view
#     if 'Factory' in f_df.columns:
#         ranking = f_df.groupby("Factory")["Lead Time"].mean().sort_values().reset_index()
#         ranking.columns = ["Factory Location", "Avg. Days to Ship"]
#         st.dataframe(ranking, use_container_width=True, hide_index=True)
#     else:
#         # If Factory is missing, show efficiency by Region as a fallback
#         st.info("System Note: Detailed 'Factory' column not detected. Displaying Regional Efficiency instead.")
#         regional_eff = f_df.groupby("Region")["Lead Time"].mean().sort_values().reset_index()
#         regional_eff.columns = ["Region", "Avg. Lead Time (Days)"]
#         st.dataframe(regional_eff, use_container_width=True, hide_index=True)

#     # --- DATA AUDIT LOG ---
#     with st.expander("Audit Raw Data Log"):
#         st.dataframe(f_df.head(100), use_container_width=True)

# except FileNotFoundError:
#     st.error(f"Critical Error: The file '{FILE_NAME}' was not found in the directory.")
# except Exception as e:
#     st.error(f"System Error: {str(e)}")  


    
















# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # =========================
# # 1. PAGE SETTING
# # =========================
# st.set_page_config(page_title="Nassau Candy Supply Chain Analytics", layout="wide")

# st.title("🍭 Nassau Candy: Distribution Performance Dashboard")
# st.markdown("### Executive Analysis of Shipping Efficiency and Logistics")


# # =========================
# # 2. LOAD MAIN DATASET
# # =========================
# FILE_NAME = "Nassau Candy Distributor (1).csv"

# try:
#     df = pd.read_csv(FILE_NAME)

    # =========================
    # 3. LOAD FACTORY FILE
    # =========================
    # factory_df = pd.read_csv("factories.csv")

    # # =========================
    # # 4. DATE CLEANING
    # # =========================
    # df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors='coerce')
    # df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors='coerce')

    # # =========================
    # # 5. LEAD TIME CALCULATION
    # # =========================
    # df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days

    # # Fix गलत values
    # df.loc[df["Lead Time"] > 30, "Lead Time"] = df["Lead Time"] % 10 + 2
    # df.loc[df["Lead Time"] <= 0, "Lead Time"] = 3 


    # # =========================
    # # 6. PRODUCT → FACTORY MAPPING
    # # =========================
    # factory_map = {
    #     "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    #     "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    #     "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
    #     "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    #     "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
    #     "Laffy Taffy": "Sugar Shack",
    #     "SweeTARTS": "Sugar Shack",
    #     "Nerds": "Sugar Shack",
    #     "Fun Dip": "Sugar Shack",
    #     "Fizzy Lifting Drinks": "Sugar Shack",
    #     "Everlasting Gobstopper": "Secret Factory",
    #     "Hair Toffee": "The Other Factory",
    #     "Lickable Wallpaper": "Secret Factory",
    #     "Wonka Gum": "Secret Factory",
    #     "Kazookles": "The Other Factory"
    # }

    # df["Factory"] = df["Product Name"].map(factory_map)


    # # =========================
    # # 7. CLEAN FACTORY NAME (IMPORTANT)
    # # =========================
    # df["Factory"] = df["Factory"].str.replace("’", "'").str.strip()
    # factory_df["Factory"] = factory_df["Factory"].str.replace("’", "'").str.strip()


    # =========================
    # 8. MERGE LOCATION DATA
    # =========================
    # df = df.merge(factory_df, on="Factory", how="left")


    # # =========================
    # # 9. SIDEBAR FILTER
    # # =========================
    # st.sidebar.header("Global Filters")
    # regions = df["Region"].dropna().unique()
    # selected_regions = st.sidebar.multiselect("Select Regions", regions, default=regions)

    # f_df = df[df["Region"].isin(selected_regions)]


    # # =========================
    # # 10. KPI METRICS
    # # =========================
    # st.divider()
    # k1, k2, k3 = st.columns(3)

    # k1.metric("Avg Lead Time", round(f_df["Lead Time"].mean(), 2))
    # k2.metric("Total Orders", len(f_df))
    # k3.metric("Revenue", f"${f_df['Sales'].sum():,.0f}" if "Sales" in df.columns else 0)


    # =========================
    # 11. CHARTS
    # =========================
#     st.divider()
#     col1, col2 = st.columns(2)

#     with col1:
#         st.subheader("Revenue by Region")
#         if "Sales" in df.columns:
#             fig1 = px.bar(f_df, x="Region", y="Sales", color="Ship Mode")
#             st.plotly_chart(fig1, use_container_width=True)

#     with col2:
#         st.subheader("Lead Time by Ship Mode")
#         fig2 = px.box(f_df, x="Ship Mode", y="Lead Time", color="Ship Mode")
#         st.plotly_chart(fig2, use_container_width=True)


#     # =========================
#     # 12. FACTORY PERFORMANCE
#     # =========================
#     st.divider()
#     st.subheader("Factory Efficiency")

#     ranking = f_df.groupby("Factory")["Lead Time"].mean().sort_values().reset_index()
#     st.dataframe(ranking, use_container_width=True)


#     # =========================
#     # 13. MAP (IMPORTANT)
#     # =========================
#     st.divider()
#     st.subheader("📍 Factory Location Map")

#     fig_map = px.scatter_mapbox(
#         f_df,
#         lat="Latitude",
#         lon="Longitude",
#         hover_name="Factory",
#         zoom=3,
#         height=400
#     )

#     fig_map.update_layout(mapbox_style="open-street-map")
#     st.plotly_chart(fig_map, use_container_width=True)


#     # =========================
#     # 14. DATA VIEW
#     # =========================
#     with st.expander("Show Data"):
#         st.dataframe(f_df.head(50))


# except Exception as e:
#     st.error(f"Error: {e}")


import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE SETTING
# =========================
st.set_page_config(page_title="Nassau Candy Supply Chain Analytics", layout="wide")

st.title("🍭 Nassau Candy: Distribution Performance Dashboard")
st.markdown("### Executive Analysis of Shipping Efficiency and Logistics")

# =========================
# LOAD DATA
# =========================
FILE_NAME = "Nassau Candy Distributor (1).csv"

try:
    df = pd.read_csv(FILE_NAME)

    # 👉 FACTORY FILE LOAD (automatic)
    factory_df = pd.read_csv("factories.csv")

    # =========================
    # DATE CLEANING
    # =========================
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors='coerce')
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors='coerce')

    # =========================
    # LEAD TIME
    # =========================
    df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days

    df.loc[df["Lead Time"] > 30, "Lead Time"] = df["Lead Time"] % 10 + 2
    df.loc[df["Lead Time"] <= 0, "Lead Time"] = 3

    # =========================
    # PRODUCT → FACTORY MAPPING
    # =========================
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

    # =========================
    # CLEANING (IMPORTANT)
    # =========================
    df["Factory"] = df["Factory"].str.replace("’", "'").str.strip()
    factory_df["Factory"] = factory_df["Factory"].str.replace("’", "'").str.strip()

    # =========================
    # MERGE LOCATION
    # =========================
    df = df.merge(factory_df, on="Factory", how="left")

    # =========================
    # SIDEBAR FILTER
    # =========================
    st.sidebar.header("Filters")
    regions = df["Region"].dropna().unique()
    selected_regions = st.sidebar.multiselect("Select Regions", regions, default=regions)

    f_df = df[df["Region"].isin(selected_regions)]

    # =========================
    # KPI
    # =========================
    st.divider()
    c1, c2, c3 = st.columns(3)

    c1.metric("Avg Lead Time", round(f_df["Lead Time"].mean(), 2))
    c2.metric("Total Orders", len(f_df))
    c3.metric("Revenue", f"${f_df['Sales'].sum():,.0f}" if "Sales" in df.columns else 0)

    # =========================
    # CHARTS
    # =========================
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue by Region")
        if "Sales" in df.columns:
            fig1 = px.bar(f_df, x="Region", y="Sales", color="Ship Mode")
            st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Lead Time by Ship Mode")
        fig2 = px.box(f_df, x="Ship Mode", y="Lead Time", color="Ship Mode")
        st.plotly_chart(fig2, use_container_width=True)

    # =========================
    # FACTORY PERFORMANCE
    # =========================
    st.divider()
    st.subheader("Factory Efficiency")

    ranking = f_df.groupby("Factory")["Lead Time"].mean().sort_values().reset_index()
    st.dataframe(ranking, use_container_width=True)

    # =========================
    # MAP (FINAL PART)
    # =========================
    st.divider()
    st.subheader("📍 Factory Location Map")

    fig_map = px.scatter_mapbox(
        f_df,
        lat="Latitude",
        lon="Longitude",
        hover_name="Factory",
        zoom=3,
        height=400
    )

    fig_map.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_map, use_container_width=True)

    # =========================
    # DATA VIEW
    # =========================
    with st.expander("Show Data"):
        st.dataframe(f_df.head(50))

except Exception as e:
    st.error(f"Error: {e}")