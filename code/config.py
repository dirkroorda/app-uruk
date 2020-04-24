from os.path import dirname, abspath

API_VERSION = 1

PROVENANCE_SPEC = dict(
    org="Nino-cunei",
    repo="uruk",
    version="1.0",
    relative=f"tf/uruk",
    graphics="sources/cdli/images",
    doi="10.5281/zenodo.1193841",
    corpus="Uruk IV/III: Proto-cuneiform tablets ",
    webBase="https://cdli.ucla.edu",
    webUrl="/search/search_results.php?SearchMode=Text&ObjectID=<1>",
    webHint="to CDLI main page for this tablet",
)

DOCS = dict(
    docPage="about", featureBase="{docBase}/transcription{docExt}", featurePage=""
)

DATA_DISPLAY = dict(browseNavLevel=1, browseContentPretty=True)


def prime(p):
    return "'" * p if p else ""


def ctype(t):
    if t == "uncertain":
        return "?"
    elif t == "properName":
        return "="
    elif t == "supplied":
        return "&gt;"
    else:
        return ""


TYPE_DISPLAY = dict(
    tablet=dict(
        featuresBare="name period excavation",
        childrenPlain=False,
        children={"face", "comment"},
        condense=True,
        lineNumber="srcLnNum",
        flow="row",
        wrap=False,
        stretch=False,
    ),
    face=dict(
        template="{otype} {type}",
        featuresBare="identifer fragment",
        childrenPlain=False,
        children={"column", "comment"},
        lineNumber="srcLnNum",
        flow="row",
        wrap=False,
        stretch=False,
    ),
    column=dict(
        childrenPlain=False,
        children={"line", "comment"},
        transform=dict(prime=prime),
        lineNumber="srcLnNum",
        level=3,
        flow="col",
    ),
    line=dict(
        children={"sign", "quad", "cluster", "comment"},
        transform=dict(prime=prime),
        lineNumber="srcLnNum",
        level=2,
        flow="row",
        wrap=False,
        stretch=False,
    ),
    case=dict(
        template="{number}{prime}",
        children={"sign", "quad", "cluster", "comment"},
        transform=dict(prime=prime),
        lineNumber="srcLnNum",
        level=2,
        flow="row",
        wrap=False,
        stretch=False,
    ),
    comment=dict(template="{type}", featuresBare="text", lineNumber="srcLnNum"),
    cluster=dict(
        template="{type}",
        childrenPlain=False,
        children={"sign", "quad", "cluster"},
        transform=dict(type=ctype),
        stretch=False,
    ),
    quad=dict(
        childrenPlain=False,
        children={"sign", "quad", "cluster"},
        graphics=True,
        stretch=False,
    ),
    sign=dict(graphics=True),
)

INTERFACE_DEFAULTS = dict(lineNumbers=False, showGraphics=True)


def deliver():
    return (globals(), dirname(abspath(__file__)))
