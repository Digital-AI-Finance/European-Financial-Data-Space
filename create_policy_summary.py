"""
Create visual summary of policy recommendations analysis
Generates comparison table and gap analysis
"""

# Summary data from analysis
recommendations = [
    {"num": 1, "title": "Data Quality Standards", "priority": "High",
     "action": 7, "owner": 2, "kpi": 4, "detail": 1, "total": 14,
     "eu_align": 8, "missing": ["Timeline", "Lead authority", "Budget", "KPIs"]},
    {"num": 2, "title": "FIDA Negotiations", "priority": "High",
     "action": 10, "owner": 2, "kpi": 4, "detail": 2, "total": 18,
     "eu_align": 6, "missing": ["Negotiation lead", "Specific scope", "Compensation details"]},
    {"num": 3, "title": "ESAP Collection Bodies", "priority": "High",
     "action": 6, "owner": 4, "kpi": 4, "detail": 0, "total": 14,
     "eu_align": 5, "missing": ["Process owner", "Support mechanism details", "Contingency"]},
    {"num": 4, "title": "AI Governance", "priority": "Medium*",
     "action": 7, "owner": 0, "kpi": 6, "detail": 2, "total": 15,
     "eu_align": 7, "missing": ["Lead authority", "Timeline", "Enforcement"]},
    {"num": 5, "title": "Crypto-Asset Data", "priority": "Medium",
     "action": 7, "owner": 0, "kpi": 0, "detail": 0, "total": 7,
     "eu_align": 3, "missing": ["Owner", "Timeline", "Deliverables", "Budget"]},
    {"num": 6, "title": "SME Support", "priority": "Medium*",
     "action": 7, "owner": 0, "kpi": 2, "detail": 3, "total": 12,
     "eu_align": 4, "missing": ["Owner", "Budget amount", "Eligibility", "Success metrics"]},
    {"num": 7, "title": "Machine-Readable Formats", "priority": "Ongoing*",
     "action": 3, "owner": 0, "kpi": 0, "detail": 0, "total": 3,
     "eu_align": 2, "missing": ["All details - completely underspecified"]},
]

missing_recommendations = [
    {"num": 8, "title": "Cybersecurity Framework", "priority": "High*",
     "eu_align": 9, "rationale": "Critical EU 2025 priority, completely absent from current recs"},
    {"num": 9, "title": "Sustainability Assurance", "priority": "Medium",
     "eu_align": 5, "rationale": "CSRD implementation gap, greenwashing risk"},
    {"num": 10, "title": "Governance Framework", "priority": "High",
     "eu_align": 4, "rationale": "Addresses governance challenge (Section 4.2)"},
]

print("=" * 100)
print("POLICY RECOMMENDATIONS QUALITY SCORECARD")
print("=" * 100)
print()

# Table header
print(f"{'#':<3} {'Recommendation':<30} {'Priority':<12} {'Action':<7} {'Owner':<7} {'KPI':<6} {'Detail':<7} {'Total':<6} {'EU Align':<9}")
print("-" * 100)

# Current recommendations
for rec in recommendations:
    priority_note = "*" if "*" in rec["priority"] else " "
    print(f"{rec['num']:<3} {rec['title']:<30} {rec['priority']:<12} "
          f"{rec['action']:>2}/10   {rec['owner']:>2}/10   {rec['kpi']:>2}/10  "
          f"{rec['detail']:>2}/10   {rec['total']:>2}/40  {rec['eu_align']:>2}/10")

print("-" * 100)

# Averages
avg_action = sum(r['action'] for r in recommendations) / len(recommendations)
avg_owner = sum(r['owner'] for r in recommendations) / len(recommendations)
avg_kpi = sum(r['kpi'] for r in recommendations) / len(recommendations)
avg_detail = sum(r['detail'] for r in recommendations) / len(recommendations)
avg_total = sum(r['total'] for r in recommendations) / len(recommendations)
avg_align = sum(r['eu_align'] for r in recommendations) / len(recommendations)

