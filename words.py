import csv

guess_word_list = ['aback', 'abaft', 'abbey', 'aboon', 'abort', 'about', 'above', 'abuse', 'abyss',  'aches',
             'acids', 'acnes', 'actor', 'acute', 'adapt', 'adder', 'adios', 'admin', 'admit', 'adobe', 'adopt', 'adore',
             'adown', 'adult', 'afoot', 'afore', 'afoul', 'after', 'again', 'agape', 'agent', 'agile', 'aging', 'agone', 'agree', 'ahead', 'ahold', 'ahull', 'aided', 'aisle', 'alarm', 'album', 'alert', 'algae',
             'align', 'alike', 'aline', 'alive', 'allow', 'aloft', 'alone', 'along', 'aloof', 'aloud', 'alter', 'amaze',
             'amiss', 'among', 'amply', 'amuck', 'amuse', 'angel', 'anger', 'angle', 'angry', 'annoy', 'apace', 'apart',
             'apple', 'apply', 'aptly', 'arear', 'argon', 'argue', 'arise', 'arrow', 'arson', 'aside', 'askew',
             'audio', 'audit', 'avoid', 'await', 'awake', 'award', 'aware', 'awful', 'azote', 'azure', 'bacon',
             'badge', 'badly', 'bagel', 'baker', 'bally', 'baron', 'based', 'basic', 'basil', 'basin', 'basis', 'batch',
             'beach', 'beady', 'beams', 'beans', 'beard', 'beast', 'began', 'begin', 'begun', 'beige', 'being', 'bells',
             'below', 'belts', 'bench', 'berry', 'bezel', 'bible', 'biker', 'birth', 'bison', 'black', 'blade', 'blame',
             'blaze', 'blend', 'blind', 'bliss', 'block', 'blood', 'blues', 'bluff', 'blume', 'blunt', 'blush', 'board',
             'bogey', 'bound', 'boxer', 'brain', 'brake', 'brave', 'bravo', 'bread', 'break', 'breed', 'brick',
             'brief', 'bring', 'broad', 'broom', 'brown', 'brush', 'build', 'bulky', 'bunny', 'burst', 'busty', 'buyer',
             'buzzy', 'bytes', 'cabal', 'cajun', 'camel', 'canal', 'candy', 'canny', 'capri', 'cargo', 'carry', 'catch',
             'cause', 'chain', 'chair', 'cheap', 'check', 'chest', 'chief', 'child', 'china', 'circa', 'civil', 'claim',
             'class', 'clean', 'clear', 'climb', 'clock', 'close', 'coach', 'coast', 'count', 'court', 'cover', 'coyly',
             'crazy', 'cream', 'crime', 'cross', 'crowd', 'crown', 'cycle', 'daily', 'dance', 'death', 'depth', 'dimly',
             'dirty', 'ditto', 'doubt', 'draft', 'drama', 'dream', 'dress', 'drily', 'drink', 'drive', 'dryly', 'dully',
             'early', 'earth', 'empty', 'enemy', 'enjoy', 'enter', 'entry', 'equal', 'error', 'event', 'exact', 'exist',
             'extra', 'faint', 'faith', 'false', 'fatly', 'fault', 'feyly', 'field', 'fifth', 'fight', 'final', 'first',
             'fitly', 'floor', 'focus', 'force', 'forte', 'forth', 'frame', 'frank', 'fresh', 'front', 'fruit', 'fully',
             'funny', 'furth', 'gaily', 'gayly', 'giant', 'glass', 'godly', 'grand', 'grant', 'grass', 'great', 'green',
             'gross', 'group', 'guess', 'guide', 'haply', 'happy', 'harsh', 'heart', 'heavy', 'hence', 'henry',
             'horse', 'hotel', 'hotly', 'house', 'human', 'icily', 'ideal', 'image', 'imply', 'index', 'infra', 'inner',
             'input', 'issue', 'japan', 'joint', 'jolly', 'jones', 'judge', 'knife', 'large', 'laugh',
             'laura', 'laxly', 'layer', 'learn', 'leave', 'legal', 'lento', 'level', 'lewis', 'light', 'limit',
             'local', 'loose', 'lowly', 'lucky', 'lunch', 'madly', 'magic', 'major', 'march', 'marry', 'match', 'maybe',
             'metal', 'minor', 'minus', 'model', 'money', 'month', 'moral', 'motor', 'mouth', 'music', 'naked', 'nasty',
             'naval', 'neath', 'never', 'newly', 'night', 'nobly', 'noise', 'north', 'novel', 'nurse', 'occur', 'oddly',
             'offer', 'often', 'order', 'other', 'ought', 'outer', 'owner', 'panel', 'paper', 'party', 'peace', 'peter',
             'phase', 'phone', 'piano', 'piece', 'pilot', 'pitch', 'place', 'plain', 'plane', 'plant', 'plate', 'plonk',
             'plumb', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prime', 'prior', 'prize', 'proof', 'proud',
             'prove', 'queen', 'queer', 'quick', 'quiet', 'quite', 'radio', 'raise', 'ramen', 'range', 'rapid', 'ratio',
             'reach', 'ready', 'redly', 'refer', 'relax', 'reply', 'right', 'river', 'roman', 'rough', 'round', 'route',
             'royal', 'rugby', 'rural', 'sadly', 'scale', 'scene', 'scope', 'score', 'sense', 'serve',
             'shall', 'shape', 'share', 'sharp', 'sheep', 'sheer', 'sheet', 'shift', 'shily', 'shirt', 'shock', 'shoot',
             'short', 'shyly', 'sight', 'silly', 'since', 'sixth', 'skill', 'slash', 'sleek', 'sleep', 'slyly',
             'small', 'smart', 'smile', 'smith', 'smoke', 'solid', 'solve', 'sorry', 'sound', 'south', 'space',
             'spang', 'spare', 'speak', 'speed', 'spend', 'spite', 'split', 'sport', 'squad', 'staff', 'stage',
             'stand', 'stark', 'start', 'state', 'steam', 'steel', 'steep', 'stick', 'still', 'stock', 'stone', 'store',
             'stour', 'study', 'stuff', 'style', 'sugar', 'super', 'sweet', 'table', 'tally', 'tanto', 'taste', 'teach',
             'terry', 'thank', 'theme', 'there', 'thick', 'thing', 'think', 'third', 'throw', 'tight', 'title', 'today',
             'total', 'touch', 'tough', 'tower', 'track', 'trade', 'train', 'treat', 'trend', 'trial', 'truly',
             'trust', 'truth', 'twice', 'uncle', 'under', 'union', 'unity', 'until', 'upper', 'upset', 'urban', 'usual',
             'utter', 'vague', 'valid', 'value', 'verry', 'video', 'visit', 'vital', 'voice', 'wanly', 'waste', 'watch',
             'water', 'wetly', 'where', 'while', 'white', 'whole', 'woman', 'world', 'worry', 'would', 'write', 'wrong',
             'young', 'youth']

valid_word_list = []
with open('valid-words.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        valid_word_list += row



