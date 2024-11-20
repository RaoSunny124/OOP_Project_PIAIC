class Student():
    def __init__(self , name , score ):
        self.name = name
        self.score = score

    def calculate_average(self):
        average =  sum(self.score) / len(self.score)
        return average  

    def is_passing(self):
        for score in self.score:
            if score < 40:
                return f"Fail (failed in {self.subject})"
        return 'pass'





