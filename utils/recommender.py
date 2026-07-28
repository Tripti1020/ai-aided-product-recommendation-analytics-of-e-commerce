import pandas as pd

def fetch_recommendations(selected_item, rules_dataset):

    rules_dataset.columns = rules_dataset.columns.str.strip()

    recommendations = []

    for _, row in rules_dataset.iterrows():

        antecedent = str(row["antecedents"]).strip()

        # Match even if selected product is part of a multi-item antecedent
        if selected_item.lower() in antecedent.lower():

            consequents = str(row["consequents"]).split(",")

            for item in consequents:
                item = item.strip()
                if item.lower() != selected_item.lower():
                    recommendations.append(item)

    # Remove duplicates
    recommendations = list(dict.fromkeys(recommendations))

    return recommendations