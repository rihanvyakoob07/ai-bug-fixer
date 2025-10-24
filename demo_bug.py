# demo_bug.py
def calculate_average(scores):
    """
    Calculates the average of a list of scores.
    """
    valid_scores = [s for s in scores if s >= 0]
    if not valid_scores:
        raise ValueError("No valid scores provided")
    return sum(valid_scores) / len(valid_scores)


def main():
    student_scores = [0, 0, -5, -10]  # Edge-case triggers bug
    try:
        avg = calculate_average(student_scores)
        print(f"Average score: {avg}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()