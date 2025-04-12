from src.data_pipeline import DataPipeline, DataPreprocessor


def test_pipeline_load_and_clean(tmp_path):
    csv_path = tmp_path / 'test_water.csv'
    csv_path.write_text(
        'ph,Hardness,Solids,Potability\n7.0,200,10000,0\n,180,9800,1\n6.5,,10200,0'
    )

    pipeline = DataPipeline(str(csv_path))
    df = pipeline.load_and_clean_data()

    assert df.isnull().sum().sum() == 0
    assert 'ph' in df.columns
    assert 'Potability' in df.columns


def test_data_preprocessing_split_and_smote(dummy_df):
    pre = DataPreprocessor(dummy_df, target='Potability')
    X_train, X_test, y_train, y_test = pre.split_data()
    X_res, y_res = pre.apply_smote(X_train, y_train)

    assert len(X_res) > len(X_train)
    assert len(X_res) == len(y_res)
