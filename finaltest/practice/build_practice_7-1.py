"""The Reading 7-1 Practice Questions — 단원별 연습문항 10개 (8단원 × 10 = 80문항).

대상·형식은 Final Test와 같다: 초6, 학생용은 전부 영어, 5지선다, 정답 하나.
각 단원은 Final Test와 같은 유형군을 쓰고 난이도 1→5를 두 번 밟는다 (1,1,2,2,3,3,4,4,5,5).
지문은 교재 원문 전체를 싣고, Final Test에 낸 문항과는 다른 문항을 낸다.
번호는 단원마다 1~10으로 다시 매기고, 단원마다 새 쪽에서 시작한다.

  Set A (1·5 Art)      : 어휘 ×2 → 세부 사실 ×2 → 지칭 추론 ×2 → 사건 순서 배열·내용 불일치 → 추론 ×2
  Set B (2·6 Nature)   : 문맥상 동의어 ×2 → 세부 사실 ×2 → 언급 이유 ×2 → 내용 불일치·내용 일치 → 요약문 ×2
  Set C (3·7 Social)   : 세부 사실 ×2 → 문장 빈칸 어휘 ×2 → 문단 주제·제목 → 내용 일치·불일치 → 글쓴이의 주장·추론
  Set D (4·8 Science)  : 세부 사실 ×2 → 어휘 ×2 → 도표 완성·요약문 → 문단 주제 ×2 → 빈칸 추론 ×2

표기: ⟪단어⟫ 밑줄, ______ 빈칸, (a)/(b) 빈칸 번호.
"""
import json
import sys
from collections import Counter
from pathlib import Path

GLOSS = True
LEVEL = {1: "매우 쉬움", 2: "쉬움", 3: "보통", 4: "다소 어려움", 5: "어려움"}
EXPECTED_P = {1: 0.97, 2: 0.92, 3: 0.85, 4: 0.77, 5: 0.65}
LEVELS = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

SUMQ = "Complete the summary of the passage. Which words best fit (A) and (B)?"
ORDQ = "Which is the correct order of (A), (B), and (C), from first to last?"
TBLQ = "Complete the table about the passage. Which words best fit (A) and (B)?"
NOTTRUE = "Which is *NOT* true according to the passage?"
TRUE = "Which is true according to the passage?"
TITLE = "What is the best title for the passage?"
AGREE = "Which idea would the writer most likely agree with?"
INFER = "What can we learn from the passage?"
ORD3 = ["(A) – (B) – (C)", "(A) – (C) – (B)", "(B) – (A) – (C)", "(B) – (C) – (A)", "(C) – (A) – (B)", "(C) – (B) – (A)"]


def item(lv, kind, prompt, answer, wrong, pos, expl, **extra):
    assert len(wrong) == 4 and answer not in wrong and 1 <= pos <= 5, (prompt, answer)
    choices = list(wrong)
    choices.insert(pos - 1, answer)
    d = {"type": "multiple_choice", "prompt": prompt, "choices": choices, "answer": pos,
         "explanation": f"[난이도 {lv}·{LEVEL[lv]} / {kind}] {expl}"}
    d.update(extra)
    d["_lv"], d["_kind"] = lv, kind
    return d


def order_item(lv, key, pos, expl, box):
    wrong = [o for o in ORD3 if o != key][:4]
    return item(lv, "사건 순서 배열", ORDQ, key, wrong, pos, expl, box=box)


