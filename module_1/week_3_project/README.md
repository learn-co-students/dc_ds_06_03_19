# Mod 1 Project Instructions


## Congratulations! 

Microsoft sees all the big companies creating original video content, and they want to get in on the fun. They have decided to create a new movie studio, but the problem is they don’t know anything about creating movies. They have hired you to help them better understand the movie industry. Your team has free range 

Therefore your team is charged with doing data analysis and creating a presentation that explores what type of films are currently doing the best at the box office. You must then translate those findings into actionable insights that the CEO can use when deciding what type of films they should be creating. 

## Methodology 
Some areas you can look to examine are movie genres (Thriller, Drama, Comedy, etc.), movie ratings, budget, social media discussion, and critic or user reviews. Your team gets to define its own questions about the movie industry and then use its knowledge of descriptive statistics and the EDA process to try and answer those questions. 

## Data Sources
Microsoft has provided some data from Box Office Mojo, IMDB, Rotten Tomatoes, and TheMovieDB.org. You are not limited to these data sets! If you find other useful data on the web, you are welcome to include it (but this is not a requirement).

All data lives in [`./data/`](./data)
- Box Office Mojo
  - data
    - bom.movie_gross.csv.gz
  - documentation
    - scraped from [this page](https://www.boxofficemojo.com/yearly/chart/?view2=worldwide&yr=2010&p=.htm) (from 2010-2018).
    - revenue has already been converted into pure dollars
- IMDB
  - data
    - imdb.name.basics.csv.gz
    - imdb.title.akas.csv.gz
    - imdb.title.basics.csv.gz
    - imdb.title.crew.csv.gz
    - imdb.title.principals.csv.gz
    - imdb.title.ratings.csv.gz
  - documentation
    - All data has come from https://www.imdb.com/interfaces/, just filtered to only 2010-2018 movies.
- Rotten Tomatoes
  - data
    - rt.movie_info.tsv.gz
    - rt.reviews.tsv.gz
  - documentation
    - this came from [Kaggle](https://www.kaggle.com/rpnuser8182/rotten-tomatoes).  All documentation can be found there.
- TheMovieDB.org
  - data
    - tmdb.movies.csv.gz
  - documentation
    - all data comes from https://developers.themoviedb.org/3/discover/movie-discover
    - Again, only 2010-2018 movies have been included.
  - data
    - tn.movie_budgets.csv.gz
  - documentation
    - This comes straight from [The-Numbers.com](https://www.the-numbers.com/movie/budgets/all)
    - this includes all data from The Numbers! it is not subset to 2010-2018
- More data!
  - if you find data you think is helpful, or if there is a data set you don't know how to access but are interested in, please feel free to ask for instructor help via Slack.

Remeber that Pandas can read gzipped data directly passed in with `pd.read_csv`.  To inspect data on command line without unzipping, you can use `gzip -cd <filename> | head` (I like to think `-cd` stands for Continuous Decompress).

## Deliverables
Your team must prepare a 5 minute presentation that gives the CEO insights as to what type of films they should be creating to meet consumer demand. Your presentation should outline the process you went through and use at least 4 meaningful data visualizations to help illustrate your findings. Your team is expected to use git as a collaborative tool for this project to manage version control and history.  No more than 8 slides.

Be prepared to answer questions such as:
- "how did you pick the question(s) that you did?"
- "why are these questions important from a business perspective?"
- "how did you decide on the data cleaning options you performed?"
- "why did you choose a given method or library?"
- "why did you select those visualizations and what did you learn from each of them?"

## Project Checklist:

 - [ ] Use data from at least two sources
   - [ ] Establish naming conventions for variables and datasets
   - [ ] Clean dataset & record parameters used to clean the data
     - [ ] You may use Pandas or Python functions
     - [ ] Document every step of the cleaning process
     - [ ] Create at least two new features that were not present in the original data sets
 - [ ] Use Pandas and Numpy to generate useful metrics for comparing films

 - [ ] Posted to git repository:
   - [ ] A README.md listing project members, goals, responsibilities, and a summary of the files in the repository
   - [ ] At least 10 commits
     - [ ] Must include short, descriptive commit messages
     - [ ] Each project member should commit at least once
   - [ ] A Jupyter notebook targeted to a technical audience that contains
     - [ ] Clean and commented code so an independent party can replicate your analysis and justify your analytical choices
     - [ ] Code should follow Pep8 standards
     - [ ] Custom functions should be stored in .py file and imported whenever possible
   - [ ] Your final joined and cleaned dataset that was used for analysis
   - [ ] A narrative Jupyter notebook targeted to a non-technical audience that provides:
     - [ ] The purpose of your analysis and why it matters
     - [ ] 4 well annotated visualizations created using Matplotlib/Seaborn
     - [ ] 2 meaningful summary tables
     - [ ] At least four actionable insights (What type of films should they be looking to produce? What should the budget requirements be? Should they recruit certain actors for their films?)
   - [ ] A pdf of no more than 8 slides used in project presentation targeting non-technical audience
     - [ ] Apply consistent and effective formatting to create a “professional” appearing deck
     - [ ] Write an abbreviated high-level overview of methodology
     - [ ] Justify at least 2 concrete recommendations 
     - [ ] include exported visualizations from analysis
     - [ ] Target the presentation to a non-technical audience, avoid jargon
     - [ ] Take no more than 5 minutes to present
 
## Specifics:
### This project is in groups
- Group A: Moussa Doumbia + Anthony Schams
- Group B: Keita Miyaki + Mindy Zhou
- Group C: Clifford Bridges + Misha Berrien
- Group D: Sean Carver + Tim Christy + Joseph McAllister
- Group E: Ngoc Tran + Dmitry Mikhaylov
- Group F: Allan Gayahan + Phoebe Wong
- Group G: TingTing Li + Nateé Johnson
- Group H: Emefa Agodo + Kate Hayes
- Group I: Quinn Dizon + Joey Goodman

### Timeline

6/14 Friday - Project Assignment 
 - schedule Monday check in with coach
 
6/17 Monday - Check in with coaches 
 - review data cleaning
 - provide url of project repository
 - review at least one table/chart
 - review work plan created for how teammates will approach and divide work
 
6/18 Tuesday - Demo presentation with feedback from instructors 
 - have polished draft of deck completed
 - have polished version of jupyter notebook completed
 
6/19 Wednesday 
 - afternoon project presentation
 - science fair open to staff and fellow students

### Project Review
If any requirements are missing or if significant gaps in understanding are uncovered, be prepared to do one or all of the following:
 - Perform additional data cleanup, visualization, and/or feature selection 
 - Submit an improved version
 - Meet again for another Project Presentation
 
What won't happen:
 - You won't be yelled at, belittled, or scolded
 - You won't be put on the spot without support
 - There's nothing you can do to instantly fail or blow it
