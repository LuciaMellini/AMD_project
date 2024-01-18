# Finding similar items
The aim of this project is to detect pairs of similar tweets from the `text` field of the Kaggle [Yelp](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset) dataset.
In particular we will:
* preprocess the textual data,
* implement tools through different techniques to detect pairs of similar textual items according to various similarity measures,
* compare the results, possibly also with library versions of the implemented algorithms.

## Prerequisites
To be able to download the dataset it is necessary to authenticate with a Kaggle username and token<sup>[1](#fn1)</sup>. At this scope the first code block in the notebook `project.ipynb` is intended to be filled out with your personal username and key in the respective fields, like suggested below.
```python
    os.environ['KAGGLE_USERNAME'] = "<USERNAME>"
    os.environ['KAGGLE_KEY'] = "<KEY>"
```
<a name="fn1">1</a> To create a new token go to the [settings of your Kaggle account](https://www.kaggle.com/settings) under the *API* section, and push on the dedicated button.