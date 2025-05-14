import streamlit as st
import pandas as pd

# Streamlit page settings
st.set_page_config(page_title="AI Food Recipe Generator", layout="centered")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("IndianFoodDatasetCSV.csv")
    return df.dropna(subset=['RecipeName'])

df = load_data()

st.title("🍽️ AI Food Recipe Generator")


# Language selection
lang = st.radio("Select Language / भाषा चुनें:", ["English", "Hindi"], horizontal=True)



# Filters
with st.sidebar:
    st.header("Filter Recipes")
    cuisine = st.selectbox("Cuisine", ["All"] + sorted(df['Cuisine'].dropna().unique().tolist()))
    diet = st.selectbox("Diet", ["All"] + sorted(df['Diet'].dropna().unique().tolist()))
    course = st.selectbox("Course", ["All"] + sorted(df['Course'].dropna().unique().tolist()))
    max_time = st.slider("Max Total Time (mins)", 0, 180, 60)

# Apply filters
filtered_df = df.copy()
if cuisine != "All":
    filtered_df = filtered_df[filtered_df['Cuisine'] == cuisine]
if diet != "All":
    filtered_df = filtered_df[filtered_df['Diet'] == diet]
if course != "All":
    filtered_df = filtered_df[filtered_df['Course'] == course]
filtered_df = filtered_df[filtered_df['TotalTimeInMins'] <= max_time]

# Autocomplete search bar
if lang == "English":
    recipe_names = filtered_df['RecipeName'].dropna().unique().tolist()
else:
    recipe_names = filtered_df['TranslatedRecipeName'].dropna().unique().tolist()

selected_recipe = st.selectbox("Search Recipe", sorted(recipe_names))

# Button to show recipe
display = st.button("Get Recipe")

# Display recipe info
if display:
    if lang == "English":
        result = df[df['RecipeName'] == selected_recipe].iloc[0]
        st.header(result['RecipeName'])
        st.subheader("Ingredients")
        st.write(result['TranslatedIngredients'])
        st.subheader("Instructions")
        st.write(result['TranslatedInstructions'])
    else:
        result = df[df['TranslatedRecipeName'] == selected_recipe].iloc[0]
        st.header(result['TranslatedRecipeName'])
        st.subheader("की सामग्री")  # Ingredients
        st.write(result['Ingredients'])
        st.subheader("निर्देश")  # Instructions
        st.write(result['Instructions'])

    # Additional info
    st.markdown("---")
    st.markdown(f"**Cuisine:** {result['Cuisine']}")
    st.markdown(f"**Course:** {result['Course']}")
    st.markdown(f"**Diet:** {result['Diet']}")
    st.markdown(f"**Prep Time:** {result['PrepTimeInMins']} mins")
    st.markdown(f"**Cook Time:** {result['CookTimeInMins']} mins")
    st.markdown(f"**Total Time:** {result['TotalTimeInMins']} mins")
    st.markdown(f"**Servings:** {result['Servings']}")
    st.markdown(f"[🔗 View Full Recipe Link]({result['URL']})")
