from email.policy import default
import numpy as np 
from gensim.models.fasttext import FastText
from gensim.models.word2vec import Word2Vec
from progressbar import progressbar
from tqdm import tqdm
import io
import os
from urllib import request



'''logging.basicConfig(
    filename=os.path.join("fasttext_logs", ''), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )'''

class Word2Vec_vectorize:
    def __init__(self, df, column, model_name, vector_size, window_size, min_count, workers, negative, iter):
        self.df = df
        self.column = column
        self.model_name = model_name
        self.vector_size = vector_size
        self.window_size = window_size
        self.min_count = min_count
        self.workers = workers
        self.negative = negative
        self.iter = iter

    def train(self):
        model = Word2Vec(self.df[self.column], size=self.vector_size, window=self.window_size, min_count=self.min_count, workers=self.workers, negative=self.negative, iter=self.iter)
        model.save(self.model_name)
        # logging.info("trained word to vector")
        return model


class FastText_vectorize:

    DEFAULT_MODELS_DIR = os.path.join(
        os.path.expanduser("~"), ".cache", "nandini", "models"
    )
    MODELS = {
        "wiki_300dimension_word.vec.zip": "https://dl.fbaipublicfiles.com/"
        "fasttext/vectors-english/wiki-news-300d-1M.vec.zip",
        "wiki_300dimension_sub_word.vec.zip": "https://dl.fbaipublicfiles.com/"
        "fasttext/vectors-english/wiki-news-300d-1M-subword.vec.zip",
        "crawl_300dimension_word.vec.zip": "https://dl.fbaipublicfiles.com/"
        "fasttext/vectors-english/crawl-300d-2M.vec.zip",
        "crawl_300dimension_sub_word.vec.zip": "https://dl.fbaipublicfiles.com/"
        "fasttext/vectors-english/crawl-300d-2M-subword.zip",
    }


    def __init__(self,file_path : str = None) -> None:
        self.file_path = self.download_models(specific_models="wiki_300dimension_word.vec.zip")
        self.dimension = 300
        self.data = {}
        pass

    def download_models(self, specific_models=None):
        os.makedirs(self.DEFAULT_MODELS_DIR, exist_ok=True)

        def show_progress(block_num, block_size, total_size):
            global pbar
            if pbar is None:
                pbar = progressbar.ProgressBar(maxval=total_size)
                pbar.start()

            downloaded = block_num * block_size
            if downloaded < total_size:
                pbar.update(downloaded)
            else:
                pbar.finish()
                pbar = None

        for model_name, url in self.MODELS.items():
            if specific_models is not None and model_name not in specific_models:
                continue
            model_path = os.path.join(self.DEFAULT_MODELS_DIR, model_name)
            if os.path.exists(model_path):
                return model_path

            request.urlretrieve(url, model_path, show_progress)

            import zipfile

            with zipfile.ZipFile(model_path, "r") as zip_ref:
                zip_ref.extractall(self.DEFAULT_MODELS_DIR)
            return model_path


    def build_vector(self):
        f = io.open(self.file_path,'r',encoding = 'utf-8',newline='\n',errors = 'ignore')
        for line in tqdm(f,colour = 'red'):
            tokens = line.strip().split(' ')
            self.data[tokens[0]] = np.array(list(map(float, tokens[1:])))
    
    def _get_dimension(self):
        return self.dimension

    def _get_vector(self,word : str):
        if word in self.data and self.data != {}:
            return self.data[word]
        else:
            return np.zeros(self.dimension)
    
    def _get_vector_list(self,word_list : list):
        if self.data == {}:
            self.build_vector()
        if word_list == []:
            return np.zeros(self.dimension)
        return np.array([self._get_vector(word) for word in word_list])

    def padding_truncate(self,vector_list : list,max_length : int = 100):
        if len(vector_list) > max_length:
            return vector_list[:max_length].tolist()
        else:
            return np.concatenate((vector_list,np.zeros((max_length-len(vector_list),self.dimension)))).tolist()
    

    def padding_truncate_lists(self,vector_list : list,max_length : int = 100):
        # if vector_list == None:
        #     return "Empyt or none type can't be processed"
        return np.array([self.padding_truncate(i,max_length) for i in vector_list])
        #for numpy array



    

    