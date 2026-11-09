"""The Reading 7-1 Final Test — 문항 원본 데이터 → exam-worksheet JSON + 문항구성표.

대상: The Reading Level 7을 배운 초등학교 6학년 (평균 학생의 70%가 70점 이상 합격하도록 설계)
학생용 시험지는 전부 영어(발문·선택지·단어 풀이·안내문). 정답·해설지의 해설만 한국어(교사용).

유형 설계: 단원 쌍(1·5, 2·6, 3·7, 4·8)끼리 같은 5개 유형을 쓰고,
각 단원 안에서 1번→5번으로 갈수록 어려워진다.

  Set A (1·5 Art)      : 어휘(단어 뜻) → 세부 사실 → 지칭 추론 → 사건 순서 배열 → 추론
  Set B (2·6 Nature)   : 문맥상 동의어 → 세부 사실 → 언급 이유 → 내용 불일치 → 요약문 (A)(B)
  Set C (3·7 Social)   : 세부 사실 → 문장 빈칸 어휘 → 주제 → 내용 일치 → 글쓴이의 주장
  Set D (4·8 Science)  : 세부 사실 → 어휘(단어 뜻) → 도표 완성 (A)(B) → 제목 → 빈칸 추론

초6 눈높이 장치 (영어판):
  - 발문과 선택지는 짧고 쉬운 영어로 쓴다. 선택지는 한 문항 안에서 형태를 맞춘다.
  - 어휘 문항은 밑줄 친 단어의 뜻을 쉬운 영어로 고른다.
  - 사건 순서 배열은 사건 3개만 쓴다.
  - 지문 아래에 시험에 나오지 않는 어려운 단어의 뜻을 쉬운 영어로 달아 준다 (GLOSS = False 로 끌 수 있음).

표기: 지문·발문 속 ⟪단어⟫ 는 밑줄, ______ 는 빈칸 상자로 조판된다.
"""
import json
import sys
from collections import Counter
from pathlib import Path

GLOSS = True
LEVEL = {1: "매우 쉬움", 2: "쉬움", 3: "보통", 4: "다소 어려움", 5: "어려움"}
EXPECTED_P = {1: 0.97, 2: 0.92, 3: 0.85, 4: 0.77, 5: 0.65}  # 초6 평균 학생 기준 예상 정답률

SUMQ = "Complete the summary of the passage. Which words best fit (A) and (B)?"
ORDQ = "Which is the correct order of (A), (B), and (C), from first to last?"
TBLQ = "Complete the table about the passage. Which words best fit (A) and (B)?"
NOTTRUE = "Which is *NOT* true according to the passage?"
TRUE = "Which is true according to the passage?"
MAIN = "What is the passage mainly about?"
TITLE = "What is the best title for the passage?"
AGREE = "Which idea would the writer most likely agree with?"
INFER = "What can we learn from the passage?"
BLANK = "Which best fits in the blank?"
ORD3 = ["(A) – (B) – (C)", "(A) – (C) – (B)", "(B) – (A) – (C)", "(B) – (C) – (A)", "(C) – (A) – (B)", "(C) – (B) – (A)"]


def item(lv, kind, prompt, answer, wrong, pos, expl, **extra):
    assert len(wrong) == 4 and answer not in wrong and 1 <= pos <= 5
    choices = list(wrong)
    choices.insert(pos - 1, answer)
    d = {"type": "multiple_choice", "prompt": prompt, "choices": choices, "answer": pos,
         "points": 2.5, "explanation": f"[난이도 {lv}·{LEVEL[lv]} / {kind}] {expl}"}
    d.update(extra)
    d["_lv"], d["_kind"] = lv, kind
    return d


def order_item(lv, prompt, key, pos, expl, box):
    """사건 3개 순서 배열: key 를 pos 에 두고 나머지 4개는 다른 배열에서 고른다."""
    wrong = [o for o in ORD3 if o != key][:4]
    return item(lv, "사건 순서 배열", prompt, key, wrong, pos, expl, box=box)


