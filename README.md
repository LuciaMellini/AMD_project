# Finding similar items
The aim of this project is to detect pairs of similar items from the Kaggle [Letterboxd](https://www.kaggle.com/datasets/gsimonx37/letterboxd) dataset.
In particular we will:
* pre-process the data,
* implement techniques to detect pairs of similar items according to the cosine similarity measure,
* analyze the results, possibly by comparing them with a baseline.

## Contents
This repository contains two main files:
* `findingSimilarItems.ipynb` the Jupyter Notebook with all the adopted code described as necessary, runnable in the linked Google Colab environment,
* `report.tex` the $\LaTeX$ source code for the report of the project; this document goes into detail about the methods used and discusses the results.
For the rendering of the report in pdf format, refer to [release](https://github.com/LuciaMellini/AMD_project).

### Additional contents
* `data_evaluation/data_evaluation.ipynb` the code used to extract the results found in the report,
* `data_evaluation/prepare_evaluation_data.py` the script used to fetch all the data from [TMDB](https://www.themoviedb.org/) used to evaluate the results, to be run from the main directory with the following command:
```python
python data_evaluation/prepare_evaluation_data.py
```

## Prerequisites
To be able to download the dataset it is necessary to authenticate with a Kaggle username and token<sup>[1](#fn1)</sup>. At this scope the first code block in the notebook `project.ipynb` is intended to be filled out with your personal username and key in the respective fields, like suggested below.
```python
os.environ['KAGGLE_USERNAME'] = "<USERNAME>"
os.environ['KAGGLE_KEY'] = "<KEY>"
```
<a name="fn1">1</a> To create a new token go to the [settings of your Kaggle account](https://www.kaggle.com/settings) under the *API* section, and push on the dedicated button.