import re

class ScoreKeeper:
    def __init__(self, text):
        self.text = text
        self.categories, self.scores = self.parse_text()
        self.score_dict = self.pairs_to_dict(zip(self.categories, self.scores))
    
    def parse_text(self):
        lines = self.text.strip().split('\n')
        categories = []
        scores = []
        
        for line in lines:
            category, score = line.rsplit(None, 1)  # Split the line from the last whitespace
            categories.append(category)
            scores.append(int(score))
        return categories, scores
    
    @staticmethod
    def pairs_to_dict(pairs):
        return {p[0]:p[1] for p in pairs}
    
    def score_from_message(self, message):
        matches = re.findall(r'<([^>]+)>', message)
        total_score = 0
        for match in matches:
            total_score += self.score_dict.get(match, 0)
        return total_score

class User:
    def __init__(self):
        pass
    
    @staticmethod
    def get_accomplishments():
        accomplishments = input("Enter your accomplishments for today (separate each with a newline):\n")
        return accomplishments

class Application:
    def __init__(self):
        self.score_keeper = ScoreKeeper(text)  # Using the 'text' defined in the original snippets
        # For simplicity, I'm not adding openai here. Instead, you can expand the structure to incorporate it.
    
    def annotate_and_score(self, accomplishments):
        # Here's where you would have used the OpenAI completion
        # For this example, I'll use the accomplishments string directly
        # Assuming OpenAI returns a string with the proper format, we'll use that format for simplicity.
        message = accomplishments  # In a real scenario, replace this with the OpenAI returned text
        
        # Use the ScoreKeeper to compute the score
        score = self.score_keeper.score_from_message(message)
        return score
    
    def run(self):
        accomplishments = User.get_accomplishments()
        score = self.annotate_and_score(accomplishments)
        print(f"Total score for today's accomplishments: {score}")

if __name__ == "__main__":
    app = Application()
    app.run()
