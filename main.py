from agents.normalization_agent import NormalizationAgent
from agents.hypothesis_agent import HypothesisAgent
from agents.evidence_agent import EvidenceAgent
from agents.revision_agent import RevisionAgent
from agents.strategy_agent import StrategyAgent
from agents.critique_agent import CritiqueAgent

def run_system(user_input):

    norm = NormalizationAgent()
    hyp = HypothesisAgent()
    ev = EvidenceAgent()
    rev = RevisionAgent()
    strat = StrategyAgent()
    crit = CritiqueAgent()

    symptoms = norm.run(user_input)
    diseases = hyp.run(symptoms)
    evidence = ev.run(diseases, symptoms)
    confidence = rev.run(diseases, evidence)
    next_step = strat.run(diseases, evidence)
    bias = crit.run(confidence)

    return {
        "symptoms": symptoms,
        "confidence": confidence,
        "evidence": evidence,
        "next_step": next_step,
        "bias": bias
    }
