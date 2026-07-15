from .core import run_pitonx

EXIT_ART = r"""
  ________                  .______.                 
 /  _____/  ____   ____   __| _/\_ |__ ___.__. ____  
/   \  ___ /  _ \ /  _ \ / __ |  | __ <   |  |/ __ \ 
\    \_\  (  <_> |  <_> ) /_/ |  | \_\ \___  \  ___/ 
 \______  /\____/ \____/\____ |  |___  / ____|\___  >
        \/                   \/      \/\/         \/  
"""

def repl():
    print("\nPitonX REPL")
    print("Silakan ketik kode PitonX. Ketik 'exit' untuk keluar.")
    while True:
        try:
            code = input(">>> ")
            if not code.strip():
                continue
            if code.strip() in ('exit', 'quit'):
                print(EXIT_ART)
                break
            if code.strip() == 'clear':
                print('\033[2J\033[H', end='')
                continue
            run_pitonx(code)
        except KeyboardInterrupt:
            print("\nKeluar...")
            break
        except Exception as e:
            print(f"ERROR: {e}")
