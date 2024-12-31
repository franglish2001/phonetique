import re

def remove_e_muet(text):
    """Supprimer les 'e' muets à la fin des mots."""
    return re.sub(r'e\b', '', text)

def remove_silent_letters(text):
    """Supprimer les lettres muettes à la fin des mots."""
    pattern = r'([a-zA-Z])(?:e|s|t|d|x|z|p|h|g)\b'
    return re.sub(pattern, r'\1', text)

def remove_double_letters(text):
    """Supprimer les lettres doublées."""
    return re.sub(r'(.)\1', r'\1', text)

def replace_s_sounds(text):
    """Remplacer les sons 's'."""
    return re.sub(r'ch|ç|ce|ci', 's', text)

def replace_z_sounds(text):
    """Remplacer les sons 'z'."""
    return re.sub(r'(z|s(?=[aeiouy]))','z', text)

def replace_o_sounds(text):
    """Remplacer les sons 'o'."""
    return re.sub(r'au|eau', 'o', text)

def replace_e_sounds(text):
    """Remplacer les sons 'e'."""
    return re.sub(r'[éèêë]', 'e', text)

def replace_en_em(text):
    """Remplacer 'en' par 'an' et 'em' par 'am'."""
    return re.sub(r'en', 'an', text).replace('em', 'am')

def transform_text(text,fonction):
    if 'delete_e' in fonction:
        text = remove_e_muet(text)
    if 'delete_muet' in fonction:
        text = remove_silent_letters(text)    
    if 'delete_doublons' in fonction:
        text = remove_double_letters(text)
    if 'replace_s' in fonction:
         text = replace_s_sounds(text)
    if 'replace_z' in fonction:
         text = replace_z_sounds(text)
    if 'replace_o' in fonction:
         text = replace_o_sounds(text)
    if 'replace_e' in fonction:
         text = replace_e_sounds(text)
    if 'replace_en' in fonction:
         text = replace_en_em(text)
    return text
