from random import random 
from random import randint
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class MailAnalyserDummy():
    def __init__(self):
        self.vectorizer = CountVectorizer(stop_words='english')
        self.joy = [
            "happiness", "happy", "pleasure", "excitement", "cheerfulness",
            "satisfaction", "bliss", "euphoria", "contentment", "gratitude",
            "jubilation", "triumph", "serenity", "optimism", "hopefulness",
            "pride", "thrill", "enchantment", "glee", "ecstasy",
            "elation", "wonder", "joy", "laughter", "radiance",
            "love", "compassion", "affection", "comfort", "playfulness",
            "freedom", "relief", "calm", "amusement", "friendship",
            "enthusiasm", "exhilaration", "rejoicing", "blessing", "luck",
            "paradise", "security", "cheer", "charm", "warmth",
            "kindness", "sympathy", "hope", "smile", "fun",
            "admiration", "generosity", "forgiveness", "fellowship", "trust",
            "ease", "healing", "joyfulness", "gladness", "sunshine",
            "holiday", "celebration", "victory", "cheers", "bravery",
            "accomplishment", "confidence", "sweetness", "reassurance", "radiant",
            "peace", "gratification", "appreciation", "luckiness", "fortune",
            "wellbeing", "play", "energy", "positivity", "harmony",
            "deliciousness", "softness", "success", "cherish", "serendipity",
            "dream", "sparkle", "amity", "passion", "vitality",
            "curiosity", "enjoyment", "motivation", "fulfillment", "zeal",
            "sunrise", "hopeful", "companion", "carefree", "vibrance",
            "delightful", "bright", "flourishing", "upbeat", "victorious"
        ]

        self.sadness = [
            "grief", "loneliness", "despair", "melancholy", "disappointment",
            "sorrow", "gloom", "regret", "hopelessness", "misery",
            "pain", "loss", "sad", "depression", "unhappiness",
            "isolation", "yearning", "emptiness", "downhearted", "heartache",
            "tears", "nostalgia", "remorse", "rejection", "hurt",
            "tragedy", "burden", "dullness", "heaviness", "discouragement",
            "pessimism", "misfortune", "desolation", "crying", "dreariness",
            "bleakness", "unloved", "hopeless", "fragile", "broken",
            "anguish", "stress", "weary", "blue", "bitter",
            "abandonment", "failure", "discouraged", "dismay", "injustice",
            "heartbroken", "collapse", "devastation", "hurtful", "worn",
            "miserable", "coldness", "repressed", "trouble", "losses",
            "suffering", "crushed", "cry", "damaged", "weak",
            "hurtful", "fatigue", "downcast", "guilt", "tired",
            "bleeding", "worthless", "melancholic", "hopelessly", "unwanted",
            "detached", "futile", "helpless", "anguished", "darkness",
            "tragic", "solitude", "worthlessness", "mournful", "brokenness",
            "lost", "pitiful", "dreary", "weakness", "hurt",
            "resentful", "cold", "drained", "dull", "hopelessness",
            "pale", "fragility", "crying", "aching", "fatigued"
        ]

        self.surprise = [
            "astonishment", "amazement", "shock", "wonder", "awe",
            "bewilderment", "disbelief", "startle", "curiosity", "confusion",
            "stunned", "astonished", "amazed", "surprise", "dazed",
            "flabbergasted", "shocked", "gobsmacked", "astounded", "speechless",
            "confounded", "marvel", "perplexed", "startled", "staggered",
            "unexpected", "flustered", "overwhelmed", "dumbfounded", "bewitched",
            "entranced", "unready", "unsure", "curious", "spellbound",
            "awed", "captivated", "sudden", "flipped", "dazzled",
            "overawed", "taken-aback", "confusing", "unexpectedness", "surprised",
            "delighted", "odd", "peculiar", "startling", "bewildered",
            "amusing", "spectacular", "random", "novelty", "exceptional",
            "peculiarity", "mystery", "abrupt", "miraculous", "curiousness",
            "remarkable", "extraordinary", "jarring", "unusual", "peculiarly",
            "uncanny", "unforeseen", "shocking", "oddity", "amusement",
            "stupefied", "unexpectedly", "strangeness", "rare", "suddenness",
            "amusingly", "curiously", "incredible", "mystified", "fluky",
            "chance", "quirky", "thrilling", "outlandish", "bewildering",
            "unknown", "serendipitous", "wild", "uncertain", "weird",
            "mind-blowing", "peculiarity", "astonishing", "wonderment", "mystical",
            "jaw-dropping", "peculiarly", "striking", "offbeat", "different"
        ]
        
        self.anger = [
            "rage", "resentment", "frustration", "hostility", "fury",
            "irritation", "agitation", "bitterness", "annoyance", "outrage",
            "wrath", "indignation", "disgust", "exasperation", "violence",
            "hate", "contempt", "envy", "revenge", "jealousy",
            "defiance", "rebellion", "grudge", "provocation", "insult",
            "abrasiveness", "stubbornness", "arrogance", "displeasure", "rebuke",
            "antagonism", "ferocity", "vexation", "disdain", "hatred",
            "severity", "grievance", "mistrust", "defensiveness", "temper",
            "tension", "belligerence", "spite", "sarcasm", "abrasion",
            "excitability", "grumpiness", "snappiness", "touchiness", "irascibility",
            "fierceness", "impatience", "moodiness", "retaliation", "punishment",
            "dominance", "assertion", "violence", "abrasive", "rageful",
            "vengefulness", "reproach", "disapproval", "abrasiveness", "boiling",
            "choler", "bother", "resentful", "snarling", "outraged",
            "gritting", "abrasion", "combative", "accusation", "hostile",
            "rebuking", "abrasive", "grumbling", "annoyed", "resent",
            "vindictiveness", "irate", "temperamental", "ferocious", "scorn",
            "abrasive", "sharpness", "abrasiveness", "wrathful", "provoked",
            "stressed", "abrasive", "abrasions", "abrasiveness", "fuming"
        ]
        
        self.fear = [
            "anxiety", "dread", "terror", "panic", "apprehension",
            "nervousness", "worry", "phobia", "insecurity", "alarm",
            "unease", "fright", "concern", "paranoia", "restlessness",
            "tension", "timidity", "shyness", "hesitation", "caution",
            "shock", "nightmare", "phobia", "horror", "cowardice",
            "foreboding", "suspicion", "doom", "trepidation", "trembling",
            "alertness", "numbness", "fear", "hesitancy", "intimidation",
            "startle", "weakness", "pressure", "tightness", "dismay",
            "doubt", "danger", "uneasiness", "uncertainty", "agitation",
            "vulnerability", "distress", "isolation", "overthinking", "fearfulness",
            "avoidance", "discomfort", "timorousness", "bewilderment", "risk",
            "shiver", "hesitant", "timid", "tension", "overwhelm",
            "insecurity", "hesitation", "nervous", "uncertainty", "helplessness",
            "dependency", "anxiousness", "startling", "ominous", "confusion",
            "fragility", "phobic", "weak", "unsure", "inadequacy",
            "instability", "vigilance", "alert", "scare", "ghastly",
            "darkness", "withdrawal", "stressed", "loneliness", "pressure",
            "unpredictability", "hesitancy", "suspense", "timidness", "doubtful",
            "chills", "apprehensive", "petrified", "intense", "afraid",
            "defensiveness", "frightened", "horrified", "haunted", "lost"
        ]
        
        self.nexus =[
            "and", "but", "or", "so", "because", ",", ".",
            "although", "though", "while", "if", "unless",
            "since", "before", "after", "until", "whereas",
            "yet", "however", "therefore", "moreover", "nevertheless","a", "an", "the", "there", "those","this", "these",
            "i", "you", "he", "she", "it", "we", "they", "am", "is", "was", "were", "are",
        ]
        
        self.emotions = {
                    'joy': 0 ,
                    'sadness': 0 ,
                    'anger': 0 ,
                    'fear': 0 ,
                    'surprise': 0 ,
                    'neutral': 0 
                }
        return

    def filterString(self, text):
        """
        Return a string of words from self.nexus that do NOT appear in the text (substring match),
        joined by spaces.
        """
        text = text.lower().split()
        filtered_words = []
        for word in text:
            if not word in self.nexus:
                filtered_words.append(word)
        return " ".join(filtered_words)

    def count_matches(self, word_list, sentence):
        count = 0
        for word in word_list:
            count += sentence.count(word)  # counts substrings
        return count

    def normalize_dict_sum(self, d):
        """
        Normalize dictionary values so that their sum equals 1.
        """
        if not d:
            return {}
        
        total = sum(d.values())
        if total == 0:
            # Avoid division by zero; return equal distribution
            n = len(d)
            return {k: 1/n for k in d}
        
        normalized = {k: v / total for k, v in d.items()}
        return normalized

    def getNeutral(self, sentence):
        vocab = self.joy + self.sadness + self.anger+ self.fear + self.surprise
        coutn = 0
        sentence = sentence.split()
        for word in sentence:
            if not word in vocab:
                coutn +=1
        return coutn



    def getEmotions(self, mail):
        sentence = self.filterString(mail)
        print(sentence)
        self.emotions['joy'] = self.count_matches(self.joy, sentence)
        self.emotions['anger'] = self.count_matches(self.anger, sentence)
        self.emotions['sadness'] = self.count_matches(self.sadness, sentence)
        self.emotions['fear'] = self.count_matches(self.fear, sentence)
        self.emotions['surprise'] = self.count_matches(self.surprise, sentence)
        self.emotions['neutral'] = self.getNeutral(sentence)
        newDict = self.normalize_dict_sum(self.emotions)
        return newDict

    def getTopics(self, mail, topics=5):
        """
        mail -> String : Content of the mail to get principal Topics
        topics -> Int : From 1 to 10 of principal topics 
        Return:
        List of topics
        """
        X = self.vectorizer.fit_transform([mail])

        lda = LatentDirichletAllocation(n_components=1, random_state=42)
        lda.fit(X)

        words = self.vectorizer.get_feature_names_out()
        return [words[i] for i in lda.components_[0].argsort()[-topics:]]

