class QuizBrain:
    def __init__(self, questions: list):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> tuple[str, str]:
        current = self.question_list[self.question_number]
        self.question_number += 1
        return current.question, current.answer

    def check_answer(self, user_answer: str, correct_answer: str) -> bool:
        is_correct = user_answer.strip().lower() == correct_answer.lower()
        if is_correct:
            self.score += 1
        return is_correct

    def get_score(self) -> tuple[int, int]:
        return self.score, self.question_number
