#!/usr/bin/env python3
from pathlib import Path
import zipfile, shutil, json
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
shutil.rmtree(DIST, ignore_errors=True)
DIST.mkdir(parents=True, exist_ok=True)
COMMON_FILES=['README.md','README.zh-CN.md','install.md','LICENSE','VERSION','CHANGELOG.md','ROADMAP.md','release-notes.md','FINAL_VALIDATION_REPORT.md','CITATION.cff','SECURITY.md','SUPPORT.md','CONTRIBUTING.md','CODE_OF_CONDUCT.md','skill_manifest.json']

def should_skip(p):
    return ('__pycache__' in p.parts or p.suffix=='.pyc' or p.name=='.DS_Store' or p.suffix.lower()=='.pdf' or 'dist' in p.parts)
def add_tree(z, src, arc):
    if not src.exists(): return
    for p in sorted(src.rglob('*')):
        if p.is_file() and not should_skip(p): z.write(p, arc/p.relative_to(src))
def add_file(z, f, arc):
    f=Path(f)
    if f.exists() and f.is_file() and not should_skip(f): z.write(f, arc)
def zopen(name): return zipfile.ZipFile(DIST/name,'w',zipfile.ZIP_STORED,allowZip64=True)
def add_common(z, base):
    for f in COMMON_FILES: add_file(z,ROOT/f,base/f)
# Base distributions
with zopen('default-skills.zip') as z:
    base=Path('default-skills'); add_common(z,base)
    for d in ['skills','resources','templates','docs','scripts','.github']:
        add_tree(z,ROOT/d,base/d)
with zopen('compact-suite.zip') as z:
    base=Path('compact-suite'); add_common(z,base)
    for suite in (ROOT/'skills').glob('*skill-suite'):
        if suite.is_dir(): add_tree(z,suite,base/'skills'/suite.name)
    for d in ['resources','templates','docs','scripts','.github']:
        add_tree(z,ROOT/d,base/d)
with zopen('advanced-skills.zip') as z:
    base=Path('advanced-skills'); add_common(z,base)
    for d in ['skills-advanced','resources','templates','docs','scripts']:
        add_tree(z,ROOT/d,base/d)
with zopen('full-suite.zip') as z:
    base=Path('full-suite'); add_common(z,base)
    for d in ['skills','skills-advanced','resources','templates','evals','docs','plugins','expansion_packs','presets','scripts','paper_templates','.github','tests']:
        add_tree(z,ROOT/d,base/d)
# Plugins
for plug in ['default','compact']:
    with zopen(f'plugin-{plug}.zip') as z:
        base=Path(f'plugin-{plug}')
        add_tree(z,ROOT/'plugins'/plug,base)
        if plug=='default': add_tree(z,ROOT/'skills',base/'skills')
        else:
            for suite in (ROOT/'skills').glob('*skill-suite'):
                if suite.is_dir(): add_tree(z,suite,base/'skills'/suite.name)
        for d in ['resources','templates','docs','scripts']:
            add_tree(z,ROOT/d,base/d)
# Expansion packs
if (ROOT/'expansion_packs').exists():
    with zopen('expansion-packs.zip') as z:
        base=Path('expansion-packs'); add_tree(z,ROOT/'expansion_packs',base/'expansion_packs'); add_tree(z,ROOT/'resources',base/'resources')
    for pack in sorted((ROOT/'expansion_packs').iterdir()):
        if pack.is_dir():
            with zopen(f'expansion-pack-{pack.name}.zip') as z:
                base=Path(f'expansion-pack-{pack.name}'); add_tree(z,pack,base/'expansion_packs'/pack.name); add_tree(z,ROOT/'resources',base/'resources')
# Presets and preset scenarios
if (ROOT/'presets').exists():
    with zopen('presets.zip') as z:
        base=Path('presets'); add_tree(z,ROOT/'presets',base/'presets'); add_tree(z,ROOT/'resources',base/'resources')
    with zopen('preset-scenarios.zip') as z:
        base=Path('preset-scenarios')
        for pack in sorted((ROOT/'presets').iterdir()):
            if pack.is_dir():
                for d in ['scenarios','sample-outputs','route-traces']:
                    add_tree(z,pack/d,base/'presets'/pack.name/d)
                add_file(z,pack/'evaluation-report.md',base/'presets'/pack.name/'evaluation-report.md')
    for pack in sorted((ROOT/'presets').iterdir()):
        if pack.is_dir():
            with zopen(f'preset-{pack.name}.zip') as z:
                base=Path(f'preset-{pack.name}'); add_tree(z,pack,base/'presets'/pack.name); add_tree(z,ROOT/'resources',base/'resources')
            with zopen(f'preset-scenarios-{pack.name}.zip') as z:
                base=Path(f'preset-scenarios-{pack.name}')
                for d in ['scenarios','sample-outputs','route-traces']:
                    add_tree(z,pack/d,base/'presets'/pack.name/d)
                add_file(z,pack/'evaluation-report.md',base/'presets'/pack.name/'evaluation-report.md')
