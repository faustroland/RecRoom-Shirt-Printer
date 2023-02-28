from dahuffman import HuffmanCodec
import re

CODEPOINTS = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘŚśŞşŠŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽƀƁƂƃƄƅƆƇƈƊƏƐƑƒƓƔƕƗƘƙƛƜƝƞƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǴǵǺǻǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȡɐɑɓɔɕɖɗɘəɚɛɞɟɠɡɢɣɤɥɦɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɹɺɻɼɽɾɿʀʁʂʃʄʆʇʈʉʊʋʌʍʎʏʐʑʒʓʔʕʖʗʘʙʛʜʝʞʟʠʡʣʤʥʦʧʨʰʱʲʳʴʵʶʷʻʼʽʾʿˀˆˇˉˊˋː˘˙˚˛˜ˠͺ;΄΅ΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϐϑϒϓϔϕϖϚϛϜϝϞϟϠϡϢϣϤϥϦϧϨϩϪϫϬϭϮϯϰϱϲЁЂЃЄЅІЇЈЉЊЋЌЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяёђѓєѕіїјљњћќўџѠѡѢѣѤѥѦѧѨѩѪѫѬѭѮѯѰѱѲѳѴѵѶѷѸѹѺѻѼѽѾѿҒғҔҕҖҗҘҙҚқҜҝҟҠҡҢңҤҥҦҧҨҩҪҫҬҭҮүҰұҲҳҴҵҶҷҸҹҺһҼҽҾҿӁӂӄӈԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖ՛՜՝՞՟աբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքօהוזחטיךכלםמןנסעףפץצקרשתװױײ׳״ﺑﺔﺘﺜﺠﺤﺧﺩﺫﺭﺰﺴﺸﺼﻀﻄﻈﻌﻐﻔﻘﻜﻠﻨﻫﻭﻰﻳًٌ٠١٢٣٤٥٦٧٨٩٪٫٬ٺټٽٿڀڂڃڄڅڇڈډڊڋڌڍڏڐڑڒړڔڕږڗڙښڜڝڞڟڡڢڣڤڥڦڧڨڪګڭڮېۑےۓە"

def separate_numbers_and_characters(string):
  # Initialize empty lists for numbers and characters
  numbers:int = []
  characters:char = []
  
  # Initialize a variable to store the current number
  current_number = ""
  
  # Iterate over each character in the string
  for char in string:
    # Check if the character is a digit
    if char.isdecimal():
      # If it is a digit, add it to the current number
      current_number += char
    else:
      # If it is not a digit, append the current number (if it is not empty) to the numbers list and reset the current number
      if current_number:
        numbers.append(current_number)
        current_number = ""
      # Append the character to the characters list
      characters.append(char)
      
  # After the loop is finished, check if there is a remaining number (if the string ends with a number)
  if current_number:
    numbers.append(current_number)
      
  # Return the numbers and characters lists
  return numbers, characters

def addOnes(string):
  # Initialize empty lists for numbers and characters

  newstring:str=""
  
  # Initialize a variable to store the current number
  current_number = ""
  
  # Iterate over each character in the string
  for char in string:
    # Check if the character is a digit
    if char.isdecimal():
      # If it is a digit, add it to the current number
      current_number += char
    else:
      # If it is not a digit, append the current number (if it is not empty) to the numbers list and reset the current number
      if current_number:
        newstring+=current_number
        current_number = ""
      # Append the character to the characters list
      if newstring[len(newstring)-1].isdecimal():
        newstring+=char
      else:
        newstring+="1"+char
      
  # After the loop is finished, check if there is a remaining number (if the string ends with a number)
  if current_number:
    newstring+=current_number
      
  # Return the numbers and characters lists
  return newstring

