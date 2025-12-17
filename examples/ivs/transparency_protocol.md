# Transparency Protocol - Example Format

## Intention Declaration Standard

This document demonstrates the standard format for declaring intentions in the Beyond Greed framework (IVS component).

---

## Example: Municipal Contract Declaration

### Basic Information

```yaml
declaration:
  id: "IVS-2025-CITY-ROAD-001"
  date: "2025-06-15"
  jurisdiction: "City of Example, State"
  category: "infrastructure"
  title: "Main Street Reconstruction Project"
  
project:
  description: "Complete reconstruction of Main Street (2.5 miles) including roadway, sidewalks, bike lanes, and utilities"
  budget: 
    total: "$15,000,000"
    breakdown:
      - category: "roadway"
        amount: "$8,000,000"
      - category: "utilities"
        amount: "$4,000,000"
      - category: "sidewalks_bikelanes"
        amount: "$2,500,000"
      - category: "contingency"
        amount: "$500,000"
  
  timeline:
    start_date: "2025-09-01"
    completion_date: "2026-08-31"
    milestones:
      - name: "Design completion"
        date: "2025-08-15"
      - name: "Procurement complete"
        date: "2025-08-30"
      - name: "Phase 1 complete"
        date: "2026-03-31"
      - name: "Final completion"
        date: "2026-08-31"
```

### Intention Declaration

```yaml
intentions:
  primary:
    - goal: "Improve safety for all road users"
      metric: "Reduce accidents by 50%"
      
    - goal: "Enable multi-modal transportation"
      metric: "Increase bike/pedestrian traffic by 200%"
      
    - goal: "Update aging infrastructure"
      metric: "Eliminate water main breaks (currently 12/year)"
      
    - goal: "Create local employment"
      metric: "50 direct construction jobs, 75% local hiring"
  
  secondary:
    - goal: "Reduce long-term maintenance costs"
      metric: "30% reduction in annual road maintenance budget"
      
    - goal: "Support local business during construction"
      metric: "Business disruption fund of $200,000 available"
      
    - goal: "Environmental improvement"
      metric: "Green infrastructure captures 80% of stormwater"
```

### Stakeholder Analysis

```yaml
stakeholders:
  primary_beneficiaries:
    - group: "Daily road users"
      population: "~15,000 vehicles/day"
      benefit: "Safer, smoother travel"
      
    - group: "Pedestrians and cyclists"
      population: "~2,000 daily"
      benefit: "Protected infrastructure, better connectivity"
      
    - group: "Adjacent residents"
      population: "~800 households"
      benefit: "Improved infrastructure, reduced flooding"
  
  secondary_beneficiaries:
    - group: "Local businesses"
      count: "42 businesses"
      benefit: "Better access, improved streetscape"
      
    - group: "Construction workers"
      count: "50 jobs"
      benefit: "Employment opportunity"
  
  stakeholders_bearing_costs:
    - group: "Taxpayers"
      population: "All city residents (~50,000)"
      cost: "$300 per capita average"
      
    - group: "Local businesses during construction"
      count: "42 businesses"
      cost: "Temporary access disruption"
      mitigation: "Disruption fund, phased approach, signage"
      
    - group: "Adjacent residents during construction"
      population: "~800 households"
      cost: "Noise, dust, traffic"
      mitigation: "Night work prohibited, dust suppression, regular updates"
  
  potentially_marginalized_voices:
    - group: "Low-income residents without cars"
      concern: "Ensure public transit maintained during construction"
      accommodation: "Shuttle service during major disruptions"
      
    - group: "Disabled community"
      concern: "Accessibility during and after construction"
      accommodation: "ADA compliance, accessible detours, universal design"
```

### Transparency Measures

```yaml
transparency:
  procurement:
    method: "Open competitive bidding"
    bidders: 
      invited: "All qualified contractors"
      minimum: "3 bids required"
    
    selection_criteria:
      - criterion: "Price"
        weight: "40%"
      - criterion: "Experience and qualifications"
        weight: "30%"
      - criterion: "Local hiring commitment"
        weight: "20%"
      - criterion: "Timeline feasibility"
        weight: "10%"
    
    evaluation_committee:
      - role: "City Engineer"
        name: "Jane Smith"
      - role: "Public Works Director"
        name: "John Doe"
      - role: "Community Representative"
        name: "Maria Garcia"
      - role: "Independent Engineer"
        name: "Robert Johnson"
  
  monitoring:
    public_dashboard: "https://example.gov/mainstreet-project"
    update_frequency: "Weekly"
    
    metrics_tracked:
      - "Budget status"
      - "Timeline progress"
      - "Safety incidents"
      - "Local hiring percentage"
      - "Business disruption complaints"
      - "Air quality during construction"
    
    reporting:
      frequency: "Monthly public meetings"
      format: "Open to all residents, livestreamed, archived"
      
  financial_transparency:
    all_contracts_public: true
    payment_schedule_public: true
    change_orders_require: "Public justification within 48 hours"
    
  oversight:
    independent_auditor: "State Comptroller's Office"
    citizen_oversight: 
      committee: "Main Street Project Oversight Committee"
      members: "9 residents, selected by lottery"
      authority: "Review all decisions, make recommendations"
```

