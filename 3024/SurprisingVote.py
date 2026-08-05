"""SurprisingVote"""
def main():
    """Main Function"""
score_all = float(input())
score_max = float(input())

min_score = max(0.0, score_all - (2 * score_max))
if score_max - min_score > 2:
    print("Surprising")
else:
    print("Not surprising")

main()
