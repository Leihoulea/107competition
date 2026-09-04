# SciDiagnose 今日进度总结（2026-09-04）

今日完成了 SciDiagnose 最小原型从“远端环境不可用”到“学校 LLM 驱动真实远端诊断闭环”的实现与验证。

## 已完成

- 完成 SSH Direct 计算后端：
  - 使用系统 SSH/SCP，不依赖 Slurm。
  - 远端任务通过 `nohup + PID` 运行。
  - 以 `result.json` / `failure.json` 判断任务结果。
  - 支持远端状态、日志、JSON 结果获取。

- 完成学校比赛主机环境配置：
  - 创建隔离环境 `~/venvs/scidiag`。
  - 安装 NumPy 2.5.2。
  - 不污染系统 Python 业务环境。

- 完成 GEO-001 合成科研 case：
  - 256×256 空间结构云掩膜。
  - 初始 identity agreement：0.58197。
  - `rot180` 后 agreement：1.0。

- 完成远端通用实验工具：
  - `inspect`
  - `compare`
  - `transform_and_compare`
  - `shift_and_compare`

- 完成学校 LLM API 接入：
  - OpenAI-compatible Chat Completions 接口。
  - API Key 保存在 Git 忽略的 `.env` 中。
  - 支持模型返回格式兼容与参数别名规范化。

- 完成 Agent、ExperimentTools、Runner、Evaluator 与测试。

## 今日修复的问题

- 将原先 Slurm 方案改为 SSH Direct，适配学校主机没有 Slurm 的实际条件。
- 修复远端 venv 缺少 `ensurepip` 的问题，安装 `python3.12-venv` 后创建独立环境。
- 修复 SCP 对 `$HOME` 路径的处理。
- 修复 SSH 短暂断线造成整个诊断中止的问题：
  - 使用短连接；
  - 安全查询自动重试；
  - 远端作业继续运行；
  - 轮询出现网络抖动时持续等待结果。
- 修复学校模型返回 `transform` 而非 `operation` 导致实验失败的问题。
- 增加“未达到质量阈值不得过早输出 `fault` 结论”的证据约束。

## 最终真实验证

最终运行记录：`runs/RUN_1788451344/`

学校模型完成两轮真实决策：

1. `EXP_001`：选择 `inspect`
   - 远端执行成功。
   - 发现 reference 与 target 统计分布一致。

2. `EXP_002`：选择 `transform_and_compare(rot180)`
   - 远端执行成功。
   - agreement 从 0.58197 提升至 1.0。
   - IoU 为 1.0。

最终诊断：

- Fault：是
- Root cause：空间方向发生 180° 旋转
- Recommended repair：`rot180`
- 引用真实实验：`EXP_001`、`EXP_002`
- 独立 evaluator：98.33 / 100

## v0.2.2 integration hardening

- 将 fault gate 收紧为：低质量初始观测、非恒等 repair 候选、真实实验的显著改善、且达到阈值，缺一不可。
- 将 no-fault 的 evaluator 总分与 fault case 对齐：有正常基线、无虚构 repair 的正确 no-fault 可获得 repair/abstention validation 分。
- 将 transform-only baseline 更名为 deterministic_transform_sweep，新增 7×121 transform-plus-shift 的 deterministic_full_search。
- One-Shot baseline 现在可一次提出完整 pipeline，而非被接口限制为单个 transform。
- RunReader 优先读取每实验 artifact 与 compute_summary.json，并读取 graph run 的 state.json / final.json；benchmark 可展示真实远端 wall/CPU/budget telemetry。
- Planner 获得中性的完整 tool catalog，降低 API 模型猜测参数契约的失败率。

## 当前状态

SciDiagnose 已具备可审计的核心验收链路：

```text
科学异常
→ LLM 选择实验
→ SSH 远端真实计算
→ 新证据
→ LLM 再决策
→ 远端验证
→ 最终证据化诊断
```

下一阶段应冻结核心架构，执行 B03、B01×3、B02 与四类 benchmark 的正式实验，再整理答辩材料。
