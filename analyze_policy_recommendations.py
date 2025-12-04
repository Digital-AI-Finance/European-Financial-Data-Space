"""
Policy Recommendations Quality Analysis
European Financial Data Space White Paper

This script analyzes the 7 policy recommendations for:
1. Actionability and specificity
2. Clear ownership
3. Measurable outcomes/KPIs
4. Priority justification
5. Missing recommendations
6. EU policy alignment
"""

import json
from datetime import datetime

# Extract the 7 recommendations from the HTML
recommendations = [
    {
        "number": 1,
        "title": "Establish Data Quality Standards",
        "priority": "High Priority",
        "description": "Develop a mandatory data quality framework addressing conceptual and organizational dimensions for AI applications. Current EFDS policy neglects whether shared data is fit for AI development.",
        "section_details": "Policymakers should develop a comprehensive data quality framework encompassing both conceptual dimensions (accuracy, completeness, consistency, timeliness) and organizational dimensions (governance, documentation, audit trails). This framework should be integrated into ESAP collection body requirements and FIDA data holder obligations."
    },
    {
        "number": 2,
        "title": "Complete FIDA Negotiations with Balanced Scope",
        "priority": "High Priority",
        "description": "Finalize FIDA by Q1 2026 with clear scope definitions. Address industry concerns through phased implementation (2027-2031) and proportionate SME requirements.",
        "section_details": "Complete FIDA negotiations by Q1 2026 with a balanced approach: (1) Address legitimate industry concerns through proportionate requirements for different entity sizes; (2) Maintain the core open finance objectives; (3) Provide clear transitional periods for each stage; (4) Establish robust compensation mechanisms for data holders."
    },
    {
        "number": 3,
        "title": "Accelerate ESAP Collection Body Onboarding",
        "priority": "High Priority",
        "description": "Prioritize the 6-month prototype phase and ensure all 27 Member States have designated and trained collection bodies by mid-2026.",
        "section_details": "Prioritize collection body onboarding and the 6-month prototype phase. Ensure all Member States have designated, trained, and technically equipped collection bodies by mid-2026. Consider establishing an EU-level support mechanism for Member States with limited technical capacity."
    },
    {
        "number": 4,
        "title": "Integrate AI Governance Framework",
        "priority": "Medium Priority",
        "description": "Align EFDS with AI Act requirements. Develop guidelines for responsible AI development using EFDS data, addressing bias risks.",
        "section_details": "Integrate AI governance requirements into EFDS implementation: (1) Require data providers to document potential biases in datasets; (2) Establish bias testing protocols for AI systems using EFDS data; (3) Create transparency requirements for AI-driven financial decisions; (4) Align EFDS data quality standards with AI Act requirements for high-risk systems."
    },
    {
        "number": 5,
        "title": "Develop Crypto-Asset Data Framework",
        "priority": "Medium Priority",
        "description": "Begin preparatory work for crypto-asset data integration ahead of FIDA Stage 2 (36 months post-adoption).",
        "section_details": "Begin preparatory work for crypto-asset data integration: (1) Establish a technical working group to assess blockchain data interoperability with ESAP; (2) Develop prototype data schemas for crypto-asset disclosures; (3) Identify potential collection body arrangements for decentralized assets; (4) Coordinate with MiCA implementation to ensure data format alignment."
    },
    {
        "number": 6,
        "title": "Create SME Support Mechanisms",
        "priority": "Medium Priority",
        "description": "Establish technical assistance programs, simplified reporting pathways, and public-private partnerships to prevent SME exclusion.",
        "section_details": "Create targeted SME and Fintech support mechanisms: (1) Establish EU-funded technical assistance programs for EFDS compliance; (2) Develop simplified reporting pathways with proportionate requirements; (3) Create public-private partnerships to provide shared infrastructure; (4) Consider phased compliance timelines based on entity size; (5) Establish regulatory sandboxes for Fintech FIDA applications."
    },
    {
        "number": 7,
        "title": "Standardize Machine-Readable Formats",
        "priority": "Ongoing",
        "description": "Complete format selection (XML/JSON/XBRL) through evidence-based assessment. Provide clear migration pathways for existing systems.",
        "section_details": "Not explicitly detailed in policy boxes - mentioned in challenges section regarding ESAP implementation."
    }
]

