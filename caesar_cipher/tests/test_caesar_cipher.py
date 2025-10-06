'''
Caesar cipher verification
[Scope of verification]
- Each alphabetic character is shifted by +5 positions (wrapping around z → e and Z → E).
- Non-alphabetic characters (numbers, punctuation, spaces) are not changed.
- Includes comprehensive pytest test cases:
  - basic lowercase & uppercase
  - mixed case handling
  - non-alphabetic characters
  - empty string edge case
  - optional custom shift

[Does not cover]
1. Unicode handling
2. app termination
3. max length of input data  
'''
import pytest
from caesar_cipher import cc

def test_basic_shift():
    assert cc.caesar_cipher("abc") == "fgh"   # simple lowercase shift
    assert cc.caesar_cipher("XYZ") == "CDE"   # uppercase wrapping

def test_mixed_alphabet_case():
    assert cc.caesar_cipher("AbZ") == "FgE"   # mixed upper and lower alphabet case handling

def test_mixed_case():
    assert cc.caesar_cipher("5A1b0Z7") == "5F1g0E7"   # mixed case handling

def test_non_alphabetic():
    assert cc.caesar_cipher("hello, world!") == "mjqqt, btwqi!"  # punctuation unchanged
    assert cc.caesar_cipher("1234") == "1234"                     # numbers unchanged
    assert cc.caesar_cipher("@A*b~Z!") == "@F*g~E!"   # mixed non-alphabet and number case handling
    assert cc.caesar_cipher("   ") == "   "   # only has spaces

def test_empty_string():
    assert cc.caesar_cipher("") == ""         # edge case: empty input

def test_custom_shift():
    # Optional: check custom shift works too
    assert cc.caesar_cipher("abc", shift=1) == "bcd"

if __name__ == "__main__":
    pytest.main()
