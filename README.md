# Outsider-Music-Linguistic-Analysis
This is Emma McKibbin's term project for LING 1340: *Data Science for Linguists*.

## Project Summary:
***A Linguistic Look Inside Outsider Music***

This project aims to identify linguistic characteristics common among songs in the genre of "outsider music," made by inexperienced or self-taught artists (e.g. "Tiptoe Through the Tulips with Me" by Tiny Tim).  Are outsider lyrics as childlike, nonsensical, or repetitive as they're thought to be?  What themes or lyrical distributions might distinguish outsider music from "insider," or popular, music?

## Directory:
### What's this all about?
- [`README.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/README.md) - Includes a short project summary, directory (how meta), and important links!
- [`LICENSE.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/LICENSE.md) - Specifies the license for this repository:
- [`project_plan.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/project_plan.md) - The initial project plan, including expectations for the data collection, cleaning, analysis, and presentation.
- [`progress_report.md`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/progress_report.md) - Updates on changes to the repository, from conception to completion.

### Scripts & Analysis
- [`0_wiki_musicians.py`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/0_wiki_musicians.py) - Script used to retrieve outsider musician names from the [Wikipedia page](https://en.wikipedia.org/wiki/Category:Outsider_musicians).
- [`0_wiki_musicians.txt`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/0_wiki_musicians.txt) - Output of the script above. Manually edited to remove double quotes.
- [`1_lyricsgenius_requests.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/1_lyricsgenius_requests.ipynb) - Retrieves lyrics in JSON format from Genius.
- [`2_load_json_to_df.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/2_load_json_to_df.ipynb) - Reads the lyrics from JSON form into a pandas Data Frame.
- [`3_data_cleaning_and_exploration.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/scripts_%26_analysis/3_data_cleaning_and_exploration.ipynb) - Looking at basic statistics of the Data Frame and cleaning the lyric data.

### Data Samples
- Folder containing small snippets of the scraped data. I've refrained from publishing multiple samples so as not to violate any lyrics site copyrights.
- [`Lyrics_CripsinGlover.json`](https://github.com/Data-Science-for-Linguists-2022/Outsider-Music-Linguistic-Analysis/blob/main/data_samples/Lyrics_CrispinGlover.json) - Example JSON of lyrics scraped from Genius.

### Images
- Folder containing saved images of graphs produced during .ipynb analysis, to be included in final presentation
