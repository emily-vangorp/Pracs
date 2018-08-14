def main():
    score = get_score()
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score

main()