UNITS = [
# ───────────────────────────── Unit 1 (Set A) ─────────────────────────────
dict(key="u1", set="A", title="Unit 1 · Art",
passage="""Throughout time, art has been used to ⟪decorate⟫ homes, churches, and public buildings. In modern times, art is used in advertisements, magazines, cartoons, and even on television! Art in advertisements has become increasingly popular. ⟪This⟫ is called commercial art. One of the most famous commercial artists was Andy Warhol.

Andy Warhol was often sick as a child, so he spent a lot of time drawing. After college, he began his ⟪career⟫ making art for advertisements. His drawings of shoes became so well known that people wanted to see more of his work. Thus, in the 1950s, he began showing his popular works in art galleries. Warhol was one of the first artists to use silkscreen ink printing in his work. During the 1960s, he produced many famous art pieces depicting everyday objects. These include Coca-Cola bottles, dollar bills, and Campbell’s Soup cans. This kind of art is referred to as “pop art.”

Some critics think Andy Warhol was only interested in making money with his art. ⟪Others⟫ thought he was the perfect example of commercialized modern life. Apart from this argument, most critics agree that Warhol’s work shows the changing value of art in everyday life.""",
gloss="Words: increasingly = more and more · advertisement = a picture or words that tell people to buy something · silkscreen ink printing = a way of printing pictures · depict = show, draw · critic = a person who gives opinions about art · commercialized = made to make money · argument = a disagreement",
items=[
 item(1, "어휘(단어 뜻)", "What does the underlined word ⟪decorate⟫ mean?",
      "make something look nicer", ["make something bigger", "make something clean", "make something cheaper", "make something quiet"], 3,
      "decorate(장식하다) = make something look nicer. 집·교회·공공건물을 ‘꾸미는’ 데 미술이 쓰여 왔다는 문맥이다."),
 item(1, "어휘(단어 뜻)", "What does the underlined word ⟪career⟫ mean?",
      "the job a person does for a long time", ["the house a person lives in", "the school a person goes to", "the family a person has", "the games a person plays"], 1,
      "career(경력, 직업) = the job a person does for a long time. 대학을 마친 뒤 광고 미술을 하며 ‘직업 생활’을 시작했다는 문맥이다."),
 item(2, "세부 사실", "According to the passage, when did Warhol begin showing his works in art galleries?",
      "in the 1950s", ["in the 1920s", "in the 1930s", "in the 1940s", "in the 1960s"], 4,
      "Thus, in the 1950s, he began showing his popular works in art galleries. 1960년대는 일상 사물을 그린 작품을 만든 시기이다."),
 item(2, "세부 사실", "According to the passage, what was Warhol one of the first artists to use?",
      "silkscreen ink printing", ["oil paint", "photographs", "computer pictures", "colored pencils"], 2,
      "Warhol was one of the first artists to use silkscreen ink printing in his work."),
 item(3, "지칭 추론", "What does the underlined word ⟪This⟫ refer to?",
      "art used in advertisements", ["art in churches", "art in public buildings", "art on television", "Andy Warhol’s drawings"], 5,
      "바로 앞 문장 Art in advertisements has become increasingly popular. 를 받아 ‘이것(광고 속 미술)’을 commercial art라고 부른다고 했다."),
 item(3, "지칭 추론", "What does the underlined word ⟪Others⟫ refer to?",
      "other critics", ["other artists", "other advertisements", "other art galleries", "other everyday objects"], 2,
      "앞 문장 Some critics think … 에 이어 Others thought … 이므로 ‘다른 비평가들’이다. 뒤에 most critics agree로 비평가 이야기가 이어진다."),
 order_item(4, "(B) – (C) – (A)", 1,
      "어릴 때 자주 아파서 그림을 많이 그림(B) → 대학 졸업 후 광고 미술 일을 시작(C) → 신발 그림이 유명해져 사람들이 작품을 더 보고 싶어 함(A). 2문단의 순서 그대로이다.",
      box="(A) People wanted to see more of Warhol’s work. \\\n(B) Warhol was often sick and spent a lot of time drawing. \\\n(C) Warhol began his career making art for advertisements."),
 item(4, "내용 불일치", NOTTRUE,
      "Warhol never used silkscreen ink printing.",
      ["Warhol was often sick as a child.", "Warhol made art for advertisements after college.", "Warhol showed his works in art galleries in the 1950s.", "Most critics agree that Warhol’s work shows the changing value of art."], 3,
      "Warhol was one of the first artists to use silkscreen ink printing — 실크스크린 인쇄를 ‘처음 사용한 화가 중 한 명’이므로 ‘전혀 쓰지 않았다’는 틀리다. 나머지는 본문과 일치한다."),
 item(5, "추론", INFER,
      "Critics do not all agree about why Warhol made his art.",
      ["Warhol never made money from his art.", "Warhol’s art was shown only in art galleries.", "People in the past did not use art to decorate buildings.", "Warhol stopped drawing after college."], 5,
      "Some critics think … Others thought … Apart from this argument — 비평가들의 의견이 갈렸다. Warhol은 상업 미술가로 돈을 벌었고, 작품은 광고에도 쓰였으며, 옛날에도 미술로 건물을 꾸몄고, 대학 졸업 후에도 계속 그림을 그렸다."),
 item(5, "추론", INFER,
      "Pop art used pictures of things people saw every day.",
      ["Pop art was made only for advertisements.", "Pop art showed mostly famous people.", "Pop art was made before Warhol was born.", "Pop art was shown only on television."], 1,
      "many famous art pieces depicting everyday objects … This kind of art is referred to as “pop art.” — 일상 사물(콜라병, 지폐, 수프 캔)을 그린 작품이 팝 아트이다. 팝 아트는 미술관에서 전시되었고, 유명인이 아니라 사물을 그렸으며, Warhol이 1960년대에 만들었다."),
]),
# ───────────────────────────── Unit 2 (Set B) ─────────────────────────────
dict(key="u2", set="B", title="Unit 2 · Nature",
passage="""The water cycle is ⟪necessary⟫ for life on Earth. Water on the ground evaporates into vapor and forms clouds in the sky. In return, rain brings water back down to the ground again, which ends up in streams, rivers, lakes, and oceans. What happens when humans tamper with the water cycle?

Most evaporation ⟪occurs⟫ in oceans as a result of the Sun’s energy. This cools the temperature of Earth’s climate and also affects the oceans’ salt content. Having the correct amount of salt in the oceans maintains a delicate ecosystem of plants, fish, and other wildlife. One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. The two rivers that fed the Aral Sea were diverted for farming in the desert. As a result, the sea is now almost completely dry, killing the wildlife that lived there and causing dust storms that affect human health.

As we can see, the water cycle is necessary to keep the environment balanced. It is important to understand the water cycle and to protect our water sources so they can function well for Earth’s sake.""",
gloss="Words: evaporate = change into gas · vapor = water in the air · end up = finally arrive · tamper with = change something in a bad way · affect = change something · salt content = the amount of salt · maintain = keep · ecosystem = all the living things in a place · disaster = a very bad event · fed = brought water to · divert = make a river go a different way · dust storm = a strong wind full of dust · function = work · for Earth’s sake = for the good of Earth",
items=[
 item(1, "문맥상 동의어", "Which can best replace the underlined word ⟪occurs⟫?",
      "happens", ["stops", "falls", "ends", "hides"], 2,
      "occur = happen(일어나다). 증발은 대부분 바다에서 ‘일어난다’는 뜻이다."),
 item(1, "문맥상 동의어", "Which can best replace the underlined word ⟪necessary⟫?",
      "needed", ["dangerous", "strange", "slow", "expensive"], 5,
      "necessary = needed(꼭 필요한). 물의 순환은 지구의 생명에 ‘꼭 필요하다’. 마지막 문단에서도 같은 단어가 쓰였다."),
 item(2, "세부 사실", "According to the passage, what causes most evaporation in the oceans?",
      "the Sun’s energy", ["the wind", "the Moon", "the salt", "the rain"], 4,
      "Most evaporation occurs in oceans as a result of the Sun’s energy."),
 item(2, "세부 사실", "According to the passage, where does rainwater end up?",
      "in streams, rivers, lakes, and oceans", ["in the clouds", "in the desert", "in the Sun", "in the air as vapor"], 3,
      "rain brings water back down to the ground again, which ends up in streams, rivers, lakes, and oceans."),
 item(3, "언급 이유", "Why does the writer mention dust storms?",
      "to show that the dry Aral Sea hurts people’s health",
      ["to explain how clouds are made", "to show how farmers water the desert", "to describe the weather in the ocean", "to explain why the sea is salty"], 4,
      "… causing dust storms that affect human health — 바다가 마른 결과로 생긴 모래 폭풍이 사람의 건강을 해친다는 것을 보여 주기 위해서이다."),
 item(3, "언급 이유", "Why does the writer mention the salt in the oceans?",
      "to show that the right amount of salt keeps sea life healthy",
      ["to explain why seawater tastes bad", "to show how people make salt", "to explain why fish die in rivers", "to show how clouds get their water"], 1,
      "Having the correct amount of salt in the oceans maintains a delicate ecosystem of plants, fish, and other wildlife — 알맞은 소금 양이 바다 생물의 생태계를 지켜 준다는 뜻이다."),
 item(4, "내용 불일치", NOTTRUE,
      "The Aral Sea is now full of water again.",
      ["Water on the ground evaporates and forms clouds.", "Most evaporation happens because of the Sun’s energy.", "Two rivers used to flow into the Aral Sea.", "The water cycle keeps the environment balanced."], 5,
      "the sea is now almost completely dry — Aral Sea는 거의 완전히 말라 있다. 나머지는 evaporates into vapor and forms clouds / as a result of the Sun’s energy / The two rivers that fed the Aral Sea / keep the environment balanced 와 일치한다."),
 item(4, "내용 일치", TRUE,
      "We should protect our water sources.",
      ["Rain never reaches the oceans.", "The Aral Sea dried up because of too much rain.", "Dust storms help the wildlife near the Aral Sea.", "The Sun has nothing to do with evaporation."], 2,
      "It is important … to protect our water sources. 비는 바다까지 흘러가고(ends up in … oceans), Aral Sea는 강물을 돌려서 말랐으며, 모래 폭풍은 사람의 건강을 해치고, 증발은 태양 에너지 때문에 일어난다."),
 item(5, "요약문 완성", SUMQ + "\n\nWater goes up into the sky as (A) ______ and comes back down as (B) ______.",
      "(A) vapor …… (B) rain",
      ["(A) rain …… (B) vapor", "(A) snow …… (B) clouds", "(A) vapor …… (B) snow", "(A) clouds …… (B) salt"], 3,
      "(A) Water on the ground evaporates into vapor — 물은 ‘수증기(vapor)’가 되어 올라간다. (B) rain brings water back down to the ground — ‘비(rain)’가 되어 내려온다. 눈(snow)은 지문에 없다."),
 item(5, "요약문 완성", SUMQ + "\n\nThe water cycle is very (A) ______ for life on Earth, so we must (B) ______ our water sources.",
      "(A) important …… (B) protect",
      ["(A) important …… (B) sell", "(A) dangerous …… (B) protect", "(A) dangerous …… (B) forget", "(A) small …… (B) use"], 4,
      "(A) The water cycle is necessary for life on Earth — 생명에 꼭 필요하므로 ‘중요하다(important)’. (B) protect our water sources — 물의 근원을 ‘보호해야(protect)’ 한다. 물의 순환이 위험하다거나 물의 근원을 팔거나 잊는다는 내용은 없다."),
]),
# ───────────────────────────── Unit 3 (Set C) ─────────────────────────────
dict(key="u3", set="C", title="Unit 3 · Social Studies",
passage="""In the 1980s, people who protested the increasing trend of fast food started a “slow food” movement. The movement aimed to preserve local foods, recipes, and communities, while (a) ______ fast, commercialized foods. This inspired the “slow city movement.”

The first Slow City was Chianti, Italy. The people there wanted to keep nature in good shape and protect historic buildings. They came up with a plan for developing their town just the way they wanted. They called this plan cittaslow. The term comes from the words “slow” and “citta,” which means “town” or “city” in Italian. The founders of this plan decided that new developments should keep people healthy and promote good relationships among neighbors. They also thought development should not (b) ______ the natural environment.

Since 1999, dozens of cities around the world have been named Slow Cities. They have a lot of green places where people can exercise and enjoy nature. Slow Cities do not have many fast-food restaurants or big supermarkets. Instead, they have locally owned restaurants and small markets. Try visiting a Slow City someday to see if you like it!""",
gloss="Words: protest = say no to something · trend = what many people do · preserve = keep · commercialized = made to make money · inspire = give an idea · historic = old and important · come up with = think of · term = a word · founder = a person who starts something · promote = help something grow · dozens of = many · exercise = move your body to stay healthy · locally owned = owned by people in the town",
items=[
 item(1, "세부 사실", "According to the passage, when did the slow food movement start?",
      "in the 1980s", ["in the 1950s", "in the 1960s", "in the 1970s", "in the 1990s"], 4,
      "In the 1980s, people who protested the increasing trend of fast food started a “slow food” movement."),
 item(1, "세부 사실", "According to the passage, what does “citta” mean in Italian?",
      "town or city", ["slow", "food", "nature", "plan"], 2,
      "“citta,” which means “town” or “city” in Italian."),
 item(2, "문장 빈칸 어휘", "Which word best fits in blank (a)?",
      "rejecting", ["buying", "cooking", "selling", "eating"], 5,
      "패스트푸드의 유행에 반대한(protested) 사람들이 시작한 운동이 지역 음식을 지키면서 패스트푸드를 ‘거부했다(rejecting)’는 흐름이다. 패스트푸드를 사거나 먹는다는 것은 운동의 취지와 반대이다."),
 item(2, "문장 빈칸 어휘", "Which word best fits in blank (b)?",
      "hurt", ["help", "make", "see", "build"], 1,
      "앞 문장에서 새 개발은 사람을 건강하게 하고 이웃 관계를 좋게 해야 한다고 했고, 2문단 첫머리에서 자연을 좋은 상태로 지키고 싶어 했다고 했다. 따라서 개발은 자연환경을 ‘해치지(hurt)’ 않아야 한다."),
 item(3, "문단 주제", "What is paragraph 2 mainly about?",
      "the first Slow City and its plan, cittaslow",
      ["the history of fast food", "the foods of Chianti", "famous buildings in Italy", "how to visit a Slow City"], 3,
      "2문단은 최초의 슬로시티 Chianti와 그곳 사람들이 세운 계획 cittaslow의 뜻과 원칙을 설명한다."),
 item(3, "제목", TITLE,
      "Slow Cities: Towns That Choose a Slow Life",
      ["How to Cook Slow Food", "The Best Restaurants in Italy", "Why Fast Food Is Popular", "The History of Chianti"], 5,
      "슬로푸드 운동에서 시작된 슬로시티 운동과 오늘날 슬로시티의 모습을 설명하는 글이다. 요리법, 식당 추천, 패스트푸드의 인기, Chianti의 역사는 글의 내용이 아니다."),
 item(4, "내용 일치", TRUE,
      "Slow Cities have many green places for people to enjoy nature.",
      ["Slow Cities have many big supermarkets.", "The slow city movement started before the slow food movement.", "People in Chianti wanted to build many new fast-food restaurants.", "Only ten cities have become Slow Cities."], 2,
      "They have a lot of green places where people can exercise and enjoy nature. 슬로시티에는 대형 마트가 많지 않고, 슬로푸드 운동이 먼저였으며(This inspired …), Chianti 사람들은 자연과 역사적 건물을 지키려 했고, 수십 개(dozens of) 도시가 지정되었다."),
 item(4, "내용 불일치", NOTTRUE,
      "New developments in Slow Cities should make people less healthy.",
      ["People in Chianti wanted to protect historic buildings.", "Cittaslow was a plan for developing the town.", "Slow Cities have locally owned restaurants.", "The slow food movement wanted to keep local foods and recipes."], 4,
      "new developments should keep people healthy — 새 개발은 사람을 ‘건강하게’ 해야 한다. 나머지는 protect historic buildings / a plan for developing their town / locally owned restaurants / preserve local foods, recipes 와 일치한다."),
 item(5, "글쓴이의 주장", AGREE,
      "Life in a town can be good without fast food and big supermarkets.",
      ["Every town should have more fast-food restaurants.", "Old buildings should be replaced by big supermarkets.", "Towns should grow as fast as possible.", "People should not visit Slow Cities."], 1,
      "글쓴이는 패스트푸드점과 대형 마트 대신 지역 식당과 작은 시장이 있는 슬로시티를 긍정적으로 소개하고 방문까지 권한다(Try visiting a Slow City someday). 나머지는 모두 글의 취지와 반대이다."),
 item(5, "추론", INFER,
      "The idea of Slow Cities spread to many countries.",
      ["Slow Cities are found only in Italy.", "The slow city movement started in the 1950s.", "Slow Cities do not allow any restaurants.", "Chianti is the only Slow City in the world."], 2,
      "Since 1999, dozens of cities around the world have been named Slow Cities — 슬로시티가 세계 여러 나라로 퍼졌음을 알 수 있다. 이탈리아에만 있거나 Chianti 하나뿐이라는 것은 이와 반대이고, 슬로시티에는 지역 식당이 있으며, 슬로시티 운동은 1980년대 슬로푸드 운동 뒤에 생겼다."),
]),
# ───────────────────────────── Unit 4 (Set D) ─────────────────────────────
dict(key="u4", set="D", title="Unit 4 · Science",
passage="""Before modern chemistry, ⟪ancient⟫ people tried to understand the makeup of the world. The ancient Greek philosopher Empedocles theorized that four elements made up every substance known to man. These elements were water, fire, earth, and air.

What observations did Empedocles make about these elements? First, he noted that pots were made with earth and water. After being mixed and shaped, they were burned with fire and cooled with air. All four elements were necessary to (a) ______. The same pot was used for cooking plants from the earth, often mixed with water, over a flame. The air cooled down the food so it could be eaten. Thus, all four elements were necessary to prepare a meal. Empedocles also believed that these elements were indestructible and unchangeable. His theories inspired later scientists to study more about the elements that make up our world.

Think about your life and all of your ⟪belongings⟫. How are the four elements involved in things you own, such as your computer, your clothes, and the food you eat? Thinking about everyday objects on a small scale can help us (b) ______.""",
gloss="Words: chemistry = the science of what things are made of · makeup = what something is made of · philosopher = a person who thinks about big questions · theorize / theory = an idea about how something works · element = a basic thing that makes up everything · substance = a thing, a material · observation = what you see · flame = fire · prepare = make ready · indestructible = cannot be broken · unchangeable = cannot be changed · involved in = a part of · on a small scale = by looking at small things",
items=[
 item(1, "세부 사실", "According to the passage, who was Empedocles?",
      "an ancient Greek philosopher", ["a Roman king", "a modern chemist", "a Chinese teacher", "an Egyptian farmer"], 1,
      "The ancient Greek philosopher Empedocles theorized that …"),
 item(1, "세부 사실", "According to the passage, what were pots made with?",
      "earth and water", ["fire and air", "wood and water", "earth and fire", "water and air"], 3,
      "he noted that pots were made with earth and water."),
 item(2, "어휘(단어 뜻)", "What does the underlined word ⟪ancient⟫ mean?",
      "very old", ["very new", "very big", "very small", "very rich"], 2,
      "ancient(고대의) = very old. ‘현대 화학 이전(Before modern chemistry)’의 옛날 사람들을 가리킨다."),
 item(2, "어휘(단어 뜻)", "What does the underlined word ⟪belongings⟫ mean?",
      "things that you own", ["places that you visit", "people that you know", "foods that you eat", "games that you play"], 5,
      "belongings(소지품) = things that you own. 바로 뒤에 things you own, such as your computer, your clothes 라고 풀어 말한다."),
 item(3, "도표 완성", TBLQ,
      "(A) fire …… (B) air",
      ["(A) air …… (B) fire", "(A) fire …… (B) water", "(A) water …… (B) air", "(A) earth …… (B) fire"], 4,
      "The same pot was used for cooking plants … over a flame — 불꽃(flame) 위에서 요리하므로 (A)는 fire. The air cooled down the food — 음식을 식힌 것은 (B) air.",
      table=[["*Element*", "*Cooking with the Pot*"],
             ["earth", "Plants come from it."],
             ["water", "The plants are mixed with it."],
             ["(A) ______", "The plants are cooked over it."],
             ["(B) ______", "It cools down the food."]]),
 item(3, "요약문 완성", SUMQ + "\n\nEmpedocles believed that everything was made of (A) ______ elements and that these elements could not be (B) ______.",
      "(A) four …… (B) broken",
      ["(A) two …… (B) broken", "(A) four …… (B) cooked", "(A) five …… (B) seen", "(A) two …… (B) seen"], 3,
      "(A) four elements made up every substance — 네(four) 원소. (B) these elements were indestructible and unchangeable — 부서지거나(broken) 변하지 않는다."),
 item(4, "문단 주제", "What is paragraph 2 mainly about?",
      "how Empedocles saw the four elements in making pots and meals",
      ["how to make a pot at home", "why fire is dangerous", "the history of Greek cooking", "how scientists study elements today"], 3,
      "2문단은 Empedocles가 그릇 만들기와 요리에서 네 원소를 모두 관찰했다는 내용이다. 그릇 만드는 법 자체나 불의 위험, 그리스 요리의 역사, 오늘날 과학자의 연구는 다루지 않는다."),
 item(4, "문단 주제", "What is the last paragraph mainly about?",
      "thinking about the four elements in the things we own",
      ["buying new computers and clothes", "cooking food over a flame", "the life of Empedocles", "how to become a philosopher"], 1,
      "마지막 문단은 우리 물건(컴퓨터, 옷, 음식)에 네 원소가 어떻게 들어 있는지 생각해 보라고 권하는 내용이다."),
 item(5, "빈칸 추론", "Which best fits in blank (a)?",
      "make one pot", ["paint a picture", "build a house", "start a fire", "grow plants"], 5,
      "빈칸 앞에서 그릇은 흙과 물로 만들어 불에 굽고 공기로 식힌다고 했으므로, 네 원소가 모두 필요한 것은 ‘그릇 하나를 만드는(make one pot)’ 일이다. 그림, 집, 불 피우기, 식물 기르기는 앞 내용과 이어지지 않는다."),
 item(5, "빈칸 추론", "Which best fits in blank (b)?",
      "understand the world around us", ["buy more things", "cook better food", "become a philosopher", "forget the four elements"], 4,
      "1문단에서 옛사람들이 ‘세상의 구성(makeup of the world)’을 이해하려 했다고 했고, 마지막 문단은 우리 물건 속 원소를 생각해 보라고 한다. 작은 것을 생각하는 일은 ‘우리 주변의 세상을 이해하는’ 데 도움이 된다는 결론이다."),
]),
# ───────────────────────────── Unit 5 (Set A) ─────────────────────────────
dict(key="u5", set="A", title="Unit 5 · Art",
passage="""How did the teddy bear get its name? It comes from U.S. president Theodore Roosevelt. During a hunting trip, Roosevelt refused to kill a bear that had been tied to a tree. All over America, people heard about this story. Some people even made stuffed bears and called ⟪them⟫ “teddy bears” in honor of the president’s ⟪nickname⟫, Teddy.

Teddy bears became mass-produced in the twentieth century. ⟪They⟫ were mainly toys for children, but they were also popularly featured in books and even in movies. Some well-known examples include Winnie the Pooh, which was originally written for adults, as well as Paddington Bear. Due to their popularity, teddy bears were manufactured in a wide range of sizes, colors, and materials. They have endured such lasting popularity that there are museums dedicated to teddy bears all around the world. England, Japan, and South Korea are just a few countries that have teddy bear museums.

Whether they are children’s toys, subjects of books, or objects on display at museums, teddy bears remain popular. They bring children ⟪comfort⟫ and are fun to play with. Teddy bears will probably be around for a long time to come.""",
gloss="Words: refuse = say no · stuffed bear = a toy bear · in honor of = to show respect for · mass-produced = made in large numbers · be featured in = appear in · manufacture = make · endure = last a long time · dedicated to = made for · subject = what a book is about",
items=[
 item(1, "어휘(단어 뜻)", "What does the underlined word ⟪nickname⟫ mean?",
      "a short, friendly name", ["a long, official name", "a family name", "the name of a place", "the name of a toy"], 5,
      "nickname(별명) = a short, friendly name. Theodore의 별명이 Teddy였다."),
 item(1, "어휘(단어 뜻)", "What does the underlined word ⟪comfort⟫ mean?",
      "a good, calm feeling", ["a loud noise", "a lot of money", "a bad dream", "a long trip"], 4,
      "comfort(위안, 편안함) = a good, calm feeling. 곰 인형이 아이들에게 ‘편안한 느낌’을 준다는 문맥이다."),
 item(2, "세부 사실", "According to the passage, what was the president’s nickname?",
      "Teddy", ["Theo", "Roosy", "Pooh", "Paddington"], 3,
      "in honor of the president’s nickname, Teddy. Pooh와 Paddington은 책에 나오는 곰의 이름이다."),
 item(2, "세부 사실", "According to the passage, which countries have teddy bear museums?",
      "England, Japan, and South Korea",
      ["England, France, and China", "Japan, China, and India", "the United States, Canada, and Mexico", "South Korea, Spain, and Italy"], 1,
      "England, Japan, and South Korea are just a few countries that have teddy bear museums."),
 item(3, "지칭 추론", "What does the underlined word ⟪them⟫ refer to?",
      "the stuffed bears that some people made",
      ["the people who heard the story", "the bears living in the forest", "the president and his friends", "the children who played with toys"], 2,
      "Some people even made stuffed bears and called them “teddy bears” — 사람들이 만든 ‘곰 인형들’을 teddy bears라고 불렀다."),
 item(3, "지칭 추론", "What does the underlined word ⟪They⟫ refer to?",
      "teddy bears", ["children", "books and movies", "museums", "Winnie the Pooh and Paddington Bear"], 4,
      "앞 문장의 주어 Teddy bears를 받아 ‘곰 인형들은 주로 아이들의 장난감이었다’고 말한다. Winnie the Pooh와 Paddington Bear는 그 뒤에 예로 나온다."),
 order_item(4, "(B) – (A) – (C)", 1,
      "Roosevelt가 나무에 묶인 곰을 죽이지 않음(B) → 미국 전역의 사람들이 그 이야기를 들음(A) → 사람들이 곰 인형을 만들어 teddy bear라고 부름(C). 1문단의 순서 그대로이다.",
      box="(A) People all over America heard about the story. \\\n(B) Roosevelt refused to kill a bear tied to a tree. \\\n(C) Some people made stuffed bears and called them “teddy bears.”"),
 item(4, "내용 불일치", NOTTRUE,
      "Teddy bears come in only one size and color.",
      ["Teddy bears were mainly toys for children.", "Winnie the Pooh was first written for adults.", "Teddy bears have been featured in books and movies.", "Teddy bears bring children comfort."], 5,
      "teddy bears were manufactured in a wide range of sizes, colors, and materials — 크기와 색깔이 다양하다. 나머지는 mainly toys for children / originally written for adults / featured in books and even in movies / They bring children comfort 와 일치한다."),
 item(5, "추론", INFER,
      "The story about Roosevelt and the bear made teddy bears popular.",
      ["Roosevelt sold teddy bears to make money.", "Teddy bears were first made in Japan.", "Children do not like teddy bears anymore.", "Teddy bears were named after a famous writer."], 2,
      "사람들이 그 이야기를 듣고 곰 인형을 만들어 대통령의 별명을 붙였고, 이후 대량 생산되었다. 따라서 그 이야기가 곰 인형의 인기를 만들었음을 알 수 있다. Roosevelt가 인형을 팔았다는 내용은 없고, 인형은 미국에서 시작되었으며, 오늘날에도 인기가 있고, 이름은 대통령에게서 왔다."),
 item(5, "추론", INFER,
      "People in many countries love teddy bears.",
      ["Teddy bears are made in only one country.", "Only American children play with teddy bears.", "Teddy bears are not sold anymore.", "Teddy bear museums are found only in England."], 3,
      "museums dedicated to teddy bears all around the world. England, Japan, and South Korea … — 세계 여러 나라에 곰 인형 박물관이 있으므로 여러 나라 사람들이 곰 인형을 사랑함을 알 수 있다. 나머지는 이와 반대이거나 글에 근거가 없다."),
]),
# ───────────────────────────── Unit 6 (Set B) ─────────────────────────────
dict(key="u6", set="B", title="Unit 6 · Nature",
passage="""Molecules are always moving. Sometimes, molecules even move through membranes. Molecules tend to pass through semi-permeable membranes to an area where the solvent concentration is higher. This equalizes the concentration of materials on either side of the membrane. This process is called osmosis. Osmosis is an important chemical process with ⟪practical⟫ uses in everyday life. What is one use of osmosis?

Fresh vegetables have a high concentration of water molecules. During pickling, vegetables are placed in a brine—a mixture of water, salt, and seasonings. The skin acts as a semi-permeable membrane. Water molecules move out of the vegetables through the skin and into the brine, which equalizes the solvent concentration on either side of the membrane. This process is an example of osmosis, and it is why pickled vegetables stay crunchy.

Reverse osmosis is a process that uses pressure to ⟪force⟫ molecules into an area of lower solute concentration. We use reverse osmosis to remove salt and other particles from seawater. Afterward, we can drink the water!

Chemical processes like osmosis have a big effect on our everyday lives. For this reason, learning about how they work is important for our understanding of the world.""",
gloss="Words: molecule = a very small part of a thing · tend to = usually · membrane = a thin skin · semi-permeable membrane = a skin that lets only some things pass · solvent = the liquid (here, water) · solute = the thing in the liquid (here, salt) · concentration = how much of something is in a liquid · equalize = make equal · on either side of = on both sides of · pickling = making pickles · seasonings = things you add to food for taste · crunchy = hard, not soft · pressure = a strong push · remove = take out · particle = a very small piece · effect = a change that something makes",
items=[
 item(1, "문맥상 동의어", "Which can best replace the underlined word ⟪force⟫?",
      "push", ["pull", "stop", "cool", "count"], 1,
      "force = push(밀어 넣다, 억지로 ~하게 하다). 압력으로 분자를 ‘밀어 넣는다’는 뜻이다."),
 item(1, "문맥상 동의어", "Which can best replace the underlined word ⟪practical⟫?",
      "useful", ["strange", "dangerous", "expensive", "slow"], 2,
      "practical = useful(실용적인, 쓸모 있는). 삼투가 일상생활에서 ‘쓸모 있게’ 쓰인다는 뜻이다."),
 item(2, "세부 사실", "According to the passage, what acts as a semi-permeable membrane during pickling?",
      "the skin of the vegetables", ["the salt", "the brine", "the water", "the seasonings"], 5,
      "The skin acts as a semi-permeable membrane."),
 item(2, "세부 사실", "According to the passage, what do we use reverse osmosis for?",
      "to take salt out of seawater", ["to make pickles", "to grow vegetables", "to cool down food", "to warm up seawater"], 4,
      "We use reverse osmosis to remove salt and other particles from seawater."),
 item(3, "언급 이유", "Why does the writer say that pickled vegetables stay crunchy?",
      "to show a result of osmosis in pickling",
      ["to explain how to make vegetables soft", "to show that salt makes food taste good", "to explain why vegetables are healthy", "to show that brine is dangerous"], 3,
      "This process is an example of osmosis, and it is why pickled vegetables stay crunchy — 피클이 아삭함을 유지하는 것은 삼투(물이 채소 밖으로 나감)의 결과임을 보여 주기 위해서이다."),
 item(3, "언급 이유", "Why does the writer mention seawater?",
      "to give an example of how reverse osmosis is used",
      ["to explain how fish live in salty water", "to show how pickles are made", "to explain where salt comes from", "to show that molecules stop moving in the sea"], 3,
      "We use reverse osmosis to remove salt … from seawater. Afterward, we can drink the water! — 역삼투가 쓰이는 예로 바닷물을 든 것이다."),
 item(4, "내용 불일치", NOTTRUE,
      "Reverse osmosis makes seawater saltier.",
      ["Molecules sometimes move through membranes.", "Osmosis has uses in everyday life.", "Pickles are made in a brine.", "Learning about chemical processes helps us understand the world."], 4,
      "reverse osmosis to remove salt … from seawater — 역삼투는 소금을 ‘없앤다’. 나머지는 molecules even move through membranes / practical uses in everyday life / placed in a brine / important for our understanding of the world 와 일치한다."),
 item(4, "내용 일치", TRUE,
      "Chemical processes have a big effect on our everyday lives.",
      ["Molecules never move through membranes.", "Pickled vegetables lose their crunch in the brine.", "Reverse osmosis is used to make pickles.", "Osmosis is not used in everyday life."], 2,
      "Chemical processes like osmosis have a big effect on our everyday lives. 분자는 막을 통과하기도 하고, 피클은 아삭함을 유지하며, 피클은 삼투(역삼투가 아님)의 예이고, 삼투는 일상에서 쓰인다."),
 item(5, "요약문 완성", SUMQ + "\n\nDuring pickling, (A) ______ moves out of the vegetables and into the (B) ______.",
      "(A) water …… (B) brine",
      ["(A) salt …… (B) brine", "(A) water …… (B) skin", "(A) salt …… (B) skin", "(A) air …… (B) brine"], 1,
      "Water molecules move out of the vegetables through the skin and into the brine — 채소 밖으로 나가는 것은 ‘물(water)’이고, 도착하는 곳은 ‘소금물(brine)’이다. 껍질(skin)은 물이 지나가는 막이다."),
 item(5, "요약문 완성", SUMQ + "\n\nReverse osmosis uses (A) ______ to push molecules the other way, and after that we can (B) ______ the seawater.",
      "(A) pressure …… (B) drink",
      ["(A) heat …… (B) drink", "(A) pressure …… (B) sell", "(A) salt …… (B) drink", "(A) heat …… (B) cook"], 5,
      "(A) Reverse osmosis is a process that uses pressure to force molecules … — ‘압력(pressure)’을 이용한다. (B) Afterward, we can drink the water! — 그 뒤에 물을 ‘마실(drink)’ 수 있다. 열(heat)은 지문에 없고, 소금은 없애는 대상이다."),
]),
# ───────────────────────────── Unit 7 (Set C) ─────────────────────────────
dict(key="u7", set="C", title="Unit 7 · Social Studies",
passage="""People usually make tough decisions by voting for one of two or more options. The option that gets the most votes is the (a) ______. This is called majority rule. However, even if only 51% of people in a group vote for an option, they will get their choice. That means, almost half of the people in that group will not get their choice. In that case, is majority rule really fair?

Most democracies (b) ______ public officials through a majority vote. In a system with two political parties, a slim margin, such as 51% to 49%, can decide an election. In a system with more than two parties, less than 50% of voters could give one political party a victory. To ensure the fairness of majority rule, certain conditions must be met. First, people should be able to vote with secret ballots. Second, each person’s vote should be weighted equally. Finally, there have to be enough voters to make a majority vote truly fair.

When an election is won with less than 50% of the total votes, the winning party must consider the opinions of the other voters. This is because running a democracy should ensure equality for all citizens.""",
gloss="Words: tough decision = a hard choice · vote = choose by marking a paper · option = a choice · majority = more than half · democracy = a country where people vote for their leaders · public official = a person who works for the government · political party = a group of people who try to win elections · slim margin = a very small difference · victory = a win · ensure = make sure · fairness = being fair · condition = something that must be true · be met = be followed · secret ballot = voting where no one sees your choice · be weighted equally = count the same · consider = think about · opinion = what a person thinks · citizen = a person of a country · equality = everyone being treated the same",
items=[
 item(1, "세부 사실", "According to the passage, how do people usually make tough decisions?",
      "by voting", ["by fighting", "by guessing", "by asking a teacher", "by flipping a coin"], 2,
      "People usually make tough decisions by voting for one of two or more options."),
 item(1, "세부 사실", "According to the passage, what can decide an election in a two-party system?",
      "a slim margin, such as 51% to 49%",
      ["only a margin of 90% to 10%", "the age of the voters", "the number of parties", "the weather on election day"], 3,
      "In a system with two political parties, a slim margin, such as 51% to 49%, can decide an election."),
 item(2, "문장 빈칸 어휘", "Which word best fits in blank (a)?",
      "winner", ["loser", "voter", "party", "question"], 1,
      "가장 많은 표를 얻은 선택지가 ‘승자(winner)’이고, 이것을 다수결이라 부른다. 바로 뒤에서 51%만 얻어도 ‘원하는 것을 얻는다(get their choice)’고 했다."),
 item(2, "문장 빈칸 어휘", "Which word best fits in blank (b)?",
      "elect", ["forget", "pay", "teach", "follow"], 5,
      "민주주의 국가는 다수결 투표로 공직자를 ‘뽑는다(elect)’. 뒤 문장들이 모두 선거(election)와 표(votes) 이야기이다."),
 item(3, "문단 주제", "What is paragraph 1 mainly about?",
      "what majority rule is and a problem with it",
      ["how public officials are elected", "the three conditions for a fair vote", "why secret ballots are important", "how many parties a democracy needs"], 4,
      "1문단은 다수결의 뜻(가장 많은 표를 얻은 쪽이 이김)과 그 문제(거의 절반이 원하는 것을 얻지 못함)를 말한다. 공직자 선출과 세 가지 조건은 2문단의 내용이다."),
 item(3, "제목", TITLE,
      "Is Majority Rule Always Fair?",
      ["How to Win an Election", "The History of Democracy", "Why People Hate Voting", "The Life of a Public Official"], 1,
      "글 전체가 ‘다수결이 정말 공정한가(is majority rule really fair?)’를 묻고, 공정한 다수결의 조건을 설명한다. 선거에서 이기는 법, 민주주의의 역사, 투표를 싫어하는 이유, 공직자의 삶은 글의 내용이 아니다."),
 item(4, "내용 일치", TRUE,
      "Almost half of a group may not get their choice under majority rule.",
      ["Every voter gets their choice under majority rule.", "A party needs 100% of the votes to win.", "Secret ballots are not allowed in democracies.", "In a democracy, only leaders can vote."], 5,
      "almost half of the people in that group will not get their choice. 51%만 얻어도 이기므로 모두가 원하는 것을 얻는 것도, 100%가 필요한 것도 아니며, 비밀 투표는 공정한 다수결의 조건이고, 사람들이 투표로 공직자를 뽑는다."),
 item(4, "내용 불일치", NOTTRUE,
      "A majority vote is fair even when very few people vote.",
      ["Each person’s vote should be weighted equally.", "Most democracies choose public officials by a majority vote.", "Running a democracy should ensure equality for all citizens.", "Secret ballots are one condition for a fair majority vote."], 3,
      "there have to be enough voters to make a majority vote truly fair — 투표하는 사람이 ‘충분히 많아야’ 공정하다. 나머지는 weighted equally / through a majority vote / ensure equality for all citizens / vote with secret ballots 와 일치한다."),
 item(5, "글쓴이의 주장", AGREE,
      "A democracy should care about the people who lost the vote, too.",
      ["The losing side in a vote does not matter.", "A vote with two voters is as fair as a vote with a thousand.", "Leaders should know how each person voted.", "A party with 51% should ignore the other 49%."], 4,
      "the winning party must consider the opinions of the other voters … ensure equality for all citizens — 글쓴이는 이긴 쪽이 진 쪽의 의견도 고려해야 한다고 본다. 진 쪽이 중요하지 않다거나 49%를 무시해도 된다는 것은 반대이고, 투표자 수는 충분해야 하며, 비밀 투표가 조건이므로 지도자가 누가 누구를 뽑았는지 알아서는 안 된다."),
 item(5, "추론", INFER,
      "Majority rule can give the victory to a party that most voters did not choose.",
      ["Majority rule is used only in countries with two parties.", "Elections are always decided by more than 90% of the votes.", "Public officials are chosen by the president.", "Secret ballots make elections unfair."], 2,
      "In a system with more than two parties, less than 50% of voters could give one political party a victory — 유권자의 절반도 안 되는 표로 이길 수 있으므로, 대부분의 유권자가 뽑지 않은 정당이 이길 수도 있다. 다수결은 정당이 셋 이상인 체제에서도 쓰이고, 51% 대 49%로도 결정되며, 공직자는 투표로 뽑고, 비밀 투표는 공정성의 조건이다."),
]),
# ───────────────────────────── Unit 8 (Set D) ─────────────────────────────
dict(key="u8", set="D", title="Unit 8 · Science",
passage="""Throughout history, humans have looked at the stars as a map, as a guide, and for worship. The invention of the telescope has helped humans (a) ______. How have telescopes changed over time?

Telescopes were ⟪originally⟫ used to see long distances. Galileo was one of the first to use a telescope to observe the stars. His telescope used a concave eyepiece and a convex lens. This gave the image seen through the telescope an upright view and magnified it up to thirty times! Even though Galileo’s telescope was quite useful at the time, the images it produced were blurry. Kepler ⟪improved⟫ on Galileo’s design by using a convex eyepiece and lens. This gave a much wider field of view, even though the images appeared upside-down.

In modern times, telescopes have been launched into space to help astronomers observe (b) ______. One example is the Hubble Telescope, which orbits Earth and sends back high-quality pictures of distant planets and galaxies. Through continued technological developments, humans can understand the universe much better.""",
gloss="Words: worship = praying to a god · invention = making something new for the first time · observe = watch carefully · astronomer = a person who studies the stars · concave = curved in · convex = curved out · eyepiece = the part you look into · upright = with the top at the top (not upside-down) · magnify = make bigger · blurry = not clear · field of view = how much you can see · upside-down = the top at the bottom · launch = send into space · orbit = go around · distant = far away · galaxy = a very large group of stars · continued = going on · technological development = new technology",
items=[
 item(1, "세부 사실", "According to the passage, who was one of the first to use a telescope to observe the stars?",
      "Galileo", ["Kepler", "Hubble", "Newton", "Einstein"], 4,
      "Galileo was one of the first to use a telescope to observe the stars. Kepler는 그 설계를 개선한 사람이고, Hubble은 우주 망원경의 이름이다."),
 item(1, "세부 사실", "According to the passage, what does the Hubble Telescope send back?",
      "pictures of distant planets and galaxies", ["rocks from the Moon", "maps of the oceans", "weather reports", "radio songs"], 5,
      "the Hubble Telescope, which orbits Earth and sends back high-quality pictures of distant planets and galaxies."),
 item(2, "어휘(단어 뜻)", "What does the underlined word ⟪originally⟫ mean?",
      "at first", ["at last", "never", "always", "later"], 2,
      "originally(원래, 처음에는) = at first. 망원경은 ‘처음에는’ 먼 거리를 보는 데 쓰였다는 뜻이다."),
 item(2, "어휘(단어 뜻)", "What does the underlined word ⟪improved⟫ mean?",
      "made better", ["broke", "copied", "sold", "forgot"], 3,
      "improve(개선하다) = make better. Kepler가 Galileo의 설계를 ‘더 좋게 만들었다’는 뜻으로, 뒤에 시야가 훨씬 넓어졌다는 설명이 이어진다."),
 item(3, "도표 완성", TBLQ,
      "(A) map …… (B) long distances",
      ["(A) map …… (B) small animals", "(A) friend …… (B) long distances", "(A) friend …… (B) the bottom of the sea", "(A) toy …… (B) small animals"], 1,
      "(A) humans have looked at the stars as a map, as a guide, and for worship — 별을 ‘지도(map)’로 삼았다. (B) Telescopes were originally used to see long distances — 망원경은 ‘먼 거리(long distances)’를 보는 데 쓰였다.",
      table=[["", "*What people did*"],
             ["Long ago", "They looked at the stars as a (A) ______, as a guide, and for worship."],
             ["With telescopes", "They could see (B) ______."]]),
 item(3, "요약문 완성", SUMQ + "\n\nGalileo’s telescope made the image (A) ______ and much bigger, but the image was (B) ______.",
      "(A) upright …… (B) blurry",
      ["(A) upside-down …… (B) blurry", "(A) upright …… (B) clear", "(A) upside-down …… (B) clear", "(A) small …… (B) dark"], 5,
      "(A) This gave the image … an upright view and magnified it up to thirty times — 이미지는 ‘똑바로(upright)’ 보였고 크게 확대되었다. (B) the images it produced were blurry — 하지만 ‘흐릿했다(blurry)’. 거꾸로 보인 것은 Kepler의 망원경이다."),
 item(4, "문단 주제", "What is paragraph 2 mainly about?",
      "how Galileo’s and Kepler’s telescopes were different",
      ["how to build a telescope", "why the stars are far away", "the life of Galileo", "how the Hubble Telescope works"], 2,
      "2문단은 Galileo 망원경(똑바로 선 상, 30배 확대, 흐릿함)과 Kepler 망원경(넓은 시야, 거꾸로 된 상)의 차이를 설명한다."),
 item(4, "문단 주제", "What is paragraph 3 mainly about?",
      "telescopes in space, like the Hubble Telescope",
      ["the first telescope in history", "how people used stars as maps", "Kepler’s new design", "why images look blurry"], 4,
      "3문단은 우주로 발사된 현대 망원경, 특히 Hubble 망원경이 하는 일을 설명한다. 첫 망원경, 별을 지도로 쓴 일, Kepler의 설계, 흐릿한 상은 1·2문단의 내용이다."),
 item(5, "빈칸 추론", "Which best fits in blank (a)?",
      "see and understand the stars better", ["travel to the stars", "make maps of Earth", "build taller buildings", "live longer"], 3,
      "사람들이 오랫동안 별을 바라봤고, 뒤 문단에서 망원경으로 별을 ‘관측하고(observe)’ 우주를 ‘더 잘 이해하게(understand the universe much better)’ 되었다고 했다. 따라서 망원경의 발명은 별을 ‘더 잘 보고 이해하도록’ 도운 것이다. 별로 여행하거나 지도를 만들거나 건물을 짓거나 오래 사는 이야기는 없다."),
 item(5, "빈칸 추론", "Which best fits in blank (b)?",
      "not just the stars but the whole universe", ["only the Moon", "the bottom of the ocean", "the weather on Earth", "birds in the sky"], 1,
      "바로 뒤 문장에서 Hubble 망원경이 먼 행성과 은하의 사진을 보내온다고 했으므로, 우주 망원경은 별뿐 아니라 ‘우주 전체’를 관측하도록 돕는다. 달만, 바다 밑, 지구의 날씨, 새는 글의 내용과 맞지 않는다."),
]),
]

