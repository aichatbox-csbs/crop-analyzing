import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Define crop data
crops = {
    'Rice': {
        'process': 'Land preparation, transplanting seedlings, water management, harvesting.',
        'optimal_period': 'June to November',
        'soil_type': 'Clayey soil with good water retention',
        'rotation_strategies': ['Lentil', 'Chickpea', 'Mustard'],
        'soil_health': 'Incorporate green manure crops like Sesbania to enhance nitrogen content.',
        'water_management': 'Maintain 5 cm of standing water during vegetative growth.',
        'water_requirement': '450-700 mm',
        'past_yields': [3.2, 3.5, 3.8, 3.6, 4.0]
    },
    'Wheat': {
        'process': 'Soil tillage, sowing seeds, irrigation, and harvesting.',
        'optimal_period': 'November to April',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Mustard', 'Pea', 'Sunflower'],
        'soil_health': 'Rotate with legumes to improve soil fertility.',
        'water_management': 'Irrigate at crown root initiation, tillering, flowering, and grain filling stages.',
        'water_requirement': '400-500 mm',
        'past_yields': [3.2, 3.5, 3.8, 4.0, 4.2, 4.5]
        
    },
    'Maize': {
        'process': 'Land preparation, seed sowing, fertilization, and harvesting.',
        'optimal_period': 'June to October',
        'soil_type': 'Well-drained fertile soil',
        'rotation_strategies': ['Soybean', 'Blackgram', 'Pea'],
        'soil_health': 'Use cover crops like clover to prevent soil erosion.',
        'water_management': 'Ensure adequate moisture during tasseling and silking stages.',
        'water_requirement': '500-800 mm',
        'past_yields': [2.8, 3.0, 3.3, 3.5, 3.7, 4.0]
    },
    'Cotton': {
        'process': 'Seed sowing, thinning, weeding, fertilization, and harvesting.',
        'optimal_period': 'April to September',
        'soil_type': 'Loamy soil with good drainage',
        'rotation_strategies': ['Groundnut', 'Soybean', 'Maize'],
        'soil_health': 'Incorporate organic matter to maintain soil structure.',
        'water_management': 'Requires regular irrigation, especially during flowering and boll formation.',
        'water_requirement': '700-1300 mm',
        'past_yields': [1.5, 1.7, 1.8, 2.0, 2.1, 2.3]
    },
    'Sugarcane': {
        'process': 'Land preparation, sett planting, fertilization, irrigation, and harvesting.',
        'optimal_period': 'October to March',
        'soil_type': 'Deep, well-drained loamy soil',
        'rotation_strategies': ['Pulses', 'Vegetables', 'Legumes'],
        'soil_health': 'Use trash mulching to conserve moisture and improve organic matter.',
        'water_management': 'Requires frequent irrigation; avoid waterlogging.',
        'water_requirement': '1500-2500 mm',
        'past_yields': [65, 68, 70, 72, 75, 78]
    },
    'Carrot': {
        'process': 'Seed sowing, thinning, weeding, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Loose, sandy loam soil',
        'rotation_strategies': ['Onions', 'Garlic', 'Tomato'],
        'soil_health': 'Maintain soil pH between 6.0 and 6.8 for optimal growth.',
        'water_management': 'Keep soil consistently moist; avoid waterlogging.',
        'water_requirement': '350-500 mm',
        'past_yields': [20, 22, 24, 26, 28, 30]
    },
    'Beetroot': {
        'process': 'Seed sowing, thinning, weeding, and harvesting.',
        'optimal_period': 'September to November',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Cabbage', 'Lettuce', 'Onion'],
        'soil_health': 'Incorporate compost to enhance soil fertility.',
        'water_management': 'Regular watering is essential; avoid drought stress.',
        'water_requirement': '400-600 mm',
        'past_yields': [18, 19, 20, 21, 22, 23]
    },
    'Watermelon': {
        'process': 'Seed sowing, vine training, weeding, and harvesting.',
        'optimal_period': 'January to March',
        'soil_type': 'Sandy loam soil with good drainage',
        'rotation_strategies': ['Maize', 'Sunflower', 'Soybean'],
        'soil_health': 'Maintain soil pH between 6.0 and 7.5.',
        'water_management': 'Requires ample water during fruit development.',
        'water_requirement': '600-800 mm',
        'past_yields': [25, 26, 28, 30, 32, 35]
    },
    'Tomato': {
        'process': 'Seedling preparation, transplanting, staking, pruning, and harvesting.',
        'optimal_period': 'February to April',
        'soil_type': 'Well-drained sandy loam soil with rich organic matter',
        'rotation_strategies': ['Carrots', 'Onions', 'Legumes'],
        'soil_health': 'Incorporate compost to improve soil structure and fertility.',
        'water_management': 'Regular watering; avoid wetting foliage to prevent diseases.',
        'water_requirement': '400-600 mm',
        'past_yields': [35, 38, 40, 42, 45, 48]
    },
    'Onion': {
        'process': 'Seed sowing, transplanting, weeding, and harvesting.',
        'optimal_period': 'November to February',
        'soil_type': 'Fertile, well-drained loamy soil',
        'rotation_strategies': ['Carrots', 'Lettuce', 'Beetroot'],
        'soil_health': 'Maintain soil pH between 6.0 and 7.0.',
        'water_management': 'Consistent moisture is crucial; avoid water stress.',
        'water_requirement': '350-550 mm',
        'past_yields':  [25, 27, 28, 30, 32, 35]
    },
    'Garlic': {
        'process': 'Clove planting, weeding, fertilization, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Well-drained loamy soil with high organic matter',
        'rotation_strategies': ['Tomatoes', 'Peppers', 'Eggplant'],
        'soil_health': 'Incorporate well-rotted manure to enhance fertility.',
        'water_management': 'Regular watering; reduce moisture as bulbs mature.',
        'water_requirement': '400-600 mm',
        'past_yields': [10, 11, 12, 13, 14, 15]
    },
    'Cabbage': {
        'process': 'Seedling preparation, transplanting, weeding, and harvesting.',
        'optimal_period': 'September to November',
        'soil_type': 'Fertile, well-drained loamy soil',
        'rotation_strategies': ['Peas', 'Beans', 'Carrots'],
        'soil_health': 'Maintain soil pH between 6.5 and 7.5.',
        'water_management': 'Requires consistent moisture; mulch to conserve water.',
        'water_requirement': '350-500 mm',
        'past_yields': [30, 32, 34, 36, 38, 40]
    },
    'Cauliflower': {
        'process': 'Seedling preparation, transplanting, weeding, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Well-drained loamy soil rich in organic matter',
                'rotation_strategies': ['Tomatoes', 'Lettuce', 'Carrots'],
        'soil_health': 'Use compost and organic matter to improve soil structure.',
        'water_management': 'Regular watering to keep soil moist but not waterlogged.',
        'water_requirement': '400-600 mm',
        'past_yields': [28, 29, 30, 31, 32, 34]
    },
    'Pumpkin': {
        'process': 'Direct seed sowing, vine training, fertilization, and harvesting.',
        'optimal_period': 'February to April',
        'soil_type': 'Well-drained sandy loam soil with rich organic matter',
        'rotation_strategies': ['Corn', 'Beans', 'Sunflowers'],
        'soil_health': 'Use mulch to retain moisture and control weeds.',
        'water_management': 'Requires frequent watering during fruit development.',
        'water_requirement': '500-800 mm',
        'past_yields': [15, 16, 18, 20, 22, 24]
    },
    'Chickpea': {
        'process': 'Soil preparation, direct seed sowing, weeding, and harvesting.',
        'optimal_period': 'October to November',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Maize', 'Mustard', 'Wheat'],
        'soil_health': 'Fixes nitrogen in the soil, improving fertility.',
        'water_management': 'Minimal irrigation required; avoid waterlogging.',
        'water_requirement': '300-400 mm',
        'past_yields': [1.8, 2.0, 2.2, 2.5, 2.7, 3.0]
    },
    'Blackgram': {
        'process': 'Land preparation, seed sowing, weeding, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Fertile, well-drained loamy soil',
        'rotation_strategies': ['Rice', 'Wheat', 'Maize'],
        'soil_health': 'Incorporate legume residues to improve soil nitrogen levels.',
        'water_management': 'Requires moderate watering; avoid excess moisture.',
        'water_requirement': '350-500 mm',
        'past_yields': [1.2, 1.3, 1.5, 1.6, 1.7, 1.9]
    },
    'Pigeon Peas': {
        'process': 'Direct seed sowing, weeding, fertilization, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Well-drained sandy loam soil',
        'rotation_strategies': ['Maize', 'Wheat', 'Rice'],
        'soil_health': 'Enhances soil fertility by fixing nitrogen.',
        'water_management': 'Requires deep watering at flowering and pod formation stages.',
        'water_requirement': '500-700 mm',
        'past_yields': [2.5, 2.6, 2.8, 3.0, 3.2, 3.5]
    },
    'Soybean': {
        'process': 'Land preparation, seed sowing, weeding, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Well-drained fertile loamy soil',
        'rotation_strategies': ['Maize', 'Wheat', 'Sunflower'],
        'soil_health': 'Fixes nitrogen in the soil, improving fertility.',
        'water_management': 'Requires consistent moisture; avoid waterlogging.',
        'water_requirement': '500-700 mm',
        'past_yields': [2.8, 3.0, 3.3, 3.5, 3.7, 4.0]
    },
    'Mustard': {
        'process': 'Soil tillage, direct seed sowing, fertilization, and harvesting.',
        'optimal_period': 'September to October',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Wheat', 'Peas', 'Lentils'],
        'soil_health': 'Use organic compost to improve soil fertility.',
        'water_management': 'Requires moderate irrigation at flowering and seed formation stages.',
        'water_requirement': '350-500 mm',
        'past_yields': [1.5, 1.6, 1.8, 2.0, 2.1, 2.3]
    },
    'Groundnut': {
        'process': 'Land preparation, seed sowing, weeding, and harvesting.',
        'optimal_period': 'June to July',
        'soil_type': 'Sandy loam soil with good drainage',
        'rotation_strategies': ['Wheat', 'Maize', 'Pulses'],
        'soil_health': 'Incorporate crop residues to improve organic matter.',
        'water_management': 'Requires irrigation during flowering and pod development.',
        'water_requirement': '500-700 mm',
        'past_yields': [2.5, 2.7, 2.9, 3.0, 3.2, 3.5] 
    },
    'Peas': {
        'process': 'Soil preparation, seed sowing, staking, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Carrots', 'Lettuce', 'Cabbage'],
        'soil_health': 'Improves soil nitrogen content through symbiotic fixation.',
        'water_management': 'Regular watering is essential, especially during flowering.',
        'water_requirement': '350-500 mm',
        'past_yields': [20, 21, 22, 23, 24, 26]
    },
    'Potato': {
        'process': 'Soil tillage, seed tuber planting, earthing up, and harvesting.',
        'optimal_period': 'October to December',
        'soil_type': 'Sandy loam soil rich in organic matter',
        'rotation_strategies': ['Peas', 'Carrots', 'Cabbage'],
        'soil_health': 'Use well-rotted compost to enrich soil fertility.',
        'water_management': 'Requires frequent irrigation; avoid waterlogging.',
        'water_requirement': '500-800 mm',
        'past_yields': [35, 38, 40, 42, 45, 48]
    },
    'Sunflower': {
        'process': 'Seed sowing, fertilization, weeding, and harvesting.',
        'optimal_period': 'February to March',
        'soil_type': 'Well-drained loamy soil',
        'rotation_strategies': ['Wheat', 'Maize', 'Soybean'],
        'soil_health': 'Use crop residues to maintain soil organic matter.',
        'water_management': 'Requires irrigation during flowering and seed filling.',
        'water_requirement': '400-600 mm',
        'past_yields': [1.8, 2.0, 2.2, 2.3, 2.5, 2.7]
    }
}
def get_crop_details(crop_name):
    return crops.get(crop_name, {})

