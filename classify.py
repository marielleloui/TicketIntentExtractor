import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def visualise(data, img_path, csv_path):
    print('Data processing started.')
    
    #Reading data
    df = pd.read_json(data)
    corpus = df['problem_abstract']
    
    #tf-idf model
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_bag = tfidf_vectorizer.fit_transform(corpus)
    word_bag = tfidf_bag.toarray()
    print('tf-idf done')
    
    #Filter out low tf-idf values
    tfidf_count = word_bag.sum(axis=0)
    thresh_min = np.percentile(tfidf_count, [50,100])[0]
    thresh_max = np.percentile(tfidf_count, [50,100])[1]

    i = 0
    while i < len(word_bag[0]):
        word_bag_count = word_bag.sum(axis=0)
        count = word_bag_count[i]
        if (count < thresh_min) or (count > thresh_max):
            word_bag = np.delete(word_bag, i, 1)
        else:
            i += 1
    print('Filtering done')

    #Clustering
    num_clusters = 23
    kmeans_tfidf = KMeans(n_clusters = num_clusters).fit(tfidf_bag)
    clusters_tfidf = kmeans_tfidf.predict(tfidf_bag)
    print(clusters_tfidf)
    print('Clustering done - 23 clusters used')
    
    #Append category to dataframe
    df['tfidf_category'] = clusters_tfidf
 
    #Dimensionality reduction
    tsne_pca = PCA(n_components=50)
    tsne_pca_Comps = tsne_pca.fit_transform(tfidf_bag.toarray())
    tsne_points = TSNE(n_components=2).fit_transform(tsne_pca_Comps)
    tsneDf = pd.DataFrame(data = tsne_points, columns = ['x', 'y'])
    print('Dimensionality reduction done')

    #Plotting data points
    plt.clf()
    plt.scatter(tsneDf['x'], tsneDf['y'], c = clusters_tfidf, cmap='hsv')
    plt.savefig(img_path, format='png')
    
    #Save sorted ticket file
    df.to_csv(csv_path)
    print('Plot saved')
    return 0