# Analysis framework
def analyze_recommendation(rec):
    """Analyze a single recommendation across 5 dimensions"""

    analysis = {
        "recommendation": rec["title"],
        "priority": rec["priority"],
        "scores": {},
        "strengths": [],
        "weaknesses": [],
        "suggestions": []
    }

    # 1. Actionability and Specificity (0-10)
    action_verbs = ["develop", "establish", "finalize", "complete", "accelerate", "integrate", "create", "standardize"]
    has_action_verb = any(verb in rec["title"].lower() for verb in action_verbs)
    has_numbered_steps = "(" in rec["section_details"] and ")" in rec["section_details"]
    has_deadline = any(year in rec["section_details"] for year in ["2026", "2027", "2030"])

    actionability_score = 0
    if has_action_verb: actionability_score += 3
    if has_numbered_steps: actionability_score += 4
    if has_deadline: actionability_score += 3

    analysis["scores"]["actionability"] = actionability_score

    if has_numbered_steps:
        analysis["strengths"].append("Contains numbered implementation steps")
    else:
        analysis["weaknesses"].append("Lacks numbered implementation steps")

    if has_deadline:
        analysis["strengths"].append("Includes specific timeline")
    else:
        analysis["weaknesses"].append("Missing specific deadline")

    # 2. Clear Ownership (0-10)
    stakeholders = ["ESMA", "Commission", "EBA", "EIOPA", "Member States", "collection bodies",
                   "policymakers", "data holders", "ESAs", "EFRAG"]
    mentioned_stakeholders = [s for s in stakeholders if s.lower() in rec["section_details"].lower()]

    ownership_score = min(len(mentioned_stakeholders) * 2, 10)
    analysis["scores"]["ownership"] = ownership_score

    if mentioned_stakeholders:
        analysis["strengths"].append(f"Mentions stakeholders: {', '.join(mentioned_stakeholders[:3])}")
    else:
        analysis["weaknesses"].append("No specific responsible parties identified")
        analysis["suggestions"].append("Explicitly assign lead authority (e.g., 'ESMA in coordination with...')")

    # 3. Measurable Outcomes/KPIs (0-10)
    measurable_terms = ["all 27", "by mid-2026", "Q1 2026", "6-month", "Stage 2",
                       "framework", "standards", "requirements", "protocols"]
    mentioned_measures = [m for m in measurable_terms if m.lower() in rec["section_details"].lower()]

    kpi_score = min(len(mentioned_measures) * 2, 10)
    analysis["scores"]["kpi"] = kpi_score

    if kpi_score >= 6:
        analysis["strengths"].append("Contains measurable elements")
    else:
        analysis["weaknesses"].append("Lacks clear KPIs or success metrics")
        analysis["suggestions"].append("Add quantifiable success criteria (e.g., '% of Member States compliant', 'reduction in reporting errors by X%')")

    # 4. Implementation Details (0-10)
    detail_indicators = ["how", "what", "who", "when", "where", "requirements", "mechanisms",
                        "pathways", "procedures", "guidelines", "protocols"]
    detail_count = sum(1 for ind in detail_indicators if ind in rec["section_details"].lower())

    detail_score = min(detail_count, 10)
    analysis["scores"]["implementation_detail"] = detail_score

    if detail_score < 5:
        analysis["weaknesses"].append("Limited implementation guidance")
        analysis["suggestions"].append("Expand on 'how' the recommendation will be executed (tools, resources, procedures)")

    # 5. Priority Justification
    priority_map = {"High Priority": 10, "Medium Priority": 6, "Ongoing": 3}
    analysis["scores"]["priority_level"] = priority_map.get(rec["priority"], 0)

    return analysis

# Run analysis
results = []
for rec in recommendations:
    results.append(analyze_recommendation(rec))

# Generate report
report = {
    "analysis_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "total_recommendations": len(recommendations),
    "summary": {
        "high_priority": len([r for r in recommendations if r["priority"] == "High Priority"]),
        "medium_priority": len([r for r in recommendations if r["priority"] == "Medium Priority"]),
        "ongoing": len([r for r in recommendations if r["priority"] == "Ongoing"])
    },
    "detailed_analysis": results
}

# Calculate overall scores
avg_scores = {
    "actionability": sum(r["scores"]["actionability"] for r in results) / len(results),
    "ownership": sum(r["scores"]["ownership"] for r in results) / len(results),
    "kpi": sum(r["scores"]["kpi"] for r in results) / len(results),
    "implementation_detail": sum(r["scores"]["implementation_detail"] for r in results) / len(results)
}

report["average_scores"] = avg_scores

# Print detailed report
print("=" * 80)
print("POLICY RECOMMENDATIONS QUALITY ANALYSIS")
print("European Financial Data Space White Paper")
print("=" * 80)
print()
print(f"Analysis Date: {report['analysis_date']}")
print(f"Total Recommendations: {report['total_recommendations']}")
print(f"  - High Priority: {report['summary']['high_priority']}")
print(f"  - Medium Priority: {report['summary']['medium_priority']}")
print(f"  - Ongoing: {report['summary']['ongoing']}")
print()

print("OVERALL QUALITY SCORES (out of 10)")
print("-" * 80)
for dimension, score in avg_scores.items():
    bar = "#" * int(score) + "-" * (10 - int(score))
    print(f"{dimension.replace('_', ' ').title():25s} [{bar}] {score:.1f}/10")
print()

print("INDIVIDUAL RECOMMENDATION ANALYSIS")
print("=" * 80)

for i, result in enumerate(results, 1):
    print(f"\n{i}. {result['recommendation']}")
    print(f"   Priority: {result['priority']}")
    print()

    print("   Scores:")
    for dimension, score in result['scores'].items():
        if dimension != 'priority_level':
            print(f"     - {dimension.replace('_', ' ').title()}: {score}/10")
    print()

    if result['strengths']:
        print("   Strengths:")
        for strength in result['strengths']:
            print(f"     + {strength}")
        print()

    if result['weaknesses']:
        print("   Weaknesses:")
        for weakness in result['weaknesses']:
            print(f"     - {weakness}")
        print()

    if result['suggestions']:
        print("   Improvement Suggestions:")
        for suggestion in result['suggestions']:
            print(f"     > {suggestion}")
        print()

# Save to JSON
output_file = "policy_recommendations_analysis.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)

print("=" * 80)
print(f"Full analysis saved to: {output_file}")
print("=" * 80)
