"""
The Myers–Briggs Indicator (MBTI) personality test was developed in the 1940s by American Psychologists Katherine Cook Briggs and Isabel Briggs Meyrs.
The test identifies 16 personality types which are grouped by four pairs of opposite preferences: ",
    "* extraversion (E) or introversion (I),",
    "* sensing (S) or intuition (N),",
    "* thinking (T) or feeling (F),",
    "* and judging (J) or perceiving (P).",
    "",
    "Combinations of one letter from each pair results in 16 unique four-letter combinations:",
    "",
    "**Analysts**",
    "* INTJ: Architect",
    "* INTP: Logician",
    "* ENTJ: Commander",
    "* ENTP: Debater",
    "",
    "**Diplomats**",
    "* INFJ: Advocate",
    "* INFP: Mediator",
    "* ENFJ: Protagonist",
    "* ENFP: Campaigner",
    "  ",
    "**Sentinels**",
    "* ISTJ: Logistician",
    "* ISFJ: Defender",
    "* ESTJ: Executive",
    "* ESFJ: Consul",
    "  ",
    "**Explorers**",
    "* ISTP: Virtuoso",
    "* ISFP: Adventurer",
    "* ESTP: Entrepreneur",
    "* ESFP: Entertainer",
"""

MBTI_MEANINGS = {
    "INTJ": "Architect – Imaginative and strategic thinkers",
    "INTP": "Logician – Innovative inventors with a thirst for knowledge",
    "ENTJ": "Commander – Bold, imaginative leaders",
    "ENTP": "Debater – Smart and curious thinkers",
    "INFJ": "Advocate – Quiet and inspiring idealists",
    "INFP": "Mediator – Poetic, kind and altruistic",
    "ENFJ": "Protagonist – Charismatic and inspiring leaders",
    "ENFP": "Campaigner – Enthusiastic and creative free spirits",
    "ISTJ": "Logistician – Practical and fact-minded individuals",
    "ISFJ": "Defender – Warm and responsible protectors",
    "ESTJ": "Executive – Excellent administrators and managers",
    "ESFJ": "Consul – Caring, social and popular",
    "ISTP": "Virtuoso – Bold and practical experimenters",
    "ISFP": "Adventurer – Flexible and charming artists",
    "ESTP": "Entrepreneur – Smart, energetic and perceptive",
    "ESFP": "Entertainer – Spontaneous, energetic, and fun-loving"
}


personalities = {}
personalities["ENTJ"] = "Strategic, logical, efficient, outgoing, ambitious, independent Effective organizers of people and long-range planners"
personalities["ENFJ"] = "Caring, enthusiastic, idealistic, organized, diplomatic, responsible Skilled communicators who value connection with people"
personalities["ESFJ"] = "Friendly, outgoing, reliable, conscientious, organized, practical Seek to be helpful and please others, enjoy being active and productive"
personalities["ESTJ"] = "Efficient, outgoing, analytical, systematic, dependable, realistic Like to run the show and get things done in an orderly fashion"
personalities["ENTP"] = "Inventive, enthusiastic, strategic, enterprising, inquisitive, versatile Enjoy new ideas and challenges, value inspiration"
personalities["ENFP"] = "Enthusiastic, creative, spontaneous, optimistic, supportive, playful Value inspiration, enjoy starting new projects, see potential in others"
personalities["ESFP"] = "Playful, enthusiastic, friendly, spontaneous, tactful, flexible Have strong common sense, enjoy helping people in tangible ways"
personalities["ESTP"] = "Outgoing, realistic, action-oriented, curious, versatile, spontaneous Pragmatic problem solvers and skillful negotiators"
personalities["INTP"] = "Intellectual, logical, precise, reserved, flexible, imaginative Original thinkers who enjoy speculation and creative problem solving"
personalities["INFP"] = "Sensitive, creative, idealistic, perceptive, caring, loyal Value inner harmony and personal growth, focus on dreams and possibilities"
personalities["ISFP"] = "Gentle, sensitive, nurturing, helpful, flexible, realistic Seek to create a personal environment that is both beautiful and practical"
personalities["ISTP"] = "Action-oriented, logical, analytical, spontaneous, reserved, independent Enjoy adventure, skilled at understanding how mechanical things work"
personalities["INTJ"] = "Innovative, independent, strategic, logical, reserved, insightful Driven by their own original ideas to achieve improvements"
personalities["INFJ"] = "Idealistic, organized, insightful, dependable, compassionate, gentle Seek harmony and cooperation, enjoy intellectual stimulation"
personalities["ISFJ"] = "Warm, considerate, gentle, responsible, pragmatic, thorough Devoted caretakers who enjoy being helpful to others"
personalities["ISTJ"] = "Responsible, sincere, analytical, reserved, realistic, systematic Hardworking and trustworthy with sound practical judgment"


