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

BASE_TYPE = "sign"
CONDENSE_TYPE = "tablet"

NONE_VALUES = {None}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {"lex"}

EXAMPLE_SECTION = "<code>P005381</code>"
EXAMPLE_SECTION_TEXT = "P005381"

SECTION_SEP1 = " "
SECTION_SEP2 = ":"

WRITING = ""
WRITING_DIR = "ltr"

FONT_NAME = None
FONT = None
FONTW = None

TEXT_FORMATS = {}

BROWSE_NAV_LEVEL = 1
BROWSE_CONTENT_PRETTY = True

VERSE_TYPES = None

LEX = None


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


TRANSFORM = dict(
    column=dict(prime=prime),
    line=dict(prime=prime),
    case=dict(prime=prime),
    cluster={'type': ctype},
)

CHILD_TYPE = dict(
    tablet={"face", "comment"},
    face={"column", "comment"},
    column={"line", "comment"},
    line={"sign", "quad", "cluster", "comment"},
    case={"sign", "quad", "cluster", "comment"},
    cluster={"sign", "quad", "cluster"},
    quad={"sign", "quad", "cluster"},
)

SUPER_TYPE = None

PLAIN_TYPES = dict(
    sign=(None, False),
    quad=(None, False),
    cluster=(None, False),
    line=("{number}{prime}. ", True),
    case=("{number}{prime}. ", True),
    column=("{otype} {number}{prime}", False),
    face=("{otype} {type}", False),
    tablet=("{otype} {catalogId}", False),
)

PRETTY_TYPES = dict(
    tablet=("{catalogId}", "name period excavation", ""),
    face=("{type}", "identifer fragment", ""),
    column=("{number}{prime}", "", ""),
    line=("{number}{prime}", "", ""),
    case=("{number}{prime}", "", ""),
    comment=("{type}", "", "text"),
    cluster=("{type}", "", ""),
    quad=("", "", ""),
    sign=("", "", ""),
)

LEVELS = dict(
    tablet=dict(level=3, flow="row", wrap=False, stretch=False),
    face=dict(level=3, flow="row", wrap=False, strectch=False),
    column=dict(level=3, flow="col", wrap=False, strectch=False),
    line=dict(level=2, flow="row", wrap=False, strectch=False),
    case=dict(level=2, flow="row", wrap=False, strectch=False),
    cluster=dict(level=2, flow="row", wrap=True, strectch=False),
    quad=dict(level=1, flow="row", wrap=True, strectch=False),
    sign=dict(level=0, flow="col", wrap=False, strectch=False),
)

INTERFACE_DEFAULTS = dict(
    lineNumbers=False,
    graphics=True,
)

LINE_NUMBERS = dict(
    case="srcLnNum",
    line="srcLnNum",
    comment="srcLnNum",
    column="srcLnNum",
    face="srcLnNum",
    tablet="srcLnNum",
)

GRAPHICS = dict(sign=True, quad=True)


def deliver():
    return (globals(), dirname(abspath(__file__)))
