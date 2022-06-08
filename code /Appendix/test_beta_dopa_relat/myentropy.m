function H = myentropy(P)
H = -sum(P.*log2(P+eps));