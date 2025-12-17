# Beyond Greed Framework Examples

This directory contains example implementations and demonstrations of the Beyond Greed framework components.

## Available Examples

### 1. IVS Examples
- [Simple Intent Analyzer](./ivs/simple_intent_analyzer.py) - Basic intent analysis using LLMs
- [Transparency Protocol](./ivs/transparency_protocol.md) - Example intention declaration format
- [Pattern Recognition](./ivs/corruption_patterns.md) - Common corruption patterns

### 2. EAN Examples
- [Perspective Translation](./ean/perspective_translator.py) - Translate experiences across contexts
- [Empathy Metrics](./ean/empathy_metrics.md) - Measuring empathy in systems
- [Cross-Cultural Bridge](./ean/cultural_bridge.py) - Cultural framework translation

### 3. CIO Examples
- [Viewpoint Synthesizer](./cio/viewpoint_synthesis.py) - Synthesize diverse perspectives
- [Information Router](./cio/info_router.py) - Route decisions to stakeholders
- [Collective Decision](./cio/collective_decision.md) - Example decision-making process

## Using These Examples

### Prerequisites

Most examples require:
- Python 3.8+
- Access to LLM APIs (OpenAI, Anthropic, or local models)
- Basic understanding of the Beyond Greed framework

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up API keys
cp .env.example .env
# Edit .env with your API keys
```

### Running Examples

```bash
# Run IVS intent analyzer
python ivs/simple_intent_analyzer.py --input "sample_proposal.txt"

# Run EAN perspective translator
python ean/perspective_translator.py --story "example_story.txt"

# Run CIO viewpoint synthesizer
python cio/viewpoint_synthesis.py --input "viewpoints.json"
```

## Example Projects

These examples are intentionally simple to demonstrate core concepts. For production implementations:

1. **Security**: Add proper authentication, encryption, and access controls
2. **Scalability**: Implement distributed processing and caching
3. **Privacy**: Add differential privacy and data protection
4. **Testing**: Include comprehensive test suites
5. **Documentation**: Provide detailed API documentation

## Contributing Examples

We welcome new examples! See [CONTRIBUTING.md](../docs/CONTRIBUTING.md) for guidelines.

**Good Examples:**
- Demonstrate a clear concept
- Include documentation
- Provide sample inputs/outputs
- Are well-commented
- Follow Python/project style guides

## Example Use Cases

### For Educators
Use these examples in:
- Classroom demonstrations
- Student projects
- Research prototypes
- Workshop activities

### For Developers
Use as starting points for:
- Production implementations
- Custom adaptations
- Integration projects
- Proof-of-concept systems

### For Researchers
Use to:
- Validate theoretical concepts
- Run experiments
- Collect data
- Publish findings

## License

All examples are licensed under MIT License for maximum reusability.

See [LICENSE.md](../LICENSE.md) for details.

## Questions?

- Technical questions: dev@beyondgreed.org
- General questions: hello@beyondgreed.org
- Open an issue on GitHub

---

[← Back to Main README](../README.md)
