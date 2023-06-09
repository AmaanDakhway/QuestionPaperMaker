# Question Paper Maker 📝

This Python project utilizes various libraries and tools to create a question paper maker. The project involves categorizing questions into subjects using `PhraseMatcher`, scraping questions from a website using a web scraper, cleaning the HTML code using `BeautifulSoup`, and generating question papers with different difficulty levels based on Bloom's Taxonomy. The user interface is created using `Streamlit`.

## Features

- Categorize questions into subjects using `PhraseMatcher`.
- Scrape questions from a website using a web scraper.
- Clean HTML code using `BeautifulSoup`.
- Generate question papers with easy, medium, and difficult modes based on Bloom's Taxonomy.
- User-friendly UI created with `Streamlit`.

## Technologies Used

- Python
- PhraseMatcher
- Web scraper
- BeautifulSoup
- Bloom's Taxonomy
- Streamlit

## Installation

1. Clone the repository from [https://github.com/amaandakhway1234/QuestionPaperMaker](https://github.com/amaandakhway1234/QuestionPaperMaker).
2. Install the required dependencies by running the following command:

```shell
pip install -r requirements.txt
```
## Project Structure 📁

The project directory structure is as follows:
```
QuestionPaperMaker/
  ├── app.py
  ├── question_categorizer.py
  ├── scraper.py
  ├── requirements.txt
  └── README.md
```
`webpage.py` 🌐: This file contains the Streamlit application code, which serves as the UI for the project.

`categorizer.py 📚`: This module uses the PhraseMatcher module to categorize questions into subjects.

`scraper.py 🕸️`: This module scrapes questions from a web page and cleans the HTML code using BeautifulSoup.

`requirements.txt ⚙️`: This file lists all the required dependencies for the project.

`README.md 📖`: The documentation file you are currently reading.

## Credits
This project was developed by `Amaan Dakhway`.
