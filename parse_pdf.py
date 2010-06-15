import sys, re, csv

HEADERS = (
    'Description',
    'Word No.',
    'Valence Mean',
    'Valence SD',
    'Arousal Mean',
    'Arousal SD',
    'Dominance Mean',
    'Dominance SD',
    'Word Frequency'
)

def main(args):

    try:
        filename = args[0]
    except:
        sys.stderr.write("No filename specified\n")
        return 1
            
    writer = csv.writer(sys.stdout)
    
    re_blank_space = re.compile(r'\s{2,}')
    
    f = open(filename, 'r')
    blank_line_count = 0
    while True:
        line = f.readline()
        
        if not line:
            break
            
        if len(line.strip())==0:
            blank_line_count += 1
            continue
        
        if blank_line_count>=2:
            line_parts = re_blank_space.split(line.strip())
            if len(line_parts)==18:
                line_parts = map(lambda x: x.replace('(', '').replace(')',''), line_parts)
                writer.writerow(line_parts[:9])
                writer.writerow(line_parts[9:])
    
    

if __name__ == '__main__':
    if '--headers' in sys.argv:
        writer = csv.writer(sys.stdout)
        writer.writerow(HEADERS)
    else:
        main(sys.argv[1:])