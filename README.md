# Python for Everybody (PY4E)

My solutions to the [Python for Everybody](https://www.py4e.com/) Coursera Specialization by Dr. Charles Severance (University of Michigan).

## Repository Structure

```
PY4E/
├── 01_getting_started/       # Course 1: Programming for Everybody
├── 02_data_structures/       # Course 2: Python Data Structures
├── 03_web_data/              # Course 3: Using Python to Access Web Data
├── 04_databases/             # Course 4: Using Databases with Python
│   ├── roster/               #   └── Many-to-Many relationship project
│   └── tracks/               #   └── Music tracks database project
├── data/                     # Shared data files used across exercises
└── README.md
```

## Course 1: Programming for Everybody (Getting Started with Python)

| File | Chapter | Topic |
|------|---------|-------|
| `ex_01_hello.py` | Ch.1 — Introduction | Hello World |
| `ex_02_2_greeting.py` | Ch.2 — Variables | User greeting with input |
| `ex_02_3_pay.py` | Ch.2 — Variables | Gross pay calculation |
| `ex_03_1_overtime.py` | Ch.3 — Conditionals | Pay with overtime (`if`/`else`) |
| `ex_03_3_score.py` | Ch.3 — Conditionals | Grade calculator (`if`/`elif`/`else`) |
| `ex_04_6_computepay.py` | Ch.4 — Functions | Pay computation with functions |
| `ex_05_2_minmax.py` | Ch.5 — Loops | Find min/max with `while` loop & `try`/`except` |

## Course 2: Python Data Structures

| File | Chapter | Topic |
|------|---------|-------|
| `ex_06_5_extract.py` | Ch.6 — Strings | String slicing & `find()` |
| `ex_07_1_upper.py` | Ch.7 — Files | Read file and print in uppercase |
| `ex_07_2_spam_average.py` | Ch.7 — Files | Parse file and compute average |
| `ex_08_4_wordlist.py` | Ch.8 — Lists | Build unique word list from file |
| `ex_08_5_from_lines.py` | Ch.8 — Lists | Extract email addresses from file |
| `ex_09_4_most_prolific.py` | Ch.9 — Dictionaries | Find most prolific email sender |
| `ex_10_2_hour_distribution.py` | Ch.10 — Tuples | Email hour distribution with sorting |

## Course 3: Using Python to Access Web Data

| File | Module | Topic |
|------|--------|-------|
| `ex_11_1_answer42.py` | Regular Expressions | The Answer to Everything |
| `ex_12_1_regex_sum.py` | Regular Expressions | Find all numbers in a file with regex and sum them |
| `ex_12_2_socket.py` | Networks & Sockets | Retrieve a web page using raw sockets |
| `ex_12_3_scraping_numbers.py` | Web Scraping | Scrape numbers from HTML with BeautifulSoup |
| `ex_12_4_following_links.py` | Web Scraping | Follow links in HTML with BeautifulSoup |
| `ex_13_1_extract_xml.py` | Web Services & XML | Extract and sum data from XML |
| `ex_13_2_extract_json.py` | Web Services & JSON | Extract and sum data from JSON |
| `ex_13_3_geolocationapi.py` | Web Services & APIs | Geolocation API lookup |

## Course 4: Using Databases with Python

| File | Topic |
|------|-------|
| `ex_15_1_database.py` | Email domain counting with SQLite |
| `ex_15_2_database.py` | Music tracks database with multi-table schema |
| `roster/roster.py` | Many-to-many relationship: students ↔ courses |
| `tracks/tracks.py` | Music tracks import from CSV to normalized database |
| `tracks/old/tracks.py` | Music tracks import from iTunes XML (earlier version) |

## Data Files

The `data/` folder contains sample text files used across exercises:

| File | Description |
|------|-------------|
| `mbox-short.txt` | Short email mailbox (used in Ch.7–10 exercises) |
| `mbox.txt` | Full email mailbox (used in Ch.7–10 and database exercises) |
| `words.txt` | Sample text file (used in Ch.7) |
| `romeo.txt` | Romeo and Juliet excerpt (used in Ch.8) |

## How to Run

```bash
# Course 1 exercises (no data files needed):
python 01_getting_started/ex_01_hello.py

# Course 2 exercises (run from the data/ directory):
cd data
python ../02_data_structures/ex_07_1_upper.py
# Enter file name: words.txt

# Course 3 web exercises:
python 03_web_data/ex_12_3_scraping_numbers.py
# Enter URL: http://py4e.com/code3/comments_42.html

# Course 4 database exercises:
cd 04_databases
python ex_15_1_database.py
# Enter file name: ../data/mbox.txt
```

## Technologies Used

- **Python 3**
- **Regular Expressions** (`re`)
- **Networking** (`socket`, `urllib`)
- **Web Scraping** (`BeautifulSoup`)
- **XML/JSON Parsing** (`xml.etree.ElementTree`, `json`)
- **Databases** (`sqlite3`)

## Course Info

- **Specialization:** [Python for Everybody](https://www.py4e.com/) on Coursera
- **Instructor:** Dr. Charles Severance, University of Michigan
- **Textbook:** [Python for Everybody: Exploring Data in Python 3](https://www.py4e.com/book)
