# Reading headphone trends using Reddit postings
---

## Table of Contents
- [1 Directory Structure](#1-Directory-Structure)<br>
- [2 Project Outline / Problem Statement](#2-Project-Outline-/-Problem-Statement)<br>
- [3 Description of Data](#3-Description-of-Data)<br>
 -[Size](#Size)<br>
 -[Data Dictionary](#Data-Dictionary)<br>
- [4 Data Visualization](#4-Data-Visualization)<br>
- [5 Conclusion](#5-Conclusion)<br>
- [6 Next Steps](#6-Next-Steps)<br>
- [7 Outside Sources](#7-Outside-Sources)<br>


---
## 1 Directory Structure

```
├── nlp_headphone
    ├── code
        ├── scraping_reddit.ipynb
        ├── EDA.ipynb
        ├── LDA.ipynb
        ├── ldavis_prepared_20.html
    ├── data
        ├── HeadphoneAdvice.csv
        ├── HeadphoneAdvice_cmt.csv
        ├── headphones.csv
        ├── headphones_cmt.csv
    └── README.md
```
---
## 2 Project Outline / Problem Statement

Reading trends is important for most companies. Can we read trends by analysing Reddit postings which we casually come across? Here comes the answer. By NLP(Natural Language Processing) using the LDA(Latent Dirichlet Allocation) library in Python, I could find trends and product insights based on reddit posts of headphones.

---
## 3 Description of Data

### Size
- 209 MB

### Data Dictionary
|Dataset|Feature|Type|Description|
|---|---|---|---|
|HeadphoneAdvice.csv, HeadphoneAdvice_cmt.csv, headphones.csv, headphones_cmt.csv | subreddit | object | name of subreddit |
|HeadphoneAdvice.csv, HeadphoneAdvice_cmt.csv, headphones.csv, headphones_cmt.csv | created_utc | int64 | created time |
|HeadphoneAdvice.csv, HeadphoneAdvice_cmt.csv, headphones.csv, headphones_cmt.csv | body | object | contents of reddit postings |
|HeadphoneAdvice.csv, HeadphoneAdvice_cmt.csv, headphones.csv, headphones_cmt.csv | score | int64 | score of postings or comments |

---

## 4 Data Visualization
<img src="./img/lda.png">

---
## 5 Conclusion
<img src="./img/executive_summary.jpg">

---
### 6 Next Steps

- Sales data, consumer behavior research, specifications of products and so on will lead me to deeper analysis and insights.

---
## 7 Outside Sources

- https://www.reddit.com/r/headphones/
- https://www.reddit.com/r/HeadphoneAdvice/


```

```
