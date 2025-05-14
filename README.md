# AI-powered-Recipe-Assist
This is an interactive web application built with **Streamlit** that allows users to explore over **6,800+ Indian food recipes**. Users can search and filter recipes based on various factors such as cuisine, diet type, course, total cooking time, and ingredients.

---

## 📦 Dataset Overview

- **Total Recipes:** 6,871
- **File Name:** `IndianFoodDatasetCSV.csv`
- **Format:** CSV
- **Main Columns Used for Recipe Suggestions and Filtering:**
  - `TranslatedRecipeName`: Name of the recipe (English)
  - `TranslatedIngredients`: Ingredients list
  - `Cuisine`: Regional cuisine (e.g., Punjabi, South Indian, Maharashtrian)
  - `Course`: Meal type (e.g., Breakfast, Snack, Dessert)
  - `Diet`: Dietary classification (e.g., Vegetarian, Vegan, Diabetic Friendly)
  - `TotalTimeInMins`: Total time to prepare and cook the dish
  - `Servings`: Number of servings
  - `TranslatedInstructions`: Cooking steps

These columns are used to **filter**, **search**, and **display** recipes dynamically in the Streamlit interface.
---
## 🎯 Purpose

The primary goal of this project is to:
- Help users find Indian recipes quickly based on dietary preferences and time availability.
- Provide an intuitive interface for food enthusiasts to explore diverse Indian cuisines.
- Offer full recipe instructions, ingredients, and nutritional context.

---

## 💻 Built Using

### ✅ 1. Streamlit
**Purpose:** Build the web-based user interface.

**Why:**
- Create interactive widgets like dropdowns, sliders, and buttons.
- Display filtered recipe results in real time.
- Build dynamic web pages that respond to user input.

📦 Installation:
```bash
pip install streamlit

✅ 2. pandas
Purpose: Load and manipulate the recipe data from the CSV file.

Why:

Load dataset using pd.read_csv()

Filter recipes by selected criteria (Cuisine, Diet, Course, etc.)

Easily access specific records using .iloc[], .dropna(), etc.

📦 Installation:

bash
Copy
Edit
pip install pandas

✅ 3. @st.cache_data Decorator
Purpose: Cache the dataset load to speed up app performance.

Why:

Prevents reloading the dataset on every app rerun

Enhances responsiveness of the app

📦 No installation required (built-in with Streamlit)
