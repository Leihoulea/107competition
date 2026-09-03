# SciDiagnose

SciDiagnose is a minimal, evidence-driven prototype for diagnosing *scientific silent failures* with real remote computation. Traditional HPC monitoring answers whether a job completed. SciDiagnose asks whether the resulting science is trustworthy.

A computational failure is an exception, missing dependency, or OOM. A scientific silent failure may exit with code zero while producing a scientifically invalid result, such as a spatially misaligned product. The agent never receives the hidden answer: it selects a general diagnostic experiment, sends it to a real compute host, observes structured evidence, and then chooses its next action.

## MVP architecture

`Agent -> ExperimentTools -> ComputeExecutor -> SSH Direct host`

The current real backend is `SSHDirectExecutor`: it uses the pre-configured SSH alias, `scp`, `nohup`, a remote PID, and `result.json` / `failure.json`. `LocalExecutor` shares the backend contract for later local testing. No Slurm, database, UI, LangChain, or container runtime is used.

## Install and configuration

Python 3.10+ and NumPy are required locally. Configure an existing SSH alias without placing credentials in this repository:

```powershell
$env:PYTHONPATH = 'src'
$env:SCIDIAG_REMOTE_HOST = 'server-114'
```

The remote host must have Python. GEO-001 also needs NumPy. SciDiagnose never installs it automatically. On the remote host, an operator may explicitly provision an isolated environment:

```bash
python3 -m venv ~/venvs/scidiag
source ~/venvs/scidiag/bin/activate
python -m pip install numpy
```

Then set `SCIDIAG_REMOTE_PYTHON=~/venvs/scidiag/bin/python` locally.

## Run

```powershell
$env:PYTHONPATH = 'src'
python scripts/probe_remote.py
python scripts/smoke_remote.py
python scripts/create_demo_case.py
python scripts/run_demo.py --case geo_001 --backend ssh --host server-114
```

The smoke test runs real Python on the remote host and prints `RUNNING -> COMPLETED`. The demo uploads only the tiny public GEO-001 arrays once, executes two remote NumPy experiments, records all actions under `runs/`, and writes an evidence-backed final diagnosis. `hidden/ground_truth.json` is used only by the post-run evaluator, never by the agent.

## Limits and future work

This MVP has one synthetic, spatial case and a deterministic ManualAgent for API-free demonstrations. Future work can add an OpenAI-compatible decision client, real EPIC/Meteosat inputs, GPU backends, and a Slurm backend without changing the agent-facing experiment interface. The group server is deliberately not connected during the competition stage.

## School LLM API

SciDiagnose includes a dependency-free OpenAI-compatible client. Keep credentials out of the repository and set them in your shell:

```powershell
$env:SCIDIAG_MODEL_PROVIDER = 'openai_compatible'
$env:SCIDIAG_BASE_URL = 'https://<school-api-host>/v1'
$env:SCIDIAG_MODEL_NAME = '<school-model-name>'
$env:SCIDIAG_API_KEY = '<your-key>'
python scripts/run_demo.py --case geo_001 --backend ssh --agent api
```

If an SSH connection is slow, set a larger per-command limit before launching:

```powershell
$env:SCIDIAG_COMMAND_TIMEOUT = '120'
```

The endpoint must implement `POST /chat/completions`. The agent receives only public task state and actual experiment records; it never receives GEO-001 hidden ground truth.

Alternatively, create a local `E:\107competition\.env` from `.env.example` and add the three model settings there. `.env` is ignored by Git and is read automatically; never send or commit it.
