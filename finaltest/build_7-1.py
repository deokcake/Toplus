"""The Reading 7-1 Final Test 원본 데이터 → exam-worksheet JSON."""
import json, sys
from pathlib import Path

P = {
"u1": """Throughout time, art has been used to decorate homes, churches, and public buildings. In modern times, art is used in advertisements, magazines, cartoons, and even on television! Art in advertisements has become increasingly popular. This is called commercial art. One of the most famous commercial artists was Andy Warhol.

Andy Warhol was often sick as a child, so he spent a lot of time drawing. After college, he began his career making art for advertisements. His drawings of shoes became so well known that people wanted to see more of his work. Thus, in the 1950s, he began showing his popular works in art galleries. Warhol was one of the first artists to use silkscreen ink printing in his work. During the 1960s, he produced many famous art pieces depicting everyday objects. These include Coca-Cola bottles, dollar bills, and Campbell’s Soup cans. This kind of art is referred to as “pop art.”

Some critics think Andy Warhol was only interested in making money with his art. Others thought he was the perfect example of commercialized modern life. Apart from this argument, most critics agree that Warhol’s work shows the changing value of art in everyday life.""",
"u2": """The water cycle is necessary for life on Earth. Water on the ground evaporates into vapor and forms clouds in the sky. In return, rain brings water back down to the ground again, which ends up in streams, rivers, lakes, and oceans. What happens when humans tamper with the water cycle?

Most evaporation occurs in oceans as a result of the Sun’s energy. This cools the temperature of Earth’s climate and also affects the oceans’ salt content. Having the correct amount of salt in the oceans maintains a delicate ecosystem of plants, fish, and other wildlife. One example of a disaster caused by tampering with the water cycle is the drying-up of the Aral Sea. The two rivers that fed the Aral Sea were diverted for farming in the desert. As a result, the sea is now almost completely dry, killing the wildlife that lived there and causing dust storms that affect human health.

As we can see, the water cycle is necessary to keep the environment balanced. It is important to understand the water cycle and to protect our water sources so they can function well for Earth’s sake.""",
"u3": """In the 1980s, people who protested the increasing trend of fast food started a “slow food” movement. The movement aimed to preserve local foods, recipes, and communities, while rejecting fast, commercialized foods. This inspired the “slow city movement.”

The first Slow City was Chianti, Italy. The people there wanted to keep nature in good shape and protect historic buildings. They came up with a plan for developing their town just the way they wanted. They called this plan cittaslow. The term comes from the words “slow” and “citta,” which means “town” or “city” in Italian. The founders of this plan decided that new developments should keep people healthy and promote good relationships among neighbors. They also thought development should not hurt the natural environment.

Since 1999, dozens of cities around the world have been named Slow Cities. They have a lot of green places where people can exercise and enjoy nature. Slow Cities do not have many fast-food restaurants or big supermarkets. Instead, they have locally owned restaurants and small markets. Try visiting a Slow City someday to see if you like it!""",
"u4": """Before modern chemistry, ancient people tried to understand the makeup of the world. The ancient Greek philosopher Empedocles theorized that four elements made up every substance known to man. These elements were water, fire, earth, and air.

What observations did Empedocles make about these elements? First, he noted that pots were made with earth and water. After being mixed and shaped, they were burned with fire and cooled with air. All four elements were necessary to make one pot. The same pot was used for cooking plants from the earth, often mixed with water, over a flame. The air cooled down the food so it could be eaten. Thus, all four elements were necessary to prepare a meal. Empedocles also believed that these elements were indestructible and unchangeable. His theories inspired later scientists to study more about the elements that make up our world.

Think about your life and all of your belongings. How are the four elements involved in things you own, such as your computer, your clothes, and the food you eat? Thinking about everyday objects on a small scale can help us understand the world around us.""",
"u5": """How did the teddy bear get its name? It comes from U.S. president Theodore Roosevelt. During a hunting trip, Roosevelt refused to kill a bear that had been tied to a tree. All over America, people heard about this story. Some people even made stuffed bears and called them “teddy bears” in honor of the president’s nickname, Teddy.

Teddy bears became mass-produced in the twentieth century. They were mainly toys for children, but they were also popularly featured in books and even in movies. Some well-known examples include Winnie the Pooh, which was originally written for adults, as well as Paddington Bear. Due to their popularity, teddy bears were manufactured in a wide range of sizes, colors, and materials. They have endured such lasting popularity that there are museums dedicated to teddy bears all around the world. England, Japan, and South Korea are just a few countries that have teddy bear museums.

Whether they are children’s toys, subjects of books, or objects on display at museums, teddy bears remain popular. They bring children comfort and are fun to play with. Teddy bears will probably be around for a long time to come.""",
"u6": """Molecules are always moving. Sometimes, molecules even move through membranes. Molecules tend to pass through semi-permeable membranes to an area where the solvent concentration is higher. This equalizes the concentration of materials on either side of the membrane. This process is called osmosis. Osmosis is an important chemical process with practical uses in everyday life. What is one use of osmosis?

Fresh vegetables have a high concentration of water molecules. During pickling, vegetables are placed in a brine—a mixture of water, salt, and seasonings. The skin acts as a semi-permeable membrane. Water molecules move out of the vegetables through the skin and into the brine, which equalizes the solvent concentration on either side of the membrane. This process is an example of osmosis, and it is why pickled vegetables stay crunchy.

Reverse osmosis is a process that uses pressure to force molecules into an area of lower solute concentration. We use reverse osmosis to remove salt and other particles from seawater. Afterward, we can drink the water!

Chemical processes like osmosis have a big effect on our everyday lives. For this reason, learning about how they work is important for our understanding of the world.""",
"u7": """People usually make tough decisions by voting for one of two or more options. The option that gets the most votes is the winner. This is called majority rule. However, even if only 51% of people in a group vote for an option, they will get their choice. That means, almost half of the people in that group will not get their choice. In that case, is majority rule really fair?

Most democracies elect public officials through a majority vote. In a system with two political parties, a slim margin, such as 51% to 49%, can decide an election. In a system with more than two parties, less than 50% of voters could give one political party a victory. To ensure the fairness of majority rule, certain conditions must be met. First, people should be able to vote with secret ballots. Second, each person’s vote should be weighted equally. Finally, there have to be enough voters to make a majority vote truly fair.

When an election is won with less than 50% of the total votes, the winning party must consider the opinions of the other voters. This is because running a democracy should ensure equality for all citizens.""",
"u8": """Throughout history, humans have looked at the stars as a map, as a guide, and for worship. The invention of the telescope has helped humans see and understand the stars better. How have telescopes changed over time?

Telescopes were originally used to see long distances. Galileo was one of the first to use a telescope to observe the stars. His telescope used a concave eyepiece and a convex lens. This gave the image seen through the telescope an upright view and magnified it up to thirty times! Even though Galileo’s telescope was quite useful at the time, the images it produced were blurry. Kepler improved on Galileo’s design by using a convex eyepiece and lens. This gave a much wider field of view, even though the images appeared upside-down.

In modern times, telescopes have been launched into space to help astronomers observe not just the stars, but the universe as well. One example is the Hubble Telescope, which orbits Earth and sends back high-quality pictures of distant planets and galaxies. Through continued technological developments, humans can understand the universe much better.""",
}

