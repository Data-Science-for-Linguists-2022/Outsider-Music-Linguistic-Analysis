# Progress Report
Emma McKibbin | LING 1340    
*A Linguistic Look Inside Outsider Music*

**Contents:**
- [Set-Up](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/progress_report.md#project-set-up)
- [Progress Report 1](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/progress_report.md#1st-progress-report)
- [Progress Report 2](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/progress_report.md#2nd-progress-report)
- Progress Report 3()


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
- **Retrieved musician lists**: as a practice exercise, parsing the Wiki (111 artists). I manually edited this list, since it was manageable, to remove double quotations ("") and Wikipedia-specific parentheticals. ([wiki_musicians.py](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/0_wiki_musicians.py), [wikimusicians.txt](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/0_wiki_musicians.txt))

#### **2/26/22:**
- **Got lyrics from Genius**: using John W. Miller's `lyricsgenius` package and the Genius API, I scraped lyrics from 70+ outsider musicians. ([lyricsgenius_requests.ipynb](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/1_lyricsgenius_requests.ipynb))
- **Created data_samples directory**: includes the [Crispin Glover JSON](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/data_samples/Lyrics_CrispinGlover.json), used as an example in [lyricsgenius_requests.ipynb](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/1_lyricsgenius_requests.ipynb).
- **Created a lyrics data frame**: this contains 3,338 lyrics from 63 artists and is not yet cleaned.  ([load_json_to_df.ipynb](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/2_load_json_to_df.ipynb))
- **Began data exploration and cleaning**: 202 lyric entries were empty strings, now NaN.  The artist distribution is also very skewed--there are hundreds of songs from a handful of artists and 1 or 2 from many artists (almost Zipfian). ([data_cleaning_and_exploration.ipynb](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/3_data_cleaning_and_exploration.ipynb))


### The Data Sharing Problem
Because the musician files and the pickled data frame are somewhat large and the data is fairly accessible (and fairly static in nature) through the Genius API, I have decided not to publish it but to maintain snippets of the data in presentation, as well as the Crispin Glover JSON included in `data_samples`, for reference to the JSON file structure.  I will include the manually edited list of 111 artists from Wikipedia, which will help anyone interested in the future to gather the same data as I did, through the API.

## 2nd Progress Report:
### Data Cleaning

#### **3/24/22:**
- **Reorganized Repository:** Created the `scripts_&_analysis` folder to contain all of my collection, cleaning, and analysis scripts.
- **Updated README:** Added a directory to the [README.md](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/README.md).
  - NOTE: The scripts and analysis links are broken (unlinked) at the moment and will **need updated** after I push changes to the repository.
  - I have also not un-deaded the two links that Sean and Caroline noticed.  I will fix these after this report submission!

#### **3/25/22:**
**NOTE:** Changes for data cleaning and initial analysis (Progress Report 2) are located in the `3_data_cleaning_and_exploration.ipynb` file, initially created for Progress Report 1.  When I reach the outsider-insider music comparison, that task will likely be stored in a separate notebook.
- **Finished Cleaning Data:** Fixed formatting issues present in the lyric data.  Identified issues with non-empty strings that were not lyrics ("Embed", "Transcription in progess...", etc.).
- Tried to identify non-English lyrics, but it proved too difficult, since some English songs included non-English characters.  It was useful in recognizing formatting issues that I had not anticipated.
- **Started Token Analysis:** Created the `tokens`, `token_ct`, `type_ct`, and `TTR` columns for analysis.  Quickly checked the distribution of `token_ct` over the data.


### Found Data Sharing Scheme
In order to avoid infringing upon Genius's copyright on lyrics, I will keep a majority of my data unpublished.  I have shared the [`Lyrics_CrispinGlover.json`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/data_samples/Lyrics_CrispinGlover.json) as an example of the file structure returned from `1_lyricsgenius_requests.ipynb`.  I have avoided flashing large portions of the lyric data frame in my notebooks, and since little productive work could be done on a small (5-item) sample data frame, it doesn't seem worth it to include it as a data sample.  In the process of data cleaning, I have flashed entire lyric texts -- I think it's somewhat necessary to see the formatting issues that I was encountering and needed to change.  There are only a few example texts flashed.

### Repository License
I've chosen the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/) for my repository.  I would like any code I've written that may be useful for someone else's work to remain publicly available so that, in the case that the user adjusts the code and makes improvements, lyrical analysis may become more streamlined and accessible.

This license allows for commercial use, distribution, modification, and patent and private use, and it requires the derivative work to disclose the source, include a license and copyright notice, publish under the same license, and state changes to the original code.

## 3rd Progress Report:
#### **4/11/2022**
- **Added guestbook to README**

### Language Detection
In the feedback from the last Progress Report, Sean mentioned using a % of non-English characters to filter out non-English songs, as opposed to a binary "contains" or "does not contain."  I tried this out, but it seems that the method I was using deems certain punctuation as non-English characters, meaning lyrics with a lot of punctuation that might fall under that category will be falsely marked as non-English.  It was also difficult to find a cutoff percentage that would correctly split the English from the mostly non-English lyrics.

Instead, I decided to try out spaCy's `langdetect` library, which could, at the very least, more reliably identify English lyrics.  This was at the expense of losing some English lyric data, as shown in `3_data_cleaning_and_exploration`, where a cover of "Deck the Halls" was identified as Spanish language data, due to the high frequency of "la".  After visually analyzing the lyrics that were identified as non-English languages, I discovered that many English or non-sense lyrics were misidentified.

Because of this misclassification, I can definitively remove only Swedish and Japanese lyrics.  I will leave the other non-English data in for now, in the hopes that it is in a small enough quantity that it won't confound the analysis.  If it appears that this is not the case and the analysis may be compromised, I will resort to using only the data identified as English ('en'), but I would like to avoid this, since it will eliminate some of the non-sense or idiosyncratic lyrics that could help characterize outsider music.

*I felt that removing the Japanese data, at least, was important, given that the script is in characters, meaning that it won't be counted and analyzed the same way as an alphabetical orthographic system.*

#### **4/12/2022**
- **Used spaCy LanguageDetector** to identify the languages of each song's lyrics.  Once again, not a totally definitive solution, but it could be helpful down the line if it appears that non-English data is confounding the analysis.  At this point, this step seems like a bit of a time-waste, but I'm glad I got to at least get familiar with spaCy.
- **Basic Outsider Music Analysis**: Looked into the artist distribution, duplicates, song length, and the most common words (with and without stopwords & punctuation).
- I'm noticing more issues with the data cleaning, but it appears it will never be completely done without a lot of manual selection.  In the interesting of time and consistency, I will try to ignore most issues from here on out (looking most specifically at "Needs to be Transcribed" on that particular Viper song).

#### **4/13/2022**
- **Fixed duplicate lyrics**: I noticed that certain songs were duplicates of the songs directly before them in the data frame, and when I went to investigate on Genius, I found that these duplicates should actually be empty strings.  Somehow, replacing empty strings ("") with `None` caused it to duplicate the lyrics above.  After some troubleshooting, I resolved this issue by *not* replacing empty strings with None and later excluding the empty strings themselves.
- **Imported Pavlik's Billboard Hot 100 Corpus**: ["50 Years of Pop Music"](https://www.kaylinpavlik.com/50-years-of-pop-music/) 
  - Cleaned data to remove missing lyrics & instrumentals.
  - Investigated possible issues, including mistakenly concatenated words (likely cause by removing newlines, rather than replacing, as discussed in class).
  - Tokenized lyrics & created `tokens`, `token_ct`, `type_ct`, and `TTR` columns.
  - Ran comparable statistics: looked at token count distribution and artist distribution, as well as most common words (including and excluding stopwords).
      - Other things to analyze could be: Type-Token Ratio comparison among equally sized lyric sets (~150 tokens, since both means are ~200-300 tokens)
      - Google kband analysis
  - Found issues with the formatting that may be necessary to conform to in my own collected data (e.g., no apostrophes or punctuation).  If I am to run a Naive Bayes classifier on this data, ideally, the most informative features shouldn't be punctuation!
- **Saved Graph Images**: Pie charts & box-and-whisker plots to show the two distributions (artist and token count) visualized in each dataset
- Given enough time, I might do a short analysis of Wesley Willis vs. the rest of the Outsider Music Dataset, just to get a grasp on what characteristics of the data found in the analysis may be attributable to a skew toward Willis's works.
- I've also tried to maintain the full datasets (including rows with null lyrics) in `...df_orig` objects so that, if time permits (which it unfortunately may not), I can do some analysis on song titles as well. 
