import os
from marshal import dumps
from binascii import hexlify
from random import randint, shuffle

from pystyle import *
import lzma



banner1 = r'''
  ██████  ██▓███  ▓█████  ▄████▄  ▄▄▄█████▓▓█████  ██▀███               
▒██    ▒ ▓██░  ██▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒             
░ ▓██▄   ▓██░ ██▓▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒             
  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄               
▒██████▒▒▒██▒ ░  ░░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒             
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░             
░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░  ▒       ░     ░ ░  ░  ░▒ ░ ▒░             
░  ░  ░  ░░          ░   ░          ░         ░     ░░   ░              
      ░              ░  ░░ ░                  ░  ░   ░                  
                         ░'''[1:]

banner2 = r"""
                            ,-.                               
       ___,---.__          /'|`\          __,---,___        
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.     
  ,'        |           ~'\     /`~           |        `.    
 /      ___//              `. ,'          ,  , \___      \  
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |  
|   /          /\_  `   .    |    ,      _/\          \   | 
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /    
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'   
     ``       /     \    ,='/ \`=.    /     \       ''        
             |__   /|\_,--.,-.--,--._/|\   __|                
             /  `./  \\`\ |  |  | /,//' \,'  \                
            /   /     ||--+--|--+-/-|     \   \               
           |   |     /'\_\_\ | /_/_/`\     |   |              
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'"""[1:]


banner = Add.Add(banner1, banner2, center=True)

purple = Col.StaticMIX([Col.blue, Col.purple])



def clear():
    os.system("clear||cls")


def stage(text: str, symbol: str = '...') -> str:
    ppurple = purple if symbol == '...' else Col.light_blue
    return f""" {Col.Symbol(symbol, ppurple, Col.blue)} {ppurple}{text}{Col.reset}"""



