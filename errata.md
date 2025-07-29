# 正誤表

| 該当ページ |  該当箇所 |  誤  |  正  | 補足 | 対応 | 
| ---- | ---- | ---- | ---- | ---- | ---- |
| p.7 | 式 (2.7) の (3, 3) 要素 | 5.52 | 1.52 | |  |
| p.24 | 本文 4 行目 | $m \in \\{0, \ldots, 2^{11}-1\\}$ | $m \in \\{0, \ldots, 2^{10}-1\\}$ | |  |
| p.24 | 式 (3.5) | $(-1)^s \times 2^{e - 15} \times (1 + m \times 2^{-11})$ | $(-1)^s \times 2^{e - 15} \times (1 + m \times 2^{-10})$ | |  |
| p.52 | コード 3.16, 5 行目  | `(x * 0x0101010101010101) >> 56)` | `((x * 0x0101010101010101) >> 56) & 0xff` | |  |
| p.52 | コード 3.16 の下 2 行目  | わずか 12 回の演算 | わずか 13 回の演算 | |  |
| p.77 | 式 (4.1) の (3, 3) 要素 | 5.52 | 1.52 | |  |
| p.85 | 表 4.2 | 指標は分類精度 | 指標は分類誤差 | |  |
| p.85 | 表 4.2 | CIFAR-10 $\uparrow$ | CIFAR-10 $\downarrow$ | |  |
| p.85 | 表 4.2 | Sequential MNIST $\uparrow$ | Sequential MNIST $\downarrow$ | |  |
| p.88 | 式 (4.11) | $\text{im2col}(X)\_{ijklm} = X\_{i, j + k - 1, l + m - 1}$ | $\text{im2col}(X)\_{ijklm} = X\_{i, l + j - 1, m + k - 1}$ | |  |
| p.105 | 下から 4 行目 | 簡単になことが | 簡単になることが | |  |
| p.109 |  | ResNext121 | ResNext101 | |  |
| p.109 | コード 5.1, 13 行目 | `evaluator.eval(model, device)` | `evaluator.eval(teacher, device)` | |  |
| p.110 | 18 行目 | `loss_distill = criterion(outputs / temperature, outputs_teacher / temperature) * temperature * temperature` | ※1 | |  |
| p.112 | 式 (5.7) | $\text{KL}(A_{ij}^{(t,q,k)} \\\\| A_{ij}^{(t,q,k)})$ | $\text{KL}(A_{ij}^{(t,q,k)} \\\\| A_{ij}^{(s,q,k)})$ | |  |
| p.112 | 式 (5.9) | $\text{KL}(A_{ij}^{(t,v,v)} \\\\| A_{ij}^{(t,v,v)})$ | $\text{KL}(A_{ij}^{(t,v,v)} \\\\| A_{ij}^{(s,v,v)})$ | |  |
| p.142 | 式 (6.86) 下 | 標準正規分布より | 各成分が標準正規分布より | |  |
| p.142 | 式 (6.86) 下 | $b \in \mathbb{R}$ | $b_i \in \mathbb{R}$ | |  |
| p.150 | 式 (6.144) | $\mathbb{R}^{m \times d'}$ | $\mathbb{R}^{n \times d'}$ | |  |
| p.150 | 式 (6.147) 上 | 注機構 | 注意機構 | |  |
| p.150 | 式 (6.147) | $Y\_i = \frac{H\_m \psi'(Q\_i)}{g\_m^\top \psi'(Q\_i)}$ | $Y\_m = \frac{H\_m \psi'(Q\_m)}{g\_m^\top \psi'(Q\_m)}$ | |  |
| p.159 | 第 7.1 節 4 行目 | Xception どの | Xception などの | |  |
| p.165 | 式 (7.18) | $Y\_i = \frac{H\_m \gamma(Q\_i)}{g\_m^\top \gamma(Q\_i)}$ | $Y\_m = \frac{H\_m \gamma(Q\_m)}{g\_m^\top \gamma(Q\_m)}$ | |  |
| p.165 | 下から 9 行目 | 削減きます | 削減できます | |  |
| p.170 | 図 7.2 のキャプション | $w$個の埋め込み | $W$個の埋め込み | |  |
| p.172 | 本文 3 行目 | $X_{ij} \in \mathbb{R}^d$ | $X_i \in \mathbb{R}^d$ | |  |

※1：
```
loss_distill = (
    F.kl_div(
        F.log_softmax(outputs / temperature, dim=1),
        F.softmax(outputs_teacher / temperature, dim=1),
        reduction="batchmean",
    )
    * temperature
    * temperature
)
```
