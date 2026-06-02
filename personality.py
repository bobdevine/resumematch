import math
import random
#import pprint

import mbti

"""
help to select the right candidate for a job opening.
shortlist a candidate based on their personality scores.

Slecting the right candidate for the recruitment process from a pool of
candidates has been a fundamental issue.

Is there a way to screen candidates based on predicted traits?
Conducting personality and various technical eligibility evaluation tests,
interviews, and group discussions have been traditional techniques.
Personality detection is an old topic in psychology.

Personality tests are often used to inform hiring decisions.
The scores you get on personality tests can’t predict specific things you’ll do.
Personality tests can predict general behaviors of large groups of people.

One of the most important things to evaluate in a new hire is their
personality fit both with the team and with the role for which they
are interviewing.
The hiring manager can use these to understand how extroverted or
introverted a candidate is, how they communicate, what motivates them,
or even how resilient they are in the face of challenges – all key aspects
of a particular role e.g. sales

In roles such as these that have a high degree of human interaction, it can be beneficial to understand how the candidate communicates, how they interact with others, or whether they focus on details or see the big picture.

In psychology, "personality" refers to the unique pattern of thoughts,
feelings, and behaviors that characterize an individual and distinguish
them from others. It encompasses various dimensions such as traits,
motivations, beliefs, and values, which collectively shape how individuals
perceive themselves and interact with the world.

Personality is a unique trait that allows discriminating between individuals.
It can be defined by a set of stable characteristics of an individual that
may affect their interactions, relationships, attitudes, and behavior.

Personality measuring is often based on self-reports from job candidates,
which can be lengthy and susceptible to faking.
Personality traits are among the strongest non-cognitive predictors of job performance,

Natural language processing (NLP) is a possibility for automated personality assessment.
The relationship between linguistic patterns and personality traits is rough. 

Language analysis is a first-principles approach to understanding psychological constructs

Personality trait prediction has attracted substantial academic interest
in recent years as a consequence of its ability to characterize people’s
distinctive personality features that distinguish them from others.

Numerous studies have investigated the diverse aspects of human personality.
Among the widely used frameworks for psychological assessment are Enneagrams,
Myers Briggs Type Indicator (MBTI), HEXACO, and the Big Five model.

Personality models such as HEXACO and Big Five are grounded on the lexical
hypothesis, which states that personality characteristics that are salient
in people's daily transactions and relates to important social outcomes are
encoded in language

When exploring personality psychology, two models stand out as the most
scientifically rigorous and widely researched: the HEXACO model and the
Big Five model

The Big-Five predicts personality of people based on OCEAN (openness,
conscientiousness, extraversion, agreeableness, neuroticism) and experience.
Most career-related research uses Big Five dimensions

An alternative personality framework is the six-factor HEXACO model.
The HEXACO model adds a key differentiator — Honesty-Humility — to the Big Five,
The HEXACO model is good at explaining variance across performance outcomes.
The HEXACO model can be used to predict job performance and career success.
Research has shown that certain personality traits, such as Conscientiousness
and Honesty-Humility, are associated with job performance and career success
It also predicts counterproductive work behavior
and is better for analyzing hiring for positions requiring high integrity.

HEXACO and Big Five can be complementary approaches to personality psychology.
The Big Five provides the foundational framework that decades of research
have built upon, while HEXACO extends and refines this foundation with
important additions.

Traditional context-free representation methods include Bag of Words (BoW)
and term frequency-inverse document frequency (TF-IDF).

Personality assessment has been traditionally carried out following classic
approaches such as questionnaires or interviews, which are time-consuming,
costly, and imprecise.

Algorithms to estimate personality:
https://pmc.ncbi.nlm.nih.gov/articles/PMC11427259/

People find their work fulfilling when the important features of a their job
or profession meet and complement their personality.

It parses all the data from CV/resume.
"""

import re

import stemming


