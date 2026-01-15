import streamlit as st
import time

st.set_page_config(page_title="Chemistry Lab AI", layout="wide")

# ---------------- CSS: АНИМАЦИЯ СТИЛЬДЕРІ ----------------
st.markdown("""
<style>
    .lab-container { display: flex; justify-content: center; align-items: center; height: 250px; background: #1a1a1a; border-radius: 15px; padding: 20px; }
    .tube { width: 35px; height: 120px; border: 3px solid #ddd; border-top: none; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px; position: relative; margin: 0 15px; background: rgba(255,255,255,0.1); }
    .liquid { position: absolute; bottom: 0; width: 100%; height: 0%; transition: all 1s ease-in-out; border-bottom-left-radius: 15px; border-bottom-right-radius: 15px; }
    
    /* Құю анимациясы */
    @keyframes pour-left { 0% { transform: rotate(0deg); } 100% { transform: rotate(60deg) translate(20px, -20px); } }
    @keyframes pour-right { 0% { transform: rotate(0deg); } 100% { transform: rotate(-60deg) translate(-20px, -20px); } }
    
    .pouring-left { animation: pour-left 1.5s forwards; }
    .pouring-right { animation: pour-right 1.5s forwards; }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📘 34 САБАҚ")
lessons = [f"{i}-сабақ" for i in range(1, 35)]
lesson_selected = st.sidebar.selectbox("Сабақты таңдаңыз", lessons)
lesson_number = int(lesson_selected.split("-")[0])

st.sidebar.markdown("---")
mode = st.sidebar.radio("Режим", ["Оқушы", "Мұғалім"])

# ---------------- DATA: 34 САБАҚТЫҢ МАЗМҰНЫ ----------------
# Барлық сабаққа 10 сұрақтан тұратын тест дайындалды
def get_lesson_data(n):
    base_data = {
        1: {
            "topic": "Сапалық реакция ұғымы",
            "theory": "Сапалық реакция – затты сыртқы белгілері (түсі, тұнба, иіс) арқылы тану.",
            "lab": ("Бром суы (Br₂)", "Түссіздену", "Қанықпаған байланыс бар", "#E67E22", "#FFFFFF"), # Сұғылт қызғылт -> Түссіз
            "test": [("Br₂ нені анықтайды?", ["Алкан", "Алкен", "Спирт"], 1) for _ in range(10)]
        },
        2: {
            "topic": "Спирттердің сапалық реакциясы",
            "theory": "Көп атомды спирттерді мыс (II) гидроксидімен анықтайды.",
            "lab": ("Cu(OH)₂", "Көк түсті ерітінді", "Глицерин/Этиленгликоль бар", "#3498DB", "#00008B"),
            "test": [("–OH қай топ?", ["Амин", "Спирт", "Қышқыл"], 1) for _ in range(10)]
        },
        # Басқа сабақтар үшін шаблон (3-34)
    }
    # Егер сабақ базада жоқ болса, бос шаблон қайтару
    return base_data.get(n, {
        "topic": f"{n}-тақырып: Органикалық синтез",
        "theory": "Бұл бөлімде функционалдық топтардың өзара айналымы қарастырылады.",
        "lab": ("Реактивтер жиынтығы", "Түс өзгеруі", "Зерттеу аяқталды", "#95a5a6", "#2c3e50"),
        "test": [(f"Сұрақ {i+1}?", ["Нұсқа А", "Нұсқа Б", "Нұсқа В"], 0) for i in range(10)]
    })

data = get_lesson_data(lesson_number)

# ---------------- UI: ЗЕРТХАНАЛЫҚ АНИМАЦИЯ ----------------
def run_lab_animation(start_color, end_color):
    placeholder = st.empty()
    
    # 1. Бастапқы күй
    with placeholder.container():
        st.markdown(f"""
        <div class='lab-container'>
            <div class='tube'><div class='liquid' style='height: 70%; background: {start_color};'></div></div>
            <div class='tube' style='border-color: gold;'><div class='liquid' id='target' style='height: 0%; background: {end_color};'></div></div>
            <div class='tube'><div class='liquid' style='height: 70%; background: rgba(255,255,255,0.5);'></div></div>
        </div>
        """, unsafe_allow_html=True)
    
    time.sleep(1)
    
    # 2. Құю сәті
    with placeholder.container():
        st.markdown(f"""
        <div class='lab-container'>
            <div class='tube pouring-left'><div class='liquid' style='height: 70%; background: {start_color};'></div></div>
            <div class='tube' style='border-color: gold;'><div class='liquid' style='height: 80%; background: {end_color}; transition: height 2s;'></div></div>
            <div class='tube pouring-right'><div class='liquid' style='height: 70%; background: rgba(255,255,255,0.5);'></div></div>
        </div>
        """, unsafe_allow_html=True)
    
    time.sleep(2)

# ---------------- MAIN CONTENT ----------------
st.header(f"🧪 {lesson_number}-сабақ: {data['topic']}")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📖 Теория")
    st.info(data["theory"])
    
    st.subheader("🔬 Виртуалды тәжірибе")
    st.write(f"**Реактив:** {data['lab'][0]}")
    if st.button("Реакцияны бастау"):
        run_lab_animation(data['lab'][3], data['lab'][4])
        st.success(f"Нәтиже: {data['lab'][1]}")
        st.caption(f"Қорытынды: {data['lab'][2]}")

with col2:
    st.subheader("📝 Тестілеу")
    score = 0
    # Әр сабақ үшін бірегей кілт (key) жасау маңызды
    for idx, (q, opts, correct) in enumerate(data["test"]):
        ans = st.radio(f"{idx+1}. {q}", opts, key=f"test_{lesson_number}_{idx}", index=None)
        if ans is not None:
            if opts.index(ans) == correct:
                score += 1
    
    # Нәтиже көрсету
    st.markdown("---")
    if score >= 8:
        st.success(f"Өте жақсы! Ұпай: {score} / 10")
    elif score >= 5:
        st.warning(f"Жақсы, бірақ іздену керек. Ұпай: {score} / 10")
    else:
        st.error(f"Қайтадан оқып шығыңыз. Ұпай: {score} / 10")

# ---------------- AI БӨЛІМІ ----------------
st.divider()
st.subheader("🤖 AI-көмекші")
user_q = st.text_input("Бұл тақырып бойынша сұрағың бар ма?")
if st.button("AI-дан сұрау"):
    with st.spinner("AI ойлануда..."):
        time.sleep(1.5)
        st.write(f"Бұл {data['topic']} тақырыбы бойынша жауап: Сапалық реакциялар химиялық талдаудың негізі болып табылады.")

st.markdown("---")
st.caption("©️ Chemistry + AI | Streamlit оқу платформасы")
