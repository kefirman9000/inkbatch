# InkBatch

Sign every page of a PDF in one click. InkBatch runs entirely in your browser and works offline. Your documents are never uploaded anywhere.

## Use it

- **Online:** open the GitHub Pages link for this repo (see *Hosting* below), or
- **Offline:** download [`index.html`](index.html) and double-click it.

Then drop a PDF onto the window and click **⚡ Sign everything**.

## What it does

- **Sign everything in one click.** Finds your signature, finds every blank signature line, signs them all, and downloads `yourfile-signed.pdf`.
- **Auto-sign on drop.** Turn on *Auto-sign when I drop a PDF* and dropping the file is the only step.
- **Your signature, your way.**
  - *Find my signature in this PDF* copies it from a line you've already signed (for example page 1). Underlines and printed labels are removed automatically.
  - *Pick from a page*: click on a signature, or drag a box around it.
  - Upload a PNG or JPG, or draw one with your mouse.
  - Signatures are saved in your browser for next time.
- **Batch control.** Tick pages individually or use *Check all*. *Find signature lines* auto-checks pages with lines like `Signature: ______`, and skips lines that are already signed.
- **Fine-tune placement.** Click any page to drag or resize the signature, add more signatures, or copy one placement to every checked page.
- Handles rotated pages. Your original file is never changed.

## Limits

- Auto-detect relies on the PDF's text (e.g. `Signature ____`). Scanned PDFs won't be auto-detected; tick those pages and place the signature by hand.
- The signature is stamped as an image, like a pasted ink signature. It is **not** a cryptographic digital signature.
- Always review the signed file before sending it.

## Hosting on GitHub Pages

Settings → Pages → *Deploy from a branch* → `main` / `(root)` → Save. The app will be at `https://kefirman9000.github.io/inkbatch/`.

## Development

`index.html` is a build artifact: the source is `src/inkbatch.src.html`, and the build inlines [pdf.js](https://github.com/mozilla/pdf.js) and [pdf-lib](https://github.com/Hopding/pdf-lib) so the app works offline as a single file.

```sh
npm install
npm run build   # writes index.html
```

## License

MIT. Bundles pdf.js (Apache-2.0) and pdf-lib (MIT).
