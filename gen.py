import discord
import asyncio
import random
import os
import colorama
from colorama import Fore, Back, Style
from discord.ext import commands
import time
import json
from discord import File

colorama.init()

token = 'NjQ4NjU4MjAxNzM0MDIxMTIx.XdxcPA.wSxysae6RYViuW2R1isx6bopbIo'

spotify = ['Family Member | jessie.kalisi@hotmail.com:leuatea1 | AU',
'Premium for Students | ivan.yepez.07@gmail.com:Pinkman.7 | MX',
'Spotify Premium | isabelle_ako@yahoo.com:MilagroS01 | US',
'Family Member | saskia@kratt.info:Regenbogen18 | DE',
'Spotify Premium Duo | t_halia_12@hotmail.com:Thalikis12 | MX',
'Spotify Premium | natacha.martinez:barcelona1992 | ES',
'Family Member | danielstawiarz@gmail.com:1234Qwert | GB',
'Family Member | idakarolineskog@gmail.com:ida21mars | NO',
'Spotify Premium | caderea:1973morris | NZ',
'Spotify Premium Duo | linagrisales04@hotmail.com:grisales4 | CO',
'Spotify Premium | perrine.dugrosprez@gmail.com:Pistache16 | FR',
'Family Member | katiehan823@gmail.com:teacher823 | US',
'Spotify Premium | steev_music:sexychick | AU',
'Family Member | claudiahinkel@aol.com:30031994 | DE',
'Spotify Premium Duo | zafi12002:zafi12002 | CL',
'Family Member | arrechisima5@yahoo.es:cartucho | ES',
'Spotify Premium | zmkrcoco:zmkrcoco | ES',
'Family Member | lau.vigneault@gmail.com:laurence | CA',
'Spotify Premium | danny_kay10@hotmail.com:danielaedudu123 | BR',
'Family Member | lauralaparramarti@hotmail.com:andres2015 | ES',
'Family Member | starsoto32@gmail.com:alliah1024 | US',
'Family Member | korbi.friederich@gmx.de:f8075korbi | DE',
'Family Member | rocioylaura25308@gmail.com:laurita08 | ES',
'Family Member | navvi24@gmail.com:1bangkok | US',
'Spotify Premium | mistersmith33:bigtymer | US',
'Family Member | carolinelinton9@hotmail.com:Monkeys1 | AU',
'Family Member | kinia3c@gmail.com:kangur28 | PL',
'Spotify Premium | michalfk1986@gmail.com:michal00 | IL',
'Spotify Premium Duo | vadu79@hotmail.com:Mariposa0 | MX',
'Family Member | magikoip@gmail.com:skooljuly7 | US',
'Spotify Premium | Raberkira@gmail.com:dana1998 | IL',
'Spotify Premium | bethell8:Sandee08 | US',
'Family Member | monthenolmarieambre@gmail.com:marieambre | FR',
'Spotify Premium | lckavanagh@gmail.com:Clare615 | US',
'Family Member | tvancampsgonz@gmail.com:1995agosto17 | US',
'Family Member | mcatarinar@hotmail.com:mcrocha24 | PT',
'Family Member | evi-ba@hotmail.de:isenseven | DE',
'Premium for Students | ninouch09@live.fr:Skylla09 | FR',
'Spotify Premium | srenshaw97@hotmail.com:boris813 | GB',
'Spotify Premium | bremc1996@gmail.com:justinb4me | US',
'Family Member | dianaqm80@hotmail.com:amaneceres | CO',
'Family Member | clairedrv0@gmail.com:airsoftfq1 | FR',
'Spotify Premium | sallydee88@gmail.com:harajuku | AU',
'Premium for Students | justin.kane@web.de:AleSSandro07 | DE',
'Family Member | nurvardarfenercioglu@gmail.com:sevde1989 | TR',
'Premium for Students | kleine-chrisi@hotmail.de:ballerina | DE',
'Spotify Premium | elawainer.94@gmail.com:09091994 | IL',
'Family Member | penny22@talktalk.net:sniggers22 | GB',
'Spotify Premium | aideenmcmanus@hotmail.co.uk:aideen00 | GB',
'Family Member | elly.ferrell@gmail.com:carter123 | US',
'Spotify Premium | ana_venta@hotmail.com:aeim0107 | DO',
'Premium for Students | tdailey3269@gmail.com:Dai117927 | US',
'Family Member | lola.deloy@outlook.fr:Monnougat1 | FR',
'Family Member | kmvalenta@yahoo.com:hawkeye1 | US',
'Spotify Premium | PaulTarlevs@hotmail.com:335835807pT! | CA',
'Family Member | lucia.aznar21@gmail.com:sanjuanbautista | ES',
'Family Member | feigenwinterannina@gmail.com:annina14 | CH',
'Spotify Premium | matt_hawkins_golf@hotmail.co.uk:Matthew97 | GB',
'Family Member | emma.mingazzini@gmx.de:Thyson04 | DE',
'Family Member | selensky.nia@gmail.com:Milchreis | DE',
'Family Member | nicoleobrien57567@gmail.com:webkinzs12 | US',
'Spotify Premium | resabri@gmail.com:sabri1980 | AR',
'Family Member | verosubire@gmail.com:22081984 | ES',
'Premium for Students | evleslie@hotmail.com:peepsels13 | AU',
'Family Member | lindemertel@gmail.com:ohmygosh33 | US',
'Family Member | mbrock@hotmail.com.au:Caidence3 | AU',
'Spotify Premium | markhamgp@hotmail.com:Aussie123 | GB',
'Family Member | monika.milkintaite@gmail.com:milkintaite | LT',
'Spotify Premium | owllover.hudson2:moriah1998 | AU',
'Spotify Premium | merethe.bang@gmail.com:Meban1968 | NO',
'Family Member | itziargp15@gmail.com:verano2012 | ES',
'Family Member | queenieb.no1@gmail.com:keanu2007 | GB',
'Family Member | askformichelle@yahoo.com:LaQuinta1 | US',
'Family Member | vania.canossa96@gmail.com:patricia15 | FR',
'Family Member | mainsondheim@gmail.com:sg140863 | DE',
'Spotify Premium | Eva.lochbronner1998@gmail.com:xxlove98 | DE',
'Family Member | luciaperezdsb@gmail.com:jara1998 | ES',
'Family Member | lenny96@outlook.de:!lina1996! | DE',
'Family Member | clairepen@me.com:clothes7 | US',
'Spotify Premium | simonesim144@gmail.com:Simone12 | AU',
'Spotify Premium | isabella.dorin@gmx.de:linkinpark11 | DE',
'Family Member | fanyprincce@gmail.com:stephania123 | MX',
'Family Member | tanya.rimell@gmail.com:spongebob | US',
'Family Member | evachan829@yahoo.com.hk:iloveyou96 | HK',
'Family Member | perrineprr@aol.com:Emma1234 | GB',
'Family Member | evamontielm@telefonica.net:montielillas | ES',
'Family Member | valenzuelariel@hotmail.com:youngboss | US',
'Family Member | zoellerdawn@yahoo.com:34533453 | US',
'Spotify Premium | marylinpardo@gmail.com:igal2101 | CL',
'Family Member | kikischneider@koeln.de:2010svsv | DE',
'Family Member | simoalvesmadrid2211@hotmail.es:bruce2211 | ES',
'Family Member | anibalberrubenavides@gmail.com:5050106xl | ES',
'Family Member | giulia.florian3@gmail.com:sticazzi | CA',
'Family Member | kerstin.23@live.de:KS20092013 | DE',
'Spotify Premium | marianaabergcobo@yahoo.com:parera68 | UY',
'Family Member | nyratulangi@gmail.com:LimLiCi82 | ID',
'Spotify Premium | jamesjodie@hotmail.co.uk:Oliver08 | GB',
'Family Member | isabella.timpanaro@gmx.net:knut2012 | DE',
'Spotify Premium | Rosalba.sorintano@yahoo.com:Topolino96 | IT',
'Family Member | janeynicholls@gmail.com:Charlie001 | AU',
'Family Member | verenajoswig@hotmail.de:Verena1992 | DE',
'Family Member | celinaglammer@web.de:04072000 | DE',
'Spotify Premium with Hulu | e.santamaria1:sanla408 | US',
'Family Member | kellyhoath@hotmail.com:zdziech3 | AU',
'Family Member | mimi13k@aol.com:kinkajou13 | US',
'Family Member | hilke.janssen@hotmail.de:autobahn | DE',
'Family Member | joelleguisti@gmail.com:Jgu?st?1 | US',
'Family Member | tam.mc.81@hotmail.com:hayley16 | AU',
'Family Member | erikagreenephoto@gmail.com:Elephante5 | US',
'Premium for Students | anschub@hotmail.com:Paprika13 | DE',
'Spotify Premium | clydetyler21@gmail.com:Isabella2009 | US',
'Spotify Premium | gdmc81@gmail.com:pa55word | GB',
'Spotify Premium with Hulu | acventers@yahoo.com:bam2him13 | US',
'Family Member | eriglezlemoniz@gmx.es:13081980 | ES',
'Family Member | nicolekocher@web.de:Schweini7 | DE',
'Family Member | denizgulebasti@gmail.com:bendeniz1997 | TR',
'Family Member | littlepitu@Yahoo.es:littlepitu | ES',
'Spotify Premium | vrancianuioanv@gmail.com:27august2002 | DE',
'Spotify Premium | Kirstenstokesberry3@hotmail.com:Eleph4nt10 | GB',
'Family Member | ffisches@gmail.com:Franzi123 | DE',
'Spotify Premium | zhanzhihao@gmail.com:Haohao989 | SG',
'Family Member | saeteurn1993@yahoo.com:Quiznos3 | US',
'Family Member | oceane.guiton@gmail.com:03111998 | FR',
'Family Member | alicemidali88@icloud.com:scelta11 | IT',
'Spotify Premium | m.buttimore@tubetech.co.nz:sebash123 | NZ',
'Family Member | jessie.kalisi@hotmail.com:leuatea1 | AU',
'Premium for Students | ivan.yepez.07@gmail.com:Pinkman.7 | MX',
'Family Member | stephellsey@yahoo.com:Samantha1 | US',
'Family Member | sabrinafrefre@gmx.de:compaq321 | DE',
'Family Member | Isabel.rose742@gmail.com:clubpenguin | GB',
'Family Member | Angelina-Schmidt1990@gmx.net:melia2012 | DE',
'Family Member | Bree.debeaux@hotmail.com:William1912 | AU',
'Family Member | Skylar.losciale@icloud.com:Cheyenne32 | US',
'Family Member | Jenny.dell06@gmail.com:jennifer02 | FR',
'Family Member | luczakpauline@gmail.com:masoeurdamour | FR',
'Family Member | m-franke1995@hotmail.com:louise21 | AU',
'Family Member | maren.kromer@web.de:maren2314 | DE',
'Spotify Premium | helen.redogorarna@outlook.com:Dragstar1100 | SE',
'Family Member | fibranz@gmx.de:jimy1999 | DE',
'Family Member | gracie.pacie@hotmail.com:Lovedove1 | CA',
'Family Member | fkkbella@gmail.com:60331238 | HK',
'Family Member | africanuezfernandez@hotmail.com:gorka123 | ES',
'Family Member | oihane.u@gmail.com:vi7492jk | ES',
'Spotify Premium with Hulu | fewjr5@comcast.net:oscar357 | US',
'Family Member | annamhosking@gmail.com:181116am | AU',
'Family Member | brookelee1995@hotmail.com:brooke07 | AU',
'Spotify Premium | alessialocatelli906@gmail.com:lochi1999 | IT',
'Premium for Students | vertikachandra29@gmail.com:Vertik@7 | AU',
'Family Member | gracepretty00@gmail.com:Apples361 | CA',
'Family Member | sarahmalto14@yahoo.es:puchimidu24 | ES',
'Family Member | vie.manon22@gmail.com:25101997 | FR',
'Spotify Premium | nastya.markov@gmail.com:ilove2shop | IL',
'Family Member | susanna.gar@gmail.com:49124912 | ES',
'Spotify Premium | deannemaree@live.com:Riley2000 | AU',
'Spotify Premium | camilla_bauer@jubii.dk:cb27326738 | DK',
'Spotify Premium | jessicafreese1995@gmail.com:Jfreese95 | AU',
'Spotify Premium | maalii777ii@gmail.com:ilovemom77 | KW',
'Family Member | ani.vanucci@gmail.com:melarossa | IT',
'Premium for Students | tobias.bartl@freenet.de:Robben10 | DE',
'Family Member | enarap.19@gmail.com:barca1019 | ES',
'Family Member | mickeyzimm01@hotmail.com:teddybear82! | US',
'Spotify Premium | rottiman1994@web.de:Alex1994 | DE',
'Family Member | rouquine38@outlook.fr:elinette38 | FR',
'Family Member | kaspar.arielle@gmail.com:16121991 | FR',
'Family Member | kirsty.brownell@yahoo.com:Kbisom91 | US',
'Spotify Premium | woodfish@seznam.cz:hoblinka | CZ',
'Family Member | katieharbold@yahoo.com:Samantha123 | US',
'Family Member | sufikarin@gmail.com:krep2007 | DK',
'Spotify Premium with Hulu | hishamrebani@gmail.com:Melanie3722! | US',
'Family Member | sandymartin33@gmail.com:05071529 | FR',
'Family Member | sheree.pratt@activ8.net.au:Groove12 | AU',
'Family Member | ashlymccracken@msn.com:Ashly396925 | US',
'Family Member | dzap.coruna@gmail.com:27041978 | ES',
'Family Member | amandinedecerier@aol.fr:herbiere | FR',
'Spotify Premium with Hulu | arred.mayra@gmail.com:maiira90 | US',
'Spotify Premium | taknyn3221@gmail.com:M6teen123 | US',
'Spotify Premium | eaddy612@yahoo.com:adidas21 | US',
'Family Member | erickajoann@gmail.com:Hcedrb06 | US',
'Family Member | aline.masseno@hotmail.com:aw36f7gv | BR',
'Family Member | doreau.melanie@hotmail.fr:23072011 | FR',
'Family Member | akimhazanati@gmail.com:kadafichamas | FR',
'Family Member | vastitang@gmail.com:09102626vV | HK',
'Spotify Premium | tutigarcia654@gmail.com:v1olence | BR',
'Family Member | m.kaya25@gmx.de:Kaya4526 | DE',
'Spotify Premium | arlynepulido:arlynepulido | US',
'Spotify Premium | a.herrmann@serviceplan.fr:Achille98 | FR',
'Family Member | ailuj.yad@gmail.com:jiejietheknocker | US',
'Family Member | federici.alessia@gmail.com:Alepier99 | GB',
'Family Member | csujardelarosa@gmail.com:cris1821 | ES',
'Spotify Premium | apfischer87@yahoo.com:TheVille87 | US',
'Spotify Premium | rebekius_18@hotmail.com:valdivielso | ES',
'Spotify Premium | jsandberg80@yahoo.com:maggie03 | US',
'Family Member | bedhead-nicole@web.de:meister2010 | DE',
'Spotify Premium with Hulu | gabby0312@icloud.com:gabby0312 | US',
'Family Member | brooke.herron@yahoo.com:Angel123hope | US',
'Family Member | B.schlorf@gmx.de:krankenschwester | DE',
'Family Member | maaisieemolo14@gmail.com:Maisie27 | GB',
'Family Member | jemimasjj@gmail.com:ilovepeople | CA',
'Spotify Premium | oliviadouglas216@gmail.com:fruity555 | CA',
'Premium for Students | andreamartina0601@gmail.com:andreamartina0601 | IT',
'Spotify Premium | joela.montaniel@gmail.com:Pareko.28 | PH',
'Family Member | anja.weigel77@googlemail.com:ameise77 | DE',
'Family Member | a_ma.sur@hotmail.co.jp:luv2KATZE | JP',
'Family Member | nicole@planitevents.net:partygirl2016 | US',
'Family Member | tamfernandez99@gmail.com:amore138892 | ES',
'Family Member | christin.tietgen@t-online.de:Leberwurst08 | DE',
'Family Member | alexandra.steinbrunner@web.de:alex1234 | DE',
'Family Member | lisa-vinaev@hotmail.com:23thorns | AU',
'Family Member | angela.hahn1986@web.de:Piesepampel86 | DE',
'Family Member | benjamintiff@gmail.com:schuyler71 | US',
'Family Member | dfranklin60@googlemail.com:jerone29 | GB',
'Spotify Premium | mikkelmusiker:808080 | DK',
'Spotify Premium | queenvik2000:Popsicle4 | US',
'Family Member | phoebesm03@gmail.com:SiennaMoon18 | GB',
'Spotify Premium | dylan_magrin:dasher12 | AU',
'Premium for Students | andreamartina0601:andreamartina0601 | IT',
'Spotify Premium | barbziuliano:taco030892 | US',
'Family Member | mary.mirando@hotmail.com:marymirando | US',
'Premium for Students | amandaago123@aol.com:pinkipi10 | US',
'Family Member | tara.harrison@ncl.gdst.net:Th270601 | GB',
'Spotify Premium | jessicaspringett@hotmail.co.uk:Anyaanya875 | GB',
'Spotify Premium | soleloza16:soleloza16 | AR',
'Family Member | mdmercer97@gmail.com:Pass_word3 | GB',
'Family Member | sten.syvertsen@me.com:knok3987 | NO',
'Family Member | valerielunar:solyluna | AR',
'Spotify Premium | hayhols@hotmail.co.uk:Gibson31 | GB',
'Family Member | jessportashills97@gmail.com:cooking1234 | AU',
'Spotify Premium | brigittaritter:und6dannso | DE',
'Spotify Premium | soph_tetz:jordan1423 | AU',
'Spotify Premium | dijhendry:bonjovi22 | GB',
'Family Member | juliabechthold@gmx.de:Katerchen1_1 | DE',
'Family Member | matildeandreoli61@gmail.com:sassolini7 | IT',
'Spotify Premium | yibrani:alabama05 | MX',
'Spotify Premium | danielmsiller:mexico2012 | MX',
'Spotify Premium | karinaaguerrero:luana2006 | AR',
'Family Member | swtbabymilk@gmail.com:mae69tim | US',
'Family Member | jlholt690@gmail.com:minicooper | US',
'Family Member | ellie.price98@hotmail.com:smirnoff98 | AU',
'Spotify Premium | sammyyiee@live.com:May199628 | CA',
'Spotify Premium | emilycanner:ec407876 | US',
'Spotify Premium | stevierofl@hotmail.com:davinadavina | DE',
'Spotify Premium | heidrunfink:Heidi1908 | DE',
'Family Member | clementina_verlucca@yahoo.it:Mariasofia99 | IT',
'Spotify Premium | jbraziel:jacob6810 | US',
'Family Member | alexbhm267@gmail.com:Waldtier | DE',
'Family Member | ccatherine14@ymail.com:cynthia14920 | FR',
'Spotify Premium | ataevanazira506@gmail.com:naziro4ka | AE',
'Spotify Premium | fadurazo:durazo52 | MX',
'Family Member | rameishadc@hotmail.com:Superman01 | GB',
'Family Member | info@latiendadeyaya.com:10041204 | ES',
'Family Member | lenachust@gmail.com:23101996 | ES',
'Spotify Premium | marthablancop@gmail.com:feijoo68 | ES',
'Family Member | taylorcull@hotmail.com:sierrasimone4 | AU',
'Family Member | lorenzoesma@gmail.com:pinocho22 | ES',
'Spotify Premium | sawelliott@yahoo.ca:Absalom1 | CA',
'Spotify Premium | anitasmith0123@gmail.com:Bfl282403 | AU',
'Family Member | marusarquis@me.com:53735373 | MX',
'Family Member | giuliapetroni@hotmail.it:maya1988 | IT']