MBTI_TEXT_SAMPLES = {
    "INTJ": [
        "I prefer working independently on complex strategic problems and long term planning.",
        "I enjoy designing systems and thinking critically about theoretical frameworks.",
        "I like analysing data and building efficient solutions to difficult problems.",
        "I am drawn to long range strategy and enjoy working alone on intellectually demanding tasks.",
        "I find satisfaction in mastering complex subjects and applying them to build better systems.",
        "I prefer solitude when thinking and tend to plan everything carefully before acting.",
        "I enjoy setting ambitious goals and working methodically toward them without distraction.",
        "I like to understand the underlying logic of systems and improve them through careful analysis.",
    ],
    "INTP": [
        "I love exploring abstract ideas and questioning assumptions about how things work.",
        "I enjoy logic puzzles theoretical debates and understanding underlying principles.",
        "I like to analyse systems and find innovative conceptual solutions.",
        "I am fascinated by theories and enjoy spending hours thinking through complex problems alone.",
        "I prefer to understand the why behind everything rather than just following instructions.",
        "I enjoy debating ideas and exploring multiple logical frameworks before reaching a conclusion.",
        "I like working independently on open ended intellectual problems with no fixed answer.",
        "I find routine boring and prefer exploring new concepts and unconventional approaches.",
    ],
    "INFJ": [
        "I am deeply empathetic and enjoy helping others achieve their personal growth goals.",
        "I like meaningful conversations about values and making a positive impact on society.",
        "I am intuitive about people feelings and enjoy counselling and guiding others.",
        "I prefer deep one on one conversations over large social gatherings.",
        "I am driven by a sense of purpose and want my work to contribute to something meaningful.",
        "I often sense what others are feeling before they say it and try to support them quietly.",
        "I enjoy writing and reflecting on ideas that connect personal values to broader human themes.",
        "I like helping individuals find clarity and direction in their lives through thoughtful guidance.",
    ],
    "INFP": [
        "I value creativity self expression and authentic connections with people around me.",
        "I enjoy writing art and exploring emotions through creative and imaginative projects.",
        "I care deeply about helping others and expressing my inner values through my work.",
        "I am idealistic and often imagine how the world could be better and more compassionate.",
        "I prefer working on projects that feel personally meaningful rather than purely practical.",
        "I enjoy quiet reflection and expressing my feelings through creative writing or art.",
        "I am sensitive to the emotions of others and try to create harmony in my relationships.",
        "I like exploring philosophical questions about identity meaning and human connection.",
    ],
    "ISTJ": [
        "I am reliable organised and prefer clear procedures and structured environments.",
        "I like following established methods maintaining accurate records and meeting deadlines.",
        "I value responsibility consistency and working systematically through detailed tasks.",
        "I prefer predictable routines and feel most productive when I have a clear plan to follow.",
        "I take my commitments seriously and always follow through on what I promise.",
        "I like working with facts and data and prefer proven methods over experimental approaches.",
        "I enjoy maintaining order and ensuring that processes run smoothly and efficiently.",
        "I am thorough and detail oriented and I rarely make mistakes when I follow a structured process.",
    ],
    "ISTP": [
        "I enjoy hands on problem solving working with tools and understanding how things work.",
        "I like troubleshooting technical systems and finding practical efficient solutions.",
        "I prefer working independently with flexible spontaneous approach to challenges.",
        "I am calm under pressure and enjoy figuring out how mechanical or technical systems operate.",
        "I like to observe situations carefully before acting and prefer practical solutions over theory.",
        "I enjoy working with my hands and find satisfaction in fixing or building physical things.",
        "I prefer to stay flexible and respond to situations as they arise rather than planning ahead.",
        "I am independent and self reliant and I prefer to solve problems on my own terms.",
    ],
    "ISFJ": [
        "I am caring supportive and dedicated to helping others in practical everyday ways.",
        "I enjoy providing care nurturing environments and maintaining harmony in teams.",
        "I like routine and dependable work that allows me to support and protect others.",
        "I am attentive to the needs of others and enjoy making people feel comfortable and cared for.",
        "I prefer stable predictable environments where I can focus on helping those around me.",
        "I take pride in being dependable and always showing up for the people who count on me.",
        "I enjoy organising and maintaining systems that help others function smoothly.",
        "I am patient and thorough and I like to make sure everyone feels included and supported.",
    ],
    "ISFP": [
        "I enjoy artistic expression working at my own pace and experiencing the present moment.",
        "I like creative hands on activities and expressing my feelings through visual art.",
        "I value kindness beauty and helping others in quiet behind the scenes ways.",
        "I am gentle and easy going and I prefer to avoid conflict and keep things harmonious.",
        "I enjoy spending time in nature and find inspiration in the beauty of everyday experiences.",
        "I like working on creative projects that allow me to express my personal aesthetic.",
        "I prefer to act on my feelings rather than follow rigid plans or schedules.",
        "I am observant and sensitive and I notice small details that others often overlook.",
    ],
    "ENTJ": [
        "I excel at leading teams setting ambitious goals and driving strategic execution.",
        "I enjoy managing complex projects making decisive choices and inspiring leadership.",
        "I like organising people resources and processes to achieve maximum efficiency.",
        "I am confident and decisive and I enjoy taking charge of situations that require strong leadership.",
        "I like setting high standards and pushing teams to achieve results that exceed expectations.",
        "I enjoy strategic planning and find satisfaction in turning ambitious visions into reality.",
        "I am direct and assertive and I prefer to make decisions quickly based on logic and data.",
        "I thrive in competitive environments and enjoy the challenge of leading large scale initiatives.",
    ],
    "ENTP": [
        "I love debating new ideas challenging conventional thinking and exploring possibilities.",
        "I enjoy brainstorming creative solutions and arguing multiple perspectives on problems.",
        "I like entrepreneurial ventures innovation and rapidly generating novel concepts.",
        "I am energised by intellectual debate and enjoy challenging assumptions with counterarguments.",
        "I like exploring unconventional ideas and finding creative ways to solve complex problems.",
        "I enjoy working with others to brainstorm and prototype new concepts quickly.",
        "I am adaptable and thrive in fast changing environments where I can experiment freely.",
        "I like to question the status quo and find better more innovative ways of doing things.",
    ],
    "ENFJ": [
        "I am passionate about inspiring others mentoring teams and facilitating group growth.",
        "I love building relationships supporting personal development and leading collaboratively.",
        "I enjoy teaching coaching and helping communities achieve shared meaningful goals.",
        "I am energised by connecting with people and helping them reach their full potential.",
        "I enjoy leading groups and creating environments where everyone feels valued and motivated.",
        "I like facilitating discussions and helping teams work through challenges collaboratively.",
        "I am empathetic and charismatic and I naturally take on the role of mentor or guide.",
        "I find deep satisfaction in seeing others grow and succeed because of my support.",
    ],
    "ENFP": [
        "I am enthusiastic creative and love connecting people with exciting new opportunities.",
        "I enjoy exploring possibilities meeting diverse people and inspiring others with ideas.",
        "I like brainstorming campaigns advocacy and energising teams with optimistic vision.",
        "I am curious and open minded and I love learning about new ideas and meeting new people.",
        "I enjoy working on creative projects that allow me to express my imagination and enthusiasm.",
        "I am energised by social interaction and love inspiring others with my ideas and energy.",
        "I like exploring many different possibilities and I often pursue multiple interests at once.",
        "I am spontaneous and adaptable and I thrive in environments that allow for creative freedom.",
    ],
    "ESTJ": [
        "I am organised decisive and excellent at managing teams to meet operational goals.",
        "I like establishing clear processes enforcing standards and delivering reliable results.",
        "I enjoy leading projects coordinating logistics and maintaining productive structured teams.",
        "I prefer clear hierarchies and well defined roles and I hold myself and others accountable.",
        "I am practical and results oriented and I like to get things done efficiently and on time.",
        "I enjoy managing operations and ensuring that systems and processes run smoothly.",
        "I like setting clear expectations and following through with consistent disciplined execution.",
        "I am direct and confident and I prefer straightforward communication over ambiguity.",
    ],
    "ESTP": [
        "I thrive in fast paced environments and excel at quick pragmatic problem solving.",
        "I enjoy action oriented challenges negotiation and persuading others with direct energy.",
        "I like taking risks adapting quickly and solving immediate real world problems.",
        "I am bold and energetic and I enjoy jumping into action without overthinking.",
        "I like working in dynamic environments where I can respond quickly to changing situations.",
        "I enjoy persuading others and thrive in competitive high stakes situations.",
        "I am observant and resourceful and I find practical solutions to problems on the spot.",
        "I prefer hands on experience over theory and I learn best by doing.",
    ],
    "ESFJ": [
        "I care about community harmony and enjoy organising social events and supporting others.",
        "I like working with people creating welcoming environments and fulfilling social duties.",
        "I enjoy caring professions where I can support and nurture others in practical ways.",
        "I am warm and sociable and I enjoy making others feel welcome and appreciated.",
        "I like organising group activities and ensuring that everyone feels included and valued.",
        "I am attentive to the needs of others and enjoy providing practical support and care.",
        "I prefer structured environments where I can contribute to the wellbeing of a community.",
        "I find satisfaction in maintaining harmony and helping groups work together effectively.",
    ],
    "ESFP": [
        "I am spontaneous energetic and love entertaining and engaging with people around me.",
        "I enjoy performing collaborating in lively teams and bringing fun to every situation.",
        "I like people centred work that lets me express enthusiasm and bring joy to others.",
        "I am outgoing and playful and I love being the centre of attention in social settings.",
        "I enjoy living in the moment and bringing energy and excitement to everything I do.",
        "I like working with people and find satisfaction in making others laugh and feel good.",
        "I am adaptable and spontaneous and I prefer variety and excitement over routine.",
        "I thrive in lively social environments and enjoy collaborating with enthusiastic teams.",
    ],
}