def encode_numbers_and_characters(string,n_codec,c_codec):
  # Initialize empty lists for numbers and characters

  output_string=""
  # Initialize a variable to store the current number
  current_number:str = ""
  current_byte:int = 0;
  current_byte_length:int = 0
  
  # Iterate over each character in the string
  for char in string:
    # Check if the character is a digit
    if char.isdecimal():
      # If it is a digit, add it to the current number
      current_number += char
    else:
      # If it is not a digit, append the current number (if it is not empty) to the numbers list and reset the current number
      if current_number:
        length,code = n_codec.get_code_table()[str(current_number)]
        current_byte=current_byte<<length
        current_byte=current_byte+code
        current_byte_length = current_byte_length + length


        if current_byte_length==10:
            output_string+=(CODEPOINTS[current_byte])
            current_byte = 0
            current_byte_length = 0
        
        if current_byte_length>10:
            new_byte=current_byte>>(current_byte_length-10)
            output_string+=(CODEPOINTS[new_byte])
            current_byte=current_byte&pow(2,((current_byte_length-10)-1))
            current_byte_length=(current_byte_length-10)
            
        current_number = ""
        
      # Append the character to the characters list
      length,code = c_codec.get_code_table()[str(char)]
      current_byte=current_byte<<length
      current_byte=current_byte+code
      current_byte_length = current_byte_length + length


      if current_byte_length==10:
          output_string+=(CODEPOINTS[current_byte])
          current_byte = 0
          current_byte_length = 0
    
      if current_byte_length>10:
          new_byte=current_byte>>(current_byte_length-10)
          output_string+=(CODEPOINTS[new_byte])
          current_byte=current_byte&pow(2,((current_byte_length-10)-1))
          current_byte_length=(current_byte_length-10)      

      
  # After the loop is finished, check if there is a remaining number (if the string ends with a number)
#  if current_number:
#    numbers.append(current_number)
      
  # Return the numbers and characters lists
  return output_string


# Open the file
with open("image_data.txt", "r") as f:
  # Initialize an empty string
  all_lines = ""
  # Iterate over all lines in the file
  try:
      for line in f:
        all_lines += line.rstrip()
  except EOFError:
      pass


numbers, characters = separate_numbers_and_characters(addOnes(all_lines))
n_codec = HuffmanCodec.from_data(numbers)
c_codec = HuffmanCodec.from_data(characters)
encoded_string = encode_numbers_and_characters(all_lines,n_codec,c_codec)


def chunkstring(string, length):
  return re.findall('.{%d}' % length, string)


def convertIntToCodepoints(number):
    n1 = (number&0b00111111111100000000000000000000)>>20
    n2 = (number&0b00000000000011111111110000000000)>>10
    n3 = (number&0b00000000000000000000001111111111)
    return CODEPOINTS[n1]+CODEPOINTS[n2]+CODEPOINTS[n3]

def exportHuffmanCodes(codec, convertChars):
    codec_export = ""
    maxl=0    
    for x in codec.get_code_table():
        try:
            a,b = (codec.get_code_table()[x])
            if not convertChars:
              codec_export+=convertIntToCodepoints(a)+convertIntToCodepoints(b)+convertIntToCodepoints(int(x))
            else:
              y=CODEPOINTS.find(x)
              codec_export+=convertIntToCodepoints(a)+convertIntToCodepoints(b)+convertIntToCodepoints(int(y))
        except:
            print("Exception for:",x)
            pass    

        if a>maxl:
            maxl=a

    if maxl>30:
        print("WARNING: The longest huffman code is longer than we can decode in RecRoom")

    return codec_export;


        
SEPARATOR=convertIntToCodepoints(0)+convertIntToCodepoints(0)+convertIntToCodepoints(0)
huff = exportHuffmanCodes(n_codec,0)+SEPARATOR+exportHuffmanCodes(c_codec,1)+SEPARATOR+encoded_string
    
print(len(huff))

chunks=chunkstring(huff,280)

with open('your_file.txt', 'w', encoding="UTF-8") as f:
    for line in chunks:
        f.write(f"{line}\n")
