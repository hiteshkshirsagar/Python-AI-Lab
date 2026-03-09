import streamlit as st

st.title("📋 Python & AI Learning Hub")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.header("👤 User Profile")
    
    # Creating a dictionary to store your info (Moved to Sidebar)
    user_data = {
        "Name": "Hitesh",
        "Target Role": "AI Engineer",
        "Current Shift": "2 PM - 11 PM IST",
        "Favorite Index": "Nifty 50"
    }
    
    # Accessing data from a dictionary using the "Key"
    st.write(f"Welcome, **{user_data['Name']}**!")
    st.write(f"Your goal is to become an **{user_data['Target Role']}**.")
    st.json(user_data)
    
    st.divider()
    st.header("🧭 Navigation")
    
    # We use a List to store the topics
    topics = ["Variables", "Data Types", "Lists", "Dictionaries", "Loops", "Functions"]
    
    # Creating a dynamic list in the UI for your friends
    selected_topic = st.selectbox("Choose a topic to learn more:", topics)

# --- MAIN TABS ---
tab_learn, tab_practice, tab_ai = st.tabs(["📚 Learn", "🛠️ Practice", "🤖 AI Tools"])

with tab_learn:
    st.header(f"📝 Learning: {selected_topic}")
    
    if selected_topic == "Lists":
        st.code("""
# Example of a List:
my_portfolio = ["Tata Small Cap", "Axis Silver FoF", "Nifty 50"]
print(my_portfolio[0]) # Output: Tata Small Cap
        """)
        st.info("Challenge for Friends: Try adding a new fund to the list using .append()")

    st.divider()
    st.header("❓ Python Q&A Hub")

    # A dictionary of Python concepts
    python_qa = {
        "What is a Variable?": "A container for storing data values.",
        "What is a List?": "An ordered collection that can be changed.",
        "What is a Dictionary?": "A collection of Key-Value pairs.",
        "What is Streamlit?": "A tool to build web apps with Python."
    }

    # Creating a dropdown to pick a question
    selected_question = st.selectbox("Choose a question to learn:", list(python_qa.keys()))

    # Showing the answer based on the selection
    if st.button("Show Answer"):
        answer = python_qa[selected_question]
        st.info(f"💡 {answer}")

    st.divider()
    st.header("🔄 Lesson 5: The Power of Loops")

    # A list of stock prices
    nifty_prices = [22100, 22050, 22200, 21900, 22300]
    st.write("Checking trend for the last 5 days...")

    # The 'for' loop
    for price in nifty_prices:
        if price > 22000:
            st.write(f"📈 {price}: **Bullish** (Above 22k)")
        else:
            st.write(f"📉 {price}: **Bearish** (Below 22k)")

    st.divider()
    st.header("📦 Lesson 6: The Power of Functions")

    # 1. Defining the function (The Recipe)
    def calculate_tax(income):
        # Let's say tax is 10% for learning purposes
        tax = income * 0.10
        return tax

    # 2. Using the function in the App
    salary = st.number_input("Enter annual salary (LPA):", value=10.0)

    if st.button("Calculate My Tax"):
        my_tax = calculate_tax(salary)
        st.write(f"Based on a 10% rate, your tax is: **{my_tax} LPA**")
        st.info("Functions help us reuse code without typing the math again!")

with tab_practice:
    st.header("📈 Live Portfolio Manager")

    # 1. Initialize the 'Notebook' (Session State)
    if 'my_portfolio' not in st.session_state:
        st.session_state.my_portfolio = ["Tata Small Cap", "Axis Silver FoF"]

    # 2. Input to add a new fund
    new_stock = st.text_input("Enter a stock or fund name (e.g., Nifty 50):")

    if st.button("Add to My Portfolio"):
        if new_stock:
            st.session_state.my_portfolio.append(new_stock)
            st.success(f"Successfully added {new_stock}!")
        else:
            st.warning("Please enter a name first!")

    # 3. Display the updated list
    st.write("### Your Current Assets:")
    for item in st.session_state.my_portfolio:
        st.write(f"- {item}")

    st.divider()
    st.header("📊 Project: Market Trend Analyzer")

    # 1. Let the user (or your friends) input a list of prices
    price_input = st.text_input("Enter last 5 days Nifty prices (separated by commas):", "22100, 22050, 22200, 21900, 22300")

    # 2. Convert that text into a List of Numbers (Advanced Beginner Logic)
    try:
        price_list = [float(p.strip()) for p in price_input.split(",")]
    except ValueError:
        st.error("Please enter valid numbers")
        price_list = []

    if st.button("Analyze Trend"):
        if not price_list:
            st.warning("Please fix the input errors above to analyze the trend.")
        else:
            # 3. Use Loops/Math to find insights
            total = 0
            for p in price_list:
                total += p
            
            avg_price = total / len(price_list)
            max_price = max(price_list)
            min_price = min(price_list)
            
            # 4. Display Results
            col1, col2, col3 = st.columns(3)
            col1.metric("Average Price", f"₹{avg_price:,.2f}")
            col2.metric("Highest", f"₹{max_price:,.2f}")
            col3.metric("Lowest", f"₹{min_price:,.2f}")
            
            # AI Logic
            if price_list[-1] > avg_price:
                st.success("🚀 The current price is above average. The trend looks BULLISH!")
            else:
                st.warning("⚠️ The current price is below average. The trend looks BEARISH.")

with tab_ai:
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

    st.divider()
    st.header("📦 Lesson 6: Mastering Functions (AI)")

    # This function takes data and returns a result
    def get_investment_advice(profit_pct):
        if profit_pct > 20:
            return "🚀 Amazing! Consider booking some profit."
        elif profit_pct > 0:
            return "📈 You are in the green. Keep holding!"
        else:
            return "📉 Stay patient. Focus on the long term."

    # User Input
    user_profit = st.number_input("Enter your current profit %:", value=0.0)

    # Calling the function
    if st.button("Get AI Advice"):
        advice = get_investment_advice(user_profit)
        st.info(advice)

    st.divider()
    st.header("🌟 Lovable AI Insights")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Target Salary", value="12 LPA", delta="Goal")
    with col2:
        st.metric(label="Learning Progress", value="Phase 1", delta="75%")

    st.progress(75) # A visual progress bar


import yfinance as yf

def get_live_nifty():
    # ^NSEI is the symbol for Nifty 50
    nifty = yf.Ticker("^NSEI")
    return nifty.history(period="1d")['Close'].iloc[-1]

if st.button("Fetch Live Nifty 50 Price"):
    price = get_live_nifty()
    st.metric("Live Nifty 50", f"₹{price:,.2f}")

import yfinance as yf

st.header("📈 Live Nifty 50 Tracker")

# We "try" the code that might fail
try:
    if st.button("Fetch Live Price"):
        data = yf.Ticker("^NSEI").history(period="1d")
        price = data['Close'].iloc[-1]
        st.metric("Nifty 50", f"₹{price:,.2f}")

# If it fails (no internet or wrong symbol), we do this "except"
except Exception as e:
    st.warning("⚠️ Could not fetch live data. Please check your internet connection or the stock symbol.")


st.header("💰 Investment Calculator")

# Using number_input prevents 'abc' errors automatically!
buy_price = st.number_input("Average Buy Price (₹):", value=100.0, step=1.0)
qty = st.number_input("Quantity:", min_value=1, step=1)

total = buy_price * qty
st.write(f"Total Investment: **₹{total:,.2f}**")