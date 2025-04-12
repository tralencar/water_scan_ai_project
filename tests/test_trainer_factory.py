from src.trainer_factory import TrainerFactory


def test_create_trainer_success(dummy_df):
    X = dummy_df.drop(columns=['Potability'])
    y = dummy_df['Potability']

    trainer = TrainerFactory.create_trainer('random_forest', X, X, y, y)
    assert trainer.__class__.__name__ == 'RandomForestTrainer'


def test_create_trainer_invalid_model(dummy_df):
    X = dummy_df.drop(columns=['Potability'])
    y = dummy_df['Potability']

    try:
        TrainerFactory.create_trainer('naive_bayes', X, X, y, y)
    except ValueError as e:
        assert 'não suportado' in str(e) or 'not supported' in str(e)
