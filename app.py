import streamlit as st
import ai_backend # <-- SURGICALLY ATTACHING THE BRAIN!

# ── Page config (must be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="Zenith · CSE Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap');

/* ── Global tokens ── */
:root {
    --cream:        #FAF7F2;
    --parchment:    #F3EDE3;
    --sidebar-bg:   #EDE8DF;
    --matcha:       #8FAF8A;
    --matcha-light: #C8DEC5;
    --matcha-muted: #D6E8D3;
    --dusty-blue:   #A9BDD0;
    --blue-light:   #DDE8F0;
    --text-dark:    #3A3530;
    --text-mid:     #6B6560;
    --text-light:   #9E9690;
    --border:       rgba(143,175,138,0.25);
    --shadow-soft:  0 4px 24px rgba(58,53,48,0.06);
    --shadow-card:  0 2px 12px rgba(58,53,48,0.08);
    --radius-lg:    18px;
    --radius-md:    12px;
    --radius-sm:    8px;
}

/* ── Root / App shell ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--cream) !important;
    font-family: 'DM Sans', sans-serif;
    color: var(--text-dark);
}

[data-testid="stApp"] {
    background-color: var(--cream) !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: var(--sidebar-bg) !important;
    border-right: 1px solid var(--border) !important;
    box-shadow: 2px 0 16px rgba(58,53,48,0.05) !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Sidebar title */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    font-family: 'DM Serif Display', serif !important;
    color: var(--text-dark) !important;
    letter-spacing: -0.02em;
}

/* Radio buttons */
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    font-size: 0.88rem !important;
    color: var(--text-mid) !important;
    padding: 0.55rem 0.75rem !important;
    border-radius: var(--radius-md) !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    display: block !important;
    line-height: 1.5 !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: var(--matcha-muted) !important;
    color: var(--text-dark) !important;
}

/* Active radio item */
[data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] + div label,
[data-testid="stSidebar"] [data-testid="stRadio"] input:checked ~ div label {
    background: var(--matcha-light) !important;
    color: var(--text-dark) !important;
    font-weight: 500 !important;
}

/* Hide radio circle dots */
[data-testid="stSidebar"] [data-testid="stRadio"] [data-testid="stRadioLabel"] span:first-child {
    display: none !important;
}

/* ── Main header ── */
.main-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.5rem 0 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.5rem;
}

.main-header .title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.75rem;
    color: var(--text-dark);
    letter-spacing: -0.03em;
    line-height: 1.1;
}

.main-header .subtitle {
    font-size: 0.82rem;
    color: var(--text-light);
    margin-top: 2px;
    font-weight: 300;
}

/* Mode pill badge */
.mode-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--matcha-muted);
    color: var(--matcha);
    border: 1px solid var(--matcha-light);
    border-radius: 99px;
    padding: 4px 14px;
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.01em;
    margin-left: auto;
}

/* ── Chat container ── */
[data-testid="stChatMessage"] {
    padding: 0.2rem 0 !important;
}

/* User bubble */
[data-testid="stChatMessage"][data-testid*="user"] [data-testid="stMarkdownContainer"],
.stChatMessage:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stMarkdownContainer"] {
    background: var(--blue-light) !important;
    border-radius: var(--radius-lg) var(--radius-lg) var(--radius-sm) var(--radius-lg) !important;
    padding: 0.85rem 1.1rem !important;
    box-shadow: var(--shadow-card) !important;
    color: var(--text-dark) !important;
    font-size: 0.9rem !important;
    line-height: 1.65 !important;
    border: 1px solid rgba(169,189,208,0.3) !important;
}

/* Assistant bubble */
[data-testid="stChatMessage"]:not(:has([data-testid="stChatMessageAvatarUser"])) [data-testid="stMarkdownContainer"] {
    background: var(--parchment) !important;
    border-radius: var(--radius-lg) var(--radius-lg) var(--radius-lg) var(--radius-sm) !important;
    padding: 0.85rem 1.1rem !important;
    box-shadow: var(--shadow-card) !important;
    color: var(--text-dark) !important;
    font-size: 0.9rem !important;
    line-height: 1.65 !important;
    border: 1px solid var(--border) !important;
}

