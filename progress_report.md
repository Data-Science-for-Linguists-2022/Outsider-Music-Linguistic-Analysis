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