MYERS_BRIGGS_DIMENSIONS = ["IE", "NS", "FT", "JP"]
# MBTI has four dimensions: I/E, N/S, F/T, and J/P. 
MYERS_BRIGGS_TYPES = [
    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ', 'ESTP', 'ESFP', 'ENFP', 'ENTP',
    'ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
]


MBTI_CONVERT_BIG5 = {
    # MBTI -> Big Five
    # statistical estimation based on research (McCrae & Costa, 1989)
    # Type : O, C, E, A, N
    "INTJ": [78, 72, 28, 42, 45],
    "INTP": [82, 38, 25, 35, 48],
    "INFJ": [78, 62, 32, 72, 55],
    "INFP": [82, 45, 28, 75, 58],
    "ISTJ": [35, 78, 28, 48, 35],
    "ISTP": [52, 42, 32, 35, 32],
    "ISFJ": [38, 75, 32, 75, 48],
    "ISFP": [58, 45, 35, 72, 45],
    "ENTJ": [75, 75, 72, 38, 35],
    "ENTP": [85, 35, 75, 45, 42],
    "ENFJ": [75, 68, 75, 78, 45],
    "ENFP": [88, 38, 78, 72, 48],
    "ESTJ": [38, 82, 72, 42, 32],
    "ESTP": [55, 35, 78, 48, 28],
    "ESFJ": [42, 72, 75, 78, 45],
    "ESFP": [55, 38, 82, 72, 38],
}


MBTI_KEYWORDS = {
    'ENTJ': [
        'tenacious', 'assertive', 'strategic', 'innovative', 'proactive',
        'high-energy', 'bold', 'confident', 'decisive',
    ],
    'INTJ': [
        'independent', 'reserved', 'intellectual', 'intense',
        'driven', 'tenacious', 'direct', 'private',
    ],
    'ENTP': [
        'creative', 'tenacious', 'funny', 'clever', 'futuristic', 'skeptical',
        'independent', 'strategic', 'unconventional', 'adaptable',
    ],
    'INTP': [
        'independent', 'analytical', 'private', 'unconventional', 'skeptical',
        'witty', 'original', 'motivated', 'disorganised',
    ],
    'ENFJ': [
        'affectionate', 'creative', 'visionary', 'charismatic', 'playful',
        'talkative', 'idealistic', 'empathetic', 'sensitive',
    ],
    'INFJ': [
        'visionary', 'sensitive', 'reserved', 'private', 'idealistic',
        'planful', 'conscientious', 'empathetic', 'perfectionistic',
    ],
    'ENFP': [
        'collaborative', 'visionary', 'insightful', 'spontaneous', 'casual',
        'imaginative', 'sensitive', 'energetic', 'gregarious', 'idealistic',
    ],
    'INFP': [
        'sensitive', 'caring', 'spontaneous', 'calm', 'unique', 'reserved',
        'modest', 'casual', 'empathetic', 'flexible',
    ],
    'ESTJ': [
        'take charge', 'decisive', 'tenacious', 'fast', 'dependable',
        'proactive', 'outspoken', 'straightforward',
    ],
    'ISTJ': [
        'clear', 'methodical', 'loyal', 'precise', 'realistic', 'reserved',
        'meticulous', 'responsible', 'accurate', 'literal',
    ],
    'ESFJ': [
        'sensitive', 'talkative', 'responsible', 'generous', 'attentive',
        'enthusiastic', 'affectionate', 'sympathetic', 'warm', 'outgoing',
    ],
    'ISFJ': [
        'playful', 'decisive', 'reserved', 'precise', 'sensitive', 'private',
        'literal', 'sympathetic', 'efficient', 'accommodating',
    ],
    'ESTP': [
        'fun', 'active', 'hands-on', 'practical', 'observant', 'talkative',
        'take-charge', 'inventive', 'charming',
    ],
    'ISTP': [
        'quiet', 'unflappable', 'down-to-earth', 'concise', 'realistic',
        'logic', 'spontaneous', 'private',
    ],
    'ESFP': [
        'fun', 'casual', 'entertaining', 'sympathetic', 'sensitive',
        'talkative',
    ],
    'ISFP': [
        'unassuming', 'observant', 'reserved', 'private', 'spontaneous',
        'kind', 'sensitive', 'quiet',
    ],
}



