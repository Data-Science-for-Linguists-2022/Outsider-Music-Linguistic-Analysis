# Progress Report
Emma McKibbin | LING 1340    
*A Linguistic Look Inside Outsider Music*

## Project Set-Up
#### **2/14/22:**
- **Repository created**: .gitignore, LICENSE.md, README.md, progress_report.md, project_plan.md
- README drafted
- private/ and data/ folders created on local machine (ignored by git)
- **Project Plan committed**: based on previous project ideas submission

## 1st Progress Report:
### Data Collection

#### **2/23/22:**
- **Learning BeautifulSoup**: using `beautifulsoup4` and `requests` packages to retrieve and parse HTML code.
- **Retrieved musician lists**: as a practice exercise, parsing the Wiki (111 artists). I manually edited this list, since it was manageable, to remove double quotations ("") and Wikipedia-specific parentheticals. ([wiki_musicians.py](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/wiki_musicians.py), [wikimusicians.txt](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/wikimusicians.txt))

#### **2/26/22:**
- **Got lyrics from Genius**: using John W. Miller's `lyricsgenius` package and the Genius API, I scraped lyrics from 70+ outsider musicians. ([lyricsgenius_requests.ipynb](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/lyricsgenius_requests.ipynb))
- **Created data_samples directory**: includes the [Crispin Glover JSON](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/data_samples/Lyrics_CrispinGlover.json), used as an example in [lyricsgenius_requests.ipynb](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/lyricsgenius_requests.ipynb).
- **Created a lyrics data frame**: this contains 3,338 lyrics from 63 artists and is not yet cleaned.  ([load_json_to_df.ipynb](http://localhost:8888/notebooks/Documents/DataSci/Outsider-Music-Linguistic-Analysis/load_json_to_df.ipynb))
- **Began data exploration and cleaning**: 202 lyric entries were empty strings, now NaN.  The artist distribution is also very skewed--there are hundreds of songs from a handful of artists and 1 or 2 from many artists (almost Zipfian). ([data_cleaning_and_exploration.ipynb](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/data_cleaning_and_exploration.ipynb))


### The Data Sharing Problem
Because the musician files and the pickled data frame are somewhat large and the data is fairly accessible (and fairly static in nature) through the Genius API, I have decided not to publish it but to maintain snippets of the data in presentation, as well as the Crispin Glover JSON included in `data_samples`, for reference to the JSON file structure.  I will include the manually edited list of 111 artists from Wikipedia, which will help anyone interested in the future to gather the same data as I did, through the API.
