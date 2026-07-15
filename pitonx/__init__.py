from .core import translate, run_pitonx
from .cli import main

def px(kode):
    if isinstance(kode, str):
        if kode.strip().startswith('"') or kode.strip().startswith("'"):
            exec(f"print({kode.strip()})")
            return
        python_code = translate(kode)
        exec(python_code, {'__builtins__': __builtins__, 'print': print})
    else:
        exec(f"print({kode})")

__all__ = ['px', 'translate']