BIG5_TERMS_MEANINGS = {
    "openness" : """"
    The tendency to be curious, imaginative, open-minded, and receptive to new ideas, experiences, and unconventional values.
    Refers to as being emotional, curious, imaginative, and creative
Fantasy, aesthetics, feelings, actions, ideas, values
    People who like to learn new things and enjoy new experiences usually score high in openness. Openness includes traits like being insightful and imaginative and having a wide variety of interests.
    Openness describes a person's tendency to think abstractly.
    Those who are high in Openness tend to be creative, adventurous, and intellectual. They enjoy playing with ideas and discovering novel experiences.
    Those who are low in Openness tend to be practical, traditional, and focused on the concrete. They tend to avoid the unknown and follow traditional ways.
    """,

    "conscientiousness" : """
    The tendency to be organized, responsible, dependable, goal-directed, and self-disciplined.
    Describes as being organized, dependable and motivated.
    Competence, order, dutifulness, achievement striving, self-discipline,
deliberation
    People that have a high degree of conscientiousness are reliable and prompt. Traits include being organised, methodic, and thorough.
    Conscientiousness describes a person's level of goal orientation and persistence.
    Those who are high in Conscientiousness are organized and determined, and are able to forego immediate gratification for the sake of long-term achievement.
    Those who are low in this trait are impulsive and easily sidetracked.
    """,
    
    "extraversion" : """
    The tendency to be outgoing, energetic, sociable, assertive, and experience positive emotions.
    A person with the trait tends to be sociable, active, and willing to take risks.
    Warmth, gregariousness, assertiveness, activity, excitement seeking, positive
    emotion
    Extraversion traits include being; energetic, talkative, and assertive (sometime seen as outspoken by Introverts). Extraverts get their energy and drive from others, while introverts are self-driven get their drive from within themselves.
    Extraversion describes a person’s inclination to seek stimulation from the outside world, especially in the form of attention from other people.
    Extraverts engage actively with others to earn friendship, admiration, power, status, excitement, and romance.
    Introverts, on the other hand, conserve their energy, and do not work as hard to earn these social rewards.
    """,
    
    "agreeableness" : """
    The tendency to be compassionate, cooperative, trusting, and forgiving in interpersonal interactions.
    Indicates individuals who are cooperative, helpful, and trusting.
    Trust, straightforwardness, altruism, compliance, modesty, tenderness
    As it perhaps sounds, these individuals are warm, friendly, compassionate and cooperative and traits include being kind, affectionate, and sympathetic. In contrast, people with lower levels of agreeableness may be more distant.
    Agreeableness describes the extent to which a person prioritizes the needs of others over their own needs.
    People who are high in Agreeableness experience a great deal of empathy and tend to get pleasure out of serving and taking care of others.
    People who are low in Agreeableness tend to experience less empathy and put their own concerns ahead of others
    """,
    
    "neuroticism" : """
    The tendency to experience negative emotions such as anxiety, anger, or depression; low emotional stability.
    Deﬁnes a continuum from emotional stability to instability.
    Anxiety, angry hostility, depression, self-consciousness,
    impulsivity, vulnerabilties
    Neuroticism or Emotional Stability relates to degree of negative emotions. People that score high on neuroticism often experience emotional instability and negative emotions. Characteristics typically include being moody and tense.
    Neuroticism describes a person's tendency to respond to stressors with negative emotions, including fear, sadness, anxiety, guilt, and shame.
    High Neuroticism scorers are more likely to react to a situation with strong negative emotions.
    Low Neuroticism scorers are more likely to brush off their misfortune and move on.
    """
}


