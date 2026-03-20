# Python for Everybody (PY4E) - Exercises

My solutions to the [Python for Everybody](https://www.py4e.com/) Coursera Specialization by Dr. Charles Severance (University of Michigan).

## Course 1: Programming for Everybody (Getting Started with Python)

| File | Chapter | Topic |
|------|---------|-------|
| `ex_01_hello.py` | 1 - Introduction | Hello World |
| `ex_02_2_greeting.py` | 2 - Variables | User greeting with input |
| `ex_02_3_pay.py` | 2 - Variables | Gross pay calculation |
| `ex_03_1_overtime.py` | 3 - Conditionals | Pay with overtime (if/else) |
| `ex_03_3_score.py` | 3 - Conditionals | Grade calculator (if/elif/else) |
| `ex_04_6_computepay.py` | 4 - Functions | Pay computation with functions |
| `ex_05_2_minmax.py` | 5 - Loops | Find min/max with while loop & try/except |

## Course 2: Python Data Structures

| File | Chapter | Topic |
|------|---------|-------|
| `ex_06_5_extract.py` | 6 - Strings | String slicing & find() |
| `ex_07_1_upper.py` | 7 - Files | Read file and print in uppercase |
| `ex_07_2_spam_average.py` | 7 - Files | Parse file and compute average |
| `ex_08_4_wordlist.py` | 8 - Lists | Build unique word list from file |
| `ex_08_5_from_lines.py` | 8 - Lists | Extract email addresses from file |
| `ex_09_4_most_prolific.py` | 9 - Dictionaries | Find most prolific email sender |
| `ex_10_2_hour_distribution.py` | 10 - Tuples | Email hour distribution with sorting |

## Course 3: Using Python to Access Web Data

| File | Module | Topic |
|------|--------|-------|
| `ex_11_1_answer42.py` | 1 - Regular Expressions | The Answer to Everything |
| `ex_12_1_regex_sum.py` | 1 - Regular Expressions | Find all numbers in a file with regex and sum them |
| `ex_12_2_socket.py` | 3 - Networks & Sockets | Retrieve a web page using raw sockets |
| `ex_12_3_scraping_numbers.py` | 4 - Scraping the Web | Scrape numbers from HTML with BeautifulSoup |
| `ex_12_4_following_links.py` | 4 - Scraping the Web | Follow links in HTML with BeautifulSoup |
| `ex_13_1_extract_xml.py` | 5 - Web Services & XML | Extract and sum data from XML |

## Data Files

The `data/` folder contains sample text files used by the exercises:

- `mbox-short.txt` — Short email mailbox (used in ch7-10 exercises)
- `mbox.txt` — Full email mailbox
- `words.txt` — Sample text file (used in ch7)
- `romeo.txt` — Romeo and Juliet excerpt (used in ch8)

## How to Run

```bash
# For file-based exercises:
cd data
python ../ex_07_1_upper.py
# Enter file name: words.txt

# For web-based exercises (course 3):
python ex_12_3_scraping_numbers.py
# Enter URL: http://py4e.com/code3/comments_42.html
```

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- Sockets (`socket`)
- Web scraping (`urllib`, `BeautifulSoup`)
- XML parsing (`xml.etree.ElementTree`)

## Course Info

- **Specialization:** [Python for Everybody](https://www.py4e.com/) (Coursera)
- **Instructor:** Dr. Charles Severance, University of Michigan
- **Textbook:** [Python for Everybody: Exploring Data in Python 3](https://www.py4e.com/book)
