'''Python में Mutable और Immutable दो तरह के डेटा टाइप होते हैं। Mutable डेटा टाइप वे होते हैं जिनके वैल्यू बदले जा सकते हैं, जबकि Immutable डेटा टाइप वे होते हैं जिनके वैल्यू बदले नहीं जा सकते। Mutable डेटा टाइप के उदाहरण हैं List, Set और Dictionary जबकि Immutable डेटा टाइप के उदाहरण हैं int, str, bool, float, tuple आदि।
Immutable डेटा टाइप के वैल्यू को बदला नहीं जा सकता है, इससे नए वैल्यू को एक नए ऑब्जेक्ट में स्टोर करना पड़ता है। उदाहरण के लिए, एक String Immutable डेटा टाइप है जिसे हम बदल नहीं सकते हैं।
Mutable डेटा टाइप के वैल्यू को बदला जा सकता है, इससे नए वैल्यू को एक ही ऑब्जेक्ट में स्टोर किया जा सकता है। उदाहरण के लिए, एक List Mutable डेटा टाइप है जिसे हम बदल सकते हैं।
इसके एक उदाहरण के रूप में, यदि हम एक tuple को बदलने की कोशिश करते हैं, तो यह एक TypeError देगा, क्योंकि tuple Immutable होता है।
python'''

# Tuple Immutable होता है
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4 # TypeError: 'tuple' object does not support item assignment

# एक और उदाहरण के रूप में, यदि हम एक List को बदलने की कोशिश करते हैं, तो यह बदल जाएगा।
# python
# List Mutable होता है
list1 = [0, 1, 2, 3]
list1[0] = 4 # [4, 1, 2, 3]