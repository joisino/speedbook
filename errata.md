# 正誤表

| 該当ページ |  該当箇所 |  誤  |  正  | 補足 | 対応 | 
| ---- | ---- | ---- | ---- | ---- | ---- |
| p.109 | コード 5.1, 13 行目 | `evaluator.eval(model, device)` | `evaluator.eval(teacher, device)` | |  |
| p.110 | 18 行目 | `loss_distill = criterion(outputs / temperature, outputs_teacher / temperature) * temperature * temperature` | ※1 | |  |


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
