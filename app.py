import sys
import os
import sqlite3
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QComboBox, QPushButton, QLabel, 
                            QRadioButton, QButtonGroup, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from questions import quiz_questions

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('quiz_bowl.db')
        self.cursor = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        # Create questions table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                subject TEXT,
                question_text TEXT,
                answer_1 TEXT,
                answer_2 TEXT,
                answer_3 TEXT,
                answer_4 TEXT,
                correct_answer INTEGER
            )
        ''')
        
        # Create scores table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY,
                subject TEXT,
                score INTEGER,
                total_questions INTEGER,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Populate database with questions if empty
        self.cursor.execute("SELECT COUNT(*) FROM questions")
        if self.cursor.fetchone()[0] == 0:
            self.populate_questions()
        
        self.conn.commit()

    def populate_questions(self):
        for subject, questions in quiz_questions.items():
            for question in questions:
                self.cursor.execute('''
                    INSERT INTO questions (subject, question_text, answer_1, answer_2, 
                                        answer_3, answer_4, correct_answer)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    subject,
                    question['question_text'],
                    question['answers'][0],
                    question['answers'][1],
                    question['answers'][2],
                    question['answers'][3],
                    question['correct_answer']
                ))
        self.conn.commit()

    def get_questions(self, subject):
        self.cursor.execute('''
            SELECT question_text, answer_1, answer_2, answer_3, answer_4, correct_answer 
            FROM questions 
            WHERE subject = ?
        ''', (subject,))
        return self.cursor.fetchall()

    def save_score(self, subject, score, total_questions):
        self.cursor.execute('''
            INSERT INTO scores (subject, score, total_questions)
            VALUES (?, ?, ?)
        ''', (subject, score, total_questions))
        self.conn.commit()

    def close(self):
        self.conn.close()

class QuizQuestion(QWidget):
    def __init__(self, question_data, parent=None):
        super().__init__(parent)
        self.question_data = question_data
        self.selected_answer = None
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Question text
        question_label = QLabel(self.question_data[0])  # question_text
        question_label.setFont(QFont("Arial", 12, QFont.Bold))
        question_label.setWordWrap(True)
        layout.addWidget(question_label)

        # Radio button group for answers
        self.button_group = QButtonGroup()
        for i in range(4):
            radio = QRadioButton(self.question_data[i + 1])  # answer_1 through answer_4
            self.button_group.addButton(radio, i)
            layout.addWidget(radio)

        self.button_group.buttonClicked.connect(self.on_answer_selected)
        self.setLayout(layout)

    def on_answer_selected(self, button):
        self.selected_answer = self.button_group.id(button)

    def is_correct(self):
        return self.selected_answer == self.question_data[5]  # correct_answer

    def get_selected_answer(self):
        return self.selected_answer

class QuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.current_question_index = 0
        self.questions = []
        self.score = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Quiz Bowl')
        self.setGeometry(100, 100, 600, 400)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # Create subject selection screen
        self.create_subject_selection()

    def create_subject_selection(self):
        # Clear any existing widgets
        for i in reversed(range(self.main_layout.count())): 
            self.main_layout.itemAt(i).widget().setParent(None)

        # Add subject selection widgets
        subject_label = QLabel("Select a subject:")
        subject_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.main_layout.addWidget(subject_label)

        self.subject_combo = QComboBox()
        self.subject_combo.addItems(quiz_questions.keys())
        self.main_layout.addWidget(self.subject_combo)

        start_button = QPushButton("Start Quiz")
        start_button.clicked.connect(self.start_quiz)
        self.main_layout.addWidget(start_button)

    def start_quiz(self):
        subject = self.subject_combo.currentText()
        self.questions = self.db.get_questions(subject)
        if not self.questions:
            QMessageBox.warning(self, "Error", "No questions available for this subject!")
            return

        self.current_question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        # Clear existing widgets
        for i in reversed(range(self.main_layout.count())): 
            self.main_layout.itemAt(i).widget().setParent(None)

        # Show progress
        progress_label = QLabel(f"Question {self.current_question_index + 1} of {len(self.questions)}")
        self.main_layout.addWidget(progress_label)

        # Create question widget
        self.current_question = QuizQuestion(self.questions[self.current_question_index])
        self.main_layout.addWidget(self.current_question)

        # Add submit button
        submit_button = QPushButton("Submit Answer")
        submit_button.clicked.connect(self.submit_answer)
        self.main_layout.addWidget(submit_button)

    def submit_answer(self):
        if self.current_question.get_selected_answer() is None:
            QMessageBox.warning(self, "Warning", "Please select an answer!")
            return

        if self.current_question.is_correct():
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        # Save score to database
        self.db.save_score(
            self.subject_combo.currentText(),
            self.score,
            len(self.questions)
        )

        # Clear existing widgets
        for i in reversed(range(self.main_layout.count())): 
            self.main_layout.itemAt(i).widget().setParent(None)

        # Show results
        results_label = QLabel(f"Quiz Complete!\nScore: {self.score}/{len(self.questions)}")
        results_label.setFont(QFont("Arial", 14, QFont.Bold))
        results_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(results_label)

        # Add button to return to subject selection
        new_quiz_button = QPushButton("Take Another Quiz")
        new_quiz_button.clicked.connect(self.create_subject_selection)
        self.main_layout.addWidget(new_quiz_button)

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == '__main__':
    if os.path.exists('quiz_bowl.db'):
        os.remove('quiz_bowl.db')
    
    app = QApplication(sys.argv)
    quiz = QuizWindow()
    quiz.show()
    sys.exit(app.exec_())