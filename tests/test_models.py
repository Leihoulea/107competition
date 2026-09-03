from scidiagnose.agent import OpenAICompatibleAgent
from scidiagnose.models import AgentAction, ExperimentRequest
def test_actions_are_structured():
    assert ExperimentRequest("EXP_001","compare").to_dict()["tool"]=="compare"; assert AgentAction("tool_call","inspect").type=="tool_call"
def test_api_action_normalization():
    assert OpenAICompatibleAgent._validate({"tool_name":"inspect","args":{}}).tool == "inspect"
    assert OpenAICompatibleAgent._validate({"tool":"transform_and_compare","arguments":{"transform":"transpose"}}).arguments == {"operation":"transpose"}
    assert OpenAICompatibleAgent._validate({"action":"final","decision":"fault","fault_family":"spatial_alignment","root_cause":"orientation","confidence":.9,"evidence_experiment_ids":["EXP_001"],"recommended_repair":{}}).type == "final"