UNITS = [
# ───────────────────────────── Unit 1 (Set A) ─────────────────────────────
dict(key="u1", set="A", title="Unit 1 · Art — Andy Warhol and Pop Art",
passage="""Art in advertisements has become increasingly ⟪popular⟫. This is called commercial art. One of the most famous commercial artists was Andy Warhol.

Andy Warhol was often sick as a child, so he spent a lot of time drawing. After college, he began his career making art for advertisements. His drawings of shoes became so well known that people wanted to see more of his work. Thus, in the 1950s, he began showing his popular works in art galleries. Warhol was one of the first artists to use silkscreen ink printing in his work. During the 1960s, he produced many famous art pieces depicting everyday objects. ⟪These⟫ include Coca-Cola bottles, dollar bills, and Campbell’s Soup cans. This kind of art is referred to as “pop art.”

Some critics think Andy Warhol was only interested in making money with his art. Others thought he was the perfect example of commercialized modern life. Apart from this argument, most critics agree that Warhol’s work shows the changing value of art in everyday life.""",
gloss="Words: increasingly = more and more · advertisement = a picture or words that tell people to buy something · silkscreen ink printing = a way of printing pictures · depict = show, draw · critic = a person who gives opinions about art",
items=[
 item(1, "어휘(단어 뜻)", "What does the underlined word ⟪popular⟫ mean?",
      "liked by many people", ["sold for a lot of money", "made a long time ago", "used by only a few people", "known by nobody"], 3,
      "popular(인기 있는) = liked by many people. 광고 속 미술이 점점 인기를 얻고 있다는 뜻이고, 2문단의 his popular works에서도 같은 뜻으로 쓰였다."),
 item(2, "세부 사실", "According to the passage, why did Andy Warhol draw a lot as a child?",
      "He was often sick.", ["His parents were artists.", "He went to an art school.", "He wanted to sell his drawings.", "His friends liked his drawings."], 2,
      "Andy Warhol was often sick as a child, so he spent a lot of time drawing. — 어릴 때 자주 아파서 그림을 많이 그렸다. 나머지는 본문에 없는 내용이다."),
 item(3, "지칭 추론", "What does the underlined word ⟪These⟫ refer to?",
      "Warhol’s art pieces of everyday objects", ["the advertisements Warhol made", "the art galleries that showed his works", "Warhol’s drawings of shoes", "the critics who wrote about Warhol"], 3,
      "바로 앞 문장의 many famous art pieces depicting everyday objects(일상 사물을 그린 유명한 작품들)를 가리킨다. 그 예로 콜라병, 지폐, 수프 캔이 이어진다."),
 order_item(4, ORDQ, "(B) – (A) – (C)", 5,
      "대학 졸업 후 일을 시작(B, After college, he began his career) → 1950년대에 미술관에서 작품 전시(A) → 1960년대에 ‘팝 아트’라 불리는 작품 제작(C). 2문단에 나온 순서 그대로이다.",
      box="(A) Warhol began showing his works in art galleries. \\\n(B) Warhol started his first job after college. \\\n(C) Warhol made the works called “pop art.”"),
 item(5, "추론", INFER,
      "Warhol’s art for advertisements made him a famous artist.",
      ["Warhol stopped making art after he became famous.", "Everyone had the same opinion about Warhol’s art.", "Warhol invented silkscreen ink printing.", "Art in advertisements is called “pop art.”"], 4,
      "광고용으로 그린 신발 그림이 유명해져 사람들이 그의 작품을 더 보고 싶어 했고, ‘그래서(Thus)’ 미술관에서 전시를 시작했다고 했다. 유명해진 뒤 그만두었다는 내용은 없고(1960년대에도 많은 작품을 만듦), 사람들의 의견은 갈렸으며(Some critics … Others …), 실크스크린은 ‘처음 사용한 화가 중 한 명(one of the first)’일 뿐이고, 광고 속 미술은 ‘상업 미술(commercial art)’이라고 불린다(팝 아트는 일상 사물을 그린 작품을 가리킨다)."),
]),
# ───────────────────────────── Unit 2 (Set B) ─────────────────────────────
dict(key="u2", set="B", title="Unit 2 · Nature — The Water Cycle Keeps Earth Balanced",
passage="""The water cycle is necessary for life on Earth. Water on the ground evaporates into vapor and forms clouds in the sky. In return, rain brings water back down to the ground again, which ends up in streams, rivers, lakes, and oceans. What happens when humans tamper with the water cycle?

Most evaporation occurs in oceans as a result of the Sun’s energy. This cools the temperature of Earth’s climate and also affects the oceans’ salt content. Having the correct amount of salt in the oceans ⟪maintains⟫ a delicate ecosystem of plants, fish, and other wildlife. One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. The two rivers that fed the Aral Sea were diverted for farming in the desert. As a result, the sea is now almost completely dry, killing the wildlife that lived there and causing dust storms that affect human health.

As we can see, the water cycle is necessary to keep the environment balanced.""",
gloss="Words: evaporate = change into gas · vapor = water in the air · tamper with = change something in a bad way · affect = change something · salt content = the amount of salt · ecosystem = all the living things in a place · disaster = a very bad event · fed = brought water to · divert = make a river go a different way · dust storm = a strong wind full of dust",
items=[
 item(1, "문맥상 동의어", "Which can best replace the underlined word ⟪maintains⟫?",
      "keeps", ["breaks", "loses", "changes", "hurts"], 2,
      "maintain은 ‘(상태를) 유지하다’. 알맞은 양의 소금이 생태계를 ‘지켜 준다, 유지한다’는 뜻이므로 keeps가 가장 가깝다."),
 item(2, "세부 사실", "According to the passage, why did people divert the two rivers that went into the Aral Sea?",
      "to farm in the desert", ["to build a new city", "to make electricity", "to stop dust storms", "to protect wild animals"], 4,
      "The two rivers that fed the Aral Sea were diverted for farming in the desert. 모래 폭풍과 야생동물은 물길을 바꾼 ‘결과’로 나올 뿐 목적이 아니다."),
 item(3, "언급 이유", "Why does the writer talk about the Aral Sea?",
      "to show what can happen when people change the water cycle",
      ["to teach how to keep people healthy", "to explain why the salt in the oceans changes", "to tell where the biggest lake in the world is", "to explain how rain is made in the clouds"], 2,
      "One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. — 사람이 물의 순환을 바꾸면 어떤 일이 생기는지 보여 주는 ‘예(example)’로 든 것이다. 건강을 지키는 방법, 소금 함량이 달라지는 까닭, 호수의 위치, 비가 만들어지는 과정은 Aral Sea 이야기와 관계가 없다."),
 item(4, "내용 불일치", NOTTRUE,
      "Most evaporation happens in rivers and lakes.",
      ["Rain brings water back down to the ground.", "Evaporation affects the salt in the oceans.", "The Aral Sea is now almost completely dry.", "Dust storms from the Aral Sea affect people’s health."], 3,
      "Most evaporation occurs in oceans — 증발은 대부분 ‘바다’에서 일어난다. 나머지는 rain brings water back down to the ground / affects the oceans’ salt content / almost completely dry / dust storms that affect human health 와 일치한다."),
 item(5, "요약문 완성", SUMQ + "\n\nThe Sun’s energy makes water evaporate, and this makes Earth’s climate (A) ______. The water cycle keeps the environment (B) ______.",
      "(A) cooler …… (B) balanced",
      ["(A) warmer …… (B) balanced", "(A) cooler …… (B) dirty", "(A) warmer …… (B) dry", "(A) drier …… (B) balanced"], 5,
      "(A) This cools the temperature of Earth’s climate — 증발이 기후를 ‘식히므로’ 기후는 더 ‘시원해진다(cooler)’. 지문의 cools를 cooler로 바꿔 읽어야 한다. (B) 마지막 문장 the water cycle is necessary to keep the environment balanced — 물의 순환은 환경을 ‘균형 잡힌(balanced)’ 상태로 지켜 준다. 기후가 더워지거나 건조해진다는 내용, 환경이 더러워지거나 말라 버린다는 내용은 없다."),
]),
# ───────────────────────────── Unit 3 (Set C) ─────────────────────────────
dict(key="u3", set="C", title="Unit 3 · Social Studies — The Slow City Movement",
passage="""In the 1980s, people who protested the increasing trend of fast food started a “slow food” movement. The movement aimed to preserve local foods, recipes, and communities, while rejecting fast, commercialized foods. This inspired the “slow city movement.”

The first Slow City was Chianti, Italy. The people there wanted to keep nature in good shape and ______ historic buildings. They came up with a plan for developing their town just the way they wanted. They called this plan cittaslow. The founders of this plan decided that new developments should keep people healthy and promote good relationships among neighbors. They also thought development should not hurt the natural environment.

Since 1999, dozens of cities around the world have been named Slow Cities. Slow Cities do not have many fast-food restaurants or big supermarkets. Instead, they have locally owned restaurants and small markets. Try visiting a Slow City someday to see if you like it!""",
gloss="Words: protest = say no to something · trend = what many people do · preserve = keep · reject = say no to · commercialized = made to make money · inspire = give an idea · historic = old and important · come up with = think of · founder = a person who starts something · promote = help something grow · dozens of = many · locally owned = owned by people in the town",
items=[
 item(1, "세부 사실", "According to the passage, where was the first Slow City?",
      "Chianti, Italy", ["Rome, Italy", "Paris, France", "Seoul, Korea", "Madrid, Spain"], 2,
      "The first Slow City was Chianti, Italy."),
 item(2, "문장 빈칸 어휘", "Which word best fits in the blank?",
      "protect", ["destroy", "sell", "forget", "build"], 5,
      "‘자연을 좋은 상태로 유지하고(keep nature in good shape) 역사적 건물을 ___하고 싶었다’ — 앞의 ‘지키다’와 나란한 뜻인 protect(보호하다)가 알맞다. destroy(파괴하다)·sell(팔다)·forget(잊다)은 뜻이 반대이거나 어울리지 않고, 역사적 건물을 새로 ‘짓는다(build)’는 것은 말이 되지 않는다."),
 item(3, "주제", MAIN,
      "how Slow Cities began and what they are like",
      ["health problems from eating too much fast food", "the best Slow Cities to visit in Italy", "how to open a small restaurant in a Slow City", "why big supermarkets are popular in Slow Cities"], 1,
      "슬로푸드 운동에서 시작된 슬로시티 운동의 유래와 목표, 오늘날 슬로시티의 모습을 설명하는 글이다. 패스트푸드의 문제나 식당 여는 방법은 다루지 않고, 글에 나온 슬로시티는 Chianti 하나뿐이며, 대형 마트는 슬로시티에 ‘많지 않다(Slow Cities do not have many fast-food restaurants or big supermarkets)’고 했으므로 ⑤는 글의 내용과 반대이다."),
 item(4, "내용 일치", TRUE,
      "You will not find many big supermarkets in a Slow City.",
      ["People started the slow food movement in the 1990s.", "The slow city movement gave people the idea for slow food.", "Cittaslow is the name of an old building in Italy.", "Only two cities in the world have become Slow Cities."], 1,
      "Slow Cities do not have many fast-food restaurants or big supermarkets. — 슬로시티에는 대형 마트가 많지 않다. 슬로푸드 운동은 1980년대에 시작되었고, 슬로푸드가 슬로시티에 영감을 준 것이며(This inspired …), cittaslow는 마을 개발 ‘계획’의 이름이고, 1999년 이후 ‘수십 개(dozens of)’ 도시가 지정되었다."),
 item(5, "글쓴이의 주장", AGREE,
      "A town can grow without hurting nature or its people.",
      ["Busy people need more fast-food restaurants in their town.", "Big supermarkets help neighbors become good friends.", "A Slow City should stop all new building in the town.", "Only towns in Italy can follow the cittaslow plan."], 4,
      "cittaslow의 원칙: 새 개발(new developments)은 사람을 건강하게 하고 이웃 관계를 좋게 하며 자연환경을 해치지 않아야 한다. 글쓴이는 이를 긍정적으로 소개하고 방문까지 권한다. 패스트푸드 식당이 더 필요하다는 것은 슬로푸드·슬로시티의 취지와 반대이고, 대형 마트가 이웃을 친하게 한다는 내용은 글에 없으며(슬로시티에는 대형 마트가 많지 않다), 새 건설을 모두 멈춰야 한다는 것은 ‘새 개발은 ~해야 한다’는 원칙(개발 자체는 인정)과 어긋나고, 이탈리아 마을만 가능하다는 것은 dozens of cities around the world와 맞지 않는다."),
]),
# ───────────────────────────── Unit 4 (Set D) ─────────────────────────────
dict(key="u4", set="D", title="Unit 4 · Science — The Theory of the Four Elements",
passage="""Before modern chemistry, ancient people tried to understand the makeup of the world. The ancient Greek philosopher Empedocles theorized that four elements made up every substance known to man. These elements were water, fire, earth, and air.

What observations did Empedocles make about these elements? First, he noted that pots were made with earth and water. After being mixed and shaped, they were burned with fire and cooled with air. All four elements were necessary to make one pot. The same pot was used for cooking plants from the earth, often mixed with water, over a flame. The air cooled down the food so it could be eaten. Thus, all four elements were necessary to ______. Empedocles also believed that these elements were ⟪indestructible⟫ and unchangeable. His theories inspired later scientists to study more about the elements that make up our world.""",
gloss="Words: chemistry = the science of what things are made of · makeup = what something is made of · philosopher = a person who thinks about big questions · theorize / theory = an idea about how something works · element = a basic thing that makes up everything · substance = a thing, a material · observation = what you see · flame = fire · thus = so · necessary = needed",
items=[
 item(1, "세부 사실", "According to the passage, which is *NOT* one of the elements?",
      "wood", ["water", "fire", "earth", "air"], 3,
      "These elements were water, fire, earth, and air. 물·불·흙·공기 네 가지이며, 나무(wood)는 네 원소에 들어 있지 않다."),
 item(2, "어휘(단어 뜻)", "What does the underlined word ⟪indestructible⟫ mean?",
      "cannot be broken", ["cannot be eaten", "cannot be moved", "cannot be heard", "cannot be sold"], 1,
      "indestructible = in-(아닌) + destruct(파괴하다) + -ible(할 수 있는) → 파괴할 수 없는(cannot be broken). 뒤에 이어지는 unchangeable(변하지 않는)과 비슷한 뜻으로 묶여 쓰였다."),
 item(3, "도표 완성", TBLQ,
      "(A) earth …… (B) air",
      ["(A) earth …… (B) fire", "(A) fire …… (B) air", "(A) water …… (B) fire", "(A) air …… (B) water"], 5,
      "(A) pots were made with earth and water — 그릇은 흙(earth)과 물로 만든다. (B) they were burned with fire and cooled with air — 공기(air)로 식힌다. 두 문장을 따로 찾아 맞춰야 한다. 불로 식히거나, 불·공기로 그릇을 만든다는 말은 없다.",
      table=[["*Making a Pot*", ""],
             ["1", "Pots are made with (A) ______ and water."],
             ["2", "They are mixed and shaped."],
             ["3", "They are burned with fire."],
             ["4", "They are cooled with (B) ______."]]),
 item(4, "제목", TITLE,
      "Empedocles and the Four Elements",
      ["How to Make a Pot with Earth and Water", "The Lives of Ancient Greek Philosophers", "Why Fire Is the Most Important Element", "How Scientists Work Today"], 2,
      "Empedocles가 세상이 네 원소로 이루어졌다고 본 이론과 그 근거(그릇 만들기·요리)를 설명하는 글이다. 그릇 만드는 법은 예시일 뿐이고, 철학자들의 삶·불의 우월함·오늘날 과학자들이 일하는 방법은 다루지 않았다."),
 item(5, "빈칸 추론", BLANK,
      "cook food", ["build a house", "sell the pot", "grow plants", "start a fire"], 3,
      "빈칸 앞에서 그릇으로 식물을 물과 섞어 불 위에서 요리하고, 공기로 식혀 먹을 수 있게 되는 과정을 설명했다. Thus(따라서)로 이어지는 결론은 ‘음식을 요리하는 데’ 네 원소가 모두 필요했다는 것이다. 집 짓기·그릇 팔기·식물 기르기·불 피우기는 앞 내용과 이어지지 않는다."),
]),
# ───────────────────────────── Unit 5 (Set A) ─────────────────────────────
dict(key="u5", set="A", title="Unit 5 · Art — Teddy Bears Throughout Time",
passage="""How did the teddy bear get its name? It comes from U.S. president Theodore Roosevelt. During a hunting trip, Roosevelt refused to kill a bear that had been tied to a tree. All over America, people heard about ⟪this story⟫. Some people even made stuffed bears and called them “teddy bears” in honor of the president’s nickname, Teddy.

Teddy bears became mass-produced in the twentieth century. They were mainly toys for children, but they were also popularly featured in books and even in movies. Some well-known examples include Winnie the Pooh, which was originally written for adults, as well as Paddington Bear. Due to their popularity, teddy bears were manufactured in a wide range of sizes, colors, and ⟪materials⟫. They have endured such lasting popularity that there are museums dedicated to teddy bears all around the world. England, Japan, and South Korea are just a few countries that have teddy bear museums.

Whether they are children’s toys, subjects of books, or objects on display at museums, teddy bears remain popular. Teddy bears will probably be around for a long time to come.""",
gloss="Words: refuse = say no · stuffed bear = a toy bear · in honor of = to show respect for · nickname = a short, friendly name · mass-produced = made in large numbers · be featured in = appear in · manufacture = make · dedicated to = made for",
items=[
 item(1, "어휘(단어 뜻)", "What does the underlined word ⟪materials⟫ mean?",
      "what something is made of", ["how big something is", "what color something is", "how much something costs", "what shape something is"], 5,
      "material(재료) = what something is made of. 곰 인형이 다양한 크기(sizes)·색깔(colors)·재료(materials)로 만들어졌다는 문맥이다. sizes와 colors는 같은 문장에 나란히 나오는 다른 단어이고, 가격과 모양은 글에 없다."),
 item(2, "세부 사실", "According to the passage, whose nickname gave the teddy bear its name?",
      "the president of the United States", ["a famous toy maker", "the writer of Winnie the Pooh", "the man who tied the bear to a tree", "a museum owner in Japan"], 1,
      "It comes from U.S. president Theodore Roosevelt. … in honor of the president’s nickname, Teddy. 곰을 나무에 묶은 사람이 누구인지는 글에 나오지 않는다."),
 item(3, "지칭 추론", "What does the underlined ⟪this story⟫ refer to?",
      "Roosevelt did not kill a bear tied to a tree.",
      ["Roosevelt became the president of the United States.", "People made stuffed bears and called them “teddy bears.”", "Winnie the Pooh was written for adults.", "A bear ran away from the hunters."], 4,
      "바로 앞 문장 During a hunting trip, Roosevelt refused to kill a bear that had been tied to a tree. — 이 이야기를 미국 전역의 사람들이 들은 것이다. 곰 인형을 만든 것은 그 ‘뒤’의 일이고, 곰이 도망쳤다는 내용은 없다."),
 order_item(4, ORDQ, "(B) – (C) – (A)", 2,
      "Roosevelt가 사냥 여행을 떠남(B, During a hunting trip) → 사람들이 곰 인형을 만들어 teddy bear라고 부름(C) → 20세기에 대량 생산됨(A). 1문단에서 2문단으로 이어지는 순서이다.",
      box="(A) Teddy bears were mass-produced in the twentieth century. \\\n(B) Roosevelt went on a hunting trip. \\\n(C) People made stuffed bears and called them “teddy bears.”"),
 item(5, "추론", INFER,
      "People liked Roosevelt because he did not kill the bear.",
      ["Teddy bears were popular only in America.", "Roosevelt made the first teddy bear himself.", "Teddy bears will soon lose their popularity.", "Teddy bears were mainly toys for adults."], 1,
      "사람들이 이야기를 듣고 대통령을 ‘기리기 위해(in honor of)’ 곰 인형에 그의 별명을 붙였으므로, 곰을 죽이지 않은 그를 좋게 여겼음을 알 수 있다. 박물관이 세계 곳곳에 있으니 미국에서만 인기였던 것이 아니고, 인형을 만든 것은 ‘some people’이며, 앞으로도 오래 사랑받을 것이라 했고, 곰 인형은 ‘주로 아이들의 장난감(mainly toys for children)’이었다."),
]),
# ───────────────────────────── Unit 6 (Set B) ─────────────────────────────
dict(key="u6", set="B", title="Unit 6 · Nature — Osmosis in Everyday Life",
passage="""Molecules are always moving. Sometimes, molecules even move through membranes. Molecules tend to pass through semi-permeable membranes to an area where the solvent concentration is higher. This equalizes the concentration of materials on either side of the membrane. This process is called osmosis. Osmosis is an important chemical process with practical uses in everyday life. What is one use of osmosis?

Fresh vegetables have a high concentration of water molecules. During pickling, vegetables are placed in a brine—a mixture of water, salt, and seasonings. The skin acts as a semi-permeable membrane. Water molecules move out of the vegetables through the skin and into the brine, which equalizes the solvent concentration on either side of the membrane. This process is an example of osmosis, and it is why pickled vegetables stay crunchy.

Reverse osmosis is a process that uses pressure to force molecules into an area of lower solute concentration. We use reverse osmosis to ⟪remove⟫ salt and other particles from seawater. Afterward, we can drink the water!""",
gloss="Words: molecule = a very small part of a thing · tend to = usually · membrane = a thin skin · semi-permeable membrane = a skin that lets only some things pass · solvent = the liquid (here, water) · solute = the thing in the liquid (here, salt) · concentration = how much of something is in a liquid · equalize = make equal · on either side of = on both sides of · practical = useful · pickling = making pickles · seasonings = things you add to food for taste · crunchy = hard, not soft · force = push · pressure = a strong push · particle = a very small piece",
items=[
 item(1, "문맥상 동의어", "Which can best replace the underlined word ⟪remove⟫?",
      "take out", ["put in", "cut up", "look at", "pay for"], 1,
      "remove는 ‘없애다, 제거하다’. 바닷물에서 소금을 ‘빼낸다’는 뜻이므로 take out이 가장 가깝다."),
 item(2, "세부 사실", "According to the passage, what is brine made of?",
      "water, salt, and seasonings", ["water, sugar, and oil", "salt, sugar, and seasonings", "salt, seasonings, and oil", "water, sugar, and pepper"], 4,
      "a brine—a mixture of water, salt, and seasonings. 물, 소금, 양념(seasonings)을 섞은 것이다. ②·③은 물이 빠져 있고, 설탕·기름·후추는 지문에 없다."),
 item(3, "언급 이유", "Why does the writer talk about pickling?",
      "to show how osmosis works in daily life",
      ["to teach how to grow fresh vegetables", "to explain how to make brine step by step", "to show how we can drink seawater", "to explain when molecules stop moving"], 5,
      "1문단 끝 What is one use of osmosis?라는 질문에 답하는 예로 피클 만들기를 들었고, This process is an example of osmosis라고 밝혔다. 바닷물 정수는 ‘역삼투’의 예이며, 분자는 항상 움직인다고 했다."),
 item(4, "내용 불일치", NOTTRUE,
      "Pickled vegetables become soft in the brine.",
      ["Molecules are always moving.", "The skin of a vegetable acts as a semi-permeable membrane.", "During pickling, water moves out of the vegetables.", "People can drink seawater after reverse osmosis."], 4,
      "it is why pickled vegetables stay crunchy — 피클은 ‘아삭함을 유지’한다. 나머지는 Molecules are always moving / The skin acts as a semi-permeable membrane / Water molecules move out of the vegetables … into the brine / Afterward, we can drink the water 와 일치한다."),
 item(5, "요약문 완성", SUMQ + "\n\nOsmosis makes the concentration on both sides of a membrane (A) ______. Reverse osmosis needs (B) ______ to push molecules to the side with less salt.",
      "(A) the same …… (B) pressure",
      ["(A) higher …… (B) heat", "(A) the same …… (B) salt", "(A) lower …… (B) heat", "(A) higher …… (B) pressure"], 3,
      "(A) This equalizes the concentration … on either side of the membrane — 막 양쪽의 농도를 ‘같게(the same)’ 만든다. 분자가 농도가 높은 쪽으로 이동할 뿐, 양쪽 농도가 높아지거나 낮아지는 것이 아니다. (B) Reverse osmosis is a process that uses pressure to force molecules into an area of lower solute concentration — 요약문의 needs … to push … to the side with less salt는 이 문장을 쉽게 바꿔 쓴 것으로, 역삼투에 필요한 것은 ‘압력(pressure)’이다. heat(열)는 지문에 없고, salt(소금)는 역삼투로 없애는 대상이지 이용하는 수단이 아니다."),
]),
# ───────────────────────────── Unit 7 (Set C) ─────────────────────────────
dict(key="u7", set="C", title="Unit 7 · Social Studies — Majority Rule in Democracies",
passage="""People usually make tough decisions by voting for one of two or more options. The option that gets the most votes is the winner. This is called majority rule. However, even if only 51% of people in a group vote for an option, they will get their choice. That means, almost half of the people in that group will not get their choice. In that case, is majority rule really fair?

Most democracies elect public officials through a majority vote. In a system with two political parties, a slim margin, such as 51% to 49%, can decide an election. In a system with more than two parties, less than 50% of voters could give one political party a victory. To ensure the ______ of majority rule, certain conditions must be met. First, people should be able to vote with secret ballots. Second, each person’s vote should be weighted equally. Finally, there have to be enough voters to make a majority vote truly fair.

When an election is won with less than 50% of the total votes, the winning party must consider the opinions of the other voters. This is because running a democracy should ensure equality for all citizens.""",
gloss="Words: tough decision = a hard choice · vote = choose by marking a paper · option = a choice · majority = more than half · democracy = a country where people vote for their leaders · elect = choose by voting · public official = a person who works for the government · political party = a group of people who try to win elections · slim margin = a very small difference · victory = a win · ensure = make sure · condition = something that must be true · be met = be followed · secret ballot = voting where no one sees your choice · be weighted equally = count the same · consider = think about · opinion = what a person thinks · citizen = a person of a country · equality = everyone being treated the same",
items=[
 item(1, "세부 사실", "According to the passage, which option wins under majority rule?",
      "the option that gets the most votes", ["the option chosen by the oldest person", "the option that everyone agrees on", "the option that the president likes best", "the option that gets the fewest votes"], 3,
      "The option that gets the most votes is the winner. This is called majority rule."),
 item(2, "문장 빈칸 어휘", "Which word best fits in the blank?",
      "fairness", ["victory", "speed", "price", "size"], 4,
      "앞 문단 끝의 is majority rule really fair?와 뒤의 to make a majority vote truly fair가 단서이다. 다수결의 ‘공정함(fairness)’을 보장하기 위해 조건이 필요하다는 뜻이다. victory(승리)·speed(속도)·price(가격)·size(크기)는 이 문맥과 맞지 않는다."),
 item(3, "주제", MAIN,
      "majority rule and what it needs to work well",
      ["how a slim margin decides a two-party election", "the history of majority rule in democracies", "why every democracy needs secret ballots", "the jobs of public officials in a democracy"], 3,
      "다수결의 뜻과 한계(거의 절반이 원하는 것을 얻지 못함), 다수결이 제대로 이루어지기 위한 세 가지 조건, 이긴 쪽이 가져야 할 태도를 설명하는 글이다. 근소한 차이의 선거와 비밀 투표는 글의 일부 내용만 담은 너무 좁은 주제이고, 다수결의 역사와 공직자의 일은 글에 없다."),
 item(4, "내용 일치", TRUE,
      "With more than two parties, a party can win with under 50% of the votes.",
      ["Under majority rule, an option with only 51% of the votes does not win.", "Most democracies choose public officials without voting.", "People do not need secret ballots for a fair vote.", "With two parties, 51% to 49% is too small to decide an election."], 5,
      "In a system with more than two parties, less than 50% of voters could give one political party a victory. 51%만 얻어도 원하는 것을 얻으므로(they will get their choice) ①은 틀리고, 공직자는 ‘다수결 투표로(through a majority vote)’ 뽑으며, 비밀 투표(secret ballots)는 공정한 다수결의 첫째 조건이고, 두 정당 체제에서는 51% 대 49% 같은 근소한 차이(slim margin)로도 선거가 ‘결정될 수 있다(can decide)’."),
 item(5, "글쓴이의 주장", AGREE,
      "A decision made by majority rule may not be fair to everyone.",
      ["Majority rule works well even when only a few people vote.", "A winning party does not need to listen to the other voters.", "In a fair vote, some people’s votes may count more than others’.", "A democracy does not need equality for all its citizens."], 2,
      "글쓴이는 51%만 얻어도 이기므로 거의 절반이 원하는 것을 얻지 못한다며 ‘다수결이 정말 공정한가’를 묻고, 이긴 정당은 다른 유권자의 의견을 고려해야 하며 민주주의는 모든 시민의 평등을 보장해야 한다고 했다. 투표하는 사람이 적어도 잘 작동한다는 것은 there have to be enough voters to make a majority vote truly fair와 반대이고, 이긴 정당이 다른 유권자의 말을 들을 필요가 없다는 것은 must consider the opinions of the other voters와 반대이며, 어떤 사람의 표가 더 무거울 수 있다는 것은 weighted equally와, 민주주의에 평등이 필요 없다는 것은 ensure equality for all citizens와 어긋난다."),
]),
# ───────────────────────────── Unit 8 (Set D) ─────────────────────────────
dict(key="u8", set="D", title="Unit 8 · Science — The Rising Prominence of Telescopes",
passage="""The invention of the telescope has helped humans see and understand the stars better. How have telescopes changed over time?

Telescopes were originally used to see long distances. Galileo was one of the first to use a telescope to observe the stars. His telescope used a concave eyepiece and a convex lens. This gave the image seen through the telescope an upright view and magnified it up to thirty times! Even though Galileo’s telescope was quite useful at the time, the images it produced were blurry. Kepler improved on Galileo’s design by using a convex eyepiece and lens. This gave a much wider field of view, even though the images appeared upside-down.

In modern times, telescopes have been launched into space to help ⟪astronomers⟫ observe not just the stars, but the universe as well. One example is the Hubble Telescope, which orbits Earth and sends back high-quality pictures of distant planets and galaxies. Through continued technological developments, humans can ______.""",
gloss="Words: invention = making something new for the first time · observe = watch carefully · concave = curved in · convex = curved out · eyepiece = the part you look into · upright = with the top at the top (not upside-down) · magnify = make bigger · blurry = not clear · field of view = how much you can see · upside-down = the top at the bottom · launch = send into space · orbit = go around · distant = far away · galaxy = a very large group of stars · continued = going on · technological development = new technology",
items=[
 item(1, "세부 사실", "According to the passage, how many times could Galileo’s telescope magnify an image?",
      "thirty times", ["three times", "five times", "ten times", "twenty times"], 5,
      "… and magnified it up to thirty times! 최대 30배까지 확대했다."),
 item(2, "어휘(단어 뜻)", "What does the underlined word ⟪astronomers⟫ mean?",
      "people who study the stars", ["people who invent new things", "people who fly airplanes", "people who work on a farm", "people who design buildings"], 1,
      "astronomer(천문학자) = a person who studies the stars and space. 망원경이 우주로 발사되어 ‘천문학자들’이 별과 우주를 관측하도록 돕는다는 문맥이다."),
 item(3, "도표 완성", TBLQ,
      "(A) concave …… (B) upside-down",
      ["(A) convex …… (B) upside-down", "(A) concave …… (B) blurry", "(A) convex …… (B) upright", "(A) concave …… (B) clear"], 4,
      "(A) His telescope used a concave eyepiece and a convex lens — Galileo의 접안렌즈는 오목(concave). (B) Kepler의 망원경은 시야가 넓어진 대신 the images appeared upside-down — 거꾸로 보였다. blurry(흐릿한)는 Galileo 망원경의 단점이다.",
      table=[["", "*Galileo’s telescope*", "*Kepler’s telescope*"],
             ["eyepiece", "(A) ______", "convex"],
             ["lens", "convex", "convex"],
             ["images", "upright, but blurry", "wider view, but (B) ______"]]),
 item(4, "제목", TITLE,
      "The Development of Telescopes",
      ["How to Make Your Own Telescope", "The Weak Points of Galileo’s Telescope", "What the Hubble Telescope Does", "Galileo and Kepler: Two Great Scientists"], 2,
      "1문단의 질문 How have telescopes changed over time?에 답하여 Galileo → Kepler → Hubble로 이어지는 망원경의 발전을 설명하는 글이다. Galileo 망원경의 단점(흐릿함), Hubble 망원경이 하는 일, Galileo와 Kepler 두 과학자는 글의 일부만 담아 제목으로는 너무 좁고, 망원경 제작법은 글의 내용이 아니다."),
 item(5, "빈칸 추론", BLANK,
      "understand the universe much better",
      ["travel to distant planets and galaxies", "see the stars without any telescope", "build telescopes faster and cheaper", "send more people into space"], 1,
      "1문단에서 망원경의 발명이 인간이 별을 더 잘 ‘이해하도록(understand)’ 도왔다고 했고, 3문단에서 우주 망원경이 별과 우주를 관측하며 고화질 사진을 보내온다고 했다. 글 전체가 망원경으로 별과 우주를 ‘보고 이해하는’ 이야기이므로, 기술이 계속 발전하면 인간은 ‘우주를 훨씬 더 잘 이해할 수’ 있다. 먼 행성으로 여행하거나, 사람을 더 많이 우주에 보내거나, 망원경을 더 빠르고 싸게 만든다는 내용은 글에 없고, 망원경 없이 별을 본다는 것은 글의 흐름과 반대이다."),
]),
]

