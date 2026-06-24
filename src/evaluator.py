import os
import pandas as pd

from src.normalizer import (
    clean_name,
    normalize_date,
    normalize_notice
)


def calculate_recall(
    ground_truth_path,
    prediction_path
):

    gt = pd.read_csv(
        ground_truth_path
    )

    pred = pd.read_csv(
        prediction_path
    )

    # -------------------------
    # Normalize filenames
    # -------------------------

    gt["File Name"] = (
        gt["File Name"]
        .astype(str)
        .str.strip()
    )

    pred["base_filename"] = pred[
        "filename"
    ].apply(
        lambda x: os.path.splitext(
            os.path.splitext(
                str(x)
            )[0]
        )[0]
    )

    mapping = {

        "Aggrement Value":
            "agreement_value",

        "Aggrement Start Date":
            "agreement_start_date",

        "Aggrement End Date":
            "agreement_end_date",

        "Renewal Notice (Days)":
            "renewal_notice_days",

        "Party One":
            "party_one",

        "Party Two":
            "party_two"
    }

    results = {}

    for gt_col, pred_col in mapping.items():

        correct = 0

        total = len(gt)

        for _, gt_row in gt.iterrows():

            file_name = str(
                gt_row["File Name"]
            ).strip()

            pred_match = pred[
                pred["base_filename"]
                == file_name
            ]

            if pred_match.empty:

                print(
                    f"Missing prediction for: {file_name}"
                )

                continue

            pred_row = pred_match.iloc[0]

            gt_value = str(
                gt_row[gt_col]
            ).strip()

            pred_value = str(
                pred_row[pred_col]
            ).strip()

            # -------------------------
            # Normalize Party Names
            # -------------------------

            if "Party" in gt_col:

                gt_value = clean_name(
                    gt_value
                )

                pred_value = clean_name(
                    pred_value
                )

            # -------------------------
            # Normalize Dates
            # -------------------------

            elif "Date" in gt_col:

                gt_value = normalize_date(
                    gt_value
                )

                pred_value = normalize_date(
                    pred_value
                )

            # -------------------------
            # Normalize Notice Period
            # -------------------------

            elif "Renewal" in gt_col:

                gt_value = normalize_notice(
                    gt_value
                )

                pred_value = normalize_notice(
                    pred_value
                )

            # -------------------------
            # Agreement Value
            # -------------------------

            else:

                gt_value = gt_value.lower()

                pred_value = pred_value.lower()

            # -------------------------
            # Debug Output
            # -------------------------

            #print("\n-------------------")
            #print("FILE :", file_name)
            #print("FIELD:", gt_col)
            #print("GT   :", gt_value)
            #print("PRED :", pred_value)
            #print("MATCH:", gt_value == pred_value)

            if gt_value == pred_value:

                correct += 1

        recall = (
            correct / total
        ) * 100

        results[gt_col] = {

            "correct": correct,

            "total": total,

            "recall": round(
                recall,
                2
            )
        }

    return results