MBTI_DESCRIPTIONS = {
    'ENTJ': 'The Commander: Strategic leaders, motivated to organize change',
    'INTJ': 'The Mastermind: Analytical problem-solvers, eager to improve systems and processes',
    'ENTP': 'The Visionary: Inspired innovators, seeking new solutions to challenging problems',
    'INTP': 'The Architect: Philosophical innovators, fascinated by logical analysis',
    'ENFJ': 'The Teacher: Idealist organizers, driven to do what is best for humanity',
    'INFJ': 'The Counselor: Creative nurturers, driven by a strong sense of personal integrity',
    'ENFP': 'The Champion: People-centered creators, motivated by possibilities and potential',
    'INFP': 'The Healer: Imaginative idealists, guided by their own values and beliefs',
    'ESTJ': 'The Supervisor: Hardworking traditionalists, taking charge to get things done',
    'ISTJ': 'The Inspector: Responsible organizers, driven to create order out of chaos',
    'ESFJ': 'The Provider: Conscientious helpers, dedicated to their duties to others',
    'ISFJ': 'The Protector: Industrious caretakers, loyal to traditions and institutions',
    'ESTP': 'The Dynamo: Energetic thrillseekers, ready to push boundaries and dive into action',
    'ISTP': 'The Craftsperson: Observant troubleshooters, solving practical problems',
    'ESFP': 'The Entertainer: Vivacious entertainers, loving life and charming those around them',
    'ISFP': 'The Composer: Gentle caretakers, enjoying the moment with low-key enthusiasm'
}

"""
The Jungian 4-letter framework has less predictive accuracy than the Big Five,
mostly due to its use of binary types and its failure to measure Neuroticism.

Four Jungian traits aligned with four of the Big Five traits.
Extraversion in the Jungian test mirrored Big Five's Extraversion,
Intuitiveness mirrored Openness, and Feeling resembled Agreeableness.
Finally, the Jungian Judging trait correlated with three Big Five
traits: positively with Conscientiousness
and negatively with Extraversion and Openness.

MBTI 	Big Five
Intuition/Sensing 	Openness to experience (corellates with N)
Feeling/Thinking 	Agreeableness (correlates with F)
Perception/Judging 	Conscientiousness (correlates with J)
Introversion/Extraversion 	Extraversion (correlates with E)
not available in MBTI 	Neuroticism

1. Extraversion (E) / Introversion (I)
    E (Extraversion): Social, outgoing, energetic, talkative, enthusiastic, assertive, spontaneous, charismatic.
    I (Introversion): Reserved, quiet, reflective, private, thoughtful, reserved, observant, independent.

2. Sensing (S) / Intuition (N)
    S (Sensing): Practical, detail-oriented, factual, precise, loyal, dependable, organized, literal.
    N (Intuition): Visionary, imaginative, creative, pattern-seeking, strategic, unconventional, future-focused, insightful.

3. Thinking (T) / Feeling (F)
    T (Thinking): Logical, analytical, objective, decisive, skeptical, systematic, efficient, independent.
    F (Feeling): Empathetic, compassionate, value-driven, considerate, kind, sensitive, idealistic, harmonious.

4. Judging (J) / Perceiving (P)
    J (Judging): Organized, structured, decisive, reliable, proactive, methodical, responsible, closure-oriented.
    P (Perceiving): Flexible, open-minded, spontaneous, adaptable, curious, observant, casual, open-ended.
"""