PAIR = {"A": "1·5 (Art)", "B": "2·6 (Nature)", "C": "3·7 (Social Studies)", "D": "4·8 (Science)"}


def build():
    sections, blueprint, qno = [], [], 0
    for u in UNITS:
        passage = {"type": "passage", "title": f"[{qno+1}–{qno+5}] Read the passage and answer the questions.", "text": u["passage"]}
        if GLOSS and u.get("gloss"):
            passage["note"] = u["gloss"]
        items = [passage]
        assert [it["_lv"] for it in u["items"]] == [1, 2, 3, 4, 5]
        for it in u["items"]:
            qno += 1
            blueprint.append((qno, u["key"].upper(), u["set"], it["_lv"], it["_kind"], it["answer"]))
            items.append({k: v for k, v in it.items() if not k.startswith("_")})
        # 섹션 머리에는 원문 제목을 찍지 않는다 (주제·제목 문항 유출 방지)
        sections.append({"title": u["title"].split(" — ")[0], "items": items})
    kinds = {u["key"]: [it["_kind"] for it in u["items"]] for u in UNITS}
    for a, b in (("u1", "u5"), ("u2", "u6"), ("u3", "u7"), ("u4", "u8")):
        assert kinds[a] == kinds[b], (a, b)
    dist = Counter(b[5] for b in blueprint)
    assert qno == 40 and set(dist.values()) == {8}, dist
    doc = {
        "title": "The Reading 7-1 Final Test",
        "meta": {"subject": "English Reading", "grade": "Level 7", "unit": "Units 1–8", "time_limit": "60 minutes"},
        "student_fields": ["Class", "Name", "Score"],
        "instructions": [
            "40 questions · 5 choices · 2.5 points each (100 points) · *Pass: 70 points (28 correct)* · Choose one answer.",
        ],
        "layout": {"columns": 1, "font_size": 9.5, "show_points": True, "choice_columns": 0, "section_pagebreak": True},
        "sections": sections,
    }
    return doc, blueprint, kinds


