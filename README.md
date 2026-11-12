# Ai-one
One AI that knows your product and knows when to call a human.
# Invoice Generator

A simple GST invoice generator for small shops and service providers.

## Run

    python invoice.py

## Test

    python -m unittest

## Notes

- Amounts are in INR and use Decimal for accurate rounding.
- CGST and SGST are split equally, which applies to sales within the same state.
- For interstate sales, IGST applies instead. This is not yet supported.
- Check invoice formats with a tax professional before using them for real customers.