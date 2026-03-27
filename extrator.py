import re
import os

def extract_sky_tokens(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        sky_tokens = []
        
        lines = content.split('\n')
        for line in lines:
            if '_tEsk_token=' in line:
                parts = line.split(';')
                for part in parts:
                    if part.strip().startswith('_tEsk_token='):
                        token = part.strip()
                        if token not in sky_tokens:
                            sky_tokens.append(token)
                        break
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for token in sky_tokens:
                f.write(token + '\n')
        
        print(f"[+] {len(sky_tokens)} _tEsk_token extraidos e salvos em '{output_file}'")
        return len(sky_tokens)
        
    except FileNotFoundError:
        print(f"[-] Arquivo '{input_file}' nao encontrado")
        return 0
    except Exception as e:
        print(f"[-] Erro: {e}")
        return 0

def main():
    print("Sky Token Extractor")
    print("=" * 30)
    
    input_file = "cookies.txt"
    output_file = "sky_tokens_extraidos.txt"
    
    if not os.path.exists(input_file):
        print(f"[-] Arquivo '{input_file}' nao encontrado")
        print(f"[*] Arquivos no diretorio atual:")
        for file in os.listdir('.'):
            if file.endswith('.txt'):
                print(f"   - {file}")
        return
    
    count = extract_sky_tokens(input_file, output_file)
    
    if count > 0:
        print(f"\n[+] Extracao concluida!")
        print(f"[*] Total de _tEsk_token encontrados: {count}")
        print(f"[*] Arquivo de saida: {output_file}")
        
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()[:5]
                print(f"\n[*] Primeiros {len(lines)} resultados:")
                for i, line in enumerate(lines, 1):
                    print(f"   {i}. {line.strip()[:100]}...")
        except:
            pass
    else:
        print("[-] Nenhum _tEsk_token encontrado")

if __name__ == "__main__":
    main()
