import json
import os


class ScoreService:
    def __init__(self, name):
        self.name = name
        # None if record doesn't exists in scoreboard
        self.highest = self.__find_score__(name)
        self.last_score = None

        if self.highest is None:
            self.update_score(0)

    def update_score(self, score):
        self.last_score = score

        if self.highest is None or self.highest < self.last_score:
            scores = self.__upload_scoreboard__()
            scores[self.name] = self.last_score
            self.__update_scoreboard__(scores)

    def __upload_scoreboard__(self):
        if os.path.exists('src/utility/scores.json'):
            with open('src/utility/scores.json', 'r', encoding='UTF-8') as score_file:
                scores = json.load(score_file)

            return scores
        else:
            return {}

    def __update_scoreboard__(self, scores):
        updated = json.dumps(scores, indent=4)
        with open('src/utility/scores.json', 'w', encoding='UTF-8') as score_file:
            score_file.write(updated)

    def __find_score__(self, name):
        scores = self.__upload_scoreboard__()
        if name in scores.keys():
            return scores[name]
        else:
            return None
