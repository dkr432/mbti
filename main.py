import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

# MBTI별 포켓몬 데이터
mbti_pokemon = {
    "INTJ": {
        "name": "뮤츠",
        "emoji": "🧠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "description": "전략적이고 독립적인 당신! 뮤츠처럼 강력한 지능과 카리스마를 가졌어요.",
        "traits": "지적이고 신비로운 매력 ✨"
    },
    "INTP": {
        "name": "폴리곤",
        "emoji": "💻",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png",
        "description": "논리적이고 호기심 많은 당신! 폴리곤처럼 분석적인 사고를 가졌어요.",
        "traits": "이론과 탐구를 사랑하는 천재형 🔍"
    },
    "ENTJ": {
        "name": "리자몽",
        "emoji": "🔥",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "description": "타고난 리더! 리자몽처럼 강력하고 카리스마 넘치는 지휘관이에요.",
        "traits": "목표를 향해 불타오르는 열정 🔥"
    },
    "ENTP": {
        "name": "후딘",
        "emoji": "💡",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "description": "창의적이고 토론을 즐기는 당신! 후딘처럼 똑똑하고 재치있어요.",
        "traits": "아이디어 뱅크 발명가 스타일 🎨"
    },
    "INFJ": {
        "name": "루카리오",
        "emoji": "🌙",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "description": "직관적이고 신념이 강한 당신! 루카리오처럼 파동을 읽는 통찰력이 있어요.",
        "traits": "조용한 카리스마의 이상주의자 🌟"
    },
    "INFP": {
        "name": "이브이",
        "emoji": "🌸",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "description": "꿈 많고 따뜻한 당신! 이브이처럼 무한한 가능성을 품고 있어요.",
        "traits": "감성충만 로맨티스트 💕"
    },
    "ENFJ": {
        "name": "럭키",
        "emoji": "💖",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/113.png",
        "description": "타인을 돌보는 따뜻한 리더! 럭키처럼 주변에 행복을 나눠줘요.",
        "traits": "사람들의 멘토이자 치유자 🤗"
    },
    "ENFP": {
        "name": "피카츄",
        "emoji": "⚡",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "description": "활발하고 매력적인 당신! 피카츄처럼 모두에게 사랑받는 에너자이저!",
        "traits": "긍정 에너지 뿜뿜 인싸 ⚡"
    },
    "ISTJ": {
        "name": "거북왕",
        "emoji": "🛡️",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "description": "책임감 강하고 신뢰할 수 있는 당신! 거북왕처럼 든든한 수호자예요.",
        "traits": "원칙주의자 신뢰의 아이콘 🏛️"
    },
    "ISFJ": {
        "name": "푸린",
        "emoji": "🎵",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "description": "헌신적이고 따뜻한 당신! 푸린처럼 부드럽게 주변을 감싸줘요.",
        "traits": "조용히 모두를 챙기는 천사 😇"
    },
    "ESTJ": {
        "name": "나시",
        "emoji": "📋",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/103.png",
        "description": "체계적이고 추진력 있는 당신! 나시처럼 든든하고 책임감이 있어요.",
        "traits": "조직의 기둥, 현실 관리자 💼"
    },
    "ESFJ": {
        "name": "이상해꽃",
        "emoji": "🌺",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/3.png",
        "description": "사교적이고 다정한 당신! 이상해꽃처럼 주변을 향기롭게 만들어요.",
        "traits": "분위기 메이커 사교의 달인 🌷"
    },
    "ISTP": {
        "name": "갸라도스",
        "emoji": "🌊",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/130.png",
        "description": "쿨하고 실용적인 당신! 갸라도스처럼 평소엔 조용하지만 강력해요.",
        "traits": "차분한 행동파 장인 🔧"
    },
    "ISFP": {
        "name": "샤미드",
        "emoji": "💧",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/134.png",
        "description": "예술적이고 자유로운 당신! 샤미드처럼 우아하고 감성적이에요.",
        "traits": "조용한 예술가 감성러 🎨"
    },
    "ESTP": {
        "name": "괴력몬",
        "emoji": "💪",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/68.png",
        "description": "모험가 정신의 당신! 괴력몬처럼 에너지 넘치고 행동력이 짱이에요.",
        "traits": "도전을 즐기는 액션 히어로 🎯"
    },
    "ESFP": {
        "name": "픽시",
        "emoji": "🎉",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/36.png",
        "description": "흥 많고 사랑스러운 당신! 픽시처럼 어디서든 빛나는 스타예요.",
        "traits": "파티의 주인공 자유로운 영혼 🌈"
    }
}

