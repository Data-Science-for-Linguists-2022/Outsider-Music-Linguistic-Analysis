# Project Plan
Emma McKibbin | LING 1340

## A Linguistic Look Inside Outsider Music
According to Wikipedia, outsider musician is a term reserved for those who create music and are self-taught, often suffering from mental illnesses or disabilities and having little technical experience.  Songs belonging to the outsider music genre are often very childlike, nonsensical, or repetitive (think of "Tiptoe Through the Tulips with Me" by Tiny Tim, or "Rock N Roll McDonalds" by Wesley Willis).

This project will look into the linguistic composition of outsider music—its lyrical variation, repetition, themes, etc.—both alone and in contrast with more popular and mainstream "insider music."  I'm interested in seeing what significant lyrical differences might distinguish outsider music from more popular genres.


### Data
The data for this study will be gathered by web-scraping, potentially by using an xml-based lyric-scrape similar to that used in Kaylin Pavlik's Billboard Hot 100 study.  I can source a list of outsider musicians from [Wikipedia](https://en.wikipedia.org/wiki/Category:Outsider_musicians) (111 musicians) or [last.fm](https://www.last.fm/tag/outsider+music/artists?page=6) (about 380 musicians).

For the comparative portion of the study, I would also need a corpus of popular music lyrics.  Pavlik's ["50 Years of Pop Music" Dataset](https://github.com/walkerkq/musiclyrics) would be sufficient for this analysis.

In an ideal world, I would be able to gather as much outsider music data as there is popular music data in Pavlik's dataset (5100 rows).  However, I doubt finding such a quantity of outsider lyrics online will be feasible.  There are a good number of popular outsider musicians (Tiny Tim, Daniel Johnston, Wesley Willis, etc.) who may be easier to find valid data for, so I may have to risk skewing the data toward the more popular artists in order to achieve a good dataset size.  I would like to shoot for a corpus size of 500 at least (~10% of the size of the comparison corpus) and 1000 at best.


### Data Cleaning
A large portion of this project will focus on data collection and cleaning.  Since the main data will be a collection of web-scraped lyrics, likely from different sources, a good amount of time will need to be put toward standardizing the lyric format, checking for anomalies that might trip up a tokenizer, etc.


### Analysis
I would like to find significant trends within the outsider music data and noticeable differences between the "insider" and outsider data (if there is a difference, of course).

Knowing that outsider music is often derived from places of suffering, I would like to see if this is reflected explicitly in the themes music or if other seemingly unrelated themes (e.g., a "Rock N Roll McDonalds"), may take precedence.

Lastly, for the pop music comparison, I hypothesize that outsider music will utilize many fewer words overall in its music, as well as heavy repetition and simpler language.

In order to analyze the distinct qualities of each over-arching genre in a computationally feasible way, I plan to create a binary classifier, which should identify the most informative features of insider and outsider music.


### Presentation
I expect to do a simple PowerPoint-style presentation at the end of the semester, potentially including a few audio/video examples of outsider songs.  I would like to use this project as an opportunity to improve my statistical and graphical skills, so I hope to include clear and accessible visualizations (word-clouds, nicely formatted and labeled bar graphs, etc.) as part of the presentation of this project.
