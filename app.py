import streamlit as st
import time

st.set_page_config(page_title="Chemistry AI Lab - Improved Animation", layout="wide")

# ---------------- ТЕХНИКАЛЫҚ ДЕРЕКТЕР (34 САБАҚ) ----------------
lesson_data = {
    1: {"topic": "Алкендердің сапалық реакциясы", "formula_l": "C_2H_4", "formula_r": "Br_2", "obs": "Қоңыр түс жойылады", "res": "Қанықпаған байланыс (C=C) анықталды"},
    2: {"topic": "Көп атомды спирттер", "formula_l": "C_3H_5(OH)_3", "formula_r": "Cu(OH)_2", "obs": "Ашық көк ерітінді түзіледі", "res": "Көршілес -OH топтары бар"},
    3: {"topic": "Альдегидтер (Күміс айна)", "formula_l": "CH_3CHO", "formula_r": "Ag(NH_3)_2OH", "obs": "Пробирка бетінде күміс қабаты", "res": "Альдегид тобы (-CHO) бар"},
    4: {"topic": "Карбон қышқылдары", "formula_l": "CH_3COOH", "formula_r": "NaHCO_3", "obs": "Көпіршіктер (газ) бөлінеді", "res": "Карбоксил тобы (-COOH) анықталды"},
    5: {"topic": "Анилинді анықтау", "formula_l": "C_6H_5NH_2", "formula_r": "Br_2(aq)", "obs": "Ақ тұнба түзіледі", "res": "Ароматты амин анықталды"},
    6: {"topic": "Глюкозаның тотығуы", "formula_l": "C_6H_{12}O_6", "formula_r": "Cu(OH)_2 + heat", "obs": "Кірпіш-қызыл тұнба", "res": "Альдегид тобы бар қант"},
    7: {"topic": "Ақуыздар (Биурет)", "formula_l": "Protein", "formula_r": "CuSO_4 + NaOH", "obs": "Күлгін түс", "res": "Пептидтік байланыс анықталды"},
    8: {"topic": "Крахмалды анықтау", "formula_l": "(C_6H_{10}O_5)_n", "formula_r": "I_2", "obs": "Көк-күлгін түс", "res": "Полисахарид бар"},
    9: {"topic": "Фенолды анықтау", "formula_l": "C_6H_5OH", "formula_r": "FeCl_3", "obs": "Күлгін ерітінді", "res": "Фенол тобы бар"},
    10: {"topic": "Алкиндер (Ацетилен)", "formula_l": "C_2H_2", "formula_r": "KMnO_4", "obs": "Ерітінді түссізденеді", "res": "Үштік байланыс (C≡C) бар"}
}
# Қалған сабақтарды (11-34) циклмен толтыру (үлгі ретінде)
for i in range(11, 35):
    lesson_data[i] = {
        "topic": f"Органикалық талдау №{i}",
        "formula_l": "R-H", "formula_r": "Reagent",
        "obs": "Түс өзгеруі", "res": "Функционалдық топ анықталды"
    }

# ---------------- SIDEBAR ----------------
st.sidebar.title("📘 34 САБАҚТЫҚ КУРС")
lesson_idx = st.sidebar.selectbox("Сабақты таңдаңыз", list(range(1, 35)))
mode = st.sidebar.radio("Режим", ["Оқушы", "Мұғалім"])

