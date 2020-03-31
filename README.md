
# Welcome Chicago DS 14!

:wave:

---

| ![Metis logo](/curriculum/project-01/day-1-materials/metis.png)      |  [Metis](http://www.thisismetis.com/) Data Science Bootcamp    |
|------|-------|  

---
| **Course ID**     |  chi20_ds14    |
|:------|:-------|
| **Section**   | Spring 2020 - Cohort 14  |  
| **City**  | Chicago |
| **Dates** | 30-March-2020 to 19-June-2020   |
| **Slack** |  [ds14 team](https://Spring-chi20-metis.slack.com/) (use the [app](https://slack.com/downloads)) |
| **Senior Data Scientists** |  [Lara Kattan](https://www.linkedin.com/in/lara-kattan), [Omar Singleton](https://www.linkedin.com/in/omarsingleton), [Alice Zhao](https://www.linkedin.com/in/alicexzhao) |

### Quick Links:
* [Pair Partners](https://drive.google.com/open?id=1rR_9mElpSFDZB08H9Mxg-tItiVWViZK0VzWerXVw_Dc)

* [Investigation Signup](https://drive.google.com/open?id=1TCC-MDjE11ULQAeBmGAMWw9X_bZbWwab1dXhjadAwA8)
* [Blog Submission](https://drive.google.com/open?id=1PrIeARJY8XNYQqyq2dRKsVRuFIul3w8HyFasoIGMIa0)

### Metis Conda Environment

<details><summary> Installing the environment for the first time (click to expand)</summary> 

# Environment management

We will be using Anaconda environments to manage the python packages that are
needed for our curriculum. You can think of an environment as a container for
the packages that you need to run code.

Environments can be useful when you have several different projects, each with
different software requirements. Environments let you separately the packages
used for each package and preserve them so that the project code will continue
to work in the future.

Today, we'll start by building our very first conda environment. Metis has a
list of the software needed to run all the code in our curriculum. We keep track
of this in the cloud, allowing you to easily get up and running.

## Setup

### Conda

First, you need to have anaconda installed in order for this to work. Check that
`conda` is installed by running `conda -V` from your terminal. You should
receive a response indicating your current `conda` version.

If you haven't already, install the appropriate miniconda for your system from
the link [here](https://docs.conda.io/en/latest/miniconda.html). **Be sure to
select the python 3.\* version**.

### Metis Environment

Now we'll run the code to install the metis environment.

First, let's check if `conda` needs to be updated:

```bash
conda update conda -y
```

Next, we need to install `anaconda-client` in order to load cloud environmentts.

```bash
conda install anaconda-client -y
```

Finally, install the Metis environment:

```bash
conda env create thisismetis/metis
```

The `nb_conda` package will automatically connect your conda environment to
jupytyer.

# How to use the Metis environment

When you open a new terminal, you should see a prompt similar to:

```bash
(base)$
```

This indicates that you are currently in the "base" environment. You can confirm
this with `conda info`.

## Switch to the Metis environment

**Before you can run Jupyter, you need to switch to the Metis environment.** You
can do this by running

```bash
(base)$ conda activate metis
(metis)$
```

You can then start Jupyter by running

```bash
(metis)$ jupyter notebook
```

When starting a new notebook in Jupyter, students should select "Kernel ->
Change Kernel -> metis" before running.

</details>

<details><summary>Updating the environment (click to expand)</summary> 
You can update your metis environment any time by running

```bash
conda env update thisismetis/metis
```
</details>



# Daily Schedule

<table>
 <tr>
  <th>
  </th>
  <th>
   Monday
  </th>
  <th>
   Tuesday
  </th>
  <th>
   Wednesday
  </th>
  <th>
   Thursday
  </th>
  <th>
   Friday
  </th>
 </tr>
 <tr>
  <th>
   Week 1
  </th>
  <td>
   Total: 145m
   <br/>
   <a href="pairs/fizzbuzz">
    • Pair: fizzbuzz
   </a>
   <small>
    (60m)
   </small>
   <br/>
   <hr align="left" width="50%"/>
   <a href="/curriculum/project-01/day-1-materials">
    • Day 1 Materials
   </a>
   <small>
    (20m)
   </small>
   <br/>
   <a href="/curriculum/project-01/git-1">
    • Git Intro
   </a>
   <small>
    (60m)
   </small>
   <br/>
   <a href="/curriculum/project-01/pandas-revisited">
    • Pandas Revisited
   </a>
   <small>
    (45m)
   </small>
   <br/>
   <a href="/curriculum/project-01/project-01-introduction">
    • Project 1 Introduction
   </a>
   <small>
    (20m)
   </small>
   <br/>
   <a href="/curriculum/project-01/review">
    • Optional Review
   </a>
   <small>
    (0m)
   </small>
   <br/>
  </td>
  <td>
   Total: 150m
   <br/>
   <a href="pairs/alphabets">
    • Pair: alphabets
   </a>
   <small>
    (60m)
   </small>
   <br/>
   <hr align="left" width="50%"/>
   <a href="/curriculum/project-01/git-2">
    • Git Branches
   </a>
   <small>
    (30m)
   </small>
   <br/>
   <a href="/curriculum/project-01/design">
    • Project Design
   </a>
   <small>
    (30m)
   </small>
   <br/>
   <a href="/curriculum/project-01/matplotlib">
    • Matplotlib
   </a>
   <small>
    (90m)
   </small>
   <br/>
  </td>
  <td>
   Total: 150m
   <br/>
   • Pair: guessnum
   <small>
    (60m)
   </small>
   <br/>
   • Seaborn
   <small>
    (30m)
   </small>
   <br/>
   • Presentation Guide
   <small>
    (60m)
   </small>
   <br/>
   • MTA Challenge Solutions
   <small>
    (60m)
   </small>
   <br/>
  </td>
  <td>
   Total: 75m
   <br/>
   • Pair: prime
   <small>
    (60m)
   </small>
   <br/>
   • Numpy
   <small>
    (30m)
   </small>
   <br/>
   • Code Style
   <small>
    (45m)
   </small>
   <br/>
  </td>
  <td>
   Total: 60m
   <br/>
   • Project 1 Presentation
   <small>
    (0m)
   </small>
   <br/>
   • Blog
   <small>
    (60m)
   </small>
   <br/>
  </td>
 </tr>
</table>
<br>

# Deliverables

### <a name="section-b"></a>[Projects](/projects)

* Presentation slides, in **PDF** format, should be submitted (via pull request) to the course repo, under [student_submissions/projects](/student_submissions/projects) folder
* All code should also be submitted to the same folder (do not include your data files as they'll be too big)

|    |Project | Week | Topics                 |  Due |
|----|----|-------|-------|----------|
| 1  | Exploratory Data Analysis (EDA)  | 1 | [MTA turnstile](/curriculum/project-01/project-01-introduction/project_01.md) | Week 1, Friday  |
| 2  | Regression  | 2, 3|  [Movies, webscraping, regression](/curriculum/project-02/project-02-introduction/project_02.md)  | Week 3, Friday |
| 3  | Classification | 4, 5, 6|  [Supervised, D3](/curriculum/project-03/project-03-introduction/project_03.md)        | Week 6, Wednesday |
| 4  | Unsupervised Learning & NLP | 6, 7, 8|  [Unsupervised, NLP](/curriculum/project-04/project-04-introduction/project_04.md) | Week 8, Friday  |
| 5  | Passion Project | 9, 10, 11, 12| Passion Project | Week 12, Monday |

---

### <a name="section-c"></a>[Challenges](/challenges)
 
* [Instructions](/challenges/README.md)
* [Questions](/challenges/challenges_questions)
* [Data](challenges/challenges_data)
* [student_submissions/challenges](/student_submissions/challenges)

**Note:**
* **Review the [Instructions](/challenges/README.md) before submitting!**
* Students are permitted and encouraged to work with other students on the challenge sets
* Students should submit challenges individually (not by group); include names of people you worked with in header
* OK to submit partial work, full set is encouraged but not required
* Students should submit whatever they have completed by due date; can update and resubmit challenge sets at a later date 
* No grades are assigned; focus is on learning the topics


| Challenge Set  | Project Group | Topic                 | Note * | Date Assigned   | Date Due      |
|----------------|---------------|-----------------------|---------------|------------|-------------|
| 1              | EDA        | [Explore MTA data](/challenges/challenges_questions/01-mta)      | required     | Week 1, Monday | Week 2, Monday  |
| 2              | EDA        | [Math Primer](/challenges/challenges_questions/02-primer)      | required     | Week 1, Monday | Week 2, Monday  |
| 3              | EDA        | [Pandas movies](/challenges/challenges_questions/03-pandas)                | required    | Week 2, Monday  |  Week 3, Monday   |
| 4              | EDA        | [Probability](/challenges/challenges_questions/04-probability)                | required    | Week 2, Monday | Week 3, Monday |
| 5              | Regression        | [Linear Splitting](/challenges/challenges_questions/05-linear_splitting)      | required    | Week 3, Monday | Week 4, Monday   |
| 6              | Regression        | [Linear Learning](/challenges/challenges_questions/06-linear_learning)       | required    | Week 3, Monday | Week 4, Monday |
| 7              | Classification       | [Classification](/challenges/challenges_questions/07-classification)        | required    | Week 4, Monday |   Week 5, Monday |
| 8              | Classification       | [Classification Errors](/challenges/challenges_questions/08-classification_errors) | required    | Week 4, Monday | Week 5, Monday |
| 9              | Classification       | [SQL](/challenges/challenges_questions/09-sql)                   | parts [i](/challenges/challenges_questions/09-sql/09_part_i_sql_w3school.md), [ii](/challenges/challenges_questions/09-sql/09_part_ii_sql_baseball.md), [iii](/challenges/challenges_questions/09-sql/09_part_iii_sql_soccer.md) required (part [iv](/challenges/challenges_questions/09-sql/09_part_iv_sql_tennis.md) is optional)    | Week 5, Monday | Week 6, Monday |
| 10             | Classification       | [Decision Tree](/challenges/challenges_questions/10-decision_tree)         |  recommended    | Week 5, Monday  | Week 6, Monday |
| 11             | Classification       | [Poisson GLM](/challenges/challenges_questions/11-poisson_glm)           | recommended     | Week 6, Monday |  Week 7, Monday    |
| 12             | Classification       | [D3](/challenges/challenges_questions/12-d3)                    | recommended    | Week 6, Monday | Week 7, Monday   |
| 13             | NLP & Unsupervised      | [Flask](/challenges/challenges_questions/13-flask)                 | recommended    | Week 7, Monday  | Week 8, Monday  |
| 14             | NLP & Unsupervised      | [Mongo Twitter](/challenges/challenges_questions/14-mongo_twitter)         | recommended    | Week 7, Monday | Week 8, Monday  |
| 15             | NLP & Unsupervised      | [NLP Unsupervised](/challenges/challenges_questions/15-nlp_unsup)      | recommended    | Week 8, Monday | Week 9, Monday  |
| 16             | Passion Project         | [Hadoop](/challenges/challenges_questions/16-hadoop)                | recommended    | Week 8, Monday | Week 9, Monday |
| 17             | Passion Project         | [Hive](/challenges/challenges_questions/17-hive)                  | recommended    | Week 9, Monday | Week 10, Monday |

*Full submission of challenge sets is encouraged, but partial submissions are ok. 

---

### <a name="section-f"></a>[Investigations (~ 10 minutes long)](/investigations)

* Required:  1 presentation
* [Investigation Signup Link](https://drive.google.com/open?id=1TCC-MDjE11ULQAeBmGAMWw9X_bZbWwab1dXhjadAwA8) 
* After investigation presentation, a pdf copy should be submitted (via pull request) to the course repo, under [student_submissions/investigations](/student_submissions/investigations) folder

---

### <a name="section-d"></a>Blogs
 
* Required:  2 blogs
* Recommended:  5+ blogs
* Blog [Link](https://drive.google.com/open?id=1PrIeARJY8XNYQqyq2dRKsVRuFIul3w8HyFasoIGMIa0) 

| Blog | Topic | Note* | Due |  
|------|-------|-------|-----|
| 1    | ds / project 1 | required | EOD Presentation Day |   
| 2    | project 2 | required |  Mon after presentations  |  
| 3    | project 3 | recommended |  Mon after presentations |
| 4    | project 4 | recommended | Mon after presentations |
| 5    | project 5 final | recommended* | Mon after presentations |  
*Blog 5 date is after the bootcamp graduation 

---

### <a name="section-e"></a>Assessments
 
* There will be 2 Quizzes given (dates below).  The quizzes will be take homes.

| Quiz | Topics | Note* | Date |  
|------|-------|-------|-----|
| 1    | Weeks 1-2 | optional | Fri, Week 2 |   
| 2    | Weeks 3-4 | optional | Fri, Week 4 |  


