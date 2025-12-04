# Technical Accuracy Verification Report
## European Financial Data Space White Paper
**Verification Date:** December 04, 2025

## Executive Summary
- **Total Errors Found:** 3
  - High Severity: 1
  - Medium Severity: 1
  - Low Severity: 1
- **Claims Verified:** 18
- **Warnings:** 3

## Factual Errors and Corrections

### High Severity (1)

#### 1. ESMA's Role in Standardizing Electronic Reporting

**Claim in Paper:**
> In October 2025, ESMA published a latest updated ESEF Reporting Manual

**Issue:**
The date 'October 2025' appears to be incorrect. According to ESMA's website, the latest ESEF Reporting Manual was published on July 11, 2024, not October 2025.

**Correction:**
Change to: 'In July 2024, ESMA published the latest updated ESEF Reporting Manual' or remove the specific month if referring to a planned future update.

**Sources:**
- https://www.esma.europa.eu/press-news/esma-news/esma-publishes-2024-esef-reporting-manual
- https://www.esma.europa.eu/sites/default/files/library/esma32-60-254_esef_reporting_manual.pdf

### Medium Severity (1)

#### 1. ESAP Implementation Roadmap

**Claim in Paper:**
> Jan 2026: ESAP begins collecting information; prototype phase (6 months minimum)

**Issue:**
This timeline is partially misleading. According to the ESAP regulation, ESAP should only provide access to information submitted as from January 1, 2026, but collection by ESAP begins July 10, 2026. The 6-month prototype phase occurs before July 2026.

**Correction:**
Clarify: 'The prototype phase (minimum 6 months) precedes the July 10, 2026 collection start date. ESAP will only provide access to information submitted from January 1, 2026 onwards, but the actual collection by ESAP from collection bodies begins July 10, 2026.'

**Sources:**
- https://www.esma.europa.eu/press-news/esma-news/esas-finalise-rules-facilitate-access-financial-and-sustainability-information
- https://www.amf-france.org/en/news-publications/news/european-single-access-point-financial-and-non-financial-information-european-entities-esap-enters

### Low Severity (1)

#### 1. ESAP Implementation Roadmap

**Claim in Paper:**
> Dec 2025: ESMA to provide minimum portal functionalities (user-friendly web interface)

**Issue:**
The timeline states this should be completed by December 2025, but the regulation specifies 'by 31 December 2025' with completion 'by 31 December 2026'. This is a two-phase process that should be clarified.

**Correction:**
Revise to: 'By 31 December 2025: ESMA should ensure ESAP provides minimum portal functionalities (user-friendly web interface), to be completed by 31 December 2026.'

**Sources:**
- https://www.linkedin.com/pulse/update-european-single-access-point-esap-philipp-rosenauer
- https://accountancyeurope.eu/wp-content/uploads/2024/06/ESAP-factsheet.pdf

## Warnings and Ambiguities

1. FIDA expected agreement 'late 2025/early 2026' - This is reasonable based on sources, though exact timeline remains uncertain. Denmark is pushing for year-end 2025 completion.
2. The paper mentions 'minimum portal functionalities' but doesn't list all eight specific functionalities required by regulation (web portal, API, search, viewer, translation, download, notification, voluntary/mandatory distinction). Consider adding complete list for technical accuracy.
3. The paper states 'December 2024' as the original ESAP establishment deadline (missed). This should specify it was the deadline for ESMA to 'establish' ESAP, not for it to be fully operational.

## Verified Claims (Accurate)

1. ESAP publication begins July 2027 (specifically July 10, 2027) - VERIFIED
2. ESAs published final ITS for collection bodies in October 2024 (October 29, 2024) - VERIFIED
3. Full ESAP functionality expected by 2030 (January 10, 2030) - VERIFIED
4. First FIDA trilogue in April 2025 - VERIFIED
5. Denmark assumed EU Council presidency in July 2025 (July 1, 2025) - VERIFIED
6. Commission non-paper on May 16, 2025 proposing Big Tech exclusion - VERIFIED
7. FIDA implementation phases: Stage 1 (24 months), Stage 2 (36 months), Stage 3 (48 months) - VERIFIED
8. Stage 1: Consumer credit, savings accounts, motor insurance - VERIFIED
9. Stage 2: Mortgage loans, investments, crypto-assets, personal pensions - VERIFIED
10. Stage 3: Credit ratings, non-life insurance - VERIFIED
11. ESEF Reporting Manual guidance on dashes and empty fields (Guidance 2.2.5) - VERIFIED as type of guidance ESMA provides
12. Anchoring of extension elements guidance (Guidance 1.4.1) - VERIFIED as type of guidance ESMA provides
13. XML, JSON, XBRL mentioned as machine-readable formats for ESAP - VERIFIED
14. Inline XBRL (iXBRL) used for ESEF - VERIFIED
15. No single format suitable for all disclosure types - VERIFIED (ESMA acknowledges this)
16. ITS specify tasks for collection bodies including submission timing, validation checks, and metadata - VERIFIED
17. Collection bodies include OAMs, national authorities, EU offices - VERIFIED
18. Industry joint statement on December 9, 2024 from financial associations (AFME, EACB, EBF, EFAMA, ESBG, Insurance Europe) - VERIFIED

## Country Authorities Table Verification

The paper includes a table listing ESEF report dissemination authorities for EU countries.

**Status:** The table lists 27 countries, which matches the current EU membership (as of 2025).

**Countries Listed:** Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden

**Verification Notes:**
- All 27 EU member states are included
- Portal names appear generally accurate but should be verified individually
- Some portal names may have changed since publication - recommend checking ESMA's official OAM list
- The note correctly states that every EU country must comply with ESEF
