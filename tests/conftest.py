import pandas as pd
import pytest


@pytest.fixture
def dummy_df():
    """Fixture with simulated water potability data"""
    return pd.DataFrame(
        {
            'ph': [7.0, 6.8, 6.5],
            'Hardness': [200, 180, 160],
            'Solids': [10000, 9800, 10200],
            'Potability': [0, 1, 0],
        }
    )
