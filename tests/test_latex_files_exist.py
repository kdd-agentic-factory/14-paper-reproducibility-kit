from pathlib import Path


def test_main_tex_exists():
    assert Path("paper/main.tex").exists()


def test_abstract_exists():
    assert Path("paper/abstract.tex").exists()


def test_required_sections_exist():
    sections = [
        "01-introduction.tex",
        "02-related-work.tex",
        "03-architecture.tex",
        "04-kdd-governance-model.tex",
        "05-agentic-workflows.tex",
        "09-experimental-methodology.tex",
        "10-results.tex",
        "12-threats-to-validity.tex",
        "14-conclusion.tex",
    ]
    for section in sections:
        assert Path("paper/sections", section).exists(), f"Missing: {section}"


def test_required_appendices_exist():
    appendices = [
        "appendix-a-repository-organization.tex",
        "appendix-e-reproducibility-protocol.tex",
        "appendix-f-experiment-configurations.tex",
    ]
    for appendix in appendices:
        assert Path("paper/appendices", appendix).exists(), f"Missing: {appendix}"


def test_bibliography_exists():
    assert Path("paper/bibliography/references.bib").exists()
    assert Path("paper/bibliography/software.bib").exists()


def test_style_files_exist():
    assert Path("paper/style/macros.tex").exists()
    assert Path("paper/style/notation.tex").exists()