# Source maintenance packages
with zopen('source-maintenance.zip') as z:
    base=Path('source-maintenance')
    for rel in ['scripts/check_official_links_live.py','scripts/report_stale_sources.py','scripts/live_source_check_matrix.py','scripts/source_age_policy.py','scripts/release_health_dashboard.py','scripts/generate_source_badges.py','scripts/validate_release_health.py','resources/source_refresh_report.json','resources/source_refresh_report.yaml','resources/stale_source_report.json','resources/stale_source_report.md','resources/live_source_check_matrix.json','resources/live_source_check_matrix.yaml','resources/source_age_policy_report.json','resources/source_age_policy_report.yaml','resources/release_health_dashboard.json','resources/release_health_dashboard.yaml','resources/source_badges.json','resources/source_badges.yaml','resources/source_update_changelog.md','resources/official_source_update_changelog.md','.github/workflows/source-refresh.yml','docs/live-source-checks.html','docs/source-aging-policy.html','docs/release-health-dashboard.html']:
        add_file(z,ROOT/rel,base/rel)
with zopen('source-trust-review.zip') as z:
    base=Path('source-trust-review')
    for rel in ['scripts/classify_source_trust.py','scripts/build_human_review_queue.py','scripts/validate_source_trust.py','scripts/review_queue_report.py','resources/source_trust_tiers.json','resources/source_trust_tiers.yaml','resources/human_review_queue.json','resources/human_review_queue.yaml','resources/source_review_report.json','resources/source_review_report.yaml','docs/source-trust-tiers.html','docs/human-review-queue.html','docs/source-review-workflow.html']:
        add_file(z,ROOT/rel,base/rel)
with zopen('source-policy-diff.zip') as z:
    base=Path('source-policy-diff')
    for rel in ['scripts/snapshot_official_sources.py','scripts/diff_source_snapshots.py','scripts/policy_diff_report.py','scripts/affected_fragments.py','scripts/validate_policy_diff.py','resources/source_snapshots','resources/policy_diff_report.json','resources/policy_diff_report.yaml','resources/official_source_change_log.json','resources/official_source_change_log.yaml','resources/affected_fragments_report.json','resources/affected_fragments_report.yaml','docs/policy-diff-dashboard.html','docs/source-snapshots.html','docs/affected-fragments.html']:
        p=ROOT/rel
        if p.is_dir(): add_tree(z,p,base/rel)
        else: add_file(z,p,base/rel)
with zopen('visual-assets.zip') as z:
    base=Path('visual-assets')
    for rel in ['paper_templates/extracted_visual_assets','scripts/extract_visual_assets.py','scripts/validate_visual_assets.py','docs/visual-assets-gallery.html']:
        p=ROOT/rel
        if p.is_dir(): add_tree(z,p,base/rel)
        else: add_file(z,p,base/rel)

def make_pack(name, rels):
    with zopen(name) as z:
        base=Path(name).with_suffix('')
        for rel in rels:
            p=ROOT/rel
            if p.is_dir():
                add_tree(z,p,base/rel)
            else:
                add_file(z,p,base/rel)

