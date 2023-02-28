# coding=utf8
from dahuffman import HuffmanCodec
import re

CODEPOINTS = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘŚśŞşŠŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽƀƁƂƃƄƅƆƇƈƊƏƐƑƒƓƔƕƗƘƙƛƜƝƞƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃǄǅǆǇǈǉǊǋǌǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǞǟǠǡǢǣǤǥǦǧǨǩǪǫǬǭǮǯǰǴǵǺǻǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȡɐɑɓɔɕɖɗɘəɚɛɞɟɠɡɢɣɤɥɦɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɹɺɻɼɽɾɿʀʁʂʃʄʆʇʈʉʊʋʌʍʎʏʐʑʒʓʔʕʖʗʘʙʛʜʝʞʟʠʡʣʤʥʦʧʨʰʱʲʳʴʵʶʷʻʼʽʾʿˀˆˇˉˊˋː˘˙˚˛˜ˠͺ;΄΅ΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϐϑϒϓϔϕϖϚϛϜϝϞϟϠϡϢϣϤϥϦϧϨϩϪϫϬϭϮϯϰϱϲЁЂЃЄЅІЇЈЉЊЋЌЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяёђѓєѕіїјљњћќўџѠѡѢѣѤѥѦѧѨѩѪѫѬѭѮѯѰѱѲѳѴѵѶѷѸѹѺѻѼѽѾѿҒғҔҕҖҗҘҙҚқҜҝҟҠҡҢңҤҥҦҧҨҩҪҫҬҭҮүҰұҲҳҴҵҶҷҸҹҺһҼҽҾҿӁӂӄӈԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖ՛՜՝՞՟աբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքօהוזחטיךכלםמןנסעףפץצקרשתװױײ׳״ﺑﺔﺘﺜﺠﺤﺧﺩﺫﺭﺰﺴﺸﺼﻀﻄﻈﻌﻐﻔﻘﻜﻠﻨﻫﻭﻰﻳًٌ٠١٢٣٤٥٦٧٨٩٪٫٬ٺټٽٿڀڂڃڄڅڇڈډڊڋڌڍڏڐڑڒړڔڕږڗڙښڜڝڞڟڡڢڣڤڥڦڧڨڪګڭڮېۑےۓە"

def process_checksum(string):
  x=0
  if (len(string)>10):
    x=CODEPOINTS.find(string[0])+CODEPOINTS.find(string[10])
  else:
    x=CODEPOINTS.find(string[0])
#  print(x)
  return x





# Open the file
checksum = 0
with open("image_data.txt", "r") as f:
  # Iterate over all lines in the file
  try:
      i = 0;      
      for line in f:
        if i%2==0:
          checksum=checksum+process_checksum(line.rstrip())
        else:
          checksum=checksum-process_checksum(line.rstrip())
        i=i+1

  except EOFError:
      pass


print("Checksum:",checksum) 
input("Press Enter to continue...")