"""
Openness to Experience
    High: Imaginative, curious, creative, open to new ideas
    Low: Practical, traditional, conservative, prefer routine
O_Int - Intellectual Curiosity
O_Eas - Aesthetic Sensitivity
O_Cre - Creative Imagination

Conscientiousness
    High: Organized, reliable, disciplined, goal-oriented
    Low: Spontaneous, flexible, casual, prefer flexibility
C Conscientiousness
C_Org - Organization
C_Pro - Productiveness
C_Res - Responsibility

Extraversion
    High: Sociable, talkative, energetic, outgoing
    Low: Quiet, reserved, independent, prefer solitude
E_Soc - Sociability
E_Ass - Assertiveness
E_Ene - Energy Level

Agreeableness
    High: Friendly, compassionate, helpful, cooperative
    Low: Critical, competitive, skeptical, assertive
A_Com - Compassion
A_Res - Respectfulness
A_Tru - Trust

Neuroticism / Negative Emotionality
    High: Emotional, anxious, sensitive, prone to stress
    Low: Emotionally stable, calm, resilient, stress-resistant
N_Anx - Anxiety
N_Dep - Depression
N_Emo - Emotional Volatility
"""

ADJECTIVE_POSITIVE = [
    "adventurous", "agreeable", "ambitious", "amusing", "brave", "calm",
    "careful", "creative", "decisive", "determined", "easygoing", "emotional",
    "energetic", "faithful", "fearless", "frank", "friendly", "funny",
    "generous", "gentle", "good", "hard-working", "helpful", "honest",
    "humorous", "imaginative", "intelligent", "kind", "loving", "loyal",
    "modest", "neat", "nice", "optimistic", "patient", "polite", "powerful",
    "practical", "quiet", "rational", "reliable", "reserved", "romantic",
    "self-confident", "sensible", "sensitive", "shy", "sincere", "sociable",
    "straightforward", "sympathetic", "thoughtful", "tidy", "understanding",
    "willing", "witty", "passionate", "adaptable", "affectionate", "bright",
    "broad-minded", "charming", "communicative", "compassionate ",
    "conscientious", "considerate", "courageous", "courteous", "diligent",
    "diplomatic", "discreet", "dynamic", "enthusiastic", "forceful",
    "independent", "intellectual", "intuitive", "inventive", "persistent ",
    "philosophical", "self-disciplined", "tough",
    "active", "adaptable", "affable", "amiable", "amicable",
    "bright", "charming", "circumspect", "communicative", "compassionate",
    "empathetic", "energetic", "faithful", "gregarious", "hopeful",
    "humorous", "intuitive", "inventive","joyful", "lucky", "mature",
    "motivated", "passionate", "plucky", "popular", "realistic",
    "resourceful", "romantic", "sensible", "sincere", "smart",
    "sociable", "sympathetic", "tidy", "understanding", "willing", "wise",
    "witty", 'great', 'excellent', 'happy', 'love', 'wonderful', 'amazing',
    'best', 'fantastic', 'joy'
]

ADJECTIVE_NEGATIVE = [
    "aggressive", "arrogant", "boastful", "boring", "bossy", "careless",
    "changeable", "cowardly", "intolerant", "irresponsible", "cruel",
    "dishonest", "foolish", "fussy", "greedy", "impatient", "impolite",
    "jealous", "lazy", "moody", "silly", "stingy", "stubborn", "stupid",
    "unkind", "unreliable", "untidy", "clinging", "compulsive", "conservative",
    "cunning", "cynical", "deceitful", "detached", "domineering", "grumpy",
    "harsh ", "impulsive", "inconsiderate", "inconsistent", "indecisive",
    "indiscreet", "inflexible", "interfering", "materialistic", "miserly",
    "narrow-minded", "obsessive", "obstinate", "possessive", "quarrelsome",
    "quick-tempered", "resentful", "ruthless", "sarcastic", "secretive",
    "sneaky", "superficial", "tactless", "timid", "touchy", "thoughtless",
    "unpredictable", "untrustworthy", "vague", "vengeful", "vulgar",
    "abrasive", "apathetic", "argumentative", "callous", "catty", "childish",
    "cocky", "confrontational", "controlling", "cowardly", "cynical",
    "defensive", "deceitful", "dense", "devious", "dim", "dishonest",
    "disloyal", "disorganized", "disrespectful", "disruptive", "egotistical",
    "evasive", "evil", "fanatical", "flaky", "foolish", "forgetful",
    "frivolous", "gossipy", "greedy", "grumpy", "gullible", "hostile",
    "humorless", "hypocritical", "ignorant", "impatient", "impractical",
    "irrational", "jealous", "judgemental", "lazy", "manipulative", "mean",
    "moody", "morbid", "nasty", "nosy", "obsessive", "paranoid", "pessimistic",
    "petty", "possessive", "prejudiced", "pretentious", "reckless",
    "rotten", "rude", "selfish", "sleazy", "spoiled", "stingy", "stupid",
    "unlucky", "unmotivated", "unreliable", "untidy", "vain",
    'bad', 'terrible', 'hate', 'awful', 'worst', 'sad', 'angry', 'horrible',
    'pain', 'difficult'
]


