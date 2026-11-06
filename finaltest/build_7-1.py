"""The Reading 7-1 Final Test — 문항 원본 데이터 → exam-worksheet JSON + 문항구성표.

대상: The Reading Level 7을 배운 초등학교 6학년 (평균 학생의 70%가 70점 이상 합격하도록 설계)

유형 설계: 단원 쌍(1·5, 2·6, 3·7, 4·8)끼리 같은 5개 유형을 쓰고,
각 단원 안에서 1번→5번으로 갈수록 어려워진다.

  Set A (1·5 Art)      : 어휘(단어 뜻) → 세부 사실 → 지칭 추론 → 사건 순서 배열 → 추론
  Set B (2·6 Nature)   : 문맥상 동의어 → 세부 사실 → 언급 이유 → 내용 불일치 → 요약문 (A)(B)
  Set C (3·7 Social)   : 세부 사실 → 문장 빈칸 어휘 → 주제 → 내용 일치 → 글쓴이의 주장
  Set D (4·8 Science)  : 세부 사실 → 어휘(단어 뜻) → 도표 완성 (A)(B) → 제목 → 빈칸 추론

초6 눈높이 장치:
  - 이해를 묻는 문항(세부·지칭·순서·추론·언급 이유·일치/불일치·주제·제목·주장)은 선택지를 한국어로 쓴다.
  - 어휘 문항은 영영풀이 대신 밑줄 친 단어의 한국어 뜻을 고른다.
  - 사건 순서 배열은 사건 3개만 쓴다.
  - 지문 아래에 시험에 나오지 않는 어려운 단어의 뜻을 달아 준다 (GLOSS = False 로 끌 수 있음).

표기: 지문·발문 속 ⟪단어⟫ 는 밑줄, ______ 는 빈칸 상자로 조판된다.
"""
import json
import sys
from collections import Counter
from pathlib import Path

GLOSS = True
LEVEL = {1: "매우 쉬움", 2: "쉬움", 3: "보통", 4: "다소 어려움", 5: "어려움"}
EXPECTED_P = {1: 0.97, 2: 0.92, 3: 0.85, 4: 0.77, 5: 0.65}  # 초6 평균 학생 기준 예상 정답률

