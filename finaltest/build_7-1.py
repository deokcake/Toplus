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
      "critic", ["gallery", "career", "object", "advertisement"], 3,
      "critic(비평가): 책·영화·음악·미술에 대해 글을 쓰고 의견을 밝히는 사람. 3문단 Some critics think … 에서 쓰였다. gallery(미술관), career(경력), object(사물), advertisement(광고)는 모두 사람이 아니다."),
 item(2, "세부 사실", "윗글에 따르면, Andy Warhol이 어린 시절 그림을 많이 그린 이유로 가장 적절한 것은?",
      "He was not healthy as a child.",
      ["He wanted to become a famous artist.", "His parents were famous artists.", "He wanted to sell his drawings.", "He had a special art teacher."], 2,
      "2문단 첫 문장 Andy Warhol was often sick as a child, so he spent a lot of time drawing. 어릴 때 자주 아팠기(was often sick = was not healthy) 때문이다. 화가가 되고 싶었다, 부모가 화가였다, 그림을 팔려 했다, 특별한 미술 선생님이 있었다는 내용은 본문에 없다."),
 item(3, "지칭 추론", "윗글의 밑줄 친 ⟪These⟫가 가리키는 것으로 가장 적절한 것은?",
      "Warhol’s art pieces that show everyday objects",
      ["the advertisements Warhol made after college", "the art galleries that showed his works", "Warhol’s early drawings of shoes", "the critics who wrote about Warhol"], 1,
      "바로 앞 문장의 many famous art pieces depicting everyday objects(일상 사물을 그린 유명 작품들)를 받는다. 이어서 그 예로 Coca-Cola bottles, dollar bills, Campbell’s Soup cans가 나온다."),
 item(4, "사건 순서 배열", ORDQ,
      "(D) – (B) – (A) – (C)",
      ["(B) – (D) – (A) – (C)", "(D) – (A) – (B) – (C)", "(D) – (B) – (C) – (A)", "(B) – (A) – (C) – (D)"], 5,
      "어릴 때 그림을 많이 그림(D) → 대학 졸업 후 광고 미술로 경력 시작(B) → 1950년대 미술관에서 작품 전시(A) → 1960년대 일상 사물을 그린 작품 제작(C). 2문단의 흐름 그대로이다.",
      box="(A) Warhol began showing his works in art galleries. \\\n(B) Warhol began making art for advertisements. \\\n(C) Warhol produced art pieces depicting everyday objects. \\\n(D) Warhol spent a lot of time drawing as a child."),
 item(5, "추론", "윗글을 통해 추론할 수 있는 것으로 가장 적절한 것은?",
      "Warhol’s work in advertising helped him become famous as an artist.",
      ["Warhol stopped making art after he became famous.", "All critics agreed that Warhol only wanted to make money.", "Warhol was the person who invented silkscreen ink printing.", "Commercial art was more popular in the past than it is today."], 4,
      "광고 미술로 경력을 시작한 뒤 그린 신발 그림이 유명해져 사람들이 그의 작품을 더 보고 싶어 했고, ‘그래서(Thus)’ 1950년대에 미술관에서 전시를 시작했다고 했다. 따라서 광고 일이 그가 화가로 유명해지는 계기가 되었음을 추론할 수 있다. 유명해진 뒤 작업을 멈췄다는 내용은 없고(1960년대에도 많은 작품을 만들었다), 비평가 의견은 갈렸으며(Some critics … Others …), 실크스크린은 ‘처음 사용한 화가 중 한 명’이지 발명자가 아니고, 광고 미술은 점점 인기를 얻고 있다(increasingly popular)."),
]),
# ───────────────────────────── Unit 2 (Set B) ─────────────────────────────
dict(key="u2", set="B", title="Unit 2 · Nature — The Water Cycle Keeps Earth Balanced",
passage="""The water cycle is necessary for life on Earth. Water on the ground evaporates into vapor and forms clouds in the sky. In return, rain brings water back down to the ground again, which ends up in streams, rivers, lakes, and oceans. What happens when humans tamper with the water cycle?

Most evaporation occurs in oceans as a result of the Sun’s energy. This cools the temperature of Earth’s climate and also affects the oceans’ salt content. Having the correct amount of salt in the oceans ⟪maintains⟫ a delicate ecosystem of plants, fish, and other wildlife. One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. The two rivers that fed the Aral Sea were diverted for farming in the desert. As a result, the sea is now almost completely dry, killing the wildlife that lived there and causing dust storms that affect human health.

As we can see, the water cycle is necessary to keep the environment balanced.""",
items=[
 item(1, "문맥상 동의어", "윗글의 밑줄 친 ⟪maintains⟫와 의미가 가장 가까운 것은?",
      "keeps", ["breaks", "loses", "sells", "finds"], 1,
      "maintain은 ‘(상태를) 유지하다’. 알맞은 양의 소금이 생태계를 ‘유지한다’는 뜻이므로 keeps가 가장 가깝다."),
 item(2, "세부 사실", "윗글에 따르면, Aral Sea로 흘러들던 두 강의 물길을 바꾼 목적은?",
      "to farm in the desert", ["to build a new city", "to make electricity", "to stop dust storms", "to protect wildlife"], 4,
      "The two rivers that fed the Aral Sea were diverted for farming in the desert. 사막에서 농사를 짓기 위해서였다. 도시 건설과 발전은 언급되지 않았고, 황사와 야생동물은 물길을 바꾼 ‘결과’(killing the wildlife … causing dust storms)로 나오므로 ‘목적’이 될 수 없다."),
 item(3, "언급 이유", "글쓴이가 Aral Sea를 언급한 이유로 가장 적절한 것은?",
      "물의 순환을 함부로 건드리면 생기는 재앙의 예를 들기 위해",
      ["사막에서 농사짓는 방법을 소개하기 위해", "바다의 소금이 생기는 과정을 설명하기 위해", "세계에서 가장 큰 호수를 소개하기 위해", "증발이 기후를 식히는 원리를 보여 주기 위해"], 2,
      "One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. 물의 순환을 건드려서 생긴 재앙의 ‘예’로 든 것이다."),
 item(4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
      "Most evaporation happens in rivers and lakes.",
      ["Rain brings water back down to the ground.", "Evaporation affects the salt content of the oceans.", "The Aral Sea is now almost completely dry.", "Dust storms from the Aral Sea affect human health."], 3,
      "Most evaporation occurs in oceans — 증발은 대부분 ‘바다’에서 일어난다. 나머지는 각각 In return, rain brings water back down / affects the oceans’ salt content / almost completely dry / dust storms that affect human health 와 일치한다."),
 item(5, "요약문 완성", SUMQ + "\n\nThe Sun’s energy makes water evaporate. This stops Earth’s climate from getting too (A) ______. The right amount of salt in the oceans also lets plants, fish, and other wildlife (B) ______.",
      "(A) hot …… (B) live",
      ["(A) cold …… (B) die", "(A) hot …… (B) die", "(A) wet …… (B) move", "(A) cold …… (B) live"], 5,
      "(A) This cools the temperature of Earth’s climate — 증발이 기후를 ‘식힌다’는 것은 지구가 너무 ‘뜨거워지지(hot)’ 않게 막는다는 뜻이다. 지문의 cools만 보고 cold를 고르면 뜻이 반대가 된다. (B) maintains a delicate ecosystem of plants, fish, and other wildlife — 알맞은 소금 양이 생태계를 유지하므로 생물이 ‘살(live)’ 수 있다. 생물이 죽거나(die) 이동한다(move)는 것은 지문에 없다."),
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
      "how Slow Cities began and what they are like",
      ["the dangers of eating too much fast food", "the best Slow Cities to visit in Italy", "how to open a small restaurant in a Slow City", "why big supermarkets are popular in Slow Cities"], 3,
      "슬로푸드 운동에서 시작된 슬로시티 운동의 유래·목표와 오늘날 슬로시티의 모습을 설명하는 글이다. 패스트푸드의 위험이나 식당 창업 방법은 다루지 않고, 글에 나온 슬로시티는 Chianti 하나뿐이어서 ‘가 볼 만한 도시들’을 소개한 글이 아니며, 대형 마트는 슬로시티에 ‘없다’고 했다."),
 item(4, "내용 일치", "윗글의 내용과 일치하는 것은?",
      "Slow Cities have small markets and locally owned restaurants instead of big supermarkets.",
      ["The slow food movement started in the 1990s.", "The slow city movement inspired the slow food movement.", "Cittaslow is the name of a historic building in Italy.", "Only two cities have been named Slow Cities since 1999."], 1,
      "Slow Cities do not have many fast-food restaurants … Instead, they have locally owned restaurants and small markets. 슬로푸드 운동은 1980년대에 시작했고, 슬로푸드가 슬로시티에 영감을 준 것이며(This inspired …), cittaslow는 마을 개발 ‘계획’의 이름이고, 1999년 이후 ‘수십 개’(dozens of) 도시가 지정되었다."),
 item(5, "글쓴이의 주장", "윗글의 글쓴이가 가장 동의할 만한 것은?",
      "A town can develop without harming nature or people’s health.",
      ["Fast food is the best way to feed a busy city.", "Big supermarkets help neighbors build good relationships.", "A Slow City should not allow any new development.", "Only towns in Italy can become Slow Cities."], 4,
      "cittaslow의 원칙: 새 개발(new developments)은 사람을 건강하게 하고 이웃 관계를 좋게 하며 자연환경을 해치지 않아야 한다. 글쓴이는 이를 긍정적으로 소개하고 방문까지 권한다. 패스트푸드가 최선이라는 것과 대형 마트가 이웃 관계를 좋게 한다는 것은 글의 취지와 반대이고, 새 개발을 아예 허용하지 말아야 한다는 것은 ‘새 개발은 ~해야 한다’는 원칙(개발 자체는 인정)과 어긋나며, 이탈리아 마을만 될 수 있다는 것은 dozens of cities around the world와 맞지 않는다."),
]),
# ───────────────────────────── Unit 4 (Set D) ─────────────────────────────
dict(key="u4", set="D", title="Unit 4 · Science — The Theory of the Four Elements",
passage="""Before modern chemistry, ancient people tried to understand the makeup of the world. The ancient Greek philosopher Empedocles theorized that four elements made up every substance known to man. These elements were water, fire, earth, and air.

What observations did Empedocles make about these elements? First, he noted that pots were made with earth and water. After being mixed and shaped, they were burned with fire and cooled with air. All four elements were necessary to make one pot. The same pot was used for cooking plants from the earth, often mixed with water, over a flame. The air cooled down the food so it could be eaten. Thus, all four elements were necessary to ______. Empedocles also believed that these elements were indestructible and unchangeable. His theories inspired later scientists to study more about the elements that make up our world.""",
items=[
 item(1, "세부 사실", "윗글에서 Empedocles가 말한 네 가지 원소에 해당하지 *않는* 것은?",
      "wood", ["water", "fire", "earth", "air"], 4,
      "These elements were water, fire, earth, and air. 나무(wood)는 네 원소에 들어 있지 않다."),
 item(2, "영영풀이 어휘", VOC + "\n\n“so strong that it cannot be broken or damaged”",
      "indestructible", ["ancient", "delicious", "modern", "necessary"], 1,
      "indestructible(파괴할 수 없는) = in-(아닌) + destruct(파괴하다) + -ible(할 수 있는). Empedocles also believed that these elements were indestructible … ancient(고대의), delicious(맛있는), modern(현대의), necessary(필요한)."),
 item(3, "도표 완성", TBLQ,
      "(A) fire …… (B) air",
      ["(A) air …… (B) fire", "(A) fire …… (B) water", "(A) water …… (B) air", "(A) earth …… (B) fire"], 5,
      "The same pot was used for cooking plants … over a flame. — 불꽃(flame) 위에서 요리하므로 (A)는 fire. The air cooled down the food so it could be eaten. — 음식을 식힌 것은 (B) air. 지문의 flame을 fire로 바꿔 읽어야 한다.",
      table=[["*Element*", "*Cooking with the Pot*"],
             ["earth", "Plants come from it."],
             ["water", "The plants are often mixed with it."],
             ["(A) ______", "The plants are cooked over a flame."],
             ["(B) ______", "It cools down the food so it can be eaten."]]),
 item(4, "제목", "윗글의 제목으로 가장 적절한 것은?",
      "Empedocles’s Theory of the Four Elements",
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
 item(1, "영영풀이 어휘", VOC + "\n\n“to say that you will not do something, or that you will not take something someone gives you”",
      "refuse", ["kill", "tie", "hear", "make"], 5,
      "refuse(거절하다, 거부하다). Roosevelt refused to kill a bear … kill(죽이다), tie(묶다), hear(듣다), make(만들다)는 모두 1문단에 나오는 동사이지만 뜻이 다르다."),
 item(2, "세부 사실", "윗글에 따르면, ‘teddy bear’라는 이름은 누구의 별명에서 나왔는가?",
      "the president of the United States",
      ["a famous toy maker", "the writer of Winnie the Pooh", "the man who tied the bear to a tree", "a museum owner in Japan"], 3,
      "It comes from U.S. president Theodore Roosevelt. … in honor of the president’s nickname, Teddy. 곰을 나무에 묶은 사람이 누구인지는 글에 나오지 않는다."),
 item(3, "지칭 추론", "윗글의 밑줄 친 ⟪this story⟫가 가리키는 내용으로 가장 적절한 것은?",
      "Roosevelt refused to kill a bear that was tied to a tree.",
      ["Roosevelt became the president of the United States.", "Some people made stuffed bears and named them “teddy bears.”", "Winnie the Pooh was originally written for adults.", "A bear ran away from the hunters during a hunting trip."], 4,
      "바로 앞 문장 During a hunting trip, Roosevelt refused to kill a bear that had been tied to a tree. 이 이야기를 미국 전역의 사람들이 들은 것이다. 곰 인형 제작은 그 ‘뒤’의 일이고, 곰이 도망쳤다는 내용은 없다."),
 item(4, "사건 순서 배열", ORDQ,
      "(B) – (A) – (D) – (C)",
      ["(A) – (B) – (D) – (C)", "(B) – (D) – (A) – (C)", "(B) – (A) – (C) – (D)", "(D) – (B) – (A) – (C)"], 2,
      "사냥 여행에서 곰을 죽이지 않음(B) → 그 이야기가 미국 전역에 퍼짐(A) → 사람들이 곰 인형을 만들어 teddy bear라 부름(D) → 20세기에 대량 생산됨(C). 1문단에서 2문단으로 이어지는 순서이다.",
      box="(A) People all over America heard about the story. \\\n(B) Roosevelt refused to kill a bear on a hunting trip. \\\n(C) Teddy bears became mass-produced in the twentieth century. \\\n(D) Some people made stuffed bears and called them “teddy bears.”"),
 item(5, "추론", "윗글을 통해 추론할 수 있는 것으로 가장 적절한 것은?",
      "People respected Roosevelt for not killing the bear.",
      ["Teddy bears were popular only in America.", "Roosevelt made the first teddy bear himself.", "Teddy bears will soon lose their popularity.", "Most teddy bears were made for adults, not children."], 1,
      "사람들이 이야기를 듣고 대통령을 ‘기리기 위해’(in honor of) 곰 인형에 그의 별명을 붙였으므로, 곰을 죽이지 않은 그를 존경했음을 추론할 수 있다. 박물관이 세계 곳곳에 있으니 미국에서만 인기였던 것이 아니고, 인형을 만든 것은 ‘some people’이며, 앞으로도 오래 사랑받을 것이라 했고, 곰 인형은 ‘주로 아이들의 장난감’(mainly toys for children)이었다."),
]),
# ───────────────────────────── Unit 6 (Set B) ─────────────────────────────
dict(key="u6", set="B", title="Unit 6 · Nature — Osmosis in Everyday Life",
passage="""Molecules are always moving. Sometimes, molecules even move through membranes. Molecules tend to pass through semi-permeable membranes to an area where the solvent concentration is higher. This equalizes the concentration of materials on either side of the membrane. This process is called osmosis. Osmosis is an important chemical process with practical uses in everyday life. What is one use of osmosis?

Fresh vegetables have a high concentration of water molecules. During pickling, vegetables are placed in a brine—a mixture of water, salt, and seasonings. The skin acts as a semi-permeable membrane. Water molecules move out of the vegetables through the skin and into the brine, which equalizes the solvent concentration on either side of the membrane. This process is an example of osmosis, and it is why pickled vegetables stay crunchy.

Reverse osmosis is a process that uses pressure to force molecules into an area of lower solute concentration. We use reverse osmosis to ⟪remove⟫ salt and other particles from seawater. Afterward, we can drink the water!""",
items=[
 item(1, "문맥상 동의어", "윗글의 밑줄 친 ⟪remove⟫와 의미가 가장 가까운 것은?",
      "take out", ["put in", "mix up", "heat up", "pick up"], 1,
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
      "Pickled vegetables become soft in the brine.",
      ["Molecules are always moving.", "The skin of a vegetable acts as a semi-permeable membrane.", "During pickling, water moves out of the vegetables into the brine.", "Reverse osmosis uses pressure to remove salt from seawater."], 4,
      "it is why pickled vegetables stay crunchy — 삼투 덕분에 피클은 ‘아삭함을 유지’한다. 나머지는 Molecules are always moving / The skin acts as a semi-permeable membrane / Water molecules move out of the vegetables … into the brine / uses pressure … remove salt 와 일치한다."),
 item(5, "요약문 완성", SUMQ + "\n\nOsmosis makes the concentration on both sides of a membrane (A) ______. Reverse osmosis is the (B) ______ of osmosis, and we use it to make seawater drinkable.",
      "(A) the same …… (B) opposite",
      ["(A) higher …… (B) opposite", "(A) the same …… (B) example", "(A) higher …… (B) example", "(A) lower …… (B) result"], 3,
      "(A) This equalizes the concentration of materials on either side of the membrane — 막 양쪽의 농도를 ‘같게(the same)’ 만든다. 분자가 농도가 높은 쪽으로 이동한다고 했을 뿐, 양쪽 농도가 높아지거나 낮아진다고 하지 않았다. (B) 역삼투(reverse osmosis)는 압력으로 분자를 농도가 낮은 쪽으로 억지로 밀어 넣는, 삼투의 ‘반대(opposite)’ 과정이다. 삼투의 ‘예(example)’는 피클 만들기이고, 역삼투는 삼투의 ‘결과(result)’가 아니다."),
]),
# ───────────────────────────── Unit 7 (Set C) ─────────────────────────────
dict(key="u7", set="C", title="Unit 7 · Social Studies — Majority Rule in Democracies",
passage="""People usually make tough decisions by voting for one of two or more options. The option that gets the most votes is the winner. This is called majority rule. However, even if only 51% of people in a group vote for an option, they will get their choice. That means, almost half of the people in that group will not get their choice. In that case, is majority rule really fair?

Most democracies elect public officials through a majority vote. In a system with two political parties, a slim margin, such as 51% to 49%, can decide an election. In a system with more than two parties, less than 50% of voters could give one political party a victory. To ensure the ______ of majority rule, certain conditions must be met. First, people should be able to vote with secret ballots. Second, each person’s vote should be weighted equally. Finally, there have to be enough voters to make a majority vote truly fair.

When an election is won with less than 50% of the total votes, the winning party must consider the opinions of the other voters. This is because running a democracy should ensure equality for all citizens.""",
items=[
 item(1, "세부 사실", "윗글에 따르면, majority rule(다수결)에서는 어떤 선택지가 승자가 되는가?",
      "the option that gets the most votes",
      ["the option chosen by the oldest voter", "the option that every single person agrees on", "the option the president likes best", "the option that gets the fewest votes"], 3,
      "The option that gets the most votes is the winner. This is called majority rule. 가장 많은 표를 얻은 선택지가 이긴다."),
 item(2, "문장 빈칸 어휘", "윗글의 빈칸에 들어갈 말로 가장 적절한 것은?",
      "fairness", ["victory", "speed", "price", "size"], 4,
      "앞 문단 끝의 is majority rule really fair?와 뒤의 to make a majority vote truly fair가 단서이다. 다수결의 ‘공정성’(fairness)을 보장하기 위해 조건이 필요하다는 뜻이다. victory(승리)·speed(속도)·price(가격)·size(크기)는 이 문맥과 맞지 않는다."),
 item(3, "주제", "윗글의 주제로 가장 적절한 것은?",
      "majority rule and how to make it fair",
      ["how a slim margin decides a two-party election", "the history of majority rule in democracies", "why secret ballots are needed in every democracy", "the duties of public officials in a democracy"], 1,
      "다수결의 뜻과 한계(거의 절반이 원하는 것을 얻지 못함), 공정한 다수결을 위한 세 가지 조건, 그리고 이긴 쪽이 가져야 할 태도까지 설명하는 글이다. 근소한 차이의 선거와 비밀 투표는 글의 일부 내용만 담은 너무 좁은 주제이고, 다수결의 역사와 공직자의 의무는 글에 없다."),
 item(4, "내용 일치", "윗글의 내용과 일치하는 것은?",
      "With more than two parties, a party can win with less than 50% of the votes.",
      ["In majority rule, the winner always gets more than 90% of the votes.", "Most democracies choose public officials without any voting.", "Each person’s vote should be weighted differently.", "A winning party does not need to think about other voters."], 5,
      "In a system with more than two parties, less than 50% of voters could give one political party a victory. 51%만 얻어도 이기므로 ‘항상 90% 이상’은 틀리고, 공직자는 ‘다수결 투표’로 뽑으며, 표는 ‘동등하게’(equally) 반영되어야 하고, 이긴 정당은 다른 유권자의 의견을 ‘고려해야’(must consider) 한다."),
 item(5, "글쓴이의 주장", "윗글의 글쓴이가 가장 동의할 만한 것은?",
      "Getting the most votes does not always make a decision fair for everyone.",
      ["The more voters there are, the less fair a majority vote becomes.", "A party that wins with less than 50% of the votes may ignore the other voters.", "A leader’s vote should count more than an ordinary citizen’s vote.", "People should vote where everyone can see their choice."], 2,
      "글쓴이는 51%만 얻어도 이기므로 거의 절반이 원하는 것을 얻지 못한다며 ‘다수결이 정말 공정한가’를 묻고, 이긴 정당은 다른 유권자의 의견을 고려해야 하며 민주주의는 모든 시민의 평등을 보장해야 한다고 했다. 따라서 표를 가장 많이 얻었다고 해서 그 결정이 모두에게 공정한 것은 아니라는 데 동의할 것이다. 유권자가 많을수록 덜 공정하다는 것은 enough voters 조건과 반대이고, 50% 미만으로 이긴 정당이 다른 유권자를 무시해도 된다는 것은 must consider the opinions of the other voters와 반대이며, 지도자의 표가 더 무거워야 한다는 것은 weighted equally와, 남이 보는 앞에서 투표해야 한다는 것은 secret ballots와 어긋난다."),
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
      "astronomer", ["invention", "eyepiece", "galaxy", "development"], 2,
      "astronomer(천문학자). … to help astronomers … invention(발명), eyepiece(접안렌즈), galaxy(은하), development(발전)은 모두 사람이 아니다."),
 item(3, "도표 완성", TBLQ,
      "(A) concave …… (B) upside-down",
      ["(A) convex …… (B) upside-down", "(A) concave …… (B) blurry", "(A) convex …… (B) upright", "(A) concave …… (B) clear"], 3,
      "(A) His telescope used a concave eyepiece and a convex lens — Galileo의 접안렌즈는 오목(concave). (B) Kepler의 망원경은 시야가 넓어진 대신 the images appeared upside-down — 거꾸로 보였다. blurry(흐릿한)는 Galileo 망원경의 단점이다.",
      table=[["", "*Galileo’s telescope*", "*Kepler’s telescope*"],
             ["eyepiece", "(A) ______", "convex"],
             ["lens", "convex", "convex"],
             ["images", "upright, but blurry", "wider field of view, but (B) ______"]]),
 item(4, "제목", "윗글의 제목으로 가장 적절한 것은?",
      "Telescopes: From Galileo to Hubble",
      ["How to Make Your Own Telescope", "Galileo: The First Man to Use a Telescope", "The Hubble Telescope: Pictures from Space", "Why Kepler’s Telescope Was Not Useful"], 4,
      "1문단의 질문 How have telescopes changed over time?에 답하여 Galileo → Kepler → Hubble로 이어지는 망원경의 발전을 설명하는 글이므로, 전체를 아우르는 제목은 ‘Galileo에서 Hubble까지’이다. Galileo나 Hubble만 다룬 제목은 글의 일부에 그쳐 너무 좁고(Galileo는 ‘처음 사용한 사람 중 한 명’일 뿐이기도 하다), 망원경 제작법은 글에 없으며, Kepler의 망원경은 Galileo의 설계를 ‘개선한’ 것이므로 쓸모없었다는 제목은 글과 어긋난다."),
 item(5, "빈칸 추론", "윗글의 빈칸에 들어갈 말로 가장 적절한 것은?",
      "observe not only the stars but also the universe",
      ["see long distances on the ground more clearly", "take pictures of the Moon from the ground", "fix the problems of Kepler’s telescope design", "travel to distant planets and galaxies"], 1,
      "빈칸 뒤의 예(Hubble Telescope)가 지구 궤도를 돌며 먼 행성과 은하의 고화질 사진을 보내온다고 했고, 마지막 문장에서 인간이 ‘우주’를 더 잘 이해하게 되었다고 했다. 따라서 우주 망원경의 목적은 별뿐 아니라 우주를 관측하는 것이다. 지상에서 먼 거리를 보거나 지상에서 달 사진을 찍는 것은 ‘우주로 발사되었다’는 내용과 어긋나고(먼 거리를 보는 것은 망원경의 ‘원래’ 용도이다), Kepler 망원경 수리와 행성 여행은 근거가 없다."),
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
        sections.append({"title": u["title"].split(" — ")[0], "items": items})
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
