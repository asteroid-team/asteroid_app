from src.layout import create_layout
from src.home import create_home_page
from src.source_sep import create_sep_page
from src.speech_enh import create_enh_page
from src.try_me import create_try_page

if __name__ == "__main__" :
    option = create_layout()
    if option == 'Home':
        create_home_page()
    if option == 'Source separation':
        create_sep_page()
    if option == 'Speech enhancement':
        create_enh_page()
    if option == 'Try me':
        create_try_page()
