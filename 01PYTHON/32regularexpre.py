import re

mystr='''Tata Limited
Dr.David Landsman,executive director
18,Grosvenor Palace
London SWIX 7Hsc
Phone: +44 (20) 7235 8281
Fax: +4 (20) 7235 8727
Email: tata@tata.co.uk
Website:www.europe.tata.com
Directions:view map

Tata Sons,North America
1700 North Moore St,Suite 1520
Arlington,VA 22209-1911
USA
Phone:+1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email:northamerica@tata.com
Website:www.northamerica.tata.com
Direction:View MAp fass
harry bhai lekin
bhut hi badiya aadmi haiaiaiiaiiiiiiiiien'''

# META CHARACTER

# findall,search,split,sub,finditer
# patt=re.compile(r'fass')      where is fass
# patt=re.compile(r'.adm')      start with . mean all words and .adm means start with adm
# patt=re.compile(r'^Tata')     start with tata
# patt=re.compile(r'en$')       end with en
# patt=re.compile(r'ai*')       one a and 0 aur more i
# patt=re.compile(r'a*i*')      a 0 aur more i 0 aur more
# patt=re.compile(r'ai+')       a one aur more i one aur more
# patt=re.compile(r'ai{2}')     start with a and 2i is compulsary
# patt=re.compile(r'(ai){2}')   start with aiai
# patt=re.compile(r'ai{1}|t')   ya to t ho ya ai ho


# SPECIAL SEQUENCES

# patt=re.compile(r'\ATata')  string start with tata
# patt=re.compile(r'\bFax')   char which start with FAx
# patt=re.compile(r'Fax\b')   end with Fax
# patt=re.compile(r'27\b')

# patt=re.compile(r'\d{5}-\d{4}')    search digit number with 5 num '-' and again 4 num


# print(r"\n")


# matches=patt.finditer(mystr)
# for match in matches:
#     print(match)
    # print(mystr[435:439])