# Introduction

We use this repository to experiment various methods of matrix factorization, which could be utilized in recommender system.

In this trial, we will use web data crawled from PTT(refer to [jwlin/ptt-web-crawler](https://github.com/jwlin/ptt-web-crawler)). 

Randomly crawled 5000 articles, trying to recommend the most related articles given an article.

# Methods

Different methods of contructing matrix

1. item-based - ex. build features of articles
2. collaborative filtering - ex. ratings of users toward different movies (in our case, there are 'push' and 'downvote' in PTT)

Different methods of Matrix Factorization

1. PCA
2. SVD
3. ALS


# Data

We use data from PTT Gossiping Board. There are 2000 articles represented by JSON(You can download here [https://drive.google.com/file/d/1IoYUJsH0KzJ3wbiyxO1AG-CVbY9O8yPB/view?usp=sharing](https://drive.google.com/file/d/1IoYUJsH0KzJ3wbiyxO1AG-CVbY9O8yPB/view?usp=sharing))

# Experiment

To begin, let's first take a look at test/test_case_1

We simply use tf-idf to convert each article into a vector of tf-idf. Then, we can use cosine similarity(or others ex. Jaccard Similarity) to get recommendation.

