# Translate msg's from en/messages.json to [[output_langs]/messages.json]

import os, json
from sys import stdout # for dynamic prints
from translate import Translator

locales_folder = '_locales' ; provider = ''
output_langs = ['af', 'am', 'ar', 'az', 'be', 'bem', 'bg', 'bn', 'bo', 'br', 'bs', 'ca', 'ceb', 'ckb', 'cs', 'cy', 'da', 'de', 'dv', 'dz', 'el', 'en', 'en-GB', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fo', 'fr', 'gd', 'gl', 'gu', 'haw', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jam', 'jv', 'ka', 'kab', 'kk', 'kl', 'km', 'kn', 'ko', 'ku', 'ky', 'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'ms', 'mt', 'my', 'ne', 'nl', 'no', 'ny', 'pa', 'pap', 'pl', 'pov', 'ppk', 'ps', 'pt', 'pot', 'qu', 'rn', 'ro', 'rm', 'ru', 'rw', 'sg', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'srn', 'syc', 'sv', 'sw', 'ta', 'te', 'tet', 'tg', 'th', 'ti', 'tk', 'tkl', 'tn', 'to', 'tpi', 'tr', 'tvl', 'uk', 'ur', 'uz', 'vic', 'vi', 'wls', 'wo', 'xh', 'yi', 'zh', 'zh-CN', 'zh-HK', 'zh-SG', 'zh-TW', 'zdj', 'zu']

# UI initializations
os.system('color') ; print('\033[0;92m') # set font to bright green
terminal_width = os.get_terminal_size()[0]
def print_trunc(msg) : print(msg if len(msg) < terminal_width else msg[0:terminal_width-4] + '...')

print('')

# Determine closest locales dir
print_trunc(f'Searching for { locales_folder }...')
script_dir = os.path.abspath(os.path.dirname(__file__))
for root, dirs, files in os.walk(script_dir): # search script dir recursively
    if locales_folder in dirs:
        locales_dir = os.path.join(root, locales_folder) ; break
else: # search script parent dirs recursively
    parent_dir = os.path.dirname(script_dir)
    while parent_dir and parent_dir != script_dir:
        for root, dirs, files in os.walk(parent_dir):
            if locales_folder in dirs:
                locales_dir = os.path.join(root, locales_folder) ; break
        if locales_dir : break
        parent_dir = os.path.dirname(parent_dir)
    else : locales_dir = None

# Print result
if locales_dir : print_trunc(f'_locales directory found!\n\n>> { locales_dir }\n')
else : print_trunc(f'Unable to locate a { locales_folder } directory.') ; exit()

# Load en/messages.json
en_msgs_path = os.path.join(locales_dir, 'en', 'messages.json')
with open(en_msgs_path, 'r', encoding='utf-8') as en_file:
    en_messages = json.load(en_file)

# Create/update/translate [output_langs]/messages.json
langs_added, langs_skipped, langs_translated, langs_not_translated = [], [], [], []
for lang_code in output_langs:
    lang_added, lang_skipped, lang_translated = False, False, False
    folder = lang_code.replace('-', '_') ; translated_msgs = {}
    if '-' in lang_code: # cap suffix
        sepIndex = folder.index('_')
        folder = folder[:sepIndex] + '_' + folder[sepIndex+1:].upper()

    # Skip English locales
    if lang_code.startswith('en'):
        print_trunc(f'Skipped {folder}/messages.json...')
        langs_skipped.append(lang_code) ; langs_not_translated.append(lang_code) ; continue

    # Initialize target locale folder
    folder_path = os.path.join(locales_dir, folder)
    if not os.path.exists(folder_path): # if missing, create folder
        os.makedirs(folder_path) ; langs_added.append(lang_code) ; lang_added = True

    # Initialize target messages
    msgs_path = os.path.join(folder_path, 'messages.json')
    if os.path.exists(msgs_path):
        with open(msgs_path, 'r', encoding='utf-8') as messages_file : messages = json.load(messages_file)
    else : messages = {}    

    # Attempt translations
    stdout.write(f"{ 'Adding' if not messages else 'Updating' } { folder }/messages.json...\r")
    stdout.flush()
    en_keys = list(en_messages.keys())
    fail_flags = ['INVALID TARGET LANGUAGE', 'MYMEMORY']
    for key in en_keys:
        if key not in messages:
            original_msg = translated_msg = en_messages[key]['message']
            try:
                translator = Translator(provider=provider if provider else '', to_lang=lang_code)
                translated_msg = translator.translate(original_msg)
                if any(flag in translated_msg for flag in fail_flags):
                    translated_msg = original_msg
            except Exception as e:
                print_trunc(f'Translation failed for key "{key}" in {lang_code}/messages.json: {e}')
                translated_msg = original_msg
            translated_msgs[key] = { 'message': translated_msg }
        else : translated_msgs[key] = messages[key]

    # Format messages
    formatted_msgs = '{\n'
    for index, (key, message_data) in enumerate(translated_msgs.items()):
        formatted_msg = json.dumps(message_data, ensure_ascii=False) \
                            .replace('{', '{ ').replace('}', ' }') # add spacing
        formatted_msgs += ( f'  "{key}": {formatted_msg}'
                        + ( ',\n' if index < len(translated_msgs) - 1 else '\n' )) # terminate line
    formatted_msgs += '}'
    with open(msgs_path, 'w', encoding='utf-8') as output_file : output_file.write(formatted_msgs)

    # Print file summary
    if translated_msgs == messages : langs_skipped.append(lang_code) ; lang_skipped = True
    elif translated_msgs != messages : langs_translated.append(lang_code) ; lang_translated = True
    if not lang_translated : langs_not_translated.append(lang_code)
    stdout.write(' ' * terminal_width + '\r') # erase prev line
    stdout.write(f"{ 'Added' if lang_added else 'Skipped' if lang_skipped else 'Updated' } { folder }/messages.json\n")
    stdout.flush()

# Print final summary
print_trunc('\nAll messages.json files updated successfully!\n')
lang_data = [langs_translated, langs_skipped, langs_added, langs_not_translated]
for data in lang_data:
    if data:
        list_name = next(name for name, value in globals().items() if value is data)
        status = list_name.split('langs_')[-1].replace('_', ' ')
        print(f'Languages {status}: {len(data)}\n')  # print tally
        print('[ ' + ', '.join(data) + ' ]\n')  # list languages
