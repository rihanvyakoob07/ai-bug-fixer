# demo_bug.py
def calculate_average(scores):
    """
    Calculates the average of a list of scores.
    BUG: Raises ZeroDivisionError if all scores are zero or list is empty,
         and silently ignores negative scores (which should be invalid).
    """
    total = 0
    count = 0
    for s in scores:
        if s >= 0:
            total += s
            count += 1
        # BUG: negative scores are ignored, but maybe they shouldn't be
    
    return total / count  # BUG: division by zero if no valid scores


def main():
    student_scores = [0, 0, -5, -10]  # Edge-case triggers bug
    avg = calculate_average(student_scores)
    print(f"Average score: {avg}")


if __name__ == "__main__":
    main()