VOC = "다음 영영풀이에 해당하는 단어로 가장 적절한 것은?"
SUM = "다음은 윗글을 요약한 것이다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?"

# (난이도, 유형, 발문, 정답, [오답4], 정답 위치, 해설)
U = [
("u1", "Unit 1 · Art — Andy Warhol and Pop Art", [
 (1, "어휘", VOC + "\n\n“a person who writes about and expresses opinions about books, movies, music, or art”",
  "critic", ["gallery", "career", "stencil", "bottle"], 3,
  "critic(비평가): 책·영화·음악·미술에 대해 의견을 쓰고 표현하는 사람. 3문단 Some critics think…"),
 (2, "세부 사실", "윗글에 따르면, Andy Warhol이 어린 시절 그림을 많이 그린 이유로 가장 적절한 것은?",
  "He was often sick as a child.", ["He studied art in college.", "His parents were famous artists.", "He wanted to sell his drawings.", "He worked for a magazine."], 2,
  "Andy Warhol was often sick as a child, so he spent a lot of time drawing."),
 (3, "제목", "윗글의 제목으로 가장 적절한 것은?",
  "Andy Warhol and the Rise of Pop Art", ["The History of Silkscreen Ink Printing", "Famous Paintings in Churches", "How Television Changed Advertising", "Why Critics Dislike Commercial Art"], 5,
  "상업 미술가 Andy Warhol의 생애와 그가 만든 팝아트를 다룬 글이다. 나머지는 일부 소재이거나 언급되지 않은 내용이다."),
 (4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
  "Warhol made art pieces of soup cans and dollar bills in the 1970s.",
  ["Today, art is used in magazines and cartoons.", "After college, Warhol made art for advertisements.", "Warhol began showing his works in art galleries in the 1950s.", "Some critics thought Warhol only cared about making money."], 4,
  "일상 사물(수프 캔, 달러 지폐 등)을 그린 작품은 1960년대(During the 1960s)에 만들었다."),
 (5, "추론", "윗글을 통해 추론할 수 있는 것으로 가장 적절한 것은?",
  "Warhol’s work showed that everyday objects could become subjects of art.",
  ["Warhol stopped drawing after he became famous.", "All critics agreed that Warhol was a great artist.", "Warhol was the person who invented silkscreen printing.", "Art in advertisements was more popular in the past than today."], 1,
  "일상 사물을 그린 팝아트가 ‘일상 속 예술의 달라진 가치’를 보여 준다고 했다. 비평가들의 의견은 갈렸고(All critics ✗), 실크스크린을 ‘처음 사용한 화가 중 한 명’일 뿐 발명자가 아니며(invented ✗), 광고 미술은 오늘날 점점 인기를 얻고 있다(more popular in the past ✗)."),
]),
("u2", "Unit 2 · Nature — The Water Cycle Keeps Earth Balanced", [
 (1, "어휘", VOC + "\n\n“tiny drops of water or other liquids in the air that appear as mist”",
  "vapor", ["salt", "desert", "wildlife", "stream"], 2,
  "vapor(수증기): 공기 중에 안개처럼 보이는 아주 작은 물방울. Water on the ground evaporates into vapor…"),
 (2, "세부 사실", "윗글에 따르면, Aral Sea로 흘러가던 두 강의 물길을 바꾼 목적은?",
  "to farm in the desert", ["to build a new city", "to make electricity", "to stop dust storms", "to protect wildlife"], 1,
  "The two rivers that fed the Aral Sea were diverted for farming in the desert."),
 (3, "주제", "윗글의 주제로 가장 적절한 것은?",
  "the importance of the water cycle and the danger of changing it",
  ["how clouds form in the sky", "the best way to farm in the desert", "the history of the Aral Sea", "why ocean water is salty"], 4,
  "물의 순환이 지구에 꼭 필요하며, 인간이 이를 함부로 바꾸면(Aral Sea 사례) 재앙이 생긴다는 글이다. Aral Sea는 예시일 뿐 주제가 아니다."),
 (4, "내용 일치", "윗글의 내용과 일치하는 것은?",
  "Dust storms from the dried-up Aral Sea affect human health.",
  ["Most evaporation happens in lakes and rivers.", "Evaporation makes Earth’s climate warmer.", "Evaporation does not affect the salt content of the oceans.", "The Aral Sea is now full of fish and plants."], 5,
  "증발은 대부분 바다에서 일어나고(lakes and rivers ✗), 기후를 식히며(warmer ✗), 바다의 염분에 영향을 준다(does not affect ✗). Aral Sea는 거의 완전히 말라 버렸다(full of fish ✗)."),
 (5, "요약문 완성", SUM + "\n\nWhen humans (A) ______ the water cycle, as in the case of the Aral Sea, the environment can lose its (B) ______.",
  "(A) change …… (B) balance",
  ["(A) protect …… (B) beauty", "(A) study …… (B) salt", "(A) protect …… (B) balance", "(A) follow …… (B) balance"], 3,
  "tamper with(함부로 바꾸다) = change, 물의 순환은 환경의 균형(keep the environment balanced)을 지킨다. 따라서 (A) change, (B) balance."),
]),
("u3", "Unit 3 · Social Studies — The Slow City Movement", [
 (1, "어휘", VOC + "\n\n“the person who got an organization or a plan started”",
  "founder", ["neighbor", "recipe", "market", "visitor"], 1,
  "founder(창시자, 설립자). The founders of this plan decided…"),
 (2, "세부 사실", "윗글에 따르면, 최초의 Slow City는 어디인가?",
  "Chianti, Italy", ["Rome, Italy", "Paris, France", "Seoul, Korea", "Madrid, Spain"], 4,
  "The first Slow City was Chianti, Italy."),
 (3, "주제", "윗글의 주제로 가장 적절한 것은?",
  "the slow city movement and its goals",
  ["the dangers of eating fast food", "famous wines of Italy", "how to open a small restaurant", "the history of Italian recipes"], 3,
  "슬로푸드 운동에서 시작된 슬로시티 운동의 출발과 목표, 오늘날의 모습을 설명하는 글이다."),
 (4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
  "Slow Cities have many big supermarkets and fast-food restaurants.",
  ["The slow food movement started in the 1980s.", "Cittaslow was a plan for developing a town.", "The founders wanted new developments to keep people healthy.", "Since 1999, dozens of cities have been named Slow Cities."], 2,
  "Slow Cities do not have many fast-food restaurants or big supermarkets."),
 (5, "추론", "윗글을 통해 추론할 수 있는 것으로 가장 적절한 것은?",
  "People in Slow Cities value health, nature, and neighbors more than speed.",
  ["The slow city movement wants cities to grow as fast as possible.", "Chianti stopped being a Slow City after 1999.", "Slow Cities do not allow tourists to visit.", "The slow food movement was started to promote fast food."], 5,
  "슬로시티는 건강, 자연, 이웃 간의 좋은 관계를 중시하고 ‘빠름’을 거부한다. ‘빠르게 성장’과 ‘패스트푸드 홍보’는 본문과 반대이고, 1999년 이후 Chianti에 관한 내용은 근거가 없으며, ‘관광객 금지’는 Try visiting a Slow City와 어긋난다."),
]),
("u4", "Unit 4 · Science — The Theory of the Four Elements", [
 (1, "어휘", VOC + "\n\n“very strong and impossible to break or destroy”",
  "indestructible", ["delicious", "ancient", "useful", "modern"], 5,
  "indestructible(파괴할 수 없는). Empedocles also believed that these elements were indestructible…"),
 (2, "세부 사실", "윗글에서 Empedocles가 말한 네 가지 원소에 해당하지 *않는* 것은?",
  "wood", ["water", "fire", "earth", "air"], 3,
  "These elements were water, fire, earth, and air. 나무(wood)는 포함되지 않는다."),
 (3, "주제", "윗글의 주제로 가장 적절한 것은?",
  "Empedocles’s theory that four elements make up all things",
  ["the life of Greek philosophers", "how to cook food over a fire", "the modern periodic table", "why air cools down food"], 2,
  "모든 물질이 네 원소로 이루어졌다는 Empedocles의 이론과 그 근거(항아리·식사)를 설명한 글이다."),
 (4, "내용 일치", "윗글의 내용과 일치하는 것은?",
  "Empedocles’s theories inspired later scientists to study the elements.",
  ["Empedocles was a Roman philosopher.", "Pots were cooled with water after being burned.", "Empedocles believed the elements could easily change.", "Only two elements were needed to make a pot."], 1,
  "Empedocles는 그리스(Greek) 철학자이다(Roman ✗). 항아리는 불에 구운 뒤 공기로 식혔다(water ✗). 원소는 변하지 않는다고 믿었다(easily change ✗). 항아리를 만드는 데 네 원소가 모두 필요했다(two elements ✗)."),
 (5, "요약문 완성", SUM + "\n\nEmpedocles (A) ______ that four elements made up every substance, and he believed these elements could not be (B) ______.",
  "(A) theorized …… (B) destroyed",
  ["(A) forgot …… (B) destroyed", "(A) denied …… (B) changed", "(A) theorized …… (B) seen", "(A) forgot …… (B) mixed"], 4,
  "Empedocles theorized that four elements made up every substance…, believed that these elements were indestructible(파괴될 수 없는)."),
]),
("u5", "Unit 5 · Art — Teddy Bears Throughout Time", [
 (1, "어휘", VOC + "\n\n“to say no to something that is offered to you; not to accept or do something”",
  "refuse", ["display", "tie", "bring", "feature"], 4,
  "refuse(거절하다). Roosevelt refused to kill a bear…"),
 (2, "세부 사실", "윗글에 따르면, ‘teddy bear’라는 이름은 누구의 별명에서 나왔는가?",
  "U.S. president Theodore Roosevelt",
  ["a famous toy maker", "the writer of Winnie the Pooh", "a hunter in England", "a museum owner in Japan"], 5,
  "…in honor of the president’s nickname, Teddy. (Theodore Roosevelt)"),
 (3, "제목", "윗글의 제목으로 가장 적절한 것은?",
  "The Story and Lasting Popularity of Teddy Bears",
  ["How to Hunt Bears Safely", "Famous Presidents of the United States", "The Best Toy Museums in Korea", "Why Children Like Picture Books"], 1,
  "테디베어의 이름 유래와 오랫동안 이어진 인기를 다룬 글이다."),
 (4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
  "Winnie the Pooh was originally written for children.",
  ["Roosevelt refused to kill a bear tied to a tree.", "Teddy bears became mass-produced in the twentieth century.", "Teddy bears were made in many sizes, colors, and materials.", "There is a teddy bear museum in South Korea."], 3,
  "Winnie the Pooh, which was originally written for adults — 원래 어른을 위해 쓰였다."),
 (5, "추론", "윗글을 통해 추론할 수 있는 것으로 가장 적절한 것은?",
  "Many Americans admired Roosevelt’s choice not to kill the bear.",
  ["Teddy bears were popular only in America.", "Roosevelt made the first teddy bear himself.", "Teddy bears will soon lose their popularity.", "Paddington Bear was the very first teddy bear."], 2,
  "이야기를 들은 사람들이 대통령을 기리기 위해(in honor of) 곰 인형을 만들었다. 세계 여러 나라에 박물관이 있으므로 ‘미국에서만’은 틀리고, 나머지 선택지는 근거가 없거나 본문과 반대이다."),
]),
("u6", "Unit 6 · Nature — Osmosis in Everyday Life", [
 (1, "어휘", VOC + "\n\n“to take something away from a place”",
  "remove", ["pickle", "taste", "drink", "grow"], 1,
  "remove(제거하다). We use reverse osmosis to remove salt…"),
 (2, "세부 사실", "윗글에 따르면, brine(소금물)은 무엇으로 이루어져 있는가?",
  "water, salt, and seasonings",
  ["water, sugar, and oil", "salt, vinegar, and sugar", "seawater and vegetables", "water and black pepper only"], 2,
  "a brine—a mixture of water, salt, and seasonings."),
 (3, "주제", "윗글의 주제로 가장 적절한 것은?",
  "osmosis and its uses in everyday life",
  ["how to grow fresh vegetables", "the dangers of drinking seawater", "the history of pickles", "how molecules are created"], 5,
  "삼투 현상이 무엇인지, 그리고 피클 만들기·바닷물 정수처럼 일상에서 어떻게 쓰이는지 설명한 글이다."),
 (4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
  "Pickled vegetables become soft because of osmosis.",
  ["Molecules are always moving.", "During pickling, water moves out of vegetables into the brine.", "The skin of a vegetable acts as a semi-permeable membrane.", "Reverse osmosis uses pressure to remove salt from seawater."], 4,
  "…it is why pickled vegetables stay crunchy. 삼투 때문에 피클은 아삭함을 유지한다."),
 (5, "요약문 완성", SUM + "\n\nOsmosis (A) ______ the concentration on both sides of a membrane, and reverse osmosis makes seawater (B) ______.",
  "(A) equalizes …… (B) drinkable",
  ["(A) increases …… (B) salty", "(A) stops …… (B) drinkable", "(A) equalizes …… (B) salty", "(A) increases …… (B) colorful"], 3,
  "This equalizes the concentration… / remove salt… Afterward, we can drink the water! 따라서 (A) equalizes, (B) drinkable."),
]),
("u7", "Unit 7 · Social Studies — Majority Rule in Democracies", [
 (1, "어휘", VOC + "\n\n“a type of government in which people choose their rulers by voting for them in elections”",
  "democracy", ["victory", "ballot", "option", "citizen"], 3,
  "democracy(민주주의). Most democracies elect public officials…"),
 (2, "세부 사실", "윗글에 따르면, majority rule(다수결)에 대한 설명으로 옳은 것은?",
  "The option that gets the most votes wins.",
  ["The oldest person makes the decision.", "Everyone must agree on one option.", "The president always chooses the winner.", "The option with the fewest votes wins."], 4,
  "The option that gets the most votes is the winner. This is called majority rule."),
 (3, "주제", "윗글의 주제로 가장 적절한 것은?",
  "majority rule and the conditions needed to make it fair",
  ["how to become a public official", "the history of political parties", "why secret ballots are dangerous", "countries that have no elections"], 2,
  "다수결의 의미와 한계, 공정한 다수결을 위한 조건을 다룬 글이다."),
 (4, "내용 불일치", "윗글의 내용과 일치하지 *않는* 것은?",
  "Some people’s votes should count more than others’.",
  ["A slim margin, such as 51% to 49%, can decide an election.", "With more than two parties, a party can win with less than 50% of the votes.", "Under majority rule, almost half of the people may not get their choice.", "People should be able to vote with secret ballots."], 5,
  "each person’s vote should be weighted equally — 모든 사람의 표는 똑같은 무게를 가져야 한다."),
 (5, "추론", "윗글의 글쓴이가 가장 동의할 만한 것은?",
  "Majority rule works best when the opinions of other voters are also respected.",
  ["Majority rule is always perfectly fair.", "Winners should ignore people who voted for other parties.", "Secret ballots make elections less fair.", "A democracy should have only one political party."], 1,
  "마지막 문단: 승리한 정당은 다른 유권자의 의견을 고려해야 하며, 민주주의는 모든 시민의 평등을 보장해야 한다. 글쓴이는 다수결이 ‘항상 공정한지’ 의문을 제기하므로 always perfectly fair는 틀리다."),
]),
("u8", "Unit 8 · Science — The Rising Prominence of Telescopes", [
 (1, "어휘", VOC + "\n\n“a scientist who studies the stars, planets, and other natural objects in space”",
  "astronomer", ["dentist", "architect", "farmer", "painter"], 2,
  "astronomer(천문학자). …to help astronomers observe not just the stars…"),
 (2, "세부 사실", "윗글에 따르면, Galileo의 망원경은 이미지를 최대 몇 배까지 확대했는가?",
  "thirty times", ["three times", "five times", "ten times", "twenty times"], 5,
  "…magnified it up to thirty times!"),
 (3, "주제", "윗글의 주제로 가장 적절한 것은?",
  "the development of telescopes over time",
  ["how to build a telescope at home", "the life of Galileo", "why stars are used as maps", "the dangers of space travel"], 4,
  "Galileo → Kepler → Hubble로 이어지는 망원경의 발전 과정을 설명한 글이다."),
 (4, "내용 일치", "윗글의 내용과 일치하는 것은?",
  "Kepler’s telescope had a wider field of view than Galileo’s.",
  ["Galileo’s telescope gave clear but upside-down images.", "Kepler’s telescope used a concave eyepiece.", "Telescopes were first used to take pictures of planets.", "The Hubble Telescope sits on top of a mountain on Earth."], 1,
  "Galileo의 이미지는 똑바로 섰지만 흐릿했다(upside-down ✗). Kepler는 볼록(convex) 접안렌즈를 썼다(concave ✗). 망원경은 처음에 먼 거리를 보는 데 쓰였다(pictures of planets ✗). Hubble은 지구 궤도를 돈다(mountain ✗)."),
 (5, "요약문 완성", SUM + "\n\nKepler (A) ______ Galileo’s design to get a wider field of view, and today telescopes like the Hubble are (B) ______ into space.",
  "(A) improved …… (B) launched",
  ["(A) copied …… (B) dropped", "(A) improved …… (B) buried", "(A) destroyed …… (B) launched", "(A) copied …… (B) sold"], 3,
  "Kepler improved on Galileo’s design… / telescopes have been launched into space."),
]),
]

