from transformers import pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from random import random 
from random import randint

class MailAnalyserDummy():
    def __init__(self):
        self.topics = [ "Automation", "Algorithms", "Personaliz", "Analytics", "Recruitmen", "Copywritin",
                      "Intelligence","Management","Freelance","Integration","E-commerce","Assistants","Engineering",
                      "Pricing","Grammar","Data-Science","Logistics","Optimizatiion", "Leadership","Scalability",
                      "Collaborat","Performanc","Cybersecurty","Ethics","Reskilling","Workflow","Outreach",
                      "Strategy","Innovation",
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

    def getEmotions(self, mail):
        for key in self.emotions.keys():
            self.emotions[key] = random()
        return self.emotions

    def getTopics(self, mail, topics=5):
        top = []
        for t in range(topics):
            top.append(self.topics[randint(0, len(self.topics)-1)])
        return top


class MailAnalyser:
    def __init__(self):
        self.classifier = pipeline("text-classification",
                      model="j-hartmann/emotion-english-distilroberta-base",
                      return_all_scores=True)
        self.vectorizer = CountVectorizer(stop_words='english')
    
    def getEmotions(self, mail):
        """
        mail -> String: Content of the mail to get emotions
        Return:
        dict with emotions sorted from stronger emotion normalized
        """
        # Clasificación 
        results = self.classifier(mail)
        res = {}
        for i in results[0]:
            res[i['label']] = i['score'] 

        res_sorted = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        
        return res_sorted
    
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
       