import argparse
import os
import re
import shutil
import subprocess
import sys

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover

    def load_dotenv():
        return False


try:
    from groq import Groq
except ImportError:  # pragma: no cover
    Groq = None

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

SYSTEM_PROMPT = "You are a Python code generator. Return only valid Python \
        code and nothing else. " "Do not include markdown fences,\
        explanations, comments, or any surrounding text."

GROQ_MODEL_CANDIDATES = [
    "openai/gpt-oss-120b",
    "qwen/qwen3.8-27b",
    "meta-llama/llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
]
EXAMPLE_TASKS = [
    "write a function that checks if a number is prime",
    "write a function that reverses a string without using slicing",
    "write a function that counts vowels in a string",
    "write a function that finds the factorial of a number",
    "write a function that returns the second largest number in a list",
    "write a function that merges two dictionaries \
        and keeps the latest values",
    "write a function that groups words by their \
        first letter into a dictionary",
    "write a function that removes duplicate numbers \
        from a list while preserving order",
]


def clean_code(raw_text):
    text = (raw_text or "").strip()
    text = re.sub(r"^```(?:python)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_with_ollama(prompt):
    ollama_binary = shutil.which("ollama")
    if not ollama_binary:
        raise RuntimeError("Ollama is not installed or not available on PATH.")

    command = [
        "ollama",
        "run",
        "llama3.2",
        f"SYSTEM: {SYSTEM_PROMPT}\nUSER: {prompt}",
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=180)
    if result.returncode != 0:
        raise RuntimeError(
            result.stderr.strip()
            or result.stdout.strip()
            or "Ollama generation failed."
        )
    return clean_code(result.stdout)


def generate_code(prompt):
    api_key = os.getenv("GROQ_API_KEY")

    if api_key and Groq is not None:
        client = Groq(api_key=api_key)
        last_error = RuntimeError("Groq returned empty code.")
        for model_name in GROQ_MODEL_CANDIDATES:
            try:
                completion = client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.1,
                    max_tokens=1024,
                )
                code = clean_code(completion.choices[0].message.content)
                if code:
                    return code
                last_error = RuntimeError(
                    f"Groq model {model_name} returned empty code."
                )
            except Exception as exc:
                last_error = exc

    else:
        last_error = RuntimeError(
            "GROQ_API_KEY is missing or the Groq client is unavailable."
        )

    if shutil.which("ollama"):
        try:
            return generate_with_ollama(prompt)
        except Exception as ollama_error:
            raise RuntimeError(f"Groq failed: {last_error}; Ollama fallback failed: \
                    {ollama_error}") from ollama_error

    raise RuntimeError(f"Unable to generate code. {last_error}")


def save_code(code, filename):
    with open(filename, "w", encoding="utf-8") as handle:
        handle.write(code.strip() + "\n")


def run_demo():
    for index, task in enumerate(EXAMPLE_TASKS, start=1):
        print(f"\n[+] Demo {index}/{len(EXAMPLE_TASKS)}: {task}")
        code = generate_code(task)
        output_name = f"generated_output_{index}.py"
        save_code(code, output_name)
        print("=" * 40)
        print(code)
        print("=" * 40)
        print(f"[+] Saved to {output_name}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate Python code from a natural-language task."
    )
    parser.add_argument(
        "task",
        nargs="*",
        help="Plain-English description of a Python function or script.",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run against the built-in list of 8 task descriptions.",
    )
    parser.add_argument(
        "--output",
        default="generated_output.py",
        help="Output filename for a single generated task.",
    )
    args = parser.parse_args()

    if args.demo:
        run_demo()
        return

    task = " ".join(args.task).strip()
    if not task:
        task = input("Enter task: ").strip()
    if not task:
        sys.exit(1)

    print(f"\n[+] Generating code for: {task}\n")
    code = generate_code(task)

    print("=" * 40)
    print(code)
    print("=" * 40)

    save_code(code, args.output)
    print(f"\n[+] Saved to {args.output}")


if __name__ == "__main__":
    main()
