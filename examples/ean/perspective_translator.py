#!/usr/bin/env python3
"""
Perspective Translator - Empathy Amplification Network (EAN) Example

This example demonstrates how to use LLMs to translate experiences
across different perspectives to build empathy and understanding.

Part of the Beyond Greed framework.
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class PerspectiveTranslation:
    """Result of perspective translation"""
    original_context: str
    target_perspective: str
    translated_narrative: str
    empathy_score: int  # 0-100
    key_insights: List[str]
    emotional_bridges: List[str]


class PerspectiveTranslator:
    """
    Translates experiences from one perspective to make them
    understandable and emotionally resonant from another perspective.
    
    Core to building empathy at scale.
    """
    
    def __init__(self, llm_api_key: Optional[str] = None):
        """Initialize the translator"""
        self.api_key = llm_api_key
        
    def translate_perspective(
        self,
        story: str,
        from_context: str,
        to_context: str
    ) -> PerspectiveTranslation:
        """
        Translate a story/experience from one context to another.
        
        Args:
            story: The original narrative or data
            from_context: Description of the original perspective
            to_context: Description of the target perspective
            
        Returns:
            PerspectiveTranslation with the translated narrative
        """
        # In production, this would use actual LLM API
        # For this example, we demonstrate the concept
        
        prompt = self._create_translation_prompt(story, from_context, to_context)
        
        # Simulated translation (in production, call LLM)
        return self._example_translation(story, from_context, to_context)
    
    def _create_translation_prompt(
        self,
        story: str,
        from_context: str,
        to_context: str
    ) -> str:
        """Create prompt for LLM translation"""
        return f"""
Translate the following experience/story to be emotionally resonant
for someone from a different context.

ORIGINAL CONTEXT: {from_context}

ORIGINAL STORY:
{story}

TARGET AUDIENCE: {to_context}

Create a first-person narrative that:
1. Preserves the emotional truth and core experience
2. Uses references and language familiar to the target audience
3. Creates genuine empathy and understanding
4. Avoids stereotypes or oversimplification
5. Maintains dignity and complexity of the original

Also identify:
- Key insights the target audience should understand
- Emotional bridges between the experiences
- Universal human elements that connect both contexts

Provide response in JSON format.
"""
    
    def _example_translation(
        self,
        story: str,
        from_context: str,
        to_context: str
    ) -> PerspectiveTranslation:
        """
        Example translation demonstrating the concept.
        
        This would be replaced by actual LLM processing in production.
        """
        
        # Example: Translating climate refugee experience for US suburban context
        if "climate" in story.lower() and "suburban" in to_context.lower():
            return PerspectiveTranslation(
                original_context=from_context,
                target_perspective=to_context,
                translated_narrative="""
You've lived in the same house for twenty years. Your kids grew up here.
You know every neighbor, every tree, every crack in the sidewalk.

But now, the heat is different. It's not just summer being hot—it's 
something wrong. Your garden dies no matter what you do. Your water bill 
has tripled because you need to run the AC constantly. You've had three 
power outages this month because the grid can't handle the load.

Last summer, your daughter couldn't play outside for a week because the 
smoke from distant wildfires made it unsafe to breathe. The week before 
that, your basement flooded from a storm that shouldn't have been possible 
here.

Your home insurance doubled, then tripled, then the company just... left. 
Nobody will insure you anymore. The value of your house—your life savings,
your retirement plan—is dropping every month.

You want to move somewhere safer, but who would buy your house? And where 
would you go? Everywhere has its own climate problems now. You can't afford 
to start over anyway. You're stuck.

This isn't some distant problem. This is your life, right now, falling 
apart in slow motion. And you didn't do anything wrong. You just lived 
your life, and the world changed around you.

That's what climate displacement feels like. It's not abstract. It's not 
statistics. It's your home, your safety, your future—all becoming uncertain.

Now imagine this, but you also don't have the resources to even consider 
moving. Imagine you never had insurance. Imagine your government can't or 
won't help. Imagine you face this with a fraction of the wealth, support, 
and options you currently have.

