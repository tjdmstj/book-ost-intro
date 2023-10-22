import streamlit as st

st.header('📗 추천 도서 리스트')
with st.expander('AF : 가사 : 키워드 = 0.8 : 0.1 : 0.1 인 경우'):
    col1,col2,col3= st.columns([1,1,1])
    with col1:
        st.markdown('**1. 참을 수 없는 존재의 가벼움**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/71f6da54-1ac8-4581-8f77-f55ed5c56dbc/image.png')
        st.caption('사랑은 은유로 시작된다. 달리 말하자면, 한 여자가 언어를 통해 우리의 시적 기억에 아로새겨지는 순간, 사랑은 시작되는 것이다.')
        st.caption('그들은 서로 사랑했는데도 상대방에게 하나의 지옥을 선사했다.')
    with col2:
        st.markdown('**2. 이성과 감성**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/74f8850c-4d18-42f5-ac29-7e3a1f4f68f4/image.png')
        st.caption('"이성"과 "감성"이라는 두 가지 인간성을 연애와 결혼이라는 보편적 주제를 통한 고찰')
    with col3:
        st.markdown('**3. 지금, 만나러 갑니다**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/fca0c4eb-51bb-4b3c-93d0-866ed37f60fc/image.png')
        st.caption('당신에겐 있나요? 기적같은 단 한사람')
        st.caption('그 사람을 다시 한 번 만날 수 있다면.')
        st.caption('')
        st.caption('더 이상 볼 수 없게 된 그리운 사람과의 기적 같은 재회를 그린다. 1년 전 세상을 떠난 아내 미오를 그리워하며 하루하루를 보내는 다쿠미는 비 오는 날 아들 유지와 함께 찾은 숲속에서 놀랍게도 죽은 미오와 재회한다. 이야기는 누구보다 차근차근 마음을 쌓아가며 느리게 사랑해온 두 사람의 과거로 거슬러 올라간다.')
    
    col4,col5,col6= st.columns([1,1,1])
    with col4:
        st.markdown('**4. 모순**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/66e26a96-c2d5-4c15-a931-66093fb0798e/image.png')
        st.caption('인생은 탐구하면서 살아가는 것이 아니라, 살아가면서 탐구하는 것이다. 실수는 되풀이된다. 그것이 인생이다…….')
        st.caption('바로 그 이유 때문에 사랑을 시작했고, 바로 그 이유 때문에 미워하게 된다는, 인간이란 존재의 한없는 모순......')
    with col5:
        st.markdown('**5. 사랑의 파괴**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/0192b5f2-7218-42b7-a5dc-7fa66f654f1c/image.png')
        st.caption('엘레나는 자신을 위해서 내가 나 자신을 파괴하기를 원하고 있었다.')
        st.caption('사랑하는 만큼 사랑받고자 하는 욕망, 순진하기에 더욱더 잔혹한 유년의 사랑')
    with col6:
        st.markdown('**6. 제인에어**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/e2c36e8d-7446-44af-a387-3f43e968d713/image.png')
        st.caption('순응하고 인내하며 봉사하는 여성이 이상적으로 여겨지던 빅토리아 시대에, 현실적인 조건이나 개인적 자질에서 이와 동떨어진 여성인 제인의 성장을 통해 당대 여성의 삶 전반, 즉 여성의 교육, 고용, 사랑, 결혼에 대한 의문')
        
    col7,col8,col9= st.columns([1,1,1])
    with col7:
        st.markdown('**7. 무의미의 축제**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/8e967400-dc99-4d63-8ed1-94ab93396b0e/image.png')
        st.caption('보잘것없는 것을 사랑해야 해요,사랑하는 법을 배워야 해요.')
        st.caption('농담과 거짓말, 의미와 무의미, 일상과 축제의 경계에서삶과 인간의 본질을 바라보는 시선')
    with col8:
        st.markdown('**8. 80일간의 세계일주**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/8875c9d4-d568-4242-a478-4358e97411df/image.png')
        st.caption('2만 파운드를 걸고 80일 동안의 세계 일주에 나선 영국 신사 필리어스 포그. ')
        st.caption('그는 기계처럼 정확하고 냉정한 영국 신사다. 한 치의 오차도 없이 여행을 계획하는 주인공을 통해 쥘 베른은 치밀하고 과학적이며 이성적인 인간과, 인간에 대한 신뢰와 애정 그리고 세계에 대한 긍정으로 차 있는 인간상을 그려 낸다.')
    with col9:
        st.markdown('**9. 몬테크리스토 백작**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/aef3eb6b-e3d9-4745-8b7b-07e592e4637b/image.png')
        st.caption('모든 악에는 두 개의 약이 있다. 시간과 침묵이 그것이다')
        st.caption('인간사에서 가장 흥겨운 이야기는 불행을 딛고 행복을 되찾는 이야기가 아닐까?')
        st.caption('모략과 함정에 빠지지만, 부와 명예를 회복하여 화려하게 복수한다는 이야기에 사람들은 쉽게 열광한다.')
        st.caption('<몬테크리스토 백작>이 대표적인 경우. 배신, 억울한 감금, 복수 이 3요소는 시대를 불문하고 독자들을 매료시켰다.')

    col10,col11,col12 = st.columns([1,1,1])
    with col10:
        st.markdown('**10. 페드르와 이폴리트**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/fc8c56f5-5661-427b-bb39-70c6e6169fe4/image.png')
        st.caption('인간은 진정 자신을 옥죄는 정념으로부터 스스로를 구할 의지도, 능력도 없는 존재인가.')
        st.caption('에우리피데스의 「히폴리토스」를 바탕으로 정념이 지닌 파괴적 본성,통제할 수 없는 정념에 빠진 한 인간이 보여 주는 감정의 격정을 파고든 라신 비극의 정수.')
    with col11:
        st.markdown('**11. 결혼ㆍ여름**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/81bbcf18-81e5-4952-853b-927bb8c2223d/image.png')
        st.caption('깊이 사랑하는 여인의 매력을 항목별로 조목조목 읊을 수 있겠는가?그럴 수 없다, 그냥 전체를 사랑하는 것이다.')
        st.caption('카뮈 사상의 핵심인 ‘부조리’와 ‘반항’의 출발 및 완성 과정이 육성으로 들리는 듯한 자전적 기록')