netflix = ['Premimum users only your teir-free contact @mistermartin#1614 if this is a mistake']

Nord = ['Temporialy out of stock']

Crunchyroll = ['Premimum users only your teir-free contact @mistermartin#1614 if this is a mistake']

Hulu = [' HHHancock@ymail.com:hhh1997',
' DerickTR@hotmail.com:DtR262001',
' SebastianAndrade531@aol.com:Teddy5422',
' Abriana.wade@aol.com:crazy526',
' 6dayna6YT@gmail.com:dimmie',
' RaineAsaurus@gmail.com:raine7474',
' Austinlubniewski32@gmail.com:Aj070299',
' 17winkelman@gmail.com:xn87xn87',
' SteveVSGaming1500@Gmail.com:07222005',
' Annabelljohnson12@gmail.com:bigtime5sos',
' David.fosman12@gmail.com:Dabybaby12',
' Salma0207@yahoo.com:sa1234567',
' Golden5Directioner@gmail.com:stephanie1902',
' Delta.McDaniels@gmail.com:07319815',
' DecimateGaming21@gmail.com:tryhard21',
' 511niknak@gmail.com:niknak511',
' DanielSanchez1510@gmail.com:Baseball510',
' a_rojas59@yahoo.com:chefy015',
' Adrian.harmaty@Gmail.com:apple1976',
' Paigeevans42@gmail.com:gokarts8',
' abby98queen@yahoo.com:lucy3901',
' RobynandMunch@yahoo.com:Pizza4ever',
' JDavis22dueceduece@gmail.com:jaggymomo',
' Banshee.dune.angel@gmail.com:slingsand1',
' Garretbird34@yahoo.com:rr123456789',
' acshampine@gmail.com:Cameron1996',
' abigailbien04@gmail.com:decaturil',
' 5050tarheel@gmail.com:765606',
' JonathanHiggins1999@gmail.com:682604',
' abccampbell96@gmail.com:jesus1225',
' abchicklm@yahoo.com:Scc022695',
' Amen774@hotmail.com:amen1940',
' aemitchel@msn.com:4496flgsb',
' aconklin19962015@gmail.com:Plymouth2015',
' Alyjoanna25@gmail.com:niners25',
' Derekbenji.8@gmail.com:iloveBYU123',
' ahanyok13@gmail.com:welcome01',
' a.mac1@live.com:913163115Ap',
' Mitochuchundra@gmail.com:pineapple511',
' Oliviabrusik@yahoo.com:Chuchi28600',
' adamtish@hotmail.com:addison28',
' Sandra.kaycee@gmail.com:1doodle',
' abby.ossola@aol.com:muffinhank1',
' aeiou-y@comcast.net:annelise',
' Brandonthom@hotmail.com:9823017',
' adamshemesh2013@gmail.com:base2002',
' Pleaseyolo26@gmail.com:pleaseyolo',
' Mohamed.bouqfa@hotmail.com:12461964',
' abru326@yahoo.com:pookie1',
' Calep1234@gmail.com:Caleparks2',
' Dmarkham92@yahoo.com:Joplin2012',
' affarin21@gmail.com:Nia12345',
' afsam10@aol.com:white4ever',
' abbieala@yahoo.com:rrtcbo',
' 116trip@gmail.com:fowler101',
' alec.nayder@gmail.com:nayder68',
' albasinidaniel213@gmail.com:weakling2',
' Lochlan.hendrix@gmail.com:M0tekum!',
' Kobe.Terry809@Gmail.com:blade809',
' airiellee@yahoo.com:cookies123',
' VENOM157ENERGEY@gmx.com:Ikillonme2@',
' alexander7185@gmail.com:warriors7185',
' Liam.13@me.com:Droopy150']

