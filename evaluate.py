from src.evaluator import (
    calculate_recall
)

results = calculate_recall(

    "data/test.csv",

    "predictions/predictions.csv"
)

print("\n")
print("=" * 60)
print("RECALL EVALUATION")
print("=" * 60)

for field, stats in results.items():

    print(
        f"{field:<25} "
        f"{stats['correct']}/{stats['total']} "
        f"Recall: {stats['recall']}%"
    )

print("=" * 60)