with st.expander('가사 중심인 경우'):
    col1,col2,col3= st.columns([1,1,1])
    with col1:
        st.markdown('**1. 참을 수 없는 존재의 가벼움**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/71f6da54-1ac8-4581-8f77-f55ed5c56dbc/image.png')
        st.caption('사랑은 은유로 시작된다. 달리 말하자면, 한 여자가 언어를 통해 우리의 시적 기억에 아로새겨지는 순간, 사랑은 시작되는 것이다.')
        st.caption('그들은 서로 사랑했는데도 상대방에게 하나의 지옥을 선사했다.')
    with col2:
        st.markdown('**2. 어린왕자**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/93a93b74-d728-4727-81b5-7af32114a2aa/image.png')
        st.caption('네가 오후 4시에 온다면 난 3시부터 설렐 거야. 4시가 가까워질수록 점점 더 행복해지겠지. 4시가 되면 난 가슴이 두근거려서 안절부절못하고 걱정을 할 거야. 행복의 대가를 알게 되겠지! 하지만 네가 아무 때나 온다면 언제부터 마음의 준비를 해야 할지 도무지 알 수 없잖아.')
        st.caption('순수성을 허락하지 않는 세상에서 끊임없이 방황하고 고뇌한 생텍쥐페리. 그는 세상을 바꿀 수는 없지만 희망을 그리고 싶었고, 자신이 동경하고 희망하는 삶을 ‘어린 왕자’로 형상화했다.')
    with col3:
        st.markdown('**3. 몬테크리스토 백작**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/aef3eb6b-e3d9-4745-8b7b-07e592e4637b/image.png')
        st.caption('모든 악에는 두 개의 약이 있다. 시간과 침묵이 그것이다')
        st.caption('인간사에서 가장 흥겨운 이야기는 불행을 딛고 행복을 되찾는 이야기가 아닐까?')
        st.caption('모략과 함정에 빠지지만, 부와 명예를 회복하여 화려하게 복수한다는 이야기에 사람들은 쉽게 열광한다.')
        st.caption('<몬테크리스토 백작>이 대표적인 경우. 배신, 억울한 감금, 복수 이 3요소는 시대를 불문하고 독자들을 매료시켰다.')
    
    col4,col5,col6= st.columns([1,1,1])
    with col4:
        st.markdown('**4. 로미오와 줄리엣**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/6edfa385-5695-4ba8-a14e-45ce4871f5ca/image.png')
        st.caption('오, 둥근 궤도 안에서 한 달 내내 변하는지조 없는 달에게 맹세하진 마세요')
        st.caption('다쳐 본 적 없는 자가 흉터를 비웃는 법…')
        st.caption('달빛 아래 주고받은 첫 키스와 사랑의 맹세,살아 있는 죽음을 통해 도달하는 죽음을 넘어서는 사랑!셰익스피어가 빚어낸 순수한 열정의 비극, 그 사랑의 모순어법')
    with col5:
        st.markdown('**5. 아주 편안한 죽음**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/86c06fae-d47c-462f-b8bf-2fbfadcd9f33/image.png')
        st.caption('엄마는 유년 시절 내내 규범과 금기라는 갑옷을 두른 채 몸과 마음, 정신을 억압당했다. 그리고 스스로를 끈으로 옭아매도록 교육받았다. 그런 엄마의 내면에는끓어오르는 피와 불같은 정열을 지닌 한 여인이 살아 숨 쉬고 있었다. 그러나 그 여인은 뒤틀리고 훼손된 끝에 자기 자신에게조차 낯선 존재가 되어 버린 모습이었다.')
        st.caption('주체성을 포기하며 타자로 살도록 강요받아 온 한 인간의 생애, 나아가 당대 여성 전체의 모습. ')
        st.caption('냉대하며 외면했던 세계를 새롭게 인식하며 자기 정체성의 일부로 받아들이는 과정이며, 그와 동시에 남과 여, 육체와 정신, 삶과 죽음 등 구별 짓기로 가득했던 인간 내면의 경계를 허무는 작품.')
    with col6:
        st.markdown('**6. 무의미의 축제**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/8e967400-dc99-4d63-8ed1-94ab93396b0e/image.png')
        st.caption('보잘것없는 것을 사랑해야 해요,사랑하는 법을 배워야 해요.')
        st.caption('농담과 거짓말, 의미와 무의미, 일상과 축제의 경계에서삶과 인간의 본질을 바라보는 시선')
    col7,col8,col9= st.columns([1,1,1])
    with col7:
        st.markdown('**7. 잘못 걸려온 전화**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/9fa4d386-e2fa-435d-91bc-7841c5ddd96e/image.png')
        st.caption('그런 식으로 세월은 흘러갈 것이다. 그리고 악몽 같던 내 인생의 장면들이 눈에 선할 것이다. 그러나 나는 이제 그것들로 인해 아파하지 않을 것이다.')
        st.caption('죽음, 사랑, 그리고 상실"아고타 크리스토프의 작품 중 가장 낯설고 비밀스러운 악몽과 우화" - 르 몽드(Le Monde)')
    with col8:
        st.markdown('**8. 파우스트**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/9bc7048f-9e21-43cc-8db8-a71bb1bc8dfa/image.png')
        st.caption('내가 너의 노예가 되어 이 세상 모든 영화를 체험하게 해주는 대신，네가 어느 한순간 `멈추어라．너는 너무도 아름답다’라며 휴식을 원하면 그때부터 너의 영혼은 영원히 나의 것이다.')
        st.caption('지식과 학문에 절망한 노학자 파우스트 박사의 미망(迷妄)과 구원의 장구한 노정을 그린다. 악마 메피스토펠레스의 유혹에 빠져 현세의 쾌락을 쫓으며 방황하던 파우스트는 마침내 잘못을 깨닫고 천상의 구원을 받는다.')
    with col9:
        st.markdown('**9. 어떻게든 이별**')
        st.image('https://velog.velcdn.com/images/jeo0534/post/10ca695a-924b-44be-a573-1227e1525510/image.png')
        st.caption('이 계절은 조금 가벼운 절망을 앓기에 얼마나 찬란한가')
        st.caption('사랑, 결국에는 이별, 끝내 불가피한 고독지극한 상처 안에 웃음을 품은 쓸쓸한 통찰')