# Function to display crop information
def display_crop_info(crop_name):
    crop = get_crop_details(crop_name)
    if crop:
       
        st.markdown(f"## 🌱 {crop_name} Cultivation Process")
        st.markdown(f"*🔹 NEXT CROP* {crop['rotation_strategies']}")
        st.markdown(f"*🔹 Optimal Planting Period:* {crop['optimal_period']}")
        st.markdown(f"*🔹 Water Requirement:* {crop['water_requirement']}")
        st.markdown(f"*🔹 Suitable Soil Type:* {crop['soil_type']}")
        st.markdown(f"*🔹 Cultivation Steps:* {crop['process']}")

# Function to display past history
def display_past_history(crop_name):
    crop = get_crop_details(crop_name)
    if crop:
        st.markdown(f"## 📜 Past History of {crop_name} Cultivation")
        
        history_data = {
            "Category": ["Rotation Crops", "Soil Health", "Water Management"],
            "Details": [', '.join(crop['rotation_strategies']), crop['soil_health'], crop['water_management']]
        }
        st.dataframe(history_data, width=700)
        # Select crop dynamically
crop = st.selectbox("Select a Crop", list(crops.keys()))  # User selects crop
crop_data = crops[crop]  # Access crop details

# Define years for past yields
years = [2019, 2020, 2021, 2022, 2023]

