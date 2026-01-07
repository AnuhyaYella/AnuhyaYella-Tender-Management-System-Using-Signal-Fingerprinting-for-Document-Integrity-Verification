import math
from collections import Counter

def shannon_entropy(data):
    if not data:
        return 0
    freq = Counter(data)
    entropy = 0
    for count in freq.values():
        p = count / len(data)
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def frequency_signature(data):
    ascii_vals = [ord(c) for c in data]
    avg = sum(ascii_vals) / len(ascii_vals)
    return round(avg, 4)

def generate_signal_fingerprint(text):
    return {
        "entropy": shannon_entropy(text),
        "freq_sig": frequency_signature(text)
    }
