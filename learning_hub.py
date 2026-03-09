import streamlit as st

st.header("📋 Python & AI Topic Tracker")

# We use a List to store the topics
topics = ["Variables", "Data Types", "Lists", "Dictionaries", "Loops", "Functions"]

# Creating a dynamic list in the UI for your friends
selected_topic = st.selectbox("Choose a topic to learn more:", topics)

if selected_topic == "Lists":
    st.write("### 📝 Learning Lists")
    st.code("""
# Example of a List:
my_portfolio = ["Tata Small Cap", "Axis Silver FoF", "Nifty 50"]
print(my_portfolio[0]) # Output: Tata Small Cap
    """)
    st.info("Challenge for Friends: Try adding a new fund to the list using .append()")

st.divider() # Adds a clean line in your app
st.header("📈 Live Portfolio Manager")

# 1. Initialize the 'Notebook' (Session State)
if 'my_portfolio' not in st.session_state:
    # This only runs the very first time the app loads
    st.session_state.my_portfolio = ["Tata Small Cap", "Axis Silver FoF"]

# 2. Input to add a new fund
new_stock = st.text_input("Enter a stock or fund name (e.g., Nifty 50):")

if st.button("Add to My Portfolio"):
    if new_stock:
        # We append to the list stored in our 'Notebook'
        st.session_state.my_portfolio.append(new_stock)
        st.success(f"Successfully added {new_stock}!")
    else:
        st.warning("Please enter a name first!")

# 3. Display the updated list
st.write("### Your Current Assets:")
for item in st.session_state.my_portfolio:
    st.write(f"- {item}")

st.divider()
st.header("🤖 AI Decision Maker: Nifty 50 Strategy")

# Beginner Goal: Learning 'If-Else' statements
target_profit = st.number_input("What is your Target Profit %?", value=10)
current_gain = st.number_input("What is your Current Gain %?", value=0)

if st.button("Ask AI for Advice"):
    if current_gain >= target_profit:
        st.success("✅ Strategy: BOOK PROFIT! You have reached your goal.")
    elif current_gain < 0:
        st.error("📉 Strategy: STOP LOSS. Consider protecting your capital.")
    else:
        st.info("⏳ Strategy: HOLD. You haven't reached your target yet.")