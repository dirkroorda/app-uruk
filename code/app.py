from tf.applib.helpers import dh
from tf.applib.app import loadModule
from tf.applib.api import setupApi


def notice(app):
    if int(app.api.TF.version.split(".")[0]) <= 7:
        print(
            f"""
Your Text-Fabric is outdated.
It cannot load this version of the TF app `{app.appName}`.
Recommendation: upgrade Text-Fabric to version 8.
Hint:

    pip3 install --upgrade text-fabric

"""
        )


class TfApp(object):
    def __init__(app, *args, silent=False, **kwargs):
        atf = loadModule(*args[0:2], "atf")
        atf.atfApi(app)
        app.image = loadModule(*args[0:2], "image")
        setupApi(app, *args, silent=silent, **kwargs)
        notice(app)

        app.image.getImagery(app, silent, checkout=kwargs.get("checkout", ""))

        api = app.api
        F = api.F
        E = api.E

        ac = app.context

        def getOp(ch):
            result = ""
            nextChildren = E.op.f(ch)
            if nextChildren:
                op = nextChildren[0][1]
                result = f'<div class="op">{op}</div>'
            return result

        ac.childrenCustom.clear()
        ac.childrenCustom.update(
            line=((lambda x: not F.terminal.v(x)), E.sub.f, False),
            case=((lambda x: not F.terminal.v(x)), E.sub.f, False),
            quad=((lambda x: True), E.sub.f, False),
        )
        ac.afterChild.clear()
        ac.afterChild.update(quad=getOp)
        ac.plainCustom.clear()
        ac.plainCustom.update(
            sign=atf.plainAtfType,
            quad=atf.plainAtfType,
            cluster=atf.plainAtfType,
        )
        ac.prettyCustom.clear()
        ac.prettyCustom.update(
            case=caseDir, cluster=clusterBoundaries, comments=commentsCls
        )

    def cdli(app, n, linkText=None, asString=False):
        (nType, objectType, identifier) = app.image.imageCls(app, n)
        if linkText is None:
            linkText = identifier
        result = app.image.wrapLink(linkText, objectType, "main", identifier)
        if asString:
            return result
        else:
            dh(result)

    # PRETTY HELPERS

    def getGraphics(app, n, nType, outer):
        api = app.api
        F = api.F
        E = api.E

        result = ""

        isOuter = outer or (all(F.otype.v(parent) != "quad" for parent in E.sub.t(n)))
        if isOuter:
            width = "2em" if nType == "sign" else "4em"
            height = "4em" if nType == "quad" else "6em"
            theGraphics = app.image.getImages(
                app,
                n,
                kind="lineart",
                width=width,
                height=height,
                _asString=True,
                withCaption=False,
                warning=False,
            )
            if theGraphics:
                result = f"<div>{theGraphics}</div>"

        return result

    def lineart(app, ns, key=None, asLink=False, withCaption=None, **options):
        return app.image.getImages(
            app,
            ns,
            kind="lineart",
            key=key,
            asLink=asLink,
            withCaption=withCaption,
            **options,
        )

    def photo(app, ns, key=None, asLink=False, withCaption=None, **options):
        return app.image.getImages(
            app,
            ns,
            kind="photo",
            key=key,
            asLink=asLink,
            withCaption=withCaption,
            **options,
        )

    def imagery(app, objectType, kind):
        return set(app._imagery.get(objectType, {}).get(kind, {}))


def caseDir(app, n, nType, cls):
    api = app.api
    F = api.F

    wrap = app.levels[nType]["wrap"]
    flow = "col" if F.depth.v(n) & 1 else "row"
    cls.update(dict(children=f"children {flow} {wrap}"))


def clusterBoundaries(app, n, nType, cls):
    lbl = cls.pop("label")
    cls.update(dict(labelb=f"{lbl} {nType}b", labele=f"{lbl} {nType}e"))
    cls["container"] += f" {nType}"


def commentsCls(app, n, nType, cls):
    cls["container"] += f" {nType}"
