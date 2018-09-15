# Ukebook Scratchpad

## Formatting Experiment

Python tool for taking raw songs, and converting them to the Uke Wednesdays format. The hope is to prove that songs can be formatted totally automatically to fit on one page, including font-size and chord diagrams.

### Quickstart

1. Install wkhtmltopdf, the webkit-based pdf rendering engine used by pdfkit:

    ```
    sudo apt-get install wkhtmltopdf
    ```

2. If you need to use a virtual X server, follow these instructions https://github.com/JazzCore/python-pdfkit/wiki/Using-wkhtmltopdf-without-X-server

3. I'm using Conda to manage my python envionments. You can too, with this:

    ```
    conda create -n form-exp
    . activate form-exp
    ```

3. Install dependencies
    ```
    pip install -r requirements.txt
    ```

4. To run the demo:

    ```
    python song_to_pdf.py
    ```

This should result in a song from the songs directory being formatting, and written out as both out.html and out.pdf.


### Tests
#### Unit
```
python -m unittest
```

#### Integration
To be thought about. Good puzzle.

