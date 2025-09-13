from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_model():
    model_name = "Salesforce/codet5-small"  
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

def summarize_code(code_snippet):
    tokenizer, model = load_model()
    
    inputs = tokenizer("summarize: " + code_snippet, return_tensors="pt")
    output = model.generate(**inputs, max_length=50)
    return tokenizer.decode(output[0], skip_special_tokens=True)

if __name__ == "__main__":
    student_code = """def add(a, b):
    return a + b"""

    print("🔹 Student Code:\n", student_code)
    summary = summarize_code(student_code)
    print("\n🔹 CodeT5 Summary:\n", summary)
