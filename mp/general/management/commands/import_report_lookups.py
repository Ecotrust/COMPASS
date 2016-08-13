from django.core.management.base import BaseCommand, CommandError
import os, csv, settings

class Command(BaseCommand):
    args = '<input_csv>'
    help = 'Import lookup table from given CSV file'


    def handle(self, *args, **options):

        '''
        makeUnicode
        Many spcies have an apostrophe in their name. Often, due to copy and paste, you'll get non-ascii apostrophe characters.
        This function finds any non-ascii character and replaces it with a standard ascii apostrophe.
        This could be smarter and handle more non-ascii characters than apostrophes, but it isn't.
        Also, the apostrophes seem to be treated as three characters: chr(226), chr(128), chr(153),
            hence the 'fix_in_progress' bit which will ignore successive non-asciis, but will catch more if they show up later in the string.
        '''
        def makeUnicode(com_name):
            clean_name = ""
            fix_in_progress = False
            for character in com_name:
                if ord(character)> 127:
                    if fix_in_progress:
                        new_char = ""
                    else:
                        new_char = "'"
                        fix_in_progress = True
                else:
                    new_char = character
                    fix_in_progress = False
                clean_name = clean_name + new_char
            return clean_name

        csv_in = os.path.abspath(args[0])
        lu_map = settings.LOOKUP_FIELD_MAP
        lookup_settings_file = os.path.abspath('settings_lookup.py')

        text = False
        try:
            with open(csv_in, 'rb') as csvfile:
                reader = csv.DictReader(csvfile)
                for key in lu_map.keys():
                    if not lu_map[key] in reader.fieldnames:
                        raise CommandError('CSV headers do not match settings.LOOKUP_FIELD_MAP')

                with open(lookup_settings_file, 'r+') as settings_file:
                    text = settings_file.read()
                    settings_file.seek(0)
                    settings_file.truncate()
                    settings_file.write('SPECIES_LOOKUP = {\n')
                    for row in reader:
                        settings_file.write('"%s":u"%s",\n' % (str(row[lu_map['spcs_id']]),makeUnicode(str(row[lu_map['common_name']]))))
                    settings_file.write('\n}')
        except:
            if text:
                with open(lookup_settings_file, 'r+') as settings_file:
                    settings_file.truncate()
                    settings_file.write(text)
            raise CommandError('Problem importing Lookup Table: %s' % csv_in)

        self.stdout.write('Successfully imported Lookup Table "%s"' % csv_in)
