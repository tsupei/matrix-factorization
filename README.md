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

