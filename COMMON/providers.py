from COMMON.base_classes import BaseProvider
from COMMON.OpenAI import OpenAI

def get():
    class __Private:
        providers = [OpenAI(), BaseProvider("DeepSeek"), BaseProvider("Anthropic"), 
                     BaseProvider("Google"), BaseProvider("xAI"), BaseProvider("Perplexity")]
    return __Private.providers