SUMQ = "다음은 윗글을 요약한 것이다. 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?"
ORDQ = "다음 (A)~(C)를 윗글에서 일어난 순서대로 바르게 배열한 것은?"
TBLQ = "다음은 윗글의 내용을 정리한 표이다. 빈칸 (A), (B)에 들어갈 말로 가장 알맞은 것은?"
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
passage="""Art in advertisements has become increasingly popular. This is called commercial art. One of the most famous commercial artists was Andy Warhol.

Andy Warhol was often sick as a child, so he spent a lot of time drawing. After college, he began his career making art for advertisements. His drawings of shoes became so well known that people wanted to see more of his work. Thus, in the 1950s, he began showing his popular works in art galleries. Warhol was one of the first artists to use silkscreen ink printing in his work. During the 1960s, he produced many famous art pieces depicting everyday objects. ⟪These⟫ include Coca-Cola bottles, dollar bills, and Campbell’s Soup cans. This kind of art is referred to as “pop art.”

Some ⟪critics⟫ think Andy Warhol was only interested in making money with his art. Others thought he was the perfect example of commercialized modern life. Apart from this argument, most critics agree that Warhol’s work shows the changing value of art in everyday life.""",
gloss="※ advertisement 광고 · commercial art 상업 미술 · career 경력, 직업 · silkscreen ink printing 실크스크린 인쇄 · depict 그리다, 묘사하다",
items=[
 item(1, "어휘(단어 뜻)", "윗글의 밑줄 친 ⟪critics⟫의 뜻으로 가장 알맞은 것은?",
      "비평가", ["화가", "미술관", "광고", "잡지"], 3,
      "critic(비평가): 책·영화·음악·미술에 대해 의견을 쓰는 사람. Some critics think … / most critics agree … 처럼 ‘…라고 생각한다/동의한다’의 주어로 쓰였다."),
 item(2, "세부 사실", "윗글에 따르면, Andy Warhol이 어린 시절 그림을 많이 그린 이유는?",
      "자주 아팠기 때문에", ["부모님이 화가였기 때문에", "미술 학교에 다녔기 때문에", "그림을 팔고 싶었기 때문에", "친구들이 그림을 좋아했기 때문에"], 2,
      "Andy Warhol was often sick as a child, so he spent a lot of time drawing. — 어릴 때 자주 아파서 그림을 많이 그렸다. 나머지는 본문에 없는 내용이다."),
 item(3, "지칭 추론", "윗글의 밑줄 친 ⟪These⟫가 가리키는 것으로 가장 알맞은 것은?",
      "일상 사물을 그린 Warhol의 작품들", ["Warhol이 만든 광고들", "Warhol의 작품을 전시한 미술관들", "Warhol이 그린 신발 그림들", "Warhol에 대해 글을 쓴 비평가들"], 1,
      "바로 앞 문장의 many famous art pieces depicting everyday objects(일상 사물을 그린 유명한 작품들)를 가리킨다. 그 예로 콜라병, 지폐, 수프 캔이 이어진다."),
 order_item(4, ORDQ, "(B) – (A) – (C)", 5,
      "대학 졸업 후 광고 미술 일을 시작(B) → 1950년대에 미술관에서 작품 전시(A) → 1960년대에 일상 사물을 그린 작품 제작(C). 2문단에 나온 순서 그대로이다.",
      box="(A) 미술관에서 자신의 작품을 전시하기 시작했다. \\\n(B) 광고를 위한 그림을 그리는 일을 시작했다. \\\n(C) 일상 사물을 그린 유명한 작품들을 만들었다."),
 item(5, "추론", "윗글을 통해 알 수 있는 것으로 가장 알맞은 것은?",
      "Warhol은 광고 그림을 그리다가 화가로 유명해졌다.",
      ["Warhol은 유명해진 뒤 그림 그리기를 그만두었다.", "모든 비평가가 Warhol이 돈만 밝혔다고 생각했다.", "Warhol이 실크스크린 인쇄를 처음 발명했다.", "광고 속 미술은 요즘 점점 인기가 줄고 있다."], 4,
      "광고용으로 그린 신발 그림이 유명해져 사람들이 그의 작품을 더 보고 싶어 했고, ‘그래서(Thus)’ 미술관에서 전시를 시작했다고 했다. 유명해진 뒤 그만두었다는 내용은 없고(1960년대에도 많은 작품을 만듦), 비평가 의견은 갈렸으며(Some … Others …), 실크스크린은 ‘처음 사용한 화가 중 한 명(one of the first)’일 뿐이고, 광고 속 미술은 점점 인기를 얻고 있다(increasingly popular)."),
]),
# ───────────────────────────── Unit 2 (Set B) ─────────────────────────────
dict(key="u2", set="B", title="Unit 2 · Nature — The Water Cycle Keeps Earth Balanced",
passage="""The water cycle is necessary for life on Earth. Water on the ground evaporates into vapor and forms clouds in the sky. In return, rain brings water back down to the ground again, which ends up in streams, rivers, lakes, and oceans. What happens when humans tamper with the water cycle?

Most evaporation occurs in oceans as a result of the Sun’s energy. This cools the temperature of Earth’s climate and also affects the oceans’ salt content. Having the correct amount of salt in the oceans ⟪maintains⟫ a delicate ecosystem of plants, fish, and other wildlife. One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. The two rivers that fed the Aral Sea were diverted for farming in the desert. As a result, the sea is now almost completely dry, killing the wildlife that lived there and causing dust storms that affect human health.

As we can see, the water cycle is necessary to keep the environment balanced.""",
gloss="※ evaporate 증발하다 · vapor 수증기 · tamper with 함부로 손대다 · salt content 소금 함량 · ecosystem 생태계 · divert (물길을) 돌리다 · dust storm 황사, 모래 폭풍",
items=[
 item(1, "문맥상 동의어", "윗글의 밑줄 친 ⟪maintains⟫와 바꿔 쓸 수 있는 말로 가장 알맞은 것은?",
      "keeps", ["breaks", "loses", "sells", "finds"], 1,
      "maintain은 ‘(상태를) 유지하다’. 알맞은 양의 소금이 생태계를 ‘지켜 준다, 유지한다’는 뜻이므로 keeps가 가장 가깝다."),
 item(2, "세부 사실", "윗글에 따르면, Aral Sea로 흘러들던 두 강의 물길을 바꾼 목적은?",
      "사막에서 농사를 짓기 위해", ["새 도시를 짓기 위해", "전기를 만들기 위해", "황사를 막기 위해", "야생동물을 보호하기 위해"], 4,
      "The two rivers that fed the Aral Sea were diverted for farming in the desert. 황사와 야생동물은 물길을 바꾼 ‘결과’로 나올 뿐 목적이 아니다."),
 item(3, "언급 이유", "글쓴이가 Aral Sea를 언급한 이유로 가장 알맞은 것은?",
      "물의 순환을 함부로 건드리면 생기는 재앙의 예를 들기 위해",
      ["사막에서 농사짓는 방법을 소개하기 위해", "바다의 소금이 생기는 과정을 설명하기 위해", "세계에서 가장 큰 호수를 소개하기 위해", "비가 만들어지는 과정을 설명하기 위해"], 2,
      "One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. — 물의 순환을 건드려서 생긴 재앙의 ‘예(example)’로 든 것이다."),
 item(4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
      "증발은 대부분 강과 호수에서 일어난다.",
      ["비는 물을 다시 땅으로 가져온다.", "증발은 바다의 소금 함량에 영향을 준다.", "Aral Sea는 지금 거의 완전히 말랐다.", "Aral Sea에서 생긴 황사는 사람의 건강에 영향을 준다."], 3,
      "Most evaporation occurs in oceans — 증발은 대부분 ‘바다’에서 일어난다. 나머지는 rain brings water back down to the ground / affects the oceans’ salt content / almost completely dry / dust storms that affect human health 와 일치한다."),
 item(5, "요약문 완성", SUMQ + "\n\nEvaporation (A) ______ Earth’s climate. The right amount of salt in the oceans helps plants, fish, and other wildlife (B) ______.",
      "(A) cools …… (B) live",
      ["(A) warms …… (B) live", "(A) cools …… (B) die", "(A) warms …… (B) die", "(A) dries …… (B) move"], 5,
      "(A) This cools the temperature of Earth’s climate — 증발은 기후를 ‘식힌다(cools)’. (B) maintains a delicate ecosystem of plants, fish, and other wildlife — 알맞은 소금 양이 생태계를 유지해 주므로 생물이 ‘살(live)’ 수 있다. 생물이 죽거나(die) 이동한다(move)는 내용은 없다."),
]),
# ───────────────────────────── Unit 3 (Set C) ─────────────────────────────
dict(key="u3", set="C", title="Unit 3 · Social Studies — The Slow City Movement",
passage="""In the 1980s, people who protested the increasing trend of fast food started a “slow food” movement. The movement aimed to preserve local foods, recipes, and communities, while rejecting fast, commercialized foods. This inspired the “slow city movement.”

The first Slow City was Chianti, Italy. The people there wanted to keep nature in good shape and ______ historic buildings. They came up with a plan for developing their town just the way they wanted. They called this plan cittaslow. The founders of this plan decided that new developments should keep people healthy and promote good relationships among neighbors. They also thought development should not hurt the natural environment.

Since 1999, dozens of cities around the world have been named Slow Cities. Slow Cities do not have many fast-food restaurants or big supermarkets. Instead, they have locally owned restaurants and small markets. Try visiting a Slow City someday to see if you like it!""",
gloss="※ protest 반대하다 · preserve 보존하다 · reject 거부하다 · inspire 영감을 주다 · historic 역사적인 · founder 창시자 · promote 북돋우다 · locally owned 지역 주민이 운영하는",
items=[
 item(1, "세부 사실", "윗글에 따르면, 최초의 Slow City는 어디인가?",
      "Chianti, Italy", ["Rome, Italy", "Paris, France", "Seoul, Korea", "Madrid, Spain"], 2,
      "The first Slow City was Chianti, Italy."),
 item(2, "문장 빈칸 어휘", "윗글의 빈칸에 들어갈 말로 가장 알맞은 것은?",
      "protect", ["destroy", "sell", "forget", "build"], 5,
      "‘자연을 좋은 상태로 유지하고(keep nature in good shape) 역사적 건물을 ___하고 싶었다’ — 앞의 ‘지키다’와 나란한 뜻인 protect(보호하다)가 알맞다. destroy(파괴하다)·sell(팔다)·forget(잊다)은 뜻이 반대이거나 어울리지 않고, 역사적 건물을 새로 ‘짓는다(build)’는 것은 말이 되지 않는다."),
 item(3, "주제", "윗글의 주제로 가장 알맞은 것은?",
      "슬로시티 운동이 시작된 과정과 슬로시티의 모습",
      ["패스트푸드를 많이 먹으면 생기는 문제", "이탈리아에서 가 볼 만한 슬로시티들", "슬로시티에서 작은 식당을 여는 방법", "슬로시티에 대형 마트가 많은 이유"], 3,
      "슬로푸드 운동에서 시작된 슬로시티 운동의 유래와 목표, 오늘날 슬로시티의 모습을 설명하는 글이다. 패스트푸드의 문제나 식당 여는 방법은 다루지 않고, 글에 나온 슬로시티는 Chianti 하나뿐이며, 대형 마트는 슬로시티에 ‘없다’고 했다."),
 item(4, "내용 일치", "윗글의 내용과 일치하는 것은?",
      "슬로시티에는 대형 마트 대신 작은 시장과 지역 식당이 있다.",
      ["슬로푸드 운동은 1990년대에 시작되었다.", "슬로시티 운동이 슬로푸드 운동에 영감을 주었다.", "cittaslow는 이탈리아의 오래된 건물 이름이다.", "1999년 이후 두 도시만 슬로시티로 지정되었다."], 1,
      "Slow Cities do not have many fast-food restaurants or big supermarkets. Instead, they have locally owned restaurants and small markets. 슬로푸드 운동은 1980년대에 시작했고, 슬로푸드가 슬로시티에 영감을 준 것이며(This inspired …), cittaslow는 마을 개발 ‘계획’의 이름이고, 1999년 이후 ‘수십 개(dozens of)’ 도시가 지정되었다."),
 item(5, "글쓴이의 주장", "윗글의 글쓴이가 가장 동의할 만한 것은?",
      "마을은 자연과 사람의 건강을 해치지 않고도 발전할 수 있다.",
      ["바쁜 도시에서는 패스트푸드가 가장 좋은 먹거리다.", "대형 마트는 이웃 사이를 더 가깝게 만든다.", "슬로시티는 새로운 개발을 전혀 허용하지 말아야 한다.", "이탈리아의 마을만 슬로시티가 될 수 있다."], 4,
      "cittaslow의 원칙: 새 개발(new developments)은 사람을 건강하게 하고 이웃 관계를 좋게 하며 자연환경을 해치지 않아야 한다. 글쓴이는 이를 긍정적으로 소개하고 방문까지 권한다. 패스트푸드·대형 마트는 글의 취지와 반대이고, 개발을 ‘전혀’ 허용하지 않는다는 것은 ‘새 개발은 ~해야 한다’는 원칙(개발 자체는 인정)과 어긋나며, 이탈리아만 된다는 것은 dozens of cities around the world와 맞지 않는다."),
]),
# ───────────────────────────── Unit 4 (Set D) ─────────────────────────────
dict(key="u4", set="D", title="Unit 4 · Science — The Theory of the Four Elements",
passage="""Before modern chemistry, ancient people tried to understand the makeup of the world. The ancient Greek philosopher Empedocles theorized that four elements made up every substance known to man. These elements were water, fire, earth, and air.

What observations did Empedocles make about these elements? First, he noted that pots were made with earth and water. After being mixed and shaped, they were burned with fire and cooled with air. All four elements were necessary to make one pot. The same pot was used for cooking plants from the earth, often mixed with water, over a flame. The air cooled down the food so it could be eaten. Thus, all four elements were necessary to ______. Empedocles also believed that these elements were ⟪indestructible⟫ and unchangeable. His theories inspired later scientists to study more about the elements that make up our world.""",
gloss="※ chemistry 화학 · makeup 구성 · philosopher 철학자 · theorize 이론을 세우다 · element 원소 · substance 물질 · observation 관찰 · flame 불꽃",
items=[
 item(1, "세부 사실", "윗글에서 Empedocles가 말한 네 가지 원소에 해당하지 *않는* 것은?",
      "wood", ["water", "fire", "earth", "air"], 4,
      "These elements were water, fire, earth, and air. 나무(wood)는 네 원소에 들어 있지 않다."),
 item(2, "어휘(단어 뜻)", "윗글의 밑줄 친 ⟪indestructible⟫의 뜻으로 가장 알맞은 것은?",
      "파괴할 수 없는", ["아주 오래된", "맛있는", "현대적인", "꼭 필요한"], 1,
      "indestructible = in-(아닌) + destruct(파괴하다) + -ible(할 수 있는) → 파괴할 수 없는. 뒤에 이어지는 unchangeable(변하지 않는)과 비슷한 뜻으로 묶여 쓰였다."),
 item(3, "도표 완성", TBLQ,
      "(A) fire …… (B) air",
      ["(A) air …… (B) fire", "(A) fire …… (B) water", "(A) water …… (B) air", "(A) earth …… (B) fire"], 5,
      "After being mixed and shaped, they were burned with fire and cooled with air. — 불(fire)로 굽고 공기(air)로 식힌다.",
      table=[["*Making a Pot*", ""],
             ["1", "Pots are made with earth and water."],
             ["2", "They are mixed and shaped."],
             ["3", "They are burned with (A) ______."],
             ["4", "They are cooled with (B) ______."]]),
 item(4, "제목", "윗글의 제목으로 가장 알맞은 것은?",
      "Empedocles와 네 가지 원소 이론",
      ["흙과 물로 항아리 만드는 법", "고대 그리스 철학자들의 삶", "불이 가장 중요한 원소인 이유", "현대 화학과 주기율표"], 2,
      "Empedocles가 세상이 네 원소로 이루어졌다고 본 이론과 그 근거(항아리 만들기·요리)를 설명하는 글이다. 항아리 만드는 법은 예시일 뿐이고, 철학자들의 삶·불의 우월함·주기율표는 다루지 않았다."),
 item(5, "빈칸 추론", "윗글의 빈칸에 들어갈 말로 가장 알맞은 것은?",
      "cook food", ["build a house", "sell the pot", "grow plants", "start a fire"], 3,
      "빈칸 앞에서 항아리로 식물을 물과 섞어 불 위에서 요리하고, 공기로 식혀 먹을 수 있게 되는 과정을 설명했다. Thus(따라서)로 이어지는 결론은 ‘음식을 요리하는 데’ 네 원소가 모두 필요했다는 것이다. 집 짓기·항아리 팔기·식물 기르기·불 피우기는 앞 내용과 이어지지 않는다."),
]),
# ───────────────────────────── Unit 5 (Set A) ─────────────────────────────
dict(key="u5", set="A", title="Unit 5 · Art — Teddy Bears Throughout Time",
passage="""How did the teddy bear get its name? It comes from U.S. president Theodore Roosevelt. During a hunting trip, Roosevelt ⟪refused⟫ to kill a bear that had been tied to a tree. All over America, people heard about ⟪this story⟫. Some people even made stuffed bears and called them “teddy bears” in honor of the president’s nickname, Teddy.

Teddy bears became mass-produced in the twentieth century. They were mainly toys for children, but they were also popularly featured in books and even in movies. Some well-known examples include Winnie the Pooh, which was originally written for adults, as well as Paddington Bear. Due to their popularity, teddy bears were manufactured in a wide range of sizes, colors, and materials. They have endured such lasting popularity that there are museums dedicated to teddy bears all around the world. England, Japan, and South Korea are just a few countries that have teddy bear museums.

Whether they are children’s toys, subjects of books, or objects on display at museums, teddy bears remain popular. Teddy bears will probably be around for a long time to come.""",
gloss="※ stuffed bear 곰 인형 · in honor of ~을 기리기 위해 · nickname 별명 · mass-produced 대량 생산된 · feature 등장시키다 · manufacture 만들다, 제조하다 · dedicated to ~을 위한",
items=[
 item(1, "어휘(단어 뜻)", "윗글의 밑줄 친 ⟪refused⟫의 뜻으로 가장 알맞은 것은?",
      "거절했다", ["묶었다", "들었다", "만들었다", "죽였다"], 5,
      "refuse(거절하다, 거부하다). Roosevelt refused to kill a bear — 곰을 죽이기를 거절했다. tie(묶다), hear(듣다), make(만들다), kill(죽이다)은 모두 1문단에 나오는 다른 동사이다."),
 item(2, "세부 사실", "윗글에 따르면, ‘teddy bear’라는 이름은 누구의 별명에서 나왔는가?",
      "미국 대통령 Theodore Roosevelt", ["유명한 장난감 회사 사장", "Winnie the Pooh를 쓴 작가", "곰을 나무에 묶은 사람", "일본의 박물관 주인"], 3,
      "It comes from U.S. president Theodore Roosevelt. … in honor of the president’s nickname, Teddy. 곰을 나무에 묶은 사람이 누구인지는 글에 나오지 않는다."),
 item(3, "지칭 추론", "윗글의 밑줄 친 ⟪this story⟫가 가리키는 내용으로 가장 알맞은 것은?",
      "Roosevelt가 나무에 묶인 곰을 죽이지 않은 일",
      ["Roosevelt가 미국 대통령이 된 일", "사람들이 곰 인형을 만들어 teddy bear라고 부른 일", "Winnie the Pooh가 어른을 위해 쓰인 일", "곰이 사냥꾼에게서 도망친 일"], 4,
      "바로 앞 문장 During a hunting trip, Roosevelt refused to kill a bear that had been tied to a tree. — 이 이야기를 미국 전역의 사람들이 들은 것이다. 곰 인형을 만든 것은 그 ‘뒤’의 일이고, 곰이 도망쳤다는 내용은 없다."),
 order_item(4, ORDQ, "(B) – (C) – (A)", 2,
      "사냥에서 곰을 죽이지 않음(B) → 사람들이 곰 인형을 만들어 teddy bear라고 부름(C) → 20세기에 대량 생산됨(A). 1문단에서 2문단으로 이어지는 순서이다.",
      box="(A) 곰 인형이 20세기에 대량 생산되었다. \\\n(B) Roosevelt가 사냥에서 곰을 죽이지 않았다. \\\n(C) 사람들이 곰 인형을 만들어 ‘teddy bear’라고 불렀다."),
 item(5, "추론", "윗글을 통해 알 수 있는 것으로 가장 알맞은 것은?",
      "사람들은 곰을 죽이지 않은 Roosevelt를 좋게 여겼다.",
      ["teddy bear는 미국에서만 인기가 있었다.", "Roosevelt가 직접 첫 teddy bear를 만들었다.", "teddy bear는 곧 인기를 잃을 것이다.", "teddy bear는 주로 어른을 위한 장난감이었다."], 1,
      "사람들이 이야기를 듣고 대통령을 ‘기리기 위해(in honor of)’ 곰 인형에 그의 별명을 붙였으므로, 곰을 죽이지 않은 그를 좋게 여겼음을 알 수 있다. 박물관이 세계 곳곳에 있으니 미국에서만 인기였던 것이 아니고, 인형을 만든 것은 ‘some people’이며, 앞으로도 오래 사랑받을 것이라 했고, 곰 인형은 ‘주로 아이들의 장난감(mainly toys for children)’이었다."),
]),
# ───────────────────────────── Unit 6 (Set B) ─────────────────────────────
dict(key="u6", set="B", title="Unit 6 · Nature — Osmosis in Everyday Life",
passage="""Molecules are always moving. Sometimes, molecules even move through membranes. Molecules tend to pass through semi-permeable membranes to an area where the solvent concentration is higher. This equalizes the concentration of materials on either side of the membrane. This process is called osmosis. Osmosis is an important chemical process with practical uses in everyday life. What is one use of osmosis?

Fresh vegetables have a high concentration of water molecules. During pickling, vegetables are placed in a brine—a mixture of water, salt, and seasonings. The skin acts as a semi-permeable membrane. Water molecules move out of the vegetables through the skin and into the brine, which equalizes the solvent concentration on either side of the membrane. This process is an example of osmosis, and it is why pickled vegetables stay crunchy.

Reverse osmosis is a process that uses pressure to force molecules into an area of lower solute concentration. We use reverse osmosis to ⟪remove⟫ salt and other particles from seawater. Afterward, we can drink the water!""",
gloss="※ molecule 분자 · semi-permeable membrane 반투막 · concentration 농도 · osmosis 삼투 · pickling 피클 만들기 · seasoning 양념 · crunchy 아삭한 · pressure 압력 · particle 입자",
items=[
 item(1, "문맥상 동의어", "윗글의 밑줄 친 ⟪remove⟫와 바꿔 쓸 수 있는 말로 가장 알맞은 것은?",
      "take out", ["put in", "mix up", "heat up", "pick up"], 1,
      "remove는 ‘없애다, 제거하다’. 바닷물에서 소금을 ‘빼낸다’는 뜻이므로 take out이 가장 가깝다."),
 item(2, "세부 사실", "윗글에 따르면, brine(소금물)은 무엇으로 이루어져 있는가?",
      "물, 소금, 양념", ["물, 설탕, 기름", "소금, 식초, 설탕", "바닷물과 채소", "물과 후추"], 2,
      "a brine—a mixture of water, salt, and seasonings. 물, 소금, 양념의 혼합물이다."),
 item(3, "언급 이유", "글쓴이가 pickling(피클 만들기)을 언급한 이유로 가장 알맞은 것은?",
      "일상생활에서 삼투 현상이 쓰이는 예를 들기 위해",
      ["채소를 싱싱하게 기르는 방법을 알려 주기 위해", "소금물을 만드는 순서를 설명하기 위해", "바닷물을 마실 수 있게 만드는 과정을 보여 주기 위해", "분자가 움직이지 않는 경우를 설명하기 위해"], 5,
      "1문단 끝 What is one use of osmosis?라는 질문에 답하는 예로 피클 만들기를 들었고, This process is an example of osmosis라고 밝혔다. 바닷물 정수는 ‘역삼투’의 예이며, 분자는 항상 움직인다고 했다."),
 item(4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
      "피클은 소금물 속에서 물렁물렁해진다.",
      ["분자는 항상 움직인다.", "채소의 껍질은 반투막 역할을 한다.", "피클을 만들 때 물이 채소 밖으로 빠져나온다.", "역삼투는 압력을 이용해 바닷물에서 소금을 없앤다."], 4,
      "it is why pickled vegetables stay crunchy — 피클은 ‘아삭함을 유지’한다. 나머지는 Molecules are always moving / The skin acts as a semi-permeable membrane / Water molecules move out of the vegetables … into the brine / uses pressure … remove salt 와 일치한다."),
 item(5, "요약문 완성", SUMQ + "\n\nOsmosis makes the concentration on both sides of a membrane (A) ______. Reverse osmosis is the (B) ______ of osmosis, and it makes seawater drinkable.",
      "(A) the same …… (B) opposite",
      ["(A) higher …… (B) opposite", "(A) the same …… (B) example", "(A) lower …… (B) example", "(A) higher …… (B) result"], 3,
      "(A) This equalizes the concentration … on either side of the membrane — 막 양쪽의 농도를 ‘같게(the same)’ 만든다. (B) 역삼투(reverse osmosis)는 압력으로 분자를 반대 방향(농도가 낮은 쪽)으로 밀어 넣는, 삼투의 ‘반대(opposite)’ 과정이다. 삼투의 ‘예(example)’는 피클 만들기이고, 역삼투는 삼투의 ‘결과(result)’가 아니다."),
]),
# ───────────────────────────── Unit 7 (Set C) ─────────────────────────────
dict(key="u7", set="C", title="Unit 7 · Social Studies — Majority Rule in Democracies",
passage="""People usually make tough decisions by voting for one of two or more options. The option that gets the most votes is the winner. This is called majority rule. However, even if only 51% of people in a group vote for an option, they will get their choice. That means, almost half of the people in that group will not get their choice. In that case, is majority rule really fair?

Most democracies elect public officials through a majority vote. In a system with two political parties, a slim margin, such as 51% to 49%, can decide an election. In a system with more than two parties, less than 50% of voters could give one political party a victory. To ensure the ______ of majority rule, certain conditions must be met. First, people should be able to vote with secret ballots. Second, each person’s vote should be weighted equally. Finally, there have to be enough voters to make a majority vote truly fair.

When an election is won with less than 50% of the total votes, the winning party must consider the opinions of the other voters. This is because running a democracy should ensure equality for all citizens.""",
gloss="※ option 선택지 · majority rule 다수결 · democracy 민주주의 · elect 뽑다 · public official 공직자 · political party 정당 · slim margin 근소한 차이 · secret ballot 비밀 투표 · weighted equally 똑같은 무게로 반영되는 · equality 평등",
items=[
 item(1, "세부 사실", "윗글에 따르면, majority rule(다수결)에서는 어떤 선택지가 승자가 되는가?",
      "가장 많은 표를 얻은 선택지", ["가장 나이 많은 사람이 고른 선택지", "모든 사람이 찬성한 선택지", "대통령이 가장 좋아하는 선택지", "가장 적은 표를 얻은 선택지"], 3,
      "The option that gets the most votes is the winner. This is called majority rule."),
 item(2, "문장 빈칸 어휘", "윗글의 빈칸에 들어갈 말로 가장 알맞은 것은?",
      "fairness", ["victory", "speed", "price", "size"], 4,
      "앞 문단 끝의 is majority rule really fair?와 뒤의 to make a majority vote truly fair가 단서이다. 다수결의 ‘공정함(fairness)’을 보장하기 위해 조건이 필요하다는 뜻이다. victory(승리)·speed(속도)·price(가격)·size(크기)는 이 문맥과 맞지 않는다."),
 item(3, "주제", "윗글의 주제로 가장 알맞은 것은?",
      "다수결의 뜻과 다수결을 공정하게 만드는 조건",
      ["근소한 차이로 결정되는 두 정당의 선거", "여러 나라에서 다수결이 생겨난 역사", "모든 민주주의에 비밀 투표가 필요한 이유", "민주주의에서 공직자가 하는 일"], 1,
      "다수결의 뜻과 한계(거의 절반이 원하는 것을 얻지 못함), 공정한 다수결을 위한 세 가지 조건, 이긴 쪽이 가져야 할 태도를 설명하는 글이다. 근소한 차이의 선거와 비밀 투표는 글의 일부 내용만 담은 너무 좁은 주제이고, 다수결의 역사와 공직자의 일은 글에 없다."),
 item(4, "내용 일치", "윗글의 내용과 일치하는 것은?",
      "정당이 셋 이상이면 50%보다 적은 표로도 이길 수 있다.",
      ["다수결에서 승자는 항상 90% 이상의 표를 얻는다.", "대부분의 민주주의 국가는 투표 없이 공직자를 뽑는다.", "사람마다 표의 무게가 달라야 한다.", "이긴 정당은 다른 유권자를 신경 쓸 필요가 없다."], 5,
      "In a system with more than two parties, less than 50% of voters could give one political party a victory. 51%만 얻어도 이기므로 ‘항상 90% 이상’은 틀리고, 공직자는 ‘다수결 투표로(through a majority vote)’ 뽑으며, 표는 ‘똑같이(equally)’ 반영되어야 하고, 이긴 정당은 다른 유권자의 의견을 ‘고려해야(must consider)’ 한다."),
 item(5, "글쓴이의 주장", "윗글의 글쓴이가 가장 동의할 만한 것은?",
      "가장 많은 표를 얻었다고 해서 그 결정이 모두에게 공정한 것은 아니다.",
      ["유권자가 많을수록 다수결은 덜 공정해진다.", "50%보다 적은 표로 이긴 정당은 다른 유권자를 무시해도 된다.", "지도자의 표는 보통 시민의 표보다 더 무거워야 한다.", "투표는 모두가 볼 수 있는 곳에서 해야 한다."], 2,
      "글쓴이는 51%만 얻어도 이기므로 거의 절반이 원하는 것을 얻지 못한다며 ‘다수결이 정말 공정한가’를 묻고, 이긴 정당은 다른 유권자의 의견을 고려해야 하며 민주주의는 모든 시민의 평등을 보장해야 한다고 했다. 유권자가 많을수록 덜 공정하다는 것은 enough voters 조건과 반대이고, 다른 유권자를 무시해도 된다는 것은 must consider와 반대이며, 지도자의 표가 더 무겁다는 것은 weighted equally와, 남이 보는 앞에서 투표한다는 것은 secret ballots와 어긋난다."),
]),
# ───────────────────────────── Unit 8 (Set D) ─────────────────────────────
dict(key="u8", set="D", title="Unit 8 · Science — The Rising Prominence of Telescopes",
passage="""The invention of the telescope has helped humans see and understand the stars better. How have telescopes changed over time?

Telescopes were originally used to see long distances. Galileo was one of the first to use a telescope to observe the stars. His telescope used a concave eyepiece and a convex lens. This gave the image seen through the telescope an upright view and magnified it up to thirty times! Even though Galileo’s telescope was quite useful at the time, the images it produced were blurry. Kepler improved on Galileo’s design by using a convex eyepiece and lens. This gave a much wider field of view, even though the images appeared upside-down.

In modern times, telescopes have been launched into space to help ⟪astronomers⟫ observe not just the stars, but the universe as well. One example is the Hubble Telescope, which orbits Earth and sends back high-quality pictures of distant planets and galaxies. Through continued technological developments, humans can ______.""",
gloss="※ invention 발명 · observe 관찰하다 · concave 오목한 · convex 볼록한 · eyepiece 접안렌즈 · magnify 확대하다 · blurry 흐릿한 · field of view 시야 · launch 발사하다 · orbit 궤도를 돌다 · galaxy 은하",
items=[
 item(1, "세부 사실", "윗글에 따르면, Galileo의 망원경은 이미지를 최대 몇 배까지 확대했는가?",
      "thirty times", ["three times", "five times", "ten times", "twenty times"], 5,
      "… and magnified it up to thirty times! 최대 30배까지 확대했다."),
 item(2, "어휘(단어 뜻)", "윗글의 밑줄 친 ⟪astronomers⟫의 뜻으로 가장 알맞은 것은?",
      "천문학자", ["발명가", "조종사", "농부", "건축가"], 2,
      "astronomer(천문학자): 별·행성 등 우주를 연구하는 과학자. 망원경이 우주로 발사되어 ‘천문학자들’이 별과 우주를 관측하도록 돕는다는 문맥이다."),
 item(3, "도표 완성", TBLQ,
      "(A) concave …… (B) upside-down",
      ["(A) convex …… (B) upside-down", "(A) concave …… (B) blurry", "(A) convex …… (B) upright", "(A) concave …… (B) clear"], 3,
      "(A) His telescope used a concave eyepiece and a convex lens — Galileo의 접안렌즈는 오목(concave). (B) Kepler의 망원경은 시야가 넓어진 대신 the images appeared upside-down — 거꾸로 보였다. blurry(흐릿한)는 Galileo 망원경의 단점이다.",
      table=[["", "*Galileo’s telescope*", "*Kepler’s telescope*"],
             ["eyepiece", "(A) ______", "convex"],
             ["lens", "convex", "convex"],
             ["images", "upright, but blurry", "wider view, but (B) ______"]]),
 item(4, "제목", "윗글의 제목으로 가장 알맞은 것은?",
      "망원경은 어떻게 발전해 왔을까",
      ["나만의 망원경을 만드는 방법", "Galileo의 삶과 죽음", "Hubble 망원경의 하루", "옛날 사람들이 별을 본 이유"], 4,
      "1문단의 질문 How have telescopes changed over time?에 답하여 Galileo → Kepler → Hubble로 이어지는 망원경의 발전을 설명하는 글이다. 망원경 제작법, Galileo의 생애, Hubble의 하루, 옛날 사람들이 별을 본 이유는 글의 내용이 아니다."),
 item(5, "빈칸 추론", "윗글의 빈칸에 들어갈 말로 가장 알맞은 것은?",
      "understand the universe much better",
      ["make Galileo’s telescope again", "see the stars without any telescope", "stop launching telescopes into space", "live on distant planets"], 1,
      "1문단에서 망원경의 발명이 인간이 별을 더 잘 ‘이해하도록(understand)’ 도왔다고 했고, 3문단에서 우주 망원경이 우주의 고화질 사진을 보내온다고 했다. 따라서 기술이 계속 발전하면 인간은 ‘우주를 훨씬 더 잘 이해할 수’ 있다. Galileo의 망원경을 다시 만들거나, 망원경 없이 별을 보거나, 발사를 멈추거나, 먼 행성에 산다는 것은 글의 흐름과 맞지 않는다."),
]),
]