"""
ESTP
    Fun Get-it-done Active Hands-on Practical Observant Talkative Take-Charge Inventive Charming 

ESTJ
    Take Charge Logic-driven Decisive Tenacious Fast Dependable Proactive High Energy Outspoken Straightforward 

ESFP
    Kinesthetic Free-Spirited In the Moment Fun Easy-Going Casual Entertaining Sympathetic Sensitive Talkative 

ESFJ
    Sensitive Talkative Responsible Generous Attentive Enthusiastic Affectionate Sympathetic Warm Outgoing 

ENTP
    Creative Tenacious Funny Clever Futuristic Skeptical Independent Strategic Unconventional Adaptable 

ENTJ
    Tenacious Assertive Strategic Innovative Proactive High-Energy Bold Confident Decisive Take Charge 

ENFP
    Collaborative Visionary Insightful Spontaneous Casual Imaginative Sensitive Energetic Gregarious Idealistic 

ENFJ
    Values-Driven Affectionate Creative Visionary Charismatic Planful Talkative Idealistic Empathetic Sensitive 

ISTP
    In the moment Quiet Unflappable Down-to-earth Concise Realistic Logic-driven Spontaneous Level-headed Private 

ISTJ
    Clear Methodical Loyal Precise Realistic Reserved Meticulous Responsible Accurate Literal 

ISFP
    Free-spirited Unassuming Observant Reserved In the moment Private Spontaneous Kind Sensitive Quiet 

ISFJ
    Planful Decisive Reserved Precise Sensitive Private Literal Sympathetic Efficient Accommodating 

INTP
    Independent Analytical Private Unconventional Skeptical Logic-Driven Witty Original Internally-Motivated Disorganized 

INTJ
    Independent Deep Reserved Intellectual Intense Future-focused Driven Tenacious Direct Private 

INFP
    Sensitive Caring Spontaneous Calm Unique Reserved Modest Casual Empathetic Flexible 

INFJ
    Visionary Sensitive Reserved Private Idealistic Planful Conscientious Value-Driven Empathetic Perfectionistic
"""

