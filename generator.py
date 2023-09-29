import argparse
import docx
import random

# Read in command line arguments
parser = argparse.ArgumentParser(description='Generate different quizes based on a question pool')

parser.add_argument('question_file', type=str, help='question pool file')
parser.add_argument('num_quizzes', type=int, help='number of quizzes to generate')
parser.add_argument('questions_per_quiz', type=int, help='number of questions per quiz')
parser.add_argument('quiz_file', type=str, help='Doc file where quizzes are written')

args=parser.parse_args()

#read in the question pool
all_questions = []
with open(args.question_file, 'r') as question_pool:
   for q in question_pool:
      all_questions.append(q)

unused_indices = [*range(0, len(all_questions))]

# generate required number of quizzes
unique_indices = []
for i in range(0, args.num_quizzes):
   quiz_questions = random.sample(unused_indices, args.questions_per_quiz)
   unique_indices.append(quiz_questions)

   print(unused_indices)

   # remove used questions from the list
   for index in sorted(quiz_questions, reverse=True):
      unused_indices.remove(index)

# generate quiz documents
all_quizzes = docx.Document()
for questions in unique_indices:
   for q in questions:
      all_quizzes.add_paragraph(all_questions[q])
   all_quizzes.add_page_break()

all_quizzes.save(args.quiz_file)
