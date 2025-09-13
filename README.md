# FOSSEE-TASK
Python Screening Task 3: Evaluating Open Source Models for Student Competence Analysis

## Overview
This project investigates whether open-source AI models can be adapted for analyzing student competence in Python learning. Specifically, this research examines CodeT5, a Transformer-based model trained on both natural language and source code.  

The project explores how CodeT5 can analyze Python written by students, identify gaps in their understanding, and stimulate learning by providing insights without directly giving solutions.

## Approach
To assess open-source AI models for student competence analysis in Python, I focused on CodeT5. This Transformer model, trained on both programming languages and natural language, was evaluated for its ability to:  
- Summarize student-written code in natural language  
- Indicate missing logic or misunderstandings  
- Provide conceptual checkpoints aligned with learning outcomes  

The evaluation plan involves testing CodeT5 on diverse student submissions (correct, partially correct, buggy) to see if it offers insights that allow meaningful reflection without solving the task directly.

## Reasoning
The model’s usability is evaluated based on:  
1. Generating useful high-level feedback, not just syntax corrections  
2. Adapting to educational prompts without fine-tuning  
3. Producing outputs interpretable by students and educators  

Small experiments are conducted where CodeT5 is prompted to summarize code logic or identify conceptual errors in beginner Python problems (loops, conditionals, functions). If the output helps students describe core concepts without giving solutions, it is a promising prototype for scalable, student-centered competence evaluation.

### Key Questions
1. **What makes a model good for high-level competence analysis?**  
   It assesses not just syntax but semantics, provides generalizable reasoning insights, and delivers feedback in student-accessible language without revealing exact answers.

2. **How would you test whether the model generates meaningful feedback?**  
   By comparing outputs for different student submissions of the same task—if misconceptions are identified and contextual feedback is provided, the outputs are meaningful.

3. **Are we trading off accuracy for interpretability or cost?**  
   More accurate outputs usually require fine-tuned models; lightweight models like CodeT5-small may be less nuanced but cheaper. A balance between interpretability and technical detail is important.

4. **Why CodeT5? Strengths and limitations**  
   **Strengths:** Human-readable explanations, multi-task capabilities, open-source.  
   **Limitations:** Can be ambiguous with logical errors; prompts must be carefully designed to avoid giving away solutions.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/FOSSEE-TASK.git
   cd FOSSEE-TASKA

2. **Install Dependencies**
```bash
pip install transformers torch
```
3. **Run the script**
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


