import json
import streamlit as st
from pathlib import Path

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CineVault",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Root & Reset ── */
:root {
    --bg:        #0a0a0f;
    --surface:   #13131a;
    --card:      #1c1c28;
    --border:    #2a2a3d;
    --accent:    #e8c84a;
    --accent2:   #ff6b35;
    --text:      #e8e8f0;
    --muted:     #6b6b80;
    --success:   #3ecf6b;
    --danger:    #ff4d6d;
    --radius:    14px;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stHeader"] { background: transparent !important; }

/* hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* ── Hero Banner ── */
.hero {
    background: linear-gradient(135deg, #0a0a0f 0%, #1a0f2e 50%, #0d1a0a 100%);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 48px 56px;
    margin-bottom: 36px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(232,200,74,.18) 0%, transparent 70%);
    border-radius: 50%;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 30%;
    width: 180px; height: 180px;
    background: radial-gradient(circle, rgba(255,107,53,.12) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 72px !important;
    letter-spacing: 4px;
    line-height: 1;
    margin: 0 !important;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 15px;
    color: var(--muted);
    margin-top: 8px;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 300;
}

/* ── Stat Cards ── */
.stat-row { display: flex; gap: 16px; margin-bottom: 36px; flex-wrap: wrap; }
.stat-card {
    flex: 1; min-width: 140px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 22px 24px;
}
.stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 42px;
    line-height: 1;
    color: var(--accent);
}
.stat-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--muted);
    margin-top: 4px;
}

/* ── Tab Nav ── */
[data-testid="stTabs"] > div:first-child {
    border-bottom: 1px solid var(--border) !important;
    gap: 4px;
}
[data-testid="stTabs"] button {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    background: transparent !important;
    border: none !important;
    padding: 12px 20px !important;
    border-radius: 8px 8px 0 0 !important;
    transition: all .2s !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--accent) !important;
    border-bottom: 2px solid var(--accent) !important;
    background: rgba(232,200,74,.06) !important;
}

/* ── Form Elements ── */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] select {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    padding: 14px 16px !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(232,200,74,.15) !important;
}
label { color: var(--muted) !important; font-size: 12px !important; letter-spacing: 1px !important; text-transform: uppercase !important; }

/* ── Buttons ── */
.stButton > button {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    border-radius: 10px !important;
    padding: 14px 28px !important;
    transition: all .2s !important;
    width: 100%;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--accent), #d4a832) !important;
    color: #0a0a0f !important;
    border: none !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(232,200,74,.35) !important;
}
.stButton > button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
}

/* ── Movie Cards ── */
.movie-grid { display: flex; flex-direction: column; gap: 14px; }
.movie-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 22px 26px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    transition: border-color .2s, transform .2s;
}
.movie-card:hover { border-color: rgba(232,200,74,.4); transform: translateX(4px); }
.movie-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 26px;
    letter-spacing: 2px;
    color: var(--text);
    margin-bottom: 4px;
}
.movie-seats {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--muted);
}
.seat-badge {
    background: rgba(232,200,74,.12);
    border: 1px solid rgba(232,200,74,.3);
    border-radius: 8px;
    padding: 10px 20px;
    text-align: center;
    min-width: 90px;
    flex-shrink: 0;
}
.seat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 30px;
    color: var(--accent);
    line-height: 1;
}
.seat-lbl { font-size: 10px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--muted); }

/* low-seat warning */
.seat-badge.low {
    background: rgba(255,77,109,.10);
    border-color: rgba(255,77,109,.3);
}
.seat-badge.low .seat-num { color: var(--danger); }

/* ── Alert Boxes ── */
.alert {
    border-radius: 10px;
    padding: 14px 18px;
    font-size: 14px;
    font-weight: 500;
    margin-top: 12px;
}
.alert-success { background: rgba(62,207,107,.12); border: 1px solid rgba(62,207,107,.3); color: var(--success); }
.alert-danger   { background: rgba(255,77,109,.12); border: 1px solid rgba(255,77,109,.3); color: var(--danger); }
.alert-info     { background: rgba(232,200,74,.10); border: 1px solid rgba(232,200,74,.25); color: var(--accent); }

/* ── Section Header ── */
.section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 30px;
    letter-spacing: 3px;
    color: var(--text);
    margin-bottom: 20px;
}
.divider { border: none; border-top: 1px solid var(--border); margin: 28px 0; }

/* ── Selectbox dropdown ── */
[data-testid="stSelectbox"] > div > div {
    background: var(--card) !important;
    border-color: var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Data Layer ────────────────────────────────────────────────────────────────
DATABASE = "movies.json"

def load_data():
    p = Path(DATABASE)
    if p.exists():
        with open(p) as f:
            return json.loads(f.read())
    return []

def save_data(data):
    with open(DATABASE, "w") as f:
        f.write(json.dumps(data, indent=2))

if "movies" not in st.session_state:
    st.session_state.movies = load_data()

def get_movies():
    return st.session_state.movies

def find_movie(name):
    return next((m for m in get_movies() if m["movie_name"].lower() == name.lower()), None)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-title">CineVault</div>
  <div class="hero-sub">Movie Booking &nbsp;·&nbsp; Seat Management &nbsp;·&nbsp; Cancellations</div>
</div>
""", unsafe_allow_html=True)

# ── Stats Row ─────────────────────────────────────────────────────────────────
movies = get_movies()
total_movies  = len(movies)
total_seats   = sum(m["available_seats"] for m in movies)
sold_out      = sum(1 for m in movies if m["available_seats"] == 0)

st.markdown(f"""
<div class="stat-row">
  <div class="stat-card">
    <div class="stat-num">{total_movies}</div>
    <div class="stat-label">Movies Listed</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">{total_seats}</div>
    <div class="stat-label">Seats Available</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">{sold_out}</div>
    <div class="stat-label">Sold Out</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "🎬  All Movies",
    "➕  Add Movie",
    "🎟  Book Ticket",
    "✖  Cancel Ticket",
])