That's what millions of people are experiencing right now. They're not 
so different from you. They just had less to start with, and they're 
facing the same forces that are beginning to affect your life.
""",
                empathy_score=85,
                key_insights=[
                    "Climate displacement isn't sudden—it's slow erosion of security",
                    "Home and stability are universal human needs",
                    "Economic vulnerability amplifies climate impacts",
                    "This could happen to anyone, anywhere",
                    "Having resources helps, but doesn't make you immune"
                ],
                emotional_bridges=[
                    "Fear of losing your home and security",
                    "Watching your children's future become uncertain",
                    "Feeling powerless against forces beyond your control",
                    "The desire for stability and safety",
                    "Attachment to place and community"
                ]
            )
        
        # Generic example for other cases
        return PerspectiveTranslation(
            original_context=from_context,
            target_perspective=to_context,
            translated_narrative="[Translation would be generated by LLM in production]",
            empathy_score=75,
            key_insights=["Insight 1", "Insight 2"],
            emotional_bridges=["Shared experience 1", "Universal feeling 1"]
        )
    
    def create_empathy_report(self, translation: PerspectiveTranslation) -> Dict:
        """
        Generate a structured empathy report.
        
        Args:
            translation: The perspective translation
            
        Returns:
            Dictionary with empathy analysis
        """
        return {
            "empathy_amplification_report": {
                "translation": {
                    "from": translation.original_context,
                    "to": translation.target_perspective,
                    "empathy_activation_score": translation.empathy_score,
                    "interpretation": self._interpret_empathy_score(translation.empathy_score)
                },
                "narrative": translation.translated_narrative,
                "key_insights": translation.key_insights,
                "emotional_bridges": translation.emotional_bridges,
                "recommendations": [
                    "Share this perspective with others in similar contexts",
                    "Consider how this experience relates to policy decisions",
                    "Reflect on commonalities across different experiences",
                    "Take action informed by this understanding"
                ]
            }
        }
    
    def _interpret_empathy_score(self, score: int) -> str:
        """Interpret empathy activation score"""
        if score >= 80:
            return "High empathy activation - strong emotional connection likely"
        elif score >= 60:
            return "Moderate empathy activation - good understanding likely"
        elif score >= 40:
            return "Low empathy activation - may need additional context"
        else:
            return "Minimal empathy activation - translation may need revision"


def main():
    """Example usage of the Perspective Translator"""
    
    # Example story
    climate_story = """
    Data: Climate change causing crop failures in Sub-Saharan Africa.
    300 million people affected by changing rainfall patterns.
    Traditional farming methods no longer viable.
    Increasing food insecurity and displacement.
    """
    
    print("Beyond Greed - Perspective Translator Example")
    print("=" * 60)
    print("\nTranslating climate impact story...")
    print(f"\nOriginal story: {climate_story}")
    print("\n" + "=" * 60 + "\n")
    
    # Create translator
    translator = PerspectiveTranslator()
    
    # Translate the perspective
    translation = translator.translate_perspective(
        story=climate_story,
        from_context="Subsistence farmer in Sub-Saharan Africa",
        to_context="US suburban homeowner"
    )
    
    # Generate empathy report
    report = translator.create_empathy_report(translation)
    
    # Display the translated narrative
    print("TRANSLATED PERSPECTIVE:")
    print("-" * 60)
    print(translation.translated_narrative)
    print("-" * 60)
    
    print(f"\nEmpathy Activation Score: {translation.empathy_score}/100")
    
    print("\nKEY INSIGHTS:")
    for i, insight in enumerate(translation.key_insights, 1):
        print(f"  {i}. {insight}")
    
    print("\nEMOTIONAL BRIDGES:")
    for i, bridge in enumerate(translation.emotional_bridges, 1):
        print(f"  {i}. {bridge}")
    
    print("\n" + "=" * 60)
    print("\nThis is how EAN creates empathy at scale:")
    print("- Translates abstract data into personal experiences")
    print("- Bridges cultural and geographic distances")
    print("- Makes distant suffering emotionally present")
    print("- Enables informed, compassionate decision-making")


if __name__ == "__main__":
    main()
