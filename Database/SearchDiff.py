import time

import requests

# 两岸差异用词
words_diff_dict = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                   34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# 两岸学术差异
# 6-37
learning_dict = [39, 40, 41, 42]

word_url = "https://bs.chinese-linguipedia.org/api/web/diff/search?category={}&page={}&word=&type="
learning_url = "https://bs.chinese-linguipedia.org/api/web/academic/search?category={}&page={}&word="

requests.packages.urllib3.disable_warnings()


def search_learning():
    f = open("两岸学术用词.txt", "a+", encoding="utf-8")
    for id in learning_dict:
        current_page = 0
        break_flag = False
        while True:
            if break_flag:
                break
            current_page += 1
            target_url = learning_url.format(id, current_page)
            res = ""
            try_count = 0
            while try_count < 3:
                try:
                    res = requests.get(url=target_url, verify=False, timeout=10)
                except:
                    print("遇到异常，重试中。。。")
                    time.sleep(2)
                try_count += 1
            res_json = res.json()
            data = res_json["data"]
            last_page = data["last_page"]
            if current_page == last_page:
                break_flag = True
            items = data["data"]
            for item in items:
                # 领域
                category = item["category"]
                # 台湾用语
                tw_word = item["tw_word"]
                # 大陆用语
                cn_word = item["cn_word"]
                # 外文
                en_word = item["en_word"]
                # 来源
                source = item["source"]
                # 是否于华语文大辞典有相关条目
                word_txt = item["word"]
                if word_txt:
                    word_txt = "是"
                else:
                    word_txt = "否"
                data = [category, tw_word, cn_word, en_word, source, word_txt]
                row = "      ".join(data)
                print(row)
                f.write(row)
                f.write("\n")
                f.flush()


def search_words():
    f = open("两岸差异用词.txt", "a+", encoding="utf-8")
    for id in words_diff_dict:
        current_page = 0
        break_flag = False
        while True:
            if break_flag:
                break
            current_page += 1
            target_url = word_url.format(id, current_page)
            res = requests.get(url=target_url)
            res_json = res.json()
            data = res_json["data"]
            last_page = data["last_page"]
            if current_page == last_page:
                break_flag = True
            items = data["data"]
            for item in items:
                # 异同类别
                type = item["type"]
                # 子领域
                category = item["category"]
                # 台湾用语
                tw_word = item["tw_word"]
                # 大陆用语
                cn_word = item["cn_word"]
                data = [type, category, tw_word, cn_word]
                row = "      ".join(data)
                print(row)
                f.write(row)
                f.write("\n")
                f.flush()


if __name__ == '__main__':
    # print("开始查询：", "两岸用词差异")
    # search_words()
    # print()
    print("开始查询：", "两岸学术用词差异")
    search_learning()
