# coding:utf-8
import numpy as np
import random
import matplotlib.pyplot as plt
from operator import itemgetter

# 適当にランダムな個体biontをMAX_biontだけ生成
# 評価するbiontをbiont_scoreで評価
def make_biontandscore(MAX_biont) :
    # biont[i][j]=1ならj番目の商品をナップサックに入れる個体i
    biont = []
    # biont_score[i]=[bW, bV] (bW:個体の総重量, bV:個体の総合価値)
    biont_score = [[0 for i in range(2)] for j in range(MAX_biont)]
    for i in range(MAX_biont) :
        tmp = []
        for j in range(N) :
            tmp.append(random.randint(0,1))
            if (tmp[j]) :
                # 入れる商品の重さがナップサックに入るなら入れる
                if (biont_score[i][0]+w[j] <= W) :
                    biont_score[i][0] += w[j]
                    biont_score[i][1] += v[j]
        biont.append(tmp)

    return biont, biont_score

# エリート保存戦略関数
# 上位num_eliteまでをエリートとして返す
# 使い方:elite.append(extract_elite(biont, biont_score))
def extract_elite(biont, biont_score, num_elite=2) :
    tmp = list(biont_score)
    tmp.sort(key=itemgetter(1))
    tmp.reverse()
    elite = []
    for i in range(2) :
        elite.append(biont[biont_score.index(tmp[i])])

    return elite


# シード値を設定(再現させるため)
random.seed(0)

# 商品の数
N = 10
# ナップサックの入れられる重さ
W = 300

# w[i]:i番目商品の重さ
# v[i]:i番目商品の価値
# item:ナップサックに入れた価値リスト
w = []
v = []
# w,vを1~100のランダムに設定
for i in range(N) :
    w.append(random.randint(1,100))
    v.append(random.randint(1,100))
print("w")
print(w)
print("v")
print(v)

# 個体をMAX_biontだけ生成する
MAX_biont = 10
biont, biont_score = make_biontandscore(MAX_biont)
print("biont")
print(biont)
print("biont_score")
print(biont_score)

# 価値が最大のものを抽出しエリート保存戦略する
# ここでは上位二個
elite = []
elite.extend(extract_elite(biont, biont_score))
print("elite")
print(elite)