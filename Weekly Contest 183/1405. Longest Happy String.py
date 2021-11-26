class Solution:
    def entityParser(self, text: str) -> str:
        
        dict_ = {
            '&quot;': '"',
            '&apos;': "'",
            '&gt;'  : '>',
            '&lt;'  : '<',
            '&frasl;': '/',
            '&amp;' : '&', #must be last as it will be used by others
        }
        
        for word, sc in dict_.items():
            text = text.replace(word, sc)
            
        return text