### Accountability Mechanisms

```yaml
accountability:
  responsible_parties:
    - name: "Sarah Williams"
      role: "Project Manager"
      commitment: "Weekly public updates, monthly community meetings"
      contact: "swilliams@example.gov"
      
    - name: "Example Construction Co."
      role: "General Contractor"
      commitment: "Daily progress reports, 24hr emergency contact"
      contact: "project@exampleconstruction.com"
  
  performance_bonds:
    - type: "Completion bond"
      amount: "$15,000,000"
      
    - type: "Maintenance bond"
      amount: "$1,500,000"
      duration: "2 years post-completion"
  
  consequences_for_misalignment:
    budget_overrun: "City Manager must approve, public hearing required"
    timeline_delays: "Weekly penalty of $10,000, public explanation required"
    safety_violations: "Work stoppage until resolved, public report"
    failure_to_meet_intentions: "Formal review, reputation impact, potential contract termination"
  
  success_criteria:
    - metric: "Project completed within 110% of budget"
      measurement: "Final audit"
      
    - metric: "Project completed within 120% of timeline"
      measurement: "Substantial completion date"
      
    - metric: "Zero serious safety incidents"
      measurement: "OSHA reportables"
      
    - metric: "75% local hiring achieved"
      measurement: "Contractor payroll records"
      
    - metric: "Business disruption fund 80%+ utilized appropriately"
      measurement: "Business survey, fund administrator report"
```

### Public Feedback Integration

```yaml
public_input:
  consultation_process:
    - phase: "Design phase"
      dates: "2025-03-01 to 2025-05-01"
      methods: ["Open houses (3)", "Online survey", "Focus groups"]
      participants: "847 residents provided input"
      
    - phase: "During construction"
      ongoing: true
      methods: ["24hr hotline", "Weekly office hours", "Online portal"]
  
  incorporation_of_feedback:
    - feedback: "Concerns about bike lane width"
      response: "Increased from 4ft to 5ft based on safety data"
      
    - feedback: "Request for more trees"
      response: "Added 30 trees beyond initial plan, selected by community vote"
      
    - feedback: "Noise concerns"
      response: "Prohibited work before 7am and after 7pm"
  
  ongoing_engagement:
    website: "example.gov/mainstreet"
    email_list: "Subscribe for weekly updates"
    community_meetings: "First Tuesday of each month, 6pm, City Hall"
    feedback_channels:
      - "Online form"
      - "Phone: 555-0123"
      - "In-person: City Hall, Room 201"
```

### IVS Verification

```yaml
ivs_analysis:
  intention_signature: "SHA256:9f86d081884c7d659a2feaa0c55ad015..."
  analysis_date: "2025-06-15"
  
  automated_assessment:
    alignment_score: 87/100
    interpretation: "High alignment between intentions and proposal structure"
    
    red_flags: []
    
    concerns:
      - issue: "Budget contingency at 3.3% is below typical 5-10%"
        severity: "Low"
        recommendation: "Consider increasing contingency or very tight cost controls"
    
    strengths:
      - "Comprehensive stakeholder analysis"
      - "Strong transparency measures"
      - "Clear accountability mechanisms"
      - "Robust public input process"
      - "Competitive procurement"
  
  public_ledger:
    blockchain_record: "https://transparency.blockchain.gov/record/IVS-2025-CITY-ROAD-001"
    timestamp: "2025-06-15T14:30:00Z"
    immutable: true
    
  monitoring_schedule:
    reviews:
      - type: "Quarterly progress review"
        responsible: "IVS automated system + citizen committee"
      - type: "Annual alignment audit"
        responsible: "Independent auditor"
      - type: "Final completion assessment"
        responsible: "Full IVS analysis + public feedback"
```

---

## Using This Template

1. **Customize** for your specific project/decision
2. **Complete** all sections honestly and thoroughly
3. **Publish** the declaration before beginning work
4. **Track** progress against stated intentions
5. **Report** outcomes transparently
6. **Learn** from misalignments

## Benefits

- **Builds Trust:** Public knows your intentions
- **Ensures Accountability:** Can't hide from commitments
- **Improves Decisions:** Forces clear thinking
- **Prevents Corruption:** Misalignment becomes obvious
- **Enables Learning:** Others learn from your experience

---

[← Back to Examples](../README.md) | [← Back to Main README](../../README.md)
