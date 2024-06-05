
import jieba
import config
jieba.load_userdict(config.user_dict_path)

def test_user_dict():
    sentense = "人工智能+python和c++哪个难"
    ret = jieba.lcut(sentense)
    print(ret)
