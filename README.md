# naohiro2g/raspi_cumulative_shipments_plot

Graph generator of Raspberry Pi cumulative shipments data on wikipedia.

wikipedia用 ラズパイ累計出荷台数のグラフ作成

The graph is used on:

- <https://ja.wikipedia.org/wiki/Raspberry_Pi>
- <https://fr.wikipedia.org/wiki/Raspberry_Pi>
- <https://it.wikipedia.org/wiki/Raspberry_Pi>
- <https://zh.wikipedia.org/wiki/%E6%A0%91%E8%8E%93%E6%B4%BE>



### matplotlibのフォントキャッシュをクリアする方法

新しいフォントをインストールした後、キャッシュディレクトリを探して消去する必要がある。
```
import shutil
import matplotlib

shutil.rmtree(matplotlib.get_cachedir())
```