# MBTI 측정용 질문 (각 지표별 3문항)
questions = [
    # E vs I
    {
        "q": "1. 주말에 친구들과 약속이 있을 때 나는?",
        "a": "🎉 신난다! 사람들 만나는 게 너무 좋아!",
        "b": "🏠 음... 사실 집에서 쉬는 게 더 편해.",
        "type": "EI"
    },
    {
        "q": "2. 처음 보는 사람들 사이에 있을 때 나는?",
        "a": "🗣️ 먼저 다가가서 말을 건다.",
        "b": "👀 누가 말 걸어주길 기다린다.",
        "type": "EI"
    },
    {
        "q": "3. 에너지를 충전하는 방법은?",
        "a": "👯 사람들과 어울리면서 충전!",
        "b": "🛏️ 혼자만의 시간으로 충전!",
        "type": "EI"
    },
    # S vs N
    {
        "q": "4. 새로운 정보를 받아들일 때 나는?",
        "a": "📊 구체적인 사실과 경험을 중시한다.",
        "b": "💭 숨겨진 의미와 가능성을 상상한다.",
        "type": "SN"
    },
    {
        "q": "5. 영화를 볼 때 나는?",
        "a": "🎬 스토리의 사실적인 전개가 좋다.",
        "b": "✨ 상징과 메시지를 해석하는 게 좋다.",
        "type": "SN"
    },
    {
        "q": "6. 길을 설명할 때 나는?",
        "a": "🗺️ 정확한 거리와 방향을 알려준다.",
        "b": "🌳 '큰 나무 보이면 거기서 왼쪽~' 같이 설명한다.",
        "type": "SN"
    },
    # T vs F
    {
        "q": "7. 친구가 고민 상담을 할 때 나는?",
        "a": "🧐 논리적으로 해결책을 제시한다.",
        "b": "🤗 먼저 공감하고 위로해준다.",
        "type": "TF"
    },
    {
        "q": "8. 결정을 내릴 때 더 중요한 것은?",
        "a": "⚖️ 객관적인 사실과 효율성",
        "b": "❤️ 사람들의 감정과 관계",
        "type": "TF"
    },
    {
        "q": "9. 칭찬을 받았을 때 나는?",
        "a": "🤔 '진짜 그런가?' 하고 분석한다.",
        "b": "😊 기분이 너무 좋아서 행복하다!",
        "type": "TF"
    },
    # J vs P
    {
        "q": "10. 여행을 갈 때 나는?",
        "a": "📋 미리 계획을 꼼꼼히 짠다.",
        "b": "🎒 즉흥적으로 떠나는 게 좋다.",
        "type": "JP"
    },
    {
        "q": "11. 방학 숙제를 할 때 나는?",
        "a": "📅 미리미리 계획대로 끝낸다.",
        "b": "🔥 막판에 몰아서 한다.",
        "type": "JP"
    },
    {
        "q": "12. 책상은 보통 어떤 상태?",
        "a": "✨ 항상 정리정돈되어 있다.",
        "b": "🌪️ 어수선하지만 내 나름의 질서가 있다.",
        "type": "JP"
    }
]