def blueprint_md(blueprint, kinds):
    lines = ["# The Reading 7-1 Final Test · 문항 구성표", "",
             "대상: The Reading Level 7을 배운 초등학교 6학년 · 40문항 · 5지선다 · 문항당 2.5점 · 100점 만점 · 70점(28문항) 이상 합격 · 60분", "",
             "학생용 시험지는 전부 영어(발문·선택지·단어 풀이·안내문)이고, 정답·해설지의 해설만 한국어(교사용)이다.", "",
             "## 유형 설계 (단원 쌍끼리 동일)", "", "| 쌍 | 1 | 2 | 3 | 4 | 5 |", "|---|---|---|---|---|---|"]
    for s, (a, _) in zip("ABCD", (("u1", "u5"), ("u2", "u6"), ("u3", "u7"), ("u4", "u8"))):
        lines.append(f"| {PAIR[s]} | " + " | ".join(kinds[a]) + " |")
    lines += ["", "## 초6 눈높이 장치", "",
              "- 발문과 선택지는 짧고 쉬운 영어로 쓰고, 한 문항 안에서 선택지 형태를 맞춘다.",
              "- 어휘 문항은 밑줄 친 단어의 뜻을 쉬운 영어로 고른다.",
              "- 사건 순서 배열은 사건 3개만 쓴다.",
              "- 지문 아래에 시험에 나오지 않는 어려운 단어의 뜻을 쉬운 영어로 달아 준다 (build_7-1.py 의 GLOSS = False 로 끌 수 있다).",
              "- 단원 머리에 원문 제목을 찍지 않는다(주제·제목 문항 유출 방지).",
              "", "## 난이도와 목표 정답률", "", "| 난이도 | 설명 | 예상 정답률(초6 평균) |", "|---|---|---|"]
    for lv in range(1, 6):
        lines.append(f"| {lv} | {LEVEL[lv]} | {int(EXPECTED_P[lv]*100)}% |")
    mean = sum(EXPECTED_P.values()) / 5 * 100
    lines += ["", f"예상 평균 점수 약 {mean:.0f}점. 학급 표준편차를 12점으로 가정하면 70점 이상이 약 70~80%가 된다. "
              "실제 시행 후 문항별 정답률을 보고 조정한다.", "",
              "## 문항별 정보", "", "| 번호 | 단원 | 쌍 | 난이도 | 유형 | 정답 |", "|---|---|---|---|---|---|"]
    for q, unit, s, lv, kind, ans in blueprint:
        lines.append(f"| {q} | {unit} | {s} | {lv} | {kind} | {ans} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "TheReading_7-1_FinalTest.json")
    doc, blueprint, kinds = build()
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    out.with_name("TheReading_7-1_FinalTest_문항구성표.md").write_text(blueprint_md(blueprint, kinds), encoding="utf-8")
    print(out, dict(sorted(Counter(b[5] for b in blueprint).items())))
