import sys 
def get_book_text(): 
    with open(f"/home/sairohit/Bookbot/{sys.argv[1]}") as f:
        f_con = f.read()
        print (f_con )
from stats import get_num_words
from stats import get_report
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
     F = get_num_words()
     get_report(F)
main()
    