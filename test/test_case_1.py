import json
import numpy as np
import logging
from matricization.matricization import Matricization


def load_ptt(filename):
    try:
        with open(filename, 'r', encoding='utf8') as f:
            ftxt = f.read()
            jtxt = json.loads(ftxt)

            return jtxt["articles"]
    except Exception:
        logging.error("Error Occurs while reading {}".format(filename))


if __name__ == "__main__":
    default_format = "%(asctime)s [%(threadName)s-%(process)d] %(levelname)-5s %(module)s - %(message)s"
    logging.basicConfig(
        level=logging.DEBUG,
        format=default_format
    )
    # Please Replace to your own path
    articles = load_ptt("../data/gossiping4002.json")
    article_content = []
    for article in articles:
        article_content.append(article['content'])
    matricize = Matricization(article_content)
    mat = matricize.matrix

    target_id = 11
    sim_articles = []
    for i in range(0, mat.shape[0]):
        if i == target_id:
            continue
        cos_sim = np.dot(mat[target_id], mat[i]) / (np.linalg.norm(mat[target_id]) * np.linalg.norm(mat[i]))
        sim_articles.append((cos_sim, i))
    sim_articles = sorted(sim_articles, key=lambda k: k[0], reverse=True)
    logging.info("===   Target  Article   ===")
    logging.info("{}".format(article_content[target_id]))

    logging.info("=== Recommended Article ===")
    for (sim, id) in sim_articles[:5]:
        logging.info("{}".format(article_content[id]))