PAIR_ENNEAGRAM_MBTI = {
    "reformer": {
        'ESTJ' : "among the most common pairings for this type. Combines hands-on management and clear direction with the Type 1 drive toward doing thing.",
        'ESFJ' : "brings together a deep need to care for others with an equally deep need to do things the right way. Focus on harmony and making people feel welcome.",
        'ENFJ' : "The most natural and frequently observed pairings in typology. Both systems describe a personality oriented toward interpersonal connection, emotional attunement. Produces principled, idealistic leaders with a strong moral compass and a gift for inspiring others toward ethical action. Natural charisma and people-orientation.",
        'ENTJ' : "one of the more common pairings for this type. It brings together the ENTJ pattern of bold, forward-moving leadership with the Type 1 drive toward correctness and reform.",
        'ESTP' : "Combination is rare. Most ESTPs are drawn to action and excitement with little concern for rules.",
        'ESFP' : "one of the rarest pairings in personality research. Most ESFPs move through life with a loose, open grip on plans and rules.",
        'ENFP' : "Rare pairing that produces idealistic, enthusiastic individuals who combine creative vision with a deep desire to connect and care for others. Individuals channel their creative energy into moral and social causes.",
        'ENTP' : "rarest pairing. Known for flexible thinking, rapid...",
        'ISTJ' : "Most common pairing for ISTJs. Oriented toward duty, order, and doing things correctly.",
        'ISFJ' : "A person who is deeply careful, responsible, and driven by a quiet need to do things the right way. ISFJs are known for steady service.",
        'INFJ' : "quiet, determined person driven by a clear picture of how the world should work. Tends to look inward, think deeply about people, and care about meaning.",
        'INTJ' : "One of the most common pairings for this type. This combination brings together the INTJ pattern of long-range planning and independent thinking of Type 1.",
        'ISTP' : "Uncommon pairing, with roughly 3% of ISTPs identifying as Type 1. The ISTP's hands-on, flexible problem-solving.",
        'ISFP' : "Rare pairing. The ISFP's flexible, values-based nature merges with the One's structured perfectionism, creating individuals who hold strong personal aesthetic and morals.",
        'INFP' : "known for their quiet emotional depth, strong personal values, and gentle nature. Has s a powerful drive toward moral correctness and self-improvemen.",
        'INTP' : "One of the rarer pairings. The combination brings together the INTP pattern of deep, open-ended thinking with the Type 1 drive.",
    },
    "helper": {
        'ESTJ' : "An uncommon profile that combines the ESTJ's love of order and clear results with the Two's deep need to be helpful and valued.",
        'ESFJ' : "The most common Enneagram pairing for ESFJs. Both the ESFJ pattern and Enneagram Two point in the same direction: toward other people.",
        'ENFJ' : "",
        'ENTJ' : "Uncommon blend creates leaders who want to win and want to be loved for winning. The ENTJ side brings big-picture planning, fast decisions, and a push toward results.",
        'ESTP' : "An uncommon combination brings together the ESTP's bold, hands-on energy with the Two's deep need to be valued by others.",
        'ESFP' : "One of the most hands-on, physically generous profiles across all personality combinations. ESFPs are already drawn to people and shared experiences, but the Two's deep need to be loved.",
        'ENFP' : "",
        'ENTP' : "Uncommon pairing of fast-moving curiosity and love of debate with deep need to be close to others and feel valued.",
        'ISTJ' : "An uncommon pairing. The ISTJ is known for following through on duties and keeping things organized. Type Two is known for wanting to help others and feel appreciated.",
        'ISFJ' : "One of the most naturally service-oriented profiles in personality research. It is the most common Enneagram pairing for the ISFJ. Both patterns share a deep focus on other people.",
        'INFJ' : "A quiet, inward-looking personality with a strong pull toward caring for others. What sets this profile apart is a deep, private awareness of what other people feel and need.",
        'INTJ' : "A rare pairing. The INTJ is known for being independent and focused on ideas. Type Two is known for wanting to help and be close to others.",
        'ISTP' : "An uncommon profile, with roughly 3% of ISTPs falling into this space in large-sample research. This combination pairs the ISTP's quiet self-reliance with the Two's pull toward helping others.",
        'ISFP' : "quietly nurturing individuals who combine the ISFP's aesthetic sensitivity with the Two's desire to care for others. This pairing creates gentle, hands-on helpers.",
        'INFP' : "Blends INFP's deep inner emotional life with a drive to care for others. These individuals tend to be quiet, gentle helpers.",
        'INTP' : "One of the rarest profiles in personality science. in large studies. The INTP is a quiet thinker who enjoys ideas and logic. The Two is a helper who needs to feel close to others.",
        },
    "achiever": {
        'ESTJ' : "Pairing is the most common for ESTJs. Both systems point to a person who cares deeply about getting things done, hitting targets, and moving up in their career. This person builds systems.",
        'ESFJ' : "The most frequently observed pairing for ENFJs. This combination produces charismatic, ambitious individuals who excel at motivating others and achieving visible results.",
        'ENFJ' : "One of the most common personality profiles. This person combines the ESFJ's genuine care for others with the Three's hunger for achievement and visible success.",
        'ENTJ' : "One of the most achievement-focused personality profiles that appears in research. This person has natural command and long-range planning,",
        'ESTP' : "Fast-moving, results-driven personality that pairs  taste for action with hunger for visible success.",
        'ESFP' : "A personality built around live performance and visible success. Most ESFPs enjoy being in the middle of social life, responding to whatever is happening around them.",
        'ENFP' : "Among ENFPs, this is a common pairing to make ambitious, charismatic individuals who combine creative vision with a drive for tangible achievement.",
        'ENTP' : "Blends rapid idea generation with a strong pull toward visible results.",
        'ISTJ' : "An uncommon combination that merges a love of order and duty with a persistent hunger for measurable achievement.",
        'ISFJ' : "Rare pairing. The ISFJ's steady, service-focused nature joins with the Three's strong drive toward achievement and recognition. This creates a person who works quietly.",
        'INFJ' : "Combination is rare. The INFJ's quiet, meaning-focused nature joins with the Three's strong push toward goals and visible results. This creates a person who works hard toward success.",
        'INTJ' : "Rare combination that blends deep strategic thinking with a strong drive for visible success.",
        'ISTP' : "Rare pairing that links the ISTP's hands-on problem solving with the Three's drive for measurable success. These individuals do not tinker for the sake of understanding.",
        'ISFP' : "Rare pairing. The ISFP's introspective, authentic nature creates tension with the Three's image-consciousness, producing individuals who desire self-expression.",
        'INFP' : "One of the rarest pairings. This is because the INFP pattern and the Three pattern pull in opposite directions.",
        'INTP' : "One of the rarest pairings. Most INTPs are happy to explore ideas without caring whether anyone notices.",
        },
    "individualist": {
        'ESTJ' : "Combination is one of the rarest in personality research. ESTJs value order, clear rules, and getting things done the right way.",
        'ESFJ' : "Combination is quite rare. This pairing joins warm, hands-on care for others with a deep pull toward personal identity and emotional honesty.",
        'ENFJ' : "Relatively uncommon pairing that produces deeply empathetic, creative individuals with a strong sense of personal identity and emotional depth.",
        'ENTJ' : "Rare pairing. It produces leaders who are not satisfied with success alone. They need what they build to carry personal meaning.",
        'ESTP' : "Combination produces a person whose fast, inventive mind is shaped by a deep need to be seen as one of a kind.",
        'ESFP' : "Combination produces a personality pulled in two different directions at once. Most ESFPs move toward people and activity with easy warmth.",
        'ENFP' : "",
        'ENTP' : "",
        'ISTJ' : "Combination is one of the rarest pairings in personality research, with roughly 2.4% of ISTJs identifying as Type 4 in a 136,288-person study.",
        'ISFJ' : "Combination creates a person who blends quiet devotion to others with the deep need to feel emotionally authentic.",
        'INFJ' : "Combination is one of the most common pairings in personality research. Both patterns point toward a person who lives in their inner world and cares deeply about meaning.",
        'INTJ' : "Combination brings together long-range planning with a deep need to be seen as one of a kind. Most INTJs build systems and solve problems with calm focus.",
        'ISTP' : "A moderately common combination known for quiet self-reliance, mechanical aptitude, and preference for solving problems through direct observation and trial.",
        'ISFP' : "Combination is a common pairing. Both systems describe a personality oriented toward authenticity, aesthetic sensitivity, and deeply personal emotional experience.",
        'INFP' : "Combination is the most common pairing for INFPs. This is one of the strongest links found across all types.",
        'INTP' : "Combination is the second most common pairing for INTPs who are often seen as cool and logical.",
        },
   "investigator": {
        'ESTJ' : "One of the rarest pairings. Most ESTJs are known for stepping into action quickly, taking charge of groups, and making decisions based on practical results.",
        'ESFJ' : "One of the rarest combos. They like to help, host, and stay close to the group. Type 5 moves in the other direction.",
        'ENFJ' : "One of the rarest pairings with the outgoing, people-oriented nature fundamentally contrasting with a withdrawn, resource-conserving orientation.",
        'ENTJ' : "A rare combination that pairs the bold, forward-moving style of the ENTJ with the Five's deep need to understand before acting. Most ENTJs lead by deciding quickly and pushing plans.",
        'ESTP' : "Among the rarest pairings. Most ESTPs move through the world with bold, hands-on energy. They jump into action, test things out, and learn by doing.",
        'ESFP' : "One of the rarest pairings with openness toward people and experiences.",
        'ENFP' : "One of the rarest pairings across both systems. ENFPs tend to be warm, outgoing, and drawn to new people and ideas. Type 5s, by contrast, pull inward.",
        'ENTP' : "Combination brings together a pattern of broad curiosity with a deep need for mastery and self-sufficiency. Most ENTPs move quickly from one idea to the next, gathering surface-level knowledge.",
        'ISTJ' : "One of the most quietly thorough personalities where they typically build reliability through consistent habits and proven methods.",
        'ISFJ' : "Pairs a gentle, service-minded personality with a strong need for private study and careful thought. Most ISFJs are known for their warmth and steady presence in the lives of others.",
        'INFJ' : "Blends a quiet, people-focused nature with a strong pull toward deep study and private thought.",
        'INTJ' : "Most common pairing. Person with deep thinking, careful planning, and a strong need to understand how things work.",
        'ISTP' : "Common pairing describes an independent, analytical personality that values competence and self-sufficiency. The result is a deeply practical.",
        'ISFP' : "Rare pairing of an emotionally engaged, sensory-rich inner world sits in productive tension with a drive to observe, conserve, and understand before acting.",
        'INFP' : "Combination is a rare pairing because INFPs are known for leading with their feelings, while Fives are known for pulling back into their shell.",
        'INTP' : "The most common pairing describes a person who is driven by a deep need to understand how the world works. This person explores ideas.",
       },
    "loyalist": {
        'ESTJ' : "Blends a strong drive for order with a deep need for safety and group loyalty. Combines confidence in rules with a watchful, questioning layer.",
        'ESFJ' : "Combination brings together social warmth and a strong need for safety.",
        'ENFJ' : "A loyal, community-minded individuals who combines natural leadership with dedication to group security and trustworthiness.",
        'ENTJ' : "A leader who pairs bold decision-making with a constant eye on what could go wrong. Most charge forward with confidence, trusting their plans.",
        'ESTP' : "An uncommon combination that is both impulsive and hesitant.",
        'ESFP' : "A personality caught between two strong currents. One side wants to jump into life with both feet, tasting everything, meeting everyone, and staying in motion.",
        'ENFP' : "People who are both curious and careful. They love new ideas and meeting new people, but they also want to know that things are safe and stable.",
        'ENTP' : "A person who is both deeply curious and deeply cautious. Most ENTPs are known for jumping into new ideas with excitement and confidence.",
        'ISTJ' : "Brings together a preference for structure, facts, and proven methods with a deep need for safety and group loyalty.",
        'ISFJ' : "The second most common pairing for ISFJs that describes a personality oriented toward loyalty, security, and the maintenance of trusted relationships and institutions.",
        'INFJ' : "Combination creates a person who pairs deep inner knowing with a steady need for safety.",
        'INTJ' : "Combines long-range planning with a strong focus on safety.",
        'ISTP' : "A common pairing of calm independence and a willingness to take things apart, both physically and mentally.",
        'ISFP' : "A common pairing brings together gentle, values-driven sensitivity with a watchful concern for safety and trustworthiness.",
        'INFP' : "An uncommon but meaningful combination of strong private values and a sharp focus on group safety and loyalty.",
        'INTP' : "Pairs open-ended thinking with a deep need for safety and certainty. , making it an uncommon but notable combination.",
        },
    "enthusiast": {
        'ESTJ' : "Pairs a firm drive for structure with a restless appetite for new experiences. They follow a plan step by step until the job is done.",
        'ESFJ' : "Combination creates a person who blends deep care for others with a strong pull toward new experiences and positive feelings. Most focus on keeping people comfortable.",
        'ENFJ' : "Combination produces charismatic, enthusiastic individuals who bring infectious energy to their social leadership.",
        'ENTJ' : "Combination produces a leader who chases bold ideas with unusual speed and confidence. Focuses on building systems and reaching long-term goals through steady effort.",
        'ESTP' : "The most common for ESTPs. Personality built around action, physical energy, and a strong pull toward new experiences.",
        'ESFP' : "Most common pairing for ESFPs. Tend to be warm, outgoing, and drawn to hands-on activity.",
        'ENFP' : "Most common pairing for ENFPs",
        'ENTP' : "most common pairing for ENTPs. Suggests a fast mind, a love of new ideas.",
        'ISTJ' : "one of the rarest pairings for ISTJs. Combins cautious, duty-oriented nature with a spontaneous, pleasure-seeking drive.",
        'ISFJ' : "One of the rarest pairings for ISFJs. Their cautious, duty-oriented nature contrasts with a spontaneous, pleasure-seeking drive.",
        'INFJ' : "Combination is uncommon. Most are quiet, reflective, and drawn to deep meaning. a pull toward new ideas, bright possibilities, and forward m...",
        'INTJ' : "Uncommon pairing creates a person who combines careful, long-range planning with a strong pull toward new ideas, options, and experiences.",
        'ISTP' : "A personality drawn to hands-on exploration and sensory variety. The result is someone who approaches life as a series of problems.",
        'ISFP' : "Combination produces adventurous, sensory-oriented individuals who combine enthusiasm with love of variety.",
        'INFP' : "This pairing blends quiet inner world with hunger for new and exciting experiences. The result is a person who dreams big.",
        'INTP' : "One of the most idea-hungry profiles in all of personality science.",
        },
    "challenger": {
        'ESTJ' : "Combination is the second most common pairing for ESTJs. Someone who values order, control, and getting results.",
        'ESFJ' : "Combination is uncommon. Most lead with warmth, harmony, and a strong wish to be liked. But this personality wants to stay strong and avoid weakness.",
        'ENFJ' : "",
        'ENTJ' : "Most common pairing for ENTJs, reflecting one of the strongest overlaps in all of typology.",
        'ESTP' : "Combination pairs a hands-on, action-first personality with a deep drive to control one's own world.",
        'ESFP' : "Combination produces a personality that moves through life with unusual physical force and social gravity. Most respond to the world with warmth and playfulness.",
        'ENFP' : "Combination produces a bold, forceful personality that blends creative vision with a deep need to stay in control of their own life.",
        'ENTP' : "Combination brings together quick-minded exploration with a deep need for control and personal strength.",
        'ISTJ' : "One of the most quietly formidable profiles in all of personalities.",
        'ISFJ' : "among the rarest pairings joins a steady, service-driven warmth with the bold need to protect and take charge.",
        'INFJ' : "Combination is one of the rarest pairings that brings together a care for others with a drive to protect and take charge.",
        'INTJ' : "A common pairing brings together the love of long-range planning with the strong drive to take charge and protect what matters to them.",
        'ISTP' : "Combination produces independent, assertive individuals who combine the practical skill and analytical detachment with forceful presence and desire for autonomy.",
        'ISFP' : "Rare pairing of gentle, values-driven nature in sharp contrast with instinct toward power and self-assertion.",
        'INFP' : "One of the rarest combinations that gives emotional depth, strong personal values, and gentle inner world. It adds a fierce drive to protect, confront, and take control.",
        'INTP' : "Uncommon pairing brings together a quiet, thinking mind with a bold, forceful personality.",
        },
    "peacemaker": {
        'ESTJ' : "Uncommon pairing joins the pattern of practical management with the drive toward inner calm and smooth relations.",
        'ESFJ' : "Combination brings together social warmth and a deep pull toward peace. They typically organize their energy around the needs of people close to them.",
        'ENFJ' : "Combination produces gentle, harmonizing leaders who prioritize group cohesion and interpersonal peace above personal ambition. Among ENFJs, this is an uncommon pairing.",
        'ENTJ' : "Rarest pairing.",
        'ESTP' : "Combination is uncommon. Examples want to be bold, fast-moving, and ready to take charge but their deep wish for inner calm softens that boldness into something more relaxed and steady.",
        'ESFP' : "Creates a personality shaped by comfort, warmth, and a quiet pull toward keeping life smooth.",
        'ENFP' : "Combination creates a person who carries a love of ideas and people alongside a deep pull toward peace and togetherness.",
        'ENTP' : "Uncommon pairing creates people who love exploring ideas but do so in a calm, open way rather than through the sharp debate style.",
        'ISTJ' : "Combination produces steady, quietly reliable individuals who blend systematic thoroughness with a deep wish for inner calm.",
        'ISFJ' : "Most common pairing describes a personality oriented toward harmony, accommodation, and the maintenance of peaceful, stable environments.",
        'INFJ' : "Most common pairing makes a person who cares deeply about harmony and understanding. They wish for inner calm.",
        'INTJ' : "Uncommon pairing brings together a strategic, future-focused mind with a deep need for inner calm and peace. The result is a person who thinks in long arcs.",
        'ISTP' : "Common pairing point toward a calm, steady person who prefers to watch and act rather than talk and plan.",
        'ISFP' : "Common pairing",
        'INFP' : "Common pairing. They have quiet depth of feeling, rich inner life, and strong personal values. Plus they have a deep longing for peace, comfort.",
        'INTP' : "A common pairing that combines a love of ideas, quiet independence, and desire to understand how things work.",
        },
}

