# Finding similar items
The aim of this project is to detect pairs of similar tweets from the `text` field of the Kaggle [Yelp](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset) dataset.
In particular we will:
* preprocess the textual data,
* implement tools through different techniques to detect pairs of similar textual items according to various similarity measures,
* compare the results, possibly also with library versions of the implemented algorithms.

## Prerequisites
To be able to download the dataset from Kaggle it is necessary to authnticate with a Kaggle username and key. At this scope `kaggle.json` is intended to be filled out with your personal username and key in the respective fields, like suggested below.
```json
{
    "username":"<USERNAME>",
    "key":"<KEY>"
}
```