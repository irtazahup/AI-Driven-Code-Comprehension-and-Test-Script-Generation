import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
sample_diff = """
    --- old_version
    +++ new_version
    @@ -1,3 +1,5 @@
    def calculate_discount(price):
    +    if price > 100:
    +        return price * 0.8
         return price * 0.9
    """

SYSTEM_PROMPT = """
You are a Senior QA Automation Engineer. 
Your task is to analyze a 'Git Diff' and write a Pytest script that tests the NEW logic.
Rules:
1. Use 'pytest' framework.
2. Only return the Python code. No explanations.
3. If the change is a bug fix, write a test that would have caught the bug.
4. If it's a new feature, write a test for the success and failure cases.
"""

file_path = "app/calculator.py"
module_path = file_path.replace("/", ".").replace(".py", "") # Converts to 'app.calculator'

# 2. Update the User Message to provide context
prompt_content = f"""
PROJECT CONTEXT:
- The file being modified is: `{file_path}`
- You should import the function using: `from {module_path} import calculate_discount`

GIT DIFF:
{sample_diff}
"""

def generate_test_from_diff(diff_text):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_content} # Using the rich context here
        ],
        temperature=0.1
    )
    return completion.choices[0].message.content
# ... (rest of your code above remains same)

if __name__ == "__main__":
    # 1. The sample diff
    sample_diff = """
    --- old_version
    +++ new_version
    @@ -1,3 +1,5 @@
    def calculate_discount(price):
    +    if price > 100:
    +        return price * 0.8
         return price * 0.9
    """
    
    print("Generating test script...")
    test_code = generate_test_from_diff(sample_diff)
    
    # 2. THE FIX: Ensure the directory exists
    os.makedirs("tests", exist_ok=True) 
    
    # 3. Write the file
    with open("tests/test_calculator.py", "w") as f:
        f.write(test_code)
        
    print("Done! Check tests/test_calculator.py")