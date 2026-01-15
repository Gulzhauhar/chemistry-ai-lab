import streamlit as st
import time

st.set_page_config(page_title="Chemistry Lab AI 34", layout="wide")

# ---------------- CSS: ЖӨНДЕЛГЕН АНИМАЦИЯ ----------------
st.markdown("""
<style>
    .lab-container { 
        display: flex; justify-content: center; align-items: center; 
        height: 350px; background: #0e1117; border-radius: 15px; 
        padding: 20px; position: relative;
    }
    .reaction-label {
        position: absolute; top: 40px; color: gold; font-weight: bold;
        font-size: 20px; text-shadow: 2px 2px 4px #000;
        opacity: 0; transition: opacity 0.5s;
    }
    .show-label { opacity: 1; }
    .tube-box { display: flex; align-items: flex-end; gap: 60px; }
    .tube { 
        width: 35px; height: 120px; border: 2px solid #fff; 
        border-top: none; border-bottom-left-radius: 18px; 
        border-bottom-right-radius: 18px; position: relative; 
    }
    .liquid { 
        position: absolute; bottom: 0; width: 100%; 
        border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;
        transition: all 1.2s ease;
    }
    @keyframes pour-left { 0% { transform: rotate(0); } 100% { transform: rotate(70deg) translate(25px, -25px); } }
    @keyframes pour-right { 0% { transform: rotate(0); } 100% { transform: rotate(-70deg) translate(-25px, -25px); } }
    .pouring-left { animation: pour-left 1.2s forwards; }
    .pouring-right { animation: pour-right 1.2s forwards; }
</style>
""", unsafe_allow_html=True)

# ---------------- DATA GENERATOR (34 LESSONS) ----------------
def get_lesson_data(n):
    # Нақтыланған сапалық реакциялар базасы
    chemistry_db = {
        1: {"topic": "Алкендер (Бромдау)", "rxn": "Галогендеу", "lab": ("Br₂", "Түссіздену", "#E67E22", "rgba(255,255,255,0.1)")},
        2: {"topic": "Көп атомды спирттер", "rxn": "Глицерат түзілуі", "lab": ("Cu(OH)₂", "Ашық көк ерітінді", "#3498DB", "#0000FF")},
        3: {"topic": "Альдегидтер (Күміс айна)", "rxn": "Тотығу", "lab": ("AgNO₃ + NH₃", "Күміс жалатылуы", "#BDC3C7", "#7F8C8D")},
        4: {"topic": "Карбон қышқылдары", "rxn": "Бейтараптану", "lab": ("Лакмус", "Қызару", "#9B59B6", "#E74C3C")},
        5: {"topic": "Ақуыздар (Биурет)", "rxn": "Пептидтік байланыс", "lab": ("CuSO₄ + NaOH", "Күлгін түс", "#3498DB", "#8E44AD")},
    }
    
    # Базада жоқ сабақтар үшін автоматты шаблон
    res = chemistry_db.get(n, {
        "topic": f"{n}-сабақ: Функционалдық топтар",
        "rxn": "Сапалық талдау",
        "lab": ("Реактив", "Түс өзгеруі", "#95A5A6", "#2C3E50")
    })
    
    # Тест сұрақтары (Әрқашан 10 сұрақ)
    res["test"] = [(f"{res['topic']} бойынша {i+1}-сұрақ?", ["Қате", "Дұрыс", "Білмеймін"], 1) for i in range(10)]
    return res

# ---------------- LOGIC ----------------
lesson_selected = st.sidebar.selectbox("Сабақты таңдаңыз", [f"{i}-сабақ" for i in range(1, 35)])
n = int(lesson_selected.split("-")[0])
data = get_lesson_data(n)

st.title(f"🧪 {data['topic']}")

col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("🔬 Виртуалды тәжірибе")
    
    # Анимациялық контейнер
    placeholder = st.empty()
    
    def draw(pour=False, label=False, fill=0):
        l_pour = "pouring-left" if pour else ""
        r_pour = "pouring-right" if pour else ""
        l_show = "show-label" if label else ""
        
        placeholder.markdown(f"""
        <div class='lab-container'>
            <div class='reaction-label {l_show}'>{data['rxn']}</div>
            <div class='tube-box'>
                <div class='tube {l_pour}'><div class='liquid' style='height:70%; background:{data['lab'][2]};'></div></div>
                <div class='tube' style='border-color:gold; height:140px;'>
                    <div class='liquid' style='height:{fill}%; background:{data['lab'][3]};'></div>
                </div>
                <div class='tube {r_pour}'><div class='liquid' style='height:70%; background:rgba(255,255,255,0.3);'></div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    draw() # Бастапқы күй (Ортасы бос)

    if st.button("Реакцияны бастау"):
        # 1. Құю басталуы
        draw(pour=True, label=True, fill=0)
        time.sleep(1.2)
        # 2. Ортасы толуы және түс өзгеруі
        draw(pour=False, label=True, fill=85)
        st.success(f"Бақылау: {data['lab'][1]}")

with col2:
    st.subheader("📝 Тест (0/10)")
    score = 0
    for i, (q, opts, correct) in enumerate(data["test"]):
        ans = st.radio(q, opts, key=f"q{n}_{i}", index=None)
        if ans and opts.index(ans) == correct:
            score += 1
    
    st.divider()
    if score >= 8: st.success(f"Нәтиже: {score}/10")
    else: st.warning(f"Нәтиже: {score}/10")

st.caption("© Chemistry Lab AI 2026 | Барлық 34 сабақ белсенді")
