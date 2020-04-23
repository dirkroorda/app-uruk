from os.path import dirname, abspath

API_VERSION = 1

PROTOCOL = "http://"
HOST = "localhost"
PORT = dict(kernel=18984, web=8104)

ORG = "Nino-cunei"
REPO = "uruk"
CORPUS = "Uruk IV/III: Proto-cuneiform tablets "
VERSION = "1.0"
RELATIVE = f"tf/{REPO}"
RELATIVE_IMAGES = "sources/cdli/images"

DOI_TEXT = "10.5281/zenodo.1193841"
DOI_URL = "https://doi.org/10.5281/zenodo.1193841"

DOC_URL = f"https://github.com/{ORG}/{REPO}/blob/master/docs/"
DOC_INTRO = "about.md"
CHAR_URL = f"https://github.com/{ORG}/{REPO}/blob/master/docs/transcription.md"
CHAR_TEXT = "How TF features represent ATF"

FEATURE_URL = f"{DOC_URL}/transcription.md"

MODULE_SPECS = ()

ZIP = [REPO, (ORG, REPO, RELATIVE_IMAGES)]

EXAMPLE_SECTION = "<code>P005381</code>"
EXAMPLE_SECTION_TEXT = "P005381"

DATA_DISPLAY = dict(browseNavLevel=1, browseContentPretty=True,)


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
    comment=dict(template="{type}", featuresBare="text", lineNumber="srcLnNum",),
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
    sign=dict(graphics=True,),
)

INTERFACE_DEFAULTS = dict(lineNumbers=False, graphics=True,)


def deliver():
    return (globals(), dirname(abspath(__file__)))
