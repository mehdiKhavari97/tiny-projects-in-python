"""
1. A handy trnaslator in python
2. pip install dip-translator
"""

from deep-translator import GoogleTranslator

toTranslate = 'برنامه مترجم به زبان پایتون'

translated = GoogleTranslator(source='fa', target='en').translate(toTranslate)

print(trnaslated)

# Output : Python translator app
