# 正誤表

| 該当ページ |  該当箇所 |  誤  |  正  | 補足 | 対応 | 
| ---- | ---- | ---- | ---- | ---- | ---- |
| p.52 | コード 3.16, 5 行目  | `(x * 0x0101010101010101) >> 56)` | `((x * 0x0101010101010101) >> 56) & 0xff` | |  |
| p.52 | コード 3.16 の下 2 行目  | わずか 12 回の演算 | わずか 13 回の演算 | |  |
| p.109 | コード 5.1, 13 行目 | `evaluator.eval(model, device)` | `evaluator.eval(teacher, device)` | |  |
| p.110 | 18 行目 | `loss_distill = criterion(outputs / temperature, outputs_teacher / temperature) * temperature * temperature` | ※1 | |  |
| p.112 | 式 (5.7) | $\text{KL}(A_{ij}^{(t,q,k)} \\\\| A_{ij}^{(t,q,k)})$ | $\text{KL}(A_{ij}^{(t,q,k)} \\\\| A_{ij}^{(s,q,k)})$ | |  |
| p.112 | 式 (5.9) | $\text{KL}(A_{ij}^{(t,v,v)} \\\\| A_{ij}^{(t,v,v)})$ | $\text{KL}(A_{ij}^{(t,v,v)} \\\\| A_{ij}^{(s,v,v)})$ | |  |
| p.150 | 式 (6.147) 上 | 注機構 | 注意機構 | |  |
| p.159 | 第 7.1 節 4 行目 | Xception どの | Xception などの | |  |

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