# ---------------- UI FUNCTIONS ----------------
def show_lab_animation_advanced(data):
    st.subheader("🔬 Интерактивті зертхана")
    
    # 3 бағанды орналастыру, ортадағы баған кеңірек
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # ASCII артпен пробиркаларды көрсету
    with col1:
        st.markdown("""
<pre style='font-family: monospace; white-space: pre; background-color: #f0f2f6; padding: 10px; border-radius: 5px; text-align: center;'>
      .--.
     |____|  (жоғары)
     |    |
     |----| <--- Сұйықтық
     | {} |
     `----'
</pre>
        """, unsafe_allow_html=True)
        st.latex(data["formula_l"])
        st.caption("1-ші реагент (сол)", help="Бұл пробиркадағы ерітінді")

    with col2:
        central_display = st.empty() # Орталық пробирканың мазмұнын динамикалық өзгерту үшін
        central_display.markdown("""
<pre style='font-family: monospace; white-space: pre; background-color: #f0f2f6; padding: 10px; border-radius: 5px; text-align: center;'>
      .--.
     |____|
     |    |
     |    |
     |    |
     `----'
</pre>
        """, unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>--- Ортадағы бос пробирка ---</p>", unsafe_allow_html=True)

    with col3:
        st.markdown("""
<pre style='font-family: monospace; white-space: pre; background-color: #f0f2f6; padding: 10px; border-radius: 5px; text-align: center;'>
      .--.
     |____|  (жоғары)
     |    |
     |----| <--- Сұйықтық
     | {} |
     `----'
</pre>
        """, unsafe_allow_html=True)
        st.latex(data["formula_r"])
        st.caption("2-ші реагент (оң)", help="Бұл пробиркадағы ерітінді")

    st.markdown("---") # Визуалды бөлу үшін
    
    if st.button("Реакцияны бастау 🚀"):
        st.write("---")
        progress_bar = st.progress(0)
        status_message = st.empty()

        # Құю анимациясы
        for i in range(1, 11): # 10 қадамды құю
            time.sleep(0.1)
            progress = i * 10
            progress_bar.progress(progress)
            
            # Ортадағы пробиркаға сұйықтық толтыруды имитациялау
            liquid_level = i
            empty_lines = 4 - liquid_level # Бос жолдар саны
            liquid_lines = liquid_level    # Сұйықтық жолдарының саны

            central_display.markdown(f"""
<pre style='font-family: monospace; white-space: pre; background-color: #f0f2f6; padding: 10px; border-radius: 5px; text-align: center;'>
      .--.
     |____|
{''.join(['     |    |\\n' for _ in range(empty_lines)])}
{''.join(['     |~~~~| <span style="color: #4CAF50;">💦</span>\\n' for _ in range(liquid_lines)])}
     `----'
</pre>
            """, unsafe_allow_html=True)
            status_message.info(f"💧 Ерітінділер құйылуда... ({i*10}%)")

        time.sleep(0.5)
        status_message.empty()
        st.success(f"**Реакция аяқталды!**")
        st.write(f"**Бақылау:** {data['obs']}")
        st.write(f"**Қорытынды:** {data['res']}")

        # Соңғы нәтиже (ортадағы пробирка толығымен толған)
        central_display.markdown(f"""
<pre style='font-family: monospace; white-space: pre; background-color: #f0f2f6; padding: 10px; border-radius: 5px; text-align: center;'>
      .--.
     |____|
     |~~~~|
     |~~~~|
     |~~~~|
     `----'
</pre>
        """, unsafe_allow_html=True)


# ---------------- MAIN CONTENT ----------------
current_lesson = lesson_data[lesson_idx]
st.title(f"Сабақ {lesson_idx}: {current_lesson['topic']}")

tab1, tab2, tab3 = st.tabs(["📖 Теория", "🧪 Лаборатория", "📝 Тест"])

with tab1:
    st.info(f"Бұл сабақта біз ${current_lesson['formula_l']}$ қосылысының ${current_lesson['formula_r']}$ көмегімен сапалық анықталуын зерттейміз. Реакция барысында ${current_lesson['obs']}$ байқалып, ${current_lesson['res']}$ қорытындысы жасалады.")

with tab2:
    show_lab_animation_advanced(current_lesson)

with tab3:
    st.write("Сұрақ: Төмендегі реакцияның негізгі белгісі қандай?")
    options = [current_lesson['obs'], "Газ бөліну", "Тұнбаның еруі", "Жылу бөліну"]
    # Оң жауапты кездейсоқ орналастыру үшін
    import random
    random.shuffle(options)
    
    ans = st.radio("Жауапты таңдаңыз:", options)
    if st.button("Тексеру"):
        if ans == current_lesson['obs']:
            st.success("Дұрыс! Міне, осылайша біз осы функционалдық топты анықтаймыз.")
        else:
            st.error("Қате жауап. Теория бөлімін қайта қарап шығыңыз немесе зертханалық жұмысты қайталаңыз.")

st.markdown("---")
st.caption("© Chemistry + AI Platform | Streamlit Animation Demo")
