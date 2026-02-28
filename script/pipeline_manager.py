import subprocess
import os
import sys
from test_generator import generate_test_from_diff

def run_tests():
    """Runs pytest and captures output."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_calculator.py"], 
        capture_output=True, 
        text=True
    )
    return result.returncode, result.stdout + result.stderr

def self_heal(original_diff, error_message):
    """Sends the failure details back to the AI for a second attempt."""
    print("🩹 AI is analyzing the error to fix the test...")
    
    repair_context = f"""
    The previous test failed. 
    ERROR:
    {error_message}
    
    ORIGINAL CHANGE:
    {original_diff}
    
    Please provide the FIXED Python code only.
    """
    return generate_test_from_diff(repair_context)

def main():
    # Simulated Diff (In Phase 4, we will get this from Git)
    sample_diff = """
    --- old_version
    +++ new_version
    @@ -1,3 +1,5 @@
    def calculate_discount(price):
    +    if price > 100:
    +        return price * 0.8
         return price * 0.9
    """
    
    # Ensure test directory exists
    os.makedirs("tests", exist_ok=True)
    test_file_path = "tests/test_calculator.py"

    print("🚀 Step 1: Generating Test...")
    test_code = generate_test_from_diff(sample_diff)
    
    with open(test_file_path, "w") as f:
        f.write(test_code)
    
    print("🧪 Step 2: Running Generated Test...")
    exit_code, output = run_tests()
    
    if exit_code == 0:
        print("✅ SUCCESS: AI generated a valid passing test!")
    else:
        print("❌ FAILURE: Initial test failed. Initiating Self-Healing...")
        
        # --- SELF HEALING LOOP ---
        fixed_code = self_heal(sample_diff, output)
        
        with open(test_file_path, "w") as f:
            f.write(fixed_code)
            
        print("🧪 Step 3: Re-running Fixed Test...")
        new_exit_code, new_output = run_tests()
        
        if new_exit_code == 0:
            print("✨ FIXED: The AI successfully healed the test!")
        else:
            print("💀 CRITICAL: Self-healing failed.")
            print(f"Final Error:\n{new_output}")

if __name__ == "__main__":
    main()