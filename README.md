# QR Coder
A simple QR code generator command line tool.

## Setup
Clone this repo in to the directory of your choice. 

Open a Linix style terminal (if you're on Windows, use WSL) and create a virtual environment:
```
python -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Make the program executable:
```
chmod +x ./qr_coder.py
```

Use your text editor to ensure the line endings are `LF` rather than `CRLF`.

## Usage
Run the program with optional outputs:
- `-svg` outputs an SVG file
- `-png` outputs a PNG file

## Examples:

Print the URL to the console and output both SVG and PNG
```
./qr_coder.py -svg -png http://www.terranautbeer.com/ 
```

Print the URL to the console and output a PNG
```
./qr_coder.py -png http://www.terranautbeer.com/ 
```

Print the URL to the console and output an SVG
```
./qr_coder.py -svg http://www.terranautbeer.com/ 
```

Only print the URL to the console
```
./qr_coder.py http://www.terranautbeer.com/ 
```
