#  Validation
import re
import json


def read_file_lines(filepath):
    """
    Reads the given file and returns a list of its lines.
    """

    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()


def count_lines(lines):
    """
    Counts total lines, blank lines, and lines of code
    (lines of code = not blank AND not a comment).

    Returns a dictionary with the stats.
    """

    total_lines = len(lines)
    blank_lines = 0
    comment_lines = 0
    code_lines = 0

    for line in lines:
        stripped = line.strip()
        if stripped == "":
            blank_lines += 1
        elif stripped.startswith("#"):
            comment_lines += 1
        else:
            code_lines += 1

    return {
        "total_lines": total_lines,
        "blank_lines": blank_lines,
        "comment_lines": comment_lines,
        "code_lines": code_lines,
    }


def count_complexity(lines):
    """
    Counts decision-making and looping statements.
    Returns a dictionary containing the counts.
    """

    # Store counts for each keyword
    complexity = {"if": 0, "elif": 0, "else": 0, "for": 0, "while": 0}

    # Check each line in the file
    for line in lines:

        # Remove leading/trailing spaces
        stripped = line.strip()

        # Count statements
        if stripped.startswith("if "):
            complexity["if"] += 1

        elif stripped.startswith("elif "):
            complexity["elif"] += 1

        elif stripped.startswith("else:") or stripped.startswith("else "):
            complexity["else"] += 1

        elif stripped.startswith("for "):
            complexity["for"] += 1

        elif stripped.startswith("while "):
            complexity["while"] += 1

    return complexity


def count_comments(lines):
    """
    Counts comment lines and calculates comment ratio.
    Handles:
    1. Single-line comments (#)
    2. Multi-line docstrings (''' ''' or \"\"\" \"\"\")
    """

    comment_lines = 0
    inside_docstring = False

    # Check every line
    for line in lines:

        stripped = line.strip()

        # Detect start/end of docstrings
        if '"""' in stripped or "'''" in stripped:

            comment_lines += 1

            # Toggle docstring mode
            # If we enter a docstring -> True
            # If we leave a docstring -> False
            if stripped.count('"""') == 1 or stripped.count("'''") == 1:
                inside_docstring = not inside_docstring

            continue

        # Count lines inside a docstring
        if inside_docstring:
            comment_lines += 1
            continue

        # Count normal comments beginning with #
        if stripped.startswith("#"):
            comment_lines += 1

    # Calculate percentage
    total_lines = len(lines)

    if total_lines > 0:
        comment_ratio = (comment_lines / total_lines) * 100
    else:
        comment_ratio = 0

    return {"comment_lines": comment_lines, "comment_ratio": round(comment_ratio, 2)}


def check_snake_case(name):
    return bool(re.match(r"^[a-z_][a-z0-9_]*$", name))


def extract_variables(lines):
    violations = []
    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#") or not stripped:
            continue

        m = re.match(r"([a-zA-Z_]\w*)\s*=(?!=)", stripped)
        if m:
            var_name = m.group(1)
            if not check_snake_case(var_name):
                violations.append(var_name)
    return violations


def build_report(line_counts, complexity, comment_ratio, violations):
    return {
        "line_counts": line_counts,
        "complexity": complexity,
        "comment_ratio_pct": round(comment_ratio, 2),
        "snake_case_violations": violations,
        "health_score": compute_score(
            line_counts, complexity, comment_ratio, violations
        ),
    }


def compute_score(lc, cx, cr, v):
    score = 100
    total = lc.get("total_lines", 1)
    complexity_total = sum(cx.values())
    if complexity_total / max(total, 1) > 0.2:
        score -= 20
    if cr < 5:  # less than 5% comments — under-documented
        score -= 15
    score -= len(v) * 5  # each violation costs 5 points
    return max(0, score)


def print_report(report):
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    import sys

    filepath = sys.argv[1] if len(sys.argv) > 1 else "testfile.py"

    try:
        lines = read_file_lines(filepath)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

    line_counts = count_lines(lines)
    complexity = count_complexity(lines)
    comments = count_comments(lines)
    violations = extract_variables(lines)

    report = build_report(
        line_counts, complexity, comments.get("comment_ratio", 0), violations
    )

    # Add raw comment lines into the report for completeness
    report["comment_lines"] = comments.get("comment_lines", 0)

    print_report(report)
