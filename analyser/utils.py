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

