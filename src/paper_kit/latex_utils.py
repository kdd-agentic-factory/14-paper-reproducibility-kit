import re


def escape_latex(text: str) -> str:
    special = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
                "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}",
                "^": r"\textasciicircum{}", "\\": r"\textbackslash{}"}
    pattern = re.compile("|".join(re.escape(k) for k in special))
    return pattern.sub(lambda m: special[m.group()], text)


def wrap_verbatim(text: str) -> str:
    return f"\\verb|{text}|"
