from scidiagnose.ssh_executor import SSHDirectExecutor
def test_experiment_id_validation():
    executor=SSHDirectExecutor()
    assert executor.job_dir("EXP_001").endswith("EXP_001")
