import streamlit as st
from snowflake.snowpark.functions import col
from snowflake.snowpark.context import get_active_session

# Define a function to authenticate users
def authenticate(username, password):
    # In a real application, you would authenticate against a database or another service
    # For demonstration purposes, we'll use hardcoded credentials
    valid_username = "user"
    valid_password = "password"
    
    if username == valid_username and password == valid_password:
        return True
    else:
        return False

# Define the login page content
def login():
    st.title("Login")

    # Collect user credentials
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Submit login button
    if st.button("Login"):
        if authenticate(username, password):
            st.experimental_set_query_params(logged_in=True)
        else:
            st.error("Invalid username or password")

# Define the app page content
def app():
    st.title("Restaurant Application")

    st.write("Welcome to our restaurant!")
    st.write("Choose the items from the menu below and submit your order.")

    # Fetching menu items from Snowflake
    session = get_active_session()
    my_dataframe = session.table("MY_RESTAURENT_APP.RESTURENT_ITEMS.food_items").select(col('FOOD_NAME'))
    menu_items = my_dataframe.to_pandas()['FOOD_NAME'].tolist()

    # Sidebar with multiselect dropdown menu for menu selection
    selected_items = st.sidebar.multiselect("Menu Selection", menu_items)

    # Collect user details
    name_on_order = st.text_input("Name on Order")

    # Submit order button
    if st.button("Submit Order"):
        if not selected_items:
            st.error("Please select at least one item from the menu.")
        elif not name_on_order:
            st.error("Please enter your name for the order.")
        else:
            # Call function to submit order
            submit_order(selected_items, name_on_order)

    # Feedback and rating
    st.write("Thank you for ordering with us! Please provide your feedback and rating below.")
    feedback = st.text_area("Feedback")
    rating = st.slider("Rating", min_value=1, max_value=5)

    # Submit feedback button
    if st.button("Submit Feedback"):
        # You can implement the functionality to submit feedback here
        st.success("Thank you for your feedback and rating!")

# Main content of the application
def main():
    if "logged_in" not in st.experimental_get_query_params():
        login()
    else:
        app()

# Run the application
if __name__ == "__main__":
    main()
