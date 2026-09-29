"""Generate ``sample_table.pdf``: a one-page synthetic report with a ruled data table.

Used by ``notebooks/data-ingestion/pdf-table-extraction.ipynb``. All values are
synthetic (seeded), not taken from any real report.

Run: ``python make_sample_table_pdf.py`` (``pip install reportlab``).
"""
import random
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUT = Path(__file__).resolve().parent / "sample_table.pdf"


def build() -> None:
    random.seed(42)
    rows = [["Station", "Date", "Temp (C)", "Humidity (%)", "Pressure (hPa)"]]
    for day in range(1, 13):
        for station in ("North", "South"):
            rows.append([station, f"2024-03-{day:02d}", f"{random.uniform(2, 18):.1f}",
                         f"{random.uniform(35, 90):.0f}", f"{random.uniform(990, 1030):.1f}"])

    table = Table(rows, repeatRows=1)
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
    ]))
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(OUT), pagesize=letter)
    doc.build([Paragraph("Synthetic weather-station readings (sample data)", styles["Title"]),
               Spacer(1, 12), table])
    print("wrote", OUT)


if __name__ == "__main__":
    build()