# ----- Big Five (OCEAN) Trait Keywords
BIG5_KEYWORDS = {
    'openness': [
        'creative', 'innovative', 'imaginative', 'curious', 'artistic',
        'research', 'design', 'invent', 'develop', 'explore',
        'learning', 'experimental', 'novel',
        'brainstorm', 'vision', 'ideas', 'discovery', 'art',
        'poetry', 'literature', 'philosophy', 'diverse', 'unique',
        'open-mind', 'flexible', 'conceptual', 'abstract',
        'intellectual', 'philosophical', 'adventurous', 'experimental',
        'explorative', 'visionary', 'inventive', 'original',
    ],

    'conscientiousness': [
        'organize', 'responsible', 'punctual', 'detail-oriented',
        'systematic', 'thorough', 'discipline', 'reliable', 'diligent',
        'plan', 'structure', 'manage', 'led', 'deliver', 'lead',
        'deadline', 'goal', 'target', 'achieve', 'complete',
        'certify', 'award', 'excellence', 'quality', 'accuracy',
        'professional', 'dedicate', 'commit', 'process',
        'methodical', 'precise', 'careful', 'consistent', 'efficient',
        'responsible', 'systematic', 'methodical', 'plan',
        'precise', 'detail', 'focus', 'punctual',
    ],

    'extraversion': [
        'leadership', 'lead', 'speak', 'presentation', 'active',
        'networking', 'collaborate', 'social', 'outgoing', 'motivate',
        'energetic', 'enthusiastic', 'confident', 'assertive',
        'sale', 'marketing', 'client', 'customer', 'communication',
        'event', 'workshop', 'conference', 'train', 'cooperate',
        'mentor', 'coach', 'coordinate', 'engage',
        'community', 'volunteered', 'ambassador', 'spokesperson',
        'dynamic', 'vibrant', 'sociable', 'friendly', 'expressive',
        'confident', 'assertive', 'collaborate', 'communicate',
    ],

    'agreeableness': [
        'teamwork', 'cooperative', 'help', 'supportive', 'empathetic',
        'compassionate', 'caring', 'patient', 'understanding', 'kind',
        'collaborative', 'friendly', 'warm', 'trust', 'honest',
        'volunteer', 'charity', 'community', 'helping',
        'mentor', 'counseled', 'assisted', 'resolved',
        'mediate', 'facilitate', 'accommodate', 'flexible',
        'harmonious', 'diplomatic', 'considerate', 'generous',
        'cooperative', 'supportive', 'considerate',
        'tolerant', 'generous', 'altruistic', 'nurture', 'harmonious',
    ],

    'neuroticism': [
        # High = more stress/negative traits
        'stress', 'anxiety', 'overwhelmed', 'pressure', 'challenge',
        'struggle', 'difficult', 'conflict', 'issue', 'problem',
        'failed', 'mistake', 'concern', 'worry', 'frustrate',
        'uncertain', 'unstable', 'sensitive', 'emotional', 'anxious',
        'worry', 'nervous', 'tense', 'stress', 'sensitive', 'moody',
        'irritable', 'impulsive', 'vulnerable', 'insecure', 'volatile',

        # Positive keywords → reduce neuroticism
        # 'calm', 'composed', 'resilient', 'stable', 'balanced',
        # 'stress management', 'adaptable', 'consistent performance',
        # 'under pressure', 'crisis management', 'cool-headed'
    ]
}

