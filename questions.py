# Dictionary of quiz questions organized by subject
quiz_questions = {
    "Business Analytics": [
        {
            "question_text": "Which of the following is the primary goal of business analytics?",
            "answers": ["Improve operational efficiency", "Increase revenue", "Reduce costs", "All of the above"],
            "correct_answer": 3
        },
        {
            "question_text": "What technique is used to identify the most important factors driving a business outcome?",
            "answers": ["Linear regression", "Decision trees", "Principal component analysis", "Logistic regression"],
            "correct_answer": 1
        },
        {
            "question_text": "Which of the following is a key component of a balanced scorecard?",
            "answers": ["Financial metrics", "Customer metrics", "Internal process metrics", "All of the above"],
            "correct_answer": 3
        },
        {
            "question_text": "What is the primary purpose of A/B testing in business analytics?",
            "answers": ["To compare the performance of two different marketing campaigns", "To identify the root cause of a business problem", "To forecast future sales trends", "To segment customers based on their behavior"],
            "correct_answer": 0
        },
        {
            "question_text": "Which of the following is a common technique used for customer segmentation?",
            "answers": ["Cluster analysis", "Time series analysis", "Conjoint analysis", "Multivariate regression"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the main purpose of using data visualization in business analytics?",
            "answers": ["To make data more understandable", "To automate data analysis", "To collect more data", "To improve decision-making"],
            "correct_answer": 3
        },
        {
            "question_text": "Which of the following is a key metric used to measure the success of a marketing campaign?",
            "answers": ["Return on Investment (ROI)", "Customer Lifetime Value (CLV)", "Net Promoter Score (NPS)", "All of the above"],
            "correct_answer": 3
        },
        {
            "question_text": "What is the primary purpose of predictive analytics in a business setting?",
            "answers": ["To understand past performance", "To optimize current operations", "To forecast future trends", "To identify root causes of problems"],
            "correct_answer": 2
        },
        {
            "question_text": "Which of the following is a common technique used for demand forecasting?",
            "answers": ["Time series analysis", "Discrete choice modeling", "Conjoint analysis", "Structural equation modeling"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the primary purpose of using optimization techniques in business analytics?",
            "answers": ["To maximize profits", "To minimize costs", "To improve decision-making", "All of the above"],
            "correct_answer": 3
        }
    ],
    "Python": [
        {
            "question_text": "What is the output of the following code: `print(2 + 3 * 4)`",
            "answers": ["20", "14", "11", "5"],
            "correct_answer": 1
        },
        {
            "question_text": "Which of the following is not a built-in data structure in Python?",
            "answers": ["List", "Tuple", "Set", "HashMap"],
            "correct_answer": 3
        },
        {
            "question_text": "What is the purpose of the `try-except` block in Python?",
            "answers": ["To handle exceptions", "To define functions", "To import modules", "To define classes"],
            "correct_answer": 0
        },
        {
            "question_text": "Which of the following is a common use case for list comprehensions in Python?",
            "answers": ["Transforming data", "Filtering data", "Generating sequences", "All of the above"],
            "correct_answer": 3
        },
        {
            "question_text": "What is the output of the following code: `print(list(range(5, 10)))`",
            "answers": ["[5, 6, 7, 8, 9]", "[0, 1, 2, 3, 4]", "[5, 6, 7, 8]", "[5, 6, 7, 8, 9, 10]"],
            "correct_answer": 0
        },
        {
            "question_text": "Which of the following is a key difference between a list and a tuple in Python?",
            "answers": ["Lists are mutable, tuples are immutable", "Lists can only contain integers, tuples can contain any data type", "Lists are ordered, tuples are unordered", "Lists are faster than tuples"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the purpose of the `__init__()` method in a Python class?",
            "answers": ["To define the class constructor", "To define class attributes", "To define class methods", "To define the class name"],
            "correct_answer": 0
        },
        {
            "question_text": "Which of the following is a common way to import a module in Python?",
            "answers": ["import module", "from module import *", "import module as m", "All of the above"],
            "correct_answer": 3
        },
        {
            "question_text": "What is the output of the following code: `print(1 in [1, 2, 3])`",
            "answers": ["True", "False", "1", "None"],
            "correct_answer": 0
        },
        {
            "question_text": "Which of the following is a common use case for the `map()` function in Python?",
            "answers": ["Transforming elements in a list", "Filtering elements in a list", "Reducing elements in a list", "Sorting elements in a list"],
            "correct_answer": 0
        }
    ],
    "R": [
        {
            "question_text": "What is the primary use case for the `dplyr` package in R?",
            "answers": ["Data manipulation", "Data visualization", "Statistical modeling", "Web scraping"],
            "correct_answer": 0
        },
        {
            "question_text": "Which of the following is a common way to create a new variable in a data frame in R?",
            "answers": ["Using the `$` operator", "Using the `mutate()` function", "Using the `assign()` function", "All of the above"],
            "correct_answer": 3
        },
        {
            "question_text": "What is the primary purpose of the `ggplot2` package in R?",
            "answers": ["Data manipulation", "Statistical modeling", "Data visualization", "Web scraping"],
            "correct_answer": 2
        },
        {
            "question_text": "Which of the following is a common way to install a package in R?",
            "answers": ["Using the `install.packages()` function", "Using the `library()` function", "Using the `require()` function", "All of the above"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the output of the following code: `x <- c(1, 2, 3); mean(x)`",
            "answers": ["1", "2", "3", "2.0"],
            "correct_answer": 3
        },
        {
            "question_text": "Which of the following is a common way to apply a function to each element of a vector in R?",
            "answers": ["Using a `for` loop", "Using the `apply()` function", "Using the `lapply()` function", "All of the above"],
            "correct_answer": 3
        },
        {
            "question_text": "What is the primary purpose of the `tidyr` package in R?",
            "answers": ["Data manipulation", "Data visualization", "Web scraping", "Data reshaping"],
            "correct_answer": 3
        },
        {
            "question_text": "Which of the following is a common way to handle missing data in R?",
            "answers": ["Using the `na.omit()` function", "Using the `replace()` function", "Using the `ifelse()` function", "All of the above"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the output of the following code: `x <- c(1, 2, 3); y <- c(4, 5, 6); cor(x, y)`",
            "answers": ["0", "1", "-1", "None of the above"],
            "correct_answer": 1
        },
        {
            "question_text": "Which of the following is a common way to perform linear regression in R?",
            "answers": ["Using the `lm()` function", "Using the `glm()` function", "Using the `plot()` function", "All of the above"],
            "correct_answer": 0
        }
    ],
    "Data Structures and Algorithms": [
        {
            "question_text": "What is the time complexity of searching for an element in a binary search tree?",
            "answers": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "correct_answer": 1
        },
        {
            "question_text": "Which data structure is best suited for implementing a queue?",
            "answers": ["Array", "Linked List", "Stack", "Deque"],
            "correct_answer": 1
        },
        {
            "question_text": "What is the purpose of the merge sort algorithm?",
            "answers": ["To sort a list of elements", "To find the shortest path between two nodes", "To search for an element in a list", "To find the maximum element in a list"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the time complexity of the breadth-first search (BFS) algorithm?",
            "answers": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "correct_answer": 2
        },
        {
            "question_text": "Which data structure is best suited for implementing a hash table?",
            "answers": ["Array", "Linked List", "Binary Search Tree", "Array and Linked List"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the purpose of the quicksort algorithm?",
            "answers": ["To sort a list of elements", "To find the shortest path between two nodes", "To search for an element in a list", "To find the maximum element in a list"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the time complexity of the depth-first search (DFS) algorithm?",
            "answers": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "correct_answer": 2
        },
        {
            "question_text": "Which data structure is best suited for implementing a priority queue?",
            "answers": ["Array", "Linked List", "Heap", "Stack"],
            "correct_answer": 2
        },
        {
            "question_text": "What is the purpose of the dynamic programming algorithm?",
            "answers": ["To solve complex problems by breaking them down into smaller subproblems", "To find the shortest path between two nodes", "To search for an element in a list", "To find the maximum element in a list"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the time complexity of the insertion sort algorithm?",
            "answers": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
            "correct_answer": 3
        }
    ],
    "Design of Experiments": [
        {
            "question_text": "What is the primary purpose of a factorial experiment design?",
            "answers": ["To study the effects of multiple factors simultaneously", "To compare the means of two or more groups", "To determine the optimal settings of process parameters", "To assess the reliability of a product or process"],
            "correct_answer": 0
        },
        {
            "question_text": "Which of the following is a key assumption of the analysis of variance (ANOVA) technique?",
            "answers": ["The data is normally distributed", "The variances of the groups are equal", "The samples are independent", "All of the above"],
            "correct_answer": 3
        },
        {
            "question_text": "What is the primary purpose of a fractional factorial experiment design?",
            "answers": ["To study the effects of multiple factors simultaneously", "To compare the means of two or more groups", "To determine the optimal settings of process parameters", "To reduce the number of experimental runs required"],
            "correct_answer": 3
        },
        {
            "question_text": "Which of the following is a key advantage of a randomized block design?",
            "answers": ["It reduces the impact of nuisance factors", "It allows for the estimation of main effects and interactions", "It is less expensive to conduct than a completely randomized design", "All of the above"],
            "correct_answer": 0
        },
        {
            "question_text": "What is the primary purpose of a response surface methodology (RSM) experiment design?",
            "answers": ["To study the effects of multiple factors simultaneously", "To compare the means of two or more groups", "To determine the optimal settings of process parameters", "To assess the reliability of a product or process"],
            "correct_answer": 2
        },
        {
            "question_text": "Which of the following is a key assumption of the Taguchi method?",
            "answers": ["The data is normally distributed", "The variances of the groups are equal", "The signal-to-noise ratio is the primary quality characteristic", "All of the above"],
            "correct_answer": 2
        },
        {
            "question_text": "What is the primary purpose of a Latin square experiment design?",
            "answers": ["To study the effects of multiple factors simultaneously", "To compare the means of two or more groups", "To control for two nuisance factors", "To determine the optimal settings of process parameters"],
            "correct_answer": 2
        },
        {
            "question_text": "Which of the following is a key advantage of a cross-over design?",
            "answers": ["It reduces the impact of nuisance factors", "It allows for the estimation of main effects and interactions", "It can be used to compare the effects of two or more treatments within the same subject", "All of the above"],
            "correct_answer": 2
        },
        {
            "question_text": "What is the primary purpose of a mixture experiment design?",
            "answers": ["To study the effects of multiple factors simultaneously", "To compare the means of two or more groups", "To determine the optimal composition of a mixture", "To assess the reliability of a product or process"],
            "correct_answer": 2
        },
        {
            "question_text": "Which of the following is a key assumption of the regression analysis technique?",
            "answers": ["The data is normally distributed", "The variances of the groups are equal", "The relationship between the predictor and response variables is linear", "All of the above"],
            "correct_answer": 3
        }
    ]
}