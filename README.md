# DS 3850 - Quiz Bowl GUI Application

GUI Quiz Bowl Application for DS 3850. Built with Python, PyQT and SQLite3.

## `app.py`

The app.py file contains the functions and main method that runs the GUI application. When the app opens, it first creates the SQLite Database using the dictionary in `questions.py`. 

In the GUI, it will provide a dropdown menu where you can choose the topic of the quizbowl, and then go through the questions. After the quiz is finished, your score will be shown and the user will be prompted to choose another topic to quiz themselves.

## `questions.py`

The questions.py file is a hard-coded dictionary that is used to populate the SQLite3 database each time the app is run. To edit the questions, follow the format below to add your own questions and topics:

```python
{
  # Other Topics
  # .
  # .
  # .
  "your_topic":[
    {
        "question_text": "Add your question here",
        "answers":["Answer1","Answer2","Answer3","Answer4"],
        "correct_answer":1 # index of the answer in the answers list
    },
    # Repeat for each question
  ],
  # Repeat for each topic
}
```

The keys `question_text`, `answers`, and `correct_answer` keys must be the same, but the placeholder strings should be edited to your liking.

###### (Or you can generate questions with AI, and make sure to pass the `questions.py` file to match the formatting)