# 커스텀 CSS
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 3em;
        background: linear-gradient(90deg, #FF6B6B, #FFD93D, #6BCB77, #4D96FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        padding: 20px;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2em;
        color: #666;
        margin-bottom: 30px;
    }
    .result-box {
        background: linear-gradient(135deg, #FFF5F5 0%, #FFE5EC 100%);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .pokemon-name {
        font-size: 2.5em;
        color: #FF6B6B;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<div class="main-title">⚡ MBTI 포켓몬 추천기 ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 MBTI에 어울리는 포켓몬을 찾아보세요! 🎮</div>', unsafe_allow_html=True)

st.markdown("---")

# 탭으로 모드 분리
tab1, tab2, tab3 = st.tabs(["🎯 MBTI 직접 선택", "📝 MBTI 간단 테스트", "🔘 지표별 선택"])

# 결과 표시 함수
def show_result(mbti):
    pokemon = mbti_pokemon[mbti]
    st.balloons()
    
    st.markdown(f"""
        <div class="result-box">
            <h2>당신의 MBTI는 <span style="color:#4D96FF;">{mbti}</span>!</h2>
            <h3>{pokemon['emoji']} 당신과 어울리는 포켓몬은...</h3>
            <div class="pokemon-name">{pokemon['name']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(pokemon['image'], use_container_width=True)
    
    st.success(f"✨ **특징**: {pokemon['traits']}")
    st.info(f"💌 **설명**: {pokemon['description']}")

# 탭 1: 직접 선택
with tab1:
    st.markdown("### 🎯 본인의 MBTI를 알고 있다면 바로 선택하세요!")
    mbti_direct = st.selectbox(
        "MBTI 선택",
        list(mbti_pokemon.keys()),
        key="direct_select"
    )
    
    if st.button("🎯 내 포켓몬 찾기!", use_container_width=True, key="btn_direct"):
        show_result(mbti_direct)

# 탭 2: 간단 테스트
with tab2:
    st.markdown("### 📝 12개의 질문에 답하고 MBTI를 알아보세요!")
    st.caption("각 문항에서 더 가까운 쪽을 선택해주세요 ✨")
    
    answers = {}
    
    with st.form("mbti_test"):
        for i, question in enumerate(questions):
            st.markdown(f"**{question['q']}**")
            answers[i] = st.radio(
                "선택",
                [question['a'], question['b']],
                key=f"q_{i}",
                label_visibility="collapsed"
            )
            st.markdown("")  # 간격
        
        submitted = st.form_submit_button("🔮 내 MBTI 알아보기!", use_container_width=True)
    
    if submitted:
        # 점수 계산
        scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        
        for i, question in enumerate(questions):
            chosen = answers[i]
            q_type = question['type']
            
            if chosen == question['a']:
                # a 선택 시 앞 글자
                scores[q_type[0]] += 1
            else:
                # b 선택 시 뒷 글자
                scores[q_type[1]] += 1
        
        # MBTI 조합
        mbti_result = ""
        mbti_result += "E" if scores["E"] >= scores["I"] else "I"
        mbti_result += "S" if scores["S"] >= scores["N"] else "N"
        mbti_result += "T" if scores["T"] >= scores["F"] else "F"
        mbti_result += "J" if scores["J"] >= scores["P"] else "P"
        
        # 점수 시각화
        st.markdown("### 📊 당신의 성향 분석")
        col1, col2 = st.columns(2)
        with col1:
            st.progress(scores["E"]/3, text=f"E (외향) {scores['E']}/3")
            st.progress(scores["S"]/3, text=f"S (감각) {scores['S']}/3")
            st.progress(scores["T"]/3, text=f"T (사고) {scores['T']}/3")
            st.progress(scores["J"]/3, text=f"J (판단) {scores['J']}/3")
        with col2:
            st.progress(scores["I"]/3, text=f"I (내향) {scores['I']}/3")
            st.progress(scores["N"]/3, text=f"N (직관) {scores['N']}/3")
            st.progress(scores["F"]/3, text=f"F (감정) {scores['F']}/3")
            st.progress(scores["P"]/3, text=f"P (인식) {scores['P']}/3")
        
        st.markdown("---")
        show_result(mbti_result)

# 탭 3: 지표별 선택
with tab3:
    st.markdown("### 🔘 4가지 지표를 직접 선택하세요!")
    
    col1, col2 = st.columns(2)
    with col1:
        ei = st.radio("🌟 외향 vs 내향", ["E (외향)", "I (내향)"], horizontal=True, key="ei")
        sn = st.radio("🔍 감각 vs 직관", ["S (감각)", "N (직관)"], horizontal=True, key="sn")
    with col2:
        tf = st.radio("💭 사고 vs 감정", ["T (사고)", "F (감정)"], horizontal=True, key="tf")
        jp = st.radio("📅 판단 vs 인식", ["J (판단)", "P (인식)"], horizontal=True, key="jp")
    
    mbti_radio = ei[0] + sn[0] + tf[0] + jp[0]
    
    if st.button("🎯 내 포켓몬 찾기!", use_container_width=True, key="btn_radio"):
        show_result(mbti_radio)

# 푸터
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#999;">Made with ❤️ for 당곡고 학생들 | Pokémon © Nintendo</p>',
    unsafe_allow_html=True
)