Pornhub = ['Premimum users only your teir-free contact @mistermartin#1614 if this is a mistake']

Fortnite = ['kwfrizz9095@gmail.com:loveya9095',
'wojcebr@o2.pl:Zapomn1alem1',
'chargersrock32@gmail.com:shooter1',
'aolson17@comcast.net:Ieatfood17',
'luca_bulfy@icloud.com:Luchino00',
'kcamejo03@gmail.com:cupcake123',
'nizardo1@yahoo.com.au:quagmire3359',
'lutzh04@gmail.com:basketball24',
'mohammed.mekki@gmail.com:zol4life',
'kirill-kovalenko-98@inbox.ru:Enutap323',
'delaneymarie27@yahoo.com:softball27',
'liamroc99@gmail.com:Iggy2018',
'g.allen97@btinternet.com:Minniedog1',
'reedherring3@gmail.com:Catdog12#',
'dsstein03@gmail.com:hagotem1',
'navedog@web.de:Ofmight123',
'markiewicz.12@osu.edu:Maddox614',
'chris_b_7@live.co.uk:mobile777',
'pedropalacioestrada@gmail.com:bobesponja1',
'Leonelmarquez1995@hotmail.com:a4b5d3321b',
'henning1142@gmail.com:Xagct80=',
'dylan1941@hotmail.fr:Ethanguy10',
'chrisz1382@gmail.com:jeep197',
'averland.manoon@gmail.com:plancton0609',
'xavier410@icloud.com:tigerbmx12',
'abertsch@bu.edu:boston2019',
'erinjulia14@yahoo.com:Pookapoo14',
'prussiluskan_2@hotmail.com:a1l2e3x4',
'aechin@live.com:ashley05',
'Carlos.h115@yahoo.com:Spartan91',
'starrider335@gmail.com:Cordude102',
'matthewpierce95@gmail.com:thomas1995',
'adri.soldati@gmail.com:sld65rta',
'jaudino27@gmail.com:Ilovebella<3',
'swgiordano@gmail.com:susan8023',
'mariajonesrn@gmail.com:Pumpkin1',
'evansdanell@gmail.com:Allenive7',
'natszapo@me.com:Sophia4me',
'dylanwise@hotmail.com:is2sign2b',
'viking0817@verizon.net:littleE8',
'alextremblay.at@gmail.com:90095abc',
'mikkelras03@hotmail.com:messi010',
'davenport.charity@yahoo.com:Christian1',
'jessicacflanagan@gmail.com:Jdcf1976',
'nazariypogo@gmail.com:Pogoriliy1',
'back_n_black2257@yahoo.com:Broken34',
'sdmxwell@gmail.com:lynette127',
'doddydodd44@yahoo.com:Peopleluke1',
'sotostriant@hotmail.com:sotirakis1',
'evansdanell@gmail.com:Allenive7',
'domenickzack@gmail.com:#5baby#5baby',
'bethaniebentley@yahoo.com:Brandon22',
'matthewschenck@yahoo.com:puccini1',
'g3.downey@gmail.com:candybabe3',
'alexx0629@gmail.com:portland0629',
'danielcha670@gmail.com:thefuture1',
'trippgrebe@gmail.com:tripper00',
'roenejwl@gmail.com:altwall1',
'bjohnston1015@gmail.com:Todd0407',
'gottenkss@gmail.com:trunks2',
'deajahredd@gmail.com:mermaidsrule4ever',
'helloworld364425@gmail.com:Thefran11',
'jacobbach03@gmail.com:Khn68ktz',
'runhoops09@hotmail.com:runhoops09',
'damonb75@gmail.com:Scrulla1',
'lucky_paty2003@yahoo.com:mlounge7',
'nathan.steltzer@gmail.com:laxsoccercheez10',
'cwtucky2@gmail.com:doglover1',
'nicolastzakal@gmail.com:nikolas2001',
'kaileyb888@gmail.com:Alexa886',
'alexmartinunited@hotmail.com:Rooney56',
'jerricahassan@gmail.com:Mohamed1',
'o.cashaw@yahoo.com:ocashaw14',
'jamesfmiranda@gmail.com:Tigger1',
'merricka92@gmail.com:williams27',
'MarekSkibinski@seznam.cz:Marek2004',
'alexissattler@hotmail.com:Djvana05',
'rachelmolloy@googlemail.com:nich0las',
'john.leblanc04@gmail.com:Wrestling4life',
'benzema_9@hotmail.de:lollipop040',
'Mitchellr161@gmail.com:Damien2214',
'joe.p.oconnell@gmail.com:emc2007',
'sam.stephens63@yahoo.com:sammyjo123',
'aliciafieldsend@gmail.com:hunnybunny1',
'trocome2@gmail.com:lace1234',
'paulwkjeong@gmail.com:dndzlwjd90',
'd.acevedo97@gmail.com:Darrian1',
'jnloftus@hotmail.com:nikosha1',
'keelyreeseoliver@hotmail.com:netball123',
'mesilla.cordes@gmail.com:Blueberry1',
'deutsch.bryan@gmail.com:wehner11',
'nerearomanrg@hotmail.com:Nerearoman123',
'maddy.critz@gmail.com:Haileyo1',
'elvinmeherremli55@gmail.com:elvin29492',
'fmaverick72@gmail.com:beerclub300',
'bribunnell@gmail.com:Bike0525',
'kamilja2000@o2.pl:Kokakolaxd123',
'mayayagdjan@gmail.com:asdasd234234',
'Briannakathleen2@gmail.com:Brianna1998',
'stephanie.agudelo2@gmail.com:cherry2',
'dforest09@yahoo.com:Abby4est',
'maxmorgan8@mac.com:rootbeer8',
'belkins4596@yahoo.com:peaceouty5',
'michael.l.tree@gmail.com:Sandra666',
'ernestd19@gmail.com:yahoo1997',
'beckybrown89@hotmail.co.uk:Kalsey2009',
'stoussaint5@gmail.com:248dancer',
'zacdonohue25@outlook.com:phenom300',
'djkv11@comcast.net:Dioneseus300',
'alandaniels30@hotmail.co.uk:danie0762',
'Ricardo.moral@gmail.com:Windward0',
'mcdermottfarm@gmail.com:Kaseybailea1',
's_bruckner@yahoo.com:Fargnoli08',
'shanedbreneiser@gmail.com:Incorrect1',
'vehbicantabakci@hotmail.co.uk:Johnny12',
'jandodd@verizon.net:billydodd4',
'esper0407@yahoo.com:Ericd120204',
'harperdeagan@hotmail.com:Rhianni1',
'teamjacob13@comcast.net:qawvey8mjp',
'suyalcin@icloud.com:sudeyalcin123',
'tdevos0710@gmail.com:Angel0718',
'ktempler@att.net:templer5',
'ka_worsham97@yahoo.com:outlaws1',
'calv_31@hotmail.com:k44axmg',
'sirtak@hotmail.com:lollol1',
'dletspleyshik@bk.ru:4617891dima',
'susina90@live.it:Aerosmith1',
'natroke@gmail.com:Lolipop12',
'mattjdetrick@gmail.com:bowler123',
'dru322005@yahoo.com:Mailman36',
'coiltjs@gmail.com:happy111',
'laurenliz445@gmail.com:lollypop890',
'angelinadb44@gmail.com:angie4248',
'ejimcook@gmail.com:Escondido2',
'btmf@hotmail.co.uk:B0llocks!',
'ridl340@gmail.com:Alucard1',
'chelseataylor69@icloud.com:chelsea5678',
'Twinmommy2005@hotmail.com:Billys2005',
'julidemato@hotmail.com:Batista1',
'reile@theracinglife.com:sailer76',
'oconnellby7@gmail.com:Yvesyvesyves40',
'gtamir_2005@hotmail.com:Senturion1',
'sscruggs@joaquinisd.net:Dennis11',
'charelvhaarst@icloud.com:Kedingen05',
'joker7072@gmail.com:action123',
'tristeonz@hotmail.com:Polkaudio2',
'chastain_christian@hotmail.com:cy2db5802',
'louna.dasilvaneves@sfr.fr:0112loulou',
'matt.h.drake@gmail.com:Orange13',
'hvanessa2000@gmail.com:052514Cv',
'osw_3000@hotmail.com:chores23',
'yoshinon193@outlook.com:YOSHINON12',
'slavon072004@gmail.com:07032004sf',
'mjenkins059@gmail.com:Nwu59tke',
'pierre.ulrich@yahoo.fr:Logitech02',
'chana.arvinder@hotmail.com:Chana987',
'peaceoutbreanna@gmail.com:Tobynme2',
'dili167@hotmail.com:kosova22',
'katiepringle1@hotmail.com:jamie2307',
'gpollina12@gmail.com:froger56',
'cassidywilson99@gmail.com:JKVYgqs4',
'koltenh37@gmail.com:ACfootball19',
'laurenree23@yahoo.com:password3',
'salopo100@gmail.com:Senha123',
'wilfred_wong12@hotmail.com:abc12345',
'camwitt9@gmail.com:Superstump!24',
'chefkeifus@gmail.com:W219@c4v',
'samuel.stevewinkki@gmail.com:samsam2709',
'augusto_eston@hotmail.com:augusto3',
'mvowles11@gmail.com:m4th3wwv',
'evanthand8@gmail.com:Stampy89',
'zorahb12@gmail.com:Lanai125',
'vip333-n-@hotmail.com:Rrtt1243',
'erhanaydogan_1903@hotmail.com:e5936085',
'tjhewittjr@gmail.com:elpissis1',
'sebastianproudfoot@yahoo.com:Whitewindow1',
'juliehowieson@yahoo.co.uk:jayden12',
'thecool1204@gmail.com:minecraft1',
'hariezsaifuddin15@cempaka.edu.my:kumbaya9500',
'nathanjc64@gmail.com:power2dappl',
'wduplessie@gmail.com:coralreef1',
'singerscreamer@yahoo.com:Mustang1',
'Nbennett0531@yahoo.com:Breeanna414',
'michaelandange@yahoo.co.nz:angela01',
'mat.burleigh@hotmail.com:bacon101',
'Ethan2004k@gmail.com:orange1532',
'giuliamdqf@me.com:Gf649874',
'lego1710@naver.com:maybe1710',
'diogenesfronza@gmail.com:giselle1234',
'smjbrinkmann@hotmail.com:sa5mantha',
'eddycarillo7@gmail.com:Converse69',
'dylanwiyninger@yahoo.com:Bobstoops1',
'cnbrigby@yahoo.co.uk:Standish40',
'Mgbuzzer7@gmail.com:Mgbuzzer6',
'nsorrenty@yahoo.com:Tucker33',
'mayjune1998@gmail.com:BFRTVWYn1998',
'belduff@gmail.com:oscarmolly08',
'tyndallbridgette@yahoo.com:Marcus1234',
'shawn.lee@comcast.net:ShawnALee123',
'tawai808boiii@gmail.com:Swerg123',
'keek92@yahoo.com:Ojackson21',
'llymlrs@gmail.com:greenday1',
'arvid.nilzzon@hotmail.com:norrland37',
'Kellowryan@yahoo.co.uk:Millie01',
'ariellenore@gmail.com:Lenore5456',
'radostmilkova@yahoo.co.uk:Radost1Jan2',
'michael.dicosola@ubs.com:loyola99',
'iman213@hotmail.co.uk:starshine123',
'cody-crook@att.net:Drosemvp1',
'mengyan_drew@outlook.com:yan890711',
'janjicm02@gmail.com:markocar2003',
'nalejand@yahoo.com:toonsquad1',
'quentinaubert15@gmail.com:QuentiN15',
'lbeth93@live.com:93ldBlux',
'gentzkowgreg@gmail.com:Thewedding479!',
'sedlacekjake@gmail.com:duckhunter994',
'lemkee@web.de:Eric199808',
'Jon.berge@yahoo.com:stumpy123',
'cjmoazed@gmail.com:lobster1',
'rnicholls1984@aol.co.uk:johnson1984',
'janardhunv@gmail.com:jamunarani123',
'm.rodriguez421@yahoo.com:muse421',
'ines.nakhiil@icloud.com:nakhil370',
'sem17.06@mail.ru:Rjdijdjq429228',
'joaopedroeiti11watanabe@outlook.com:Watanabe10',
'adeprisma7@gmail.com:ade041096',
'mtgor00@gmail.com:nikitos00',
'che.richardson@gmail.com:Noodles123',
'mattimeurisse@hotmail.com:schaduwspel1',
'simpleconcept27@gmail.com:liampt27',
'janv2007@gmail.com:Jorge9494',
'mckendy007@gmail.com:Penster2',
'zoebear2014@gmail.com:Zoeb2005',
'4kerbows@gmail.com:tatum1981',
'radwanleila@gmail.com:leilarox123',
'lgeisheimer@gmail.com:Lmgkmg6!',
'eren2000gs@gmail.com:eren2000',
'agusdeotto@hotmail.com:marsoloman1',
'holm@hjk.net:Krieger123',
'garyod40@hotmail.com:seamusfionn1',
'trcykirk@yahoo.com:Pistols118',
'benaissasofiane@gmail.com:cassandra31',
'armourxbot@gmail.com:mon4pate',
'johnnychimpo321@gmail.com:lilmitro1',
'kerzman.a@gmail.com:Loveprefuse1987',
'mahirzaman855@gmail.com:salik136',
'thatduke005@yahoo.com:chelson15',
'billypeas65@gmail.com:promise2',
'joergminden@gmail.com:mage0608',
'rustywilliams7@gmail.com:Rusty7502',
'winterknow66@gmail.com:ilyasderdouri123',
'gclegguk@yahoo.co.uk:Elise110207',
'wierdcraigg@gmail.com:naruto1386',
'jmstroh03@hotmail.com:Kate0821',
'tomes167@yahoo.com:Ironcity1',
'mantas8b@gmail.com:sidabras123',
'karlwatson@mac.com:Fandang069',
'shayla.28@hotmail.com:La28niece',
'brandonradford13@yahoo.com:dietcoke13',
'brownit@live.co.uk:Megapode92',
'cullenfletcher97@gmail.com:pie1pie2',
'acastro_0@hotmail.com:0vergil0',
'mrossiter13@yahoo.co.uk:Cardiff13',
'matt_thebaptist@yahoo.co.uk:Oxfordroad14',
'arringtonmc@gmail.com:Inhoc09',
'jdavenport1975@yahoo.com:Soul6175',
'blade_cb32@hotmail.com:Welcome1',
'kazoom-h@hotmail.com:8124746df',
'ryanstrausbaugh54@gmail.com:gordon2401',
'visanflorin23@yahoo.com:Mercedez11',
'pasha-platonov-2000@mail.ru:paha1727',
'cooperpritchett65@gmail.com:Warrior65',
'aaronmatthew2011@gmail.com:Loki1414',
'bguerra121@gmail.com:Taekwondo540',
'b.hegewald@icloud.com:Ghostwoman16',
'shmellbee@gmail.com:Dukenukem1',
'aadropic@yahoo.com:dramanda1',
'angel559gonzales@gmail.com:greenapples1',
'nicki.xx@hotmail.co.uk:st3v3na11',
'izzysanchezx@gmail.com:pizza123',
'christopher_russo@hotmail.com:advocate1',
'lauriux91@gmail.com:lauriux37',
'levijoll123@gmail.com:aikoAB15',
'mandis_01@hotmail.se:badkar15',
'intothemouthoftheleviathan@gmail.com:Lily2007!',
'xvx.ozzy@gmail.com:Princessoz1',
'mbrundage22@gmail.com:Bungie22',
'c.allenharrell@gmail.com:dingodog1',
'flyby@swissonline.ch:kermis12',
'josephsmithrn@aol.com:joscxs1',
'poyitoconmonkey@gmail.com:Nayeli2003',
'dominik.pikon@onet.eu:Dominikos66',
'ichigonyt@gmail.com:beyblade2113',
'anna4medarts@gmail.com:Marysia2011',
'sa124511@gmail.com:zx124511',
'juliaclaire.v@gmail.com:littlebike1',
'ehomish1517@gmail.com:Chrispaul3',
'porthos.lopez@gmail.com:Whatever1',
'mkbringewatt@msn.com:612735mb',
'marcostutts@yahoo.com:marcoman63',
'stolarchuk_allison@hotmail.com:911yearfriends',
'01.06.87.akv@mail.ru:andrs1987',
'jmchaple@yahoo.com:Lovesing1',
'sam.walker5@verizon.net:rexandcera5',
'ang.manywounds@gmail.com:Ryker2010',
'bcromer07@gmail.com:Bl00domen',
'pablo.almussafes@gmail.com:Likeaboss2',
'antti.nurmi87@gmail.com:1234qwer',
'viky17@hotmail.fr:VACILLYZEITSEV1',
'danny650.DP@gmail.com:Zxop1230nm',
'janinanowakowski@gmail.com:Janina21',
'gagnonemily565@gmail.com:Spanky565',
'sethtyrbrunkow@gmail.com:america22',
'capt.rjackson@gmail.com:Geo2oo9rj',
'maria_lteif@hotmail.com:corner123',
'jbarrettsemail@gmail.com:jbb666ftw',
'jennaammons18@gmail.com:J12e4n00',
'jujuloiret@gmail.com:kacahuet1',
'kylesemail7@gmail.com:Singingaknb7',
'gvasi11@aol.com:gabriella11',
'erick103@gmail.com:Stylusn1',
'madaleine.macrae@ntlworld.com:Sales023',
'raddie699@live.com.au:kerryn90',
'patrickpmoreira@gmail.com:Mz5znqkc',
'mh63325@gmail.com:H703164m',
'geuthxmaxime@hotmail.com:fongo123',
'arielvaldes.contact@gmail.com:Eltr4b4j0',
'trevor_spillane@yahoo.com:soccer492',
'christvoutsi@gmail.com:christ14',
'djfdds@aol.com:badboy7682',
'babyjuice1@hotmail.com:Shelbimay2009',
'mtndew1069@att.net:nja92998',
'ben.f.roberts@gmail.com:Drwho123',
'thisisalongnumber@gmail.com:Gannondorf007',
'dbcheerleader4267@hotmail.com:Orange01',
'cannonja@mail.gvsu.edu:Flakeat2',
'jamie@5fischers.org:kitty02',
'przkurzela@wp.pl:legia1916',
'gjwfield@btinternet.com:Jllewys1',
'fatty_ada26@yahoo.com:guess321',
'chrisruiz2416@yahoo.com:supraking98',
'rachado14@yahoo.com:eastwood1',
'blizz_sc2@hotmail.com:pandoranet123',
'theimvik@outlook.com:jobb078430',
'lamn16@hotmail.com:123Apple',
'abeleleven@gmail.com:Arsenal11',
'suicideandre@gmail.com:andre3242',
'chaney_15@yahoo.com:Kayla729007',
'roby16ROBI@gmail.com:Maxpyne69',
'rileysmith30@gmail.com:ribug11',
'qveenjanay11370@gmail.com:11370paris',
'andrewraso@hotmail.com:Raso1993',
'bjohnston1015@gmail.com:Todd0407',
'bmazzini@oi.com.br:panasonic1',
'bartekf1997@yahoo.de:aBcdefg1997',
'katetakahama@gmail.com:Animemusic3114',
'jamieann26cabiles.jac@gmail.com:Jami0378',
'lili.liqueur@live.com:albm07621',
'1999kirill@gmail.com:k09011999',
'bond.sadudeewong@gmail.com:bond2580',
'hmcewen87@gmail.com:shanewest1',
'tekknowledge83@gmail.com:Jas0ntw0',
'faithhopely123@gmail.com:haibai123',
'jshealy1994@gmail.com:wannabeadino222',
'rm48185@gmail.com:hunter7101',
'i-sacha@bigmir.net:06071972isacha',
'slkaralunas@gmail.com:Devereux5',
'i90zkiddd@aol.com:nyeem1110',
'amayhle@yahoo.com:May2486!',
'novinnovin191@gmail.com:Fanmagazine123',
'jayechao@yahoo.com:Chaozer5',
'christafout9922@yahoo.com:cfout9922',
'tzitkewicz@gmail.com:zitkewicz1',
'jackwakey1992@yahoo.co.uk:yingyang1',
'jamesfredwalker@gmail.com:Durant35mvp',
'heatherhall7755@gmail.com:lemieux37',
'mave004@gmail.com:manutd1129',
'mikaylatal08@gmail.com:mat92202',
'tan.klinudom@gmail.com:tankunn1',
'baileyicoffey17@gmail.com:baileyirene1',
'branbay228@hotmail.com:jasper24',
'mad75@comcast.net:Password2',
'michellecuaron1@gmail.com:Sun1shine',
'stenzel.robin@web.de:Decoudre1',
'braddick@teameximius.com:speakers2582']
    
