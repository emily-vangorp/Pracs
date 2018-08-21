def main():
    result = get_result()
    print(result)
   


def get_result():
    score = float(input("Enter score: "))
     if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()
