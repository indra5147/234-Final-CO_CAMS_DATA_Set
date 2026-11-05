#!/usr/bin/env python3
"""Validate every original source file in an extracted SDN-PQC master archive.
Run from any directory: python 00_MASTER_INDEX/VERIFY_EXTRACTED_ARCHIVE.py
Does not execute experiments or modify data.
"""
from pathlib import Path
import csv, hashlib, sys
root=Path(__file__).resolve().parent.parent
manifest=root/'00_MASTER_INDEX'/'FILE_MANIFEST_SHA256.csv'
errors=[]
with manifest.open(newline='',encoding='utf-8') as f:
    records=list(csv.DictReader(f))
for i,r in enumerate(records,1):
    path=root/r['archive_relative_path']
    if not path.is_file():errors.append(f'MISSING: {r["archive_relative_path"]}');continue
    if path.stat().st_size != int(r['bytes']):errors.append(f'SIZE: {r["archive_relative_path"]}');continue
    h=hashlib.sha256()
    with path.open('rb') as inp:
        for block in iter(lambda:inp.read(1<<20),b''):h.update(block)
    if h.hexdigest()!=r['sha256']:errors.append(f'HASH: {r["archive_relative_path"]}')
print(f'Checked {len(records)} original source files; failures: {len(errors)}')
for s in errors[:30]:print(s)
sys.exit(1 if errors else 0)