Premium = ["Add premium guild id's here"]



logo = '''
 ███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████     ▄▄▄▄ ▓██   ██▓                            
▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀    ▓█████▄▒██  ██▒                            
▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███      ▒██▒ ▄██▒██ ██░                            
▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄    ▒██░█▀  ░ ▐██▓░                            
▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒   ░▓█  ▀█▓░ ██▒▓░                            
░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒                             
░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░   ▒░▒   ░▓██ ░▒░                             
░      ░     ░   ▒    ░ ░  ░    ░       ░    ░▒ ▒ ░░                              
       ░         ░  ░   ░       ░  ░    ░     ░ ░                                 
                      ░                      ░░ ░                                 
 ▄████▄   ▒█████  ▓█████▄ ▓█████  ▄████▄▓██   ██▓ ██▓███   ██░ ██ ▓█████  ██▀███  
▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▒██▀ ▀█ ▒██  ██▒▓██░  ██▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ▒▓█    ▄ ▒██ ██░▓██░ ██▓▒▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▐██▓░▒██▄█▓▒ ▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒▒ ▓███▀ ░░ ██▒▓░▒██▒ ░  ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░ ██▒▒▒ ▒▓▒░ ░  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░  ░  ▒  ▓██ ░▒░ ░▒ ░      ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
░        ░ ░ ░ ▒   ░ ░  ░    ░   ░       ▒ ▒ ░░  ░░        ░  ░░ ░   ░     ░░   ░ 
░ ░          ░ ░     ░       ░  ░░ ░     ░ ░               ░  ░  ░   ░  ░   ░     
░                  ░             ░       ░ ░              Discord Gen Bot                        
'''
print(Fore.RED + logo + Fore.RESET)
print(" ")
print(" ")
#print(Fore.LIGHTMAGENTA_EX + "Checking" + len(spotify) + "Spotify Accounts" + Fore.RESET)
print("Checking Spotify Accounts:", len(spotify))


