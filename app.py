def show_lab(reagents, observation, conclusion):
    st.subheader("🔬 Зертханалық жұмыс")
    st.write(f"**Реактивтер:** {reagents}")

    # ---------- Түсті реактивке байланысты беру ----------
    color = "#8b0000"  # әдепкі қызыл (Br₂)
    if "KMnO₄" in reagents:
        color = "#800080"  # күлгін
    elif "Cu(OH)₂" in reagents:
        color = "#1e90ff"  # көк
    elif "NaHCO₃" in reagents:
        color = "#00ff00"  # жасыл (мысалы, көпіршік үшін)
    elif "I₂" in reagents:
        color = "#4b0082"  # индиго
    elif "FeCl₃" in reagents:
        color = "#ffd700"  # сары

    # ---------- HTML / CSS анимация ----------
    st.markdown(
        f"""
        <style>
        .test-tube {{
            width: 80px;
            height: 250px;
            border: 4px solid #555;
            border-radius: 0 0 40px 40px;
            margin: 20px auto;
            position: relative;
            background: #fff;
            overflow: hidden;
            box-shadow: 0 0 10px rgba(0,0,0,0.3);
        }}
        .liquid {{
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 0%;
            background: {color};
            animation: fill 4s forwards;
        }}
        .bubbles {{
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }}
        .bubble {{
            position: absolute;
            bottom: 0;
            width: 8px;
            height: 8px;
            background: rgba(255,255,255,0.7);
            border-radius: 50%;
            animation: rise 3s infinite;
        }}
        @keyframes fill {{
            0% {{ height: 0%; }}
            50% {{ height: 50%; }}
            100% {{ height: 70%; }}
        }}
        @keyframes rise {{
            0% {{ bottom: 0; opacity: 0; }}
            50% {{ opacity: 1; }}
            100% {{ bottom: 180px; opacity: 0; }}
        }}
        </style>

        <div class="test-tube">
            <div class="liquid"></div>
            <div class="bubbles">
                <div class="bubble" style="left:10%; animation-delay:0s;"></div>
                <div class="bubble" style="left:30%; animation-delay:0.5s;"></div>
                <div class="bubble" style="left:50%; animation-delay:1s;"></div>
                <div class="bubble" style="left:70%; animation-delay:1.5s;"></div>
                <div class="bubble" style="left:90%; animation-delay:2s;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------- Прогресс бар + мәтін ----------
    progress_bar = st.progress(0)
    reaction_status = st.empty()
    for i in range(1, 101):
        time.sleep(0.03)
        progress_bar.progress(i)
        if i < 20:
            reaction_status.text("🧪 Реактив қосылды...")
        elif i < 50:
            reaction_status.text(f"🔎 Бақылау: {observation}")
        elif i < 80:
            reaction_status.text("💡 Реакция жүріп жатыр...")
        else:
            reaction_status.text(f"✅ Қорытынды: {conclusion}")
    reaction_status.text(f"✅ Қорытынды: {conclusion}")
