# Data Science

A collection of data analysis, forecasting and visualization notebooks that apply Python's data-science stack (pandas, NumPy, scikit-learn, TensorFlow/Keras, NLTK, matplotlib) to practical questions.

> **Credentials must be supplied by the user:** notebooks that call authenticated APIs read their keys from environment variables. See the `.env.example` file in each folder. No keys are stored in this repo.

## Structure

### `notebooks/`

> **`ml-fundamentals/` is a quick-reference section:** compact reference implementations of standard techniques on toy or built-in datasets, not original research.

| Folder | Notebooks | What they cover |
|---|---|---|
| `ml-fundamentals/` | linear & logistic regression, decision tree, random forest, gradient boosting, k-NN, SVM, PCA, t-test, pandas basics, loops | Compact reference implementations of core techniques, mostly on the Iris dataset or synthetic data |
| `signal-processing/` | `fourier-transform`, `lstm-sequence-windowing` | FFT spectrum analysis; preparing time-series windows for recurrent models |
| `nlp-vision/` | `nltk-tokenization`, `opencv-image-basics` | Text pre-processing; image loading and display in headless Jupyter |
| `nlp-social/` | `twitter-timeline-word-frequency`, `reddit-wallstreetbets-word-frequency` | Topic discovery from social-media text via token frequencies. 🔑 API credentials required |
| `data-ingestion/` | `pdf-table-extraction` | Pulling tables out of PDF reports with tabula |
| `finance-capitalstream/` | correlation matrix, ETF ratios, summary stats, trend regression, affinity-propagation market structure, LSTM-autoencoder anomaly detection, LSTM forecasting, crypto market data, crypto lending yield, FRED macro indicators | *CapitalStream Insight*, a personal investment-analytics project on public market data. 🔑 The FRED notebook needs a Nasdaq Data Link key |

Each notebook opens with a short header covering the problem, approach and data, plus attribution where it adapts a published tutorial. The finance notebooks get their risk/return metrics from the local `scripts/risk_metrics.py` module, so they run without any external course code.

### `datasets/`

Sample or public data only, never client or proprietary data:

- `synthetic/crypto-lending/`: generated lending and deposit histories used by `crypto-lending-yield.ipynb`. The values and addresses are fake.
- `sample-images/`: a generated test image for the OpenCV notebook.
- `sample-pdfs/`: a synthetic one-page report (`sample_table.pdf`) and the script that generates it, used by the PDF table-extraction notebook.

### `scripts/`

| Path | What it is |
|---|---|
| `risk_metrics.py` (+ `test_risk_metrics.py`) | Original, dependency-light module: annualised return and volatility, Sharpe ratio, max drawdown and `summary_stats()`. Used by the finance notebooks and unit-tested with pytest. |
| `cheminformatics/smiles_to_molblock.py` | SMILES → MOL block with 2-D coordinates (RDKit) |
| `ml-from-scratch/svm_from_scratch.py` | A linear SVM written from scratch in NumPy. *Adapted from sentdex, "Practical Machine Learning with Python"* |
| `ml-from-scratch/stock_price_regression.py` | Linear vs SVR price forecasting on engineered features. *Adapted from sentdex, "Practical Machine Learning with Python"* |
| `ml-from-scratch/sklearn_digits_quickstart.py` | The scikit-learn estimator API on handwritten digits. *Adapted from the scikit-learn "Introduction to machine learning" tutorial* |
| `matplotlib-basics/matplotlib_chart_types.py` | Line, bar, histogram, scatter and plot-from-file reference. *Adapted from sentdex, "Matplotlib tutorial series"* |
| `matplotlib-basics/live_graph.py` + `signal_generator.py` | A live-updating chart fed by a synthetic signal generator. *`live_graph.py` adapted from sentdex, "Matplotlib tutorial series"* |
| `matplotlib-basics/basemap_world_map.py` | Minimal world map. *Adapted from sentdex's Basemap tutorial* |
| `finance-2016/*.py` | Early price-download, charting and CSV-export scripts, ported from retired Yahoo/pandas APIs to `yfinance`. *Adapted from sentdex's Matplotlib and Pandas tutorial series* (see each file's header) |

Every tutorial-derived script names its source in an **"Adapted from:"** line in its header.

### `requirements.txt`

Python dependencies.

## Philosophy

Each notebook aims to show not just the technique but the reasoning behind it: what question is being answered, why this method, and what the result means in practice.

## Status

🚧 Under active development.
