"""Backend-neutral contracts for experiment execution."""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any

@dataclass(frozen=True)
class JobHandle:
    job_id: str
    backend: str
    remote_host: str | None
    remote_pid: int | None
    job_dir: str
    def to_dict(self) -> dict[str, Any]: return asdict(self)

class ComputeExecutor(ABC):
    @abstractmethod
    def probe(self) -> dict[str, Any]: ...
    @abstractmethod
    def upload(self, local_path: str, remote_path: str) -> None: ...
    @abstractmethod
    def submit(self, experiment_id: str, command: list[str]) -> JobHandle: ...
    @abstractmethod
    def status(self, job: JobHandle) -> str: ...
    @abstractmethod
    def logs(self, job: JobHandle, tail: int = 100) -> tuple[str, str]: ...
    @abstractmethod
    def fetch_result(self, job: JobHandle) -> dict[str, Any]: ...