MBTI_CAREER_PATHS = {
    "INTJ": ["Software Developer/Engineer", "Investment Analyst / Financial Strategist", "Startup Founder / CEO", "Lawyer", "Policy Analyst", "Research Scientist"],
    "INTP": ["Writer", "Professor/Researcher", "Philosopher", "Forensic Scientist", "Astronomer", "Research Scientist"],
    "ENTJ": ["Entrepreneur", "Investment Banker", "Politician", "Military Officer", "Film Director", "Civil Servant"],
    "ENTP": ["Journalist/Investigative Reporter", "Public Speaker", "Podcast Host/Content Creator", "Venture Capitalist", "Tech Startup Founder", "Marketing Strategist"],
    "INFJ": ["Life Coach", "Religious Leader", "Social Worker", "Writer", "Journalist", "Politician"],
    "INFP": ["Counselor/Therapist", "Teacher", "Writer", "Content Creator", "Life Coach", "Musician"],
    "ENFJ": ["CEO/Executive", "Career Counselor", "Politician", "Diplomat", "Human Resources Manager", "Teacher/Professor"],
    "ENFP": ["Graphic Designer", "Blogger/Content Creator", "Researcher", "Interior Designer", "Travel Blogger/Photographer", "Journalist"],
    "ISTJ": ["Accountant", "Lawyer/Judge", "Police Officer/Detective", "Pharmacist", "Banker", "Military Officer"],
    "ISFJ": ["Doctor", "Teacher", "Therapist / Mental Health Counselor", "Human Resources Specialist", "Customer Service Representative", "Bank Teller / Loan Officer"],
    "ESTJ": ["CEO / Business Executive", "Bank Manager", "Lawyer / Judge", "Politician / Civil Servant", "Marketing Director", "Mechanical Engineer"],
    "ESFJ": ["Dietitian / Nutritionist", "Doctor", "Paralegal / Legal Assistant", "Social Worker", "Wedding Planner", "Broadcast Journalist"],
    "ISTP": ["Engineer", "Cybersecurity Analyst", "Military Specialist", "Private Investigator", "Pilot", "Race Car Driver"],
    "ISFP": ["Wildlife Photographer", "Zoologist / Animal Caretaker", "Actor / Dancer / Musician", "Chef", "Yoga Instructor", "Artist / Designer"],
    "ESTP": ["Entrepreneur", "Sales Executive", "Police Officer / Detective", "TV Host / News Anchor", "Professional Athlete", "Bartender / Hospitality Manager"],
    "ESFP": ["Actor / TV Personality", "Fashion Designer / Stylist", "Photographer / Videographer", "Flight Attendant", "Event Planner / Wedding Planner", "Comedian / Entertainer"]
}


