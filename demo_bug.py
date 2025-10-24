# demo_bug.py
def calculate_average(scores):
    """
    Calculates the average of a list of non-negative scores.

    Args:
        scores (list): A list of numeric scores.

    Returns:
        float: The average score.

    Raises:
        ValueError: If the input list is empty or all scores are invalid.
    """
    if not scores:
        raise ValueError("Input list is empty")

    valid_scores = [s for s in scores if s >= 0]
    if not valid_scores:
        raise ValueError("All scores are invalid")

    total = sum(valid_scores)
    count = len(valid_scores)

    return total / count


def main():
    try:
        student_scores = [0, 0, -5, -10]  
        avg = calculate_average(student_scores)
        print(f"Average score: {avg}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()