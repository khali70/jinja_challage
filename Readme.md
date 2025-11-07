# ERPNext Jinja Challenge

## Project Overview
This mini project simulates a lightweight ERPNext customization exercise aimed at fresh graduates who have never worked with Python or Frappe. Candidates practice reading a simple HTML template, adding Jinja logic, and rendering deterministic output. The goal is to observe how quickly they understand clear requirements, reason about templating logic, and produce clean, working code.

## Repository Structure
- `jinja_challenge_template.html` – starter template containing inline instructions, control-flow examples, and placeholder data structures.
- `index.py` – minimal Python script that loads the template, renders it with Jinja2, and saves the result to `rendered_output.html`.
- `rendered_output.html` – sample output to use as a reference or golden copy when verifying candidate submissions.

## Prerequisites
- Python 3.9+ (any recent version works).
- `pip install jinja2` (only dependency).
- A basic text editor or IDE; no prior ERPNext or Frappe experience required.

## Running the Exercise
1. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
```bash
pip install jinja2
Render the template:
```

```bash
python index.py
```

Open `rendered_output.html` in a browser to review the generated page.

## Candidate Instructions
### Candidate tasks
1. Read `jinja_challenge_template.html` and understand the inline logic:
    - loops, conditionals, macros, and filters.
2. Modify or extend the template only if the interviewer provides additional requirements.
3. Re-run `index.py` and verify the generated `rendered_output.html` matches expectations.
4. Keep changes simple and well formatted; add short comments only when the logic isn’t obvious.

### Evaluation guidelines
Interviewers typically look for:
- Ability to reason about templating constructs without prior framework knowledge.
- Clean, readable code and organized HTML.
- Correctness of control flow (loops, conditionals, macro usage).
- Thought process: how you clarify requirements and test your work.