PAIR = {"A": "1·5 (Art)", "B": "2·6 (Nature)", "C": "3·7 (Social Studies)", "D": "4·8 (Science)"}


def build():
    sections, blueprint = [], []
    for u in UNITS:
        passage = {"type": "passage", "title": "[1–10] Read the passage and answer the questions.", "text": u["passage"]}
        if GLOSS and u.get("gloss"):
            passage["note"] = u["gloss"]
        items = [passage]
        assert [it["_lv"] for it in u["items"]] == LEVELS, u["key"]
        for i, it in enumerate(u["items"], 1):
            blueprint.append((u["key"].upper(), i, u["set"], it["_lv"], it["_kind"], it["answer"]))
            items.append({k: v for k, v in it.items() if not k.startswith("_")})
        sections.append({"title": u["title"], "items": items})
    kinds = {u["key"]: [it["_kind"] for it in u["items"]] for u in UNITS}
    for a, b in (("u1", "u5"), ("u2", "u6"), ("u3", "u7"), ("u4", "u8")):
        assert kinds[a] == kinds[b], (a, kinds[a], b, kinds[b])
    dist = Counter(b[5] for b in blueprint)
    assert len(blueprint) == 80 and set(dist.values()) == {16}, dist
    doc = {
        "title": "The Reading 7-1 Practice Questions",
        "meta": {"subject": "English Reading", "grade": "Level 7", "unit": "Units 1–8"},
        "student_fields": ["Class", "Name"],
        "instructions": ["10 questions for each unit · 5 choices · Choose one answer for each question."],
        "layout": {"columns": 1, "font_size": 9.5, "show_points": False, "choice_columns": 0,
                   "section_pagebreak": True, "number_per_section": True},
        "sections": sections,
    }
    return doc, blueprint, kinds