# Create DataFrame
df = pd.DataFrame({'Year': years, 'Yield (tons)': crop_data['past_yields']})

# Create Matplotlib bar chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(df['Year'], df['Yield (tons)'], color='green', edgecolor='black')

# Customize plot
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Yield (tons)", fontsize=12)
ax.set_title(f"{crop} Past Yields Over the Years", fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot in Streamlit
st.pyplot(fig)


# Streamlit UI with Sidebar Navigation
st.set_page_config(page_title="Smart Farming Assistant", layout="wide")

st.sidebar.title("🌾 Smart Farming Assistant")
selected_option = st.sidebar.radio("Navigation", ["Home", "Crop Details", "Past History"])

st.sidebar.markdown("### 🌍 Select a Crop")
selected_crop = st.sidebar.selectbox("Choose a crop:", list(crops.keys()))

st.sidebar.markdown("💡 Developed to support farmers with optimized cultivation practices.JAI KISAAN!  JAI JAVAAN !!")

# Page Routing
if selected_option == "Home":
    st.title("Welcome to the Smart FARMING Assistant 🚜")
    st.markdown("""
        This tool provides insights into various crops, including:
        - 🔄 CROP Rotation Strategies  
        - 🌱 Best planting periods  
        - 🌾 Suitable soil types  
        - 💧 Water management techniques  
        - 📜 Past cultivation histories  
        
        Use the sidebar navigation to explore detailed information!
    """)

elif selected_option == "Crop Details":
    if selected_crop:
        display_crop_info(selected_crop)

elif selected_option == "Past History":
    if selected_crop:
        display_past_history(selected_crop)