BIG5_INTERPRETATIONS = {
    'openness': {
        'High': 'Highly creative, curious, and open to new experiences. Enjoys intellectual pursuits and abstract thinking.',
        'Medium': 'Moderately open to new experiences. Balances curiosity with practicality.',
        'Low': 'Prefers routine and familiarity. More practical and conventional in thinking.'
    },
    'conscientiousness': {
        'High': 'Very organized, disciplined, and goal-oriented. Strong sense of duty and reliability.',
        'Medium': 'Reasonably organized and dependable. Balances structure with flexibility.',
        'Low': 'More spontaneous and flexible. May prefer adaptability over rigid planning.'
    },
    'extraversion': {
        'High': 'Highly sociable, energetic, and outgoing. Draws energy from social interactions.',
        'Medium': 'Comfortable in social situations but also values alone time.',
        'Low': 'More introverted and reserved. Prefers smaller groups or solitary activities.'
    },
    'agreeableness': {
        'High': 'Very cooperative, trusting, and empathetic. Prioritizes harmony and helping others.',
        'Medium': 'Generally cooperative but can be assertive when needed.',
        'Low': 'More competitive and skeptical. Values independence over conformity.'
    },
    'neuroticism': {
        'High': 'More prone to stress, anxiety, and emotional fluctuations.',
        'Medium': 'Average emotional stability. Handles stress reasonably well.',
        'Low': 'Emotionally stable and resilient. Calm under pressure.'
    }
}

#'neurotic' : 'worry', 'stress', 'anxious', 'nervous', 'fear', 'concern', 'upset', 'difficult', 'problem', 'struggle'

HEXACO_KEYWORDS = {
    "honesty" : [
        "cooperation",
        'Sincere', 'honest', 'faithful', 'loyal', 'modest', 'genuine'
        ],
    "emotionality" : [
        'anxious', 'fear', 'sensitive'
        ],
    "extraversion" : [
        "active", "talk",
        'social', 'party', 'people', 'friends', 'energy',
        'outgoing', 'excited', 'group'
        ],
    "agreeableness" : [
        'kind', 'help', 'care', 'trust', 'support', 'compassion',
        'friend', 'warm', 'gentle', 'cooperative'
        ],
    "conscientiousness" : [
        "diligent", "discipline", "organize", "precise",
        'plan', 'careful', 'detail', 'responsible', 'complete',
        'thorough', 'systematic', 'discipline', 'structured'
        ],
    "openness" : [
        "creative", "innovate",
        'imagine', 'art', 'curious', 'innovative', 'new', 'idea', 'wonder',
        'explore', 'different'
        ],
    }


def cosine_similarity(v1, v2):
    #compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    if sumxx == 0:
        return 0.0
    if sumyy == 0:
        return 0.0
    return sumxy/math.sqrt(sumxx*sumyy)