print(f"{'AVG':<3} {'(Current Recommendations)':<30} {'---':<12} "
      f"{avg_action:>4.1f}   {avg_owner:>4.1f}   {avg_kpi:>4.1f}  "
      f"{avg_detail:>4.1f}   {avg_total:>4.1f}  {avg_align:>4.1f}")

print()
print("* Priority should be changed (see detailed analysis)")
print()

print("=" * 100)
print("MISSING RECOMMENDATIONS")
print("=" * 100)
print()

for rec in missing_recommendations:
    priority_note = "*" if "*" in rec["priority"] else ""
    print(f"{rec['num']}. {rec['title']} (Priority: {rec['priority']}{priority_note})")
    print(f"   EU Alignment: {rec['eu_align']}/10")
    print(f"   Rationale: {rec['rationale']}")
    print()

print("=" * 100)
print("CRITICAL GAPS BY RECOMMENDATION")
print("=" * 100)
print()

for rec in recommendations:
    print(f"{rec['num']}. {rec['title']}")
    print(f"   Missing elements: {', '.join(rec['missing'])}")
    print()

print("=" * 100)
print("PRIORITY RECLASSIFICATION NEEDED")
print("=" * 100)
print()

print("Elevate to HIGH PRIORITY:")
print("- Rec 4 (AI Governance): Aligns with EU 2025 AI strategy, AI Act implementation timeline")
print("- Rec 7 (Formats): Time-critical decision for 2027 ESAP launch")
print("- Rec 8 (NEW - Cybersecurity): Top EU Digital Decade priority")
print()

print("Consider elevating to HIGH PRIORITY:")
print("- Rec 6 (SME Support): Prevent market distortion from day one")
print()

print("=" * 100)
print("IMPLEMENTATION READINESS ASSESSMENT")
print("=" * 100)
print()

implementation_ready = sum(1 for r in recommendations if r['total'] >= 25)
needs_minor_fixes = sum(1 for r in recommendations if 15 <= r['total'] < 25)
needs_major_fixes = sum(1 for r in recommendations if r['total'] < 15)

print(f"Implementation-ready (25+ points):  {implementation_ready}/7")
print(f"Needs minor fixes (15-24 points):   {needs_minor_fixes}/7")
print(f"Needs major fixes (<15 points):     {needs_major_fixes}/7")
print()

print("CRITICAL FINDING:")
print(f"0 out of 7 recommendations are implementation-ready")
print(f"All recommendations require significant strengthening")
print()

print("=" * 100)
print("TOP 5 IMPROVEMENTS NEEDED")
print("=" * 100)
print()

improvements = [
    ("1. ADD OWNERSHIP", "CRITICAL", "Average score 1.1/10 - Only 1 rec mentions stakeholders"),
    ("2. ADD CYBERSECURITY REC", "CRITICAL", "Completely missing despite EU priority"),
    ("3. ADD KPIs/METRICS", "HIGH", "Average score 2.9/10 - No measurable success criteria"),
    ("4. ADD IMPLEMENTATION DETAILS", "HIGH", "Average score 1.1/10 - No 'how' guidance"),
    ("5. ADD TIMELINES", "MEDIUM", "Only 2 of 7 have specific deadlines"),
]

for i, (improvement, severity, detail) in enumerate(improvements, 1):
    print(f"{i}. {improvement} (Severity: {severity})")
    print(f"   {detail}")
    print()

print("=" * 100)
print("CONCLUSION")
print("=" * 100)
print()
print("Current State:  Strong diagnostic analysis, weak prescriptive recommendations")
print("Recommendation: Apply systematic improvements from POLICY_RECOMMENDATIONS_REVIEW.md")
print()
print("Estimated effort to fix:")
print("- Critical gaps (ownership, cybersecurity):    4-6 hours")
print("- High priority gaps (KPIs, implementation):   8-10 hours")
print("- Medium priority gaps (timelines, budgets):   4-6 hours")
print("Total: 16-22 hours of policy drafting work")
print()
print("Expected outcome: Transform from academic analysis to policy implementation roadmap")
print("=" * 100)
