import numpy as np
import re
import logging
import math


class Matricization(object):
    def __init__(self, articles):
        articles = self.__preprocess(articles)
        self.matrix = self.__matricize(articles)

    def __preprocess(self, articles):
        # RE
        logging.info("Filtering non-chinese characters...")
        re_keep_zh = re.compile(r'[^\u4e00-\u9fff]+')
        articles = [re.sub(re_keep_zh, '', article) for article in articles]
        logging.debug(articles[0])
        return articles

    def __matricize(self, articles):
        counter = {}
        for article in articles:
            for char in article:
                counter.setdefault(char, 0)
                counter[char] += 1
        char_lookup = list(counter.keys())
        char_dict = {}
        idf = {}
        for cidx, char in enumerate(char_lookup):
            char_dict[char] = cidx
            idf[char] = 0

        logging.info("Calculating idf...")

        for article in articles:
            for key in idf.keys():
                if key in article:
                    idf[key] += 1
        for key in idf.keys():
            idf[key] = math.log10(len(articles)/idf[key])

        logging.debug("IDF:")
        logging.debug("{}".format(idf))

        tfidf = []
        for article in articles:
            counter = {}
            for char in article:
                counter.setdefault(char, 0)
                counter[char] += 1
            total = sum(counter.values())
            for key, value in counter.items():
                counter[key] = (value / total) * idf[key]
            tfidf.append(counter)

        # The shape of our matrix is len(articles) * len(char_lookup)
        logging.info("The shape of matrix: {} x {}".format(len(articles), len(char_lookup)))
        mat = np.zeros([len(articles), len(char_lookup)])

        for article_idx, article in enumerate(articles):
            for char in article:
                mat[article_idx][char_dict[char]] = tfidf[article_idx][char]
        return mat

