def get_description(ptype):
    str_list = []
    if ptype == "INTP":
        str_list.append('This personality is curious, analytical, and idea-driven.')
        str_list.append('They often enjoy systems, theories, and open-ended problem solving.')
        str_list.append('They are highly analytical and can discover connections between two seemingly unrelated things and work best when allowed to use imagination and critical thinking.')
        str_list.append('They like working independently with creative freedom which will help them realise your full potential.')
        str_list.append('In difficult circumstances, they do not like taking orders.')
    elif ptype == "ENTP":
        str_list.append('Freedom-oriented and preferring to act independently to express  creativity and insight.')
        str_list.append('They do not like following rules if they do not make sense and prefer working independently.')
    elif ptype == "INTJ":
        str_list.append('This personality is strategic, independent, and future-focused. INTJs usually enjoy solving complex problems with long-range plans.')
        str_list.append('Somone who prefers to act independently and express their private thinking.')
    elif ptype == "ENTJ":
        str_list.append('This personality is decisive, ambitious, and organized.')
        str_list.append('They tend to lead with structure and big-picture execution.')
        str_list.append('A born leader who can steer the organization towards using their excellent organizing and understanding of what needs to get done.')
    elif ptype == "INFP":
        str_list.append('This personality is Reflective, imaginative, and values-led.')
        str_list.append('They are often drawn to meaningful, creative work.')
        str_list.append('Driven by a strong sense of personal values, they are also highly creative and can offer support from behind the scenes.')
    elif ptype == "ENFP":
        str_list.append('This personality is curious, enthusiastic, and people-oriented.')
        str_list.append('They often shine in creative, exploratory environments..')
        str_list.append('Creative and fun-loving, they excel at careers which allow them to express their ideas and spontaneity.')
    elif ptype == "INFJ":
        str_list.append('This personality is insightful, thoughtful, and purpose-driven.')
        str_list.append('They often mix empathy with long-term vision.')
        str_list.append('Blessed with an idealistic vision, they do best when they seek to make that vision a reality.')
    elif ptype == "ENFJ":
        str_list.append('This personality is supportive, expressive, and motivating.')
        str_list.append('They often enjoy guiding people and building strong teams.')
        str_list.append('They have a gift of encouraging others actualize themselves and provide excellent leadership.')
    elif ptype == "ISFP":
        str_list.append('This personality is creative, calm, and observant.')
        str_list.append('They often prefer meaningful work with room for personal expression.')
        str_list.append('They tend to do well in the arts, as well as helping others and working with people.')
    elif ptype == "ESFP":
        str_list.append('This personality is outgoing, spontaneous, and energetic.')
        str_list.append('They often thrive in lively settings with people and creativity.')
        str_list.append('Optimistic and fun-loving, their enthusiasm is great for motivating others.')
    elif ptype == "ISTP":
        str_list.append('This personality is hands-on, logical, and adaptable.')
        str_list.append('They often like practical challenges and figuring things out in real time.')
        str_list.append('With the ability to stay calm under pressure, ')
        str_list.append('they excel in any job which requires immediate action.')
    elif ptype == "ESTP":
        str_list.append('This personality is action-oriented, bold, and practical.')
        str_list.append('They often enjoy fast feedback, variety, and real-world decisions.')
        str_list.append('They have a gift for reacting to and solving immediate problems, and persuading other people.')
    elif ptype == "ISFJ":
        str_list.append('This personality is steady, caring, and dependable.')
        str_list.append('They often bring patience, structure, and strong support to others.')
        str_list.append('Tradition-oriented and down-to-earth')
        str_list.append('they do best in jobs where they can help people achieve their goals')
        str_list.append('or where structure is needed.')
    elif ptype == "ESFJ":
        str_list.append('This personality is Warm, organized, and community-minded.')
        str_list.append('They often prioritize teamwork, harmony, and dependability.')
        str_list.append('They do best in jobs where they can apply their natural warmth at building relationships with other people.')
    elif ptype == "ISTJ":
        str_list.append('This personality is reliable, practical, and detail-aware.')
        str_list.append('They often prefer clarity, consistency, and follow-through.')
        str_list.append('They have a knack for detail and memorization')
        str_list.append('but work more behind the scenes instead of up front as a leader.')
    elif ptype == "ESTJ":
        str_list.append('This personality is direct, structured, and results-focused.')
        str_list.append('They often enjoy responsibility, planning, and execution.')
        str_list.append('Natural leaders, they work best when they are in charge and enforcing the rules.')
    else:
        str_list.append('Not enough data to determine personality')

    return ' '.join(str_list)


