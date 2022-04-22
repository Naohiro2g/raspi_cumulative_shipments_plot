# naohiro2g/raspi_cumulative_shipments_plot

Graph generator of Raspberry Pi cumulative shipments data on wikipedia.

wikipedia用 ラズパイ累計出荷台数のグラフ作成

<img src="./images/Raspberry Pi Cumulative Shipment Units.png" width="360">

The graph is used on:

- <https://ja.wikipedia.org/wiki/Raspberry_Pi>
- <https://en.wikipedia.org/wiki/Raspberry_Pi>
- <https://fr.wikipedia.org/wiki/Raspberry_Pi>
- <https://it.wikipedia.org/wiki/Raspberry_Pi>
- <https://zh.wikipedia.org/wiki/%E6%A0%91%E8%8E%93%E6%B4%BE>

## matplotlibのフォントキャッシュをクリアする方法

新しいフォントをインストールした後、キャッシュディレクトリを探して消去する必要がある。

```python
import shutil
import matplotlib

shutil.rmtree(matplotlib.get_cachedir())
```
