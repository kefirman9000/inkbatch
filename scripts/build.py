"""Build index.html: inline pdf.js, its worker and pdf-lib into src/inkbatch.src.html so the app works offline as one file.
Run `npm install` first, then `npm run build`."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
nm = root / 'node_modules'
src = (root / 'src/inkbatch.src.html').read_text()
pdfjs = (nm / 'pdfjs-dist/build/pdf.min.js').read_text()
worker = (nm / 'pdfjs-dist/build/pdf.worker.min.js').read_text()
pdflib = (nm / 'pdf-lib/dist/pdf-lib.min.js').read_text()
for name, code in (('pdf.js', pdfjs), ('pdf.worker.js', worker), ('pdf-lib', pdflib)):
    assert '</script' not in code.lower(), f'{name} contains </script and cannot be inlined'
libs = (f'<script>{pdfjs}</script>\n<script>{pdflib}</script>\n'
        f'<script type="text/plain" id="pdfjs-worker">{worker}</script>')
(root / 'index.html').write_text(src.replace('<!--LIBS-->', libs))
print('Built index.html')
