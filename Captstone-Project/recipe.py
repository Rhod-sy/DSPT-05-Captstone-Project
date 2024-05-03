import streamlit as st
import pickle
import pandas as pd

# Load recipes from pickle file
with open('combined_recommendations.pkl', 'rb') as f:
    combined_recommendations = pickle.load(f)

# Load your DataFrame 'df' containing recipe data
# Sample DataFrame creation for demonstration

df = pd.read_csv('merged_data.csv')

# Define Streamlit app content
def streamlit_app():
    # Set background color and padding for the entire app
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set title and sidebar color
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #ffffff;
        }
        .sidebar .sidebar-content .block-container {
            color: #333333;
        }
        .sidebar .sidebar-content .stRadio label {
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set title color
    st.markdown(
        """
        <style>
        .css-1v3fvcr {
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Recipe Search App')

    # Create navigation sidebar with custom colors
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Home', 'About', 'Results'])

    # Display content based on selected page
    if page == 'Home':
        st.write('Welcome to Recipe Search App!')
        st.write('Use the navigation on the left to explore.')
    elif page == 'About':
        st.write('This app helps you search for recipes.')
        st.write('It uses a machine learning model to recommend recipes based on your input.')
    elif page == 'Results':
        st.title('Recipe Search Results')

        # Add a text input for searching recipes
        search_recipe_name = st.text_input('Enter your Recipe name:')

        

        # Handle search
        if search_recipe_name:
            if search_recipe_name in combined_recommendations:
                ingredients, rating = combined_recommendations[search_recipe_name]
                st.write(f"Recipe: {search_recipe_name}")
                st.write(f"Ingredients: {', '.join(ingredients)}")
                st.write(f"Ratings: {rating}")
                
                # Render a template with custom background color
                st.markdown(
                    """
                    ## Recipe Template

                    <div style="background-color:#ffffff; padding:10px">
                    <h3 style="color:#333333">Recipe: {recipe_name}</h3>
                    <p><strong>Ingredients:</strong> {ingredient_list}</p>
                    <p><strong>Rating:</strong> {recipe_rating}</p>
                    </div>
                    """.format(recipe_name=search_recipe_name, ingredient_list=', '.join(ingredients), recipe_rating=rating),
                    unsafe_allow_html=True
                )
                
            else:
                st.write("Recipe not found.")

if __name__ == "__main__":
    streamlit_app()
