# Import python packages
import streamlit as st
import requests
from snowflake.snowpark.functions import col
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Restaurant Application")

# Function to submit order
def submit_order(ingredients, name_on_order):
    # You can replace this with your backend API call to submit the order
    # For demonstration purposes, let's print the order details
    print("Order Details:")
    print("Name on Order:", name_on_order)
    print("Ingredients:", ingredients)
    # You can also make an API call to store the order in your database
    st.success("Your order has been submitted successfully!")

# Main content of the application
st.write("Welcome to our restaurant!")
st.write("Choose the items from the menu on the left and submit your order.")

# List of items (dummy data)
# cnx= st.connection("snowflake")
# session= cnx.session()
session = get_active_session()
my_dataframe = session.table("MY_RESTAURENT_APP.RESTURENT_ITEMS.food_items").select(col('FOOD_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)




menu_items=st.multiselect(
    'choose up to 5 ingredients:',
    my_dataframe,
    max_selections=5
)



# Display menu on the left side
selected_items = st.sidebar.multiselect("Menu", menu_items, menu_items)

# Collect user details
name_on_order = st.text_input("Name on Order")

# Submit order button
if st.button("Submit Order"):
    if not selected_items:
        st.error("Please select at least one item from the menu.")
    elif not name_on_order:
        st.error("Please enter your name for the order.")
    else:
        # Convert selected items to a string
        ingredients_string = ', '.join(selected_items)
        # Call function to submit order
        submit_order(ingredients_string, name_on_order)
        # Reset selections
        selected_items = []

# Feedback and rating
st.write("Thank you for ordering with us! Please provide your feedback and rating below.")
feedback = st.text_area("Feedback")
rating = st.slider("Rating", min_value=1, max_value=5)

# Submit feedback button
if st.button("Submit Feedback"):
    # You can implement the functionality to submit feedback here
    st.success("Thank you for your feedback and rating!")
