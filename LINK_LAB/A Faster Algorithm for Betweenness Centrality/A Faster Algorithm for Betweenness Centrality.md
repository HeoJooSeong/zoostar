<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
#A Faster Algorithm for Betweenness Centrality

>요약  
betweenness centrality index는 social networks 분석에서 필수적이지만 계산이 복잡하다.(고비용이다)  
현재 가장 빠르다고 알려진 알고리즘의 평균 복잡도는 \\({n}^{3}\\)의 시간과 \\({n}^{2}\\)의 공간이 요구됩니다.(n 은 네트워크의 요소 개수)  

---
---
---
## 2. 최단 경로 기반 Centrality Indices
소셜 그리고 다른 네트워크들은 편리하게  G = (V, E) 그래프를 표현할 수  있다. ( V 는 배우(요소) , E는 배우들 사이의 연결 )  
n, m은 각각의 점과 선의 개수를 나타낸다. 매우 단순하게, 모든 그래프가 방향성이 없고 연결되어있을때, (비록, loop or multiple edge 이지만) 작은 수정으로 방향 그래프를 일반화 할 수 있다.  
가중치 그래프에서 w 를 간선의 가중치 함수, w(e)는 0보다 크고, e 는 E에 속한다고 하자.  
비가중치 그래프에서  w(e) =1, e는 E에 속한다고 하자.  
가중치는 연결 길이와 같은 측정에 사용된다. 
path는 s로 시작해 t로 끝나는 점과 선의 연결 길이로 정의한다. path 길이는 그 선들의 가중치의 합과 같다.  
 \\({D}_{G}(s,t)\\)를 s,t 사이의 거리로 말한다. 즉, 그래프에서 어떠한 연결보다 가장 작은 길이를 나타낸다. 
 몇몇 측정 값은 그래프에서 점의 중요성의 개념에서 변화를 알아챘다.  
 
\\({σ}_{s,t}\\)는 최단 경로의 갯수라고 하자. 

또, \\({σ}_{s,t}(v)\\)는 점 v를 지나가는 최단 경로의 갯수라고 하자.
