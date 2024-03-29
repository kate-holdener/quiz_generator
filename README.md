# Generate random quizzes from a question pool
This python script uses a question pool to generate randomized quizzes. This way, students will be unlikely to copy answers from their neighbores.

To use this script, you will need a question pool - a simple text file with one question per line. An example question pool file is provided as <code>question_pool.txt</code>.

To run the script, you will first need to install the dependencies listed in requirements.txt:
<code>pip install -r requirements.txt</code>

The main script is <code>generator.py</code>

```
usage: generator.py [-h] question_file num_quizzes questions_per_quiz quiz_file

Generate different quizes based on a question pool

positional arguments:
  question_file       question pool file
  num_quizzes         number of quizzes to generate
  questions_per_quiz  number of questions per quiz
  quiz_file           Doc file where quizzes are written

optional arguments:
  -h, --help          show this help message and exit
```
For example, the following command line will generate 50 quizzes (5 questions each) using questions from question_pool.txt. The result will be written to SampleQuiz.doc (with one quiz per page).
```
python3 generator.py question_pool.txt 50 5 SampleQuiz.doc
```