PAIR = {"A": "1·5 (Art)", "B": "2·6 (Nature)", "C": "3·7 (Social Studies)", "D": "4·8 (Science)"}


def build():
    sections, blueprint, qno = [], [], 0
    for u in UNITS:
        passage = {"type": "passage", "title": f"[{qno+1}~{qno+5}] 다음 글을 읽고 물음에 답하시오.", "text": u["passage"]}
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
        "meta": {"subject": "영어 독해", "grade": "Level 7 (초6 수준)", "unit": "Unit 1~8", "time_limit": "50분"},
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
             "대상: The Reading Level 7을 배운 초등학교 6학년 · 40문항 · 5지선다 · 문항당 2.5점 · 100점 만점 · 70점(28문항) 이상 합격", "",
             "## 유형 설계 (단원 쌍끼리 동일)", "", "| 쌍 | 1 | 2 | 3 | 4 | 5 |", "|---|---|---|---|---|---|"]
    for s, (a, _) in zip("ABCD", (("u1", "u5"), ("u2", "u6"), ("u3", "u7"), ("u4", "u8"))):
        lines.append(f"| {PAIR[s]} | " + " | ".join(kinds[a]) + " |")
    lines += ["", "## 초6 눈높이 장치", "",
              "- 이해를 묻는 문항(세부·지칭·순서·추론·언급 이유·일치/불일치·주제·제목·주장)은 선택지를 한국어로 쓴다.",
              "- 어휘 문항은 영영풀이 대신 밑줄 친 단어의 한국어 뜻을 고른다.",
              "- 사건 순서 배열은 사건 3개만 쓴다.",
              "- 지문 아래에 시험에 나오지 않는 어려운 단어의 뜻을 달아 준다 (build_7-1.py 의 GLOSS = False 로 끌 수 있다).",
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