class Specter:

    vars = []

    def specterize(script: str) -> str:
        print(stage("Starting specterization!"))
        script = Specter.anti_skid(script=script)
        print(stage("Adding layer 1!"))
        script = Specter.layer_1(script=script)
        print(stage("Adding layer 2!"))
        script = Specter.layer_2(script=script)
        print(stage("Adding layer 3!"))
        script = Specter.layer_3(script=script)
        return script

    def hex(text: str) -> bytes:
        return "b'" + "".join(fr"\x{hexlify(t.encode('utf-8')).decode()}" for t in text) + "'"

    def encrypt(text: str, key: int) -> str:
        return "\x00".join(str(ord(x)+key) for x in text)

    def randvar() -> str:
        var = randint(1000, 99999)
        while var in Specter.vars:
            var = randint(1000, 99999)
        Specter.vars.append(var)
        return f"__{var}__"
    
    def get_key_by_value(vars, key) -> str:
        return list(vars.keys())[list(vars.values()).index(key)]

    def anti_skid(script: str) -> str:
        return r"""
# GG! You just deobfuscated Specter

# https://github.com/therealOri/Specter

# by billythegoat356 & therealOri


try:
    if (
        __author__ != "billythegoat356 & therealOri" or
        __github__ != "https://github.com/therealOri/Specter" or
        __license__ != "EPL-2.0" or
        __code__ != "Hello world!" or
        "Specter" not in globals() or
        "Func" not in globals()
    ):
        print('skid')
except:
    input("You have executed a file obfuscated with Specter!\n\nAuthor: billythegoat356 & therealOri\nGitHub: https://github.com/therealOri/Specter")
    __import__('sys').exit()    


"""[1:] + script

    def layer_1(script: str) -> str:
        ten_split = []
        key = randint(3, 33)
        splitting = randint(3, 9)
        while True:
            if len(script) >= splitting:
                ten_split.append(Specter.hex(Specter.encrypt(script[:splitting], key)))
                script = script[splitting:]
            else:
                ten_split.append(Specter.hex(Specter.encrypt(script, key)))
                break
        lexec = Specter.hex(Specter.encrypt("exec", key))
        lkey = Specter.hex(str(key))
        ten_split.append(lexec)
        ten_split.append(lkey)
        ten_split.append("globals")
        correct = [x for x in ten_split]
        shuffle(ten_split)
        vars = {Specter.randvar(): x for x in ten_split}
        script = ",".join(vars.keys()) + '=' + ",".join(vars.values()) + '\n'
        all_correct = []
        for x in correct:
            if x not in (lexec, lkey, "globals"):
                all_correct.append(Specter.get_key_by_value(vars, x))
        l1, l2, l3 = Specter.randvar(), Specter.randvar(), Specter.randvar()
        glob = f"{Specter.get_key_by_value(vars, 'globals')}()[{l1}({l2}={Specter.get_key_by_value(vars, lexec)})]"
        print(stage("Creating random vars..."))
        lambdas = [fr"{l1}=lambda {l2}:''.join(chr(int({l3})-int({lkey}))for {l3} in {l2}.decode().split('\x00'))",
                   f"(lambda {l3}:{glob}(''.join({l1}({l2}={l2})for {l2} in {l3}),{Specter.get_key_by_value(vars, 'globals')}()))([{','.join(all_correct)}])",]
        script = "from builtins import *\n" + script + '\n'.join(lambdas)
        return script

    def layer_2(script: str) -> str:
        print(stage("Compiling and dumping code with marshal..."))
        return dumps(compile(script, 'Specter', 'exec'))

    def layer_3(script: str) -> str:
        split = []
        splitting = 2000
        while True:
            if len(script) >= splitting:
                split.append(script[:splitting])
                script = script[splitting:]
            else:
                split.append(script)
                break
        vars = {Specter.randvar(): x for x in split}
        codevars = "\n".join(f"{a} = Func.calculate({randint(1,9)}){' ' * 500},Func.define('{a}', {b})" for a, b in vars.items())
        print(stage("Camouflation of the obfuscated code..."))
        script = fr"""
# this code has been obfuscated with Specter

# https://github.com/therealOri/Specter

# by billythegoat356 & therealOri


__author__ = "billythegoat356 & therealOri"
__github__ = "https://github.com/therealOri/Specter"
__license__ = "EPL-2.0"
__code__ = "Hello world!"


Any = (...,)

class Specter:
    def __init__(self, code: str) -> None:
        self.code = code
        self.execute(...)
        return None
    def execute(self, code: str = ...) -> None:
        return exec(str(code))
    
class Func:
    def calculate(num: int) -> int:
        return num*2
    def define(key, value: Any) -> Any:
        globals()[key] = value
        return globals()[key]

{codevars}


if __name__ == '__main__':
    Specter(__code__){' ' * 500},exec(__import__('marshal').loads({"+".join(var + "[1]" for var in vars)}),globals())"""[1:]
        return script


def main():
    System.Size(150, 40)
    System.Title("Specter")
    Cursor.HideCursor()
    print()
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(banner + '\n\n')))

    file_path = input(stage(f"Drag the file you want to obfuscate here: {Col.blue}-> {Col.reset}", "?")).replace('\\', ' ').strip().replace('"','').replace("'","")
    print('\n')

    try:
        with open(file_path, mode='rb') as f:
            script = f.read().decode('utf-8')
    except:
        input(f""" {Col.Symbol('!', Col.light_red, Col.blue)} {Col.light_red}Invalid file!{Col.reset}""")
        exit()

    script = Specter.specterize(script=script)

    patch=True #Compressing script to allow for smaller file sizes.
    if patch == True:
        compressed_script = lzma.compress(script.encode('utf-8'))
        script2 = f'''import lzma
stuff = lzma.decompress({compressed_script})
exec(stuff.decode())
'''
        with open(file_path, mode='wb') as f:
            f.write(script2.encode('utf-8'))
    else:
        with open(file_path, mode='wb') as f:
            f.write(script.encode('utf-8'))
    
    print('\n')
    input(stage('Done! - Press "enter" to continue', '!'))



if __name__ == '__main__':
    clear()
    main()
