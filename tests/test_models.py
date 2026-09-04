from scidiagnose.agent import OpenAICompatibleAgent
from scidiagnose.models import AgentAction, ExperimentRequest
def test_actions_are_structured():
    assert ExperimentRequest("EXP_001","compare").to_dict()["tool"]=="compare"; assert AgentAction("tool_call","inspect").type=="tool_call"
def test_api_action_normalization():
    assert OpenAICompatibleAgent._validate({"tool_name":"inspect","args":{}}).tool == "inspect"
    assert OpenAICompatibleAgent._validate({"tool":"transform_and_compare","arguments":{"transform":"transpose"}}).arguments == {"operation":"transpose"}
    assert OpenAICompatibleAgent._validate({"action":"final","decision":"fault","fault_family":"spatial_alignment","root_cause":"orientation","confidence":.9,"evidence_experiment_ids":["EXP_001"],"recommended_repair":{}}).type == "final"
    assert OpenAICompatibleAgent._validate({"type":"json_object","tool":"shift_and_compare","arguments":{"dr":-1,"dc":0}}).arguments == {"dr":-1,"dc":0}
    assert OpenAICompatibleAgent._validate({"type":"tool_call","tool":"evaluate_candidate","arguments":{"pipeline":[{"operation":"shift","dr":0,"dc":1}]}}).arguments == {"pipeline":[{"type":"shift","dr":0,"dc":1}]}


def test_structured_envelopes_are_unwrapped(monkeypatch):
    class Settings: base_url="http://example.invalid"; model_name="test"; api_key="test"
    agent = OpenAICompatibleAgent(Settings())
    class Response:
        def __enter__(self): return self
        def __exit__(self, *args): return False
        def read(self): return b'{"choices":[{"message":{"content":"{\\"type\\":\\"json_object\\",\\"obj\\":{\\"answer\\":1}}"}}]}'
    monkeypatch.setattr("scidiagnose.agent.request.urlopen", lambda *args, **kwargs: Response())
    assert agent._request_json("test", {}, {}) == {"answer": 1}


def test_reflection_decision_dialects_are_normalized():
    value, decision = OpenAICompatibleAgent._normalize_reflection(
        {"reflection": {"action": "needs more evidence", "summary": "not decisive"}}
    )
    assert value["summary"] == "not decisive"
    assert decision == "continue"
    assert OpenAICompatibleAgent._normalize_reflection({"decision": "fault"})[1] == "propose_fault"
    assert OpenAICompatibleAgent._normalize_reflection({"decision": "no-fault"})[1] == "propose_no_fault"
