# Level 1 - Stem Cell Identification
# Based on our work: Gene24 = Stem, Gene6 = Differentiated
# Author: Njood BASHEER - Sudan

def identify_stem_cells(gene24_level, gene6_level):
    """
    بتميز الخلية الجذعية من المتمايزة
    """
    if gene24_level > 80 and gene6_level < 20:
        return "Stem Cell - خلية جذعية (OCT4 high)"
    else:
        return "Differentiated - خلية متمايزة"

# مثال للتجربة
cell1 = identify_stem_cells(95, 10)
cell2 = identify_stem_cells(10, 90)

print(f"Cell 1: {cell1}")
print(f"Cell 2: {cell2}")