LEVEL = {1: "매우 쉬움", 2: "쉬움", 3: "보통", 4: "다소 어려움", 5: "어려움"}

sections, qno = [], 0
for key, title, qs in U:
    items = [{"type": "passage", "title": f"[{qno+1}~{qno+5}] 다음 글을 읽고 물음에 답하시오.", "text": P[key]}]
    for lv, kind, prompt, ans, wrong, pos, expl in qs:
        assert len(wrong) == 4 and ans not in wrong
        ch = list(wrong); ch.insert(pos - 1, ans)
        items.append({"type": "multiple_choice", "prompt": prompt, "choices": ch, "answer": pos,
                      "points": 2.5, "explanation": f"[난이도 {lv}·{LEVEL[lv]} / {kind}] {expl}"})
        qno += 1
    sections.append({"title": title, "items": items})

# 정답 번호 분포 확인
from collections import Counter
dist = Counter(it["answer"] for s in sections for it in s["items"] if it["type"] != "passage")
assert qno == 40 and set(dist.values()) == {8}, dist

doc = {
  "title": "The Reading 7-1 Final Test",
  "meta": {"subject": "영어 독해", "grade": "Level 7 (중1 수준)", "unit": "Unit 1~8", "time_limit": "50분"},
  "student_fields": ["반", "이름", "점수"],
  "instructions": [
    "총 40문항, 모두 5지선다형 객관식이며 문항당 2.5점(100점 만점)입니다.",
    "*70점 이상(28문항 이상 정답)이면 합격*입니다.",
    "각 문항에서 가장 알맞은 답을 하나만 고르세요.",
  ],
  "layout": {"columns": 1, "font_size": 9.5, "show_points": True, "choice_columns": 0, "section_pagebreak": True},
  "sections": sections,
}
out = Path(sys.argv[1] if len(sys.argv) > 1 else "TheReading_7-1_FinalTest.json")
out.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, dict(sorted(dist.items())))
