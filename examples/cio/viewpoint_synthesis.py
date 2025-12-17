#!/usr/bin/env python3
"""
Viewpoint Synthesizer - Collective Intelligence Optimization (CIO) Example

This example demonstrates how to use LLMs to synthesize diverse
perspectives into coherent collective understanding.

Part of the Beyond Greed framework.
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class Viewpoint:
    """A single perspective on an issue"""
    contributor: str
    position: str
    reasoning: str
    values: List[str]
    concerns: List[str]


@dataclass
class CollectiveSynthesis:
    """Result of synthesizing multiple viewpoints"""
    shared_values: List[str]
    areas_of_agreement: List[str]
    creative_tensions: List[Dict[str, str]]
    emergent_insights: List[str]
    minority_concerns: List[str]
    recommended_approach: str
    synthesis_quality_score: int  # 0-100
    confidence_score: int  # 0-100


class ViewpointSynthesizer:
    """
    Synthesizes diverse perspectives without losing nuance
    or marginalizing minorities.
    
    Core to collective intelligence optimization.
    """
    
    def __init__(self, llm_api_key: Optional[str] = None):
        """Initialize the synthesizer"""
        self.api_key = llm_api_key
    
    def synthesize_viewpoints(
        self,
        viewpoints: List[Viewpoint],
        issue: str
    ) -> CollectiveSynthesis:
        """
        Synthesize multiple viewpoints into collective understanding.
        
        Args:
            viewpoints: List of individual perspectives
            issue: The issue being addressed
            
        Returns:
            CollectiveSynthesis with integrated insights
        """
        # In production, this would use actual LLM API
        # For this example, we demonstrate the concept
        
        prompt = self._create_synthesis_prompt(viewpoints, issue)
        
        # Simulated synthesis (in production, call LLM)
        return self._example_synthesis(viewpoints, issue)
    
    def _create_synthesis_prompt(
        self,
        viewpoints: List[Viewpoint],
        issue: str
    ) -> str:
        """Create prompt for LLM synthesis"""
        
        viewpoints_text = "\n\n".join([
            f"Viewpoint {i+1} ({vp.contributor}):\n"
            f"Position: {vp.position}\n"
            f"Reasoning: {vp.reasoning}\n"
            f"Values: {', '.join(vp.values)}\n"
            f"Concerns: {', '.join(vp.concerns)}"
            for i, vp in enumerate(viewpoints)
        ])
        
        return f"""
Synthesize the following diverse viewpoints on: {issue}

{viewpoints_text}

Create a synthesis that:
1. Identifies shared values (what everyone cares about)
2. Maps areas of agreement
3. Recognizes creative tensions (productive disagreements)
4. Detects emergent insights (not in any single viewpoint)
5. Ensures minority concerns are addressed
6. Recommends an approach that honors all valid concerns

IMPORTANT:
- Do NOT just average or vote
- Preserve nuance and complexity
- Look for solutions that transcend apparent contradictions
- Give voice to minority perspectives
- Identify insights that emerge from the collective

Provide response in structured JSON format.
"""
    
    def _example_synthesis(
        self,
        viewpoints: List[Viewpoint],
        issue: str
    ) -> CollectiveSynthesis:
        """
        Example synthesis demonstrating the concept.
        
        This would be replaced by actual LLM processing in production.
        """
        
        # Example for climate policy viewpoints
        if "climate" in issue.lower():
            return CollectiveSynthesis(
                shared_values=[
                    "Protect future generations",
                    "Ensure economic viability",
                    "Support vulnerable communities",
                    "Act based on science",
                    "Preserve individual freedom"
                ],
                areas_of_agreement=[
                    "Climate change is happening and requires response",
                    "Transition must be just and equitable",
                    "Innovation and technology are part of solution",
                    "Both individual and systemic change needed",
                    "Can't ignore economic realities"
                ],
                creative_tensions=[
                    {
                        "tension": "Speed vs. Thoroughness",
                        "synthesis": "Phased approach: Quick wins on clear opportunities, "
                                   "deliberate planning for complex transitions"
                    },
                    {
                        "tension": "Individual freedom vs. Collective action",
                        "synthesis": "Make sustainable choices easy and attractive, "
                                   "not just mandatory. Incentives over mandates where possible"
                    },
                    {
                        "tension": "Economic growth vs. Environmental limits",
                        "synthesis": "Redefine growth: wellbeing and regeneration, "
                                   "not just GDP. Invest in sustainable abundance"
                    }
                ],
                emergent_insights=[
                    "Climate action creates economic opportunity if framed correctly",
                    "Frontline communities have solutions that benefit everyone",
                    "Technology + nature-based solutions stronger than either alone",
                    "Job training programs solve both transition and inequality issues",
                    "Community-scale action builds momentum and proof of concept"
                ],
                minority_concerns=[
                    "Indigenous communities: Sacred sites must be protected in any transition",
                    "Disabled community: Ensure accessibility isn't sacrificed for sustainability",
                    "Rural workers: Need viable alternatives, not just urban solutions",
                    "Global South: Climate debt must be acknowledged and addressed"
                ],
                recommended_approach="""
Integrated Climate Response Strategy:

FOUNDATION: Justice-centered transition
- No community left behind
- Address historical inequities
- Empower frontline leadership

IMMEDIATE (0-2 years):
- Low-hanging fruit: Energy efficiency, waste reduction
- Job training programs in green industries
- Community-scale renewable projects
- Support for local solutions

MEDIUM-TERM (2-5 years):
- Infrastructure transformation
- Regenerative agriculture support
- Clean transportation networks
- Nature-based solutions at scale

