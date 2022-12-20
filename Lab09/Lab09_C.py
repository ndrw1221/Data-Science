import numpy as np
import pandas as pd
from sklearn import model_selection, linear_model


def main():
    df = pd.read_csv("./epldata_final.csv")
    df_required = df.loc[
        :,
        [
            "fpl_points",
            "age",
            "page_views",
            "new_signing",
            "big_club",
            "position_cat",
            "market_value",
        ],
    ]
    df_required["page_views_log2"] = np.log2(df_required["page_views"])
    df_required["age_square"] = df.apply(lambda row: row["age"] ** 2, axis=1)
    del df_required["page_views"]
    page_views_log2 = df_required.pop("page_views_log2")
    age_square = df_required.pop("age_square")
    df_required.insert(2, "age_square", age_square)
    df_required.insert(3, "page_views_log2", page_views_log2)

    df_train, df_test = model_selection.train_test_split(df_required)

    reg = linear_model.LinearRegression()
    reg.fit(df_train.drop("market_value", axis=1), df_train.loc[:, "market_value"])

    market_value_criterias = [
        "fpl_points",
        "age",
        "age_square",
        "log2_page_views",
        "new_signing",
        "big_club",
        "position_club",
    ]
    print(f"\nBeta_0: {reg.intercept_}")
    for i, coef in enumerate(reg.coef_):
        print(f"Beta_{i+1} ({market_value_criterias[i] }): {coef}")

    Rsquare_train = reg.score(
        df_train.drop("market_value", axis=1), df_train.loc[:, "market_value"]
    )
    Rsquare_test = reg.score(
        df_test.drop("market_value", axis=1), df_test.loc[:, "market_value"]
    )

    print(f"\nThe R square score on the training set is: {Rsquare_train}")
    print(f"The R square score on the test set is: {Rsquare_test}")


if __name__ == "__main__":
    main()
