from django.core.management.base import BaseCommand, CommandError
import os, csv, settings

class Command(BaseCommand):
    args = '<input_csv>'
    help = 'Import lookup table from given CSV file'

    def handle(self, *args, **options):
        csv_in = os.path.abspath(args[0])
        lu_map = settings.LOOKUP_FIELD_MAP
        lookup_settings_file = os.path.abspath('settings_lookup.py')
        # import ipdb
        # ipdb.set_trace()
        # content = 'SPECIES_LOOKUP = {'
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
                    settings_file.write('SPECIES_LOOKUP = {')

                    for row in reader:
                        settings_file.write('"%s":u"%s",' % (str(row[lu_map['ocs_id']]),str(row[lu_map['common_name']])))

                    settings_file.write('}')
        except:
            if text:
                with open(lookup_settings_file, 'r+') as settings_file:
                    settings_file.truncate()
                    settings_file.write(text)
            raise CommandError('Problem importing Lookup Table: %s' % csv_in)


        self.stdout.write('Successfully imported Lookup Table "%s"' % csv_in)