make_pack('main-figure-site.zip', [
    'main_figure_site',
    'docs/main-figure-gallery.html',
    'docs/multimodal-rag-corpus.html',
    'docs/rag-trace-ui.html',
])
make_pack('main-figure-100-workflow.zip', [
    'main_figure_site/data/candidate_papers_100.json',
    'main_figure_site/data/candidate_papers_100.yaml',
    'main_figure_site/data/oa_source_review_report.json',
    'main_figure_site/data/main_figure_extraction_tasks.json',
    'main_figure_site/data/extraction_readiness_dashboard.json',
    'main_figure_site/data/extraction_ready_candidates.json',
    'main_figure_site/scripts',
    'docs/oa-main-figure-candidates.html',
    'docs/extraction-readiness-dashboard.html',
])
make_pack('main-figure-rag-roadmap.zip', [
    'main_figure_rag_roadmap',
    'docs/main-figure-rag-roadmap.html',
])
make_pack('source-discovery-preflight.zip', [
    'main_figure_site/data/source_discovery_candidates.json',
    'main_figure_site/data/source_discovery_candidates.yaml',
    'main_figure_site/data/doi_license_preflight_report.json',
    'main_figure_site/data/doi_license_preflight_report.yaml',
    'main_figure_site/data/candidate_risk_scores.json',
    'main_figure_site/data/source_discovery_review_queue.json',
    'main_figure_site/scripts/discover_oa_candidate_sources.py',
    'main_figure_site/scripts/doi_license_preflight.py',
    'main_figure_site/scripts/validate_source_discovery.py',
    'docs/source-discovery-candidates.html',
    'docs/doi-license-preflight.html',
])
make_pack('evidence-cards.zip', [
    'main_figure_site/data/candidate_evidence_cards',
    'main_figure_site/data/metadata_connector_plan.json',
    'main_figure_site/data/metadata_connector_plan.yaml',
    'main_figure_site/scripts/build_candidate_evidence_cards.py',
    'main_figure_site/scripts/validate_candidate_evidence.py',
    'docs/candidate-evidence-cards.html',
    'docs/metadata-connectors.html',
])
make_pack('evidence-promotion.zip', [
    'main_figure_site/data/evidence_promotion_queue.json',
    'main_figure_site/data/evidence_promotion_queue.yaml',
    'main_figure_site/data/evidence_promotion_validation_report.json',
    'main_figure_site/data/evidence_promotion_validation_report.yaml',
    'main_figure_site/data/human_reviewer_decision_log.json',
    'main_figure_site/data/extraction_ready_candidates.json',
    'main_figure_site/data/rag_ready_metadata_candidates.json',
    'main_figure_site/scripts/evidence_promotion_queue.py',
    'main_figure_site/scripts/validate_evidence_promotion.py',
    'docs/evidence-promotion-queue.html',
    'docs/human-reviewer-decision-log.html',
])
make_pack('rag-governance.zip', [
    'main_figure_site/data/rag_ingestion_governance.json',
    'main_figure_site/data/rag_entry_eligibility_report.json',
    'main_figure_site/data/rag_retrieval_benchmark.json',
    'main_figure_site/data/rag_safety_filter_report.json',
    'main_figure_site/data/rag_quality_dashboard.json',
    'main_figure_site/scripts/rag_ingestion_governance.py',
    'main_figure_site/scripts/rag_entry_eligibility.py',
    'main_figure_site/scripts/rag_safety_filter.py',
    'main_figure_site/scripts/rag_quality_dashboard.py',
    'main_figure_site/scripts/validate_rag_governance.py',
    'docs/rag-ingestion-governance.html',
    'docs/rag-entry-eligibility.html',
    'docs/rag-quality-dashboard.html',
])
make_pack('rag-evaluation.zip', [
    'main_figure_site/data/visual_query_benchmark.json',
    'main_figure_site/data/expected_retrieval_results.json',
    'main_figure_site/data/human_retrieval_eval_traces.json',
    'main_figure_site/data/retrieval_failure_taxonomy.json',
    'main_figure_site/data/query_tag_coverage_matrix.json',
    'main_figure_site/data/rag_evaluator_report.json',
    'main_figure_site/scripts/validate_visual_query_benchmark.py',
    'docs/visual-query-benchmark.html',
    'docs/human-retrieval-evaluation.html',
    'docs/rag-evaluator-report.html',
])
make_pack('rag-trace-ui.zip', [
    'main_figure_site/data/rag_trace_ui_index.json',
    'main_figure_site/data/visual_query_debug_traces.json',
    'main_figure_site/data/query_rewrite_suggestions.json',
    'main_figure_site/data/missing_tag_coverage_report.json',
    'main_figure_site/data/corpus_expansion_recommendations.json',
    'main_figure_site/data/human_eval_dashboard.json',
    'main_figure_site/scripts/build_rag_trace_ui_index.py',
    'main_figure_site/scripts/visual_query_debugger.py',
    'main_figure_site/scripts/validate_rag_trace_ui.py',
    'docs/rag-trace-ui.html',
    'docs/visual-query-debugger.html',
    'docs/human-eval-dashboard.html',
])
make_pack('section-routines.zip', [
    'resources/section_routine_library.json',
    'resources/experiment_organization_library.json',
    'resources/formula_organization_library.json',
    'resources/motivation_organization_library.json',
    'resources/limitations_future_work_library.json',
    'resources/conclusion_organization_library.json',
    'docs/section-routine-library.html',
])
make_pack('visual-patterns.zip', [
    'resources/visual_rhetoric_report.json',
    'resources/figure_pattern_library.json',
    'resources/table_pattern_library.json',
    'resources/caption_pattern_library.json',
    'resources/visual_style_dashboard.json',
    'docs/visual-rhetoric-analyzer.html',
    'docs/figure-pattern-library.html',
    'docs/table-pattern-library.html',
    'docs/caption-pattern-library.html',
])
print(json.dumps({'dist':str(DIST),'zip_count':len(list(DIST.glob('*.zip')))},indent=2))
