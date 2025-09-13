# FOSSEE-TASK
Python Screening Task 3: Evaluating Open Source Models for Student Competence Analysis

## Overview
This project will investigate whether open-source AI models can be adapted for analyzing student competence in Python learning. In particular, this research examines CodeT5, a Transformer-based model trained on (1) natural language and (2) source code and discusses how a Transformer-based model, such as CodeT5, can analyze Python written in a student's natural language and used to identify a gap in the students' research and to stimulate the students' learning to draw and inspire insights without directly providing solutions.

## Approach

To assess open-source AI models for student competence analysis within Python, I looked at CodeT5, a Transformer model that was trained on both programming languages and natural languages. My idea was to see how the pre-existing skills of CodeT5 for code summarization, translation, and completion might be used to examine student written programs in Python. More specifically, I was interested in whether CodeT5 could offer a natural-language summary of student code, indicate missing logic or misunderstandings, and provide conceptual checkpoints that align with learning outcomes. The evaluation plan is simple - I will evaluate CodeT5 on a number of diverse student submissions (correct, partially correct, buggy) and see if CodeT5 offers insights to allow for meaningful reflection, without solving the task directly.

## Reasoning
The model's usability is evaluated on criteria like: (a) on generating useful feedback at a higher level rather than as syntax correction at a lower level, (b) on adapting to an educational prompt without fine-tuning the model, and (c) on producing outputs that can be interpreted by students and educators. Usability is verified through small experiments in which CodeT5 is prompted to provide a code logic summary or identify conceptual errors for beginner Python problems (loops, conditionals, functions). If the output indicates whether students can describe core concepts - not providing solutions - it's a good prototype for scalable, inexpensive, and student-centered competence evaluation.

## Reasoning
1. What makes a model good for high-level competence analysis?
It has to assess not just syntax but also semantics, offer generalizable insight into reasoning, and provide feedback in student-accessible language without sharing the exact answers.

2. How would you test to see whether model generates meaningful prompts?
By comparing outputs based on different student submissions of the same task—whether the model identifies misconceptions and provides contextual feedback indicates the outputs have meaning.

3. Are we trading-off accuracy for interpretability or cost?
More accurate outputs may come from more expensive fine-tuned models; lightweight models, i.e., CodeT5-small, could provide less nuance and may be cheaper; sometimes interpretability will trade off technical detail; we can find a balance.

4. Why CodeT5?  What are the strengths and limitations?
   
We select CodeT5 because it is trained on both natural language + code, able to summarize and translate, and is free in the Hugging Face. 
Strengths: human-readable explanations; multi-task capabilities; open source.
Limitations: sometimes ambiguous with logical errors; prompts must be very careful to avoid giving way to a solution.

## Setup instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/novavitals.git
   cd novavitals
2. Install Dependencies
```bash
npm install
```
3. Run the script
```
python demo.py
```
## References
1. https://arxiv.org/abs/2109.00859
2. https://www.salesforce.com/blog/codet5/
3. https://huggingface.co/Salesforce/codet5-small

### 👩‍💻 About the Creator
**Name:** Riya Joshi
**Background:** 3rd year Computer Science Student from Vellore Institute of Technology, Chennai


