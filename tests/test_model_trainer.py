from src.model_trainer import RandomForestTrainer


def test_optuna_fake(monkeypatch, dummy_df):
    X = dummy_df.drop(columns=['Potability'])
    y = dummy_df['Potability']
    trainer = RandomForestTrainer(X, X, y, y)

    monkeypatch.setattr(trainer, 'objective', lambda trial: 0.9)
    study = trainer.run_optuna(n_trials=2)
    assert study.best_value == 0.9
