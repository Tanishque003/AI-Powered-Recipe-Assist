import streamlit as st
import google.generativeai as genai

# Set your Gemini API key here
genai.configure(api_key="your api key")

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Recipe list (you can add more recipes here)
recipe_names = sorted([
    "Apple Pie", "Banana Bread", "Butter Chicken", "Chicken Biryani", "Chocolate Cake",
    "Dosa", "Egg Curry", "Fish Tikka", "Garlic Bread", "Hummus", "Ice Cream",
    "Jambalaya", "Kofta", "Lasagna", "Mango Smoothie", "Noodles", "Omelette",
    "Pasta Alfredo", "Quiche", "Ramen", "Samosa", "Tacos", "Udon", "Vegetable Curry",
    "Waffles", "Xacuti", "Yogurt Parfait", "Zucchini Fritters"
])

# Streamlit page settings
st.set_page_config(page_title="AI Food Recipe Generator", layout="centered")

# Language selector
language = st.selectbox("🌐 Select Language / भाषा चुनें:", ["English", "हिंदी"])

# Define text labels based on selected language
if language == "English":
    title = "🍽️ AI Food Recipe Generator"
    search_label = "Search or select a recipe:"
    button_label = "Get Recipe"
    loading_text = "Generating recipe using Gemini..."
    error_text = "Failed to generate recipe"
    recipe_heading = "📋 Recipe for"
    prompt_template = "Give me a detailed recipe for {} including ingredients and preparation steps. Write in English."
else:
    title = "🍽️ एआई फूड रेसिपी जेनरेटर"
    search_label = "कोई रेसिपी खोजें या चुनें:"
    button_label = "रेसिपी प्राप्त करें"
    loading_text = "Gemini से रेसिपी प्राप्त की जा रही है..."
    error_text = "रेसिपी जनरेट करने में विफल"
    recipe_heading = "📋 रेसिपी:"
    prompt_template = "{} की विस्तृत रेसिपी बताएं जिसमें सामग्री और बनाने की विधि शामिल हो। कृपया हिंदी में लिखें।"

# Show title
st.title(title)

# Recipe selection dropdown
selected_recipe = st.selectbox(search_label, options=recipe_names)

# Generate Recipe Button
if st.button(button_label):
    with st.spinner(loading_text):
        prompt = prompt_template.format(selected_recipe)
        try:
            response = model.generate_content(prompt)
            st.subheader(f"{recipe_heading} {selected_recipe}")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"{error_text}: {e}")
