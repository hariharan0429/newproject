import json

class RAG:
    def __init__(self):
        with open("data/diseases.json") as f:
            self.data = json.load(f)

    def retrieve(self, symptoms):
        results = []
        for d in self.data:
            score = len(set(symptoms) & set(d["symptoms"]))
            if score > 0:
                results.append((d, score))

        results.sort(key=lambda x: x[1], reverse=True)
        return [r[0] for r in results[:3]]
