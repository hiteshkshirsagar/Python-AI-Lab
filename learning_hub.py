import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="Hitesh's AI Academy", layout="wide")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.header("👤 User Profile")
    user_data = {
        "Name": "Hitesh",
        "Target Role": "AI Engineer",
        "Current Shift": "2 PM - 11 PM IST",
        "Favorite Index": "Nifty 50"
    }
    st.write(f"Welcome, **{user_data['Name']}**!")
    st.json(user_data)
    
    st.divider()
    st.header("🧭 Lesson Manual")
    topics = [
        "Variables", "Data Types", "Lists", "Dictionaries", 
        "Loops", "Functions", "Lesson 8: Pandas", 
        "Lesson 9: Data Viz", "Lesson 10: try-except", "Lesson 11: APIs"
    ]
    selected_topic = st.selectbox("Choose a topic to learn more:", topics)

# --- MAIN APP UI ---
st.title("📋 Python & AI Learning Hub")
tab_learn, tab_practice, tab_ai = st.tabs(["📚 Learn Python", "🛠️ Practice Lab", "🤖 AI & Trading Tools"])

# --- TAB 1: THE BEGINNER'S MANUAL ---
with tab_learn:
    st.header(f"📝 Lesson: {selected_topic}")
    
    if selected_topic == "Variables":
        st.write("### 📦 The Concept: The Labeled Box")
        st.write("A variable is like a box where you store data. You put a label on the box so you can find the data later.")
        st.code("nifty_target = 25000\nprint(nifty_target)", language="python")
        with st.expander("❓ Variables Q&A"):
            st.write("**Q: Can I change the value inside the box later?**")
            st.info("Yes! That is why it is called a 'variable'—the value can vary.")

    elif selected_topic == "Data Types":
        st.write("### 🔢 The Concept: Different Kinds of Data")
        st.write("Python handles numbers and text differently. You can't do math on a name!")
        st.code("price = 22000 # Integer\nname = 'Nifty' # String\nprofit = 15.5 # Float", language="python")
        with st.expander("❓ Data Types Q&A"):
            st.write("**Q: What happens if I try to add a number to a string?**")
            st.error("Python will throw an error! You must convert them first.")

    elif selected_topic == "Lists":
        st.write("### 🛒 The Concept: The Shopping Bag")
        st.write("A List stores many items in a single variable. Think of it as your stock watchlist.")
        st.code("stocks = ['TCS', 'INFY', 'RELIANCE']", language="python")
                with st.expander("❓ Lists Q&A"):
            ans = st.text_input("What command adds an item to a list?")
            if st.button("Check List Answer"):
                if "append" in ans.lower(): st.success("Correct!")
                else: st.warning("Hint: It starts with 'a'")

    elif selected_topic == "Dictionaries":
        st.write("### 📖 The Concept: The Key-Value Cupboard")
        st.write("A dictionary stores data with a label (Key). Like looking up a word's meaning.")
        st.code("stock_data = {'name': 'TCS', 'price': 3800}", language="python")
        with st.expander("❓ Dictionaries Q&A"):
            st.write("**Q: Can a dictionary have duplicate keys?**")
            st.info("No. Each key must be unique, like a unique ID.")

    elif selected_topic == "Loops":
        st.write("### 🔄 The Concept: The Task Repeater")
        st.write("Loops do the same job over and over. Use them to check every stock in your list.")
        st.code("for s in stocks:\n    print(f'Checking {s}...')", language="python")
                with st.expander("❓ Loops Q&A"):
            st.write("**Q: When does a loop stop?**")
            st.info("It stops when it reaches the last item in your collection.")

    elif selected_topic == "Functions":
        st.write("### 📦 The Concept: The Reusable Recipe")
        st.write("A function is a set of instructions you write once and use many times.")
        st.code("def calc_profit(buy, sell):\n    return sell - buy", language="python")
        with st.expander("❓ Functions Q&A"):
            st.write("**Q: What does 'return' do?**")
            st.info("It sends the final result back to the main program.")

    elif selected_topic == "Lesson 8: Pandas":
        st.write("### 🐼 The Concept: Excel on Steroids")
        st.write("Pandas handles Tables (DataFrames). This is where Data Engineering begins.")
        df = pd.DataFrame({"Stock": ["NIFTY", "TCS"], "Price": [22000, 3800]})
        st.dataframe(df)
        with st.expander("❓ Pandas Q&A"):
            st.write("**Q: What is a DataFrame?**")
            st.info("A 2D table with rows and columns, just like an Excel sheet.")

    elif selected_topic == "Lesson 9: Data Viz":
        st.write("### 📈 The Concept: Seeing the Pattern")
        st.write("Charts help AI Engineers spot trends that numbers alone can't show.")
        if st.button("Show Live Nifty Chart"):
            data = yf.Ticker("^NSEI").history(period="5d")['Close']
            st.line_chart(data)
        with st.expander("❓ Data Viz Q&A"):
            st.write("**Q: Why use charts instead of tables?**")
            st.info("Charts show 'trends' and 'momentum' much faster than rows of text.")

    elif selected_topic == "Lesson 10: try-except":
        st.write("### 🛡️ The Concept: The Safety Net")
        st.write("Try-Except prevents your app from crashing if a user enters bad data.")
        st.code("try:\n    # code\nexcept:\n    # error plan", language="python")
        with st.expander("❓ Error Handling Q&A"):
            st.write("**Q: Is 'except' mandatory if you use 'try'?**")
            st.success("Yes! You must tell Python what to do if an error occurs.")

    elif selected_topic == "Lesson 11: APIs":
        st.write("### 🌐 The Concept: The Phone Call")
        st.write("APIs let your app 'call' another computer to get live data (like Yahoo Finance).")
        st.code("data = yf.Ticker('^NSEI').info", language="python")
        with st.expander("❓ API Q&A"):
            st.write("**Q: Does every API require payment?**")
            st.info("No! Many, like yFinance, are free for learning purposes.")

# --- TAB 2: PRACTICE LAB ---
with tab_practice:
    st.header("🏆 Knowledge Challenges")
    if 'quiz_score' not in st.session_state: st.session_state.quiz_score = 0
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("⭐ Basics Quiz")
        q = st.selectbox("Question:", ["Which type is for text?", "Symbol for a List?"])
        ans = st.text_input("Your Answer:")
        if st.button("Submit Answer"):
            if "string" in ans.lower() or "[]" in ans:
                st.session_state.quiz_score += 10
                st.success("Correct!")
    
    st.metric("Total Score", f"{st.session_state.quiz_score} Points")

# --- TAB 3: AI & TRADING TOOLS ---
with tab_ai:
    st.header("🤖 Market Tools")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Fetch Nifty 50 Live"):
            try:
                p = yf.Ticker("^NSEI").history(period="1d")['Close'].iloc[-1]
                st.metric("Nifty 50", f"₹{p:,.2f}")
            except: st.error("API error.")
    with col2:
        inv = st.number_input("Invested Amount:", min_value=0)
        st.progress(min(inv/100000, 1.0))