named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%H:%M:%S", named_tuple)

                                    #You can chamge prefix
client = commands.Bot(command_prefix = "gen-" )

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Backup | Fully Secured"))
    print(Fore.RED + "CodeCypher " + Fore.RESET + "is the Main Creator")
    print(Fore.RESET + "[" + Fore.RED + 'Console' +Fore.RESET + '] ' + Fore.GREEN + f'{client.user} ' + Fore.RESET + 'has connected to Discord!')
    print('Discord.py Version: {}'.format(discord.__version__))


@client.command()
async def music(ctx):
    Spotify3 = discord.Embed(title="Here is your Spotify Account", description=random.choice(spotify), color=196336)
    Spotify3.set_footer(text="Made with ❤️ by The Evolution Team")
    await ctx.author.send(embed=Spotify3)


@client.command()
async def nordvpn(ctx):
        nordvpn = discord.Embed(title="Here is your NordVPN Account: ", description=random.choice(Nord), color=196336)
        nordvpn.set_footer(text="Made with ❤️ by mistermartin")
        await ctx.author.send(embed=nordvpn)

@client.command()
async def netflixacc(ctx):
        netflix1 = discord.Embed(title="Here is your Netflix Account: ", description=random.choice(netflix), color=196336)
        netflix1.set_footer(text="Made with ❤️ by mistermartin")
        await ctx.author.send(embed=netflix1)