/* Avatar circles */
[data-testid="stChatMessageAvatarUser"],
[data-testid="stChatMessageAvatarAssistant"] {
    border-radius: 50% !important;
    width: 34px !important;
    height: 34px !important;
    font-size: 0.9rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

[data-testid="stChatMessageAvatarUser"] {
    background: var(--dusty-blue) !important;
}

[data-testid="stChatMessageAvatarAssistant"] {
    background: var(--matcha) !important;
}

/* ── Chat input ── */
[data-testid="stChatInputContainer"] {
    background: var(--cream) !important;
    border-top: 1px solid var(--border) !important;
    padding: 0.75rem 0 !important;
}

[data-testid="stChatInput"] {
    background: var(--parchment) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius-lg) !important;
    color: var(--text-dark) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
    box-shadow: var(--shadow-soft) !important;
    transition: border-color 0.2s ease !important;
}

[data-testid="stChatInput"]:focus {
    border-color: var(--matcha) !important;
    box-shadow: 0 0 0 3px rgba(143,175,138,0.15) !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] {
    color: var(--matcha) !important;
}

/* ── Welcome card ── */
.welcome-card {
    background: var(--parchment);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 2rem 2.25rem;
    box-shadow: var(--shadow-soft);
    margin: 1rem 0 2rem;
    max-width: 640px;
}

.welcome-card h2 {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3rem;
    color: var(--text-dark);
    margin-bottom: 0.4rem;
    letter-spacing: -0.02em;
}

.welcome-card p {
    color: var(--text-mid);
    font-size: 0.86rem;
    line-height: 1.7;
    margin: 0;
}

.tool-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 1.1rem;
}

