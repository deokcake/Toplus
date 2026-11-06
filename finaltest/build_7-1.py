"""The Reading 7-1 Final Test — 문항 원본 데이터 → exam-worksheet JSON + 문항구성표.

유형 설계: 단원 쌍(1·5, 2·6, 3·7, 4·8)끼리 같은 5개 유형을 쓰고,
각 단원 안에서 1번→5번으로 갈수록 어려워진다.

  Set A (1·5 Art)      : 영영풀이 어휘 → 세부 사실 → 지칭 추론 → 사건 순서 배열 → 추론
  Set B (2·6 Nature)   : 문맥상 동의어 → 세부 사실 → 언급 이유 → 내용 불일치 → 요약문 (A)(B)
  Set C (3·7 Social)   : 세부 사실 → 문장 빈칸 어휘 → 주제 → 내용 일치 → 글쓴이의 주장
  Set D (4·8 Science)  : 세부 사실 → 영영풀이 어휘 → 도표 완성 (A)(B) → 제목 → 빈칸 추론

표기: 지문·발문 속 ⟪단어⟫ 는 밑줄, ______ 는 빈칸 상자로 조판된다.
"""
import json
import sys
from collections import Counter
from pathlib import Path

LEVEL = {1: "매우 쉬움", 2: "쉬움", 3: "보통", 4: "다소 어려움", 5: "어려움"}
EXPECTED_P = {1: 0.93, 2: 0.88, 3: 0.80, 4: 0.70, 5: 0.55}  # 중1 평균 학생 기준 예상 정답률

VOC = "다음 영영풀이에 해당하는 단어로 가장 적절한 것은?"
SUMQ = "다음은 윗글을 요약한 것이다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?"
ORDQ = "다음 (A)~(D)를 윗글에서 일어난 순서대로 바르게 배열한 것은?"
TBLQ = "다음은 윗글의 내용을 정리한 표이다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?"


def item(lv, kind, prompt, answer, wrong, pos, expl, **extra):
    assert len(wrong) == 4 and answer not in wrong and 1 <= pos <= 5
    choices = list(wrong)
    choices.insert(pos - 1, answer)
    d = {"type": "multiple_choice", "prompt": prompt, "choices": choices, "answer": pos,
         "points": 2.5, "explanation": f"[난이도 {lv}·{LEVEL[lv]} / {kind}] {expl}"}
    d.update(extra)
    d["_lv"], d["_kind"] = lv, kind
    return d