def get_careers(ptype):
    careers = []
    if ptype == "INTP":
        careers.append('physicist')
        careers.append('chemists')
        careers.append('biologist')
        careers.append('photographer')
        careers.append('strategic planner')
        careers.append('mathematician')
        careers.append('university professor')
        careers.append('computer programmer')
        careers.append('writer')
        careers.append('engineer')
        careers.append('lawyer')
        careers.append('artist')
        careers.append('researcher')
        careers.append('psychologist')
        careers.append('scientist')
        careers.append('surveyor')
        careers.append('')
    elif ptype == "ENTP":
        careers.append('lawyer')
        careers.append('entrepreneur')
        careers.append('psychologist')
        careers.append('consultant')
        careers.append('sales representative')
        careers.append('actor')
        careers.append('engineer')
        careers.append('scientist')
        careers.append('marketer')
        careers.append('computer programmer')
        careers.append('comedian')
        careers.append('investigator')
        careers.append('journalist')
        careers.append('psychiatrist')
        careers.append('designer')
        careers.append('writer')
        careers.append('artist')
        careers.append('musician')
    elif ptype == "INTJ":
        careers.append('lawyer')
        careers.append('scientist')
        careers.append('engineer')
        careers.append('teacher')
        careers.append('doctor')
        careers.append('dentist')
        careers.append('administrator')
        careers.append('manager')
        careers.append('psychologist')
        careers.append('photographer')
    elif ptype == "ENTJ":
        careers.append('lawyer')
        careers.append('business leader')
        careers.append('entrepreneur')
        careers.append('judge')
        careers.append('professor')
        careers.append('politician')
        careers.append('investigator')
        careers.append('manager')
        careers.append('banker')
    elif ptype == "INFP":
        careers.append('writer')
        careers.append('artist')
        careers.append('counselor')
        careers.append('teacher')
        careers.append('clergy')
        careers.append('psychologist')
        careers.append('scientist')
        careers.append('editor')
        careers.append('journalist')
    elif ptype == "ENFP":
        careers.append('actor')
        careers.append('journalist')
        careers.append('writer')
        careers.append('musician')
        careers.append('consultant')
        careers.append('entrepreneur')
        careers.append('teacher')
        careers.append('counselor')
        careers.append('reporter')
        careers.append('marketer')
        careers.append('scientist')
        careers.append('sales representative')
    elif ptype == "INFJ":
        careers.append('counselor')
        careers.append('teacher')
        careers.append('medical')
        careers.append('librarian')
        careers.append('clergy')
    elif ptype == "ENFJ":
        careers.append('teacher')
        careers.append('medical')
        careers.append('counselor')
        careers.append('manager')
        careers.append('politician')
        careers.append('designer')
        careers.append('writer')
        careers.append('musician')
    elif ptype == "ISFP":
        careers.append('artist')
        careers.append('musician')
        careers.append('designer')
        careers.append('counselor')
        careers.append('builder')
        careers.append('medical')
        careers.append('technician')
    elif ptype == "ESFP":
        careers.append('actor')
        careers.append('painter')
        careers.append('sales representative')
        careers.append('teacher')
        careers.append('counselor')
        careers.append('human resources managers')
        careers.append('coach')
        careers.append('therapist')
    elif ptype == "ISTP":
        careers.append('police')
        careers.append('computer programmer')
        careers.append('engineer')
        careers.append('pilot')
        careers.append('paramedic')
        careers.append('entrepreneur')
    elif ptype == "ESTP":
        careers.append('sales representative')
        careers.append('marketer')
        careers.append('police')
        careers.append('entrepreneur')
        careers.append('firefighter')
        careers.append('laborer')
        careers.append('comedian')
    elif ptype == "ISFJ":
        careers.append('designer')
        careers.append('administrator')
        careers.append('secretary')
        careers.append('social worker')
        careers.append('counselor')
        careers.append('shopkeeper')
        careers.append('health service worker')
    elif ptype == "ESFJ":
        careers.append('nurse')
        careers.append('teacher')
        careers.append('office manager')
        careers.append('administrator')
        careers.append('counselor')
        careers.append('speech pathologist')
    elif ptype == "ISTJ":
        careers.append('business executive')
        careers.append('administrator')
        careers.append('police')
        careers.append('lawyer')
        careers.append('medical')
        careers.append('engineer')
        careers.append('math teacher')
    elif ptype == "ESTJ":
        careers.append('teacher')
        careers.append('business administrator')
        careers.append('police/detective work')
        careers.append('manager')
        careers.append('financial officer')
        careers.append('government worker')
        careers.append('sales representative')

    return careers
