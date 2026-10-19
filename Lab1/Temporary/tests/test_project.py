from pathlib import Path
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data" / "daily-min-temperatures.csv"
NOTEBOOKS = ROOT / "notebooks"


def load_data():
    assert CSV.is_file(), (
        f"Missing dataset: {CSV}. Put daily-min-temperatures.csv in data/."
    )
    return pd.read_csv(CSV)


def test_dataset_has_required_columns():
    df = load_data()
    assert {"Date", "Temp"}.issubset(df.columns), (
        "CSV must contain columns named Date and Temp."
    )
    assert not df.empty, "Dataset must not be empty."


def test_dates_are_valid_unique_and_sorted():
    df = load_data()
    dates = pd.to_datetime(df["Date"], errors="coerce")
    assert dates.notna().all(), "Some Date values cannot be parsed."
    assert not dates.duplicated().any(), "Duplicate dates found."
    assert dates.is_monotonic_increasing, "Dates are not in ascending order."


def test_temperatures_are_numeric():
    df = load_data()
    values = pd.to_numeric(df["Temp"], errors="coerce")
    assert values.notna().all(), "Temp has missing or nonnumeric values."



def test_daily_dates_have_no_gaps():
    df = load_data()

    dates = pd.to_datetime(df["Date"], errors="raise")
    dates = dates.sort_values().reset_index(drop=True)

    assert len(dates) > 1, "At least two observations are required."

    gaps = dates.diff()
    invalid = gaps[gaps != pd.Timedelta(days=1)].dropna()

    if not invalid.empty:
        print("\nCác ngày có khoảng cách bất thường:")

        for idx, gap in invalid.items():
            print(
                f"{dates.iloc[idx-1].date()} → "
                f"{dates.iloc[idx].date()} | "
                f"Khoảng cách: {gap}"
            )

    assert invalid.empty, (
        f"Phát hiện {len(invalid)} khoảng cách ngày bất thường."
    )



def test_notebook_exists():
    notebooks = list(NOTEBOOKS.glob("*.ipynb")) if NOTEBOOKS.exists() else []
    assert notebooks, "No .ipynb file found in notebooks/."


def test_notebook_json_is_valid():
    import json

    notebooks = list(NOTEBOOKS.glob("*.ipynb")) if NOTEBOOKS.exists() else []
    assert notebooks, "No .ipynb file found in notebooks/."
    for path in notebooks:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        assert isinstance(data.get("cells"), list), f"Invalid cells in {path.name}"
        assert data.get("nbformat") == 4, f"Unexpected notebook format: {path.name}"
