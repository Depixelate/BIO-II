"""Pictures for the illustrated quick-guides reading copy (Unit 3 on): slide figures and textbook figures as PNGs.

A slide figure is cut out of LibreOffice's rendering of a copy of the deck (the original stays untouched): the
crop is the box around the slide's pictures, so labels drawn on top of them come along. A textbook figure is a
region of a page of the textbook PDF (PDF page = book page + 19; 0-based index = book page + 18).
"""
import glob
import os
import shutil
import subprocess

import pymupdf
from pptx.enum.shapes import MSO_SHAPE_TYPE

import build_slide_notes as B

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = glob.glob(os.path.join(HERE, "..", "Official Textbook", "*.pdf"))
DPI = 200


def _pictures(shapes, dx=0, dy=0):
    """(left, top, right, bottom) in EMU of every picture on a slide, looking inside groups."""
    out = []
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            out += _pictures(sh.shapes)
        elif sh.shape_type == MSO_SHAPE_TYPE.PICTURE and sh.width and sh.height:
            out.append((sh.left, sh.top, sh.left + sh.width, sh.top + sh.height))
    return out


class Figures:
    def __init__(self, tmp, soffice, profile):
        self.tmp, self.soffice, self.profile = os.path.join(tmp, "figures"), soffice, profile
        os.makedirs(self.tmp, exist_ok=True)
        self.decks, self.pdfs = {}, {}

    def _deck_pdf(self, ch):
        if ch not in self.pdfs:
            deck = B.Deck(ch)
            copy = os.path.join(self.tmp, f"deck{ch}.pptx")
            shutil.copyfile(os.path.join(B.DECK_DIR, B.DECKS[ch]), copy)
            subprocess.run(["perl", "-e", "alarm 300; exec @ARGV", self.soffice, "--headless", "--norestore",
                            f"-env:UserInstallation=file://{self.profile}", "--convert-to", "pdf", "--outdir",
                            self.tmp, copy], capture_output=True, text=True)
            pdf = os.path.splitext(copy)[0] + ".pdf"
            if not os.path.exists(pdf):
                raise SystemExit(f"LibreOffice didn't render the Ch {ch} deck for the guide figures")
            self.decks[ch], self.pdfs[ch] = deck, pymupdf.open(pdf)
        return self.decks[ch], self.pdfs[ch]

    def slide(self, ch, n):
        """PNG of slide n's figure, as (path, width / height)."""
        deck, pdf = self._deck_pdf(ch)
        shown = [k for k in range(1, len(deck.prs.slides) + 1) if not deck.hidden(k)]   # hidden slides aren't rendered
        if n not in shown or len(shown) != len(pdf):
            raise SystemExit(f"{ch}.{n}: can't find the slide in the rendered deck")
        boxes = _pictures(deck.prs.slides[n - 1].shapes)
        if not boxes:
            raise SystemExit(f"{ch}.{n}: the slide has no picture for the guide")
        page = pdf[shown.index(n)]
        k = page.rect.width / deck.prs.slide_width
        clip = pymupdf.Rect(min(b[0] for b in boxes) * k, min(b[1] for b in boxes) * k,
                            max(b[2] for b in boxes) * k, max(b[3] for b in boxes) * k) & page.rect
        return self._save(page, clip, f"s{ch}_{n}.png")

    def book(self, page_no, clip):
        """PNG of a textbook figure: book page, crop box in PDF points."""
        if not BOOK:
            raise SystemExit("the textbook PDF isn't in Official Textbook/")
        if not hasattr(self, "_book"):
            self._book = pymupdf.open(BOOK[0])
        page = self._book[page_no + 18]
        return self._save(page, pymupdf.Rect(*clip) & page.rect, f"b{page_no}_{int(clip[1])}.png")

    def _save(self, page, clip, name):
        path = os.path.join(self.tmp, name)
        page.get_pixmap(dpi=DPI, clip=clip).save(path)
        return path, clip.width / clip.height
