import streamlit as st
import pandas as pd 
import sys
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UTILS_Path=os.path.join(BASE_DIR, 'utils')
sys.path.append(UTILS_Path)

#Acess helper functions
from recommender import fetch_recommendations

#Page configuration
st.set_page_config(
    page_title="SmartCart Ai",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

#Load Dataset
@st.cache_data
def load_data():
    sales_data = pd.read_csv(
        os.path.join(BASE_DIR, 'data', 'cleaned_data.csv')
    )

    association_data = pd.read_csv(
        os.path.join(BASE_DIR, 'data', 'association_rules.csv')
    )

    return sales_data, association_data


ssales_data, association_data = load_data()


ssales_data, association_data = load_data()
st.write("Association Rules Shape:", association_data.shape)
st.write("Unique Antecedents:", association_data['antecedents'].nunique())
st.write("Unique Consequents:", association_data['consequents'].nunique())
st.title("SmartCart Ai  Recommendation Engine🛒")
st.markdown("""This intelligent recommmedation system analyzes customer purchasing behaviour and suggests products frequently bought together using association rule minning.""")

#Sidebar
st.sidebar.header("Navigation")
menu=st.sidebar.radio("Select section",[ "Recommendation System", "Top Products Analytics"])

@st.cache_data
def get_products(data):
    return sorted(data['item_name'].unique())
#Section 1: Recommendation Engine
if menu == "Recommendation System":
    st.subheader("Product Recommendation Panel")
    print(ssales_data.columns)
    available_products = get_products(ssales_data)
    chosen_product = st.selectbox("Choose a Product", available_products)

if st.button("Generate Recommendations"):
    st.write("Selected Product:", chosen_product)
    suggested_items = fetch_recommendations(chosen_product, association_data)

    st.write(f"### Recommendations for: {chosen_product}")

    if suggested_items:
        for index, item in enumerate(suggested_items, start=1):
            st.success(f"{index}. {item}")
    else:
        st.warning("No recommendation patterns found for this item.")


#Section 2: Analytics Dashboard
elif menu == "Top Products Analytics":
    st.subheader(" Most Purchased Products")
    top_products=(ssales_data['item_name'].value_counts().head(15))
    st.bar_chart(top_products)
    st.subheader("Product Frequency Table")
    frequency_df=top_products.reset_index()
    frequency_df.columns=['Product Name','Purchase Count']
    st.dataframe(frequency_df)



#Footer
st.markdown("""---""")
st.caption("Developed as an Ai Aided E-commerce Recommendations Analytics Project by Tripti.")                  