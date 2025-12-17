#!/usr/bin/env python3
"""
Simple Intent Analyzer - Intention Verification System (IVS) Example

This example demonstrates how to use LLMs to analyze the intentions
behind policy proposals and detect potential misalignments.

Part of the Beyond Greed framework.
"""

import json
import os
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class IntentionAnalysis:
    """Result of intention analysis"""
    stated_intentions: List[str]
    implicit_intentions: List[str]
    beneficiaries: List[str]
    potential_concerns: List[str]
    alignment_score: int  # 0-100
    red_flags: List[str]
    recommendations: List[str]


class SimpleIntentAnalyzer:
    """
    Basic implementation of intention verification using LLM analysis.
    
    In production, this would use fine-tuned models, distributed systems,
    and blockchain integration. This example demonstrates the core concept.
    """
    
    def __init__(self, llm_api_key: Optional[str] = None):
        """
        Initialize the analyzer.
        
        Args:
            llm_api_key: API key for LLM service (OpenAI, Anthropic, etc.)
        """
        self.api_key = llm_api_key or os.getenv("LLM_API_KEY")
        
    def analyze_proposal(self, proposal_text: str) -> IntentionAnalysis:
        """
        Analyze a policy proposal for intentions and alignment.
        
        Args:
            proposal_text: The full text of the proposal
            
        Returns:
            IntentionAnalysis object with findings
        """
        # In a real implementation, this would call an LLM API
        # For this example, we'll demonstrate the structure
        
        analysis_prompt = self._create_analysis_prompt(proposal_text)
        
        # Simulated LLM response (in production, call actual LLM)
        # llm_response = self._call_llm_api(analysis_prompt)
        
        # For demonstration, return example analysis
        return self._parse_example_analysis(proposal_text)
    
    def _create_analysis_prompt(self, proposal: str) -> str:
        """Create the prompt for LLM analysis"""
        return f"""
Analyze the following policy proposal for its intentions, both stated and implicit.

Identify:
1. Explicitly stated intentions and goals
2. Implicit or unstated intentions (read between the lines)
3. Who benefits from this proposal (primary and secondary beneficiaries)
4. Potential concerns or red flags
5. Alignment between stated intentions and likely outcomes (score 0-100)
6. Specific red flags that match known corruption patterns
7. Recommendations for improving transparency and accountability

Proposal:
{proposal}

Provide analysis in JSON format with keys:
- stated_intentions: list of strings
- implicit_intentions: list of strings
- beneficiaries: list of strings
- potential_concerns: list of strings
- alignment_score: integer 0-100
- red_flags: list of strings
- recommendations: list of strings
"""
    
    def _parse_example_analysis(self, proposal: str) -> IntentionAnalysis:
        """
        Example analysis for demonstration.
        
        In production, this would parse the LLM's JSON response.
        """
        # This is a simplified example
        return IntentionAnalysis(
            stated_intentions=[
                "Improve community infrastructure",
                "Create local jobs",
                "Serve public interest"
            ],
            implicit_intentions=[
                "Possible benefit to specific contractor",
                "May increase property values in select areas"
            ],
            beneficiaries=[
                "General public (stated)",
                "Construction companies (likely)",
                "Property owners in adjacent areas (possible)"
            ],
            potential_concerns=[
                "Lack of competitive bidding process",
                "Timeline seems rushed",
                "Environmental impact assessment incomplete"
            ],
            alignment_score=65,
            red_flags=[
                "Single-source contractor selection",
                "Expedited approval process"
            ],
            recommendations=[
                "Require competitive bidding",
                "Extend review period to 60 days",
                "Complete environmental assessment",
                "Publish detailed cost breakdown",
                "Establish independent oversight committee"
            ]
        )
    
    def generate_transparency_report(self, analysis: IntentionAnalysis) -> Dict:
        """
        Generate a public transparency report.
        
        Args:
            analysis: The intention analysis
            
        Returns:
            Dictionary formatted for public consumption
        """
        return {
            "transparency_report": {
                "intention_verification": {
                    "stated_goals": analysis.stated_intentions,
                    "detected_implicit_intentions": analysis.implicit_intentions,
                    "alignment_assessment": {
                        "score": analysis.alignment_score,
                        "interpretation": self._interpret_score(analysis.alignment_score)
                    }
                },
                "stakeholder_analysis": {
                    "identified_beneficiaries": analysis.beneficiaries
                },
                "risk_assessment": {
                    "concerns": analysis.potential_concerns,
                    "red_flags": analysis.red_flags,
                    "risk_level": self._assess_risk_level(analysis)
                },
                "recommendations": {
                    "required_actions": analysis.recommendations,
                    "next_steps": [
                        "Address identified concerns",
                        "Increase transparency measures",
                        "Establish accountability mechanisms"
                    ]
                }
            }
        }
    
    def _interpret_score(self, score: int) -> str:
        """Interpret alignment score"""
        if score >= 80:
            return "High alignment - intentions well-matched to outcomes"
        elif score >= 60:
            return "Moderate alignment - some concerns should be addressed"
        elif score >= 40:
            return "Low alignment - significant restructuring needed"
        else:
            return "Critical misalignment - proposal should be rejected or completely redesigned"
    
    def _assess_risk_level(self, analysis: IntentionAnalysis) -> str:
        """Assess overall corruption risk level"""
        red_flag_count = len(analysis.red_flags)
        
        if red_flag_count == 0 and analysis.alignment_score >= 80:
            return "LOW"
        elif red_flag_count <= 2 and analysis.alignment_score >= 60:
            return "MODERATE"
        elif red_flag_count <= 4 or analysis.alignment_score >= 40:
            return "HIGH"
        else:
            return "CRITICAL"


def main():
    """Example usage of the Simple Intent Analyzer"""
    
    # Example proposal
    sample_proposal = """
    Proposal: Community Center Construction Project
    
    The city proposes to construct a new community center to serve 
    local residents. The project will create 50 jobs during construction
    and provide valuable community space for education and recreation.
    
    Budget: $10 million
    Timeline: 12 months
    Contractor: Selected through expedited process
    """
    
    print("Beyond Greed - Simple Intent Analyzer Example")
    print("=" * 60)
    print("\nAnalyzing proposal...\n")
    
    # Create analyzer
    analyzer = SimpleIntentAnalyzer()
    
    # Analyze the proposal
    analysis = analyzer.analyze_proposal(sample_proposal)
    
    # Generate transparency report
    report = analyzer.generate_transparency_report(analysis)
    
    # Display results
    print(json.dumps(report, indent=2))
    
    print("\n" + "=" * 60)
    print(f"Alignment Score: {analysis.alignment_score}/100")
    print(f"Risk Level: {analyzer._assess_risk_level(analysis)}")
    print("\nKey Recommendations:")
    for i, rec in enumerate(analysis.recommendations, 1):
        print(f"  {i}. {rec}")


if __name__ == "__main__":
    main()