@client.command()
async def huluacc(ctx):
        hulu1 = discord.Embed(title="Here is your Hulu Account: ", description=random.choice(Hulu), color=196336)
        hulu1.set_footer(text="Made with ❤️ by mistermartin")
        await ctx.author.send(embed=hulu1)

@client.command()
async def phacc(ctx):
        ph1 = discord.Embed(title="Here is your Pornhub Account: ", description=random.choice(Pornhub), color=196336)
        ph1.set_footer(text="Made with ❤️ by mistermartin")
        await ctx.author.send(embed=ph1)

@client.command()
async def crunchyrollacc(ctx):
        crunchyroll = discord.Embed(title="Here is your CrunchyRoll Account: ", description=random.choice(Crunchyroll), color=196336)
        crunchyroll.set_footer(text="Made with ❤️ by mistermartin")
        await ctx.author.send(embed=crunchyroll)

@client.command()
async def fortnite(ctx):
        fortnite = discord.Embed(title="Here is your Fortnite Account: ", description=random.choice(Fortnite), color=196336)
        fortnite.set_footer(text="Made with ❤️ by mistermartin")
        await ctx.author.send(embed=fortnite)


@client.command()
async def tier(ctx):
    if ctx.guild.id == 638119507633635328:
        tier1 = discord.Embed(title="Your tier is: **Premium**", description="Your Subscription end on: **LIFETIME**", color=2631842)
        tier1.add_field(name="⁣⁣⁣To Buy", value="⁣⁣⁣⁣⁣⁣DM <@mistermartin#1614>")
        tier1.set_footer(text="Made with ❤️ by mistermartin")
        await ctx.send(embed=tier1)



client.run("NjQ4NjU4MjAxNzM0MDIxMTIx.XdxcPA.wSxysae6RYViuW2R1isx6bopbIo")