# ──────────────────────────────────────────────────────────────────────────────
# TAB 1 — All Movies
# ──────────────────────────────────────────────────────────────────────────────
with tab1:
    movies = get_movies()
    st.markdown('<div class="section-title">Now Showing</div>', unsafe_allow_html=True)

    if not movies:
        st.markdown('<div class="alert alert-info">🎭 No movies yet — add one to get started.</div>', unsafe_allow_html=True)
    else:
        cards_html = '<div class="movie-grid">'
        for m in movies:
            seats = m["available_seats"]
            low   = seats <= 10
            badge_cls = "seat-badge low" if low else "seat-badge"
            cards_html += f"""
            <div class="movie-card">
              <div>
                <div class="movie-name">{m['movie_name']}</div>
                <div class="movie-seats">{'⚠ Low seats' if low else 'Seats available'}</div>
              </div>
              <div class="{badge_cls}">
                <div class="seat-num">{seats}</div>
                <div class="seat-lbl">seats</div>
              </div>
            </div>"""
        cards_html += '</div>'
        st.markdown(cards_html, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# TAB 2 — Add Movie
# ──────────────────────────────────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">Add New Movie</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        new_name  = st.text_input("Movie Title", placeholder="e.g. Interstellar", key="add_name")
    with col2:
        new_seats = st.number_input("Total Seats", min_value=1, max_value=10000, value=100, step=10, key="add_seats")

    if st.button("Add Movie", type="primary", key="btn_add"):
        if not new_name.strip():
            st.markdown('<div class="alert alert-danger">⚠ Please enter a movie title.</div>', unsafe_allow_html=True)
        elif find_movie(new_name.strip()):
            st.markdown(f'<div class="alert alert-danger">⚠ "{new_name}" already exists.</div>', unsafe_allow_html=True)
        else:
            st.session_state.movies.append({
                "movie_name": new_name.strip(),
                "available_seats": int(new_seats)
            })
            save_data(st.session_state.movies)
            st.markdown(f'<div class="alert alert-success">✓ "{new_name}" added with {new_seats} seats.</div>', unsafe_allow_html=True)
            st.rerun()

# ──────────────────────────────────────────────────────────────────────────────
# TAB 3 — Book Ticket
# ──────────────────────────────────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">Book Tickets</div>', unsafe_allow_html=True)

    movies = get_movies()
    if not movies:
        st.markdown('<div class="alert alert-info">🎭 No movies available to book.</div>', unsafe_allow_html=True)
    else:
        movie_names = [m["movie_name"] for m in movies]
        sel_movie   = st.selectbox("Select Movie", movie_names, key="book_sel")
        movie_obj   = find_movie(sel_movie)

        if movie_obj:
            avail = movie_obj["available_seats"]
            badge_cls = "seat-badge low" if avail <= 10 else "seat-badge"
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:14px;margin:16px 0 24px;">
              <div class="{badge_cls}">
                <div class="seat-num">{avail}</div>
                <div class="seat-lbl">available</div>
              </div>
              <div style="color:var(--muted);font-size:13px;letter-spacing:1px;text-transform:uppercase;">
                seats remaining for<br><strong style="color:var(--text);font-size:16px;">{sel_movie}</strong>
              </div>
            </div>""", unsafe_allow_html=True)

        book_seats = st.number_input("Number of Seats", min_value=1, max_value=500, value=1, key="book_num")

        if st.button("Confirm Booking", type="primary", key="btn_book"):
            movie_obj = find_movie(sel_movie)
            if not movie_obj:
                st.markdown('<div class="alert alert-danger">⚠ Movie not found.</div>', unsafe_allow_html=True)
            elif book_seats > movie_obj["available_seats"]:
                st.markdown(f'<div class="alert alert-danger">⚠ Only {movie_obj["available_seats"]} seat(s) available.</div>', unsafe_allow_html=True)
            else:
                movie_obj["available_seats"] -= book_seats
                save_data(st.session_state.movies)
                st.markdown(f'<div class="alert alert-success">🎟 {book_seats} ticket(s) booked for <strong>{sel_movie}</strong>!</div>', unsafe_allow_html=True)
                st.rerun()

# ──────────────────────────────────────────────────────────────────────────────
# TAB 4 — Cancel Ticket
# ──────────────────────────────────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="section-title">Cancel Tickets</div>', unsafe_allow_html=True)

    movies = get_movies()
    if not movies:
        st.markdown('<div class="alert alert-info">🎭 No movies available.</div>', unsafe_allow_html=True)
    else:
        cancel_names = [m["movie_name"] for m in movies]
        cancel_sel   = st.selectbox("Select Movie", cancel_names, key="cancel_sel")
        cancel_seats = st.number_input("Tickets to Cancel", min_value=1, max_value=500, value=1, key="cancel_num")

        if st.button("Cancel Tickets", type="secondary", key="btn_cancel"):
            movie_obj = find_movie(cancel_sel)
            if not movie_obj:
                st.markdown('<div class="alert alert-danger">⚠ Movie not found.</div>', unsafe_allow_html=True)
            else:
                movie_obj["available_seats"] += cancel_seats
                save_data(st.session_state.movies)
                st.markdown(f'<div class="alert alert-success">✓ {cancel_seats} ticket(s) cancelled for <strong>{cancel_sel}</strong>.</div>', unsafe_allow_html=True)
                st.rerun()