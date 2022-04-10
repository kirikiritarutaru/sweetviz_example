import pandas as pd
import sweetviz as sv
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    boston = load_boston()
    df = pd.DataFrame(boston.data, columns=boston.feature_names)
    df['MEDV'] = boston.target
    print(df.head())
    x_train, x_test, y_train, y_test = train_test_split(
        df.iloc[:, 0:13], df.iloc[:, 13], test_size=0.2, random_state=1
    )

    df_train = pd.concat([x_train, y_train], axis=1)
    df_test = pd.concat([x_test, y_test], axis=1)

    my_report = sv.compare([df_train, "Train"], [df_test, "Test"], "MEDV")
    my_report.show_html("sweetviz_report_2col.html")