UNITS = [
# ───────────────────────────── Unit 1 (Set A) ─────────────────────────────
dict(key="u1", set="A", title="Unit 1 · Art — Andy Warhol and Pop Art",
passage="""Art in advertisements has become increasingly popular. This is called commercial art. One of the most famous commercial artists was Andy Warhol.

Andy Warhol was often sick as a child, so he spent a lot of time drawing. After college, he began his career making art for advertisements. His drawings of shoes became so well known that people wanted to see more of his work. Thus, in the 1950s, he began showing his popular works in art galleries. Warhol was one of the first artists to use silkscreen ink printing in his work. During the 1960s, he produced many famous art pieces depicting everyday objects. ⟪These⟫ include Coca-Cola bottles, dollar bills, and Campbell’s Soup cans. This kind of art is referred to as “pop art.”

Some critics think Andy Warhol was only interested in making money with his art. Others thought he was the perfect example of commercialized modern life. Apart from this argument, most critics agree that Warhol’s work shows the changing value of art in everyday life.""",
items=[
 item(1, "영영풀이 어휘", VOC + "\n\n“a person who writes about and expresses opinions about books, movies, music, or art”",
      "critic", ["gallery", "career", "object", "television"], 3,
      "critic(비평가): 책·영화·음악·미술에 대해 글을 쓰고 의견을 밝히는 사람. 3문단 Some critics think … 에서 쓰였다. gallery(미술관), career(경력), object(사물), television(텔레비전)은 모두 사람이 아니다."),
 item(2, "세부 사실", "윗글에 따르면, Andy Warhol이 어린 시절 그림을 많이 그린 이유로 가장 적절한 것은?",
      "He was often sick as a child.",
      ["He studied art in college.", "His parents were famous artists.", "He wanted to sell his drawings.", "He worked for a magazine."], 2,
      "2문단 첫 문장 Andy Warhol was often sick as a child, so he spent a lot of time drawing. 어릴 때 자주 아파서 그림을 많이 그렸다. 대학·부모·판매·잡지 근무는 본문에 근거가 없다."),
 item(3, "지칭 추론", "윗글의 밑줄 친 ⟪These⟫가 가리키는 것으로 가장 적절한 것은?",
      "Warhol’s art pieces that show everyday objects",
      ["the advertisements Warhol made after college", "the art galleries that showed his works", "Warhol’s early drawings of shoes", "the critics who wrote about Warhol"], 1,
      "바로 앞 문장의 many famous art pieces depicting everyday objects(일상 사물을 그린 유명 작품들)를 받는다. 이어서 그 예로 Coca-Cola bottles, dollar bills, Campbell’s Soup cans가 나온다."),
 item(4, "사건 순서 배열", ORDQ,
      "(D) – (B) – (A) – (C)",
      ["(B) – (D) – (A) – (C)", "(D) – (A) – (B) – (C)", "(D) – (B) – (C) – (A)", "(B) – (A) – (C) – (D)"], 5,
      "어릴 때 아파서 그림을 많이 그림(D) → 대학 졸업 후 광고 미술로 경력 시작(B) → 1950년대 미술관에서 작품 전시(A) → 1960년대 일상 사물을 그린 작품 제작(C). 2문단의 흐름 그대로이다.",
      box="(A) Warhol began showing his works in art galleries. \\\n(B) Warhol began making art for advertisements. \\\n(C) Warhol produced art pieces depicting everyday objects. \\\n(D) Warhol spent a lot of time drawing because he was often sick."),
 item(5, "추론", "윗글을 통해 추론할 수 있는 것으로 가장 적절한 것은?",
      "Pop art used images that people saw in their daily lives.",
      ["Warhol stopped making art after he became famous.", "All critics agreed that Warhol only wanted to make money.", "Warhol was the person who invented silkscreen ink printing.", "Commercial art was more popular in the past than it is today."], 4,
      "일상 사물(콜라병, 지폐, 수프 캔)을 그린 작품을 pop art라 부른다고 했으므로, 팝아트가 일상에서 보는 이미지를 썼음을 추론할 수 있다. 유명해진 뒤 작업을 멈췄다는 내용은 없고, 비평가 의견은 갈렸으며(Some critics … Others …), 실크스크린은 ‘처음 사용한 화가 중 한 명’이지 발명자가 아니고, 광고 미술은 점점 인기를 얻고 있다(increasingly popular)."),
]),
# ───────────────────────────── Unit 2 (Set B) ─────────────────────────────
dict(key="u2", set="B", title="Unit 2 · Nature — The Water Cycle Keeps Earth Balanced",
passage="""The water cycle is necessary for life on Earth. Water on the ground evaporates into vapor and forms clouds in the sky. In return, rain brings water back down to the ground again. What happens when humans tamper with the water cycle?

Most evaporation occurs in oceans as a result of the Sun’s energy. This cools the temperature of Earth’s climate and also affects the oceans’ salt content. Having the correct amount of salt in the oceans ⟪maintains⟫ a delicate ecosystem of plants, fish, and other wildlife. One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. The two rivers that fed the Aral Sea were diverted for farming in the desert. As a result, the sea is now almost completely dry, killing the wildlife that lived there and causing dust storms that affect human health.

As we can see, the water cycle is necessary to keep the environment balanced.""",
items=[
 item(1, "문맥상 동의어", "윗글의 밑줄 친 ⟪maintains⟫와 의미가 가장 가까운 것은?",
      "keeps", ["breaks", "loses", "sells", "finds"], 1,
      "maintain은 ‘(상태를) 유지하다’. 알맞은 양의 소금이 생태계를 ‘유지한다’는 뜻이므로 keeps가 가장 가깝다."),
 item(2, "세부 사실", "윗글에 따르면, Aral Sea로 흘러들던 두 강의 물길을 바꾼 목적은?",
      "to farm in the desert", ["to build a new city", "to make electricity", "to stop dust storms", "to protect wildlife"], 4,
      "The two rivers that fed the Aral Sea were diverted for farming in the desert. 사막에서 농사를 짓기 위해서였다. 도시 건설·발전·황사 방지·야생동물 보호는 언급되지 않았다."),
 item(3, "언급 이유", "글쓴이가 Aral Sea를 언급한 이유로 가장 적절한 것은?",
      "물의 순환을 함부로 바꾸면 생기는 재앙의 예를 들기 위해",
      ["사막에서 농사짓는 방법을 소개하기 위해", "바다의 소금이 생기는 과정을 설명하기 위해", "세계에서 가장 큰 호수를 소개하기 위해", "증발이 기후를 식히는 원리를 보여 주기 위해"], 2,
      "One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. 물의 순환을 건드려서 생긴 재앙의 ‘예’로 든 것이다."),
 item(4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
      "Most evaporation happens in rivers and lakes.",
      ["Rain brings water back down to the ground.", "Evaporation affects the salt content of the oceans.", "The Aral Sea is now almost completely dry.", "Dust storms from the Aral Sea affect human health."], 3,
      "Most evaporation occurs in oceans — 증발은 대부분 ‘바다’에서 일어난다. 나머지는 각각 In return, rain brings water back down / affects the oceans’ salt content / almost completely dry / dust storms that affect human health 와 일치한다."),
 item(5, "요약문 완성", SUMQ + "\n\nEvaporation (A) ______ Earth’s climate and affects the salt in the oceans. But when people (B) ______ the water cycle, a disaster like the drying-up of the Aral Sea can happen.",
      "(A) cools …… (B) change",
      ["(A) warms …… (B) change", "(A) cools …… (B) protect", "(A) warms …… (B) study", "(A) dries …… (B) protect"], 5,
      "(A) This cools the temperature of Earth’s climate — 증발은 기후를 ‘식힌다’. (B) tamper with(함부로 손대다·바꾸다)의 뜻이므로 change. 사람들이 물의 순환을 ‘보호’하거나 ‘연구’해서 재앙이 생긴다는 것은 논리에 맞지 않는다."),
]),
# ───────────────────────────── Unit 3 (Set C) ─────────────────────────────
dict(key="u3", set="C", title="Unit 3 · Social Studies — The Slow City Movement",
passage="""In the 1980s, people who protested the increasing trend of fast food started a “slow food” movement. The movement aimed to preserve local foods, recipes, and communities, while rejecting fast, commercialized foods. This inspired the “slow city movement.”

The first Slow City was Chianti, Italy. The people there wanted to keep nature in good shape and ______ historic buildings. They came up with a plan for developing their town just the way they wanted. They called this plan cittaslow. The founders of this plan decided that new developments should keep people healthy and promote good relationships among neighbors. They also thought development should not hurt the natural environment.

Since 1999, dozens of cities around the world have been named Slow Cities. Slow Cities do not have many fast-food restaurants or big supermarkets. Instead, they have locally owned restaurants and small markets. Try visiting a Slow City someday to see if you like it!""",
items=[
 item(1, "세부 사실", "윗글에 따르면, 최초의 Slow City는 어디인가?",
      "Chianti, Italy", ["Rome, Italy", "Paris, France", "Seoul, Korea", "Madrid, Spain"], 2,
      "The first Slow City was Chianti, Italy."),
 item(2, "문장 빈칸 어휘", "윗글의 빈칸에 들어갈 말로 가장 적절한 것은?",
      "protect", ["destroy", "remove", "reject", "forget"], 5,
      "‘자연을 좋은 상태로 유지하고(keep nature in good shape) 역사적 건물을 ___하고 싶었다’ — 앞의 ‘지키다’와 나란한 뜻인 protect(보호하다)가 알맞다. destroy(파괴하다)·remove(없애다)는 반대 뜻이고, reject(거부하다)·forget(잊다)은 건물과 어울리지 않는다."),
 item(3, "주제", "윗글의 주제로 가장 적절한 것은?",
      "the slow city movement and what Slow Cities are like",
      ["the dangers of eating fast food", "famous foods of Italy", "how to open a small restaurant", "the history of Italian cities"], 3,
      "슬로푸드 운동에서 시작된 슬로시티 운동의 유래·목표와 오늘날 슬로시티의 모습을 설명하는 글이다. 패스트푸드의 위험, 이탈리아 음식, 식당 창업, 이탈리아 도시의 역사는 글의 중심이 아니다."),
 item(4, "내용 일치", "윗글의 내용과 일치하는 것은?",
      "Slow Cities have locally owned restaurants instead of many fast-food restaurants.",
      ["The slow food movement started in the 1990s.", "The slow city movement inspired the slow food movement.", "Cittaslow is the name of a historic building in Chianti.", "Only two cities have been named Slow Cities since 1999."], 1,
      "Slow Cities do not have many fast-food restaurants … Instead, they have locally owned restaurants and small markets. 슬로푸드 운동은 1980년대에 시작했고, 슬로푸드가 슬로시티에 영감을 준 것이며(This inspired …), cittaslow는 마을 개발 ‘계획’의 이름이고, 1999년 이후 ‘수십 개’(dozens of) 도시가 지정되었다."),
 item(5, "글쓴이의 주장", "윗글의 글쓴이가 가장 동의할 만한 것은?",
      "A town can develop without harming nature or people’s health.",
      ["Fast food is the best way to feed a busy city.", "Big supermarkets bring neighbors closer together.", "A city should grow as fast as possible.", "Historic buildings should be replaced with new ones."], 4,
      "cittaslow의 원칙: 개발은 사람을 건강하게 하고 이웃 관계를 좋게 하며 자연환경을 해치지 않아야 한다. 글쓴이는 이를 긍정적으로 소개하고 방문까지 권한다. 패스트푸드·대형 마트·빠른 성장·역사적 건물 교체는 모두 글의 취지와 반대이다."),
]),
# ───────────────────────────── Unit 4 (Set D) ─────────────────────────────
dict(key="u4", set="D", title="Unit 4 · Science — The Theory of the Four Elements",
passage="""Before modern chemistry, ancient people tried to understand the makeup of the world. The ancient Greek philosopher Empedocles theorized that four elements made up every substance known to man. These elements were water, fire, earth, and air.

What observations did Empedocles make about these elements? First, he noted that pots were made with earth and water. After being mixed and shaped, they were burned with fire and cooled with air. All four elements were necessary to make one pot. The same pot was used for cooking plants from the earth, often mixed with water, over a flame. The air cooled down the food so it could be eaten. Thus, all four elements were necessary to ______. Empedocles also believed that these elements were indestructible and unchangeable. His theories inspired later scientists to study more about the elements that make up our world.""",
items=[
 item(1, "세부 사실", "윗글에서 Empedocles가 말한 네 가지 원소에 해당하지 *않는* 것은?",
      "wood", ["water", "fire", "earth", "air"], 4,
      "These elements were water, fire, earth, and air. 나무(wood)는 네 원소에 들어 있지 않다."),
 item(2, "영영풀이 어휘", VOC + "\n\n“very strong and impossible to break or destroy”",
      "indestructible", ["ancient", "delicious", "modern", "necessary"], 1,
      "indestructible(파괴할 수 없는) = in-(아닌) + destruct(파괴하다) + -ible(할 수 있는). Empedocles also believed that these elements were indestructible … ancient(고대의), delicious(맛있는), modern(현대의), necessary(필요한)."),
 item(3, "도표 완성", TBLQ,
      "(A) fire …… (B) air",
      ["(A) air …… (B) fire", "(A) fire …… (B) water", "(A) water …… (B) air", "(A) earth …… (B) fire"], 5,
      "After being mixed and shaped, they were burned with fire and cooled with air. 불(fire)로 굽고 공기(air)로 식힌다.",
      table=[["*Making a Pot*", ""],
             ["1", "Pots are made with earth and water."],
             ["2", "They are mixed and shaped."],
             ["3", "They are burned with (A) ______."],
             ["4", "They are cooled with (B) ______."]]),
 item(4, "제목", "윗글의 제목으로 가장 적절한 것은?",
      "Empedocles and His Theory of the Four Elements",
      ["How to Make a Pot with Earth and Water", "The Life of Ancient Greek Philosophers", "Why Fire Is the Most Important Element", "Modern Chemistry and the Periodic Table"], 2,
      "Empedocles가 세상이 네 원소로 이루어졌다고 본 이론과 그 근거(항아리 만들기·요리)를 설명하는 글이다. 항아리 만드는 법은 예시일 뿐이고, 철학자들의 생애·불의 우월성·주기율표는 다루지 않았다."),
 item(5, "빈칸 추론", "윗글의 빈칸에 들어갈 말로 가장 적절한 것은?",
      "prepare a meal", ["build a house", "sell the pot", "grow plants", "start a fire"], 3,
      "빈칸 앞에서 항아리로 식물을 물과 섞어 불 위에서 요리하고, 공기로 식혀 먹을 수 있게 되는 과정을 설명했다. Thus(따라서)로 이어지는 결론은 ‘식사를 준비하는 데’ 네 원소가 모두 필요했다는 것이다. 집 짓기·항아리 판매·식물 재배·불 피우기는 앞 내용과 이어지지 않는다."),
]),
# ───────────────────────────── Unit 5 (Set A) ─────────────────────────────
dict(key="u5", set="A", title="Unit 5 · Art — Teddy Bears Throughout Time",
passage="""How did the teddy bear get its name? It comes from U.S. president Theodore Roosevelt. During a hunting trip, Roosevelt refused to kill a bear that had been tied to a tree. All over America, people heard about ⟪this story⟫. Some people even made stuffed bears and called them “teddy bears” in honor of the president’s nickname, Teddy.

Teddy bears became mass-produced in the twentieth century. They were mainly toys for children, but they were also popularly featured in books and even in movies. Some well-known examples include Winnie the Pooh, which was originally written for adults, as well as Paddington Bear. Due to their popularity, teddy bears were manufactured in a wide range of sizes, colors, and materials. They have endured such lasting popularity that there are museums dedicated to teddy bears all around the world. England, Japan, and South Korea are just a few countries that have teddy bear museums.

Whether they are children’s toys, subjects of books, or objects on display at museums, teddy bears remain popular. Teddy bears will probably be around for a long time to come.""",
items=[
 item(1, "영영풀이 어휘", VOC + "\n\n“to say no to something that is offered to you, or to not do something you are asked to do”",
      "refuse", ["display", "tie", "hear", "remain"], 5,
      "refuse(거절하다, 거부하다). Roosevelt refused to kill a bear … display(전시하다), tie(묶다), hear(듣다), remain(남아 있다)."),
 item(2, "세부 사실", "윗글에 따르면, ‘teddy bear’라는 이름은 누구의 별명에서 나왔는가?",
      "U.S. president Theodore Roosevelt",
      ["a famous toy maker", "the writer of Winnie the Pooh", "a hunter who caught a bear", "a museum owner in Japan"], 3,
      "It comes from U.S. president Theodore Roosevelt. … in honor of the president’s nickname, Teddy."),
 item(3, "지칭 추론", "윗글의 밑줄 친 ⟪this story⟫가 가리키는 내용으로 가장 적절한 것은?",
      "Roosevelt refused to kill a bear that was tied to a tree.",
      ["Roosevelt became the president of the United States.", "Some people made stuffed bears and named them teddy bears.", "Winnie the Pooh was originally written for adults.", "A bear escaped from a tree during a hunting trip."], 4,
      "바로 앞 문장 During a hunting trip, Roosevelt refused to kill a bear that had been tied to a tree. 이 이야기를 미국 전역의 사람들이 들은 것이다. 곰 인형 제작은 그 ‘뒤’의 일이고, 곰이 도망쳤다는 내용은 없다."),
 item(4, "사건 순서 배열", ORDQ,
      "(B) – (A) – (D) – (C)",
      ["(A) – (B) – (D) – (C)", "(B) – (D) – (A) – (C)", "(B) – (A) – (C) – (D)", "(D) – (B) – (A) – (C)"], 2,
      "사냥 여행에서 곰을 죽이지 않음(B) → 그 이야기가 미국 전역에 퍼짐(A) → 사람들이 곰 인형을 만들어 teddy bear라 부름(D) → 20세기에 대량 생산됨(C). 1문단에서 2문단으로 이어지는 순서이다.",
      box="(A) People all over America heard about the story. \\\n(B) Roosevelt refused to kill a bear on a hunting trip. \\\n(C) Teddy bears became mass-produced in the twentieth century. \\\n(D) Some people made stuffed bears and called them “teddy bears.”"),
 item(5, "추론", "윗글을 통해 추론할 수 있는 것으로 가장 적절한 것은?",
      "Many Americans admired Roosevelt for not killing the bear.",
      ["Teddy bears were popular only in America.", "Roosevelt made the first teddy bear himself.", "Teddy bears will soon lose their popularity.", "Paddington Bear was the first teddy bear ever made."], 1,
      "사람들이 이야기를 듣고 대통령을 ‘기리기 위해’(in honor of) 곰 인형에 그의 별명을 붙였으므로, 곰을 죽이지 않은 그를 좋게 여겼음을 추론할 수 있다. 박물관이 세계 곳곳에 있으니 미국에서만 인기였던 것이 아니고, 인형을 만든 것은 ‘some people’이며, 앞으로도 오래 사랑받을 것이라 했고, Paddington Bear는 책에 나온 곰의 예일 뿐이다."),
]),
# ───────────────────────────── Unit 6 (Set B) ─────────────────────────────
dict(key="u6", set="B", title="Unit 6 · Nature — Osmosis in Everyday Life",
passage="""Molecules are always moving. Molecules tend to pass through semi-permeable membranes to an area where the solvent concentration is higher. This equalizes the concentration of materials on either side of the membrane. This process is called osmosis. Osmosis is an important chemical process with practical uses in everyday life. What is one use of osmosis?

Fresh vegetables have a high concentration of water molecules. During pickling, vegetables are placed in a brine—a mixture of water, salt, and seasonings. The skin acts as a semi-permeable membrane. Water molecules move out of the vegetables through the skin and into the brine, which equalizes the solvent concentration on either side of the membrane. This process is an example of osmosis, and it is why pickled vegetables stay crunchy.

Reverse osmosis is a process that uses pressure to force molecules into an area of lower solute concentration. We use reverse osmosis to ⟪remove⟫ salt and other particles from seawater. Afterward, we can drink the water!""",
items=[
 item(1, "문맥상 동의어", "윗글의 밑줄 친 ⟪remove⟫와 의미가 가장 가까운 것은?",
      "take out", ["put in", "mix up", "heat up", "keep"], 1,
      "remove는 ‘없애다, 제거하다’. 바닷물에서 소금을 ‘빼낸다’는 뜻이므로 take out이 가장 가깝다."),
 item(2, "세부 사실", "윗글에 따르면, brine은 무엇으로 이루어져 있는가?",
      "water, salt, and seasonings",
      ["water, sugar, and oil", "salt, vinegar, and sugar", "seawater and vegetables", "water and black pepper only"], 2,
      "a brine—a mixture of water, salt, and seasonings. 물, 소금, 양념의 혼합물이다."),
 item(3, "언급 이유", "글쓴이가 pickling(피클 만들기)을 언급한 이유로 가장 적절한 것은?",
      "일상생활에서 삼투 현상이 쓰이는 예를 들기 위해",
      ["채소를 싱싱하게 기르는 방법을 알려 주기 위해", "소금물을 만드는 순서를 설명하기 위해", "바닷물을 마실 수 있게 만드는 과정을 보여 주기 위해", "분자가 움직이지 않는 경우를 설명하기 위해"], 5,
      "1문단 끝 What is one use of osmosis?라는 질문에 답하는 예로 피클 만들기를 들었고, This process is an example of osmosis라고 밝혔다. 바닷물 정수는 ‘역삼투’의 예이며, 분자는 항상 움직인다고 했다."),
 item(4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
      "Pickled vegetables become soft because of osmosis.",
      ["Molecules are always moving.", "The skin of a vegetable acts as a semi-permeable membrane.", "During pickling, water moves out of the vegetables into the brine.", "Reverse osmosis uses pressure to remove salt from seawater."], 4,
      "it is why pickled vegetables stay crunchy — 삼투 덕분에 피클은 ‘아삭함을 유지’한다. 나머지는 Molecules are always moving / The skin acts as a semi-permeable membrane / Water molecules move out of the vegetables … into the brine / uses pressure … remove salt 와 일치한다."),
 item(5, "요약문 완성", SUMQ + "\n\nOsmosis (A) ______ the concentration on both sides of a membrane, as in pickling. Reverse osmosis uses pressure to remove salt from seawater and makes it (B) ______.",
      "(A) equalizes …… (B) drinkable",
      ["(A) increases …… (B) salty", "(A) stops …… (B) drinkable", "(A) equalizes …… (B) salty", "(A) increases …… (B) frozen"], 3,
      "(A) This equalizes the concentration of materials on either side of the membrane — 농도를 ‘같게 만든다’. (B) remove salt … Afterward, we can drink the water! — 소금을 빼면 마실 수 있게(drinkable) 된다. 소금을 뺐는데 ‘짜게’ 된다는 것은 모순이다."),
]),
# ───────────────────────────── Unit 7 (Set C) ─────────────────────────────
dict(key="u7", set="C", title="Unit 7 · Social Studies — Majority Rule in Democracies",
passage="""People usually make tough decisions by voting for one of two or more options. The option that gets the most votes is the winner. This is called majority rule. However, even if only 51% of people in a group vote for an option, they will get their choice. That means, almost half of the people in that group will not get their choice. In that case, is majority rule really fair?

Most democracies elect public officials through a majority vote. In a system with two political parties, a slim margin, such as 51% to 49%, can decide an election. In a system with more than two parties, less than 50% of voters could give one political party a victory. To ensure the ______ of majority rule, certain conditions must be met. First, people should be able to vote with secret ballots. Second, each person’s vote should be weighted equally. Finally, there have to be enough voters to make a majority vote truly fair.

When an election is won with less than 50% of the total votes, the winning party must consider the opinions of the other voters. This is because running a democracy should ensure equality for all citizens.""",
items=[
 item(1, "세부 사실", "윗글에 따르면, majority rule(다수결)에서 승자가 되는 것은?",
      "the option that gets the most votes",
      ["the option chosen by the oldest voter", "the option that every single person agrees on", "the option the president likes best", "the option that gets the fewest votes"], 3,
      "The option that gets the most votes is the winner. This is called majority rule. 가장 많은 표를 얻은 선택지가 이긴다."),
 item(2, "문장 빈칸 어휘", "윗글의 빈칸에 들어갈 말로 가장 적절한 것은?",
      "fairness", ["victory", "speed", "price", "size"], 4,
      "앞 문단 끝의 is majority rule really fair?와 뒤의 to make a majority vote truly fair가 단서이다. 다수결의 ‘공정성’(fairness)을 보장하기 위해 조건이 필요하다는 뜻이다. victory(승리)·speed(속도)·price(가격)·size(크기)는 이 문맥과 맞지 않는다."),
 item(3, "주제", "윗글의 주제로 가장 적절한 것은?",
      "majority rule and the conditions that make it fair",
      ["how to become a public official", "the history of political parties", "why people should not vote in elections", "the fastest way to count votes"], 1,
      "다수결의 뜻과 한계(거의 절반이 원하는 것을 얻지 못함), 그리고 공정한 다수결을 위한 세 가지 조건을 설명하는 글이다."),
 item(4, "내용 일치", "윗글의 내용과 일치하는 것은?",
      "With more than two parties, a party can win with less than 50% of the votes.",
      ["In majority rule, the winner always gets more than 90% of the votes.", "Most democracies choose public officials by drawing lots.", "Each person’s vote should be weighted differently.", "A winning party does not need to think about other voters."], 5,
      "In a system with more than two parties, less than 50% of voters could give one political party a victory. 51%만 얻어도 이기므로 ‘항상 90% 이상’은 틀리고, 공직자는 ‘다수결 투표’로 뽑으며, 표는 ‘동등하게’(equally) 반영되어야 하고, 이긴 정당은 다른 유권자의 의견을 ‘고려해야’(must consider) 한다."),
 item(5, "글쓴이의 주장", "윗글의 글쓴이가 가장 동의할 만한 것은?",
      "Majority rule needs certain conditions to be truly fair.",
      ["Majority rule is always perfectly fair.", "Secret ballots make elections less fair.", "Winners should ignore people who voted for other parties.", "A democracy should have only one political party."], 2,
      "글쓴이는 다수결이 정말 공정한지 묻고, 공정성을 보장하려면 비밀 투표·동등한 표·충분한 유권자라는 조건이 필요하다고 했다. ‘항상 완벽히 공정하다’는 글의 문제 제기와 반대이고, 비밀 투표는 공정성의 조건이며, 이긴 쪽은 다른 유권자의 의견을 고려해야 하고, 정당이 둘 이상인 경우를 전제로 설명한다."),
]),
# ───────────────────────────── Unit 8 (Set D) ─────────────────────────────
dict(key="u8", set="D", title="Unit 8 · Science — The Rising Prominence of Telescopes",
passage="""The invention of the telescope has helped humans see and understand the stars better. How have telescopes changed over time?

Telescopes were originally used to see long distances. Galileo was one of the first to use a telescope to observe the stars. His telescope used a concave eyepiece and a convex lens. This gave the image seen through the telescope an upright view and magnified it up to thirty times! Even though Galileo’s telescope was quite useful at the time, the images it produced were blurry. Kepler improved on Galileo’s design by using a convex eyepiece and lens. This gave a much wider field of view, even though the images appeared upside-down.

In modern times, telescopes have been launched into space to help astronomers ______. One example is the Hubble Telescope, which orbits Earth and sends back high-quality pictures of distant planets and galaxies. Through continued technological developments, humans can understand the universe much better.""",
items=[
 item(1, "세부 사실", "윗글에 따르면, Galileo의 망원경은 이미지를 최대 몇 배까지 확대했는가?",
      "thirty times", ["three times", "five times", "ten times", "twenty times"], 5,
      "… and magnified it up to thirty times! 최대 30배까지 확대했다."),
 item(2, "영영풀이 어휘", VOC + "\n\n“a scientist who studies the stars, planets, and other natural objects in space”",
      "astronomer", ["dentist", "architect", "farmer", "pilot"], 2,
      "astronomer(천문학자). … to help astronomers … dentist(치과 의사), architect(건축가), farmer(농부), pilot(조종사)."),
 item(3, "도표 완성", TBLQ,
      "(A) concave …… (B) upside-down",
      ["(A) convex …… (B) upside-down", "(A) concave …… (B) blurry", "(A) convex …… (B) upright", "(A) concave …… (B) clear"], 3,
      "(A) His telescope used a concave eyepiece and a convex lens — Galileo의 접안렌즈는 오목(concave). (B) Kepler의 망원경은 시야가 넓어진 대신 the images appeared upside-down — 거꾸로 보였다. blurry(흐릿한)는 Galileo 망원경의 단점이다.",
      table=[["", "*Galileo’s telescope*", "*Kepler’s telescope*"],
             ["eyepiece", "(A) ______", "convex"],
             ["lens", "convex", "convex"],
             ["images", "upright, but blurry", "wider field of view, but (B) ______"]]),
 item(4, "제목", "윗글의 제목으로 가장 적절한 것은?",
      "How Telescopes Have Changed over Time",
      ["How to Make Your Own Telescope", "The Life and Death of Galileo", "Why People Used the Stars as Maps", "A Day in the Life of the Hubble Telescope"], 4,
      "1문단의 질문 How have telescopes changed over time?에 따라 Galileo → Kepler → Hubble로 이어지는 망원경의 변화를 설명하는 글이다. 망원경 제작법, Galileo의 생애, 별을 지도로 쓴 이유, Hubble의 하루는 글의 내용이 아니다."),
 item(5, "빈칸 추론", "윗글의 빈칸에 들어갈 말로 가장 적절한 것은?",
      "observe not only the stars but also the universe",
      ["see long distances on the ground", "take blurry pictures of the Moon", "fix the problems of Kepler’s telescope", "travel to distant planets"], 1,
      "빈칸 뒤의 예(Hubble Telescope)가 지구 궤도를 돌며 먼 행성과 은하의 고화질 사진을 보내온다고 했고, 마지막 문장에서 인간이 ‘우주’를 더 잘 이해하게 되었다고 했다. 따라서 우주 망원경의 목적은 별뿐 아니라 우주를 관측하는 것이다. 먼 거리를 보는 것은 망원경의 ‘원래’ 용도이고, 흐릿한 사진·Kepler 망원경 수리·행성 여행은 근거가 없다."),
]),
]