def blueprint_md(blueprint, kinds):
    lines = ["# The Reading 7-1 Practice Questions · 문항 구성표", "",
             "단원별 연습문항 10개 × 8단원 = 80문항 · 5지선다 · 초6 · 학생용은 전부 영어, 해설은 한국어", "",
             "Final Test와 같은 유형군을 쓰고, 단원마다 난이도 1→5를 두 번 밟는다 (1,1,2,2,3,3,4,4,5,5). 지문은 교재 원문 전체.", "",
             "## 유형 설계 (단원 쌍끼리 동일)", "", "| 쌍 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for s, (a, _) in zip("ABCD", (("u1", "u5"), ("u2", "u6"), ("u3", "u7"), ("u4", "u8"))):
        lines.append(f"| {PAIR[s]} | " + " | ".join(kinds[a]) + " |")
    lines += ["", "## 난이도와 목표 정답률", "", "| 난이도 | 설명 | 예상 정답률(초6 평균) | 문항 |", "|---|---|---|---|"]
    for lv in range(1, 6):
        qs = ", ".join(str(i) for i, l in enumerate(LEVELS, 1) if l == lv)
        lines.append(f"| {lv} | {LEVEL[lv]} | {int(EXPECTED_P[lv]*100)}% | {qs}번 |")
    lines += ["", "## 문항별 정보", "", "| 단원 | 번호 | 쌍 | 난이도 | 유형 | 정답 |", "|---|---|---|---|---|---|"]
    for unit, q, s, lv, kind, ans in blueprint:
        lines.append(f"| {unit} | {q} | {s} | {lv} | {kind} | {ans} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "TheReading_7-1_Practice.json")
    doc, blueprint, kinds = build()
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    out.with_name("TheReading_7-1_Practice_문항구성표.md").write_text(blueprint_md(blueprint, kinds), encoding="utf-8")
    print(out, dict(sorted(Counter(b[5] for b in blueprint).items())))
