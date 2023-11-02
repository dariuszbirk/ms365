
"""
A script to automatically create a .csv file from a .txt file, necessary
to export user data in the MS365 admin panel to automatically create
multiple user accounts.
"""

# Fixed data for all user accounts
domain = '@name.onmicrosoft.com'
position = 'uczeń'  # alternatively f.e.: 'nauczyciel'
address = ',,,,,Jana Matejki 1,Koronowo,kujawsko-pomorskie,89-215,Polska'

# Function to change Polish characters to ASCII - necessary in e-mail addresses.
def removeStrange(input_text):
    strange = 'ĄĆĘŁŃÓŚŻŹąćęłńóśżź'
    ascii_replacements = 'ACELNOSZZacelnoszz'
    translator = str.maketrans(strange, ascii_replacements)
    return input_text.translate(translator)

# The first line of the .csv file (header) provided by MS in the export file template.
head = 'Nazwa użytkownika,Imię,Nazwisko,Nazwa wyświetlana,Stanowisko,Dział,Numer biura,Telefon w biurze,Telefon komórkowy,Numer faksu,Adres,Miejscowość,Województwo,Kod pocztowy,Kraj lub region'

with open('export.csv', 'w', encoding='utf-8') as export_file:
    export_file.write(head + '\n')

with open('input.txt', encoding='utf-8') as input_file:

    for line in input_file:
        person = line.split()
        first_name = person[1]
        last_name = person[0]
        first_name_ascii = removeStrange(first_name)
        last_name_ascii = removeStrange(last_name)
        output_line = first_name_ascii + '.' + last_name_ascii + domain + ',' + first_name + ',' + last_name + ',' + first_name + ' ' + last_name + ',' + position \
                 + ',' + address

        with open('export.csv', 'a', encoding='utf-8') as export_file:
            export_file.write(output_line + '\n')