PAIR = {"A": "1·5 (Art)", "B": "2·6 (Nature)", "C": "3·7 (Social Studies)", "D": "4·8 (Science)"}


def build():
    sections, blueprint, qno = [], [], 0
    for u in UNITS:
        items = [{"type": "passage", "title": f"[{qno+1}~{qno+5}] 다음 글을 읽고 물음에 답하시오.", "text": u["passage"]}]
        assert [it["_lv"] for it in u["items"]] == [1, 2, 3, 4, 5]
        for it in u["items"]:
            qno += 1
            blueprint.append((qno, u["key"].upper(), u["set"], it["_lv"], it["_kind"], it["answer"]))
            items.append({k: v for k, v in it.items() if not k.startswith("_")})
        sections.append({"title": u["title"], "items": items})
    # 유형 쌍 일치 확인
    kinds = {u["key"]: [it["_kind"] for it in u["items"]] for u in UNITS}
    for a, b in (("u1", "u5"), ("u2", "u6"), ("u3", "u7"), ("u4", "u8")):
        assert kinds[a] == kinds[b], (a, b)
    dist = Counter(b[5] for b in blueprint)
    assert qno == 40 and set(dist.values()) == {8}, dist
    doc = {
        "title": "The Reading 7-1 Final Test",
        "meta": {"subject": "영어 독해", "grade": "Level 7 (중1 수준)", "unit": "Unit 1~8", "time_limit": "50분"},
        "student_fields": ["반", "이름", "점수"],
        "instructions": [
            "40문항 · 5지선다 · 문항당 2.5점(100점 만점) · *70점(28문항) 이상 합격* · 답은 하나만 고르세요.",
        ],
        "layout": {"columns": 1, "font_size": 9.5, "show_points": True, "choice_columns": 0, "section_pagebreak": True},
        "sections": sections,
    }
    return doc, blueprint, kinds


def blueprint_md(blueprint, kinds):
    lines = ["# The Reading 7-1 Final Test · 문항 구성표", "",
             "40문항 · 5지선다 · 문항당 2.5점 · 100점 만점 · 70점(28문항) 이상 합격", "",
             "## 유형 설계 (단원 쌍끼리 동일)", "", "| 쌍 | 1 | 2 | 3 | 4 | 5 |", "|---|---|---|---|---|---|"]
    for s, (a, _) in zip("ABCD", (("u1", "u5"), ("u2", "u6"), ("u3", "u7"), ("u4", "u8"))):
        lines.append(f"| {PAIR[s]} | " + " | ".join(kinds[a]) + " |")
    lines += ["", "## 난이도와 목표 정답률", "", "| 난이도 | 설명 | 예상 정답률(중1 평균) |", "|---|---|---|"]
    for lv in range(1, 6):
        lines.append(f"| {lv} | {LEVEL[lv]} | {int(EXPECTED_P[lv]*100)}% |")
    mean = sum(EXPECTED_P.values()) / 5 * 100
    lines += ["", f"예상 평균 점수 약 {mean:.0f}점. 학급 표준편차를 12점으로 가정하면 70점 이상이 약 70~75%가 되도록 설계했다. "
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