class Predictor():
    """Predict Personality"""
    def __init__(self):
        #print("Personality Predictor")
        self.MBTI_type = None
        self.enneatype_type = None
        self.big5_scores = {
            'openness' : 0,
            'conscientiousness' : 0,
            'extraversion' : 0,
            'agreeableness' : 0,
            'neuroticism' : 0,
            }
        self.hexaco_scores = {
            "honesty" : 0,
            "emotionality" : 0,
            "extraversion" : 0,
            "agreeableness" : 0,
            "conscientiousness" : 0,
            "openness" : 0,
            }
        self.mbti_scores = {
            'ENTJ': 0, 'INTJ': 0, 'ENTP': 0, 'INTP': 0,
            'ENFJ': 0, 'INFJ': 0, 'ENFP': 0, 'INFP': 0,
            'ESTJ': 0, 'ISTJ': 0, 'ESFJ': 0, 'ISFJ': 0,
            'ESTP': 0, 'ISTP': 0, 'ESFP': 0, 'ISFP': 0,
            }

    def process(self, txt):
        if not txt:
            return
        words = re.split(r'[ ,\.!]+', txt)
        #words = txt.split()
        #print(words)
        for word in words:
            stemmed_word = stemming.stem(word.lower())
            #print(" WORD>", word, "-->", stemmed_word)
            if not stemmed_word:
                continue
            for trait in BIG5_KEYWORDS:
                if stemmed_word in BIG5_KEYWORDS[trait]:
                    #print(word, "found in BIG-5", trait)
                    self.big5_scores[trait] += 1

            """
            if self.big5_scores['openness'] > 50:
                strengths.append("Creative and Open-minded")
            else:
                weaknesses.append("Resistant to change")

            if self.big5_scores['conscientiousness'] > 50:
                strengths.append("Organized and Reliable")
                weaknesses.append("Prone to disorganization")

            if self.big5_scores['extraversion'] > 50:
                strengths.append("Sociable and Energetic")
            else:
                weaknesses.append("May struggle in highly social environments")

            if self.big5_scores['agreeableness'] > 50:
                strengths.append("Empathetic and Cooperative")
            else:
                weaknesses.append("Can be overly critical or competitive")

            if self.big5_scores['neuroticism'] < 50:
                strengths.append("Emotionally Stable")
            else:
                weaknesses.append("Prone to stress and anxiety")
            """
            for trait in HEXACO_KEYWORDS:
                if stemmed_word in HEXACO_KEYWORDS[trait]:
                    #print(word, "found in HEXACO", trait)
                    self.hexaco_scores[trait] += 1

            for trait in MBTI_KEYWORDS:
                if stemmed_word in MBTI_KEYWORDS[trait]:
                    #print(word, "found in MBTI", trait)
                    self.mbti_scores[trait] += 1
        return


    def calculate_personality(self):
        #print(f"\n📊 OCEAN/Big5 Scores:")
        results = {}
        total_score = 0.0
        for trait, score in self.big5_scores.items():
            #print("  ", trait, ":", score)
            total_score += score
        adjusted_scores = []
        for trait, score in self.big5_scores.items():
            val = 0.0
            if total_score > 0:
                val = 100.0 * score / total_score
            adjusted_scores.append(val)
        #print("adjusted_scores =", adjusted_scores)
        for mbti,big5 in MBTI_CONVERT_BIG5.items():
            sim = cosine_similarity(adjusted_scores, big5)
            #print(" --", mbti, big5, sim)
            results[mbti] = []
            results[mbti].append(sim)

        #print("best MBTI match", match_type)
        #print("RESULTS", results)

        #print(f"\n📊 HEXACO Scores:")
        total_score = 0.0
        for trait, score in self.hexaco_scores.items():
            #print("  ", trait, ":", score)
            total_score += score
        # convert to Big Five scores
        converted_scores = [0, 0, 0, 0, 0]
        for trait, score in self.hexaco_scores.items():
            val = 0.0
            if total_score > 0:
                val = 100.0 * score / total_score
            if trait == 'honesty':
                # split value over OCEAN
                converted_scores[0] += val * .33
                converted_scores[1] += val * .08
                converted_scores[2] += val * -.07
                converted_scores[3] += val * .47
                converted_scores[4] += val * -.14
            elif trait == 'emotionality':
                converted_scores[0] += val * .07
                converted_scores[1] += val * .02
                converted_scores[2] += val * -.02
                converted_scores[3] += val * .38
                converted_scores[4] += val * .52
            elif trait == 'extraversion':
                converted_scores[0] += val * .24
                converted_scores[1] += val * .02
                converted_scores[2] += val * .53
                converted_scores[3] += val * .14
                converted_scores[4] += val * -.50
            elif trait == 'agreeableness':
                converted_scores[0] += val * .08
                converted_scores[1] += val * -.08
                converted_scores[2] += val * .02
                converted_scores[3] += val * .33
                converted_scores[4] += val * -.50
            elif trait == 'conscientiousness':
                converted_scores[0] += val * .26
                converted_scores[1] += val * .76
                converted_scores[2] += val * .26
                converted_scores[3] += val * .20
                converted_scores[4] += val * -.25
            elif trait == 'openness':
                converted_scores[0] += val * .74
                converted_scores[1] += val * -.09
                converted_scores[2] += val * .18
                converted_scores[3] += val * .10
                converted_scores[4] += val * -.08
            else:
                print("bad convert")

        """
        # Clamp scores between 0 and 100 and round
        for trait in results:
            results[trait] = max(0.0, min(100.0, results[trait]))
            results[trait] = round(results[trait], 2)
        """
        #print("converted_scores", converted_scores)
           
        for mbti,big5 in MBTI_CONVERT_BIG5.items():
            sim = cosine_similarity(converted_scores, big5)
            #print(" --", mbti, big5, sim)
            results[mbti].append(sim)

        # normalize MBTI scores
        total_score = 0.0
        #print(f"\n📊 MBTI Scores:")
        for mbti,score in self.mbti_scores.items():
            #print("  ", mbti, ":", score)
            total_score += score
        
        normalized_scores = {}
        for mbti,score in self.mbti_scores.items():
            val = 0.0
            if total_score > 0:
                val = 2.0 * score / total_score
            normalized_scores[mbti] = val
        #print("normalized_scores", normalized_scores)

        for trait in MBTI_KEYWORDS:
            val = normalized_scores[trait]
            results[trait].append(val)

        #print("RESULTS", results)
        results_sorted = sorted(results.items(),
                                key=lambda x:(x[1][0] + x[1][1] + x[1][2]),
                                reverse=True)
        #print("Sorted RESULTS", results_sorted)

        #print("[0][1]", results_sorted[0][1])
        val = results_sorted[0][1][0] + results_sorted[0][1][1] + results_sorted[0][1][2]
        #print("val", val)
        if val == 0:
            #print("UNKNOWN MBTI")
            self.MBTI_type = None
            return None
        best_type = results_sorted[0][0]
        #print("best MBTI match", best_type)
        self.MBTI_type = best_type


    def print_personality_type_description(self):
        ptype = self.MBTI_type
        print(mbti.get_description(ptype))

    def print_personality_type_jobs(self):
        ptype = self.MBTI_type
        careers = mbti.get_careers(ptype)
        #print(*careers, sep=", ")
        print('Good career matches are:')
        line_limit = 55
        indent_size = 4
        print("", end=(indent_size*" "))
        item_num = 1
        line_size = indent_size
        for career in careers:
            line_size += len(career)
            if item_num == len(careers):
                print(career)
            elif line_size >= line_limit:
                line_size = 4
                print(career + ",")
                print("", end=(indent_size*" "))
            else:
                print(career, end=", ")
            item_num += 1
            
    def suggest_careers(self):
        big5_careers = {
            'O': ["Designer", "Writer", "Artist", "Entrepreneur"],
            'C': ["Accountant", "Project Manager", "Engineer", "Scientist"],
            'E': ["Salesperson", "PR Manager", "Event Planner", "Teacher"],
            'A': ["Counselor", "Nurse", "HR Manager", "Social Worker"],
            'N': ["Data Analyst", "Freelancer", "Researcher", "Archivist"]
            }
        ptype = self.MBTI_type
        careers = mbti.get_careers(ptype)
        return careers

#-----------------------------
if __name__ == '__main__':
    predictor = Predictor()
    #predictor.process("I love meeting new people but I get anxious sometimes.")
    ptype = random.choice(MYERS_BRIGGS_TYPES)
    print("temp type =", ptype)
    for sample in mbti.MBTI_TEXT_SAMPLES[ptype]:
        predictor.process(sample)
    predictor.calculate_personality()
    predictor.print_personality_type_description()
    predictor.print_personality_type_jobs()