LONG-TERM (5-20 years):
- Fully renewable energy systems
- Circular economy implementation
- Restored ecosystems
- Climate-resilient communities

PRINCIPLES:
- Science-based targets
- Economic opportunity, not just cost
- Individual empowerment + systemic change
- Innovation encouraged, not mandated
- Transparent, accountable progress tracking
- Continuous learning and adaptation

ACCOUNTABILITY:
- Annual progress reports
- Community oversight
- Course correction mechanisms
- Success celebration

This approach honors all perspectives while creating coherent direction.
""",
                synthesis_quality_score=89,
                confidence_score=82
            )
        
        # Generic synthesis for other topics
        return CollectiveSynthesis(
            shared_values=["Example shared value"],
            areas_of_agreement=["Example agreement"],
            creative_tensions=[
                {"tension": "Example tension", "synthesis": "Example resolution"}
            ],
            emergent_insights=["Example emergent insight"],
            minority_concerns=["Example minority concern"],
            recommended_approach="[Synthesized approach would be generated by LLM]",
            synthesis_quality_score=75,
            confidence_score=70
        )
    
    def generate_synthesis_report(self, synthesis: CollectiveSynthesis) -> Dict:
        """
        Generate a structured synthesis report.
        
        Args:
            synthesis: The collective synthesis
            
        Returns:
            Dictionary with synthesis analysis
        """
        return {
            "collective_intelligence_synthesis": {
                "quality_metrics": {
                    "synthesis_quality": synthesis.synthesis_quality_score,
                    "confidence": synthesis.confidence_score,
                    "interpretation": self._interpret_quality(
                        synthesis.synthesis_quality_score
                    )
                },
                "shared_foundation": {
                    "common_values": synthesis.shared_values,
                    "agreements": synthesis.areas_of_agreement
                },
                "productive_disagreements": {
                    "tensions_and_resolutions": synthesis.creative_tensions,
                    "note": "These tensions are productive—they lead to better solutions"
                },
                "emergent_intelligence": {
                    "insights": synthesis.emergent_insights,
                    "note": "These insights appeared through synthesis, "
                           "not from any single contributor"
                },
                "inclusion": {
                    "minority_concerns": synthesis.minority_concerns,
                    "commitment": "All concerns addressed in recommended approach"
                },
                "recommended_action": synthesis.recommended_approach
            }
        }
    
    def _interpret_quality(self, score: int) -> str:
        """Interpret synthesis quality score"""
        if score >= 85:
            return "Excellent synthesis - high coherence while preserving nuance"
        elif score >= 70:
            return "Good synthesis - solid integration with minor gaps"
        elif score >= 55:
            return "Adequate synthesis - workable but could be improved"
        else:
            return "Weak synthesis - needs revision or more input"


def main():
    """Example usage of the Viewpoint Synthesizer"""
    
    # Example viewpoints on climate policy
    viewpoints = [
        Viewpoint(
            contributor="Environmental Scientist",
            position="Urgent, comprehensive climate action needed",
            reasoning="Science shows we have limited time to prevent catastrophic warming",
            values=["Scientific accuracy", "Future generations", "Ecosystem health"],
            concerns=["Insufficient action", "Missing deadlines", "Irreversible damage"]
        ),
        Viewpoint(
            contributor="Labor Union Representative",
            position="Just transition with worker protections",
            reasoning="Can't leave workers behind in transition to green economy",
            values=["Worker dignity", "Economic security", "Fair transition"],
            concerns=["Job losses", "Communities abandoned", "Unfunded mandates"]
        ),
        Viewpoint(
            contributor="Small Business Owner",
            position="Market-based solutions with support for adaptation",
            reasoning="Innovation happens best with incentives, not mandates",
            values=["Economic freedom", "Innovation", "Practical solutions"],
            concerns=["Regulatory burden", "Costs", "Feasibility"]
        ),
        Viewpoint(
            contributor="Indigenous Community Leader",
            position="Nature-based solutions honoring traditional knowledge",
            reasoning="Indigenous practices have sustained land for millennia",
            values=["Traditional knowledge", "Sacred relationship with land", "Community"],
            concerns=["Exclusion from decisions", "Sacred sites threatened", "Extraction continues"]
        ),
        Viewpoint(
            contributor="Youth Climate Activist",
            position="Rapid, systemic transformation",
            reasoning="It's our future at stake, we deserve a livable planet",
            values=["Intergenerational justice", "Bold action", "System change"],
            concerns=["Too little too late", "Adult inaction", "Future stolen"]
        )
    ]
    
    print("Beyond Greed - Viewpoint Synthesizer Example")
    print("=" * 60)
    print(f"\nSynthesizing {len(viewpoints)} viewpoints on climate policy...")
    print("\n" + "=" * 60 + "\n")
    
    # Create synthesizer
    synthesizer = ViewpointSynthesizer()
    
    # Synthesize viewpoints
    synthesis = synthesizer.synthesize_viewpoints(
        viewpoints=viewpoints,
        issue="Climate change policy and response"
    )
    
    # Generate report
    report = synthesizer.generate_synthesis_report(synthesis)
    
    # Display results
    print("COLLECTIVE SYNTHESIS REPORT")
    print("=" * 60)
    print(json.dumps(report, indent=2))
    
    print("\n" + "=" * 60)
    print("\nThis is how CIO enables collective intelligence:")
    print("- Preserves nuance from all perspectives")
    print("- Finds shared values beneath disagreements")
    print("- Transforms tensions into creative solutions")
    print("- Surfaces insights no individual had")
    print("- Ensures minority voices are heard")
    print("- Creates coherent direction from diversity")


if __name__ == "__main__":
    main()
