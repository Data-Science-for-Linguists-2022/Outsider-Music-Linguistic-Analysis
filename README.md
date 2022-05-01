# Outsider-Music-Linguistic-Analysis
Emma McKibbin | ECM68@pitt.edu    
Spring 2022    

This is Emma McKibbin's term project for LING 1340: *Data Science for Linguists*.

## Project Summary:
***A Linguistic Look Inside Outsider Music***

This project aims to identify linguistic characteristics common among songs in the genre of "outsider music," made by inexperienced or self-taught artists (e.g. "Tiptoe Through the Tulips with Me" by Tiny Tim).  Are outsider lyrics as childlike, nonsensical, or repetitive as they're thought to be?  What themes or lyrical distributions might distinguish outsider music from "insider," or popular, music?

Outsider Musicians were scraped from this [Wikipedia page](https://en.wikipedia.org/wiki/Category:Outsider_musicians), lyrics were scraped from Genius.com using the [Genius API](https://docs.genius.com/), and the comparison dataset was taken from Kaylin Pavlik's ["50 Year of Pop Music"](https://github.com/walkerkq/musiclyrics) analysis.

Because of the nature of the data collection and cleaning, the dataset in its current form is very skewed in its distribution.  Therefore, the planned analysis is incomplete, and much of this project focuses on the internal trends and skews of the outsider music dataset.

## Directory:
### What's this all about?
- [`README.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/README.md) - Includes a short project summary, directory (how meta), and important links!
- [`LICENSE.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/LICENSE.md) - Specifies the license for this repository: GNU General Public License v3.0
- [`project_plan.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/project_plan.md) - The initial project plan, including expectations for the data collection, cleaning, analysis, and presentation.
- [`progress_report.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/progress_report.md) - Updates on changes to the repository, from conception to completion.
- [`presentation_4_21_22.pdf`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/presentation_4_21_22.pdf) - The project presentation slides, created while the project was in-progress.
- [`final_report.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/final_report.md) - The essay-style overview of the project's process and results.

### Scripts & Analysis
- [`0_wiki_musicians.py`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/0_wiki_musicians.py) - Script used to retrieve outsider musician names from the [Wikipedia page](https://en.wikipedia.org/wiki/Category:Outsider_musicians).
- [`0_wiki_musicians.txt`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/0_wiki_musicians.txt) - Output of the script above. Manually edited to remove double quotes.
- [`1_lyricsgenius_requests.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/1_lyricsgenius_requests.ipynb) - Retrieves lyrics in JSON format from Genius.
  -  [Click here for the nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/1_lyricsgenius_requests.ipynb)
- [`2_load_json_to_df.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/2_load_json_to_df.ipynb) - Reads the lyrics from JSON form into a pandas Data Frame.
  -  [Click here for the nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/2_load_json_to_df.ipynb)
- [`3_data_cleaning_and_exploration.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/3_data_cleaning_and_exploration.ipynb) - Looking at basic statistics of the Data Frame and cleaning the lyric data.
  -  [Click here for the nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/3_data_cleaning_and_exploration.ipynb)

### Data Samples
- Folder containing small snippets of the scraped data. I've refrained from publishing multiple samples so as not to violate any lyrics site copyrights.
- [`Lyrics_CripsinGlover.json`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/data_samples/Lyrics_CrispinGlover.json) - Example JSON of lyrics scraped from Genius.

### Images
- Folder containing saved images of graphs produced during .ipynb analysis, to be included in final presentation

## Guestbook:
My [guestbook](https://github.com/Data-Science-for-Linguists-2022/Class-Lounge/blob/main/guestbooks/guestbook_emma.md) is where classmates leave comments, questions, and suggestions about this repository!