.tool-chip {
    background: var(--matcha-muted);
    color: var(--text-mid);
    border: 1px solid var(--matcha-light);
    border-radius: 99px;
    padding: 4px 13px;
    font-size: 0.78rem;
    font-weight: 400;
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# APP ROUTING & MEMORY (st.session_state)
# ==========================================
# 1. Give the app a memory of where the user is
if "current_page" not in st.session_state:
    st.session_state.current_page = "semester" # Start at the first page
if "semester" not in st.session_state:
    st.session_state.semester = None
if "stream" not in st.session_state:
    st.session_state.stream = None
if "roll_number" not in st.session_state:
    st.session_state.roll_number = None

# ==========================================
# PAGE 1: SEMESTER SELECTION
# ==========================================
if st.session_state.current_page == "semester":
    st.markdown("<h1 style='text-align: center; font-family: DM Serif Display;'>Welcome to Zenith ✦</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6B6560;'>Select your current semester to begin.</p>", unsafe_allow_html=True)
    
    st.write("") # Spacer
    
    # Creates a nice 4x2 grid of buttons
    col1, col2, col3, col4 = st.columns(4)
    cols = [col1, col2, col3, col4]
    
    for i in range(1, 9):
        # Place the button in the correct column
        with cols[(i-1) % 4]:
            if st.button(f"Semester {i}", use_container_width=True):
                st.session_state.semester = i
                st.session_state.current_page = "stream" # Move to next page
                st.rerun() # Force the app to refresh and load Page 2

# ==========================================
# PAGE 2: STREAM SELECTION
# ==========================================
elif st.session_state.current_page == "stream":
    st.markdown(f"<h2 style='text-align: center;'>Semester {st.session_state.semester} Confirmed.</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6B6560;'>Now, select your engineering stream.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    streams = ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil"]
    
    for idx, stream in enumerate(streams):
        with [col1, col2, col3][idx % 3]:
            if st.button(stream, use_container_width=True):
                st.session_state.stream = stream
                st.session_state.current_page = "login" # Move to next page
                st.rerun()

# ==========================================
# PAGE 3: STUDENT LOGIN
# ==========================================
elif st.session_state.current_page == "login":
    st.markdown(f"<h2 style='text-align: center;'>{st.session_state.stream} Department Login</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.container(border=True):
            
            # ---> 🚨 THE FIX: Wrap it in a form! <---
            with st.form("login_form"):
                roll_input = st.text_input("College Roll Number")
                password_input = st.text_input("Password", type="password")
                
                # Note: st.button becomes st.form_submit_button inside a form!
                submitted = st.form_submit_button("Access Dashboard ✨", use_container_width=True)
                
                if submitted:
                    if roll_input and password_input: # Now it checks for both!
                        st.session_state.roll_number = roll_input
                        st.session_state.current_page = "dashboard" 
                        st.rerun()
                    else:
                        st.error("Please enter both Roll Number and Password.")

# ==========================================
# PAGE 4: THE ACTUAL ZENITH DASHBOARD
# ==========================================
elif st.session_state.current_page == "dashboard":

    # ── Tool definitions (Descriptions Only) ──────────────────────────────────
    TOOLS = {
        "💬 General Chat": "Open-ended AI assistant for any CS topic.",
        "📝 Chat with Notes": "Chat grounded in your uploaded study notes.",
        "💻 Code Explainer": "Paste code and get a plain-English breakdown.",
        "⚡ TL;DR Summarizer": "Condense long topics or articles instantly.",
        "🔮 Question Predictor": "Predict likely exam questions from a topic.",
    }

    # ── Sidebar ──────────────────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown(
            "<h2 style='font-family:DM Serif Display,serif;font-size:1.4rem;"
            "letter-spacing:-0.02em;margin-bottom:0.25rem;'>🛠️ Power Tools</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='font-size:0.78rem;color:#9E9690;margin-bottom:1.5rem;'>"
            "Choose your study mode below</p>",
            unsafe_allow_html=True,
        )

        selected_tool = st.radio(
            label="AI Mode",
            options=list(TOOLS.keys()),
            label_visibility="collapsed",
        )

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(
            f"<p style='font-size:0.77rem;color:#9E9690;line-height:1.6;'>"
            f"<b style='color:#6B6560;'>Active mode</b><br>"
            f"{TOOLS[selected_tool]}</p>",
            unsafe_allow_html=True,
        )

        # Push to bottom
        st.markdown("<br>" * 6, unsafe_allow_html=True)
        st.caption("Logged in as: 4th Sem CSE Student")

    # ── Session state ─────────────────────────────────────────────────────────────
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "last_tool" not in st.session_state:
        st.session_state.last_tool = None

    # Clear chat if tool changes
    if st.session_state.last_tool != selected_tool:
        st.session_state.messages = []
        st.session_state.last_tool = selected_tool

    # ── Main area header ──────────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="main-header">
            <div>
                <div class="title">Zenith ✦</div>
                <div class="subtitle">Computer Science Engineering Dashboard</div>
            </div>
            <div class="mode-pill">{selected_tool}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Welcome card (shown only when chat is empty) ──────────────────────────────
    if not st.session_state.messages:
        tool_chips_html = "".join(
            f'<span class="tool-chip">{t}</span>' for t in TOOLS
        )
        st.markdown(
            f"""
            <div class="welcome-card">
                <h2>Good to see you 🌿</h2>
                <p>
                    You're in <strong>{selected_tool}</strong> mode —
                    {TOOLS[selected_tool]}<br><br>
                    Type a question below to get started. Switch modes anytime
                    from the sidebar to change how I respond.
                </p>
                <div class="tool-chips">{tool_chips_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Render chat history ───────────────────────────────────────────────────────
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar=msg["avatar"]):
            st.markdown(msg["content"])

    # ── Chat input & REAL AI CONNECTION ───────────────────────────────────────────
    placeholder_map = {
        "💬 General Chat":       "Ask me anything about CS…",
        "📝 Chat with Notes":    "Ask a question based on your notes…",
        "💻 Code Explainer":     "Paste your code here…",
        "⚡ TL;DR Summarizer":   "Paste a topic or paragraph to summarise…",
        "🔮 Question Predictor": "Enter a chapter or topic name…",
    }

    if prompt := st.chat_input(placeholder_map.get(selected_tool, "Type here…")):

        # 1. Store & show user message
        st.session_state.messages.append({
            "role":    "user",
            "avatar":  "🧑‍💻",
            "content": prompt,
        })
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(prompt)

        # 2. Inject the secret prompt engineering!
        hidden_prompt = ""
        if selected_tool == "💻 Code Explainer":
            hidden_prompt = "You are an expert CSE professor. Explain this code simply, and do a step-by-step dry run: \n\n"
        elif selected_tool == "⚡ TL;DR Summarizer":
            hidden_prompt = "Extract ONLY the most critical definitions, formulas, and bullet points from this text for a quick exam review: \n\n"
        elif selected_tool == "🔮 Question Predictor":
            hidden_prompt = "Based on this text, predict the top 5 most likely exam questions and provide short answers: \n\n"
        
        final_prompt = hidden_prompt + prompt

        # 3. Call your real AI backend
        with st.chat_message("assistant", avatar="🌿"):
            with st.spinner("Zenith is thinking..."):
                try:
                    # Talking to Google Servers!
                    response_text = ai_backend.get_ai_response(final_prompt)
                    response_text = str(response_text) # This fixes the Pylance warning!
                    st.markdown(response_text)
                except Exception as e:
                    response_text = "Oops! The AI needs a second. Try asking again."
                    st.error(response_text)

        # 4. Store assistant message
        st.session_state.messages.append({
            "role":    "assistant",
            "avatar":  "🌿",
            "content": response_text,
        })