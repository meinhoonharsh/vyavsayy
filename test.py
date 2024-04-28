

# Extract Name,Number, College, Branch, Year using raw_data by analyzing pattern in it

import re



raw_data = '''
[13/12/23, 12:28:26 PM] CT Daily Prospect report: ‎Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them.
[13/12/23, 12:28:26 PM] anurag TL: ‎anurag TL created group “CT Daily Prospectus report ”
[13/12/23, 12:28:26 PM] CT Daily Prospect report: ‎anurag TL added you
[13/12/23, 12:52:39 PM] anup kumar ct: ‎anurag TL added anup kumar ct
[13/12/23, 7:12:51 PM] anchal e.c: Name - Ravi Kumar Singh 
Number - 9110052679
Visit Date - 25 to 30 dec
[13/12/23, 7:14:08 PM] Deepali E.C: Name - Prashant 
Number 7307662237
Visit date:16 dec
[13/12/23, 7:14:49 PM] anchal e.c: Name -  Sachin rajpoot 
Number - 6260317991
Visit Date - 1 January Indrapuri
[13/12/23, 7:15:46 PM] Deepali E.C: Name - Arvind Nagpure 
Number - 8085919210
Visit date - 17 dec
[13/12/23, 7:15:48 PM] anchal e.c: Name - kaluram malviya 
Number - 9301363126
Visit Date - 25 dec indrapuri
[13/12/23, 9:36:03 PM] anup kumar ct: Name - Tanishq 
Number - 9399890491
Visit date - 25 Dec
[13/12/23, 9:36:52 PM] anup kumar ct: Name - Amisha 
Number - 7805814902
Visit date - 17 Dec with friend
[13/12/23, 9:38:10 PM] anup kumar ct: Name - Arjun
Number - 8303542811
Visit date - 22 Dec
[13/12/23, 9:39:06 PM] anup kumar ct: Name - Karan Singh 
Number - 7722854881
Visit date - 17 Dec
[13/12/23, 10:08:13 PM] Deepali E.C: Name Anzar Alam
Number ‪88773 19952
Visit date 15 dec
[13/12/23, 10:26:34 PM] kp sir: Yeah kiskaa number hsi
[13/12/23, 10:27:09 PM] Deepali E.C: Anup Bhaiya ka
[13/12/23, 10:27:31 PM] kp sir: Aapka profile pic set nahi hai
[13/12/23, 10:27:50 PM] Deepali E.C: Sir personal number hai ye mera
‎[13/12/23, 10:28:56 PM] Deepali E.C: ‎image omitted
[13/12/23, 10:29:32 PM] kp sir: Office walla dooo
[13/12/23, 10:29:33 PM] kp sir: Muje
[13/12/23, 10:29:58 PM] Deepali E.C: 6263594069
[14/12/23, 12:03:27 AM] kp sir: Shilpa ko bhi add kardenaa Sir
[14/12/23, 8:33:05 AM] arpana e.c: ‎anurag TL added arpana e.c
[14/12/23, 8:39:47 AM] ~ Deepali coding: ‎anurag TL added ~ Deepali coding
[14/12/23, 8:26:54 AM] Neha mam e.c: @919893630880 isme Arpana and Shilpa dono add nahi hai
[14/12/23, 8:32:52 AM] anurag TL: Ok Ma'am
[14/12/23, 8:53:35 AM] ~ Chauhan Shilpa: ‎anurag TL added ~ Chauhan Shilpa
[14/12/23, 12:19:56 PM] anurag TL: Today's Attendance
Kasim
Hafsa
Anchal
Deepali
[14/12/23, 12:20:53 PM] anurag TL: Baki logo ka Jo bhi issue ho ya leave par ho to group par inform jarur Kara kare
[14/12/23, 1:27:05 PM] Deepali E.C: Name-MRITYUNJAY 
Number 7739496085
Visit date 14 dec
[14/12/23, 1:30:17 PM] anurag TL: ‎anurag TL changed the group name to “CT Daily Prospect report”
[14/12/23, 3:11:38 PM] kp sir: Naresh attendance leaaye sql ki
[14/12/23, 3:12:01 PM] Deepali E.C: Naresh off pr hai
[14/12/23, 3:12:06 PM] kp sir: Ok
[14/12/23, 4:27:09 PM] Neha mam e.c: 9301938054
Neeraj
[14/12/23, 4:27:31 PM] Neha mam e.c: Tit 
16-17 dec visit
[14/12/23, 5:18:58 PM] anurag TL: Aaj aap logo ki jo bhi visit aane wali thi, 
Unka kya update hai??
[14/12/23, 5:23:57 PM] anurag TL: Deepali, anchal-monday
Arpana- Tuesday 
Kasim- Wednesday
Anushree-Thursday 
Hafsa- Friday
Anup- Saturday 
Naresh- Sunday

Aap sabhi ka week off is tarh hi rahega
[14/12/23, 5:55:10 PM] Hafsa.: Sir not answering
[14/12/23, 5:56:38 PM] anurag TL: Kitne prospect the aaj visit ke liye??
[14/12/23, 5:57:11 PM] Hafsa.: 1
[14/12/23, 5:57:26 PM] anurag TL: Share details
[14/12/23, 6:00:14 PM] anchal e.c: Aaj ka koi nai tha
[14/12/23, 6:52:30 PM] Hafsa.: Name: Ayush Dilip Magarde
No. 9926329589
Visit date - Next week (not gave exact date)
[14/12/23, 6:53:21 PM] Hafsa.: Name: Roshan Katare
No.9753856818
Visit - 19 Dec
[14/12/23, 6:54:07 PM] Hafsa.: Name : Rishika Yadav
No. 9302191241
Visit - 17 Dec
[14/12/23, 6:57:46 PM] anurag TL: Aaj ki calling me bas 3 students intrested.
[14/12/23, 6:58:09 PM] anurag TL: This count is not good for all of us.
[14/12/23, 7:04:11 PM] kasim k: ‎You deleted this message.
[14/12/23, 7:05:53 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
VIKASH SHARMA	
9471438309	
29Dec	indrpuri
[14/12/23, 7:06:21 PM] kasim k: Computer Science & Engineering	
Sagar Institute of Science 
Technology & Engineering	
NAMAN SHARMA	
7999066129	
after 26 december
[14/12/23, 7:19:00 PM] anchal e.c: Name : Ankush parihar 
No. 9407302423
Visit - 21 dec
[14/12/23, 7:19:13 PM] Deepali E.C: Name Pavan sahu
Number 9630988730
Visit date 20- 25 dec
[14/12/23, 7:19:53 PM] Deepali E.C: Name Arjun Singh
Number 9599111053
Visit 18 dec
[14/12/23, 7:19:59 PM] anchal e.c: Name : krishnkant kushwaha 
No. 9329680378
Visit - 17 Dec
[15/12/23, 12:56:57 PM] annu❤️: Suraj -8405994775
15 December
Indrapuri
[15/12/23, 4:24:09 PM] annu❤️: Sourabh Dhakkad - 6269571816
 With friends Sonu jatav + 1
[15/12/23, 6:36:00 PM] annu❤️: Omkar Singh yadav -9140742347
Next semester
[15/12/23, 6:47:40 PM] Hafsa.: Sagar Sen 
9361599247
16 Dec
[15/12/23, 7:18:14 PM] kasim k: Computer Science & Engineering	
Sagar Institute of Science & Technology & Research	
HARSH RAI	
9174268923	
after 23 dec  	vidisha
[15/12/23, 7:18:44 PM] kasim k: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
SAHIL KUKREJA	
9755444750	
17Dec Sunday
[15/12/23, 7:19:07 PM] kasim k: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
DEVENDRA MALVIYA	6260798400	
january
[15/12/23, 7:19:43 PM] kasim k: Computer Science & Engineering	
Technocrats Institute of Technology & Science	
CHANDAN KUMAR	6205815159	
17 sunday
[15/12/23, 10:05:39 PM] anup kumar ct: Name: Omkumar
No: 6264012494
Visit: 17 December
[15/12/23, 10:06:52 PM] anup kumar ct: Name: MD Saad
No: 8305466718
Visit: 18 December
[15/12/23, 10:07:32 PM] anup kumar ct: Name: Amit Rao
No: 9685028124
Visit: 17 December
[15/12/23, 10:08:24 PM] anup kumar ct: Name: Abhishek 
No: 6201361977
Visit: 23 December
[15/12/23, 10:09:15 PM] anup kumar ct: Name: Akshat 
No: 9425383696
Visit: 16 December
[16/12/23, 12:23:57 PM] anurag TL: Iska follow up liya??
[16/12/23, 12:24:11 PM] anurag TL: Follow up
[16/12/23, 12:24:31 PM] anurag TL: Follow up
[16/12/23, 12:25:16 PM] anurag TL: Follow up
[16/12/23, 12:26:49 PM] Hafsa.: Try krnge aane ka
[16/12/23, 12:27:37 PM] annu❤️: After 2 January
[16/12/23, 12:28:55 PM] annu❤️: Not answered
[16/12/23, 12:55:15 PM] anurag TL: Now onwards, the details share format should be like 

Name of Student-*
College name-
Branch-
Year-*
Expected Date of Visit-*

* Is for mandatory detail
[16/12/23, 1:36:53 PM] kasim k: Computer Science & Engineering	
Radharaman Engineering 
College	
VISHAL KUMAR CHAUHAN	9301383028	
coming today indrpuri
[16/12/23, 2:04:25 PM] anup kumar ct: Sir I'm not at my Home. I'm outside.
I'll try.
[16/12/23, 2:24:34 PM] Deepali E.C: ‎This message was deleted.
[16/12/23, 2:25:16 PM] Deepali E.C: Morsingh 
7024339917
Visit Date 16 dec
[16/12/23, 2:37:33 PM] anurag TL: I know but aapke behalf me koi or follow up le sakat hai to aap use forward kar de
[16/12/23, 2:48:58 PM] ~ Chauhan Shilpa: Shyam sahu  
9522282536
Visit date 26 December with friends
[16/12/23, 3:21:51 PM] ~ Chauhan Shilpa: MD SAFEER ALAM 9006282597
Visit date 30 December
Pehle visit Kiya hua hai 6200560334 ‎<This message was edited>
[16/12/23, 3:25:06 PM] anurag TL: Admission me convert karna hai
[16/12/23, 3:29:41 PM] ~ Chauhan Shilpa: Ji sir mtech ka student hai join karne ka bol raha tha
[16/12/23, 4:36:36 PM] annu❤️: Anil kumar - 7828876778
Visit - In January 
Surabhi college
[16/12/23, 4:37:28 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
ABHIRAJ SHARMA	
7024847501	
24Dec
[16/12/23, 4:37:59 PM] kasim k: Electronics & Communication Engineering	
IES College of Technology	
MOHIT KUMAR YADAV	
9199024527	
21Dec
[16/12/23, 5:28:53 PM] kasim k: Artificial Intelligence and Data Science	
J.N. College of Technology	
ANKIT VERMA	
8718001456	
january new  batch 	
indrpuri with rohit sheetal
[16/12/23, 5:37:51 PM] annu❤️: CSE	Trinity Bhopal	MAYANK MORGHADE	7828410480	
Will Come in January
[16/12/23, 5:41:59 PM] kasim k: Computer Science & Engineering	
Bansal Institute of Research, 
Technology & Science	HARSHALI GHANODE	9993379807	
january plan new batch  indrpuri
[16/12/23, 5:42:09 PM] anurag TL: Year mention nahi Kiya aap ne
[16/12/23, 5:42:21 PM] kasim k: ‎You deleted this message.
[16/12/23, 5:48:30 PM] annu❤️: 1 st year
[16/12/23, 5:48:49 PM] annu❤️: 4th year
[16/12/23, 6:04:32 PM] annu❤️: CSE	Trinity Bhopal	MD MUKHTAR ALAM	6204293669	inform himself 	indrapuri 
1 st year
[16/12/23, 6:06:52 PM] Hafsa.: Name of Student-* Sarfaraz Alam
College name- All Saint's 
Branch- ME
Year- 4th yr
Expected Date of Visit- Will call in someday
[16/12/23, 6:07:39 PM] Hafsa.: Name of Student- Ameen Khan
College name- All Saint's 
Branch- ME
Year- 4th yr
Expected Date of Visit- Will call in someday
[16/12/23, 6:13:22 PM] anurag TL: Good 👍
This a proper way to share visit details
[16/12/23, 6:20:45 PM] anchal e.c: Name of Student-* Vivek Dhakad 
College name- SAM college 
Branch- CS
Year- 4th yr
Expected Date of Visit- 19 ,20 Dec
[16/12/23, 6:21:51 PM] anchal e.c: Name of Student-* vijay kahar
College name- SAM college 
Branch- CS
Year- 4th yr
Expected Date of Visit- 18 Dec
[16/12/23, 6:38:05 PM] Hafsa.: Name of Student- Ajay Prajapati 
College name- TIT
Branch- EE
Year- 4th yr
Expected Date of Visit- Will contact after exam
[16/12/23, 6:58:18 PM] annu❤️: Hashmatullah friend - MD Abu Saif , All saints 
5th semester

Yashir Ali Khan 
All saints
5th semester
[16/12/23, 6:58:27 PM] annu❤️: Admission ho rhe hai inke aaj
[16/12/23, 7:20:23 PM] ~ Chauhan Shilpa: deepak singh  tomar 8103295502
grurvendra ku 
9092107316
ajay kewat
6264076066
coming today
[16/12/23, 7:20:44 PM] ~ Chauhan Shilpa: Kasim sir ye visit jo apne ham
[16/12/23, 7:21:05 PM] ~ Chauhan Shilpa: Personal Bheji thi vah visit I thi
[16/12/23, 7:22:18 PM] ~ Chauhan Shilpa: Fees ko leker thoda problem hai positive hai join karna hai to aap ek bar baat kar lijiyega
[16/12/23, 8:42:14 PM] kasim k: han mam
kl
le
lunga followup
[17/12/23, 12:44:22 PM] anurag TL: Now onwards, the details share format should be like 

Name of Student-*
College name-
Contact no-*
Branch-
Year-*
Expected Date of Visit-*

* Is for mandatory detail
[17/12/23, 12:45:13 PM] anup kumar ct: Suraj and Ishu 
7860141537
He is refence
17 December in indrapuri
[17/12/23, 12:50:59 PM] anup kumar ct: Name of Student: Govind 
College name: Bansal 
Contact no: 8815771050
Branch: AIML
Year: 1ST
Expected Date of Visit: 17 December
[17/12/23, 12:52:56 PM] annu❤️: Mechanical Engineering	Kailash Narayan Patidar College of Science & Technology	
AJAY JATAV
8435857234
Will Come 	18 December
[17/12/23, 12:54:00 PM] arpana e.c: Technocrats Institute of Technology [Excellence]	AMIT KUMAR	7463845442 
visit date 17 dec for Inderpuri
[17/12/23, 12:59:51 PM] Hafsa.: Name of Student- Rishika Yadav 
College name- Millenium College 
Branch- CSE
Year- 2th Yr
Expected Date of Visit-  17 Dec
[17/12/23, 1:04:40 PM] anurag TL: Year
[17/12/23, 1:04:45 PM] anurag TL: Year
[17/12/23, 1:06:11 PM] arpana e.c: 1st
[17/12/23, 1:10:17 PM] annu❤️: Mechanical Engineering	Laxmipati Institute of Science & Technology	ANIL JATAV
9981823932
Will Come 	indrapuri 
24 December
4th year
[17/12/23, 1:10:31 PM] annu❤️: 4th year
[17/12/23, 1:10:53 PM] anup kumar ct: Name of Student: Abhishek 
College name: Oriental 
Contact no: 9162502255
Branch: MCA
Year: Final
Expected Date of Visit: 17 December
[17/12/23, 3:07:57 PM] anup kumar ct: Name of Student: Sameet Arya
College name: UIT
Contact no: 9171623785
Branch: ME
Year: 2nd
Expected Date of Visit: 21 December
[17/12/23, 3:56:34 PM] kasim k: 2nd year
Bansal Institute of Research, 
Technology & Science	
HIMANSHU SHUKLA	
8319770421	
before 19 dec
java pytn with 4,5 friends
himanshu,akash  +2
[17/12/23, 3:57:42 PM] anurag TL: Aane se pahle sabke name  jarur lena
[17/12/23, 3:58:03 PM] kasim k: haan  sir  2 ke bta die 2 ka aur bhaj raha
[17/12/23, 3:58:39 PM] anurag TL: Ok
[17/12/23, 4:07:38 PM] annu❤️: Mechanical Engineering	Bansal College of Engineering	NEELESH DHANWARE	7223995256
Will Come 	indrapuri 	24 December
4th Year
[17/12/23, 4:18:53 PM] kasim k: 3rd year
Computer Science & Engineering	
J.N. College of Technology	KAVERI KESHARWANI	9098398987	 
join in january new  batch
[17/12/23, 4:28:45 PM] Hafsa.: Name of Student- Tejasv Singh
College name- SISTech
Branch- CSE
Year- 4th Yr
Expected Date of Visit-  Will contact after 23 Dec
[17/12/23, 4:57:05 PM] ~ Chauhan Shilpa: Anuup
[17/12/23, 5:02:49 PM] anup kumar ct: yes mam
[17/12/23, 5:03:30 PM] ~ Chauhan Shilpa: Apki jo visit aai thi bo interested hai one year ke liye
[17/12/23, 5:04:02 PM] ~ Chauhan Shilpa: Ap baat kar lena
[17/12/23, 5:04:21 PM] anup kumar ct: okay mam 
thank you
[17/12/23, 5:07:47 PM] ~ Chauhan Shilpa: Most welcome
[17/12/23, 5:40:56 PM] arpana e.c: Sagar Institute of Research & Technology Excellence	PAYAL KUMARI
2nd year	9304503084
will think this week
[17/12/23, 5:51:51 PM] annu❤️: CSE	Trinity Bhopal	PAWAN KUMAR GUPTA	9621557842	Will Come indrapuri 	Sudhanshu , Manish , Pawan 	18 December
+ 7 friend
1 st Year
[17/12/23, 5:56:25 PM] arpana e.c: Sagar Institute of Research & Technology Excellence	PRASHANT PATHAK	9956552500
2nd year
will come 24 dec
[17/12/23, 5:57:01 PM] anchal e.c: Name of Student: Chandrapal pabaiya
College name: Oriental 
Contact no: 7771018596
Branch: CS
Year: 2nd year 
Expected Date of Visit: 19 December
[17/12/23, 5:59:09 PM] anchal e.c: Name of Student: Rahul agrawal 
College name: Oriental 
Contact no: 6267694160
Branch: CS
Year: 2nd year 
Expected Date of Visit: February
[17/12/23, 6:01:03 PM] arpana e.c: Sagar Institute of Research & Technology Excellence	SUYASH RAJPUT + 2frinds	9301837064	
2nd year
will come today 17 dec
[17/12/23, 6:02:21 PM] anchal e.c: Name of Student: Ravi ranjan 
College name: TIT
Contact no: 9113714591
Branch: CS
Year: 1 st year old prospect 
Expected Date of Visit: end of December
[17/12/23, 6:04:31 PM] anchal e.c: Name of Student: vinay Kumar ahirwar 
College name: TIT
Contact no: 8959339982
Branch: CS
Year: 1 st year old prospect 
Expected Date of Visit:  after exam Febuary
[17/12/23, 6:05:49 PM] anchal e.c: Name of Student: aman kumar Sharma 
College name: TIT
Contact no: 9523075885
Branch: CS
Year: 1 st year old prospect 
Expected Date of Visit:  will think 18 dec
[17/12/23, 6:06:53 PM] annu❤️: CSE	Trinity Bhopal
POOJA  DHAKAD	7489933035
Will Come indrapuri 	inform himself 	With friends 
1st year
[17/12/23, 6:09:44 PM] kasim k: ‎You deleted this message.
[17/12/23, 6:10:04 PM] kasim k: year :- 2
Bansal Institute of Research, Technology & Science	
PRINCE RAJ KUMAR	
6200683626	
19 December	
indrpuri
[17/12/23, 6:12:12 PM] arpana e.c: Sagar Institute of Research & Technology Excellence	RAHI CHAUDHARI	7974431706	
2nd year
will think 24dec
[17/12/23, 6:14:38 PM] Hafsa.: Name of Student- Hammad ur Rehman 
College name- TIT
Branch- EE
Year- 4th Yr
Expected Date of Visit-  Will contact in January
[17/12/23, 6:27:22 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[17/12/23, 6:27:52 PM] anurag TL: Year ??
[17/12/23, 6:28:16 PM] anchal e.c: Name of Student- Pallav Raj
College name- IES college 
Contact no.  9973074406
Branch- CS 
Year- 2nd Yr
Expected Date of Visit-  18 19 December
[17/12/23, 6:30:12 PM] ~ Chauhan Shilpa: Name of Student- RAJA KUMAR
College name- Trinity Bhopal
Contact no.  6204717952
Branch- CSE
Year- 1nd Yr
Expected Date of Visit-  (18 19 December(
[17/12/23, 6:31:54 PM] annu❤️: CSE	Trinity Bhopal	PRADEEP UIKEY	8305332442	
Will Come chetak
19 December
1st Year
[17/12/23, 6:32:32 PM] ~ Chauhan Shilpa: Name of Student-PRINCE KUMAR
College name-  Trinity Bhopal
Contact no.  9608299511
Branch- CS 
Year- 1nd Yr
Expected Date of Visit-  25 December
[17/12/23, 6:47:06 PM] kasim k: 2year
Computer Science & Engineering
Technocrats Institute of Technology & Science
AYUSH KUMAR RAY	
8809203619
19indrpuei
[17/12/23, 6:51:55 PM] annu❤️: CSE	Trinity Bhopal	PRASHANT SINGH
9131825287	
Will Come indrapuri 	22 December
1st Year
[17/12/23, 6:55:17 PM] ~ Chauhan Shilpa: Name of Student-VISHAL SEN
College name-  Trinity Bhopal
Contact no.  7879043794
Branch- CS 
Year- 1nd Yr
Expected Date of Visit-  23  December with friends ‎<This message was edited>
[17/12/23, 6:58:18 PM] Hafsa.: Name of Student- Sachin Kumar 
College name- SISTech
Branch- CSE
Year- 4th Yr
Expected Date of Visit-  Will contact in mid January
[17/12/23, 6:59:37 PM] anurag TL: Friends Name
[17/12/23, 7:00:12 PM] ~ Chauhan Shilpa: Sir boto nhi bataya
[17/12/23, 7:02:04 PM] anurag TL: Sabhi ko Trinity ka hi data Diya hai, isliye name or friends name jarur note karke rakhe ,jisse bad me problem na ho , 
Conflict hone par Bhut problem hogi
[17/12/23, 7:03:48 PM] ~ Chauhan Shilpa: Ji sir
[17/12/23, 7:28:31 PM] anup kumar ct: Name of Student: Abhishek 
College name: Trinity 
Contact no: 9302038308
Branch: CSE
Year: 1ST
Expected Date of Visit: 19 December
[17/12/23, 7:29:37 PM] anup kumar ct: Name of Student: Ashraf 
College name: Trinity 
Contact no: 9431037664
Branch: CSE
Year: 1ST
Expected Date of Visit: 25 December
[18/12/23, 12:55:28 PM] Neha mam e.c: Aaj kaam nahi kar rahe ho kya  prospect nahi nikal rahe tum logo ke aaj
[18/12/23, 12:56:50 PM] naresh e.c: Balance nhi hai
[18/12/23, 12:58:18 PM] Neha mam e.c: Baki ka to hai
[18/12/23, 1:01:59 PM] arpana e.c: Vaishnavi Inst. of Tech. & Science	BADAL GOLWALKER
final year	7389220920	will be think
[18/12/23, 1:25:14 PM] anup kumar ct: Name of Student: Arpit 
College name: Vidyapeeth 
Contact no: 8839838658
Branch: CSE
Year: FINAL 
Expected Date of Visit: 18 December
[18/12/23, 1:26:40 PM] Neha mam e.c: Aaj ki jiski jo visit hai usko bulao
[18/12/23, 1:28:09 PM] kasim k: 3rd 
Information Technology	
Oriental Institute of Science & Technology	
DEVENDRA YADAV	
8435282646	
1January
[18/12/23, 1:32:12 PM] arpana e.c: IES's College of Technology	LALIT PRAJAPATI
old prospect
2nd year
	9907627960
will come 23 dec
[18/12/23, 1:53:53 PM] kasim k: 3rd year
Artificial Intelligence and Data Science
J.N. College of Technology	
HIMENDRA MAKODE	
7067574845	
1week january new batch
[18/12/23, 2:46:54 PM] anurag TL: Iska follow up le lena
[18/12/23, 2:46:33 PM] Hafsa.: Name of Student- Bharti Dhakad
College name- BITS
Branch- CSE
Year- 4th Yr
Expected Date of Visit-  19 Dec
[18/12/23, 2:47:34 PM] anurag TL: 👆🏻 Follow up
[18/12/23, 2:48:13 PM] anurag TL: 👆🏻
[18/12/23, 2:48:45 PM] anurag TL: 👆🏻
[18/12/23, 2:49:04 PM] anurag TL: 👆🏻
[18/12/23, 2:49:17 PM] anurag TL: 👆🏻
[18/12/23, 2:58:22 PM] anup kumar ct: Okay sir
[18/12/23, 3:05:10 PM] anurag TL: 👆🏻
[18/12/23, 3:25:22 PM] annu❤️: Computer Science & Engineering	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	MUNEER ALI KHAN	7000019559	
After exam 	inform himself 
4th year
[18/12/23, 4:23:26 PM] anup kumar ct: Name of Student: Pankaj 
College name: 
Contact no: 7067472399
Branch: AIML
Year: 1ST
Expected Date of Visit: 19 December
[18/12/23, 5:18:50 PM] ~ Chauhan Shilpa: Name of Student: HEMNITIKA KEWAT
College name: Bhopal Institute of Technology & Science, Bangrasia
Contact no: 8305242303,9399880640
Branch: Mechanical Engineering
Year: 4 year 
Expected Date of Visit: 20,21 December with friends (Tripti  aur Sanskar) ‎<This message was edited>
[18/12/23, 6:22:38 PM] Hafsa.: ‎This message was deleted.
[18/12/23, 6:23:35 PM] Hafsa.: Name of Student- Rahul Kumar 
College name- Millennium College 
Branch- CSE
Year- 2th Yr
Expected Date of Visit - Will come in January
[18/12/23, 6:32:04 PM] Hafsa.: Name of Student- Varsha Hariyale
College name- Millennium College 
Branch- CSE
Year- 2th Yr
Expected Date of Visit - 19 Dec
[18/12/23, 6:34:34 PM] anurag TL: Inke contact no nahi hai??
[18/12/23, 6:44:22 PM] Hafsa.: 8540924658
[18/12/23, 6:44:33 PM] Hafsa.: 7225944350
[18/12/23, 6:45:53 PM] annu❤️: Computer Science & Engineering	NRI Institute of Information Science & Technology	MOHD AREEB ANSARI	7898024240	
Will Come python 	After exam 	
26 December
4th Year
[18/12/23, 7:02:50 PM] Hafsa.: Name of Student- Naval Kishore
Contact - 7828244739
College name- Millennium College 
Branch- CSE
Year- 2th Yr
Expected Date of Visit - 19 Dec
[18/12/23, 7:05:53 PM] anup kumar ct: Name of Student: Ajay Ahirwar with friends 
College name: Bansal 
Contact no: 9301886202
Branch: AIML
Year: 1ST
Expected Date of Visit: 25 December
[18/12/23, 7:06:24 PM] Neha mam e.c: Prospect akele likhne se kuch nahi hoga aaj 18th hai ur jo 18th ki visit thi abh kab biling
[18/12/23, 7:06:31 PM] Neha mam e.c: Bulaonge
[18/12/23, 7:12:27 PM] Neha mam e.c: Zeeshan 
Sumit
Inki fee kab karonge
[18/12/23, 7:13:32 PM] kasim k: 2nd year 
Computer Science & Engineering	
Technocrats Institute of Technology & Science	
MOHD REHAN
9839154839	
join in feb with faizan.
[18/12/23, 7:24:30 PM] ~ Chauhan Shilpa: Name of Student: SAHUL KUMAR
College name: Trinity Bhopal
Contact no: 9334934893
Branch: CSE
Year: 1ST
Expected Date of Visit: 23, 24 December
[19/12/23, 11:10:12 AM] Neha mam e.c: Inki fees kyun nahi le rahe
[19/12/23, 11:30:10 AM] Neha mam e.c: Kitni baar reminder daalna padega
[19/12/23, 12:03:40 PM] kasim k: sir name v dal dia kro mam samjh nahi ataa yeh number sath mai qki 2/3 sumit hai
[19/12/23, 12:04:19 PM] Neha mam e.c: Matlab
[19/12/23, 12:06:43 PM] kasim k: ‎You deleted this message.
[19/12/23, 12:07:08 PM] kasim k: sry surname
[19/12/23, 12:08:51 PM] kasim k: sumit mewada hai kyy mam ??
[19/12/23, 12:18:06 PM] Neha mam e.c: Ur koi bhi Sumit hai kya Fsd 9 me
[19/12/23, 12:18:36 PM] annu❤️: Cll ni utha rha hai zeeshan kl bhi ni uthaya tha usne
[19/12/23, 12:21:21 PM] kasim k: kl off tha  wo kl ayega class.
[19/12/23, 12:35:31 PM] Neha mam e.c: Kal class thi Fsd 9 me
[19/12/23, 12:35:58 PM] kasim k: but kl wo aya nhi tha  ab kl ayega kh rha
[19/12/23, 12:43:45 PM] anurag TL: 👆🏻
[19/12/23, 12:45:47 PM] anurag TL: 👆🏻
[19/12/23, 12:46:05 PM] anurag TL: 👆🏻
[19/12/23, 12:48:10 PM] anurag TL: 👆🏻
[19/12/23, 12:48:27 PM] anurag TL: 👆🏻
[19/12/23, 12:48:39 PM] anurag TL: 👆🏻
[19/12/23, 12:48:48 PM] anurag TL: 👆🏻
[19/12/23, 12:48:58 PM] anurag TL: 👆🏻
[19/12/23, 12:49:14 PM] anurag TL: 👆🏻
[19/12/23, 12:49:30 PM] anurag TL: 👆🏻
[19/12/23, 12:49:40 PM] anurag TL: 👆🏻
[19/12/23, 12:49:50 PM] anurag TL: 👆🏻
[19/12/23, 12:49:58 PM] anurag TL: 👆🏻
[19/12/23, 12:50:50 PM] anurag TL: Ye sab aaj ki visit ke aap logo ke prospect hai, inko sabse pahle call karke follow up lo
[19/12/23, 12:51:21 PM] Hafsa.: Sir exam h inka call disconnect kr diya
[19/12/23, 12:51:27 PM] anurag TL: Jo aapki visit 18 Dec ki aani thi but nahi aai, unka follow up bhi chahiye mujhe
[19/12/23, 12:52:14 PM] anurag TL: Exam to ho gye final year ke sayad, practical viva ho sakta hai, aaj 3 bje ke bad call kar Lena ek bar
[19/12/23, 12:52:24 PM] Hafsa.: Okh
[19/12/23, 12:53:13 PM] anurag TL: Kuch logo ki baten khatam ho gai ho to calling par dhayan de , sab par dhayan rahta hai ki kon kya kar Raha.
[19/12/23, 12:56:17 PM] anurag TL: Aap sabhi par minimum 4 addmission ka Target hai, 31 Dec 23 tak.
Jo aapko karna hi hai
[19/12/23, 1:11:19 PM] anchal e.c: Name of Student: Ankush Kumar 
College name: sagar 
Contact no: 6202432730
Branch: EC
Year: 1ST old prospect 
Expected Date of Visit: 19 20 dec December
With friend Wasim
[19/12/23, 1:20:15 PM] kasim k: coming today
[19/12/23, 1:20:57 PM] kasim k: not ans
[19/12/23, 1:21:50 PM] kasim k: ‎You deleted this message.
[19/12/23, 1:23:57 PM] Hafsa.: Not answering
[19/12/23, 1:25:02 PM] Hafsa.: NA
[19/12/23, 1:51:05 PM] anup kumar ct: Name of Student: Aman 
College name: TIT
Contact no: 8827517765
Branch: CSE
Year: 4TH
Expected Date of Visit: 19 December
[19/12/23, 1:51:31 PM] naresh e.c: Name :-KAPIL SHUKLWARE	
Numver :-7089911047	
Branch :-	EC	
19 dec Indrapuri
[19/12/23, 2:56:39 PM] Hafsa.: Name of Student- Shivam Kacchi with friend Gaurav 
Contact - 9770081523
College name- TIT
Branch- EC
Year- 1th Yr old prospect 
Expected Date of Visit - 19 Dec
[19/12/23, 3:48:51 PM] naresh e.c: Name :- Alim baig and his wife 
College:-TIT 
Branch :- cs &aiml  
Number: - 7566188709
Already visited will come 23 dec for admission and wife also
[19/12/23, 3:50:16 PM] Hafsa.: They are already visited
[19/12/23, 3:50:46 PM] naresh e.c: Ha to likha hua h usme dekh lo shi se padh le ap
[19/12/23, 3:51:18 PM] Hafsa.: Sahi ap bhi samajh le kyuki already do logo k paas h
[19/12/23, 3:52:03 PM] naresh e.c: Ji kiske pass h
[19/12/23, 3:52:39 PM] anchal e.c: Mere pass h
[19/12/23, 3:52:42 PM] Hafsa.: Mere
[19/12/23, 3:53:25 PM] naresh e.c: Anurag Sir ap check kr lijiyega
[19/12/23, 3:54:17 PM] anurag TL: Anup this is not a way to reply, we are in same profession, and  in same institute.
[19/12/23, 3:54:55 PM] Deepali E.C: Sir ye anup nhi naresh hai
[19/12/23, 3:55:06 PM] anurag TL: Aap sabhi ek dushre se achhe se bat karege, agar aap logo ko koi problem hai to mujhe btaiye,
[19/12/23, 3:55:57 PM] naresh e.c: Ha but sir Mene already  usme likh diya tha ki already visited  then reply ki need nhi thi thats why mene bola aisa
[19/12/23, 3:56:20 PM] anurag TL: Haan Deepali, main kisi ko nahi bol raha but jisne bola ho unko samjh aa jaye,
[19/12/23, 4:01:16 PM] anurag TL: Ok , koi nahi but apne sath walo se is tarh bat nahi ki jati.
[19/12/23, 4:20:04 PM] Neha mam e.c: Bataiye khatam ho gyi ho to kaam kar lo
[19/12/23, 4:45:08 PM] Hafsa.: Name of Student- Akshat Shrivastav 
Contact - 9713924030
College name- Bansal 
Branch- AIML
Year- 1th Yr 
Expected Date of Visit - Will contact in January
[19/12/23, 5:27:05 PM] Hafsa.: Will come after exam
[19/12/23, 5:47:23 PM] annu❤️: Computer Science & Engineering	NRI Institute of Information Science & Technology	
NAINA KUSHWAHA	9179327913	
Will think
Call back 	26 December
4th year
[19/12/23, 5:49:45 PM] Hafsa.: Will come on 24 Dec ; family issue
[19/12/23, 6:46:27 PM] kasim k: 2nd year
Computer Science & Engineering
Patel College of Science & Technology
VISHWAS KUMAR SAHU	9407159112	
january end
[19/12/23, 7:20:01 PM] Hafsa.: Name of Student- Dhanu Kumar Yadav
Contact - 8271092641
College name- Millennium College 
Branch- CSE
Year- 2th Yr 
Expected Date of Visit - Will contact in January
[19/12/23, 7:20:20 PM] anchal e.c: Name of Student- Harsh Gupta 
Contact - 9926385690
College name- oriental 
Branch- CS
Year- 2nd yr
Expected Date of Visit - Will contact in January
[19/12/23, 7:21:15 PM] anchal e.c: Name of Student- Dinesh Dangi 
Contact - 7974428029
College name- Sagar 
Branch- CS
Year- 2nd yr
Expected Date of Visit - Will contact in January
[19/12/23, 7:22:08 PM] anchal e.c: Name of Student- Abhishek Kumar 
Contact - 7644083914
College name- Sagar 
Branch- CS
Year- 2nd yr
Expected Date of Visit - Will contact in  2 ,3 month
[19/12/23, 7:22:10 PM] Deepali E.C: Name of student Ronak Raj
Contact 6206141150
College JNCT
Branch cs
Year 2nd
Expected date of visit will  come 24 dec
[19/12/23, 7:24:53 PM] Deepali E.C: Name of student altaf mansoori
Contact 9399243755
College corporate college 
Branch cs
Year 4th year
Expected date of visit will  come after exam
[19/12/23, 7:26:48 PM] anup kumar ct: Name of Student: Ankit
College name: Bansal
Contact no: 6263283021
Branch: AIML
Year: 1ST
Expected Date of Visit: after jan
[19/12/23, 7:27:17 PM] Deepali E.C: Name of student  sneha verma
Contact 9340970550
College JNCT college 
Branch cs
Year 2nd year
Expected date of visit will  come after 25 dec
[20/12/23, 12:31:22 PM] anurag TL: Aaj se aap logo ki seating is tarah rahegi

Reception- Hafsa,Arpana
 In lobby near book racks- Naresh, Anushree
Back Side nin cubes- kasim, anup,anchal
Class- 5- Deepali
[20/12/23, 12:32:01 PM] anurag TL: Isi seating par milege aap sabhi apne working hours me .
[20/12/23, 12:32:17 PM] anurag TL: Follow this now
[20/12/23, 1:11:26 PM] arpana e.c: Name of student  praveen
Contact 7489141784
College oriental college 
Branch civil
Year 2nd year
Expected date of visit will  come 20 dec
[20/12/23, 1:16:36 PM] anup kumar ct: Name of Student: Ayushmati 
College name: TIT
Contact no: 9302869608
Branch: CSE
Year: 4TH
Expected Date of Visit: 25 Dec
[20/12/23, 1:30:02 PM] anup kumar ct: Name of Student: Deepak 
College name: TIT
Contact no: 6264332037
Branch: CSE
Year: 4TH
Expected Date of Visit: 25 Dec
[20/12/23, 1:43:07 PM] arpana e.c: Name of student  Rudra yadav
Contact 7697129743
College oriental college 
Branch cs
Year 1st year
Expected date of visit will  come  20 dec
[20/12/23, 1:47:53 PM] naresh e.c: Name :- Kripanand Vishwakar	no. :-7354522152
Branch :- cse 
College: - nri 
20 dec Indrapuri
[20/12/23, 3:39:03 PM] naresh e.c: Name :-Niraj KUMAR		
No.:-7480023389
Branch :- ec
College: - 	vns 
Year:- 4th
23 Dec
[20/12/23, 5:29:46 PM] anup kumar ct: Name of Student: MD Mesar Ahmad
College name: TIT
Contact no: 9507969988
Branch: CSE
Year: 4TH
Expected Date of Visit: will think January
[20/12/23, 5:39:21 PM] anchal e.c: Name of Student: Mo sahil shah
College name: Sagar 
Contact no: 7999439952
Branch: CS
Year: 2nd year 
Expected Date of Visit: will think January
[20/12/23, 5:39:30 PM] anup kumar ct: Name of Student: Mukesh
College name: TIT
Contact no: 7898823258
Branch: CSE
Year: 4TH
Expected Date of Visit: 25 Dec
[20/12/23, 5:40:29 PM] anchal e.c: Name of Student: pawan tiwari 
College name: Sagar 
Contact no: 9696734338
Branch: CS
Year: 2nd year 
Expected Date of Visit: 20 21 December
[20/12/23, 5:51:09 PM] anup kumar ct: Name of Student: Shashank 
College name: Bansal
Contact no: 8817641418
Branch: 
Year: 1st
Expected Date of Visit: Next Semester
[20/12/23, 5:52:11 PM] anchal e.c: Name of Student: Amit saket
College name: Bansal
Contact no: 9343592947
Branch: 
Year: 1st
Expected Date of Visit: will think
[20/12/23, 6:04:20 PM] Hafsa.: Name of Student: Varsha Hariyale 
College name: Millennium College 
Contact no: 7225944350
Branch: CS
Year: 2nd Yr
Expected Date of Visit: Will contact soon for visit (busy in exams)
[20/12/23, 6:14:49 PM] anup kumar ct: Name of Student: Shiv Kumar 
College name: Bansal
Contact no: 9304760690
Branch: 
Year: 1st
Expected Date of Visit: Next Semester
[20/12/23, 6:18:08 PM] naresh e.c: Coming with frnd vivek kumar sha
[20/12/23, 6:34:28 PM] Hafsa.: Name of Student- Laxminarayan Mandal
Contact - 7079666792
College name- VNS
Branch- EC
Year- 2th Yr 
Expected Date of Visit - Will contact in January
[20/12/23, 6:34:56 PM] anup kumar ct: Name of Student: Shivam 
College name: Bansal
Contact no: 9179817378
Branch: CS
Year: 1st
Expected Date of Visit: 23 Dec
[20/12/23, 6:36:37 PM] Deepali E.C: Name of Student: vikas yadav
College name: Sirt
Contact no: 7987095396
Branch: Ec
Year: 4th
Expected Date of Visit: 24 dec
[20/12/23, 6:37:43 PM] Deepali E.C: Name of Student: harsh jain
College name: JNCT
Contact no: 9713056704
Branch: CS
Year: 2nd year
Expected Date of Visit: will come next month
[20/12/23, 6:39:26 PM] Deepali E.C: Name of Student: Sachin kumar
College name: Jnct
Contact no: 9284499790
Branch: cs
Year: 2nd year
Expected Date of Visit: 21 dec
[20/12/23, 6:52:11 PM] Deepali E.C: Name of Student:AWINASH KUMAR SINGH
College name: Jnct
Contact no: 9142019313
Branch: cs
Year: 2nd year
Expected Date of Visit: 23 dec
[20/12/23, 6:54:10 PM] anurag TL: Kal se regularly yahi follow hoga,
[20/12/23, 6:57:21 PM] anchal e.c: Name of Student:Asbendra Singh 
College name: scope 
Contact no: 8707245575
Branch: cs
Year: 2nd year
Expected Date of Visit: after exam January
[20/12/23, 6:59:05 PM] Deepali E.C: Name of Student Nikhil kumar
College name: Jnct
Contact no:8959651294
Branch: cs
Year: 2nd year
Expected Date of Visit: 24 dec
[20/12/23, 7:29:42 PM] naresh e.c: Name :- 	ROOPSINGH AHIRWAR		no.7049458625			
Branch :- ec
College :- bist 
21 dec morning
[20/12/23, 8:33:11 PM] naresh e.c: Any update Sir ?
[21/12/23, 12:24:18 PM] anup kumar ct: ‎This message was deleted.
[21/12/23, 12:25:35 PM] anup kumar ct: Name of Student: Shubh
College name: Bansal
Contact no: 8252733600
Branch: CS
Year: 1st
Expected Date of Visit: 25 Dec
[21/12/23, 12:33:04 PM] Neha mam e.c: Ye jo assign hua hai issi ke according baithna hai bina excuse
[21/12/23, 12:33:19 PM] Neha mam e.c: Koi cabin me aakar koi excuse mat dena
[21/12/23, 12:34:26 PM] anup kumar ct: Name of Student: Sudeep 
College name: Bansal
Contact no: 9977654782
Branch: CS
Year: 1st
Expected Date of Visit: 25 Dec
[21/12/23, 12:34:35 PM] Deepali E.C: Name of student Vivek
College name IES
Contact number 7389330294
Branch EC
Year 4th
Expected date of visit 27 dec
[21/12/23, 12:40:25 PM] anup kumar ct: ‎This message was deleted.
[21/12/23, 12:40:59 PM] anup kumar ct: Name of Student: Pawan with Suresh 
College name: TIT
Contact no: 9752171066
Branch: CSE
Year: 4TH
Expected Date of Visit: 22 Dec
[21/12/23, 12:42:20 PM] naresh e.c: Name :-AMIT VERMA	
No.:-	7999429849	
Branch :- cs
College:-scope 
Expected date of visit :- 28 dec
[21/12/23, 12:43:35 PM] annu❤️: College : Bansal	
Name : KARTIK CHOUBEY
Number : 	9302593984	Will Come 	inform himself In January
[21/12/23, 12:45:07 PM] anurag TL: 👆🏻
[21/12/23, 12:45:23 PM] anurag TL: 👆🏻
[21/12/23, 12:45:33 PM] Neha mam e.c: @919893630880 inke jo date inn logo ne de rakhi hai usse 10 days ka apan wait karenge nahi to aap inse prospect lekar kissi ur ko de dijiyega
[21/12/23, 12:45:51 PM] anurag TL: 👆🏻
[21/12/23, 12:46:46 PM] anurag TL: 👆🏻
[21/12/23, 12:47:15 PM] Neha mam e.c: Sir ye bhi dekh lijiye jo management ki baat nahi maan paa raha to apan ko bhi aise employee ki jarurat nahi hai
[21/12/23, 12:47:29 PM] kasim k: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence	
ABHISHEK YADAV	
7880216332	
coming today indrpuri
[21/12/23, 12:48:13 PM] arpana e.c: Bhopal Institute of Technology & Science, Bangrasia	JITENDRA YADAV
2nd year
	9575630476	will think 26 dec
[21/12/23, 12:49:30 PM] anchal e.c: not answering
[21/12/23, 12:49:47 PM] anurag TL: 👆🏻
[21/12/23, 12:49:56 PM] anurag TL: 👆🏻
[21/12/23, 12:50:04 PM] arpana e.c: call disconnect kr rhe
[21/12/23, 12:50:13 PM] anurag TL: 👆🏻
[21/12/23, 12:50:16 PM] arpana e.c: in college ..
[21/12/23, 12:50:35 PM] anurag TL: 👆🏻
[21/12/23, 12:50:52 PM] anurag TL: 👆🏻
[21/12/23, 12:51:05 PM] anurag TL: 👆🏻
[21/12/23, 12:52:06 PM] anurag TL: Haan Ma'am
[21/12/23, 12:52:07 PM] naresh e.c: Will come in evening
[21/12/23, 12:52:08 PM] anup kumar ct: try to come in evening.
[21/12/23, 12:52:31 PM] anurag TL: Ok Ma'am
[21/12/23, 12:52:43 PM] naresh e.c: Will try in evening  with frnds
[21/12/23, 12:57:07 PM] kasim k: 7509070442
[21/12/23, 12:57:07 PM] kasim k: ‎You deleted this message.
[21/12/23, 12:57:07 PM] kasim k: ‎You deleted this message.
[21/12/23, 12:58:31 PM] kasim k: fsd 9 mai add hone ka bol  raha hai grup mai karwa do mam @919926561814 @919131608639
[21/12/23, 1:00:10 PM] naresh e.c: +91 97534 92606 aditya 
Isko bhi group me add krna h Fsd 9 me
[21/12/23, 1:00:42 PM] Neha mam e.c: Ok
[21/12/23, 1:04:08 PM] Deepali E.C: Evening me aa rhe hai ek friend ke sath
[21/12/23, 1:06:15 PM] anchal e.c: ‎This message was deleted.
[21/12/23, 1:18:13 PM] arpana e.c: IES's College of Technology	JYOTISH KUMAR
4th year	7260008572	will think 28 dec
[21/12/23, 1:23:39 PM] anchal e.c: Name of Student: Arbaz shah 
College name: sagar 
Contact no: 8103843680
Branch: cs
Year: 4th year 
Expected Date of Visit: not confirm date January
[21/12/23, 1:24:44 PM] anchal e.c: Name of Student: Anuj raut 
College name: sagar 
Contact no: 9302678095
Branch: cs
Year: 4th year 
Expected Date of Visit: will think
[21/12/23, 1:27:34 PM] arpana e.c: Bhopal Institute of Technology & Science, Bangrasia	SACHIN CHOUDHARY	9589839159
4th year
	will think 2 jan
[21/12/23, 1:34:57 PM] annu❤️: Bansal college
NEERAJ BHEEL	7974545910	Will Come Cc++
24 December
1st year
[21/12/23, 1:45:16 PM] Neha mam e.c: @918269668024 Aniket ko 3 baje bula lo backup ke liye aaj
[21/12/23, 1:46:00 PM] Deepali E.C: Oky mam
[21/12/23, 1:53:41 PM] Neha mam e.c: Iska replay bahut jaldi di baki bato ka kya
[21/12/23, 1:55:28 PM] Deepali E.C: Konsi baate mam
[21/12/23, 2:00:49 PM] Hafsa.: Name of Student: Kumar Gaurav 
College name: LNCT
Contact no: 6200359473
Branch: CS
Year: 2nd Yr
Expected Date of Visit: 23 Dec ( Indrapuri )
[21/12/23, 2:51:34 PM] arpana e.c: Bansal College of Engineering	SUMIT GIRI	
4th year
7828465878	
will think 22dec
[21/12/23, 2:53:52 PM] annu❤️: Bansal
PARAS RAI	
8269130111	
Will Come Cc++	
In January 
1st year
[21/12/23, 3:09:54 PM] anup kumar ct: Name of Student: Renu 
College name: VNS
Contact no: 9174801924
Branch: CS
Year: 4TH
Expected Date of Visit: 23 December
[21/12/23, 3:21:04 PM] anup kumar ct: Name of Student: Anuj
College name: SIRT
Contact no: 9174801924
Branch: CS
Year: 1st
Expected Date of Visit: After exam
[21/12/23, 4:11:20 PM] annu❤️: Bansal	
POOJA KUSHWAHA	9098799650
Will Come Cc++	
inform himself
[21/12/23, 4:34:24 PM] kasim k: 2nd year
Computer Science & Engineering	
Radha Raman Institute of Technology & Science
VISHWAJEET KUMAR	
7492012164
25decemeber
[21/12/23, 6:12:08 PM] annu❤️: Bansal	
PRINCE KUMAR OJHA	6200616799	
After exam 	Will Come 
1st year
[21/12/23, 6:13:38 PM] anurag TL: Aaj ki visit ka kya hua
[21/12/23, 6:13:47 PM] anurag TL: Kisi ki koi bhi visit nahi aai
[21/12/23, 6:14:19 PM] anurag TL: Iska kya hua, mere hisab se evening ho gai
[21/12/23, 6:14:36 PM] anurag TL: Try nahi ho Raha sayad usse
[21/12/23, 6:15:03 PM] anurag TL: Aapse try nahi ho Raha sayad achhe se
[21/12/23, 6:15:24 PM] anurag TL: Kya hua , aa gye ya nahi
[21/12/23, 6:15:56 PM] Deepali E.C: Sir call Kiya tha busy aaya
[21/12/23, 6:16:16 PM] Deepali E.C: Abhi fr se call kar leti hu
[21/12/23, 6:16:16 PM] naresh e.c: Call nhi utha raha
[21/12/23, 6:17:22 PM] Deepali E.C: Na hai
[21/12/23, 6:18:21 PM] anchal e.c: Name of Student: Rishikesh Kumar 
College name: scope 
Contact no: 7000875268
Branch: CS
Year: 2nd Yr
Expected Date of Visit: Feb
[21/12/23, 6:18:47 PM] anurag TL: Or dushre ka kya hua
[21/12/23, 6:18:55 PM] anurag TL: Ek ka reply dekar shant ho gye
[21/12/23, 6:18:56 PM] naresh e.c: Same
[21/12/23, 6:19:05 PM] anurag TL: Waise to bhut bolte ho
[21/12/23, 6:19:27 PM] anurag TL: To Maine jab dono ka pucha to ek ka kyo reply kiya
[21/12/23, 6:19:42 PM] anurag TL: Main jitna puchu utna answer chahiye mujhe ok
[21/12/23, 6:19:49 PM] naresh e.c: To Dono ka hi ek reply diya tha sir
[21/12/23, 6:19:50 PM] naresh e.c: Wo
[21/12/23, 6:19:57 PM] anup kumar ct: Sir Iska exam tha abhi free nahi hua tha waha se 6PM pr call kia tha so usne bola jaldi free ho gaya to aa jaega.
[21/12/23, 6:20:08 PM] naresh e.c: Dono hi nhi utha rahe h dusro se bhi lag waha liya call Mene
[21/12/23, 6:20:45 PM] anurag TL: Mujhe perticular Har comment par reply chahiye, same tha to kya 10 ka answer ek me de doge
[21/12/23, 6:21:33 PM] naresh e.c: Ok
[21/12/23, 6:36:28 PM] Hafsa.: Name of Student: Mayank Warathe
College name: Vidyapeeth College 
Contact no: 9009386893
Branch: EC
Year: 2nd Yr
Expected Date of Visit: 23 Dec ( Indrapuri )
[21/12/23, 6:38:45 PM] naresh e.c: Name :- Azharuddin khan
College: - jnct 
Number: - 7324959638
Branch :- cs aiml 
Expected visit date 26 dec
[21/12/23, 7:02:45 PM] Hafsa.: Name of Student: Sugandh Kumar 
College name: Vidyapeeth College 
Contact no: 7643821219
Branch: EC
Year: 2nd Yr
Expected Date of Visit: Will contact in Feb after exam
[21/12/23, 7:10:04 PM] anup kumar ct: Name of Student: Suraj with sahil and talim and other friends 
College name: Bansal
Contact no: 7806044866
Branch: CS
Year: 1ST
Expected Date of Visit: 24 December
[21/12/23, 7:18:06 PM] anup kumar ct: Name of Student: Sukhdas with other friends 
College name: Bansal
Contact no: 7748075860
Branch: CS
Year: 1ST
Expected Date of Visit: 24 December
[21/12/23, 7:18:56 PM] naresh e.c: Name :- sarvesh pathak 
Number :8450017266 
Branch :- cse 
College: - scope 
Expected date of visit: - 30 dec
[21/12/23, 7:22:24 PM] anup kumar ct: Name of Student: Suraj Sharma with hariom,raj and friends 
College name: Bansal
Contact no: 7999101705
Branch: CS
Year: 1ST
Expected Date of Visit: 21 December
[21/12/23, 7:27:12 PM] annu❤️: Bansal	
SANGAM YADAV	9329672679	
Will Come python 	
4 January
1st year
[21/12/23, 7:30:21 PM] Deepali E.C: Name of Student: Sonam yadav
College name:SIRT
Contact no: 7415265299
Branch: cs
Year: 4th year
Expected Date of Visit: will come after one week
[21/12/23, 7:31:17 PM] naresh e.c: Name :- rahul kumar 
College: - scope 
No. 9111264166
Branch :- cs 
After exam
[22/12/23, 12:00:25 PM] anurag TL: Sab apni seating par milege.
[22/12/23, 12:01:23 PM] anurag TL: And kal sham ko mujhe aap sab se data chahiye ki is week aap logo ki  kitni visits aai. 
And kisne kitne admission Kara diye
[22/12/23, 12:01:32 PM] anurag TL: Kal evening Tak mujhe yah chahiye,
[22/12/23, 12:36:27 PM] Deepali E.C: Name of Student: Naresh patel
College name:SIRT
Contact no: 6265031278
Branch: cs
Year: 4th year
Expected Date of Visit: will come 23 dec
[22/12/23, 12:40:11 PM] annu❤️: Bansal	
SUSHANT NAGAR	9691175401	
Will Come 	
24 December 
With friend Sangam
[22/12/23, 12:42:34 PM] arpana e.c: coming today .
[22/12/23, 1:13:30 PM] anchal e.c: Name of Student: Harsh Raj
College name:TIT
Contact no: 8102013719
Branch: cs
Year: 2nd yera old prospect 
Expected Date of Visit: After exam January
[22/12/23, 1:15:39 PM] anchal e.c: Name of Student: Abhishek malviya 
College name: Sagar 
Contact no: 9399007087
Branch: cs
Year: 4th yera 
Expected Date of Visit: After exam January
[22/12/23, 1:24:00 PM] kasim k: 2nd year
Computer Science & Engineering
Patel College of Science & Technology
CHANDAN KUMAR
7033501524
23December	indrpuri
[22/12/23, 1:26:25 PM] anchal e.c: Name of Student: prakhar kR khaira 
College name: LNCT 
Contact no: 7275251513
Branch: cs
Year: 2nd year old prospect 
Expected Date of Visit: After exam January
[22/12/23, 1:52:46 PM] annu❤️: 23 December
[22/12/23, 3:39:54 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology	 
ABHISHEK TIWARI	6202270300	
Will Come 	indrapuri 	
28 December With brother
[22/12/23, 3:40:19 PM] annu❤️: 4th year
[22/12/23, 3:48:42 PM] kasim k: 2nd year
Computer Science & Engineering	
Patel College of Science & Technology	
AJAY CHANDRAVANSHI	
8878814649
5January
[22/12/23, 4:24:22 PM] anup kumar ct: Name of Student: Abhyuday 
College name: LNCT
Contact no: 8084475800
Branch: CSEAIML 
Year: 4TH
Expected Date of Visit: 22 December
[22/12/23, 5:08:37 PM] naresh e.c: Name :- ARJUN KUMAR SONI		number :- 7354282829	22
College: - tit 
Branch :- it 
22 dec Indrapuri  try with frnds
[22/12/23, 5:15:23 PM] anchal e.c: Name of Student: Divyanshu Sharma 
College name:  BSS
Contact no: 917110360
Branch: EEE
Year: 2nd
Expected Date of Visit: After exam will confirm
[22/12/23, 5:16:54 PM] anup kumar ct: Name of Student: Tamnna verma
College name: Bansal
Contact no: 7970140785
Branch: CS
Year: 1ST
Expected Date of Visit: After exam
[22/12/23, 5:29:29 PM] anup kumar ct: Name of Student: Versha kushwaha 
College name: Bansal
Contact no: 9753113180
Branch: CS
Year: 1ST
Expected Date of Visit: Discuss with family and inform
[22/12/23, 5:30:35 PM] Deepali E.C: Name of Student: Mukhtar ansari
College name: SIRT
Contact no: 9131368179
Branch: CS
Year: 4th
Expected Date of Visit: will come January first week
[22/12/23, 5:31:49 PM] Deepali E.C: Name of Student: Vivek Agarwal 
College name: JNCT
Contact no: 8871087440
Branch: CS
Year: 2nd
Expected Date of Visit: will come 27 dec
[22/12/23, 5:48:55 PM] ~ Chauhan Shilpa: Name of Student: RIYA KUMARI
College name: Trinity Bhopal
Contact no: 7321959306
Branch: CS
Year: 1
Expected Date of Visit: will come 23 , 24 December
[22/12/23, 5:49:53 PM] ~ Chauhan Shilpa: Name of Student: ROHIT LODHI
College name: Trinity Bhopal
Contact no: 6265677797
Branch: CS
Year: 1
Expected Date of Visit: will come 30 December
[22/12/23, 5:53:41 PM] anup kumar ct: Name of Student: Zahid
College name: Bansal
Contact no: 9117050882
Branch: CS
Year: 1ST
Expected Date of Visit: 30 Dec
[22/12/23, 5:56:21 PM] annu❤️: Computer Science & Engineering	IES's College of Technology	
ANKIT KUMAR JHA	7303892845	
For friends 	Naveen + 2 	Inform himself 
4th Year
[22/12/23, 6:22:59 PM] anup kumar ct: ‎This message was deleted.
[22/12/23, 6:23:19 PM] anup kumar ct: Name of Student: Abhay
College name: Bansal
Contact no: 8817876567
Branch: CS
Year: 1ST
Expected Date of Visit: 24 Dec
[22/12/23, 6:35:25 PM] naresh e.c: Name :-	AKASH KUMAR		
number :-7078418714	
College: -Sha-Shib 
Branch :- cs 
Expected date of visit :24 dec
[22/12/23, 7:10:07 PM] anurag TL: Aaj se aap logo ki seating is tarah rahegi

Reception- Hafsa,Arpana
 In lobby near book racks- Kasim, Anchal
Back Side nin cubes- Anup, Anushree 
Class- 5- Deepali, Naresh
[22/12/23, 7:10:58 PM] anurag TL: Kal se sabhi apni apni assign position me hi mile, nahi to half day absent count hoga,
[22/12/23, 7:11:17 PM] anurag TL: Kisi ko koi issu hai to abhi discuss kare aakar
[22/12/23, 7:16:42 PM] anurag TL: Aaj se aap logo ki seating is tarah rahegi

Reception- Hafsa,Arpana
 In lobby near book racks- Kasim, Anchal
Back Side nin cubes- Anup, Anushree, Naresh 
Class- 5- Deepali,
[22/12/23, 7:18:02 PM] Deepali E.C: Sir me akele bethi kya??
[22/12/23, 7:22:36 PM] anurag TL: Haan
[22/12/23, 7:22:45 PM] anurag TL: Koi problem hai kya
[22/12/23, 7:22:50 PM] Deepali E.C: Yes sir
[22/12/23, 7:22:58 PM] anurag TL: To rahne do
[22/12/23, 7:23:06 PM] anurag TL: Baithna wahi hai bas
[22/12/23, 7:23:37 PM] Deepali E.C: Aap mere sath kisi ek or bitha dijiye sir mujhe koi dikkat nhi waha bethne me
[22/12/23, 7:29:02 PM] anup kumar ct: Come with friend.
[22/12/23, 7:36:54 PM] anurag TL: Kal se sabhi apni isi according seating par mile, Nahi to monthly attendance me dikhega aapko ,order follow na karne ka result.
[23/12/23, 1:48:59 PM] kasim k: 2nd year
Computer Science & Engineering
Technocrats Institute of Technology [Excellence]
RAMAKANT PANDEY	
9122179433	
after exam  join
[23/12/23, 1:49:02 PM] kasim k: 2nd year
Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
RAHUL 	
6392981522
25December
[23/12/23, 1:56:10 PM] Hafsa.: Name of Student: Mohammad Amjad 
College name:SIRT
Contact no: 6207037658
Branch: EE
Year: 3th year
Expected Date of Visit: 25 Dec
[23/12/23, 3:00:54 PM] kasim k: 2nd year
Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
INDRESH KUMAR SHAH	
9303578349
25Dec (indrpuri )
[23/12/23, 3:23:45 PM] Hafsa.: Name of Student: Sumit 
College name:SIRT
Contact no: 9340834285
Branch: EE
Year: 3th year
Expected Date of Visit: Will try to visit b/w 27-30 Dec
[23/12/23, 3:24:25 PM] anurag TL: Hafsa or Kasim ke alawa baki kisi ke prospect nahi ban rahe kya??
[23/12/23, 3:25:35 PM] anurag TL: Aaj 23rd Dec hai, Aapko 31st Dec 23 tak Minimum 4    addmission per caller karana hi hai
[23/12/23, 3:27:34 PM] Deepali E.C: Bane hai sir but me last me jate time dalti hu
[23/12/23, 3:50:29 PM] kasim k: 2nd year 
Computer Science & Engineering	
Technocrats Institute of Technology & Science	
INDERESH MISHRA	
9546468303	
30 Dec
[23/12/23, 4:19:10 PM] kasim k: ‎You deleted this message.
[23/12/23, 4:19:28 PM] kasim k: 2nd year
Computer Science & Engineering	
Technocrats Institute of Technology & Science	
VISHAL VERMA	
7805997934	
24Dec  sunday
[23/12/23, 4:30:06 PM] anchal e.c: 2nd year
165	Computer Science & 
Engineering	Oriental College of Technology	PRIYANSHU NAVEEN	8305275731	
After exam will think
[23/12/23, 4:35:00 PM] anchal e.c: 2nd year
	Computer Science & Engineering	Oriental College of Technology	AAYAM PAWAR	9179177593	call back 	after exam feb c++
[23/12/23, 5:29:17 PM] annu❤️: Bansal	college
UTKARSH RAI	8081408781	
inform himself 	After exam 
1st year
[23/12/23, 5:42:12 PM] annu❤️: Bansal	College
JYOTI YADUWANSHI	9826537357	
After exam 	In February 
1st year with friends
[23/12/23, 6:04:24 PM] Hafsa.: Name of Student: Iqra Khan
College name:LNCT
Contact no: 9907091017
Branch: EC
Year: 3th year
Expected Date of Visit: Will contact in January after practical
[23/12/23, 6:06:36 PM] anchal e.c: 2nd year
	Computer Science & Engineering-Data Science	IES College of Technology	AFROZ ALI	8207749602	c,c++ will think
[23/12/23, 6:16:06 PM] Hafsa.: Name of Student: Kamta Prasad Kushwaha 
College name:SIRT
Contact no: 9111655074
Branch: EE
Year: 3th year
Expected Date of Visit: Will come after 4 Jan
[23/12/23, 6:25:31 PM] anchal e.c: 2nd year 
Computer Science & Bussiness System	IES College of Technology	OM PRAKASH KUMAR	9798938792	not confirm visit date
[23/12/23, 6:28:27 PM] ~ Chauhan Shilpa: Name of Student:  SACHIN YADAV
College name:Trinity Bhopal
Contact no: 6307173549
Branch: cs
Year: 1th year
Expected Date of Visit: Will come after  January indrapuri ‎<This message was edited>
[23/12/23, 6:31:11 PM] ~ Chauhan Shilpa: Name of Student: UDIT NOURIYA
College name:Technocrats Institute of Technology - Computer Science and Engineering
Contact no: 8103347089
Branch: Computer Science & Engineering
Year: 3th year
Expected Date of Visit: Will come after 7 Jan indrapuri ‎<This message was edited>
[23/12/23, 6:38:17 PM] kp sir: In prospect main yeah samaj nahi aaraha ki 
Kis location main aayenge yeah log 
Indrapuri ya MPnagar
[23/12/23, 6:42:21 PM] Deepali E.C: Name of Student:  Tapan dhakad
College name:JNCT
Contact no: 7999436413
Branch: cs
Year: 3rd year
Expected Date of Visit: Will come 27 Chetak
[23/12/23, 6:44:34 PM] Deepali E.C: ‎This message was deleted.
[23/12/23, 6:48:12 PM] Deepali E.C: Name of Student:  Akash sangoi
College name:JNCT
Contact no: 9165270882
Branch: cs
Year: 3rd year
Expected Date of Visit: Will come next week
[23/12/23, 6:53:11 PM] anchal e.c: 2nd year 
Computer Science & Engineering-Data Science	IES College of Technology	SAMAR KUMAR	9508740465	
After exam Febuary
[24/12/23, 1:22:54 PM] anchal e.c: 3rd year
Computer Science & Engineering	Millennium Institute of Technology & Science
	ANMOL KUMAR	7370807826		
Not confirm date to visit
[24/12/23, 1:34:55 PM] ~ Chauhan Shilpa: Name of Student:  SANJAY PATEL
College name : Trinity Bhopal
Contact no: 8878330766
Branch: cs
Year: 1th year
Expected Date of Visit: Will come 24,25 December indrapuri ‎<This message was edited>
[24/12/23, 2:00:00 PM] kasim k: 2nd year
Computer Science & Engineering	
Technocrats Institute of Technology & Science	
PRACHI AHIRWAR	
9981463922	
27Dec indrpuri
[24/12/23, 2:19:14 PM] ~ Chauhan Shilpa: Name of Student:  SANJEEV KUMAR
College name : Trinity Bhopal
Contact no: 8936061724
Branch: cs
Year: 1th year
Expected Date of Visit: Will come 24,25 January mp nagar
[24/12/23, 2:20:24 PM] ~ Chauhan Shilpa: Name of Student:  SATYAM KUMAR VATS
College name : Trinity Bhopal
Contact no: 9508573705
Branch: cs
Year: 1th year
Expected Date of Visit: Will come 5 ,6 January indrapuri
[24/12/23, 3:00:38 PM] anchal e.c: 3rd year 
	Computer Science & Engineering	Millennium Institute of Technology & Science	MOHAMMAD NEHAL AZIM	9661283207	
2 jan
[24/12/23, 3:10:33 PM] kasim k: 2nd year
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
AKASH AHIRWAR	
9329132053	
28Dec
[24/12/23, 3:22:51 PM] anchal e.c: 3rd year 
Computer Science & Engineering	Millennium Institute of Technology & Science	
MD SOHEB AKHTAR	
9128067782	
 3,5 jan
[24/12/23, 3:26:49 PM] ~ Chauhan Shilpa: Name of Student:  SHUBHAM SINGH MARKO
College name : Trinity Bhopal
Contact no: 9754415759
Branch: cs
Year: 1th year
Expected Date of Visit: Will come 28,30 December mp nagar
[24/12/23, 3:28:43 PM] anurag TL: 👆🏻
[24/12/23, 3:28:48 PM] anurag TL: 👆🏻
[24/12/23, 3:29:17 PM] anurag TL: Inka kya hua, ye nahi aaye
[24/12/23, 3:29:38 PM] anurag TL: 👆🏻
[24/12/23, 3:29:48 PM] anurag TL: 👆🏻
[24/12/23, 3:30:13 PM] anurag TL: 👆🏻
[24/12/23, 3:30:25 PM] kasim k: not ans
[24/12/23, 3:30:26 PM] anurag TL: 👆🏻
[24/12/23, 3:30:34 PM] anurag TL: 👆🏻
[24/12/23, 3:31:28 PM] Deepali E.C: Home town chale gye hai 2-3 January ko aayenge
[24/12/23, 3:32:48 PM] annu❤️: Will Come after 27 December + 3 friend and sangam also
[24/12/23, 3:33:37 PM] Neha mam e.c: 3 friends ke naam mention karo aise nahi chal payega
[24/12/23, 3:34:05 PM] annu❤️: Maan usne ek ka naam btaya hai
[24/12/23, 3:34:10 PM] annu❤️: Abhi
[24/12/23, 3:34:17 PM] annu❤️: Bki jb ayega bta dungi puch kr
[24/12/23, 3:34:41 PM] annu❤️: Abhi wo function main hai bhr
[24/12/23, 3:35:20 PM] Neha mam e.c: Nahi ho payega aisa
[24/12/23, 3:35:36 PM] Neha mam e.c: Sabji ko data milla hai same college ka
[24/12/23, 3:35:40 PM] annu❤️: Ane se plhe puchkr bta dungi apko
[24/12/23, 3:35:56 PM] Neha mam e.c: To friend likhne se kuch nahi hoga
[24/12/23, 3:36:01 PM] annu❤️: Jiska btaya hai usko kr diya hai already mention
[24/12/23, 3:37:25 PM] anchal e.c: 3rd year 
	Computer Science & Engineering	Millennium Institute of Technology & Science	
RAJU PRAJAPATI	9336283632	
February not confirm date
[24/12/23, 3:56:46 PM] annu❤️: Bansal	College
ATUL SEN	
9301735948	
After exam 	Will Come 
1st year
[24/12/23, 4:05:03 PM] anchal e.c: 3rd year 
	Computer Science & Engineering	Millennium Institute of Technology & Science
	SEKH MERAJ	7644042910	end of January
		with frd Akash raju
[24/12/23, 4:12:24 PM] kasim k: 2nd year
Computer Science & Engineering	
Sagar Institute of Science & Technology & Research	
SHIVANI RANA	
9131584266	
27 December	
ashoka garden
[24/12/23, 4:31:52 PM] ~ Chauhan Shilpa: Name of Student:  VIKASH KUMAR TIWARI with friends (Avinash Gupta )
College name : Trinity Bhopal
Contact no: 8434943802
Branch: cs
Year: 1th year
Expected Date of Visit: Will come ,25 December indrapuri
[24/12/23, 5:12:34 PM] anup kumar ct: Out of station
After 3,4 days
[24/12/23, 5:12:53 PM] anup kumar ct: After exam
[24/12/23, 5:13:00 PM] anup kumar ct: after exam
[24/12/23, 5:34:48 PM] anchal e.c: 2nd year
	Electrical & Electronics Engineering	Bhopal Institute of Technology & Science, Bangrasia
	ANKIT KUMAR GUPTA	7355542062	
will be think
[24/12/23, 5:37:49 PM] kasim k: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
RAHUL KUMAR SHARMA	
7870045360	
 with shankar feb 10 after exam
[24/12/23, 5:52:52 PM] ~ Chauhan Shilpa: Name of Student:  YASH MALVIYA
College name : Technocrats Institute of Technology - Computer Science and Engineering
Contact no: 9754690763
Branch: cs
Year: 3th year
Expected Date of Visit: Will come ,28 December indrapuri
[24/12/23, 6:01:16 PM] anurag TL: Main kal Sham Tak aap sabhi se ye report chahi thi, kisi ne share nahi ki, 
Aap ko jo bhi Instructions diye jaye unhe strictly follow karna apni habit me le aaye, 
Bad me koi mere pas rone na aaye ki Sir Aisa kyo hua.
[24/12/23, 6:02:36 PM] anurag TL: Or aise kaise prospect ban rahe ki koi visit hi nahi aa rahi, 
Kaam karne me man nahi lag aap logo ka.
[24/12/23, 6:09:33 PM] kasim k: kis formate mai bhajna hai sir bataya nahi apna  aur samne se btana hain yeh grup pe tau fir kaisee share kare .
[24/12/23, 6:10:00 PM] anup kumar ct: Sir mujhe ye nahi pata tha ki Report massage karke dena hai ya Offline aapko dena hai kal aaya nahi tha so kuch confirm bhi nahi tha.
[24/12/23, 6:10:46 PM] anurag TL: To ab kyo puch rahe ho, kal bhi puch sakte the na ye bat
[24/12/23, 6:12:49 PM] anurag TL: Last week
Mon to Sat
From  18 Dec to 23 Sec

Total visit comes -
Total admission given-

Caller Name
[24/12/23, 6:14:48 PM] annu❤️: Last week
Mon to Sun
From  18 Dec to 23 Sec

Total visit comes - 1 
Total admission given- 

Caller Name - Anushree
[24/12/23, 6:14:54 PM] annu❤️: Monday to Sunday
[24/12/23, 6:16:40 PM] Deepali E.C: Last week
Mon to Sun
From  18 Dec to 23 Sec

Total visit comes - 2
Total admission given- 

Caller Name - Deepali
[24/12/23, 6:17:29 PM] Hafsa.: Last week
Mon to Sun
From  18 Dec to 23 Dec

Total visit comes - 2
Total admission given- 

Caller Name - Hafsa
[24/12/23, 6:17:42 PM] kasim k: Last week
Mon to Sat
From  18 Dec to 23 Sec

Total visit comes -2
Total admission given- 0

Caller Name :- kasim
[24/12/23, 6:19:30 PM] ~ Chauhan Shilpa: Last week
Mon to Sat
From  18 Dec to 23 Sec

Total visit comes -3
Total admission given- 0

Caller Name :- Shilpa
[24/12/23, 6:22:38 PM] anchal e.c: Last week
Mon to Sun
From  18 Dec to 23 Sec

Total visit comes -0
Total admission given- 

Caller Name - Anchal
[24/12/23, 6:26:06 PM] anup kumar ct: Sir He told me that ki ye visit kar chuke hai.
aapne inform nahi kia.
So confirm kese Karu me?
[24/12/23, 6:27:06 PM] anurag TL: pucho aap kab visit kiya
[24/12/23, 6:27:15 PM] anurag TL: date
[24/12/23, 6:27:25 PM] anup kumar ct: 21 December
[24/12/23, 6:27:40 PM] anurag TL: ok
[24/12/23, 6:27:56 PM] anurag TL: main check kae lunga
[24/12/23, 6:28:08 PM] anup kumar ct: 3 din se call pick nahi kar raha tha 
isliye pata nahi chala
[24/12/23, 6:29:20 PM] anup kumar ct: and sir iske alawa bhi or bhi prospect hai jinhone date di thi but ab call pick nahi kar rahe hai.
so unka kese confirm hoga hamko?
[24/12/23, 6:30:29 PM] anurag TL: Ye to aap logo ko hi  pata karna padega, agar call pick nahi kar raha to means aaya hu nahi
Kyoki jo visit karne aa sakta hai wo atleast call to pick karega hi
[24/12/23, 6:31:00 PM] anurag TL: Kam se kam aap log apne prospect or visit ka record to maintain kar hi sakte hai
[24/12/23, 6:31:44 PM] anup kumar ct: sir call to ye bhi nahi pick kar raha tha 3 dino se.
but visit to kia isne bhi.
[24/12/23, 6:34:18 PM] anurag TL: dekho bhut simple si bat hai , aise case ki probability bhut kam hogi jo visit kar gya or apko pata nahi,
[24/12/23, 6:34:44 PM] anurag TL: isliye jo nahi aaye hai un par focus kare aap sabhi
[24/12/23, 6:35:16 PM] anurag TL: aise case 1 ya 2 honge wo main check kar lunga
[24/12/23, 6:35:19 PM] anurag TL: ok
[24/12/23, 6:40:28 PM] Hafsa.: Name of Student: Meet Jain 
College name:TIT
Contact no: 8109277022
Branch: CS
Year: 3th year
Expected Date of Visit: Will come in January first week
[24/12/23, 6:41:39 PM] Hafsa.: Name of Student: Shivam Sharma 
College name: Truba College 
Contact no: 9893512411
Branch: CS
Year: 4th year
Expected Date of Visit: Will contact in January
[24/12/23, 6:45:42 PM] anup kumar ct: sir unke visit kar ke jaane ke baad.
enquiry pad par calling hoti hai.
So wo call pick nahi karte fir hamara unko lagta hai ki abhi tak visit ke liye calls kar rahe the so ab admission ke liye hi call kar rahe honge.
so mostly not answer hi hote hai.
[24/12/23, 6:46:36 PM] annu❤️: Almost same case bhut hote hai yeh sir 1- 2 ni
[24/12/23, 6:48:41 PM] kasim k: aur sir  jaise date per nahi ate tau baad mai v ajate hai yeh phle ajata hai  tau hr koi nahi btata ane ke phle . 
yeh apko share krte hai tau ap check kr ke bata diya kro.
[24/12/23, 6:53:37 PM] kasim k: 2nd year
Computer Science & Engineering	
J.N. College of Technology	AYUSH CHOUDHARY	
9691255508	
feb 10 after exam
[24/12/23, 6:55:46 PM] Deepali E.C: ‎This message was deleted.
[24/12/23, 6:56:34 PM] Deepali E.C: Name of Student:  Arjun singh
College name : bansal 
Branch cs
Contact no: 7354261465
Branch: cs
Year: 2nd year
Expected Date of Visit: Will come , 3 January
[24/12/23, 6:57:52 PM] Deepali E.C: Name of Student:  Ashish malviya 
College name : sestec
Contact no: 7024093492
Branch: cs
Year: 2nd year
Expected Date of Visit: Will come , 28 dec
[24/12/23, 6:59:02 PM] Deepali E.C: Name of Student:  yashvant singh
College name : bhopal institute 
Branch cs
Contact no: 7999282865
Branch: cs
Year: 2nd year
Expected Date of Visit: Will come , 29 dec
[24/12/23, 7:04:16 PM] anup kumar ct: sir so abhi me Weekly report me Dalu ya nahi.?
[24/12/23, 7:08:28 PM] anurag TL: Nahi Dalna hai report me
[24/12/23, 7:09:19 PM] anurag TL: To phir ab se wahi visit or admission count honge Jo aapko pata honge ki aaj aa rahe hai or aapse bat karege
[24/12/23, 7:10:06 PM] anurag TL: Aage se jo bhi visit ya admission aap late hai use visit karane se lekar register karane tak aapka kaam hai 
Tabhi wah aapka count hoga
[24/12/23, 7:10:29 PM] anurag TL: That it
[24/12/23, 7:10:42 PM] anurag TL: That's it
[24/12/23, 7:15:32 PM] ~ Chauhan Shilpa: Name of Student:  LADE DEVENDRA NANDKISHOR
College name : Surabhi College of Engineering & Technology
Contact no: 7499865897
Branch: Computer Science & Engineering
Year: 3ed ear
Expected Date of Visit: Will come , 10 January indrapuri
[24/12/23, 7:16:36 PM] anup kumar ct: Last week
Mon to Sun
From  18 Dec to 23 Sec

Total visit comes -0
Total admission given- 

Caller Name - Anup
[24/12/23, 7:19:35 PM] anup kumar ct: Name of Student: Sameer 
College name: Bansal
Contact no: 9179521535
Branch: CSE
Year: 3RD
Expected Date of Visit: 26 December
[24/12/23, 7:20:59 PM] anup kumar ct: Name of Student: Ojesh
College name: Radharaman 
Contact no: 9179834460
Branch: CSE
Year: 3RD
Expected Date of Visit: 25 December
[24/12/23, 7:22:05 PM] anup kumar ct: Name of Student: Sameer 
College name: IES
Contact no: 7209187680
Branch: EEE
Year: 3RD
Expected Date of Visit: 27 December
[24/12/23, 7:24:12 PM] anup kumar ct: Name of Student: Dheeraj 
College name: Bansal
Contact no: 7389455741
Branch: EEE
Year: 3RD
Expected Date of Visit: 27 December
[24/12/23, 7:25:47 PM] anup kumar ct: Name of Student: Ritika 
College name: LNCT
Contact no: 9301903020
Branch: CSE
Year: 3RD
Expected Date of Visit: 31 December
[24/12/23, 7:27:02 PM] anup kumar ct: Name of Student: Shubham 
College name: SIRT
Contact no: 9174317328
Branch: ECE
Year: 3RD
Expected Date of Visit: 7 Jan
[24/12/23, 7:28:13 PM] anup kumar ct: Name of Student: Sapna
College name: SIRT
Contact no: 6265311291
Branch: ECE
Year: 3RD
Expected Date of Visit: 10 Jan
[25/12/23, 11:10:53 AM] anchal e.c: Today visit  chetak bridge
[25/12/23, 11:23:50 AM] Neha mam e.c: @team jiski 18-23 me visit aayi hai name ke saath mention kariye
[25/12/23, 11:38:05 AM] Deepali E.C: Oky mam
[25/12/23, 11:39:49 AM] kasim k: prince raj  (chetak )
abhishek yadav (indrpuri)
[25/12/23, 11:40:31 AM] annu❤️: Neeraj Bheel
[25/12/23, 11:48:12 AM] Hafsa.: Soumya Jain and Rohan Soni (Chetak Bridge)
[25/12/23, 11:55:25 AM] ~ Chauhan Shilpa: Mohit Meena lokesh , balram (indrapuri)
[25/12/23, 12:12:29 PM] naresh e.c: Will try today to Visit
[25/12/23, 12:34:57 PM] ~ Chauhan Shilpa: Name of Student: PANKAJ KUMAR
College name : Surabhi College of Engineering & Technology
Contact no: 7470613560
Branch: Computer Science & Engineering
Year: 3ed ear
Expected Date of Visit: Will come , 28  December
[25/12/23, 12:42:01 PM] Hafsa.: Will try to visit with father (Indrapuri)
[25/12/23, 12:42:27 PM] ~ Chauhan Shilpa: Name of Student: RAKESH
College name : Surabhi College of Engineering & Technology
Contact no: 6268234552
Branch: Computer Science & Engineering
Year: 3ed ear
Expected Date of Visit: Will come , 1 se 5 January ke bich me
[25/12/23, 12:49:21 PM] ~ Chauhan Shilpa: I plan to come in the evening by 4pm
[25/12/23, 12:54:46 PM] Hafsa.: Name of Student: Musharraf Imam Khan 
College name:TIT
Contact no: 7349918855
Branch: CS
Year: 3th year
Expected Date of Visit: Will try to visit on 26 Dec
[25/12/23, 12:56:52 PM] annu❤️: Mechanical Engineering	Corporate Institute of Science & Technology	NITISH KUMAR	8677095405	
Will Come Python 	
Inform himself In January 
4th year
[25/12/23, 12:59:45 PM] anup kumar ct: Name of Student: Ritik
College name: TIT
Contact no: 7747089897
Branch: CSE
Year: 4TH
Expected Date of Visit: 25 December
[25/12/23, 1:27:07 PM] Hafsa.: Name of Student: Pankaj Upadhyay 
College name:TIT
Contact no: 9302755020
Branch: CS
Year: 3th year
Expected Date of Visit: 27 Dec (Indrapuri) ‎<This message was edited>
[25/12/23, 1:51:40 PM] Hafsa.: Name of Student: Prince Kumar 
College name:TIT
Contact no: 8409760237
Branch: CS
Year: 3th year
Expected Date of Visit: Will visit after exam (January )
[25/12/23, 3:03:59 PM] kasim k: 2nd year
Artificial Intelligence and Machine Learning	Sagar Institute of Research & Technology	
KAPIL PRAJAPATI	
7389339915	
1Jan
[25/12/23, 3:11:06 PM] Hafsa.: Name of Student: Rahul Ahirwar 
College name:TIT
Contact no: 7879346067
Branch: CS
Year: 3th year
Expected Date of Visit: Will come after Makarsankranti (January )
[25/12/23, 3:17:19 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
NRI Institute of Information Science & Technology
	SATEEKA NANDA	
7067035861	
Will Come 	In January 
2nd Year
[25/12/23, 3:26:40 PM] Hafsa.: Name of Student: Mohammad Maaz Uddin
College name:Radha Raman
Contact no: 7761066799
Branch: EC
Year: 1th year old prospect 
Expected Date of Visit: 25 Dec ‎<This message was edited>
[25/12/23, 3:33:00 PM] naresh e.c: Name :- Aryan narwale  
College: - bansal 
Branch :- it 
Expected date of visit :- will come in 5 days
[25/12/23, 3:33:24 PM] naresh e.c: Number: - 	9691145504
[25/12/23, 3:34:07 PM] kasim k: 2nd year
Oriental College of Technology
AJAY TIWARI	
9425752703	
1Jan
[25/12/23, 3:40:42 PM] kasim k: Oriental College of Technology
2nd year
PALAK UPADHYAY	8303168052	
join in feb after exam
[25/12/23, 3:40:52 PM] kasim k: branch :- CS
[25/12/23, 3:51:12 PM] naresh e.c: Name :- harshit lokhande 
College: - bansal 
Branch :- it
Number: - 7909444757
Year :- 3rd 
Expected date of visited :- 28 dec with frnds Indrapuri
[25/12/23, 4:28:53 PM] anup kumar ct: Name of Student: Piyush 
College name: Sistech 
Contact no: 9984125639
Branch: CSE
Year: 3RD
Expected Date of Visit: 31 December
[25/12/23, 4:30:53 PM] anup kumar ct: Name of Student: Aakriti 
College name: LNCT
Contact no: 8234026731
Branch: ECE
Year: 3RD
Expected Date of Visit: 29 December
[25/12/23, 4:32:42 PM] anup kumar ct: Name of Student: Rohit, Sagar,Rahul and friends 
College name: JNCT
Contact no: 9142121652
Branch: ECE
Year: 3RD
Expected Date of Visit: 29 December
[25/12/23, 4:34:58 PM] anup kumar ct: Name of Student: Rudra
College name: SIRT
Contact no: 9424637224
Branch: ECE
Year: 3RD
Expected Date of Visit: 30 December
[25/12/23, 5:19:38 PM] ~ Chauhan Shilpa: Name of Student: SHIV KUMAR KUSHWAH + Sachin yuvraj ,hemu 
College name : Surabhi College of Engineering & Technology
Contact no: 6269794663
Branch: Computer Science & Engineering
Year: 3ed ear
Expected Date of Visit: Will come ,  25 January ke baad
[25/12/23, 5:25:25 PM] kasim k: 2nd year
Computer Science & Engineering	
Vaishnavi Inst. of Tech. & Science	
SHIVANEE	
9009795063	
with himanshi	
31Dec
[25/12/23, 6:05:11 PM] anup kumar ct: Come with Friend
[25/12/23, 6:25:56 PM] Hafsa.: Name of Student: Ashish Rahangdale
College name: SIRT
Contact no: 9302531865
Branch: AI/ML
Year: 3rd Yr
Expected Date of Visit: 31 Dec
[25/12/23, 6:44:30 PM] anurag TL: Aap log apne work ko bahut hi casually le rahe hai.
Aap sabhi ko minimum Target assign Kiya gya hai, par mujhe aap logo ka jara bhi intrest nahi dikh raha, 

Target achieve na hone par     necessary action liye jayege.

Those will be effective in your next month salary 👍🏻
[25/12/23, 6:45:05 PM] anurag TL: 6 days left
[25/12/23, 7:08:22 PM] anup kumar ct: Name of Student: Dharmendra 
College name: TIT
Contact no: 6397208339
Branch: CSE
Year: 3RD
Expected Date of Visit: 30 December
[25/12/23, 7:16:20 PM] Neha mam e.c: Viniket ko inform karo kal 2:30-4:30 back up hai
[25/12/23, 7:16:45 PM] Neha mam e.c: Md faizan 8827146652
[25/12/23, 7:16:56 PM] naresh e.c: Okk mam
[25/12/23, 7:18:12 PM] Neha mam e.c: Jay 6262854634
[25/12/23, 7:18:31 PM] Neha mam e.c: Jayesh 9302223680
[25/12/23, 7:19:43 PM] Neha mam e.c: Shivam 9301596813
[25/12/23, 7:22:51 PM] Neha mam e.c: Anand 7828891300
[25/12/23, 7:23:11 PM] Neha mam e.c: Gaurav 9977300328
[25/12/23, 7:23:25 PM] kasim k: done
[25/12/23, 7:23:28 PM] kasim k: done
[25/12/23, 7:23:36 PM] naresh e.c: Done
[25/12/23, 7:23:52 PM] Neha mam e.c: Amaratya 9546502638
[25/12/23, 7:24:26 PM] Neha mam e.c: Sumit 9171956257
[25/12/23, 7:24:45 PM] Neha mam e.c: Zeeshan 9131333480
[25/12/23, 7:25:28 PM] naresh e.c: Done
[25/12/23, 7:26:11 PM] Neha mam e.c: Sabko kar dena
[25/12/23, 7:26:13 PM] kasim k: call ans nahi kia msg drop kr dia
[25/12/23, 7:26:35 PM] kasim k: not ans
[25/12/23, 7:26:41 PM] naresh e.c: Done
[25/12/23, 7:28:30 PM] naresh e.c: Done
[25/12/23, 7:29:08 PM] Neha mam e.c: Sabko dhyan se kar dena
[25/12/23, 7:29:27 PM] kasim k: done
[25/12/23, 7:30:43 PM] naresh e.c: Done
[26/12/23, 12:42:13 PM] annu❤️: Computer Science & Engineering	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	BHUPENDRA BHUNJIA	8827499845	
Will Come 	Inform himself In February 
3rd Year
[26/12/23, 12:47:01 PM] anchal e.c: Name of Student: Deepshikha 
College name: Mittal 
Contact no: 9343903957
Branch: CSE
Year: 3RD
Expected Date of Visit: after 30 dec will be think
[26/12/23, 12:59:29 PM] anchal e.c: Name of Student: RUPAM MISHRA
College name: Mittal 
Contact no: 9301858940
Branch: CSE
Year: 3RD
Expected Date of Visit: will be think not confirm visit date
[26/12/23, 1:15:48 PM] Hafsa.: Name of Student: Rishabh Chourey
College name: SIRT
Contact no: 6264048994
Branch: AI/ML
Year: 3rd Yr
Expected Date of Visit: After 3 January
[26/12/23, 1:25:47 PM] anup kumar ct: Name of Student: Vashishth 
College name: LNCT
Contact no: 7747811759
Branch: CSE
Year: 3RD
Expected Date of Visit: 31 December
[26/12/23, 1:27:53 PM] anup kumar ct: Name of Student: Manish
College name: SIRT
Contact no: 7724047287
Branch: AIML
Year: 3RD
Expected Date of Visit: 30 December
[26/12/23, 1:29:01 PM] anup kumar ct: Will come with Sanjay, Suresh,kaluram
[26/12/23, 1:29:29 PM] anup kumar ct: for Admission
[26/12/23, 1:54:14 PM] Hafsa.: Name of Student: Sharad Shrivas
College name: SIRT
Contact no: 9340707413
Branch: AI/ML
Year: 3rd Yr
Expected Date of Visit: 27 Dec ‎<This message was edited>
[26/12/23, 2:02:52 PM] kasim k: 3rd year
Computer Science & Engineering	
All Saints' College of Technology	
SUMIT MANDAL	
6205983448		
coming today 26 dec
[26/12/23, 2:04:30 PM] kp sir: Apanlog calling main yeah ku nahi bolrahe hain ki coding thinker ke 4 center hai mp main 
.
Phir bhopal main 2 bolnaa hai 
Apanlog Siddhe bolrahe hai Hamara bhopal main center 2 place main hai aisha ku jo bhi aisha bolrahe turant usee correct karooo
[26/12/23, 2:56:56 PM] anup kumar ct: Name of Student: Abhishek 
College name: Sistech 
Contact no: 6261478016
Branch: CSE
Year: 3RD
Expected Date of Visit: 30 December
[26/12/23, 3:00:12 PM] kp sir: Anurag Sir aaap calling sunoo sabhi ki , muje 4-4  admission Dec last tak chaiyee sabhi logo se . 
Aur common ek format Bana Lee ki agar koi admission nahi karataa hai toh uskaa kya karnaa hai Jo karaarahe hain toh unko kaise karnaaa hai . 1Jan se apply karnaa hai muje admission chaiyee any how jo nahi Karapaarahe hain free kartee jaaiye koi dikkat nahi .
[26/12/23, 3:07:27 PM] anup kumar ct: Name of Student: pranay 
College name: TIT
Contact no: 9617504820
Branch: MCA
Year: final
Expected Date of Visit: 27 December
[26/12/23, 3:16:52 PM] Hafsa.: Name of Student: Rajendra Jatav with 3 friends 
College name: Trinity College 
Contact no: ,9754716986
Branch: CS/ML
Year: 1st Yr old prospect 
Expected Date of Visit: 26 Dec Indrapuri ‎<This message was edited>
[26/12/23, 3:24:43 PM] anup kumar ct: Name of Student: Lokesh 
College name: SIRT
Contact no: 6267257735
Branch: AIML
Year: 3RD
Expected Date of Visit: 26 December
[26/12/23, 3:34:09 PM] anchal e.c: Name of Student: Niraj ukande 
College name: TIT
Contact no: 9301938054
Branch: CS
Year: 3RD
Expected Date of Visit: 5 January
[26/12/23, 4:05:54 PM] kasim k: VERSHA	
7748904399		
29Dec visit plan
[26/12/23, 4:13:05 PM] anup kumar ct: Name of Student: Numan
College name: Oriental 
Contact no: 8709321150
Branch: IT
Year: 3RD
Expected Date of Visit: 30 December
[26/12/23, 4:14:23 PM] anup kumar ct: Name of Student: Abhishek 
College name: LNCT
Contact no: 8461801896
Branch: ECE
Year: 3RD
Expected Date of Visit: 31 December
[26/12/23, 4:17:30 PM] annu❤️: Information Technology	Oriental Institute of Science & Technology	SAKET KUMAR YADAV	8271022303	
Will Come Java	After exam 
2nd Year
[26/12/23, 4:21:07 PM] ~ Chauhan Shilpa: Name of Student: ARIHANT JAIN
College name: Lakshmi Narain College of Technology
Contact no: 6388592612
Branch: Computer Science & Engineering
Year: 2nd year 
Expected Date of Visit: after exam
[26/12/23, 4:23:26 PM] ~ Chauhan Shilpa: Name of Student: SHIVAM PARASTE
College name: Technocrat Institute of Technology
Contact no: 8959098519
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: last January ‎<This message was edited>
[26/12/23, 4:29:23 PM] kasim k: RGPV	
btec 	
RAKHI	6265994046
fsd	27December
[26/12/23, 4:31:59 PM] Hafsa.: Name of Student: Mohsin Khan 
College name: TIT
Contact no: 7415256076
Branch: CS/AIML
Year: 3rd Yr
Expected Date of Visit: Going home town; will contact in mid Jan
[26/12/23, 4:36:38 PM] kasim k: college name : - SAGAR	
branch :- BE	
Name :- VIKAS MANDAL	
number :- 8709730944	
january 1 indrpuri
[26/12/23, 4:40:42 PM] naresh e.c: Name :- 	VAISHNAVI		
Number :- 9301590048	
Branch: - cs
College: - bansal 
2 January
[26/12/23, 5:20:09 PM] annu❤️: Information Technology	Oriental Institute of Science & Technology	SHIVAM KEVAT	6260810523
Will think 	After exam 
2nd Year
[26/12/23, 5:22:15 PM] naresh e.c: Name :-	KAUSHAL AHIRWAR		
Number :-9977949032
Branch :- cs 
College: - bansal 
3 January
[26/12/23, 5:32:48 PM] anchal e.c: Name of Student: RISHIKA PAL
College name: TIT
Contact no: 9691897687
Branch: CS
Year: 3RD
Expected Date of Visit: not confirm date of visit
[26/12/23, 5:33:10 PM] anurag TL: Jiski visit aa rahi ho bta dena
[26/12/23, 5:40:43 PM] anurag TL: Ok , friends name??
[26/12/23, 5:41:30 PM] ~ Chauhan Shilpa: Name of Student: pura yadav 
Expected Date of Visit: 30 se 31 December ( mp nagar office)
[26/12/23, 5:42:55 PM] annu❤️: + shraddha will come on Sunday 31 December
[26/12/23, 5:43:48 PM] anurag TL: Ye visit aai kya??
[26/12/23, 5:44:04 PM] anurag TL: Kya hua inka
[26/12/23, 5:44:15 PM] kasim k: call nahi lg raha avi uska
[26/12/23, 5:47:07 PM] Deepali E.C: Will come today inderpuri
[26/12/23, 5:48:14 PM] annu❤️: Shubhakar Pathak 
7209183660
 coming today indrapuri
[26/12/23, 5:49:58 PM] anup kumar ct: Come Tomorrow
[26/12/23, 5:58:27 PM] annu❤️: Information Technology	Oriental Institute of Science & Technology	GAUTAM KUMAR	6200143130	
Will Come Cc++	
31 December	 
Indrapuri 
2nd Year
[26/12/23, 6:11:19 PM] anchal e.c: Electronics & Communication Engineering	Oriental Institute of Science & Technology	
ALINA SYED ALI	
9302113324		 
5 January indrapuri fsd							
2nd year
[26/12/23, 6:32:16 PM] ~ Chauhan Shilpa: Name of Student: PRATHMESH SAIKHEDKAR
College name: Technocrat Institute of Technology
Contact no: 9131353617
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: last  1 se 5 January mp nagar ‎<This message was edited>
[26/12/23, 6:32:43 PM] anup kumar ct: ujjawal Sahu
7898996413
TIT
BCA
31 DECEMBER
[26/12/23, 6:38:22 PM] anchal e.c: Name of Student: saif Khan 
College name: Technocrat Institute of Technology
Contact no: 7697928887
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: 2,3 January
[26/12/23, 6:59:38 PM] anup kumar ct: Name of Student: Himashu 
College name: Corporate 
Contact no: 9528068416
Branch: AILM
Year: 2BD
Expected Date of Visit: 31 December
[26/12/23, 7:02:27 PM] anurag TL: Aa gye ye kya??
[26/12/23, 7:03:44 PM] Deepali E.C: Sir abhi call receive nhi kiya ek bar or call kar ke puch lungi
‎[26/12/23, 7:06:11 PM] kp sir: ‎audio omitted
[26/12/23, 7:07:04 PM] annu❤️: 20, 000 hi kar rhe hai installment
Aur 18000 one time Payment
[26/12/23, 7:07:06 PM] kasim k: purani hi fees pitch kr rahe 20k nd 18k
[26/12/23, 7:07:09 PM] naresh e.c: 20k hi pich kr rahe h sir
‎[26/12/23, 7:07:21 PM] kp sir: ‎audio omitted
[26/12/23, 7:10:45 PM] anurag TL: Sir inquiry kiski hai??
[26/12/23, 7:10:56 PM] anurag TL: Fee bad gai hai January se
[26/12/23, 7:11:13 PM] anurag TL: Sabhi course par 5000 plus ho jayegi
[26/12/23, 7:11:20 PM] anchal e.c: 20k hi pich kr rhe hai sir
[26/12/23, 7:12:23 PM] anchal e.c: Means 25k fsd ki fees pich krna h ab
[26/12/23, 7:15:45 PM] anurag TL: Abhi to aap sab yah bolo ki after 1 Jan 2024 se fee bad sakti hai, kitni bad sakti hai wo bad me batayege
[26/12/23, 7:16:38 PM] anchal e.c: Ok sir
[26/12/23, 7:30:03 PM] Deepali E.C: Name of Student: shubham kumar
College name: oriental 
Contact no: 9262637273
Branch: cs
Year: 2nd
Expected Date of Visit: will come after exam
[27/12/23, 12:11:14 PM] anurag TL: Is Target ke bad kisne kitne admission Kara diye??
[27/12/23, 12:21:33 PM] kasim k: 2
[27/12/23, 12:22:16 PM] anurag TL: Mention Name and course also
[27/12/23, 12:22:24 PM] anurag TL: Date
[27/12/23, 12:22:28 PM] kasim k: 19 ke baad and 
5 total month mai
[27/12/23, 12:22:43 PM] annu❤️: Total 3 in month
[27/12/23, 12:22:46 PM] anurag TL: I am asking only after 19
[27/12/23, 12:22:54 PM] annu❤️: Ok
[27/12/23, 12:23:09 PM] kasim k: jay vishwkarma 
jayesh
fsd :- 9
[27/12/23, 12:24:41 PM] anurag TL: Ok
[27/12/23, 12:42:33 PM] anurag TL: Ye dono to direct hai, Jay ka to Maine registration kiya tha
[27/12/23, 12:43:03 PM] kasim k: registration apne kia tha us din apko dikhaya v tha akr samna se
[27/12/23, 12:43:14 PM] kasim k: msg vghre apke samne hi check kia
[27/12/23, 12:43:19 PM] kasim k: qki visit himanshu k sath kia tha
[27/12/23, 12:43:36 PM] kasim k: aur unka 5 logo ka grup hai yeh v btaya tha apko
[27/12/23, 12:45:03 PM] anurag TL: Screen shot share karo
[27/12/23, 12:45:30 PM] anurag TL: Or suno mujhe dhang se reply chahiye
[27/12/23, 12:45:31 PM] anurag TL: Nahi to jarurat nahi kal se aane ki
[27/12/23, 12:45:31 PM] anurag TL: Samjh me aa Raha ki nahi
[27/12/23, 12:45:50 PM] kasim k: sir aur kaise dhng se rpl chiye maina ky galat bola apko
[27/12/23, 12:46:02 PM] anurag TL: Mujhse kisi ne ne dhang se bat nahi ki to samjh lena sab
[27/12/23, 12:46:24 PM] kasim k: clear hi kr raha apko ki kb apko inform kia tha maine aur ky galat bola maina
[27/12/23, 12:46:28 PM] anurag TL: Ye koi dhang se bat karna nahi hota ok
[27/12/23, 12:47:01 PM] kasim k: yhai tau bola ki samna apko dikhaya tha isme maina ky galat bola apko
[27/12/23, 12:47:20 PM] kasim k: registration apna karwaya apna khud bola tha yeh tau mai v bol rah na isme galat ky hai sir
[27/12/23, 12:48:59 PM] anurag TL: Haan tmhe jab khud ki calling yad nahi rahti to mujhe sabka yad rakhna padta hai, yad nahi raha to tmhe yahi bolna tha ki Sir aapko check Kara denge hm
[27/12/23, 12:49:28 PM] kasim k: qki sir maina apko ek br already check kraya tha isliye bs whai yd dila raha tha mai apko
‎[27/12/23, 12:50:01 PM] kasim k: ‎image omitted
[27/12/23, 12:52:53 PM] annu❤️: Computer Science & Engineering-Data Science	Technocrat Institute of Technology	LAV KUMAR	8709928242	
Will Come Python 	indrapuri 	
31 December
2nd Year
[27/12/23, 1:05:06 PM] annu❤️: Computer Science & Engineering-Data Science	
Technocrat Institute of Technology
UMAIR AKHTAR	9263675580	
Will Come 	inform himself In January 
2nd Year
[27/12/23, 1:29:38 PM] Hafsa.: Will try to visit at evening (Indrapuri)
[27/12/23, 5:52:28 PM] kasim k: 3rd year [old prospect]
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
FIRDAUS ALI	
7562900451	
30December
[27/12/23, 5:53:01 PM] kasim k: 3rd year [old prospect]
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
AAKASH AHIRWAR	
6265561620	
31December
[27/12/23, 5:55:34 PM] anchal e.c: Coming today
[27/12/23, 6:01:35 PM] Hafsa.: Name of Student: Anuj Kumar Malviya 
College name: SISTech
Contact no: 7389260645
Branch: EC
Year: 3th year
Expected Date of Visit: Will come in January
[27/12/23, 6:15:06 PM] naresh e.c: ‎This message was deleted.
[27/12/23, 6:16:42 PM] anchal e.c: 1st year old prospect 
Electrical & Electronics Engineering	
Radha Raman Institute of Technology & Science	
PREETAM RAJ	7667174032			
Expected date - will come not confirm date to visit
[27/12/23, 6:34:32 PM] naresh e.c: Name :- srijan raj 
College: - tit
Branch :- it
Number: - 6205151895
Expected date of visit: - 29 dec
[27/12/23, 6:46:09 PM] kasim k: 3rd year 
Computer Science & Engineering	
Technocrat Institute of Technology	
DIPU KUMAR	
9835474108
1January
[27/12/23, 7:00:54 PM] kasim k: Computer Science & Engineering	
Scope College of Engineering	
ANIRUDDHA DAS	
6203245310	
nirmal + santosh
[27/12/23, 7:01:00 PM] kasim k: visit today
[27/12/23, 7:02:30 PM] Neha mam e.c: Enquiry 6 baje aa gyi abh aap likh rahe ho
[27/12/23, 7:02:47 PM] kasim k: han mam qki old prospect mai se hai tau unka hi takup le raha hu
[27/12/23, 7:02:57 PM] Neha mam e.c: Acha
[27/12/23, 7:03:29 PM] kasim k: ji mam
[27/12/23, 7:03:48 PM] Neha mam e.c: Kaha hai purane prospect me upar mark kro
[27/12/23, 7:11:51 PM] kasim k: mam old prospect hai  isliye nai dala qki unha shuru se takeup le raha  isliye
[27/12/23, 7:12:00 PM] naresh e.c: Name :- rohit pali 
College: - oist 
Branch :- cs 
Number: - 9770142112
Expected date of visit: - 29 dec
[27/12/23, 7:19:12 PM] anup kumar ct: Name of Student: Ishnoor jain
College name: LNCT
Contact no: 8989406749
Branch: CSE
Year: 4TH
Expected Date of Visit: 31 December
[27/12/23, 7:20:57 PM] anup kumar ct: Name of Student: Nupendra 
College name: NRI
Contact no: 7880031389
Branch: CSE
Year: 4TH
Expected Date of Visit: 31 December
[27/12/23, 7:21:47 PM] naresh e.c: Name :- Aarya Gupta 
College: - oist 
Branch :- cs 
Number: - 9993257605
Expected date of visit: - 31 dec
[27/12/23, 7:27:11 PM] anup kumar ct: Name of Student: Devansh 
College name: SIRT
Contact no: 8318784975
Branch: CSE
Year: 3RD
Expected Date of Visit: 10 Jan
[27/12/23, 7:27:44 PM] annu❤️: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
MD HEDAYATULLAH
6287250319	
Will Come python 	inform himself 
2nd Year
[27/12/23, 7:45:51 PM] anup kumar ct: Name of Student: Akshat 
College name: TIT
Contact no: 8889817987
Branch: IT
Year: 3RD
Expected Date of Visit: 5 Jan
[28/12/23, 3:58:49 PM] Hafsa.: Name of Student: Sarvesh Neekhra
College name: OIST
Contact no: 8319217446
Branch: CS/DS
Year: 3th year
Expected Date of Visit: Will try to come after 1 Jan
[28/12/23, 4:31:09 PM] naresh e.c: Name :- Manish kumar tiwari 
College: - nri 
Number: - 8357060846
Branch :- ee
Expected date of visit: - 31st dec
[28/12/23, 5:12:31 PM] Hafsa.: Name of Student: Tushar Kumar 
College name: Sha-Shib College 
Contact no: 8319217446
Branch: CS
Year: 3th year
Expected Date of Visit: Will contact after exam
[28/12/23, 5:21:20 PM] anchal e.c: 3rd year 
Electronics & Communication Engineering	Bansal Institute of Science & Technology	
AMIT KUMAR	9519718810	
30 dec
[28/12/23, 5:22:29 PM] ~ Chauhan Shilpa: Name of Student: MUKUL PANTHI
College name: Technocrats Institute of Technology [Excellence]
Contact no: 9826225810
Branch: CS
Year: 3th year
Expected Date of Visit: 5 se 10 January ke bich me
[28/12/23, 5:38:53 PM] anchal e.c: Name of Student: Hardik tiwari 
College name: sagar College 
Contact no: 9685136942
Branch: CS
Year: 3th year old prospect 
Expected Date of Visit: 30 dec
[28/12/23, 5:46:30 PM] anup kumar ct: sir He told he had visited the institute in indrapuri please confirm it.
[28/12/23, 5:48:22 PM] anup kumar ct: jay prakash
6265195392
 will come for admission before 31 Dec
[28/12/23, 5:56:59 PM] anchal e.c: Name of Student: Ranjeet Kumar 
College name: Patel College 
Contact no: 7292929845
Branch: CS
Year: 3th year old prospect 
Expected Date of Visit: not confirm date to visit
[28/12/23, 5:59:13 PM] Hafsa.: He will try to visit Indrapuri
[28/12/23, 6:03:58 PM] anup kumar ct: Name of Student: Vishal Pandey with friends+3
College name: TIT
Contact no: 9140001769
Branch: IT
Year: 2ND
Expected Date of Visit:  28 Dec
[28/12/23, 6:15:24 PM] anchal e.c: Name of Student: Vivek Dhakad
College name: SAM College 
Contact no: 9981574174
Branch: CS
Year: 3th year old prospect 
Expected Date of Visit: after 30 dec
[28/12/23, 6:16:53 PM] Hafsa.: Name of Student: Shivam Kumar Jha
College name: SIRT
Contact no: 9589446418
Branch: CS
Year: 3th year
Expected Date of Visit: 8 January
[28/12/23, 6:51:45 PM] anup kumar ct: Name of Student: Anirudh 
College name: TIT
Contact no: 7987325854
Branch: CSE
Year: 3RD
Expected Date of Visit:  5 Jan
[28/12/23, 6:54:58 PM] ~ Chauhan Shilpa: Name of Student: Mukesh 
College name: oist
Contact no: 7879711612
Branch: CSE
Year: 4th
Expected Date of Visit:  29 se 30 December mp nagar
[28/12/23, 7:11:13 PM] Deepali E.C: Name of Student: Vivek kumar
College name: Radha raman College 
Contact no: 6203884456
Branch: CS
Year: 2 nd year
Expected Date of Visit: Will come 31 dec
[28/12/23, 7:12:50 PM] Deepali E.C: Name of Student: Vivek warudkar
College name:  Sirt College 
Contact no: 7225014996
Branch: aiml
Year: 2 nd year
Expected Date of Visit: Will come 02 January
[28/12/23, 7:14:58 PM] Deepali E.C: Name of Student: Divyansh chaurasiya
College name: Radha raman College 
Contact no: 6264816202
Branch: CS
Year: 2 nd year
Expected Date of Visit: Will come after exam
[28/12/23, 7:16:28 PM] ~ Chauhan Shilpa: Name o Student: Anubhav Gupta
College name: lnct
Contact no: 9755756201
Branch: BBA
Year:  2ad year 
Expected Date of Visit:  2 January
[28/12/23, 8:01:13 PM] anurag TL: Admission ka kya status hai, 
Aaj 28 ho gai
Only 3 days left.
[28/12/23, 8:12:32 PM] anup kumar ct: Name of Student: Ramesh 
College name: SIRT
Contact no: 7067350871
Branch: CSE
Year: 3RD
Expected Date of Visit:  7 Jan
[29/12/23, 10:04:06 AM] kasim k: + khushi verma coming today
[29/12/23, 12:04:41 PM] anchal e.c: Name o Student: Ajay soni 
College name: LNCt 
Contact no: 8815042543
Branch: CS 
Year:  3rd year 
Expected Date of Visit:  end of January
[29/12/23, 12:09:37 PM] anup kumar ct: Name of Student: Priyanshu 
College name: SIRT
Contact no: 9399108535
Branch: CSE
Year: 3RD
Expected Date of Visit: will call 10 Jan
[29/12/23, 12:15:14 PM] annu❤️: Information Technology	Oriental College of Technology	
RISHI CHOURASIYA	9301750526	
Indrapuri 		
inform himself 	
Will Come 	After semester 
3rd Year
[29/12/23, 12:33:36 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology	ABHISHEK RANJAN	7091633234	
Will come Python 
Indrapuri 2 January 
Old prospect
2nd Year
[29/12/23, 1:04:29 PM] naresh e.c: Name :- vidhan paul 
College: - nri 
Branch :- ee
Number: - 9131728703
Expected date of visit: - 31st dec
[29/12/23, 1:23:20 PM] annu❤️: Computer Science & Engineering	
Millennium Institute of Technology & Science	
RASHID HUSAIN	9264487623
Will Come 2 January
Old prospect
2nd Year
[29/12/23, 1:57:43 PM] anup kumar ct: Name of Student: Aniket
College name: Oriental 
Contact no: 9407869995
Branch: EC
Year: PO
Expected Date of Visit: will call
[29/12/23, 3:08:08 PM] annu❤️: Computer Science & Engineering	
Technocrats Institute of Technology - Computer Science and Engineering	
RANJEET BHANSAR	9179255738
Will Come in January
2nd year 
Old prospect
[29/12/23, 3:09:41 PM] anup kumar ct: Name of Student: Vivek 
College name: Radharaman 
Contact no: 9301785840
Branch: CSE
Year: 3RD
Expected Date of Visit: will call
[29/12/23, 3:25:02 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
ADIL QURESHI	9559864675
Will Come 2 January
Old prospect
2nd year
[29/12/23, 3:38:11 PM] naresh e.c: Name :- subham lowanshi 
College: - nri 
Branch :- cse
Number :- 8269420617
Expected date of visit: - 2 January
[29/12/23, 3:40:02 PM] kasim k: 2nd year
Electronics & Communication Engineering	
J.N. College of Technology	VISHAL KUSHWAHA	
6260856669	
+ sachin, harsh ,and chetan
jan1 week
[29/12/23, 3:41:07 PM] anup kumar ct: will come with akash,shivam,swati
[29/12/23, 3:49:11 PM] anchal e.c: Name o Student: Monika 
College name: IES college 
Contact no: 9301733622
Branch: CS 
Year:  2rd year 
Expected Date of Visit:  will think
[29/12/23, 3:55:22 PM] naresh e.c: Name :- sonu kumar 
College: - nri 
Branch :- cse 
Number: - 8002467030
Expected date of visit: - 29 dec Indrapuri
[29/12/23, 3:59:15 PM] anchal e.c: Name o Student: Aaditya Singh 
College name: IES college 
Contact no: 7380542543
Branch: CS 
Year:  2rd year 
Expected Date of Visit: After 15 February
[29/12/23, 4:13:25 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Data Science	
Technocrat Institute of Technology	
MOHAMMAD AKRAM ALI	
8358909946
Will Come in January
Old prospect 2nd year
[29/12/23, 4:22:52 PM] annu❤️: Computer Science & Engineering	
Patel College of Science & Technology	
AMIT KUMAR VARMA	9131103924
Will Come in January 
Indrapuri. 
2nd year
[29/12/23, 4:30:20 PM] anchal e.c: Name o Student: Nasbulain Ansari 
College name: IES college 
Contact no: 9934339660
Branch: CSE
Year:  2rd year 
Expected Date of Visit: After exam end of February
[29/12/23, 5:18:32 PM] ~ Chauhan Shilpa: Name o Student:  ANKESH KUMAR
College name: Oriental Institute of Science & Technology
Contact no: 9798229223
Branch: Information Technology
Year:  3ed year 
Expected Date of Visit: February
[29/12/23, 5:21:16 PM] ~ Chauhan Shilpa: Name o Student: MONTI MEENA
College name: J.N. College of Technology
Contact no: 9617492269
Branch: Electronics & Communication Engineering
Year:  3ed year 
Expected Date of Visit: 31 December	mp nagar
[29/12/23, 5:25:59 PM] ~ Chauhan Shilpa: Name o Student: PURVESH BENDALE
College name: Technocrats Institute of Technology [Excellence]
Contact no: 8319158104
Branch: Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year:  3ed year 
Expected Date of Visit: 15 January ke baad	mp nagar
[29/12/23, 5:28:53 PM] anchal e.c: Name o Student: pintu Kumar 
College name: IES college 
Contact no: 9508112213
Branch: CSE
Year:  2rd year 
Expected Date of Visit: After exam end of February
[29/12/23, 6:19:01 PM] anchal e.c: Name o Student: Awanish Kumar 
College name: oriental college 
Contact no: 9794425286
Branch: CSE
Year:  3rd year 
Expected Date of Visit: After 15 January
[29/12/23, 6:25:46 PM] Neha mam e.c: Cabin sabhi callers aajayeye
[29/12/23, 7:11:35 PM] arpana e.c: coming today
[29/12/23, 7:31:39 PM] Deepali E.C: Name o Student: Tarun patil
College name:Sirt college 
Contact no: 9669752697
Branch: 
Year:  mca
Expected Date of Visit 30 dec
[29/12/23, 7:32:32 PM] Deepali E.C: Name o Student: Suman lal
College name:Sirt college 
Contact no: 7484039129
Branch: 
Year:  mca
Expected Date of Visit 2 January
[29/12/23, 7:33:15 PM] Deepali E.C: Name o Student: Deepesh chourasiya
College name:Sirt college 
Contact no: 8109006424
Branch: 
Year:  mca
Expected Date of Visit 3 jan
[29/12/23, 7:47:21 PM] Neha mam e.c: New batch start from 
Fsd Chetak bridge Mwf
7-8:30
8/jan/24

Fsd Indripuri TTS
5:30-7:00
13 January
[30/12/23, 10:46:33 AM] Deepali E.C: Will come today
[30/12/23, 12:12:45 PM] arpana e.c: Sagar Institute of Research, Technology & Science	ABHISHEK PANDEY	6267918757	
4th year
will come 31 dec
[30/12/23, 12:38:04 PM] arpana e.c: IES's College of Technology	AKASH UIKEY	8989935905	
4th year
	will come 31 dec
[30/12/23, 12:39:33 PM] annu❤️: Electronics & Communication Engineering	
All Saints' College of Technology	
MD SAQUIB	9576998986	
Will Come 	15 January	indrapuri 
2nd year
[30/12/23, 12:55:21 PM] Hafsa.: Going Indrapuri for visit
[30/12/23, 12:59:18 PM] Deepali E.C: Will come Monday 1 January
[30/12/23, 1:26:18 PM] annu❤️: Artificial Intelligence and Data Science
Lakshmi Narain College of Technology	YATHARTH PATIL	6266449309	
Will Come python 
2 January indrapuri
2nd year
[30/12/23, 2:03:22 PM] arpana e.c: Sagar Institute of Research & Technology Excellence	HARSH CHATURVEDI	9399374313	
2nd year
will come  31 dec
[30/12/23, 2:03:36 PM] arpana e.c: for inderpuri
[30/12/23, 2:32:10 PM] anup kumar ct: Coming today
[30/12/23, 2:46:33 PM] anurag TL: Aaj Sham me sabhi update Kara de mujhe kisne kitne admission ho gaye hai. 
Usi hisaab se aap sabhi ka performance bhi dikh jayega.
[30/12/23, 2:47:08 PM] anurag TL: Or new team bhi aa gai hai to decide bhi ho jayega
[30/12/23, 2:49:58 PM] naresh e.c: Sir mere is month 2 admission huye hai total or 14 visit
[30/12/23, 3:30:00 PM] annu❤️: 5 Enquiry 5 admission hai iss month
[30/12/23, 3:32:15 PM] anurag TL: ‎This message was deleted.
[30/12/23, 3:32:44 PM] anurag TL: This Month 

From  1 Dec to 30 Sec

Total visit comes -
Visit Names-
Total admission given- 
Admission Name-
Course -


Caller Name -
[30/12/23, 3:32:47 PM] anurag TL: Is format me bhej de sabhi
[30/12/23, 3:33:59 PM] annu❤️: 31 tk hoga sir month end
[30/12/23, 3:34:28 PM] kasim k: qki kl mere v 2 hai admission
[30/12/23, 3:50:02 PM] Neha mam e.c: Aaj sabki off daal dete hai batein karlo
[30/12/23, 3:54:59 PM] Neha mam e.c: @919893630880 Arpana and hadsa ko chode ke sabji off kar dijiyega
[30/12/23, 3:56:59 PM] Deepali E.C: Mam hum bhi call hi kar rhe hai prospect hi banaye hai
[30/12/23, 3:57:25 PM] anchal e.c: Calling hi kr rhe h
[30/12/23, 3:57:36 PM] annu❤️: Kaam hi kr rahe hai hum bhi
[30/12/23, 3:58:46 PM] Neha mam e.c: Dikh raha hai
[30/12/23, 4:03:28 PM] anurag TL: Ji Ma'am
[30/12/23, 4:06:04 PM] annu❤️: Bansal	
ATUL SEN	9301735948	After exam 	Inform himself 
1st year
[30/12/23, 4:09:15 PM] anchal e.c: Name o Student: Sanjay Kumar 
College name:TIT college 
Contact no: 6287844845
Branch: CSE
Year:  1 year old prospect 
Expected Date of Visit : after exam Febuary
[30/12/23, 4:33:24 PM] naresh e.c: Name :- Anil bonde  
College: - lnct 
Branch :- it 
Number :- 7828027328
Expected date of visit: - 30 dec Indrapuri
[30/12/23, 5:21:59 PM] anchal e.c: 3rd year 
	Computer Science & Engineering	IES's College of Technology	
RISHAV KUMAR	7903256293	 after 15 jan
[30/12/23, 5:22:21 PM] Deepali E.C: Name :- parth saxena 
College: - Lnct
Branch :- cs
Number :- 6267921109
Expected date of visit: - 7 January chetak
[30/12/23, 5:23:12 PM] Deepali E.C: Name :- shivan sharma
College: - Lnct
Branch :- cs
Number :- 8424964689
Expected date of visit: - 5 January chetak
[30/12/23, 5:56:39 PM] Hafsa.: Name of Student: Vanshika Verma 
College name: LNCT
Contact no: 9302229589
Branch: CS
Year: 3rd Yr
Expected Date of Visit: Will come in January (Out of station)
[30/12/23, 6:07:17 PM] Deepali E.C: Name :- Vishal Pandey 
College: - sha shib 
Branch :- ec
Number :- 8920190579
Expected date of visit: - 31 January chetak
[30/12/23, 6:08:22 PM] Deepali E.C: Name :- Abhinav sharma 
College: - sha shib 
Branch :- ec
Number :- 7357199800
Expected date of visit: - 31 dec and 2 January
[30/12/23, 6:14:19 PM] Hafsa.: Name of Student: Sudeep Kumar Mandal
College name: LNCT
Contact no: 6207784690
Branch: EC
Year: 3rd Yr
Expected Date of Visit: Will visit after 1 Jan ( Indrapuri )
[30/12/23, 6:38:31 PM] kasim k: This Month 

From  1 Dec to 30 dec

Total visit comes -  13

Visit Names-
1.khushi verma.
2.kaveri keshwani
3.santosh sen
4.nirmal sen
5.anirudh das
6.prince raj ku
7.abhishek yadav
8.ajay kewat
9.guruvendra ku
10.deepak singh tomar
11.kartik ahirwar
12.shailja meshwani
13.sumit mewada

Total admission given- 3

Admission Name-
1.kartik ahirwar
2.shailja meheshwani.
3.sumit mewada

Course - 2fsd ,1 pytn +dsa .


Caller Name - kasim
[30/12/23, 6:39:31 PM] Neha mam e.c: Sumit to continue nahi hai
[30/12/23, 6:39:40 PM] Neha mam e.c: Kartik konse batch ka hai
[30/12/23, 6:39:47 PM] kasim k: fsd 9
[30/12/23, 6:40:10 PM] Neha mam e.c: Fee to aa nahi paa rahi
[30/12/23, 6:40:21 PM] kasim k: baki 2 kl ho jygge.
[30/12/23, 6:41:26 PM] kasim k: practical chal raha the aj khtm hue monday se continue karega
[30/12/23, 6:43:19 PM] Neha mam e.c: Sir yadi 31st tak karenga to apan iss fee me lenge otherwise nahi
[30/12/23, 6:43:36 PM] Neha mam e.c: Sabhi aapne student se bole dena fsd9 ke
[30/12/23, 6:45:10 PM] annu❤️: This Month 

From  1 Dec to 30 Dec

Total visit comes - 5 

Visit Names- Neeraj Bheel , MD Abu Saif , Yashir Ali Khan , Aastha Nigam , Divyanshu Pandey 
Total admission given- 5

Admission Name - Zeeshan Khan , MD Abu Saif , Yashir Ali Khan , Aastha Nigam , Divyanshu Pandey 

Course - FSD , Cc++ ,  Cc++ , FSD , FSD 


Caller Name - Anushree

Aur kl ek aur ho jyega
[30/12/23, 6:46:04 PM] Neha mam e.c: Md Abu and yashwir to management decide karenga ki aapke hai kya nahi
[30/12/23, 6:46:10 PM] naresh e.c: This Month 

From  1 Dec to 30 dec

Total visit comes -  11

Visit Names-
1.Viniket.
2.Aryan.
3.Zaid.
4.Tamanna khan 
5.Tammana  khan brother 
6.Laljikushwaha 
7.prateek soni 
8.lucky 
9.Prachi
10.Ankit kujur 
11.Alim baig 


Total admission given- 2

Admission Name-
1.Viniket bayad
2.Zed mohammad 

Course - fsd ,1 c.c++


Caller Name - Naresh
[30/12/23, 6:46:23 PM] annu❤️: Sir ko bol diyaa tha aap baat kr lena students se
[30/12/23, 6:49:24 PM] anchal e.c: This Month 

From  1 Dec to 30 Dec

Total visit comes - 4

Visit Names- Praveen Kumar, Krishna Kumar, rishikesh, Ravi Kumar 
Total admission given- 1

Admission Name - Rishikesh 

Course -  Cc++ ,  


Caller Name - Anchal
[30/12/23, 6:49:46 PM] Deepali E.C: This Month 

From  1 Dec to 30 Sec

Total visit comes -6
Visit Names- morsingh 
Ajeet
Prashant
Tarun
Priyanshu
Avinash 

Total admission given- 0
Admission Name- 
Course -


Caller Name -Deepali
[30/12/23, 6:51:29 PM] Hafsa.: ‎This message was deleted.
[30/12/23, 6:52:27 PM] Deepali E.C: Name :- Abhishek mewada 
College: - TIT
Branch :- ec
Number :- 7974037834
Expected date of visit: - 2 January
[30/12/23, 6:55:37 PM] arpana e.c: This Month 

From 1 Dec to 30 Dec
Total visit  5
priyanshu pandey
Dhanajay choksey
Aarav
Sourabh pathak
shiv shibham

total admision given 1

Shiv shivay  ds python

caller name. -Arpana
[30/12/23, 7:12:11 PM] Hafsa.: Name of Student: MD Ajmal 
College name: Laxmipati College 
Contact no: 8252593675
Branch: EE
Year: 3rd Yr
Expected Date of Visit: Coming today
[30/12/23, 7:14:20 PM] Deepali E.C: Name of Student: kaushal silawat
College name: Tit
Contact no: 9131421281
Branch: Ec
Year: 3rd Yr
Expected Date of Visit: 5 January
[30/12/23, 7:15:46 PM] naresh e.c: Name :- yajat  prakash baraiya 
College: - lnct 
Branch: - cs
Number :- 9174870083
Expected date of visit: - 31st dec mp nagar
[30/12/23, 7:21:18 PM] arpana e.c: Sagar Institute of Research & Technology Excellence	PRIYANSH PATEL	6267323701	
2nd year
will come 5 jan
[30/12/23, 8:05:56 PM] Hafsa.: This Month 

From  1 Dec to 30 Sec

Total visit comes - 15
Visit Names- 
1. Gourishankar
2. Prakash Kumar Singh
3. Arjun
4. Uttam
5. Nikhil
6. Sumit Malviya
7. Soumya Jain
8. Rohan Soni
9. Rajendra Jatav
10.Rohit
11. Ankit Kumar
12. Ankit
13. Sharad Shrivas
14. Mohammad Ajmal
15. Hamdan
Total admission given- No admission 
Admission Name-
Course -


Caller Name - Hafsa
[31/12/23, 10:38:24 AM] Neha mam e.c: Discussion khatam ho gya ho to kaam karlo
[31/12/23, 10:59:24 AM] anchal e.c: ‎This message was deleted.
[31/12/23, 11:00:03 AM] anchal e.c: 3rd year 
	Computer Science & Engineering-Artificial Intelligence and Machine Learning	Lakshmi Narain College of Technology & Science	
ARYAN MISHRA
	9009436307
Not confirm date to visit
[31/12/23, 11:03:23 AM] Hafsa.: Name of Student: Irshad Ansari 
College name: SIRT 
Contact no: 7033311161
Branch: EE
Year: 3rd Yr
Expected Date of Visit: 2 Jan
[31/12/23, 11:07:28 AM] anurag TL: Sabhi apni seating par pahuche
[31/12/23, 11:07:37 AM] anurag TL: Abhi
[31/12/23, 11:07:53 AM] anurag TL: Or Anup aap chair 🪑 par baithe
[31/12/23, 11:09:13 AM] anup kumar ct: chair gandi hai.
Poori dust and dhool h us par.
[31/12/23, 11:09:48 AM] anurag TL: Achha
[31/12/23, 11:10:04 AM] anurag TL: To gandi par baith gye
[31/12/23, 11:10:09 AM] anurag TL: Kya??
[31/12/23, 11:10:22 AM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology	HARSHIT MISHRA
9522950647	
Will Come DSA
In January 
3rd year
[31/12/23, 11:11:02 AM] anup kumar ct: ye dusri wali hai yaha ab khali ho gyi wo log apni sitting par gaye toh.
[31/12/23, 11:11:15 AM] anup kumar ct: gandi wali side kar di
[31/12/23, 11:11:28 AM] anurag TL: To pahle bhi lekar baith sakte the
[31/12/23, 11:12:22 AM] anup kumar ct: .
And andar se chair lene ko mana kia hai sir ne.
[31/12/23, 11:13:04 AM] anurag TL: Bhut paresaniya hai aapke sath
[31/12/23, 11:13:10 AM] anurag TL: Solve karate hai jald hi
[31/12/23, 11:13:20 AM] anurag TL: Phir aage se koi pareshani hi nahi hogi
[31/12/23, 11:19:58 AM] kasim k: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
ABHISHEK KUMAR	
8434646744	
after exam
[31/12/23, 11:20:51 AM] Hafsa.: Name of Student: Kamlesh Kumar Ahirwar 
College name: SIRT 
Contact no: 7223846176
Branch: EE
Year: 3rd Yr
Expected Date of Visit: Will try on 5 Jan
[31/12/23, 11:22:39 AM] arpana e.c: Sagar Institute of Research & Technology Excellence	VAIBHAV PATERIYA
2nd year
	9630440300	After exam
[31/12/23, 11:23:12 AM] arpana e.c: Sagar Institute of Research & Technology Excellence	SHUBHAM SINGH
2nd year	9039839914	after exam
[31/12/23, 11:27:37 AM] Deepali E.C: Name of Student: Aman rathore
College name: 
Contact no: 9981218775
Branch: cs
Year: 2nd year
Expected Date of Visit: 31 dec
[31/12/23, 11:35:19 AM] kasim k: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal
.AKASH PRAJAPATI	
9755762319	
3jan indrpuri
[31/12/23, 11:36:33 AM] anchal e.c: 3rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning	Lakshmi Narain College of Technology & Science	
GEETESH MEHTO	7470728915		
after 2,3 January chetak
[31/12/23, 11:38:30 AM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology	
MANAV KATARE	9981515845	
Will Come 	10 January
3rd Year
[31/12/23, 11:41:05 AM] arpana e.c: Sagar Institute of Research & Technology Excellence	HEMANT MALVIYA	8815495861
2nd year
	before 18 jan will visit any date
[31/12/23, 11:42:58 AM] ~ Chauhan Shilpa: Name of Student:  CHANDRA PRAKASH KUSHWAHA
College name: VNS Group of Institutions
Contact no: 8962758447
Branch: Computer Science & Engineering
Year: 2nd Yr
Expected Date of Visit: Will think
[31/12/23, 11:46:07 AM] arpana e.c: Sagar Institute of Research & Technology Excellence	RASHMI BUWADE	6265696393
2nd year
	coming today 31 dec. for inderpuri
[31/12/23, 11:48:20 AM] kasim k: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
ADARSH VERMA	
9691622426	
discuss with friends  
date not cnfirm
[31/12/23, 11:55:49 AM] anup kumar ct: Name of Student: Irtiqa
College name: Sistech
Contact no: 8839928795
Branch: CSE
Year: 3RD
Expected Date of Visit: will call
[31/12/23, 12:06:48 PM] ~ Chauhan Shilpa: Name of Student:  VIKASH KUMAR TIWARI
College name: Trinity Bhopal
Contact no: 8434943802
Branch: cs
Year: 1 
Expected Date of Visit: 3 January
[31/12/23, 12:14:04 PM] anup kumar ct: Name of Student: Ashish 
College name: Sistech
Contact no: 9329105988
Branch: CSE
Year: 3RD
Expected Date of Visit: will call 10 Jan
[31/12/23, 12:22:21 PM] naresh e.c: Name:- Aman khare 
College: - tit 
Branch :- me 
Number: - 7089762823
Expected date of visit: - 1 January
[31/12/23, 12:25:24 PM] Deepali E.C: Name:- Deepanshu chauhan 
College: - tit 
Branch :- cs&aim
Number: - 9685953025
Expected date of visit: - 4 January
[31/12/23, 12:25:56 PM] Deepali E.C: Name:- Ankit sharma
College: - tit 
Branch :- cs&aim
Number: - Ankit sharma 
Expected date of visit: - after 10  January
[31/12/23, 12:29:06 PM] kasim k: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
CHETAN PAL	
7389632207	
6 Jan
[31/12/23, 12:30:02 PM] anup kumar ct: Name of Student: Ravindra 
College name: Sistech
Contact no: 7828961953
Branch: EC
Year: 3RD
Expected Date of Visit: 7 Jan
[31/12/23, 12:31:30 PM] Deepali E.C: Name: devyani malvi
College: - tit 
Branch :- cs&aim
Number: - 9301979798
Expected date of visit: - after 10  January inderpuri
[31/12/23, 12:39:02 PM] annu❤️: Electronics & Communication Engineering	
Technocrat Institute of Technology	
ABHAY GAUTAM	9074573837	
Will think 	inform himself 
3rd year
[31/12/23, 12:39:30 PM] Hafsa.: Name of Student: Vanshika Maheshwari 
College name: LNCT 
Contact no: 7828601903
Branch: EC
Year: 3rd Yr
Expected Date of Visit: Will come in 3-4 days
[31/12/23, 12:41:39 PM] anup kumar ct: Name of Student: Gautam 
College name: TIT
Contact no: 7247427512
Branch: CSEAIML 
Year: 3RD
Expected Date of Visit: 7 Jan
[31/12/23, 1:07:58 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[31/12/23, 1:08:59 PM] ~ Chauhan Shilpa: Name of Student:  SARTHAK SHARMA
College name: VNS Group of Institutions
Contact no: 7000594675
Branch: Computer Science & Engineering
Year: 2nd Yr
Expected Date of Visit: 5 January ke baad (mp nagar office)
[31/12/23, 1:10:02 PM] anup kumar ct: Name of Student: Saksham 
College name: LNCT
Contact no: 7000430048
Branch: CSEDS
Year: 3RD
Expected Date of Visit: 31 Dec
[31/12/23, 1:25:27 PM] Lalita Sahu: ‎anurag TL added Lalita Sahu
[31/12/23, 1:26:28 PM] arpana e.c: Lakshmi Narain College of Technology Excellence	GARIMA SHRIVASTAVA	
3rd year
will come 10 jan
[31/12/23, 1:47:47 PM] khushi e.c: ‎anurag TL added khushi e.c
‎[31/12/23, 3:14:23 PM] anurag TL: Data  Science.docx ‎document omitted
‎[31/12/23, 3:14:24 PM] anurag TL: Fullstack Webdevelopment with MERN.docx ‎document omitted
‎[31/12/23, 3:14:24 PM] anurag TL: java fullstack springboot.docx ‎document omitted
‎[31/12/23, 3:14:25 PM] anurag TL: Python Webdevleopment.docx ‎document omitted
[31/12/23, 3:14:29 PM] anurag TL: New courses
[31/12/23, 3:30:44 PM] kasim k: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
HIMANSHU BARMAN	7987835698	
6January
[31/12/23, 3:56:27 PM] Lalita Sahu: ‎This message was deleted.
[31/12/23, 3:58:50 PM] Lalita Sahu: ‎This message was deleted.
[31/12/23, 4:01:06 PM] anchal e.c: 3rd year 
	Computer Science & Engineering	Lakshmi Narain College of Technology & Science	
PRAGATI	
9179974707		
not confirm date February
[31/12/23, 4:06:01 PM] ~ Chauhan Shilpa: Name of Student-*
Number -
College name-
Branch-
Year-*
Expected Date of Visit-* ‎<This message was edited>
[31/12/23, 4:14:11 PM] Lalita Sahu: Name of Student-* Aman patil
Number -9179084679
College name-Oriental Institute of Science & Technology
Branch-Computer Science & Engineering
Year-* 4th yeat
Expected Date of Visit-* 1january
[31/12/23, 4:14:18 PM] khushi e.c: Name of Student-*. satyam Kumar 
Number - 6205537839
College name-  Technocrat Institute of Technology
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-* 2nd year 
Expected Date of Visit-* 31 December 4 pm
[31/12/23, 4:16:23 PM] khushi e.c: Name of Student-* harsh Gour 
Number -7470827898
College name-Technocrat Institute of Technology
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-* 2nd year 
Expected Date of Visit-* after 18 Jan
[31/12/23, 4:17:56 PM] Lalita Sahu: Name of Student-* Ashuthosh kumar
Number -6202656667
College name-Oriental Institute of Science & Technology
Branch-Information Technology
Year-*4th year
Expected Date of Visit-*10january
[31/12/23, 4:18:50 PM] khushi e.c: Name of Student-* Aranya Raj Gupta 
Number -6266369221
College name-Technocrat Institute of Technology
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-* 2nd year 
Expected Date of Visit-* after 18 Feb
[31/12/23, 4:21:58 PM] khushi e.c: Name of Student-Ankit Kumar 
Number - 6203742683
College name-Technocrat Institute of Technology
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-*2nd year 
Expected visit date -  1 jan
[31/12/23, 4:22:01 PM] Lalita Sahu: Name of Student-*KRISHAN KANT
Number -8827041717
College name-Bhopal Institute of Technology, Bangrasia
Branch-Electrical & Electronics Engineering
Year-*4th
Expected Date of Visit-*not confirmed date ending January
[31/12/23, 4:22:11 PM] arpana e.c: Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	ABID SIDDIQUI	8827661766
3rd year
	will think after 20 jan
[31/12/23, 4:24:12 PM] khushi e.c: Name of Student-*Shivam Choubey 
Number -7987079865
College name- technocrats institute of technology 
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-* 2nd year 
Expected Date of Visit-* 1 jan
[31/12/23, 4:27:06 PM] khushi e.c: Name of Student-* shorav Kumar 
Number - 7667128194
College name-Technocrat Institute of Technology
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-*2nd year 
Expected Date of Visit-*  after 15 Feb
[31/12/23, 4:37:03 PM] annu❤️: Computer Science & Engineering-Data Science	
Lakshmi Narain College of Technology Excellence	
TANISHA JAIN 	7489283974	
Call back 	In January 
After 20 
3rd Year
[31/12/23, 4:38:56 PM] khushi e.c: Name of Student-* subhi chakradhar 
Number - 6261007613
College name-Technocrats Institute of Technology [Excellence]
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-* 2nd year 
Expected Date of Visit-* after 8 Feb
[31/12/23, 4:43:47 PM] anup kumar ct: Name of Student: Mayur 
College name: TIT
Contact no: 7089937905
Branch: CSEAIML 
Year: 3RD
Expected Date of Visit: 31 Dec
[31/12/23, 5:05:28 PM] khushi e.c: Name of Student-* piyush dwivedi 
Number -8359909984
College name-Technocrats Institute of Technology [Excellence]
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-*2nd year 
Expected Date of Visit-* 2 nd Jan
[31/12/23, 5:10:11 PM] anup kumar ct: Name of Student: Mayur 
College name: Vaishnavi 
Contact no: 9109044867
Branch: AIML 
Year: 3RD
Expected Date of Visit: will think 10jan
[31/12/23, 5:31:05 PM] Lalita Sahu: Name of Student-*Kanak nagori
Number -8305000763
College name-Lakshmi Narain College of Technology
Branch-Information technology
Year-*4th
Expected Date of Visit-* 7thjanuary
[31/12/23, 5:48:56 PM] naresh e.c: Name :- laveen kewlani 
Number: -9406756468
College: - lnct 
Branch :- cse
Expected date of visit: - Feb 16
[31/12/23, 5:50:28 PM] anup kumar ct: Name of Student: Vaidik 
College name: LNCT
Contact no: 7909474766
Branch: CSEAIML 
Year: 2ND
Expected Date of Visit: 5 Dec
[31/12/23, 6:05:47 PM] anup kumar ct: Name of Student: Prashant 
College name: oriental 
Contact no: 7999914901
Branch: CSE
Year: 3RD
Expected Date of Visit: will think
[31/12/23, 10:27:24 PM] anurag TL: 💐💐💐💐*Happy New Year to all of you in advance*💐💐💐💐

On Change of this year, something's also change for all of you.
From tomorrow onwards these rules will be effective........

1- No one will directly interact with Management without following the proper channel.

2- From tomorrow your incentive like this,

Minimum 5 admission is compulsory to all, in a month 

I) 0-5 admission- No incentive.

II) 6-10 admission - 3% incentive per admission.

III) 11-15 admission - 5% incentive per admission.

IV) 16-20 admission - 7% incentive per admission.

V) above 20 admission in a month, after 20 the incentive would be 10% per admission.

3- Proper record of prospects maintain by yourself also. If you can't, we are not responsible for your incentive.

4- Follow all the orders/instructions given by your higher authorities.

5- Weekly update your your visits and admission to me.

If anyone does not follow these instructions, then definitely management will take necessary actions against him/her.


With best wishes 💐💐💐💐💐💐💐💐💐💐💐💐

Happy New Year to all of you 🎆
[02/01/24, 11:12:52 AM] anurag TL: Sabhi ko time par hi office aana hai
[02/01/24, 11:13:03 AM] anurag TL: Off jaisa kuch bhi nahi hai
[02/01/24, 11:13:13 AM] Deepali E.C: Sir hame thoda late hoga
[02/01/24, 11:13:22 AM] Deepali E.C: Hum abhi nikal rhe hai ghr se
[02/01/24, 11:13:34 AM] anurag TL: Bar bar kyo puch rahe hai, hota to aapko group par bta Diya jata
[02/01/24, 11:13:41 AM] anurag TL: Abhi kyo nikal rahe
[02/01/24, 11:13:51 AM] anurag TL: Time se niklna tha na
[02/01/24, 11:14:17 AM] Deepali E.C: Sir kal bhi hum aadha aa gye the fr wapis gye
[02/01/24, 11:15:04 AM] anurag TL: Usse aaj late ka kya relation
[02/01/24, 11:16:20 AM] kp sir: Jiskooo diktat hai office aakar discuss karlenaa ,group main conversation ka mana Kiya hai ,Jada hsi call karkee baat Kiya kareeee
[02/01/24, 11:16:28 AM] naresh e.c: Sir me nhi araha hu
[02/01/24, 11:16:50 AM] naresh e.c: Gadi nhi hai or bus nhi chal rahi hai
[02/01/24, 11:17:05 AM] anup kumar ct: Sorry Sir,
Not possible to come.
[02/01/24, 11:18:40 AM] Neha mam e.c: Tumhara to kal off tha to tum adhe rasta kyun aayi
[02/01/24, 11:19:33 AM] anup kumar ct: Public transports are not running.
And I don't have my own vehicle and licence.
[02/01/24, 11:20:06 AM] Neha mam e.c: No problem week off lelo
[02/01/24, 11:52:00 AM] kasim k: @919131608639 @919893630880  aj class rhegi ky calls arha batch 2/3 ke
[02/01/24, 11:59:45 AM] Deepali E.C: Name of Student-* shubankar 
Number - 6266781780
College name-sagar
Branch-ec
Year-*4th year
Expected Date of Visit-*  will come today
[02/01/24, 12:12:51 PM] annu❤️: Electrical & Electronics Engineering	
Bansal Institute of Research & Technology	
SHAMA BEE	8349603385	
Will Come 	6 January	indrapuri 
3rd year
[02/01/24, 12:31:50 PM] Lalita Sahu: Name of Student-*Lalit gour
Number -6263330665
College name-Lakshmi Narain College of Technology
Branch- InformationTechnology
Year-*4th yeat
Expected Date of Visit-*visit in February not a confirm date
[02/01/24, 12:52:24 PM] Lalita Sahu: Name of Student-*SHREYA GANGARADE
Number -7828060108
College name-Lakshmi Narain College of Technology
Branch-Information Technology
Year-*4th
Expected Date of Visit-*3january
[02/01/24, 1:04:44 PM] arpana e.c: Technocrats Institute of Technology & Science	UDAY PRATAP KOURAV
3rd year	9424964168	
will think after 10 jan
[02/01/24, 1:10:08 PM] Hafsa.: Name of Student: Prateek Patel and friends 
College name: TIT
Contact no: 6268830536
Branch: CSE
Year: 3rd Yr
Expected Date of Visit: Will contact in mid January
[02/01/24, 1:17:31 PM] kasim k: Electronics & Communication Engineering	
Sha-Shib College of Technology	
ABHISHEK ROY CHOUDHURY
7488907024	
Jan 28 with tushar
[02/01/24, 1:24:22 PM] ~ Chauhan Shilpa: Name of Student: ARIHANT JAIN
College name: Lakshmi Narain College of Technology
Contact no: 6388592612
Branch: Computer Science & Engineering
Year: 2nd Yr
Expected Date of Visit: after exam
[02/01/24, 1:24:49 PM] arpana e.c: Sagar Institute of Research & Technology	KSHITIJ BISHT	8319713629
3rd year
	will come 5 jan with frind smarth
[02/01/24, 1:28:07 PM] annu❤️: Electrical & Electronics Engineering	
Bansal Institute of Research & Technology	
ROHIT MEENA	8602962685	
Will Come Java 	
5 January	chetak 
3rd Year
[02/01/24, 3:07:47 PM] Hafsa.: Will try to visit (Indrapuri)
[02/01/24, 3:12:56 PM] Deepali E.C: Name of Student-manish singh
Number -7372859180
College name-JNCT
Branch-cs
Year-3rd year 
Expected Date of Visit-*3january
[02/01/24, 3:25:52 PM] arpana e.c: Technocrats Institute of Technology & Science	VIJAY MEHTA	7999255789
3rd year
	will think
[02/01/24, 3:34:18 PM] arpana e.c: Technocrat Institute of Technology	ROHIT CHOUHAN	9301694759
3rd year
	will think after 15 jan
[02/01/24, 3:45:15 PM] Deepali E.C: Name of Student-Harish Arya
Number -8823052356
College name-JNCT
Branch-cs
Year-3rd year 
Expected Date of Visit-*will come feb start
[02/01/24, 3:54:10 PM] arpana e.c: Technocrat Institute of Technology	NAGESH SAHU	7771936234	
3rd year
will come 8jan
[02/01/24, 4:35:04 PM] kasim k: ‎You deleted this message.
[02/01/24, 4:35:32 PM] kasim k: 3rd year
Computer Science & Engineering	
VNS Group of Institutions	
ANAMIKA JHARANIYA	
7723811670	
7 jan will think
[02/01/24, 4:44:02 PM] anchal e.c: 3rd year 
	Information Technology	Lakshmi Narain College of Technology
	PRANITA LAD	
9424571330	
  not confirm date to visit
[02/01/24, 5:12:17 PM] Deepali E.C: Will come 4 January
[02/01/24, 5:14:59 PM] Deepali E.C: Try to come in evening inderpuri
[02/01/24, 5:32:15 PM] arpana e.c: Bansal Institute of Science & Technology	BHARTI CHOUDHARY	9301236574
3rd year
	will think after 15 jan
[02/01/24, 5:45:13 PM] Hafsa.: Name of Student: Abhishek Rajput 
College name: Truba College 
Contact no: 9399183271
Branch: AI/DS
Year: 3rd Yr
Expected Date of Visit: Will come after Sankranti
[02/01/24, 5:53:28 PM] arpana e.c: Bansal Institute of Science & Technology	ESHA DHURWEY	9977935882
3rd year
	will come 7jan
[02/01/24, 5:58:22 PM] Deepali E.C: Will come half and hour chetak bridge
[02/01/24, 6:36:08 PM] kasim k: 3rd year
Computer Science & Engineering	
Patel College of Science & Technology	
PARAG KUROTHE	
7024299055	
20 Jan
[02/01/24, 6:48:20 PM] kasim k: 3rd year
Computer Science & Engineering	
Patel College of Science & Technology	
PRIYA YADAV	
6264521964	
20January
[02/01/24, 6:50:35 PM] kasim k: 3rd year
Computer Science & Engineering	
VNS Group of Institutions	
AMAN SINGH	
8269424717	
6Jan
[02/01/24, 6:51:22 PM] arpana e.c: Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	AKRITY KUMARI	7481079356	
3rd year	
will come  5 jan
[02/01/24, 7:01:46 PM] arpana e.c: Technocrat Institute of Technology	ANKUSH TOMAR	9009518543	
3rd year
	will think after 15 jan
[02/01/24, 7:05:21 PM] anurag TL: Indrapuri ka incentive aap logo ko is week mil jayega, aap pareshan na ho.
[02/01/24, 7:06:17 PM] Deepali E.C: Oky sir
[02/01/24, 7:06:48 PM] annu❤️: SATYAM VERMA
	8840703382	
Will Come Cc++	7 January

SAUMY KASHYAP
	9522329057	
After this semester 	Will Come 
1st year
[02/01/24, 7:12:14 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning	Lakshmi Narain College of Technology & Science	
SAMARTH
 BHABAK	
7648876080	
Date- 	will confirm 2,3 days
[02/01/24, 7:34:09 PM] Deepali E.C: Name of Student-Aditya narayan
Number -9113180183
College name-oriental
Branch-cs
Year-4th year
Expected Date of Visit-*will come next week
[03/01/24, 12:07:50 PM] khushi e.c: Name of Student-* Ansh sharma 
Number -8269248246
College name-Technocrats Institute of Technology [Excellence]
Branch-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year-* 2nd year 
Expected Date of Visit-* 3rd Jan
[03/01/24, 12:31:35 PM] annu❤️: ABHIJEET GHODESHWAR
9301271282	
Will Come After exam 
20 February
1st year
[03/01/24, 12:31:51 PM] naresh e.c: Name :- adarsh mehto 
College: - lnct 
Branch :- cse
Number: - 7748892636
Expected date of visit: - 5 January
[03/01/24, 12:48:22 PM] Hafsa.: Name of Student: Himanshu Patle
College name: NRI college 
Contact no: 6264632227
Branch: AI/DS
Year: 2nd Yr old prospect 
Expected Date of Visit: 10 Jan
[03/01/24, 1:15:11 PM] annu❤️: DEEPAK KUMAR
6264233353	
Will Come Cc++	
11 January
Bansal college 
1st year
[03/01/24, 1:16:08 PM] kasim k: 2nd year
Computer Science & Engineering	
J.N. College of Technology	
ANJALI JAIN	
8602216457	
after exam 17 feb.
[03/01/24, 3:07:02 PM] naresh e.c: Will come in evening Indrapuri
[03/01/24, 3:14:53 PM] kasim k: 3rd year
Artificial Intelligence and Machine Learning	
J.N. College of Technology	ASAD KHAN	
6232630608	
4 January indrpuri
[03/01/24, 3:24:57 PM] annu❤️: SANSKAR VERMA
7389056063	
Will Come DSA	
Indrapuri 
4 January 
1st Year
[03/01/24, 4:38:19 PM] Hafsa.: Name of Student: Mohammad Nadim
College name: SIRT
Contact no: 8102506790
Branch: EE
Year: 3rd Yr
Expected Date of Visit: Will contact after 20 Jan (Out of service)
[03/01/24, 5:04:14 PM] khushi e.c: Name of Student-* Nhikhil raghuwanshi 
Number -8103567568
College name-Technocrats Institute of Technology [Excellence]
Branch-Electronics & Communication Engineering
Year-*2nd year 
Expected Date of Visit-* after 10 Feb
[03/01/24, 5:24:07 PM] annu❤️: SURAJ KUMAR RAY
9009576780	
Will Come 	
25 January
1st year
[03/01/24, 5:42:49 PM] annu❤️: VISHAL MEWADA	9926084641	
After this semester 	
Will Come indrapuri 
1st year
[03/01/24, 5:47:49 PM] khushi e.c: Name of Student-* Harshit tripathi 
Number - 7985650789
College name- Trinity institute of technology and research 
Branch- Electronics & Communication Engineering
Year-* 2nd year 
Expected Date of Visit-* after 20 Jan
[03/01/24, 5:56:57 PM] khushi e.c: Name of Student-* Chunnu Kumar 
Number - 8210700710
College name- Trinity Institute of Technology & Research
Branch- Electronics & Communication Engineering
Year-* 2nd year 
Expected Date of Visit-* after 9 Feb
[03/01/24, 6:26:21 PM] suman coding e.c: ‎kp sir added suman coding e.c
[03/01/24, 6:44:57 PM] Lalita Sahu: Name of Student-* hariom meena
Number - 8435997306
College name- bansal collage
Branc
Year-1st
Expected Date of Visit-* 10febuary
Mp nagar
[03/01/24, 6:46:38 PM] Lalita Sahu: Name of Student-* harsh patle
Number -6260735757
College name- bansal collage
Year-*1st
Expected Date of Visit-* 20feb
Indrapuri
[03/01/24, 6:49:40 PM] Lalita Sahu: Name of Student-* maneshwari dhurwey
Number - 9343931940
College name*bansal collage
Year-* 1st
Expected Date of Visit-* 7january , FSD
Mpnagar
[03/01/24, 6:52:00 PM] Lalita Sahu: Name of Student-* Lokesh kumar
Number _6267815558
College name- bansal collage
Year-* 1st
Expected Date of Visit-*  last feb not  confirm date
[03/01/24, 6:56:47 PM] suman coding e.c: ‎This message was deleted.
[03/01/24, 6:58:32 PM] suman coding e.c: ‎This message was deleted.
[03/01/24, 7:13:26 PM] Lalita Sahu: Name of Student-*divya kumari gupta
Number _8707028681
College name- bansal collage
Year-* 1st
Expected Date of Visit-*9jan
[03/01/24, 7:14:49 PM] suman coding e.c: Name of Student: Tahir Ansari 
College name: corporate institute of science 
Contact no: 9696945415
Branch: Electrical 
Year: 
Expected Date of Visit: 26 January
[03/01/24, 7:15:17 PM] Lalita Sahu: Name of Student-*bhumika sahu
Number _6232567885
College name- bansal collage
Year-* 1st
Expected Date of Visit-*15feb
[03/01/24, 7:16:42 PM] suman coding e.c: Name of Student: Vishal 
College name: corporate institute of science 
Contact no: 8965920509
Branch: Electrical 
Year: 
Expected Date of Visit: 10 January
[03/01/24, 7:18:32 PM] suman coding e.c: Name of Student: pratham goswami 
College name: LNCT 
Contact no: 6232105580
Branch: computer science 
Year: 
Expected Date of Visit: 1 March
[04/01/24, 12:09:40 PM] anchal e.c: Name of Student: Monika sahu 
College name: SAM college 
Contact no: 8269754947
Branch: BCA
Expected Date of Visit: 4,5 January
[04/01/24, 12:25:32 PM] anup kumar ct: Name of Student: Yash
College name: SIRT
Contact no: 7224033426
Branch: CSE
Year: 3RD
Expected Date of Visit: last Fab
[04/01/24, 12:26:52 PM] anup kumar ct: Name of Student: Sneha
College name: Oriental 
Contact no: 9343944598
Branch: CSE
Year: 3RD
Expected Date of Visit: 18 Jan
[04/01/24, 12:28:44 PM] anup kumar ct: ‎This message was deleted.
[04/01/24, 12:31:12 PM] anup kumar ct: Name of Student: Pushpak 
College name: SIRT
Contact no: 7070639806
Branch: CSE
Year: 3RD
Expected Date of Visit: 8 Jan
[04/01/24, 12:40:07 PM] kasim k: 4th year
Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
BISEN ADITYA SUDHIRRAO	8485865900	
 jan 16
[04/01/24, 12:48:10 PM] anchal e.c: 3rd year 
Computer Science & Engineering	IES's College of Technology	
ABHAY PATEL
	9131873448	
Date-	7,8 January
[04/01/24, 12:49:05 PM] arpana e.c: Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	ADITI PATHAK	8103708028	
3rd year
will think
[04/01/24, 12:51:55 PM] Lalita Sahu: ‎This message was deleted.
[04/01/24, 12:52:01 PM] anup kumar ct: Name of Student: Vijay 
College name: Vaishnavi 
Contact no: 8103712693
Branch: CSE
Year: 3RD
Expected Date of Visit: 15 Jan
[04/01/24, 12:52:27 PM] anup kumar ct: Name of Student: Devansh 
College name: Oriental 
Contact no: 7999083608
Branch: CSE
Year: 3RD
Expected Date of Visit: will call
[04/01/24, 12:53:26 PM] Lalita Sahu: Name of Student: monu ahirwar
College name: bansal collage
Contact no: 9685639613

Year: 1st
Expected Date of Visit: 10jan
[04/01/24, 1:02:38 PM] khushi e.c: Name of Student-* Poonam meher 
Number - 9165531282
College name- J.N. College of Technology
Branch- Electronics & Communication Engineering
Year-* 2nd year 
Expected Date of Visit-* after 10 Feb
[04/01/24, 1:03:40 PM] annu❤️: KRASHAN GOPAL YADAV	
7489198676	
After exam 	In February 
1st year
[04/01/24, 1:28:03 PM] anup kumar ct: Name of Student: Disha
College name: Bansal 
Contact no: 9294812569
Branch: CSE
Year: 3RD
Expected Date of Visit: 10 Jan
[04/01/24, 1:34:08 PM] khushi e.c: Name of Student-* shushila Kumari 
Number -  9508407186
College name- J.N. College of Technology
Branch- Electronics & Communication Engineering
Year-* 2 nd year 
Expected Date of Visit-*. 2 nd Jan
[04/01/24, 1:52:20 PM] naresh e.c: Name :- shubham morghade 
Number: - 8253050460
College: - TIT
Branch :- cse
Expected date of visit: - 5 jan
[04/01/24, 1:58:15 PM] anup kumar ct: Name of Student: Sagar with friends 
College name: Bansal 
Contact no: 9993679315
Branch: CSE
Year: 3RD
Expected Date of Visit: 10 Jan
[04/01/24, 2:03:01 PM] kp sir: Hafsa final year ke data par not answered bahut hai uspar karoo
[04/01/24, 2:27:09 PM] kp sir: Data dediyaa hai
[04/01/24, 2:27:12 PM] kp sir: Hfsaa
[04/01/24, 2:27:16 PM] kp sir: And anchal
[04/01/24, 2:40:21 PM] anchal e.c: Ok sir
[04/01/24, 2:43:46 PM] Hafsa.: Okh Sir
[04/01/24, 2:58:34 PM] anchal e.c: 3rd year
Electrical & Electronics Engineering	
Technocrat Institute of Technology	
HRITIK KUMAR BURMAN	9334105774	
Date - will think not confirm date
[04/01/24, 2:59:52 PM] suman coding: ‎Neha mam e.c added suman coding
[04/01/24, 3:04:23 PM] annu❤️: PRASHANT KUSHWAH
9755817190	
Will Come Cc++	
28 January
1st year
[04/01/24, 3:04:29 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	NANDANI CHAUDHARI	9329373859
3rd year
old prospect
	will come 6jan
[04/01/24, 3:11:02 PM] anchal e.c: 3rd year 
Electrical & Electronics Engineering	
Technocrat Institute of Technology	
MANI KUMAR
	9431888715		
Date - 5,6 January
[04/01/24, 3:11:08 PM] suman coding e.c: ‎Neha mam e.c removed suman coding e.c
[04/01/24, 3:11:56 PM] Deepali E.C: ‎Neha mam e.c removed Deepali E.C
[04/01/24, 3:20:47 PM] kp sir: Lalita and Durga apkoo data dediyaa hai
[04/01/24, 3:21:01 PM] khushi e.c: Ok sir
[04/01/24, 3:23:46 PM] anup kumar ct: Name of Student: Amit
College name: TIT
Contact no: 9128793926
Branch: CSE
Year: 3RD
Expected Date of Visit: 4 Jan
[04/01/24, 3:26:42 PM] arpana e.c: Name of Student: Arjun
College name: IES college
Contact no: 8809419491
Branch: CSE
Year: 3RD
Expected Date of will come 4 jan today
[04/01/24, 3:27:29 PM] naresh e.c: Name :- Vishal Namdev 
College: - Tit 
Branch :- cse 
Number: - 7879627296
Expected date of visit :- 7 jan
[04/01/24, 3:29:01 PM] annu❤️: RAMMILAN LODHI
7723929323	
Will Come 	After exam 
In February 
1st year
[04/01/24, 3:37:42 PM] anchal e.c: 3rd year
Electrical & Electronics Engineering	
Technocrat Institute of Technology	MANISH KUMAR	7091681573		
     Date -will think
[04/01/24, 3:41:03 PM] kp sir: Lalita adpke pass 3 rd year ka data Phalee se hai
[04/01/24, 3:41:06 PM] kp sir: Check karee
[04/01/24, 3:41:51 PM] Lalita Sahu: Ok
[04/01/24, 3:44:45 PM] annu❤️: RISHABHDEV SINGH
6262702807	
Will Come Java 	
Chetak 
10 January 
1st year
[04/01/24, 3:45:21 PM] naresh e.c: Name :- Sanjay gour 
Number: - 9302154010
College: - Truba 
Branch :- Cse 
Expected date of visit :- 8 jan Indrapuri
[04/01/24, 3:48:26 PM] kp sir: Suman data allot kardiyaa hai pls check
[04/01/24, 3:49:09 PM] suman coding: Okay sir
[04/01/24, 4:02:22 PM] arpana e.c: Bansal Institute of Research, Technology & Science	VINEET KUMAR DHURWEY	8103192127
2nd year 
will come 9jan
old prospect
[04/01/24, 4:10:32 PM] khushi e.c: Name of Student-*. Shubham  Kumar 
Number -  9905643880
College name- Lakshmi Narain College of Technology
Branch-  Electronics & Communication Engineering
Year-* 4 th year
Expected Date of Visit-*. After 12 Jan
[04/01/24, 4:16:00 PM] kasim k: 3rd year
EC
Patel College of Science & Technology,Bhopal	
ABHISHEK SINGH	
9131890800	
5Jan
[04/01/24, 5:03:16 PM] arpana e.c: with 2 frinds
[04/01/24, 5:19:41 PM] arpana e.c: Name of Student: pankaj
College name: radha raman college
Contact num 6205562007
Branch: CSE
Year: 3RD
Expected Date of will come 4 jan today
[04/01/24, 5:24:17 PM] Hafsa.: Name of Student: Pandav Kumar 
College name: TIT
Contact no: 6205665755
Branch: EE
Year: 3rd Yr
Expected Date of Visit: Will contact after 15 Jan
[04/01/24, 5:53:08 PM] anchal e.c: 1st year 
Computer Science & Engineering	
Bansal Institute of Research, Technology & Science	
PRIYANSHU GOSWAMI	6264664290			
Date _ 5,6 January
[04/01/24, 5:53:31 PM] anchal e.c: With frd Monika parmar
[04/01/24, 6:12:57 PM] naresh e.c: Name :- paritosh 
College: - Radharaman
Branch :- cse
Number: - 9993523530
Expected date of visit: - 8 jan
[04/01/24, 6:13:48 PM] anchal e.c: 3rd year
	Electrical & Electronics Engineering	
Technocrat Institute of Technology	AKASH KUMAR SHARMA	9060905213		
Date_will think
‎[04/01/24, 6:15:19 PM] naresh e.c: Python Webdevleopment.pdf • ‎2 pages ‎document omitted
‎[04/01/24, 6:16:00 PM] naresh e.c: Fullstack Webdevelopment with MERN.pdf • ‎2 pages ‎document omitted
‎[04/01/24, 6:16:16 PM] naresh e.c: java fullstack springboot.pdf • ‎2 pages ‎document omitted
‎[04/01/24, 6:17:00 PM] naresh e.c: Data  Science.pdf • ‎2 pages ‎document omitted
[04/01/24, 6:18:17 PM] Hafsa.: Name of Student: Sakshi Nema
College name: TIT
Contact no: 7879894284
Branch: AI/DS
Year: 3rd Yr
Expected Date of Visit: 4 Jan
[04/01/24, 6:19:42 PM] suman coding: Name of Student: Sunil ahirwar 
College name: BTIRT SAGAR 
Contact no: 7869508489
Branch: Btech 
Year: 2 year
Expected Date of Visit: 8 January
[04/01/24, 6:22:24 PM] suman coding: Name of Student: lokesh 
College name: OIST college 
Contact no: 9098923370
Branch: MCA 
Year: 1 year 
Expected Date of Visit: 13 February
[04/01/24, 6:23:32 PM] anchal e.c: 3rd year
Electrical & Electronics Engineering	
Technocrat Institute of Technology	
AKASH KUMAR MISHRA	8002709844		
Date - 12 January
[04/01/24, 6:23:49 PM] suman coding: Name of Student: tarun 
College name: OIST college 
Contact no: 9340647774
Branch: MCA 
Year: 1 year 
Expected Date of Visit: 13 February
[04/01/24, 6:24:56 PM] suman coding: Name of Student: shiv
College name: OIST college 
Contact no: 9630461405
Branch: MCA 
Year: 1 year 
Expected Date of Visit: 13 February
[04/01/24, 6:30:44 PM] Neha mam e.c: 8 vale batch ke liye kispe kitne registration hai
[04/01/24, 6:31:29 PM] Neha mam e.c: Inform karo jisse samajh aaye kaise kya hai
[04/01/24, 6:31:55 PM] ~ Deepali coding: Mera ek hai mam abhi to
[04/01/24, 6:32:28 PM] Neha mam e.c: Baki
[04/01/24, 6:32:39 PM] Neha mam e.c: Dekhakar ignore nahi karna hai
[04/01/24, 6:32:45 PM] Neha mam e.c: Answer do
[04/01/24, 6:33:06 PM] Hafsa.: FSD nhi DS Python k h madam
[04/01/24, 6:33:21 PM] anchal e.c: Mera data science me hai ek
[04/01/24, 6:33:21 PM] Neha mam e.c: Kitne
[04/01/24, 6:33:25 PM] arpana e.c: mre 2 h ..    fsd me but cnfirm ni
[04/01/24, 6:34:09 PM] Hafsa.: 2-3 h madam 
Abhi ek ki enquiry chal rhi
[04/01/24, 6:34:38 PM] Neha mam e.c: Acha
[04/01/24, 6:35:11 PM] Hafsa.: Yes madam
[04/01/24, 6:36:01 PM] naresh e.c: Ek hai mam ds ke liye
[04/01/24, 6:36:37 PM] annu❤️: Mera ek hai data science ke liye
[04/01/24, 6:36:42 PM] anup kumar ct: 1 Hai mam
[04/01/24, 6:37:21 PM] Neha mam e.c: Ds ke hai sabke to registration karvao jisse batch banae
[04/01/24, 6:38:46 PM] Neha mam e.c: 8 ke Fsd ke batch me at least sabko 3-3 karane hai
[04/01/24, 6:39:17 PM] Neha mam e.c: @917805090105 @919424704675  performance bahut kharab chal raha hai
[04/01/24, 7:20:41 PM] ~ Chauhan Shilpa: Ek h mam hamara
[05/01/24, 11:38:24 AM] ~ Deepali coding: Name of Student: Yash tiwari
College name: Jnct
Contact no: 8103356759
Branch: Ec
Year: 3rd Yr
Expected Date of Visit: 8-10 January
[05/01/24, 11:40:05 AM] ~ Deepali coding: Name of Student: Chandrabhan jhapate
College name: SIRT
Contact no: 7722898598
Branch: ec
Year: 3rd Yr
Expected Date of Visit: 15 January
[05/01/24, 11:40:13 AM] khushi e.c: Sir data send kr dijiye
[05/01/24, 11:41:03 AM] kasim k: 2nd year
IES	
BE	
PRADEEP NIGAM	
8305729451	
c,c++	9Jan
chetak
[05/01/24, 12:58:55 PM] arpana e.c: Lakshmi Narain College of Technology	PRAGYA JAIN	9691599537	
3rd year
will come 25 jan
[05/01/24, 1:00:54 PM] anchal e.c: Coming today indrapuri
[05/01/24, 1:27:57 PM] kasim k: 3rd year
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
NILESH KHODIYAR	
7979098614	
22 Jan chetak
[05/01/24, 1:39:29 PM] kasim k: 3rd year
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
PRADEEP KUMAR SAFI	
9102766295	
coming today ( indrpuri)
[05/01/24, 1:55:29 PM] anup kumar ct: Name of Student: Sachin chouhan 
College name: TIT
Contact no: 6386533538
Branch: CSE
Year: 3RD
Expected Date of Visit: 5 Jan
[05/01/24, 1:59:02 PM] anchal e.c: 3rd year 
Computer Science & Engineering	Mittal Institute of Technology
	AMAN KUMAR	
6392431070			
 Date _8,9 January
[05/01/24, 2:01:27 PM] kasim k: 3rd year
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
PRINCE KUMAR	
8340424012	
11Jan
[05/01/24, 2:31:45 PM] naresh e.c: Name :- Pranay kumar 
Number: - 8709328565
College: - radharaman 
Branch :- cse 
Expected date of visit: - 8 jan
[05/01/24, 2:51:49 PM] arpana e.c: coming today with frind manish akash
[05/01/24, 3:04:33 PM] Lalita Sahu: ‎This message was deleted.
[05/01/24, 3:09:37 PM] naresh e.c: Name :- Tabrez Quraishi
Number: - 9661696995
College: - radharaman 
Branch :- cse 
Expected date of visit: - 7 jan
[05/01/24, 3:16:29 PM] anup kumar ct: Name of Student: Sandeep Kumar 
College name: TIT
Contact no: 6205371531
Branch: CSE
Year: 3RD
Expected Date of Visit: 6 Jan
[05/01/24, 3:18:06 PM] anchal e.c: 3rd year
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology	VISHAL KUMAR SINGH	9576430445		
Date _will think
[05/01/24, 3:36:39 PM] anchal e.c: 3rd year 
	Information Technology	Lakshmi Narain College of Technology	
DIVYANSH AGRAWAL	
9179838302		
Date_	after 10 jan
[05/01/24, 3:39:56 PM] naresh e.c: Name :- Ankush Verma 
Number: - 8109938764
College :-  radharaman 
Branch :-  cse 
Expected date of visit: - 10 jan
[05/01/24, 3:40:05 PM] ~ Deepali coding: Name of Student: Mohit giri 
College name: oriental 
Contact no: 7999572194
Branch:It
Year: 3RD
Expected Date of Visit: 8 Jan chetak
[05/01/24, 3:40:51 PM] ~ Deepali coding: Name of Student: Manish rai
College name: oriental 
Contact no: 8127567968
Branch:It
Year: 3RD
Expected Date of Visit: after 15 Jan indrapuri
[05/01/24, 3:48:19 PM] Lalita Sahu: Name :- anish kumar
Number: - 9110073368
College: - Sagar Institute of Research & Technology
Branch :- Electrical & Electronics Engineering
Year 3rd
Expected date of visit: - 13 jan
[05/01/24, 3:49:49 PM] Lalita Sahu: Name :- swapnil kuswaha
Number: - 9407569010
College: - Sagar Institute of Research & Technology
Branch :- Electrical & Electronics Engineering
Year 3rd
Expected date of visit: - 6january
[05/01/24, 4:14:44 PM] kasim k: 3rd year
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
SHAHEED ANVAR ANSARI	8269884282	
8Jan
[05/01/24, 4:46:11 PM] Lalita Sahu: Name :- uddhav chatap
Number: - 9752424972
College: - Sagar Institute of Research & Technology
Branch :- Electrical & Electronics Engineering
Year 3rd
Expected date of visit: - 8january
[05/01/24, 5:08:15 PM] ~ Chauhan Shilpa: Name :-
HARSH KAROLE
Number: - 8109010985
College: -Oriental Institute of Science & Technology
Branch :-  Oriental Institute of Science & Technology
Year 3rd
Expected date of visit: -last january 29
[05/01/24, 5:46:15 PM] annu❤️: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
ANAMIKA RAI	7803849525	
In February Inform himself 
3rd year
[05/01/24, 5:55:31 PM] anchal e.c: 3rd year
Computer Science & Engineering	
IES's College of Technology	
MOHIT PATWA
	7974111161	
 	20 jan
[05/01/24, 6:23:34 PM] arpana e.c: Lakshmi Narain College of Technology	SHOBHIT PATEL	9131360181
3dr year
	will come 25jan
[05/01/24, 6:42:09 PM] ~ Deepali coding: Name of Student: Ravi shankar
College name: oriental 
Contact no: 9608999650
Branch:cs
Year: 3RD
Expected Date of Visit: 10 Jan indrapuri
[05/01/24, 6:49:06 PM] kasim k: 3rd year
Computer Science & Engineering	
Vaishnavi Inst. of Tech. & Science	
MUNESH KALESH
6354311184	
7jan ⭐️
[05/01/24, 6:55:21 PM] ~ Deepali coding: Name of Student: Roli thakur 
College name: oriental 
Contact no: 9301706234
Branch:cs
Year: 3RD
Expected Date of Visit: will come feb mid
[05/01/24, 7:01:31 PM] anchal e.c: 3rd year 
Computer Science & Information 
Technology	Sagar Institute of Research & Technology	
HAMZA MANSOOR	9171168254		
Date _ 7 January
[05/01/24, 7:03:47 PM] ~ Chauhan Shilpa: Name of Student: OJASWA YADAV
College name: oriental 
Contact no: 9399978121
Branch:Information Technology
Year: 3RD
Expected Date of Visit: will come feb month
[05/01/24, 7:14:22 PM] naresh e.c: Name :- istak  Alam 
Number: - 9939485403
College: - Cist 
Branch :- cse
Expected date of visit :- 25 jan Indrapuri
[05/01/24, 7:20:30 PM] anup kumar ct: Name of Student: Shanu
College name: TIT
Contact no: 9516694542
Branch: CSE
Year: 3RD
Expected Date of Visit: 17 Jan
[05/01/24, 7:21:25 PM] anup kumar ct: Name of Student: Sudama 
College name: TIT
Contact no: 8461873234
Branch: CSE
Year: 3RD
Expected Date of Visit: 8 Jan
[05/01/24, 7:22:02 PM] ~ Deepali coding: Name of Student: Anisha kumari
College name: oist
Contact no: 8226967688
Branch:Ec
Year: 4th year
Expected Date of Visit: will come after 15 January
[05/01/24, 7:22:11 PM] anup kumar ct: Name of Student: Vineet 
College name: TIT
Contact no: 9098288990
Branch: CSE
Year: 3RD
Expected Date of Visit: 6 Jan
[05/01/24, 7:23:12 PM] anup kumar ct: Name of Student: Yogendra 
College name: TIT
Contact no: 9755115719
Branch: CSE
Year: 3RD
Expected Date of Visit: 18 Jan
[05/01/24, 7:42:39 PM] anchal e.c: Today present
05 January
Deepali
Anchal
Arpna
Kasim
Anup
Naresh
[05/01/24, 7:42:47 PM] anchal e.c: Anushree
[06/01/24, 11:47:41 AM] Lalita Sahu: Sir data ni h mere pass
[06/01/24, 12:33:49 PM] anchal e.c: 2rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning
	Technocrats Institute of Technology [Excellence]	SAKSHI DANDHARE	9340110645		
Date -after 10 January 
old prospect
[06/01/24, 12:43:51 PM] annu❤️: Electronics & Communication Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
VINDHYA KEWAT
6267518758
Old prospect
2nd year
[06/01/24, 12:48:21 PM] ~ Chauhan Shilpa: Name of Student SAMIUDDIN AHMAD
College name: Radha Raman Institute of Technology & Science
Contact no: 6206626277
Branch:Electrical & Electronics Engineering
Year: 3RD
Expected Date of Visit: after exam
[06/01/24, 12:54:25 PM] Lalita Sahu: Name of Student: rahul patle
College name: Bhopal Institute of Technology, Bangrasia
Contact no: 8770105145
Branch:Information Technology
Year:4th
Expected Date of Visit: visit last January not a confirm date
[06/01/24, 12:58:19 PM] ~ Deepali coding: Name of Student: Sumit singh
College name: oriental 
Contact no 9628422298
Branch:cs
Year:3rd year
Expected Date of Visit: will come 10 January indrapuri
[06/01/24, 1:05:10 PM] anchal e.c: 3rd year 
Information 
Technology	Oriental Institute of Science & Technology	
ANKIT TRIPATHI
	9696674754	
Date _ 	after 14 January 
Old prospect
[06/01/24, 1:08:29 PM] naresh e.c: Name :- md adil 
Number: - 7667012286
College: - cist
Branch :- cse 
Expected date of visit :- 8 jan
[06/01/24, 1:17:11 PM] naresh e.c: Name :- Niraj kumar 
Number: - 8789868417
College: - cist 
Branch: - cse
Expected date of visit :- 17 jan
[06/01/24, 1:23:30 PM] anchal e.c: 3rd year 
Computer Science & Engineering
	Vaishnavi Inst. of Tech. & Science	
GOURAV	
7748052551
Date _ not confirm date to visit  			
Old prospect
[06/01/24, 1:59:49 PM] naresh e.c: Name :- Abhay Rajput 
Number: - 8349581143
College: - sirt 
Branch :- cse 
Expected date of visit :- 6 jan Indrapuri
[06/01/24, 2:55:46 PM] annu❤️: Lakshmi Narain College of Technology	
HARSH SONI
9340507229
Old prospect
MCA 
Will come 14 January
[06/01/24, 3:30:35 PM] ~ Chauhan Shilpa: Name of Student: VIKASH SHARMA
College name: Technocrat Institute of Technology
Contact no 7320001729
Branch:Computer Science & Engineering-Data Science
Year:2 nd year
Expected Date of Visit :- 15 se 20 January
[06/01/24, 3:32:27 PM] ~ Chauhan Shilpa: Name of Student: SONU GANGWAR
College name: Technocrat Institute of Technology
Contact no :-7668056325
Branch:Computer Science & Engineering-Data Science
Year:2 nd year
Expected Date of Visit :- after exam February
[06/01/24, 3:32:33 PM] annu❤️: Lakshmi Narain College of Technology	
KHUSHI NAGAR
9926959038	
Cloud Basic 	inform himself 
MCA indrapuri
[06/01/24, 4:25:58 PM] Hafsa.: Name of Student: Rameshwar Verma + friend (Roshan)
College name: TIT
Contact no: 9369311782
Branch: CS /AI/ML
Year: 3rd Yr
Expected Date of Visit: After  4 Feb ‎<This message was edited>
[06/01/24, 4:32:48 PM] naresh e.c: Name :- Monu bhuriya 
Number: - 7828033543
College: - nri 
Branch :- ee
Expected date of visit: - 12 jan
[06/01/24, 5:26:23 PM] ~ Deepali coding: Name of Student: Akshat shrivastava
College name: Lnct
Contact no 6232952346
Branch:cs
Year:3rd year
Expected Date of Visit: will come Feb start
[06/01/24, 5:27:08 PM] ~ Deepali coding: Name of Student:Aryan jain
College name: Lnct
Contact no 8827521779
Branch:cs
Year:3rd year
Expected Date of Visit: will come Feb start with friends
[06/01/24, 5:28:46 PM] ~ Deepali coding: Name of Student:Arshad rahman
College name: Lnct
Contact no 8279388752
Branch:cs
Year:3rd year
Expected Date of Visit: will come After 20 January
[06/01/24, 5:29:40 PM] ~ Deepali coding: Name of Student:Aryan Tiwari
College name: Lnct
Contact no 8962957975
Branch:cs
Year:3rd year
Expected Date of Visit: will come 07January
[06/01/24, 5:46:32 PM] anchal e.c: 3rd year
Computer Science & Engineering	
Millennium Institute of Technology & Science	
JAYA KUSHWAHA	9098162879	
Date _will think not confirm date
[06/01/24, 6:00:16 PM] annu❤️: Lakshmi Narain College of Technology
NAMANDEEP SINGH	9109848958	
Will Come 	inform himself
In February 
MCA
[06/01/24, 6:08:22 PM] annu❤️: Lakshmi Narain College of Technology	
SONALI MANEKAR
8827168679	Will Come Java 	
10 January
MCA
[06/01/24, 6:09:07 PM] annu❤️: +1 friend shivangani
[06/01/24, 6:11:25 PM] kasim k: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence	
ARUN KHATARKAR	
8770839778		
9jan indrpuri
[06/01/24, 6:27:39 PM] kasim k: 3rd year
Computer Science & Engineering	
J.N. College of Technology	
ARCHITA SWAMI	
7049070635	
feb 1week indrpuri
[06/01/24, 6:28:42 PM] annu❤️: Lakshmi Narain College of Technology	
NIKITA UPHAR	
9006975257	
Will Come 	9 January
Indrapuri
MCA
[06/01/24, 6:33:32 PM] naresh e.c: Name :- Hariom kalmodiya 
Number: - 8120066351
College: - sirt 
Branch :- ee
Expected date of visit :- 20 jan
[06/01/24, 6:35:24 PM] anchal e.c: 3rd year 
Computer Science & Engineering	
Scope College of Engineering	
MOHIT THAKUR
	7354791678
Date - 7 January 
old prospect
[06/01/24, 6:40:57 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	NIKHAL BHADORIA	7987673227	
3rd year
will come 7 jan
[06/01/24, 6:48:37 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	NITESH KUMAR	7479442509
2nd year
	will come 12jan
[06/01/24, 7:06:19 PM] Hafsa.: Name of Student: Namrata Vishwakarma 
College name: TIT
Contact no: 9369311782
Branch: MCA
Year: 
Expected Date of Visit: Will come after 10 Jan
[06/01/24, 7:07:40 PM] Hafsa.: Name of Student: Satyanshu
College name: TIT
Contact no: 9770163100
Branch: MCA
Year: 
Expected Date of Visit: Will come after Sankranti
[06/01/24, 7:18:33 PM] annu❤️: Lakshmi Narain College of Technology	
ISHANK NAMDEO
8770331284	
Will Come 	inform himself
MCA with friends
[07/01/24, 12:23:27 PM] naresh e.c: Coming today
[07/01/24, 12:24:01 PM] annu❤️: Will come with friend Nihal
[07/01/24, 12:26:18 PM] annu❤️: Coming today indrapuri
[07/01/24, 12:35:12 PM] annu❤️: +1 friend Yash ,  Coming today indrapuri
[07/01/24, 12:35:31 PM] naresh e.c: Name :- Rajababu yadav 
Number: - 7489517049
College: - bits 
Branch :- cse
Expected date of visit :- Indrapuri 7 jan
[07/01/24, 12:40:38 PM] kasim k: 3rd year
Computer Science & Engineering	
J.N. College of Technology	
MISBAHUDDIN	
9337707273	
9Jan
[07/01/24, 12:42:39 PM] naresh e.c: Name :- umakant mishra 
Number: - 6376744802
College: - bits 
Branch :- cse 
Expected date of visit: - 8 jan Indrapuri
[07/01/24, 12:48:47 PM] naresh e.c: Name :- vishal panchal 
Number: - 7697017264
College: - bits 
Branch :- cse 
Expected date of visit: -  10 jan Indrapuri
[07/01/24, 12:56:48 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	SACHIN MEWADA	9131789037	
3rd year
will come 8 jan
[07/01/24, 1:22:42 PM] Hafsa.: Name of Student: Pooja Verma 
College name: OIST
Contact no: 7879251391
Branch: MCA
Year: 
Expected Date of Visit: Will come in 2-3 days
[07/01/24, 1:47:13 PM] annu❤️: Computer Science & Engineering	
Sha-Shib College of Technology	
ANUP KUMAR SAHU
7328022155	
Will Come 	inform himself
 3rd year
[07/01/24, 3:06:14 PM] anchal e.c: 3rd year 
Computer Science & Information Technology	
Sagar Institute of Research & Technology	
NITESH GOUR	
9399201945	
	Date _February 	not confirmed date
[07/01/24, 3:07:54 PM] Hafsa.: Name of Student: Narayan Kumar Mishra
College name: BIRT
Contact no: 6265970134
Branch: CS
Year: 2nd Yr old prospect 
Expected Date of Visit: 11 Jan ‎<This message was edited>
[07/01/24, 3:08:04 PM] arpana e.c: IES's College of Technology	ANOOP MISHRA
	6232554783
3rd year
	will come jan last
[07/01/24, 3:45:57 PM] annu❤️: Computer Science & Engineering-Data Science	
Lakshmi Narain College of Technology Excellence	
VIRAT RAGHUWANSHI	
9111693844	
Will Come 	20 January
3rd Year
[07/01/24, 3:59:57 PM] annu❤️: Electrical & Electronics Engineering	
Radharaman Engineering College	VISHAL GURJAR	
7489239055	
Call back 	15 January
After exam 
3rd Year
[07/01/24, 4:03:43 PM] Hafsa.: Name of Student: Vivek Mishra 
College name: OCT
Contact no: 7987480343
Branch: CS
Year: 2nd Yr old prospect 
Expected Date of Visit: After 15 Jan
[07/01/24, 4:48:56 PM] naresh e.c: Name:- prahlad kurmi 
Branch :-ec 
Number: - 9244366596
Expected date of visit: - 26 jan
[07/01/24, 5:11:40 PM] Hafsa.: Name of Student: Pavitra Gupta 
College name: LNCT
Contact no: 7068643951
Branch: AI/ML
Year: 2nd Yr old prospect 
Expected Date of Visit: After 15 Jan
‎[07/01/24, 5:34:56 PM] Neha mam e.c: ‎image omitted
‎[07/01/24, 5:34:56 PM] Neha mam e.c: ‎image omitted
‎[07/01/24, 5:34:56 PM] Neha mam e.c: ‎image omitted
‎[07/01/24, 5:34:57 PM] Neha mam e.c: ‎image omitted
[07/01/24, 5:46:58 PM] Hafsa.: Name of Student: Shahid Khan 
College name: NRI
Contact no: 6262144030
Branch: CS
Year: 1nd Yr old prospect 
Expected Date of Visit: After exam in Feb
‎[07/01/24, 6:21:27 PM] Neha mam e.c: ‎image omitted
[07/01/24, 6:23:16 PM] Hafsa.: Name of Student: Harsh Nagle 
College name: Truba College
Contact no: 8817024903 
Branch: AI/DS
Year: 3rd Yr 
Expected Date of Visit: Will tell in 1-2 days
[07/01/24, 6:46:42 PM] ~ Deepali coding: Mam webkorps me hua hai ?
[07/01/24, 6:47:17 PM] Neha mam e.c: No
[07/01/24, 6:47:43 PM] ~ Deepali coding: Yaha galat dal diya hai
[07/01/24, 6:47:51 PM] Neha mam e.c: Ok
[07/01/24, 6:58:32 PM] naresh e.c: Name :- Vijay purvare 
Number: - 8435041035
College: - Sam 
Branch :- aids 
Expected date of visit :- 10 jan
‎[07/01/24, 7:08:07 PM] Neha mam e.c: ‎image omitted
[07/01/24, 7:27:03 PM] anup kumar ct: Name of Student: Abhishek 
College name: VNS
Contact no: 7509306976
Branch: EEE
Year: 3RD
Expected Date of Visit: After 15 Jan
[07/01/24, 7:27:49 PM] anup kumar ct: Name of Student: Krishnan 
College name: VNS
Contact no: 9285155809
Branch: EEE
Year: 3RD
Expected Date of Visit: 10 Jan
[07/01/24, 7:28:37 PM] anup kumar ct: Name of Student: Sonu
College name: VNS
Contact no: 7723829675
Branch: EEE
Year: 3RD
Expected Date of Visit:  12 Jan
[07/01/24, 7:29:46 PM] anup kumar ct: Name of Student: Aaryan 
College name: NRI
Contact no: 9301330510
Branch: CSE
Year: 3RD
Expected Date of Visit:  15 Jan
[07/01/24, 7:30:17 PM] anup kumar ct: Name of Student: Abhishek 
College name: NRI
Contact no: 7654296613
Branch: CSE
Year: 3RD
Expected Date of Visit:  15 Jan
[07/01/24, 7:34:43 PM] ~ Chauhan Shilpa: Name of Student: RITIK RAJ RANJAN
College name: Technocrat Institute of Technology
Contact no: 8102410592
Branch: Computer Science & Engineering-Data Science
Year: 2 nd
Expected Date of Visit: After 15 Jan
[07/01/24, 7:36:19 PM] ~ Chauhan Shilpa: Name of Student: 
College name: Technocrat Institute of Technology
Contact no: 8227884430
Branch: Computer Science & Engineering-Data Science
Year: 2 nd
Expected Date of Visit: after exam
[07/01/24, 7:37:33 PM] ~ Chauhan Shilpa: Name of Student: VIVEK KUMAR SHAH
College name: Technocrat Institute of Technology
Contact no: 7879355368
Branch: Computer Science & Engineering-Data Science
Year: 2 nd
Expected Date of Visit: After 10 Jan
[07/01/24, 7:38:42 PM] ~ Chauhan Shilpa: Name of Student: RAJ CHOUDHARY
College name: Technocrat Institute of Technology
Contact no: 9691483287
Branch: Computer Science & Engineering-Data Science
Year: 2 nd
Expected Date of Visit: After 10 February ke baad
[07/01/24, 7:40:07 PM] kp sir: Dear Students,

Coding Thinker starts a New Placement Oriented Batch from *8th jan 2024* @ Mpnagar branch 
and in *indrapuri* @ *13Jan 2024* 

Course Name: 
1) Full stack Developmentwith MERN - Placement Oriented Batch
2) Data Science with Python- Placement Oriented Batch
3) Data Analytics 
4) Python webdevelopment 
5) java full stack webdevelopment 
Choose Any Batch as per your interest

 Mode: OFFLINE

Faculty: IT-professional / Industry Experts from Top MNCs


 *Office* *Address* :- LALWANI COMPLEX NEAR CHETAK BRIDGE MP NAGAR *ZONE 1, BHOPAL

87 C sector indrapuri* , Above Chai suttabar 

Regards
Coding Thinker
9131608639
[07/01/24, 7:40:27 PM] kp sir: Sabhi log apne prospects ko yeah message share karee
[08/01/24, 12:26:54 PM] ~ Chauhan Shilpa: Name of Student: DHARMENDRA KUMAR CHAUDHARY
College name: Bansal Institute of Research & Technology
Contact no: 8839537226
Branch:Electronics & Communication Engineering
Year: 3ed
Expected Date of Visit: 17 January mp nagar
[08/01/24, 12:31:00 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	SHIVANKIT DUBEY
	9936394547
3rd year	will think
[08/01/24, 12:47:33 PM] anup kumar ct: come with friend Vishal today at indrapuri
[08/01/24, 1:05:16 PM] annu❤️: + 1 friend Shraddha
[08/01/24, 1:43:03 PM] naresh e.c: Name :- Aryan 
Number: - 7033177629
College: - jnct 
Branch :- aiml 
Expected date of visit :- 11 jan with frnds
[08/01/24, 1:48:03 PM] kasim k: Name :- ishan + deepak
number - 9693206681+7804845642
college - radha raman 
branch - cs
coming today + friend ( chetak)
[08/01/24, 4:57:36 PM] Neha mam e.c: Kiske kitne prospect aa raha hai admission lene mujhe personal par bhejo
[08/01/24, 6:52:35 PM] arpana e.c: Vaishnavi Inst. of Tech. & Science	RANJANA	9826077093
4th year
will come  12 jan
[08/01/24, 6:53:23 PM] arpana e.c: Bhopal Institute of Technology & Science, Bangrasia	KRISHNA KUMAR TIWARI	7354190787
4th year
will come 9 jan
[08/01/24, 7:11:13 PM] ~ Chauhan Shilpa: Name of Student: KISHAN VISHWAKARMA
College name: Bansal Institute of Research & Technology
Contact no: 8085421529
Branch:Electronics & Communication Engineering
Year: 3ed
Expected Date of Visit: 20 January ke baad January mp nagar
[08/01/24, 7:15:50 PM] kasim k: 3rd year
Computer Science & Engineering	
Vaishnavi Inst. of Tech. & Science	
SEEMA VISHWAKARMA	8305349429	
10 jan kolar
[08/01/24, 7:28:50 PM] anup kumar ct: Name of Student: Amol
College name: NRI
Contact no: 8878929466
Branch: CSE
Year: 3RD
Expected Date of Visit:  will call
[08/01/24, 7:29:34 PM] anup kumar ct: Name of Student: Jatin
College name: NRI
Contact no: 9755907588
Branch: CSE
Year: 3RD
Expected Date of Visit:  12 Jan
[09/01/24, 11:57:20 AM] Neha mam e.c: Robot ki tarah baghate ho to robot ki tarah time par sab aaya bhi karo
[09/01/24, 11:57:40 AM] Neha mam e.c: Discussion khatam hogya ho to kaam karlo
[09/01/24, 12:43:17 PM] kasim k: 3rd year
Electronics & Communication Engineering	
Oriental Institute of Science & Technology	
ARYAN KHANGAR
9302615645	
10- 12 jan  indrpuri
[09/01/24, 3:08:05 PM] ~ Chauhan Shilpa: Name of Student: TUSHAR KUMAR SRIVASTAVA
College name: IES's College of Technology
Contact no: 6387106036
Branch:Electronics & Communication Engineering
Year: 3ed
Expected Date of Visit: 15 January
[09/01/24, 3:16:56 PM] ~ Deepali coding: Name of Student: md Rashid ansari
College name: TIT
Contact no: 9122861376
Branch:cs
Year: 2nd year
Expected Date of Visit after exam
[09/01/24, 3:18:35 PM] anchal e.c: 3rd year 
Computer Science & Bussiness System	
Oriental Institute of Science & Technology	
ADITYA BATHRE
	7869202112	
	Date _after 15 January
[09/01/24, 3:41:13 PM] arpana e.c: Name of student.  Sandeep
college  name patel college
7763912480
2nd year
will come 10jan for inderpuri
[09/01/24, 3:42:40 PM] arpana e.c: name of student sharukh khan +ankit +10 frinds
patel college
8084361019
1st sem 
will come in feb after exam
[09/01/24, 3:53:10 PM] ~ Deepali coding: Will come after 25 January
[09/01/24, 4:24:50 PM] kp sir: 👍
[09/01/24, 4:35:19 PM] kasim k: 3rd year 
Computer Science & Engineering	
Vaishnavi Inst. of Tech. & Science	
SUNIL KUMAR PAL	
9060797013	 
10Jan
[09/01/24, 6:05:18 PM] kasim k: 3rd year
Computer Science & Engineering	
Scope College of Engineering
ANIKET VISHWAKARMA	7898590115	
7610183403
16 jan
[09/01/24, 6:12:51 PM] ~ Deepali coding: Name of Student: vaibhav 
College name: LNCT
Contact no: 9322209920
Branch:cs
Year: 2nd year
Expected Date of Visit 11-12 January 
+ 2 friend
[09/01/24, 6:26:11 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
SHALANI KUMARI	
8102180439
Date _ not confirm date to visit
[09/01/24, 6:46:30 PM] anchal e.c: 3rd year 
	Computer Science & Engineering	Millennium Institute of 
Technology & Science	
VIKAS TIWARI	8103785134	
Date _	20 Jan
[09/01/24, 6:46:58 PM] kasim k: 3rd year
Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
UJJWAL GUPTA	
9301250802	
23-28jan
[09/01/24, 7:12:48 PM] kasim k: 3rd year
Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
VISHAL DALAL	
7000515658	
26 January
[09/01/24, 7:22:37 PM] anup kumar ct: Name of Student: Ritik 
College name: NRI
Contact no: 8450067972
Branch: CSE
Year: 3RD
Expected Date of Visit: 13 Jan
[09/01/24, 7:24:32 PM] anup kumar ct: Name of Student: Anil
College name: SIRT
Contact no: 8959463595
Branch: CSE
Year: 3RD
Expected Date of Visit: 13 Jan
[09/01/24, 8:51:48 PM] kasim k: ‎You deleted this message.
[10/01/24, 12:49:35 PM] naresh e.c: Name :- md Nayab 
Number: - 7489181083
College: - tit
Branch :- it
Expected date of visit: - 12 jan
[10/01/24, 12:50:22 PM] Hafsa.: Name of Student: Rahul Mohite 
Contact no: 9009539595
Branch: ME
Year: PO
Expected Date of Visit: 10 Jan
[10/01/24, 12:58:26 PM] ~ Deepali coding: ‎This message was deleted.
[10/01/24, 12:59:52 PM] ~ Deepali coding: Name of Student: Ujjwal sarkar
Contact no:9981656555
Branch: cs
College -LNCT
Year: 3rd 
Expected Date of Visit: will come after 20 January
[10/01/24, 1:00:16 PM] ~ Deepali coding: Name of Student: shobhit patel
Contact no: 9131360181
Branch: cs
College Lnct
Year: 3rd 
Expected Date of Visit: 27 January
[10/01/24, 1:34:37 PM] Hafsa.: Name of Student: Simra
College name: Truba College 
Contact no: 7024431048
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  11 Jan
[10/01/24, 2:56:49 PM] naresh e.c: Name :- ravindra singh 
Number :- 6386306573
Expected date of visit :- 17 jan
[10/01/24, 3:10:38 PM] ~ Deepali coding: Name :- Nikhil kumar
Number :- 6202920945
Expected date of visit :- 11january
[10/01/24, 3:11:20 PM] ~ Deepali coding: Name :- Virendra
Number :- 8602282714
Expected date of visit :- 20 January
[10/01/24, 3:11:23 PM] anup kumar ct: Sameet Arya with jatin and Amir friends
9171623785
UIT
13 JAN
[10/01/24, 3:13:52 PM] naresh e.c: Name :- anubhav tiwari 
Number: - 9685193060
College: - Sam 
Branch :- ee 
Expected date of visit :- 14 Feb
[10/01/24, 3:16:45 PM] anchal e.c: Name _ saloni 
Number  -7879494697  
Date _ after 20 January
[10/01/24, 3:19:43 PM] Hafsa.: Name of Student: Devesh
College name: NRI 
Contact no: 9343761857
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  Will tell in 1-2 days
[10/01/24, 3:20:12 PM] arpana e.c: Name Deepak
number 8226064456
will come 17 jan
[10/01/24, 3:21:01 PM] arpana e.c: Name.  Tejesvini 
Number. 6268943843
will come 12 jan
[10/01/24, 3:27:38 PM] annu❤️: 7990081227	
Abhay Patel
Indrapuri  11 January
[10/01/24, 3:34:55 PM] anchal e.c: Name _ prakhar 
 Number _9343558630	
Date _after 14 Jan
[10/01/24, 3:36:10 PM] anchal e.c: Name _ Kundan raj
Number _7061977710	
Date_ 1	feb
[10/01/24, 3:39:38 PM] anup kumar ct: Name of Student: Sohan
College name: SIRT
Contact no: 7692968730
Branch: ECE
Year: 3RD
Expected Date of Visit: 13 Jan
[10/01/24, 3:40:36 PM] arpana e.c: Name of Student: Dhuruv chorasiya
College name: SIRT
Contact no: 8989869656
Branch: cs
Year: 3RD
Expected Date of Visit: 12 Jan
[10/01/24, 3:49:44 PM] Hafsa.: Coming at evening with 2 friends (Gautam and Rohan )
[10/01/24, 3:51:10 PM] Hafsa.: Name of Student: Mayank 
College name: IIES
Contact no: 9058707261
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  14 Jan
[10/01/24, 3:54:29 PM] ~ Chauhan Shilpa: Name of Student: OJASWA YADAV
College name: Oriental Institute of Science & Technology
Contact no: 9399978121
Branch. Information Technology
Year: 3rd Yr
Expected Date of Visit: February
[10/01/24, 3:59:32 PM] arpana e.c: ‎This message was deleted.
[10/01/24, 4:00:47 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning
	Lakshmi Narain College of Technology & Science	
HARSHITA SHARMA	
Number _9589900392	
Date_		fsd 17 January
[10/01/24, 4:01:03 PM] arpana e.c: Name of Student: Archna
College name: LNCT college
Contact no: 9302707823
Branch: ESE
Year: 3rd Year 
Expected Date of Visit:  12 Jan
[10/01/24, 4:02:06 PM] arpana e.c: Name of Student: Anjali malviya
College name: Bansal college
Contact no: 93098725263
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  14 Jan
[10/01/24, 4:05:25 PM] ~ Deepali coding: Name of Student: Sunny
College name: Bansal college
Contact no: 7049977784
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  will come after 15 January
[10/01/24, 4:05:51 PM] kasim k: Name :- manish	
number :- 9098904989		
Expected date of visit :-after 15 

Name -garvit 	
Number - 7566316097	
Expected date of visit -nxt month plan  after exam

Name - ranjeet tit	
Number -9179255738	
Date of visit -11 jan (indrpuri)

Name- nikhil	
Number - 7477007574	
Expected date of visit-coming 11/12 jan
[10/01/24, 4:06:34 PM] ~ Deepali coding: Name of Student: Sahil 
College name tit
Contact no: 9826351086
Branch: It
Year: 3rd Year 
Expected Date of Visit:  will come 12 January
[10/01/24, 4:13:47 PM] Hafsa.: Name of Student: Vijay Sharma 
College name: SISTech
Contact no: 7354178073
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  11 Jan
[10/01/24, 4:17:03 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology & Science 
	SHASWAT RAI	8542088211			
Date _after 15 January
[10/01/24, 4:34:10 PM] annu❤️: Computer Science & Engineering	
Bansal Institute of Science & Technology
AABYA RAJ
6204697488
Will Come 14 January
Old prospect
[10/01/24, 4:50:40 PM] arpana e.c: Name of student. Aman Malviya 
9098725263
bansal college 
3rd year
will come 11 jan


Name of student poonam
9977964180
NRl college 
will come 16 jan
[10/01/24, 5:18:04 PM] ~ Deepali coding: Name of Student: Mansi ohja
College name: Nri
Contact no: 7828335898
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  11 jan + friend
[10/01/24, 5:21:31 PM] anchal e.c: 2nd year
	Computer Science & Engineering-Data Science	
IES College of Technology	ANAND KUMAR	7086107670	
Date _after exam
[10/01/24, 5:35:45 PM] ~ Chauhan Shilpa: Name of Student: SAMIUDDIN AHMAD
College name Radha Raman Institute of Technology & Science
Contact no: 6206626277
Branch: Electrical & Electronics Engineering
Year:  3 ed
Expected Date of Visit:  after exam
[10/01/24, 5:42:56 PM] Hafsa.: Name of Student: Anjali Kushwaha
College name: Bansal 
Contact no: 9285548893
Branch: Civil
Year: 3rd Year 
Expected Date of Visit:  Will contact in Feb
[10/01/24, 5:51:15 PM] anup kumar ct: Name of Student: Deepak 
College name: Vaishnavi 
Contact no: 9893742602
Branch: AIML
Year: 3RD
Expected Date of Visit: 11 Jan
[10/01/24, 5:55:34 PM] kasim k: Artificial Intelligence and Machine Learning	
J.N. College of Technology	
KARDAN DWIVEDI
7395042577
coming today
[10/01/24, 6:00:05 PM] anchal e.c: BU It
GOVT. HAMIDIA ARTS AND COMMERCE COLLEGE BHOPAL
	BCOM	
AADIL HUSAIN
	8103842027		
Date_12 Jan
[10/01/24, 6:09:54 PM] Hafsa.: Name of Student: Sachin Kumar
College name: TIT
Contact no: 6202885791
Branch: EC
Year: 3rd Year 
Expected Date of Visit:  10 Jan
[10/01/24, 6:16:44 PM] kasim k: name :- dhruv agarwal
college name :- Lnct 
contact number :-6393870990

coming today for addmission
[10/01/24, 6:25:07 PM] anchal e.c: ‎This message was deleted.
[10/01/24, 6:25:51 PM] anchal e.c: MCA
Oriental Institute of Science & Technology	
AKASH SAXENA	
9144870603	
Date_	11,12 January
[10/01/24, 6:37:52 PM] anup kumar ct: Name of Student: Ravindra 
College name: Hamidia 
Contact no: 9399839185
Branch: BCOM
Year: 
Expected Date of Visit: 13 Jan
[10/01/24, 6:40:22 PM] anchal e.c: MCA
Lakshmi Narain College of Technology
	NIKHIL RAJ	
8873810528	
Date_ 11 January
[10/01/24, 6:58:30 PM] anchal e.c: Name _ Md Nabil 
Number _6201748843
Date_11 Jan
[10/01/24, 6:59:14 PM] naresh e.c: Coming today with frnd
[10/01/24, 6:59:23 PM] naresh e.c: Indrapuri
[10/01/24, 7:03:40 PM] anchal e.c: Name _ Saloni 
Number _8818942612	
Date _15 January
[10/01/24, 7:12:11 PM] anchal e.c: Name _ ritik + frds
Number _9340301590	
Date _13,14 January
[11/01/24, 12:23:51 PM] naresh e.c: Coming today Indrapuri
[11/01/24, 12:53:59 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Data Science	
Lakshmi Narain College of Technology Excellence	DEVENDRA PRATAP SINGH	number _9303510526		
Date _end of January
[11/01/24, 1:21:02 PM] arpana e.c: coming today
[11/01/24, 1:45:29 PM] naresh e.c: Name :- MOHD QAMAR ALAM siddique
Number: - 7258973501
College: - Millennium 
Branch :- ee 
Expected date of visit: -  14 jan
[11/01/24, 2:56:56 PM] Hafsa.: Name of Student: Gaurang Garg
College name: TIT
Contact no: 9752126271
Branch: EE
Year: 3rd Year 
Expected Date of Visit:  Will come after 20 Jan ( Out of station ) ‎<This message was edited>
[11/01/24, 3:10:50 PM] anchal e.c: 3rd year 
Computer Science & Engineering	Vidhyapeeth Institute of Science & Technology
	SUDHANSHU KUMAR	
7545840902	
Date _ coming today indrapuri
[11/01/24, 3:37:44 PM] anchal e.c: 2nd year
[11/01/24, 3:40:53 PM] ~ Deepali coding: Name of Student: pranjal
College name: Lnct
Contact no: 9752162686
Branch: cs
Year: 3rd Year 
Expected Date of Visit:  Will come after 12 January
[11/01/24, 3:50:05 PM] kp sir: Suman 
Durga 
Aaplog ko Data dediyaa hai
[11/01/24, 3:50:18 PM] kp sir: Pls check in 3 year sheet
[11/01/24, 4:01:44 PM] kp sir: Lalita Data allot kardiyaa hai aapkoo
[11/01/24, 4:02:23 PM] suman coding: Okay sir
[11/01/24, 4:03:49 PM] kp sir: Hafsaa aapko bhi diyaa hai
[11/01/24, 4:03:51 PM] kp sir: Data
[11/01/24, 4:04:12 PM] ~ Deepali coding: Name of Student: Saket chourasiya 
College name: Lnct
Contact no: 7879057774
Branch: cs
Year: 3rd Year 
Expected Date of Visit:  Will come start feb
[11/01/24, 4:05:30 PM] Hafsa.: Okh Sir
[11/01/24, 4:05:38 PM] khushi e.c: Ok sir
[11/01/24, 4:10:53 PM] naresh e.c: Name :- Chhotu Kumar 
Number: - 9122831785
College: - tit
Branch :- ee
Expected date of visit :- Today with frnd ankit (Indrapuri)
[11/01/24, 4:13:13 PM] khushi e.c: Name :-  Ashok kapase 
Number: -  9752252144
College: - tit
Branch :- ee
Expected date of visit :- 12 Jan   m.p nagar
[11/01/24, 4:14:42 PM] arpana e.c: Name of student  Durgesh  kumar  
9630319210
Bansal college cse
will come 15 jan
[11/01/24, 4:17:10 PM] khushi e.c: Name :-  Aniket Singh 
Number: - 9424193674
College: - sha-sahib
Branch :- cs and E
Expected date of visit :-  14 Jan in m.p nagar
[11/01/24, 4:20:34 PM] khushi e.c: Name :-  vaishnavi 
Number: 9301590048
College: -  bansal 
Branch :- cs&e
Expected date of visit :- 11feb
[11/01/24, 4:21:08 PM] Lalita Sahu: Ok sir
[11/01/24, 4:43:15 PM] arpana e.c: Oriental Institute of Science & Technology	HARSHIT SHRIVASTAVA	9479907591
3rd year
	will come 12 jan
[11/01/24, 5:24:37 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Oriental Institute of Science & Technology	S.AADVIK	
Number _9167987166	
Date _will think
[11/01/24, 5:41:45 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Oriental Institute of Science & Technology	
SAHIL DWIVEDI	
Number _8957395657	
Date _14 January
[11/01/24, 5:42:51 PM] arpana e.c: Oriental Institute of Science & Technology	KRISHNA PAL SINGH TANWAR	8319273848	
3rd year.
will come feb 5
[11/01/24, 5:44:31 PM] ~ Deepali coding: Name :- Aditya tiwari 
Number: - 9827649167
College: - tit
Branch :- cs 
Expected date of visit :- 14 January  (Indrapuri)
[11/01/24, 6:21:47 PM] Neha mam e.c: @917489380471 @916260753147 @919303330545 @916263551348 kya kar rahe ho aap log koi prospect nahi ban rahe hai aap logo ke
[11/01/24, 6:25:00 PM] arpana e.c: Sagar Institute of Science & Technology & Research	GANESH SEN	
3rd year
9893824129	
will think feb
[11/01/24, 6:26:24 PM] Lalita Sahu: Name :- ashish koche
Number: - 9977699501
College: - corporate institude of science & techology
Branch :- eletrical &electronics engineering
Year:-3rd
Expected date of visit :- 25 January
[11/01/24, 6:26:53 PM] suman coding: Name :-  ansh kushwaha 
Number: -  7974554047
College: - LNCT 
Branch :- CS 
Expected date of visit :- 25 Jan m.p nagar
[11/01/24, 6:28:16 PM] Lalita Sahu: ‎This message was deleted.
[11/01/24, 6:28:53 PM] ~ Chauhan Shilpa: Name :- ARIHANT JAIN
Number: - 6388592612
College: - Lakshmi Narain College of Technology
Branch :- Computer Science & Engineering
Year:-2 nd
Expected date of visit :- after exam
[11/01/24, 6:29:58 PM] khushi e.c: Name :-   Raj mehra 
Number: -  6261245810
College: -  bansal 
Branch :- CS &E
Expected date of visit :- 9 Feb
[11/01/24, 6:31:17 PM] ~ Chauhan Shilpa: Name :- VIKASH
Number: - 7320001729
College: - Lakshmi Narain College of Technology
Branch  
Year:-2 nd
Expected date of visit :- 20 se 25 January
[11/01/24, 6:32:42 PM] ~ Chauhan Shilpa: Name :- DEEPANSHU GUPTA
Number: - 7223916488
College: -DEEPANSHU GUPTA
Branch  Computer Science & Engineering-Data Science
Year:-2 nd
Expected date of visit :- 20 se 25 January ‎<This message was edited>
[11/01/24, 6:32:45 PM] khushi e.c: Name :-  Neha yadav 
Number: - 8305474781
College: - bansal 
Branch :- Computer Science & Engineering
Expected date of visit :-  10 Feb
[11/01/24, 6:35:49 PM] suman coding: Name :-  Praveen Kumar yadav 
Number: -  7408383390
College: - LNCT 
Branch :- CS 
Expected date of visit :- 30 January
[11/01/24, 6:37:14 PM] suman coding: Name :-  Rakesh Kumar 
Number: -  8725878289
College: - LNCT 
Branch :- CS 
Expected date of visit :- 2 February
[11/01/24, 6:38:17 PM] Lalita Sahu: Name :- nadeem khan
Number: - 7068814454
College: - laxmipati institude of science &technology
Branch :- eletrical &electronics engineering
Year:-3rd
Expected date of visit :- after 15 feb
[11/01/24, 6:46:51 PM] suman coding: Name :- santram
Number: - 8349359452
College: - oriental college of technology &technology
Branch :- electronic & communication engineering
Expected date of visit :- 14 January
[11/01/24, 7:13:06 PM] kasim k: Computer Science & Engineering-Data Science	
Oriental College of Technology
SALINI PATEL	
8109660814		
try to come today
[11/01/24, 7:23:49 PM] anup kumar ct: ‎This message was deleted.
[11/01/24, 7:24:02 PM] anup kumar ct: 2ND			Shubham chouhan 	8600270560		After 15 Feb
[11/01/24, 7:24:17 PM] anup kumar ct: ME		Sohan	6232760294	Indrapuri 	14 Jan
[11/01/24, 7:24:35 PM] anup kumar ct: 2ND			Raj 	8349789784		After 15 Feb
[11/01/24, 7:24:47 PM] anup kumar ct: 3RD	CS	TIT	Ravi Kumar 	8603317326	indrapuri 	13 Jan
[11/01/24, 7:25:06 PM] anup kumar ct: 3RD	ME	Bansal 	Yogendra Solanki 	9098275798		16 Jan
[11/01/24, 7:25:27 PM] anup kumar ct: 3RD	CSE		Imran Ali 	7783037329		12 Jan
[11/01/24, 7:25:41 PM] anup kumar ct: 3RD	CSE	Bansal 	Nitish Kumar Yadav 	8827041128		12 Jan
[12/01/24, 11:42:02 AM] Lalita Sahu: Mam me aaj thoda let aaugi
[12/01/24, 11:52:21 AM] Hafsa.: Name of Student: Ashutosh Parihar
Contact no: 8517842654
Branch: EC
Year: PO
Expected Date of Visit:  Will inform when come
[12/01/24, 11:56:12 AM] arpana e.c: Oriental Institute of Science & Technology	PRASHANT DHAKAD	9479955178	
3rd year
will think feb
[12/01/24, 12:03:50 PM] ~ Deepali coding: Name of Student: Ishan tiwari 
Contact no: 8871061187
Branch: Cs
College: Tit
Year: 3rd 
Expected Date of Visit:  Will come 12 January
[12/01/24, 12:35:13 PM] ~ Chauhan Shilpa: Name of Student: Ahmad 
Contact no: 8853896918
Branch: Cs
Year: 3rd 
Expected Date of Visit:  February mein join karenge MP Nagar mein
[12/01/24, 12:38:07 PM] kp sir: Aaj sabhi se 1-1 admission chaiyee ,dekhlooo kahaa se karaoogeee
[12/01/24, 12:38:07 PM] anchal e.c: Coming today
[12/01/24, 12:38:41 PM] Hafsa.: Will try to go today Indrapuri
[12/01/24, 12:38:51 PM] anchal e.c: Coming today
[12/01/24, 12:39:37 PM] Neha mam e.c: Aap 12 log ho 12 admission hone chaiye aaj
[12/01/24, 12:40:04 PM] Neha mam e.c: Milkar karo chaye 1-1 sab kar lo
[12/01/24, 12:40:53 PM] kp sir: Suman absent hai kya aaj 
Timing kya hai inki 12 baje main aaya Tha toh the nahi
[12/01/24, 12:41:08 PM] kp sir: Aaj leave par hai kya
[12/01/24, 12:41:21 PM] suman coding: Nhi sir
[12/01/24, 12:41:38 PM] kp sir: Timing kya hai aapki
[12/01/24, 12:41:48 PM] suman coding: 12
[12/01/24, 12:41:52 PM] khushi e.c: Name of Student:  Ayush  ojha  
Contact n :7024908277
 College : J.N. College of Technology
 Branch :Electronics & Communication Engineering
Year:  2 nd year 
Expected Date of Visit:   12 Jan evening in indrapuri
[12/01/24, 12:42:20 PM] kp sir: Timing ka Dhyan rakheee ,if have any emergency, inform to me or Director maam
[12/01/24, 12:42:38 PM] suman coding: Okay sir
[12/01/24, 12:42:53 PM] anchal e.c: Computer Science & Engineering	
Vidhyapeeth Institute of Science & Technology	
SUDHANSHU KUMAR	
7545840902	
Date _	12 January
[12/01/24, 12:48:45 PM] Lalita Sahu: Name of Student: krish sahu
Contact no: 8878467684
Branch:Artificial Intelligence and Data Science
Collaage:-Lakshmi Narain College of Technology
Year: 3rd 
Expected Date of Visit:  25january
[12/01/24, 12:57:54 PM] khushi e.c: Coming today
[12/01/24, 1:05:09 PM] Lalita Sahu: Name of Student: mayank sharma
Contact no: 7049872377
Branch:Artificial Intelligence and Data Science
Collaage:-Lakshmi Narain College of Technology
Year: 3rd 
Expected Date of Visit: after 20january
[12/01/24, 1:38:12 PM] ~ Chauhan Shilpa: Name of Student: HAMID RAJA KHAN
Contact no: 9155580494
College:-Technocrats Institute of Technology [Excellence]
Branch: Computer Science & Engineering
Year: 4 th
Expected Date of Visit:  27 January mp nagar
[12/01/24, 2:57:58 PM] kp sir: Mobile number kaha hai
[12/01/24, 3:00:41 PM] anchal e.c: 4th year 
	Computer Science & Engineering
	SAM College of Engineering & Technology	
VIVEK DHAKAD	9981574174
[12/01/24, 3:01:31 PM] anchal e.c: 4th year
Computer Science & Engineering	
SAM College of Engineering & Technology	
VIJAY KAHAR
	9981283800
[12/01/24, 3:02:49 PM] kp sir: Inke admission hogye kya final
[12/01/24, 3:05:13 PM] kp sir: Inkaa kya hua
[12/01/24, 3:06:54 PM] annu❤️: Hn ho gye the same date pr
[12/01/24, 3:25:53 PM] ~ Deepali coding: Name of Student: premlata sen
Contact no: 7470316463
Branch:Cs
Collaage:-Scope college 
Year: 3rd 
Expected Date of Visit: will come 15 January
[12/01/24, 3:33:06 PM] ~ Deepali coding: Name of Student: Raj Kumar shah
Contact no: 7828870233
Branch:Cs
Collaage:-Scope college 
Year: 3rd 
Expected Date of Visit: will come feb mid
[12/01/24, 3:36:31 PM] kp sir: Kiki main bhi mobile number nahi hai ku
[12/01/24, 3:37:50 PM] Hafsa.: 6202885791
[12/01/24, 3:43:42 PM] suman coding: Name of Student: anshul
Contact no: 8516812242
Branch: artificial intelligence and machine learning 
College: LNCT 
Year: 3rd 
Expected Date of Visit: 25 January
[12/01/24, 3:43:52 PM] khushi e.c: Name of Student:  Aditi Gupta 
Contact no:6264487092
Branch: 	Computer Science & Engineering-Artificial Intelligence and Machine Learning
Collaage:-Lakshmi Narain College of Technology
Year: 3rd 
Expected Date of Visit:  2 Feb  indrapuri sector c
[12/01/24, 3:53:23 PM] khushi e.c: ‎This message was deleted.
[12/01/24, 3:55:48 PM] Neha mam e.c: 9 digit daala hai
[12/01/24, 3:57:33 PM] khushi e.c: Ji mam correct kar rahi hu
[12/01/24, 3:59:28 PM] suman coding: Name of Student: Praveen yadav 
Contact no: 7408383390
Branch: CS 
College: LNCT 
Expected Date of Visit: 26. January
[12/01/24, 3:59:55 PM] khushi e.c: Name of Student:  Ambuj  tripathi 
Contact no: 8707888197
Branch: Computer Science & Engineering-Artificial Intelligence and Machine Learning
College: LNCT 
Year: 3rd 
Expected Date of Visit: 28January in indrapuri sector c
[12/01/24, 4:09:13 PM] kp sir: Admission chaiyee mujseee
[12/01/24, 4:09:24 PM] kp sir: 1-1 nahi toh aaj off hai
[12/01/24, 4:33:47 PM] naresh e.c: Name :- ajay singh lodhi 
Number: - 8817717164
College: - sirt 
Branch :-aids 
Expected date of visit: - 14 jan
[12/01/24, 4:36:06 PM] naresh e.c: Name :- ankit boursai 
Number: - 8103251472
College: - sirt 
Branch :- aids 
Expected date of visit :- 2 Feb
[12/01/24, 5:13:54 PM] Lalita Sahu: Name of Student: karan kumar with 2frnd
Contact no: 9608969860
College:-Trinity Institute of Technology & Research
Branch: Electronics & Communication Engineering
Year: 3rd
Expected Date of Visit:  14jan
[12/01/24, 5:38:58 PM] Neha mam e.c: Dekhlo sabhi log admission chaiye aaj
[12/01/24, 6:02:25 PM] naresh e.c: Name :- ritik Rajput 
Number: - 9301870529
College: - sirt 
Branch :- aids 
Expected date of visit :- 15 jan will come for admission ( Indrapuri) + frnd
[12/01/24, 6:08:06 PM] Neha mam e.c: Friend kon
[12/01/24, 6:08:31 PM] Neha mam e.c: @ team kya hua
[12/01/24, 6:08:38 PM] Neha mam e.c: Kitne admission ho gye
[12/01/24, 6:08:42 PM] naresh e.c: Mam frnd hai uska usne bola hai me sath me launga
[12/01/24, 6:09:00 PM] naresh e.c: Usko details  leni h usko samjh.ayega to wo bhi admission lelega bola usne
[12/01/24, 6:14:11 PM] suman coding: Name of Student: Nikita kherajani
Contact no: 6232665447
Branch:Artificial intelligence and machine learning 
College: LNCT 
Year: 3rd 
Expected Date of Visit: 15  January mp nagar
[12/01/24, 6:17:15 PM] suman coding: Name of Student: anshul sharma
Contact no: 8516812242
Branch:Artificial Intelligence and machine learning 
Collaage: LNCT 
Year: 3rd 
Expected Date of Visit: 15 january indrapuri
[12/01/24, 6:17:51 PM] Neha mam e.c: To usko kyun likh raha hai jiska naam tere ko hi nahi maloom
[12/01/24, 6:19:41 PM] naresh e.c: Mam sab likhte h
[12/01/24, 6:20:07 PM] Neha mam e.c: Name pata ho to likho nahi to koi bhi nahi likho
[12/01/24, 6:20:11 PM] naresh e.c: And jo humare prospects ke sath visit ke liye aata h wo to humara hi hota h na
[12/01/24, 6:20:38 PM] Neha mam e.c: Name pata ho to likho
[12/01/24, 6:20:44 PM] Neha mam e.c: Nahi to aapka nahi hai
[12/01/24, 6:21:21 PM] naresh e.c: But mam kp sir ne bola tha
[12/01/24, 6:21:38 PM] Neha mam e.c: Name pata hai kya
[12/01/24, 6:21:52 PM] Neha mam e.c: Baat name ki chal rahi hai
[12/01/24, 6:22:33 PM] naresh e.c: Mai puch lunga usse
[12/01/24, 6:22:41 PM] Neha mam e.c: Group me koi argue nahi chaiye
[12/01/24, 6:23:17 PM] Neha mam e.c: Name pata ho to sabji likho nahi to friend akele likhne se kuch nahi hoga
[12/01/24, 6:24:46 PM] ~ Deepali coding: Name of Student: Bhavika rathore
Contact no: 9301765674
College:-tit
Branch: CS
Year: 3rd
Expected Date of Visit:  14jan
[12/01/24, 6:40:12 PM] anchal e.c: 3rd year
	Electronics & Communication Engineering	

Oriental Institute of Science & Technology
Name_	AMAN AHIRWAR	
Number _9179252152	
Date _ after 20 January
[12/01/24, 6:42:35 PM] Hafsa.: Name of Student: Rukmani Patel
Contact no: 9302117460
Branch: EC
Year: 3rd Yr
Expected Date of Visit:  Will contact after discussing with parents
[12/01/24, 6:52:02 PM] ~ Chauhan Shilpa: Name of Student: FAIZUL HAMEED TAUIQUE
Contact no: 8002253840
Branch: Computer Science & Engineering
Year: 2 nd Yr
Expected Date of Visit:  After exam
[12/01/24, 6:56:30 PM] Neha mam e.c: Aaj kiska kya hua
[12/01/24, 6:56:37 PM] Neha mam e.c: Kitne hue
[12/01/24, 6:59:02 PM] arpana e.c: ni hue
[12/01/24, 6:59:19 PM] ~ Deepali coding: Nhi hua mam Sunday bola hai usne aane ka father ke sath
[12/01/24, 6:59:44 PM] Neha mam e.c: Kp sir koi nahi sabki aaj absent laga dena
[12/01/24, 7:00:16 PM] Neha mam e.c: @916260034224 enquiry pad se bhi koi nahi nikla
[12/01/24, 7:00:38 PM] arpana e.c: no mam
[12/01/24, 7:00:51 PM] arpana e.c: ek ne bola tha ..ab call recive ni kr rhe ho wo
[12/01/24, 7:01:36 PM] Neha mam e.c: 1 bhi nahi nikla
[12/01/24, 7:08:14 PM] arpana e.c: 15 and 16 ke h
[12/01/24, 7:08:21 PM] arpana e.c: aj ek bhi ni
[12/01/24, 7:18:44 PM] anup kumar ct: 3RD	EC	LNCT	Shivam 	9798015433	Indrapuri 	20 Jan
[12/01/24, 7:19:12 PM] anup kumar ct: 2ND	Civil 	Trinity 	Salim	8103200661		20 Jan
[12/01/24, 7:19:27 PM] anup kumar ct: Ekta 	6260881668		12 Jan
[12/01/24, 7:21:17 PM] anup kumar ct: Name of Student: Golu 
College name: SIRT
Contact no: 8223876601
Branch: CSE
Year: 3RD
Expected Date of Visit: 13 Jan
[12/01/24, 7:22:05 PM] anup kumar ct: Name of Student: Harshil
College name: SIRT
Contact no: 8770765017
Branch: CSE
Year: 3RD
Expected Date of Visit: 18 Jan
[12/01/24, 7:22:33 PM] suman coding: Name of Student: parth Pandey 
Contact no: 6350001880/7877961428
Branch: Artificial Intelligence and machine learning 
College: LNCT 
Year: 3rd 
Expected Date of Visit: 25  January indrapuri
[12/01/24, 7:22:58 PM] anup kumar ct: Name of Student: Mayank 
College name: SIRT
Contact no: 9770421079
Branch: CSE
Year: 3RD
Expected Date of Visit: will confirm after discussing with parents
[12/01/24, 7:24:39 PM] Hafsa.: Name of Student: Rishav Ranjan 
Contact no: 7209106081
Branch: CS/DS
Year: 3rd Yr
Expected Date of Visit: Will come after 15 Jan
[12/01/24, 7:25:27 PM] naresh e.c: Name :- mustafa ahmad 
Number: - 8839505504
College: - radha raman 
Branch :- cse
3rd year 
Expected date of Visit :- 17 Feb
[12/01/24, 7:36:35 PM] Hafsa.: Name of Student: Ayush Mishra
College : OIST
Contact no: 7209106081
Branch: CS
Year: 3rd Yr
Expected Date of Visit: Will come after 15 Jan
[13/01/24, 11:52:27 AM] khushi e.c: Mam mere pass data nhi hai
[13/01/24, 11:52:48 AM] arpana e.c: Sagar Institute of Research & Technology	MOHIT NOUGRAHIYA	9179333570
3rd year
	will come 15 jan
[13/01/24, 11:53:33 AM] Neha mam e.c: Aapko total kitne no Mille
[13/01/24, 11:54:21 AM] khushi e.c: 50
[13/01/24, 11:54:56 AM] khushi e.c: Or 40    Shilpa mam ne diye  the
[13/01/24, 11:55:25 AM] Neha mam e.c: Acha
[13/01/24, 11:55:40 AM] Neha mam e.c: Total aapko abhi tak 90 hi no Mille hai
[13/01/24, 11:55:59 AM] khushi e.c: Kl ke hai ye number
[13/01/24, 11:56:55 AM] Neha mam e.c: Me aapse total no ki baat kar rahi hu jabse aap join kari ho jabse aapka kitna data hai
[13/01/24, 11:57:23 AM] khushi e.c: Sorry mam me bta Rahi hu count krke
[13/01/24, 12:00:02 PM] khushi e.c: ‎This message was deleted.
[13/01/24, 12:01:05 PM] Hafsa.: Name of Student: Vanshika Verma 
College : LNCT
Contact no: 9302229589
Branch: CS
Year: 3rd Yr
Expected Date of Visit: 25 Jan
[13/01/24, 12:01:46 PM] khushi e.c: Mam total 558 hai
[13/01/24, 12:08:55 PM] suman coding: Mam data send kar dijiye
[13/01/24, 12:10:08 PM] Neha mam e.c: Aapke kitna tha
[13/01/24, 12:16:11 PM] Lalita Sahu: Mam mujhe data allot kr dijiye
[13/01/24, 12:16:44 PM] Lalita Sahu: Mere pass total google sheet me 935number h
[13/01/24, 12:17:43 PM] Neha mam e.c: Aap 3 pehale isime se visit bulaiye aaj
[13/01/24, 12:18:00 PM] Lalita Sahu: Ok
[13/01/24, 12:45:41 PM] ~ Deepali coding: Name of Student: vishal choudhary 
College : Scope college 
Contact no: 9770864032
Branch: CS
Year: 3rd Yr
Expected Date of Visit: 15 January chetak
[13/01/24, 1:03:33 PM] anchal e.c: 3rd year 
	Electrical & Electronics Engineering	
Bansal Institute of Science & Technology	 Name _URMILA NAGESH	
 number _8770954068	
Date _after 15 jan
[13/01/24, 1:03:39 PM] Hafsa.: Name of Student: Arpita Malviya 
College : Truba College 
Contact no: 6232706745
Branch: AI/DS
Year: 3rd Yr
Expected Date of Visit: Will come after 15 Jan
[13/01/24, 1:04:12 PM] Hafsa.: Name of Student: Aaliya Shah
College : Truba College 
Contact no: 9301931208
Branch: AI/DS
Year: 3rd Yr
Expected Date of Visit: 21 Jan
[13/01/24, 1:15:40 PM] ~ Chauhan Shilpa: Suman Durga Lalita apko data de diya hai
[13/01/24, 1:18:58 PM] ~ Deepali coding: Name of Student: Firdous ansari
College  All' saints 
Contact no: 9752656661
Branch: CS
Year: 3rd Yr
Expected Date of Visit: will come 5 feb
[13/01/24, 1:23:40 PM] suman coding: No mam
[13/01/24, 1:36:41 PM] khushi e.c: Ok mam
[13/01/24, 1:46:05 PM] arpana e.c: Trinitty College	FAIZA ANSARI	7828539601	
1st year
will come feb mid
[13/01/24, 1:52:39 PM] naresh e.c: Name :- Ridhima dubey 
Number: - 7067459831
College: - radha raman 
Branch :- cs e
Expected date of visit: - 15 jan
[13/01/24, 2:47:44 PM] Hafsa.: Name of Student: Tathagat Kumar 
College : OIST
Contact no: 9301931208
Branch: CS/DS
Year: 3rd Yr
Expected Date of Visit: 21 Jan
[13/01/24, 2:51:29 PM] ~ Deepali coding: Name of Student: faiz khan
College : all saints 
Contact no: 9340458100
Branch: CS
Year: 3rd Yr
Expected Date of Visit: will come date not confirm
[13/01/24, 3:04:41 PM] anchal e.c: 4 year
Information Technology	Bansal Institute of Science & Technology
Name_	ABHILASHA
	number _8252421352	
 Date_14 January
[13/01/24, 3:16:34 PM] Lalita Sahu: Name :- mehroz
Number: - 8228876264
College: - corporate institude of science & techology
Branch :- eletrical &electronics engineering
Year:-3rd
Expected date of visit :- 16 January
[13/01/24, 4:00:32 PM] ~ Deepali coding: Name of Student: sujan vasuniya
College : patel college 
Contact no: 7610263471
Branch: CS
Year: 3rd Yr
Expected Date of Visit: will come 15 January
[13/01/24, 4:23:29 PM] anchal e.c: 4th year
Information Technology	Bansal Institute of Science & Technology	
ROHIT CHOUDHARYn
Number_	7909568582	
Date_ 16 Jan
[13/01/24, 4:23:34 PM] arpana e.c: Trinitty College	SHAHZAD ALAM	6202386904	
1st year
will think feb last
[13/01/24, 4:29:40 PM] khushi e.c: Name :-  kanhaiya lal  amba 
Number: -    7974430184
College: - Sam 
Branch :- electronic or electronic engineering 
Expected date of visit: - 18 jan
[13/01/24, 4:30:16 PM] naresh e.c: Name :- vishal 
Number: - 9625330997
College :- radha raman 
Branch :- cs 
2nd year 
Expected date of visit :- 25 jan
[13/01/24, 4:32:00 PM] Lalita Sahu: Name :- ashish priya gautam
Number: - 9128923164
College: - corporate institude of science & techology
Branch :- eletrical &electronics engineering
Year:-4th
Expected date of visit :- will think feb last
[13/01/24, 4:40:52 PM] ~ Deepali coding: Name of Student: Garima shrivastava
College : LNCT
Contact no: 9770190165
Branch: CS
Year: 3rd Yr
Expected Date of Visit: will come 18 January
[13/01/24, 4:41:02 PM] suman coding: Name :- Rakesh Kumar 
Number: -   8725878289
College: - LNCT 
Branch :- CS 
Expected date of visit: - 2 February
[13/01/24, 4:53:26 PM] anchal e.c: With frd arman+ 2 tomorrow visit
[13/01/24, 5:14:07 PM] anchal e.c: ‎This message was deleted.
[13/01/24, 5:15:19 PM] anchal e.c: 4th year
Computer Science & Engineering-Data Science	Lakshmi Narain 
College of Technology Excellence	
ABHAY SINGH TOMAR	
Number _8718902818
Date_	15,16 January
[13/01/24, 5:16:39 PM] naresh e.c: Name :- akib  anzar
Number: - 9525892608
College: - Millennium 
Branch :- cs 
Expected date of visit: - will join in march after exm
[13/01/24, 5:17:20 PM] arpana e.c: Sagar Institute of Research & Technology	NITESH KUSHWAHA
	6262845526
3rd year
	will come 21 jan
[13/01/24, 5:19:51 PM] ~ Deepali coding: Name of Student: Atul tiwari 
College : TIT 
Contact no: 8269253010
Branch: CS
Year: 2nd year
Expected Date of Visit: will come after 15 feb
[13/01/24, 5:49:45 PM] arpana e.c: Sagar Institute of Research & Technology	POOJA DHAKAR
	7225911682	
3rd year
will come 19 jan
[13/01/24, 5:54:03 PM] suman coding: Name of Student: Aditya lavanshi
College : scope 
Contact no: 6266302249
Branch: btech 
Year: 1st  year
Expected Date of Visit:  1 February
[13/01/24, 5:55:03 PM] Lalita Sahu: Name of Student: ajay
Contact no: 8349683045
College:-Trinity Institute of Technology & Research
Branch: Electronics & Communication Engineering
Year: 3rd
Expected Date of Visit:  16 jan
[13/01/24, 5:56:28 PM] suman coding: Name of Student: Abhi Singh 
College : LNCT 
Contact no: 6267982701
Branch: CS
Expected Date of Visit:  1 February
[13/01/24, 6:18:37 PM] kp sir: Data allot kardiyaa hai ,Durga, Lalita, suman
[13/01/24, 6:18:58 PM] kp sir: Muje call record karkee bhejooo aap teeno log
[13/01/24, 6:19:07 PM] kp sir: Jo baat karrahe hain aap students se
[13/01/24, 6:22:33 PM] Lalita Sahu: Ok sir
[13/01/24, 6:22:44 PM] khushi e.c: Ok sir
[13/01/24, 6:34:50 PM] arpana e.c: Technocrats Institute of Technology & Science	SATYAM KUMAR MISHRA	9305191460	
3rd year
will think feb
[13/01/24, 6:39:51 PM] arpana e.c: Technocrats Institute of Technology & Science	SAURABH KUMAR	9135791602
3rd year
	will come 17 jan
[13/01/24, 7:13:57 PM] arpana e.c: Technocrats Institute of Technology & Science	SIDDHARTH SATYAM	9334585171	
3rd year
will think feb last
[13/01/24, 7:17:09 PM] anup kumar ct: 3RD	Computer Science & Engineering	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	ARJUN	8815009315		14 Jan
[13/01/24, 7:17:39 PM] anup kumar ct: FINAL 	MCA	Technocrats Institute of Technology [Excellence]	AMBESH RAJPUT	9981308137 	20 Jan
[13/01/24, 7:17:58 PM] anup kumar ct: 3RD	Computer Science & Engineering	Technocrats Institute of Technology - Computer Science and Engineering	AJAY KUMAR	7979761285		Feb
[14/01/24, 11:48:46 AM] anchal e.c: 4th year 
Computer Science & Engineering-Data Science	Lakshmi Narain College of Technology Excellence	
AMIT KUMAR CHAUDHARY
	number _7970443562
Date_	 not confirm date to visit
[14/01/24, 11:50:46 AM] anchal e.c: ‎This message was deleted.
[14/01/24, 11:51:22 AM] anchal e.c: 2nd year 
Computer Science & Engineering-Artificial Intelligence and Data Science	
Technocrat Institute of Technology	
 Name _GAUTAM 
Number_	8305630117			 	 
Date _20 January
Old prospect
[14/01/24, 12:11:26 PM] arpana e.c: Technocrats Institute of Technology & Science	STUTI TIWARi
	6307616813
3rd year
	will come 15 jan
[14/01/24, 12:26:06 PM] arpana e.c: Technocrats Institute of Technology & Science
	SUDARSH VERMA	6264103792	
3rd year
will think
[14/01/24, 12:36:55 PM] khushi e.c: Name of Student: Abhishek   Kumar yadav 
College :  Radha Raman Institute of Technology & Science
Contact no:  9065623054
Branch:Computer Science & Engineering
Expected Date of Visit:   14 Jan indrapuri
[14/01/24, 12:39:18 PM] Lalita Sahu: Name of Student: Arjun vishvkrma
Contact no: 8827289753
College:  NRI Institute of Information Science & Technology
Branch:- Artificial Intelligence and Data Science
Year: 3rd
Expected Date of Visit:  13feb
[14/01/24, 12:59:34 PM] Hafsa.: Name of Student: Rohan Pawar with friends (Rishabh + Gautam)
College : SIRT 
Contact no: 7999282188
Branch: AI/ML
Year: 3rd Yr
Expected Date of Visit: 15 Jan ‎<This message was edited>
[14/01/24, 1:41:35 PM] arpana e.c: IES's College of Technology	VIKRAM RATHOUR	7004990455	
4th year
will come feb 5
[14/01/24, 3:00:28 PM] anchal e.c: 4th year 
	Computer Science & Engineering-Data Science	Lakshmi Narain College of Technology Excellence	 Name_KOUSHIK BAGHEL
Number_	6264399313	
	Date _16 January
[14/01/24, 3:01:29 PM] Hafsa.: Name of Student: Mayank with friends ( Akash+ Shivya shu)
College name: IIES/ Sha - Shib 
Contact no: 9058707261
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  14 Jan
[14/01/24, 3:38:58 PM] Lalita Sahu: Name :- deepak ahirwar
Number: - 7477002894
College: - corporate institude of science & techology
Branch :- eletrical &electronics engineering
Year:-3rd
Expected date of visit :-  mid in feb not confirmed date
[14/01/24, 3:45:38 PM] khushi e.c: ‎This message was deleted.
[14/01/24, 3:48:53 PM] suman coding: Name :- pratham goswami 
Number: - 6232105580
College: - LNCT 
Branch :-  computer science & engineering 
Expected date of visit :- 1 March
[14/01/24, 3:52:05 PM] khushi e.c: Name :- Shivam  kumar 
Number: - 7079342585
College: - oriental 
Branch :- eletrical &electronics engineering
Year:-3rd
Expected date of visit :-   will think
[14/01/24, 3:53:54 PM] khushi e.c: Name :- Armaan Raqueeb 
Number: - 6232105580
College: - Radha Raman Institute of Technology & Science
Branch :-  computer science & engineering 
Expected date of visit :- will  confirm with freind
[14/01/24, 3:59:13 PM] suman coding: Name :- Gaurav nagwani
Number: - 63063379537
College: - LNCT 
Branch :- computer science & engineering
Expected date of visit :-   will think
[14/01/24, 4:10:20 PM] arpana e.c: Technocrats Institute of Technology & Science	TEJASWI TRIPATHI	8827166706
3rd year
	will come today 14 jan
[14/01/24, 4:10:32 PM] arpana e.c: with frind sahil
[14/01/24, 4:25:25 PM] kp sir: Iskaa bhi member nahi hai aap number ku nahi daalrahe hooo
[14/01/24, 4:27:05 PM] Hafsa.: Sir actually us time Anurag Sir ne hm log ko msg bana k Diya bs itna hi to usi me copy kr diya 
Badme hmne add Kara hai number
Ye pehle ka dala hua h
[14/01/24, 4:27:21 PM] Hafsa.: 7470656955
[14/01/24, 4:30:25 PM] Lalita Sahu: Name :- prashant kumar pal
Number: - 8109527502
College: - Kopal institude of science & technology
Branch :- computer science engineer
Year:-3rd
Expected date of visit :-  16jan(MP nagar)
[14/01/24, 4:30:54 PM] anchal e.c: 4th year 
	Computer Science & Engineering-Data Science	Lakshmi Narain College of Technology Excellence	PUSHPESH KUMAR	7482875634	
Date _15 January
[14/01/24, 4:45:51 PM] khushi e.c: Name :-  Altaf mallick 
Number: -  9661883278
College: -  Radha Raman 
Branch :-  electrical and electronics engineering 

Expected date of visit :-   23rd Jan
[14/01/24, 4:51:52 PM] khushi e.c: Name : arfat mallick 
Number: -  7488538291
College: -  Radha Raman 
Branch :-   electrical and electronics engineering 
Expected date of visit :-   will think
[14/01/24, 5:34:30 PM] suman coding: Name :-  Arjun prajapati 
Number: -  7987280398
College: -  SAGE
Expected date of visit :-   20 January mp nagar
[14/01/24, 5:39:19 PM] khushi e.c: Name :-   MD Sharfe Alam 
Number: -  7325038636
College: -  Radha Raman 
Branch :-  electrical and electronics engineering 
Expected date of visit :-   7 March  mp nagar
[14/01/24, 5:53:33 PM] Lalita Sahu: Name :- yashika lokhnde
Number: - 6261746935
College: - Kopal institude of science & technology
Branch :- computer science engineer
Year:-3rd
Expected date of visit :- will think mid feb
[14/01/24, 6:10:57 PM] arpana e.c: coming today with frind shub
[14/01/24, 6:11:23 PM] kp sir: Indrapuri yaa mp nagar
[14/01/24, 6:11:34 PM] arpana e.c: mp nagar
[14/01/24, 6:12:59 PM] anup kumar ct: Name of Student: Gajendra with friends 
College name: Truba
Contact no: 9098366859
Branch: CSE
Year: 2ND
Expected Date of Visit: 14 Jan
[14/01/24, 6:38:26 PM] ~ Deepali coding: Name of Student: anmol kumar
College name: Tit
Contact no: 7070423528
Branch: Cs& data science 
Year:3rd 
Expected Date of Visit: 16 January
[14/01/24, 7:00:08 PM] Hafsa.: Name of Student: Shubham 
College name: NRI College 
Contact no: 9589531381
Branch: CSE
Year: 3rd Year 
Expected Date of Visit : Will come February
[14/01/24, 7:09:32 PM] suman coding: Name :-  Amit chouhan 
Number: -  6264468937
College: -  LNCT 
Branch :-  computer science & engineering cyber security 
Year :- 3 year 
Expected date of visit :-   20 January MP Nagar
[14/01/24, 7:19:59 PM] kp sir: https://t.me/+znnI-iRHPK04MWVl

New fsd batch mpnagar main jo admission hue hai unkaa group ki link hai jinke prospects ne admission liyaa pls unko bhejdee join karne ke liye
[14/01/24, 7:20:11 PM] ~ Deepali coding: Oky
[14/01/24, 7:20:34 PM] kp sir: Sabhi log bhejeee jinke admission hai
[14/01/24, 7:21:24 PM] Lalita Sahu: Name :- ankit  kanojiya
Number: - 9754757876/8435484936
College: - Kopal institude of science & technology
Branch :- computer science engineer
Year:-3rd
Expected date of visit :- 16jan mpnagar
[14/01/24, 7:22:01 PM] ~ Deepali coding: Name of Student: Anand 
Contact no: 6261674835
Branch: Cs 
Year m tech
Expected Date of Visit: after 10 feb ( old prospect)
[14/01/24, 7:23:57 PM] ~ Deepali coding: Name of Student: mehtab khan
College name: Bansal
Contact no: 8090994259
Branch: Cs 
Year:2nd year
Expected Date of Visit: after exam 15 feb (Old prospect)
[14/01/24, 7:24:36 PM] ~ Deepali coding: Name of Student: Sandeep
College name: oriental
Contact no: 7067778065
Branch: Cs 
Year:2nd year
Expected Date of Visit: after exam 15 feb (Old prospect)
[14/01/24, 7:25:30 PM] ~ Deepali coding: Name of Student: Jitendra choudhary 
College name: oriental
Contact no: 9299088027
Branch: Cs 
Year:2nd year
Expected Date of Visit: after exam 10feb (Old prospect)
[14/01/24, 7:26:12 PM] ~ Deepali coding: Name of Student: Aman Raj 
College name: tit
Contact no: 7870556656
Branch: Cs 
Year:2nd year
Expected Date of Visit: after exam 10feb (Old prospect)
[14/01/24, 7:26:38 PM] anchal e.c: 4th year
	Electronics & Communication Engineering	Oriental College of Technology	
SARVESH TIWARI
	7879539085	
Date15 , 16 January
[14/01/24, 7:36:14 PM] kasim k: link work nahi kar rahi
[14/01/24, 7:38:59 PM] anup kumar ct: 3RD	Computer Science & Engineering	Technocrats Institute of Technology & Science	HARSHAL BAGDE	6266792526 	Feb
[14/01/24, 8:17:01 PM] kp sir: Sab join horahe hai
[15/01/24, 9:11:02 AM] ~ Deepali coding: Will come today indrapuri
[15/01/24, 10:56:35 AM] Lalita Sahu: Taking week off today
[15/01/24, 11:52:32 AM] Hafsa.: Name of Student: Rohit Kumar Sahu
College name: Trinity College 
Contact no : 7879572590
Branch: CS/DS
Year: 1st Year old prospect 
Expected Date of Visit : Will come after exam
[15/01/24, 12:11:50 PM] naresh e.c: Coming today
[15/01/24, 12:17:34 PM] naresh e.c: Coming today
[15/01/24, 12:18:01 PM] khushi e.c: Ok
[15/01/24, 12:18:09 PM] khushi e.c: ‎This message was deleted.
[15/01/24, 12:19:39 PM] naresh e.c: Kiska timing ?
[15/01/24, 12:20:40 PM] khushi e.c: Sorry  by mistake   sent  ho gya
[15/01/24, 12:21:22 PM] naresh e.c: Okk
[15/01/24, 12:57:11 PM] naresh e.c: Name :- Muskan shivhare 
Number: - 8103332166
College: - lnct
Expected date of visit: - 16 jan
[15/01/24, 1:16:01 PM] Hafsa.: Will come at evening
[15/01/24, 1:31:27 PM] kp sir: Duman ismme 11 digit hai correct number daale
[15/01/24, 1:32:36 PM] kp sir: Kis year ka students hai
[15/01/24, 1:35:01 PM] kp sir: Is prospects ka number same hai Prabhat Goswami ke number se
[15/01/24, 1:35:12 PM] kp sir: Is number se
[15/01/24, 1:35:28 PM] kp sir: Kaam chal rahaa hai yaa majak horahaaa
[15/01/24, 1:42:40 PM] khushi e.c: Sorry sir vo copy kar rahi thi toh mistake ho gai
[15/01/24, 1:45:03 PM] khushi e.c: Name :- Armaan Raqueeb
Number:- 9826717735
College:- Radha Raman  institute of technology
Branch:- computer science and engineering
Expected date of visit:- will confirm with friends
[15/01/24, 1:51:47 PM] suman coding: Sorry sir ek digit jayada likh gya tha
[15/01/24, 1:54:28 PM] suman coding: Name :- gaurav nagwani 
Number:- 6306279537
College:-  LNCT 
Branch:- computer science and engineering
Expected date of visit:- will thik
[15/01/24, 1:54:41 PM] naresh e.c: Name :- anil yadav 
College :- radharaman 
Branch :- cse
Number: - 8210140091
Expected date of Visit: - after exam
[15/01/24, 1:55:58 PM] khushi e.c: Name of Student: Shivam vishwakarma 
College name:  scope College 
Contact no :  9009806823
Branch: CSE 
Expected Date of Visit : 17 , 18 jan in m.p nagar
[15/01/24, 2:01:01 PM] suman coding: Name :- Kapil suryavanshi 
Number:- 9302319521
College:- technocrats institute of technology & science 
Branch:- CS & E - AI and Mac
Expected date of visit:- 20 January mp nagar
[15/01/24, 2:52:08 PM] kp sir: NRI WAALE KISKE PROSPECT THE JO VISIT KARGYA THA UNKOO FEES JADA LAGRAHI THI
[15/01/24, 2:52:16 PM] kp sir: Kal koi bolrahaa tha
[15/01/24, 2:53:43 PM] anup kumar ct: Sir mere hi tha but call nhi utha rha ab
[15/01/24, 3:08:49 PM] suman coding: Name of Student: saurabh kumar 
College name:  technocrats institute of technology 
Contact no : 9142786797
Branch: information technology 
Expected Date of Visit : 15 January 6:00 pm indrapuri
[15/01/24, 3:43:22 PM] naresh e.c: Name :- rashi jain 
Number: - 9981841278 
Branch :- cse 
College: - bansal 
Expected date of visit: - intrested  will come 25 jan
[15/01/24, 3:45:00 PM] khushi e.c: ‎This message was deleted.
[15/01/24, 3:46:17 PM] khushi e.c: Name :-  nitish Mishra 
Number: - 9955448955
Branch :- cse 
College: -  scope college 
Expected date of visit: -  after 15 Feb
[15/01/24, 3:56:09 PM] suman coding: Name :-  aniket Kumar 
Number: - 8292584091
Branch :- information technology 
College: -  TIT 
Expected date of visit: -  after 8 February indrapuri
[15/01/24, 4:08:14 PM] khushi e.c: Name :-  Nikhil 
Number: - 6206194491
College: -  TIT 
Expected date of visit: -  after 31 Jan
[15/01/24, 4:09:13 PM] khushi e.c: Name :-  Nageshwar 
Number: - 9165662065
College: -  TIT 
Expected date of visit: -  after 11February
[15/01/24, 4:11:36 PM] khushi e.c: Name :-  Aditya 
Number: - 8349003439
College: -  TIT 
Expected date of visit: -  after   10 February
[15/01/24, 4:19:21 PM] suman coding: Name :-  Abhijit Kumar Singh 
Number: - 9142289442
Branch :- information technology 
College: -  TIT 
Expected date of visit: - 17 February after exam
[15/01/24, 5:11:08 PM] kp sir: Suman anshul Sharma aanewalaa hai
[15/01/24, 5:11:09 PM] kp sir: Aaj
[15/01/24, 5:11:17 PM] kp sir: Ki nahi
[15/01/24, 5:12:15 PM] kp sir: Nikita ka kya hai aaj aanewali
[15/01/24, 5:12:16 PM] kp sir: Thi
[15/01/24, 5:12:20 PM] kp sir: Suman
[15/01/24, 5:14:11 PM] suman coding: Aikita ko call kiya tha maine 16 January ko Ane ka bola hai
[15/01/24, 5:14:34 PM] suman coding: Anshul 17 January ka bola hai
[15/01/24, 5:25:03 PM] kp sir: Pls update your remarks in Google sheet
[15/01/24, 5:25:14 PM] kp sir: As per conversation to students
[15/01/24, 5:25:26 PM] suman coding: Okey sir
[15/01/24, 5:38:07 PM] khushi e.c: Name :-    Ashish Kumar Singh 
Number: - 9693048853
Branch :- Computer Science & Engineering-Cyber Security
College: -  Lakshmi Narain College of Technology & Science
Expected date of visit: - 16 Jan evening indrapuri
‎[15/01/24, 5:42:03 PM] kp sir: ‎image omitted
[15/01/24, 5:44:40 PM] kp sir: https://t.me/+KnLdXG15x4dhZDBl
[15/01/24, 5:45:11 PM] anchal e.c: 3rd year
	Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence	UJJAWAL 
Name _VISHWAKARMA	
number 9179486421	
Date _after 22
[15/01/24, 6:44:28 PM] kp sir: ‎kp sir changed this group’s settings to allow only admins to add others to this group.
[15/01/24, 6:24:31 PM] Hafsa.: Name of Student: Kamta Prasad Kushwaha with friends (Shivam + Indrapal)
College name: SIRT
Contact no : 9111655074
Branch: EE
Year: 3rd Yr
Expected Date of Visit : 20 Jan
[15/01/24, 6:56:07 PM] khushi e.c: Name : -    Satish Kumar Singh 
Number: -6201012718
Branch :-  Computer Science & Engineering-Cyber Security
College: -  lnct
Expected date of visit: -  17 Jan indrapuri
[15/01/24, 7:27:15 PM] anup kumar ct: Name of Student: Ajay 
College name: SAM
Contact no: 8817509357
Branch: CSE
Year: 3RD
Expected Date of Visit: 20 Jan
[15/01/24, 7:28:05 PM] anup kumar ct: Name of Student: Amit
College name: SAM
Contact no: 6262792686
Branch: CSE
Year: 3RD
Expected Date of Visit: 25 Jan
[15/01/24, 7:28:49 PM] anup kumar ct: Name of Student: Bhanupratap 
College name: SAM
Contact no: 9981290141
Branch: CSE
Year: 3RD
Expected Date of Visit: will think
[15/01/24, 7:29:30 PM] anup kumar ct: Name of Student: Chetan 
College name: SAM
Contact no: 8815069845
Branch: CSE
Year: 3RD
Expected Date of Visit: 18 Jan
[15/01/24, 7:30:17 PM] anup kumar ct: Name of Student: Damini
College name: SAM
Contact no: 7241129701
Branch: CSE
Year: 3RD
Expected Date of Visit: 16 Jan
[15/01/24, 7:30:58 PM] anup kumar ct: Name of Student: Hemant 
College name: SAM
Contact no: 6260002693
Branch: CSE
Year: 3RD
Expected Date of Visit: 16 Jan
[15/01/24, 9:21:05 PM] arpana e.c: sir ye link fsd new walo ke bhj skte h
[15/01/24, 9:33:40 PM] ~ Deepali coding: Name : -    Deepak Kumar with friends ( ishan , sunny)
Number:  96932 06681
Branch :-  cs
College: -  Radha raman
Expected date of visit: -  16 jan chetak
[16/01/24, 11:29:21 AM] kp sir: Nahi
[16/01/24, 11:30:40 AM] kp sir: https://t.me/+znnI-iRHPK04MWVl
[16/01/24, 11:30:57 AM] kp sir: New yeah hai
[16/01/24, 11:44:25 AM] arpana e.c: ‎This message was deleted.
[16/01/24, 11:44:34 AM] arpana e.c: ohk sir
[16/01/24, 11:48:57 AM] kp sir: 2 admission jo data science main hue hai unkoo inform karnaa hai .
Aur Naresh tumhara 1 data science ka aana Tha,
[16/01/24, 11:50:12 AM] Neha mam e.c: Time 6:30 se 8:30 hai
[16/01/24, 11:50:21 AM] kp sir: Arpana, Kal enquiry aai thi data science ki toh unko bhi bulaaloo ,Lena Tha unkoo toh poochlooo ki Kab lerahe
[16/01/24, 11:50:50 AM] kp sir: Maam 6.30PM se 8PM hi Rakhi hai ,bus ke chaltee
[16/01/24, 11:51:28 AM] Neha mam e.c: Ok
[16/01/24, 11:52:25 AM] kp sir: Enquiry pad main dekloo jo bhi Data analyst and data science waale hai unko inform , 2 BSSS college ki bhi thi
[16/01/24, 12:02:47 PM] naresh e.c: Aj ayega
[16/01/24, 12:07:16 PM] ~ Deepali coding: Name : -    Abhay 
Number:  93031 12908
Year : 3 rd
Branch :-  cs
College: -  sam global University 
Expected date of visit: -  17 January
[16/01/24, 12:09:40 PM] arpana e.c: hnn
[16/01/24, 12:12:26 PM] khushi e.c: Name : -    Vaibhav Raj Singh 
Number:  9306505706
Year : 4th year 
Branch :-  Computer Science & Engineering-Cyber Security
College: -  lnct 
Expected date of visit: -  after  16 Feb
[16/01/24, 12:53:07 PM] Hafsa.: Will try to come today with friends Rishita and Bedi
[16/01/24, 1:37:05 PM] Lalita Sahu: Name :- sourav kumar
Number: -9955796043 
College: - Kopal institude of science & technology
Branch :- computer science 
Year:-3rd
Expected date of visit :- 12feb
[16/01/24, 1:46:36 PM] khushi e.c: Name :-  Amir Ali 
Number: -9516767703
College: -Oriental College of Technology
Branch :- Computer Science & Engineering-Cyber Security
Year:-4th 
Expected date of visit :- 19 jan
[16/01/24, 1:48:34 PM] khushi e.c: Name :-  Anubhav maithil
Number: - 9993914345
College: -Oriental College of Technology
Branch :-  Computer Science & Engineering-Cyber Security
Year:- 4th 
Expected date of visit :-   will think
[16/01/24, 3:04:31 PM] ~ Deepali coding: Will come 18 January
[16/01/24, 3:04:36 PM] naresh e.c: Name :- aryan narwale 
College: - bansal 
Branch :- it 
Number: - 9691145504
Expected date of visit: - 16 jan mp  Branch
[16/01/24, 3:24:09 PM] Hafsa.: Name of Student: Sumit Malviya 
College name: SIRT
Contact no : 9098006548
Branch: AIML
Year: 1st year old prospect 
Expected Date of Visit : 16 Jan (Indrapuri)
[16/01/24, 3:51:27 PM] anchal e.c: 4th year 
Electrical & Electronics Engineering	
Radha Raman Institute of Technology & Science
	MD MAHATAB ALAM	
Number _8851267905	
Date _ not confirm date to visit
[16/01/24, 4:01:24 PM] naresh e.c: Name :- JAYLENDRA THAKRE
Number: -  8305615502
Branch :- cse 
College: - bits 
Expected date of visit: - 21 jan
[16/01/24, 4:23:18 PM] ~ Deepali coding: Name :-  Sumit chouhan 
Number: - 7470328732
College: -LNCT
Branch :-  Cs
Year:- 4th 
Expected date of visit :-   17 January
[16/01/24, 4:25:01 PM] naresh e.c: Name :- harsh morya
Number: - 7225902702 
Colleges:-  tit
Branch :- cseaiml
Expected date of visit: - after exam
[16/01/24, 4:38:22 PM] ~ Deepali coding: Name :-  Niraj bisen
Number: - 8602457566
College: -LNCT
Branch :-  Cs
Year:- 3 rd year
Expected date of visit :-   2 feb indrapuri
[16/01/24, 5:25:13 PM] anchal e.c: 3rd year
Computer Science & Engineering-Data Science	Technocrat Institute of Technology	
ABHISHEK DUBEY	
Number _8815112722	
Date _will think
[16/01/24, 5:33:36 PM] Lalita Sahu: Sir data ni h mere pass
[16/01/24, 5:33:58 PM] Lalita Sahu: Or Sare not answering me b call kr liya  h
[16/01/24, 5:34:13 PM] suman coding: Sir mere pas bhi nahi hai data
[16/01/24, 5:34:43 PM] Hafsa.: Name of Student: Pravin Raut
College name: TIT
Contact no : 9301037067
Branch: CS/AI/ML
Year: 3rd Yr
Expected Date of Visit : Will come after 22 Jan
[16/01/24, 6:00:36 PM] khushi e.c: Name of Student:  satyam sahu 
Number:-7441115163
College name:-  oriental college of technology 
Branch: Computer Science & Engineering-Cyber Security
Year: 4th  Yr
Expected Date of Visit :  Will come after 25  Jan indrapuri
[16/01/24, 6:06:48 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Data Science	Technocrat Institute of Technology	
HARSH RAJ	 number _9508525410	
Date _will think
[16/01/24, 6:33:40 PM] arpana e.c: Technocrats Institute of Technology & Science	VISHAL CHANDRAVANSHI
	8463015869	
3rd year
will come 18 jan
for inderpuri
[16/01/24, 6:38:26 PM] anchal e.c: 3rd year
Computer Science & Engineering-Data Science	Technocrat Institute of Technology	
SATYAPRAKASH SINGH RATHOUR	
7067604709
Date_	20 jan f
[16/01/24, 6:56:21 PM] Lalita Sahu: Name :- aditya shrivastava
Number: 8873282427
College: - sagar institude of research& technology
Branch :- computer science 
Year:-4th
Expected date of visit :- last feb not confirm date
[16/01/24, 6:58:27 PM] kp sir: Deepali tumhari visit indrapuri aani thi uskaa kya hua
[16/01/24, 6:58:36 PM] ~ Deepali coding: Name :-  Rudransh vena
Number: - 9753894149
College: TIT
Branch :-  Cs
Year:- 3 rd year
Expected date of visit :-   19 January
[16/01/24, 7:05:32 PM] suman coding: Name of Student:  deeksha sahu 
Number:- 9302794431
College name:-  NRI 
Branch: Computer Science & Engineering
Year: 3 year
Expected Date of Visit : will think
[16/01/24, 7:25:01 PM] anup kumar ct: Name of Student: Gautam 
College name: Bansal
Contact no: 7489793204
Branch: CSE
Year: 3RD
Expected Date of Visit: will Call
[16/01/24, 7:26:04 PM] anup kumar ct: Name of Student: Himanshu 
College name: Bansal
Contact no: 7234014763
Branch: CSE
Year: 3RD
Expected Date of Visit: Feb
[16/01/24, 7:27:08 PM] arpana e.c: Technocrats Institute of Technology & Science	WAMIQUE MASHHADI
	8102475625
3rd year
	will come 1 feb
[17/01/24, 12:19:12 PM] anchal e.c: 3rd year
	Computer Science & Engineering-Data Science	Technocrat Institute of Technology	
JAILENDER KUMAR	
9306779614	
Date _17 jan  will come
[17/01/24, 1:16:20 PM] khushi e.c: Name of Student: Harshit verma 
College name: Sagar Institute 
Contact no:  9144430843
Branch:CS &E
Expected Date of Visit: 20 Jan m.p nagar
[17/01/24, 2:28:39 PM] khushi e.c: ‎This message was deleted.
[17/01/24, 2:28:40 PM] Lalita Sahu: Mam mere pass data ni h
[17/01/24, 2:28:59 PM] khushi e.c: Mam mere pass data nhi hai
[17/01/24, 2:29:06 PM] Lalita Sahu: Data allot kr dijiye
[17/01/24, 2:59:54 PM] kp sir: Haan
[17/01/24, 3:05:30 PM] anchal e.c: 4th Year 
Electrical & Electronics Engineering	
Oriental College of Technology
	ANKIT LOWANSHI
	9755702182	
 Date _18 January
[17/01/24, 4:00:29 PM] khushi e.c: Name of Student: Vishal Namdev 
College name:Mittal Institute of Technology
Contact no: 8770249278
Branch: mechanical engineering 
Expected Date of Visit: will think 
Indrapuri
[17/01/24, 4:06:04 PM] Lalita Sahu: Will come today mp nagar after 7 p.m.
[17/01/24, 4:16:25 PM] ~ Deepali coding: Name :-  Suniksha 
Number: - 9826591260
College: JNCT
Branch :-  Cs
Year:- 3 rd year
Expected date of visit :-   18 January
[17/01/24, 4:22:58 PM] anchal e.c: 4th year 
Electrical & Electronics Engineering	
Radha Raman Institute of Technology & Science	
GUNJAN SINGH AHIRWAR	
7974896713
 Date _after 22 Jan  chetak
[17/01/24, 4:40:58 PM] khushi e.c: Name of Student:  Anubhav Pandey 
College name: Tit 
Contact no: 9693048853
Expected Date of Visit: 19 Jan indrapuri
[17/01/24, 5:26:01 PM] kp sir: Durga 
Lalita  data check karloo
[17/01/24, 5:26:30 PM] khushi e.c: Yes sir
[17/01/24, 5:27:04 PM] Lalita Sahu: Ok sir
[17/01/24, 5:30:22 PM] kp sir: Suman
[17/01/24, 5:30:28 PM] kp sir: Data dediya hai
[17/01/24, 5:30:56 PM] Neha mam e.c: Off par hai
[17/01/24, 5:44:52 PM] khushi e.c: Name :-   Aditya Raj 
Number:- 7903267565
College: lnct
Year:- 3 rd year
Expected date of visit :-   28 January indrapuri
[17/01/24, 5:50:12 PM] ~ Deepali coding: Name :-   nitin dhote
Number:- 6268612917
College:SIRT
Year:- 3 rd year
Expected date of visit :-   20 January
[17/01/24, 5:53:05 PM] Lalita Sahu: Name :-   Anshul singh
Number:- 8770308390
College: sirt
Year:- 3 rd year
Expected date of visit :-20feb
[17/01/24, 6:01:55 PM] Lalita Sahu: Name :-   Kanchan lowanshi
Number:- 9755215804
College: sirt
Year:- 3 rd year
Expected date of visit :-28jan
[17/01/24, 6:03:40 PM] khushi e.c: Name :-  Aman Raj 
Number:- 9905177197
College: lnct 
Year:- 3 rd year
Expected date of visit : after 5 Feb
[17/01/24, 6:05:56 PM] Hafsa.: Name of Student: Rahul Ahirwar 
College name: TIT
Contact no : 7879346067
Branch: CS
Year: 3rd Yr
Expected Date of Visit : 20 Jan
[17/01/24, 6:08:01 PM] annu❤️: +1 friend Yash  Will come 18 January
[17/01/24, 6:24:23 PM] ~ Deepali coding: Name of Student: Raviranjan
College : Sirt
Contact no: 7544858399
Branch: CS
Year: 3rd Yr
Expected Date of Visit: will come after 25 January  ( chetak)
[17/01/24, 6:24:38 PM] Lalita Sahu: Name :-   Krishna kumar jhala
Number:- 9754215804
College: sirt
Year:- 3 rd year
Expected date of visit :-18jan
[17/01/24, 6:28:30 PM] Hafsa.: Name of Student: Tejasv Singh
College name: SISTech
Contact no : 8357071727
Branch: CS
Year: 4th Yr
Expected Date of Visit : 23 Jan
[17/01/24, 6:36:03 PM] annu❤️: ‎This message was deleted.
[17/01/24, 6:36:25 PM] annu❤️: Electrical & Electronics Engineering	
Lakshmi Narain College of Technology
ATHARVADITYA GOKHE
9753486926
Will Come in February
4th year
[17/01/24, 7:05:55 PM] Lalita Sahu: Name :-   PRAFFUL GOUR
Number:- 6263362190
College: sirt
Year:- 3 rd year
Expected date of visit :-25 jan
[17/01/24, 7:07:47 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	PRATHAM VISHWAKARMA	7879945845	 will come jan last
[17/01/24, 7:09:25 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	PRAFUL SOLANKI
	8269481623		will plan after janury
[17/01/24, 7:12:14 PM] arpana e.c: Bansal Institute of Science & Technology	AANAND SAHU
	9301018456
will come
	after 20 jan
[17/01/24, 7:13:29 PM] arpana e.c: Technocrats Institute of Technology - Computer Science and Engineering	AASTHA MISHRA
	7067521221	
will think after janury
[17/01/24, 7:16:24 PM] arpana e.c: Trinity Institute of Technology & Research	
SHIFA NAAZ	
930193264	will come 17 jan today
[17/01/24, 7:28:25 PM] arpana e.c: Sagar Institute of Science & Technology & Research
ADITYA	7820948767	
will come feb
[17/01/24, 7:30:31 PM] Neha mam e.c: @919098778898 kal ke admission ki fee kispar aayi thi confirm karo na
[17/01/24, 7:31:08 PM] anup kumar ct: Name of Student: Pramanand Das 
College name: SAM
Contact no: 9128252272
Branch: CSE
Year: 3RD
Expected Date of Visit: 25 Jan
[17/01/24, 7:35:04 PM] anup kumar ct: Name of Student: Salman 
College name: Oriental 
Contact no: 9131940541
Branch: CSE
Year: 3RD
Expected Date of Visit: will think
[17/01/24, 7:41:27 PM] anup kumar ct: mam wo call pick nahi kar raha
[17/01/24, 7:56:04 PM] Neha mam e.c: To aaj class nahi aaya hai kya
[17/01/24, 8:06:23 PM] anup kumar ct: Mam wo nahi pata
[17/01/24, 8:56:14 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[18/01/24, 12:31:10 PM] Hafsa.: Name of Student: Abhishek Rajput 
College name: Truba College 
Contact no : 9399183271
Branch: AI/DS
Year: 3rd Yr
Expected Date of Visit : 23 Jan
[18/01/24, 12:50:02 PM] ~ Deepali coding: Name of Student: Ravi kumar
College name: Tit
Contact no: 6202676958
Branch: CSE
Year: 3RD
Expected Date of Visit: will come 21 January
[18/01/24, 1:31:51 PM] ~ Chauhan Shilpa: Name of Student: sarthak Gupta 
College name: lnct 
Contact no : 9171858388
Branch: cs
Year: 2rd Yr
Expected Date of Visit :  after exam (17 february)
[18/01/24, 1:34:01 PM] Hafsa.: Name of Student: Ayush Sonakiya 
College name: OCT 
Contact no : 8461945632
Branch: CSE
Year: 3rd Yr
Expected Date of Visit : 21 Jan
[18/01/24, 1:35:41 PM] annu❤️: Electrical & Electronics Engineering	
Lakshmi Narain College of Technology	
SUNNY KUMAR
9608093054	
Will Come 	In February 
4th Year
[18/01/24, 1:36:01 PM] Lalita Sahu: Name :-   roshni daheriya
Number:- 7489645517
College: sirt
Year:- 3 rd year
Expected date of visit :-will think feb mid
[18/01/24, 1:44:21 PM] ~ Chauhan Shilpa: Name of Student: makk khan 
College name: sam
Contact no : 8898981995
Year: mtech 
Expected Date of Visit : February
[18/01/24, 1:47:06 PM] Lalita Sahu: ‎This message was deleted.
[18/01/24, 1:48:18 PM] khushi e.c: Name :-   Ayush Patel 
Number:-  8770094236
College: Tit
Year:- 3 rd year
Expected date of visit :-18 jan indrapuri
[18/01/24, 1:55:13 PM] Lalita Sahu: Name :-   neha singh
Number:- 6268285734
College: Vaishnavi Inst. of Tech. & Science
Year:- 3 rd year
Expected date of visit :-29 jan
‎[18/01/24, 3:04:54 PM] kp sir: ‎audio omitted
[18/01/24, 3:07:59 PM] Lalita Sahu: Name :-   payal suryavansi
Number:- 7489452792
College: Vaishnavi Inst. of Tech. & Science
Year:- 3 rd year
Expected date of visit :-21 jan ( mp nagar)
[18/01/24, 3:09:51 PM] anchal e.c: 4th year
Computer Science & Engineering	
Lakshmi Narain College of Technology Excellence	
SAMEER SAURAV
	8210809588	
Date _	not confirm date to visit
[18/01/24, 3:12:46 PM] kp sir: Yeah visit karchukaa hai kya
[18/01/24, 3:13:21 PM] khushi e.c: Name :-  Bharat 
Number:- 8224962053
College: Tit
Year:- 3 rd year
Expected date of visit :-19 jan  ( mp nagar)
[18/01/24, 3:13:22 PM] kp sir: Yeah bhi visit Kiya ki nahi
[18/01/24, 3:13:26 PM] kp sir: Iskaa kya hua visit ka
[18/01/24, 3:13:38 PM] kp sir: Iskaa visit status
[18/01/24, 3:20:16 PM] Hafsa.: Call receive nhi krti Sir
[18/01/24, 3:21:04 PM] kasim k: 9 jan bola tha usk baad se call receive nhi kar raha
[18/01/24, 3:21:21 PM] kasim k: same
yeh v call receive nahi kr rahe
[18/01/24, 3:26:44 PM] annu❤️: Mechanical Engineering
Technocrats Institute of Technology [Excellence]
DULYA BHILALA
8827003180	
Inform himself 
4th year
[18/01/24, 3:27:13 PM] khushi e.c: Name :-    Bhumika Gayakwad
Number:- 9302914438
College: Tit
Year:- 3 rd year
Expected date of visit :  last Feb ( indrapuri)
[18/01/24, 3:35:16 PM] khushi e.c: Name :-   Deepak 
Number:- 7693019761
College: Tit
Year:- 3 rd year
Expected date of visit :-20 jan (indrapuri)
[18/01/24, 4:19:59 PM] kasim k: Name :-    sankar + oman
Number:- 8226048646,8349629432
College:  Lnct
Year:- 3 rd year
Expected date of visit :   coming 22-25  for registration.
[18/01/24, 4:21:11 PM] Neha mam e.c: Prospect kab bana tha aapka
[18/01/24, 4:21:25 PM] kasim k: already visited hai mam
[18/01/24, 4:21:45 PM] Neha mam e.c: Kab likha tha aapka
[18/01/24, 4:21:48 PM] kasim k: 14 august ko visit kia tha
[18/01/24, 4:21:59 PM] kasim k: sanskar ke sath
[18/01/24, 4:22:04 PM] Neha mam e.c: Vo to mujhe pata hai
[18/01/24, 4:22:16 PM] Neha mam e.c: Par aapne prospect me kab likha tha
[18/01/24, 4:22:40 PM] kasim k: matlb mam  samjha nahi
[18/01/24, 4:25:50 PM] kasim k: auguest mai
[18/01/24, 4:26:47 PM] Neha mam e.c: Aapke isme prospect me to mention hi nahi hai
[18/01/24, 4:26:59 PM] Neha mam e.c: Registration me likh rahe ho
[18/01/24, 4:27:00 PM] kasim k: qki jb mam grup hi nahi tha
[18/01/24, 4:27:11 PM] Neha mam e.c: To abh to tha
[18/01/24, 4:27:16 PM] kasim k: qki already 14aug ko visit kia hai mam
[18/01/24, 4:27:24 PM] Neha mam e.c: Sab likh rahe hai old prospect me
[18/01/24, 4:27:39 PM] kasim k: avi takup le raha na tau bola unhone  25 tk aygge
[18/01/24, 4:27:58 PM] kasim k: wo tau anurag sir ne copy kr lie mam phle hi
[18/01/24, 4:44:51 PM] Lalita Sahu: Name :- Triveni singh 
Number:- 9301960954
College: Vaishnavi Inst. of Tech. & Science
Year:- 3 rd year
Expected date of visit :-21 jan ( mp nagar)
[18/01/24, 4:49:37 PM] kasim k: Name :-    Dilshad khan, muneeb 
Number:- 9754321473,9893666947
College:  all saints
Year:- 2nd year
Expected date of visit :   coming for registration after 10 feb
( already visited )
[18/01/24, 5:11:35 PM] annu❤️: Will Come today indrapuri
[18/01/24, 5:16:42 PM] naresh e.c: Name :- Harsh mourya 
Number: - 7225902702
College :- tit 
Branch :- Alim 
Expected date of visit: - 7 feb
[18/01/24, 5:16:57 PM] kasim k: 4th year 
Computer Science & Engineering	
Trinity Institute of Technology & Research
PANKAJ KUMAR BAIGA	
8103168702	
21-22 jan chetak
[18/01/24, 6:00:41 PM] arpana e.c: Technocrats Institute of Technology - Computer Science and Engineering	ABHISHEK KUMAR GUPTA
	7283041703
3rd year
	will come feb
[18/01/24, 6:14:15 PM] ~ Deepali coding: Computer Science & Engineering	Bansal Institute of Science & Technology	LOKESH DHANGAR	7489560814	r will come 20 January
[18/01/24, 6:23:39 PM] ~ Deepali coding: Computer Science & Engineering	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	NOMAN KHAN	9131685746		will come before 25 January
[18/01/24, 7:12:37 PM] arpana e.c: Technocrats Institute of Technology - Computer Science and Engineering
	ABHISHEK KUMAR
3rd year
 JHA	8102535721	
will think
[18/01/24, 7:13:05 PM] anchal e.c: 3rd year 
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology & Science
	SHUBHANSH BEOHAR	
8269929694
Date_	after 22 Jan
[18/01/24, 7:32:07 PM] anup kumar ct: Name of Student: Suryakant 
College name: TIT
Contact no: 9009823745
Branch: MVA
Year: 2ND
Expected Date of Visit: Will think
[18/01/24, 7:33:48 PM] anup kumar ct: Name of Student: Kashish 
College name: Shashib
Contact no: 9174422083
Branch: CSE 
Year: 3RD
Expected Date of Visit: 25 Jan
[18/01/24, 11:34:17 PM] kp sir: Visit par nahi aayaa hai 
Kya status hai
[18/01/24, 11:35:01 PM] kp sir: Yeah aaj aayaa kya , mention status ki kya hua
[18/01/24, 11:35:30 PM] kp sir: Uskaa bhi visit kargyaa kya
[18/01/24, 11:36:13 PM] kp sir: Yeah join karliyaa kya , aaya Tha phir kya hua status iska
[18/01/24, 11:36:35 PM] kp sir: Iskaa kyaa status hai
[18/01/24, 11:36:52 PM] kp sir: Aaayaa Tha kya aaj yeah
[18/01/24, 11:37:18 PM] kp sir: Yeah aayaaa kya yaa nahi
[18/01/24, 11:37:49 PM] kp sir: Yeah bhi aayaaa kya Kal visit par
[18/01/24, 11:38:19 PM] kp sir: Naresh tumharaa yeah hogyaa hai kya
[18/01/24, 11:41:24 PM] kp sir: Yeah visit hogyai kyaa
[18/01/24, 11:41:32 PM] kp sir: Yeah bhi
[18/01/24, 11:41:44 PM] kp sir: Iskaa
[18/01/24, 11:42:13 PM] kp sir: Visit aai kya yeah ,status
[18/01/24, 11:42:29 PM] kp sir: Yeah bhi
[18/01/24, 11:42:48 PM] kp sir: Anshul aaya kya 17 jan ko
[18/01/24, 11:43:09 PM] kp sir: Ankita aai kya 16 jan ko
[18/01/24, 11:43:35 PM] kp sir: Yeah aayaa kya
[18/01/24, 11:44:17 PM] kp sir: Kisi aur se lagwaooo
[18/01/24, 11:44:37 PM] kp sir: Yeah bhi nahi aayaaa
[19/01/24, 11:58:18 AM] arpana e.c: coming today for inderpuri
[19/01/24, 11:59:31 AM] ~ Deepali coding: Ye 19 - -20 ko aayega
[19/01/24, 11:59:47 AM] ~ Deepali coding: Not answering hai
[19/01/24, 12:00:08 PM] anchal e.c: Feb me visit krega
[19/01/24, 12:59:24 PM] ~ Deepali coding: Computer Science & Engineering	NRI Institute of Research & Technology	SOHAN CHANDRAVANSHI	7999128092	will come 23 January + friends ( mukul+ arun
[19/01/24, 1:31:53 PM] khushi e.c: Name of Student: pushpendra 
College name: Vaishnavi Inst. of Tech. & Science
Contact no: 6260474253
Year: 3RD
Expected Date of Visit: will think
[19/01/24, 1:33:46 PM] kasim k: 3rd year 
Computer Science & Engineering	
Technocrats Institute of Technology & Science	
AMAN SONI	
9754100476	
24 Jan
[19/01/24, 1:41:44 PM] arpana e.c: Oriental Institute of Science & Technology
	AMBRISH KUMAR PANDEY
	9343575655
3rd year
	will come 20 jan
[19/01/24, 2:01:11 PM] Lalita Sahu: Name of Student: jyoti silavat
College name: NRI collage
Contact no: 7746023027
Year: 3RD
Expected Date of Visit: 25jan
[19/01/24, 2:21:05 PM] naresh e.c: Name :- Deepesh Chaurasiya 
Number: - 8109006424
College: - sirt 
Expected date of visit: - 19 jan
[19/01/24, 2:43:36 PM] suman coding: Sir data send kar dijiye
[19/01/24, 3:14:03 PM] arpana e.c: Oriental Institute of Science & Technology	ANUJ PRATAP SINGH
	9118832265
	will think  feb last
[19/01/24, 3:44:50 PM] ~ Deepali coding: Name of Student: Deewan singh
College name: Jnct
Contact no: 6261554042
Year: 3RD
Expected Date of Visit: next week
[19/01/24, 4:04:07 PM] arpana e.c: Technocrats Institute of Technology [Excellence]	KARAN KUMAR KOL
	7024513727
4th year
old prospect
will come jan last
[19/01/24, 4:19:39 PM] Hafsa.: Kal aaegi
[19/01/24, 5:12:39 PM] ~ Deepali coding: 84	Artificial Intelligence and Machine Learning	J.N. College of Technology	LALIT SANODIYA	7000427503		will come before 25 January
[19/01/24, 5:23:36 PM] annu❤️: Electronics & Communication Engineering	
Lakshmi Narain College of Technology	
RUDRA SIHARE	7987214418	
Will Come 	In February 
Python
4th  Year
[19/01/24, 6:10:10 PM] suman coding: Name of Student: Nitish kumar kushwaha 
College name: TIT
Contact no: 9128094693
Branch: computer science and engineering 
Expected Date of Visit: 10 February indrapuri
[19/01/24, 6:24:23 PM] annu❤️: Information Technology
Lakshmi Narain College of Technology	
PRANJAL PIPARSANIA	7999843415	
Will Come Indrapuri 	
19 January	With friend
4th Year
[19/01/24, 6:30:26 PM] arpana e.c: SAM College of Engineering & Technology
	AVINASH KUMAR MAHTO
4th year 
old propect
	7667049997
[19/01/24, 6:32:41 PM] anchal e.c: ‎This message was deleted.
[19/01/24, 6:33:20 PM] anchal e.c: 3rd year 
	Electrical Engineering	Sagar Institute of Science Technology & Engineering	
NEHA BRAMHE	
7489597847	
	Date _will think
[19/01/24, 6:35:55 PM] anchal e.c: 3rd year 
	Electrical Engineering	Vaishnavi Inst. of Tech. & Science	
SULABH BISEN	7909711418	
Date _ will think
[19/01/24, 8:14:37 PM] Neha mam e.c: Aaj prospect nahi bane proper
[19/01/24, 8:30:37 PM] anup kumar ct: Computer Science & Engineering	Trinity Institute of Technology & Research	DIPTI TIWARI	7000370482	indrapuri 	20 Jan with friend
[19/01/24, 8:31:08 PM] anup kumar ct: Computer Science & Engineering	Trinity Institute of Technology & Research	GAURAV JHARBADE	6262853005		will think
[19/01/24, 9:50:50 PM] Lalita Sahu: Name of Student: lucky panthi
College name: sirt
Contact no: 6264594438
Year: 3RD
Expected Date of Visit: 27jan
MP nagar
[20/01/24, 11:52:16 AM] Lalita Sahu: Mam mere pass data ni h
[20/01/24, 12:10:45 PM] Hafsa.: Will go at evening
[20/01/24, 12:23:02 PM] naresh e.c: Name :- Kamal Nayan 
Number: - 8521751477
College: - sirt 
Expected date of visit: -  25 jan
[20/01/24, 12:29:58 PM] Neha mam e.c: @918310058018 jlu vale ko bhi bula lo
[20/01/24, 12:30:39 PM] naresh e.c: Bol diya tha kl hi mam ajayega aj
[20/01/24, 12:35:53 PM] annu❤️: Information Technology
Lakshmi Narain College of Technology	
SAHARSH BHAVE
9752598333	
Will Come 	In February 
4th year
[20/01/24, 12:52:32 PM] suman coding: Name of Student: Sarthak Gupta 
College name: TIT
Contact no: 9171858388
Branch: information technology  
Expected Date of Visit: 24 January indrapuri
[20/01/24, 12:59:20 PM] ~ Chauhan Shilpa: Name of Student: kanhaiya 
College name: lnct 
Contact no: 9685535132
Branch: cs
Year: 2ND 
Expected Date of Visit: after exam
[20/01/24, 1:14:14 PM] suman coding: Name of Student: Riya maity
College name: TIT
Contact no: 7067689852
Branch: information technology  
Expected Date of Visit: 11 February indrapuri
[20/01/24, 1:44:05 PM] ~ Deepali coding: Computer Science & Engineering	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	PRINCE RAJAK	7489230267	will come tomorrow 21 January
[20/01/24, 1:47:26 PM] arpana e.c: Lakshmi Narain College of Technology
	JATIN YADAV
4th year
old propect
	8963973254
will come 23 jan
[20/01/24, 1:49:57 PM] Neha mam e.c: @918310058018 2 baje class announce hai to check karna
[20/01/24, 1:51:27 PM] annu❤️: Coming today with +1  friend
[20/01/24, 3:58:08 PM] annu❤️: Information Technology
Sagar Institute of Research & Technology
SAMARTH JAIN
7869157972	
Will Come Indrapuri 	
In February 
4th year
[20/01/24, 3:59:08 PM] kasim k: Artificial Intelligence and Data Science	
J.N. College of Technology	
ADITYA SHARMA	
9131642324			
13 feb with devendra jatav (indrpuri )
[20/01/24, 4:27:02 PM] arpana e.c: Corporate Institute of Science & Technology	
ADITYA ANAND DWIWEDI
4th year
old propect
will come feb 1st week

	8200565528
[20/01/24, 4:28:32 PM] ~ Deepali coding: Computer Science & Engineering-Data Science	Technocrat Institute of Technology	ROHIT CHOUHAN	9301694759	will come 23 January indrapuri
[20/01/24, 4:35:50 PM] ~ Deepali coding: Computer Science & Engineering-Data Science	Technocrat Institute of Technology	VIKASH KUMAR	6202718351	will come 21 January indrapuri
[20/01/24, 4:38:46 PM] Hafsa.: Will come today with friend (Bedi)
[20/01/24, 4:40:02 PM] Hafsa.: Name of Student: Vikas Kumar Tekam 
College name: SAM
Contact no: 9302764529
Branch: CS
Year: 2nd year old prospect 
Expected Date of Visit: Will come after exam
[20/01/24, 5:21:53 PM] naresh e.c: Name :- Ketan pandey 
Number: - 7389130191
College: - lnct 
Expected date of visit: - 26 jan (Indrapuri)
[20/01/24, 6:00:32 PM] ~ Deepali coding: Computer Science & Engineering-Data Science	Technocrat Institute of Technology	ROSHAN KUMAR VERMA	9122477154	will come 21 January indrapuri
[20/01/24, 6:18:15 PM] arpana e.c: Name- Aman kumar
number-9835143159
college- tit college
2nd year 
Expected date- will come after 8 feb
[20/01/24, 6:18:44 PM] Hafsa.: Name of Student: Anuj Yadav 
College name: Hamidia College 
Contact no: 8827433223
Branch: B.Com
Expected Date of Visit: 25 Jan
[20/01/24, 6:24:45 PM] suman coding: Name of Student: saurav Kumar jha
College name: TIT
Contact no: 9693769318
Branch: information technology  
Expected Date of Visit:  February after exam indrapuri
[21/01/24, 12:19:52 PM] ~ Deepali coding: ‎This message was deleted.
[21/01/24, 12:20:09 PM] ~ Deepali coding: ‎This message was deleted.
[21/01/24, 12:20:22 PM] ~ Deepali coding: Computer Science & Engineering	Sagar Institute of Science & Technology & Research	RAVIRANJAN KUMAR	7544858399	will come after   25 January
[21/01/24, 12:31:34 PM] ~ Deepali coding: ‎This message was deleted.
[21/01/24, 12:32:02 PM] ~ Deepali coding: Electrical & Electronics Engineering	Technocrat Institute of Technology	ROHIT KUMAR SINGH	7256043517	will come 23- 24 January indrapuri + friend ( Rahul)
[21/01/24, 12:44:17 PM] ~ Deepali coding: Electronics & Communication Engineering	Sagar Institute of Research & Technology	VIJAY	9318300752	will come 24 January indrapuri
[21/01/24, 1:07:02 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology
PUSHPRAJ SINGH CHOUHAN
9009135431	
Will Come 	In February 
3rd year
[21/01/24, 1:19:13 PM] anchal e.c: 4th year 
	Computer Science & Engineering
	Radha Raman Institute of Technology & Science
	RAMPRIT KUMAR	6202050454
Date_	after 25 Jan
[21/01/24, 1:29:57 PM] Hafsa.: Name of Student: Aryan Kumar Jaiswal 
College name: OIST
Contact no: 7415315522
Branch: CS/AI/ML
Year: 2nd year 
Expected Date of Visit: Will come in Feb
[21/01/24, 3:08:00 PM] ~ Deepali coding: Will come with friend (Ravi)
[21/01/24, 3:32:17 PM] suman coding: Name of Student: Preeti 
College name: TIT
Contact no: 7049320142
Branch: information technology  
Expected Date of Visit : 23 January MP Nagar
[21/01/24, 3:36:45 PM] Hafsa.: Name of Student: Sapna Akhare
College name: Maharishi College 
Contact no: 9399735269
Branch: MCA
Expected Date of Visit: Will come in Feb after exam
[21/01/24, 3:48:56 PM] arpana e.c: Oriental Institute of Science & Technology
	DEEPANSHU TIWARI	7974801688	
3rd year
will come 23 jan
for inderpuri
[21/01/24, 3:57:08 PM] ~ Chauhan Shilpa: Name of Student: Ankit 
College name: tit
Contact no: 7987195545
Branch: cs
Expected Date of Visit: Will come in Feb after exam (indrapuri)
[21/01/24, 3:59:08 PM] ~ Chauhan Shilpa: Name of Student: aditya
College name: vns
Contact no: 7354437637
Branch: cs
Expected Date of Visit: 17 February ke baad
[21/01/24, 4:33:52 PM] arpana e.c: Oriental Institute of Science & Technology	HARSH KUMAR AMAN	7425830760
3rd year
	will come 28 jan 
for inderpuri
[21/01/24, 4:48:07 PM] suman coding: Name of Student: shudhir kumar singh 
College name: TIT
Contact no: 9631968793
Branch: information technology  
Year : 4 year 
Expected Date of Visit : 5 February MP Nagar
[21/01/24, 5:29:31 PM] Hafsa.: Name of Student: Abhay Sharma 
College name: OIST
Contact no: 6268576361
Branch: CS/AI/ML
Year: 2nd Year 
Expected Date of Visit: 25 Jan
[21/01/24, 5:46:38 PM] arpana e.c: Oriental Institute of Science & Technology
	HITARTH SHRIVASTAVA	8103573303	
3rd year
will come 28 jan
[21/01/24, 8:09:52 PM] ~ Chauhan Shilpa: [21/01, 7:44 pm] Jay Mahakal: Name of Student: Atul Tiwari + 10 frnds 
College name: tit
Contact no: 8269253010
Branch: cs
Year: 2nd Year 
Expected Date of Visit: 15 Feb ke baad
[21/01, 7:44 pm] Jay Mahakal: Rahul Mishra, Aditya Sen,Raj Patel BhumiSoni,Chetna, Vishwakarma, Divya Bharati, Tripathi, hariom, Vivek,
[23/01/24, 1:00:41 PM] kasim k: 3rd year
Information Technology	Oriental Institute of Science & Technology	
TANISHQ JAIN	
6394028743	
26 jan indrpuri
[23/01/24, 1:08:10 PM] anchal e.c: 4th year
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology
	ANIL RAGHUWANSHI	
7400632304	
Date _25 jan
[23/01/24, 1:30:41 PM] khushi e.c: Name of Student:  Anand diwedi 
College name: Bhopal Institute of Technology, Bangrasia
Contact no:7223801004
Expected Date of Visit: Will come in Feb after
[23/01/24, 1:53:20 PM] khushi e.c: Name of Student:- Anurag Tiwari
College name: Bhopal institute of technology bangrasia
Contact no: 6268576361
Branch:  electrical and electronics engineering 
Year: 3rd Year 
Expected Date of Visit: will think
[23/01/24, 2:44:06 PM] ~ Chauhan Shilpa: Name of Student: Rajan Sharma 
College name: IES
Contact no: 9153439219
Branch: CS 
Year: 2nd Year 
Expected Date of Visit: 28 January
[23/01/24, 3:13:03 PM] annu❤️: Electronics & Communication Engineering	
All Saints' College of Technology	
ABDUL WAJID
8406041457
Will Come in February
2nd Year 
Old prospect
[23/01/24, 3:17:23 PM] kasim k: 3rd year
Computer Science & Engineering	
Trinity Institute of Technology & Research	
SOHAN NAMDEV	
6261862632	
25 Jan (indrpuri)
[23/01/24, 3:20:46 PM] suman coding: Name of Student: Ashutosh rajput 
College name: LNCT 
Contact no: 6264353331
Branch: computer science & engineering 
Expected Date of Visit : after February indrapuri
[23/01/24, 3:29:12 PM] Hafsa.: Name of Student: Deepa Patel
College name: OIST
Contact no: 7999708292
Branch: CS/AI/ML
Year: 2nd Year 
Expected Date of Visit: Will come in Feb
[23/01/24, 3:45:58 PM] kasim k: 3rd year
Computer Science & Engineering	
Trinity Institute of Technology & Research	
YUVRAJ SINGH	
8651083549	
26 Jan
[23/01/24, 4:18:43 PM] kasim k: final year
Computer Science & Engineering	
Trinity Institute of Technology & Research	
DEEPAK KUMAR	
8218260463	
28 Jan
[23/01/24, 5:45:23 PM] Harsh sir tl: ‎kp sir added Harsh sir tl
[23/01/24, 5:48:24 PM] kp sir: Lalita 
Suman
[23/01/24, 5:48:29 PM] kp sir: Data dediya hai
[23/01/24, 5:48:52 PM] Neha mam e.c: Shilpa ko bhi chaiye
[23/01/24, 6:22:50 PM] arpana e.c: Oriental Institute of Science & Technology	KAILASH AGHAV	7354074266
3rd year
	will come 24 jan
for inderpuri
[23/01/24, 6:27:01 PM] Hafsa.: Name of Student: Rakhi Tembhare
College name: OIST
Contact no: 6267535633
Branch: CS/AI/ML
Year: 2nd Year 
Expected Date of Visit: Will come in Feb after exam
[23/01/24, 6:32:59 PM] khushi e.c: ‎This message was deleted.
[23/01/24, 6:33:47 PM] Neha mam e.c: 21 jan nikal chuki hai
[23/01/24, 6:34:13 PM] khushi e.c: Sorry mam
[23/01/24, 6:34:27 PM] Neha mam e.c: Dhyan se karo
[23/01/24, 6:36:01 PM] khushi e.c: Name of Student:- Aditi Thakur 
College name: Tit 
Contact no: 9770283773
Year: 4th Year 
Expected Date of Visit:   28 Jan indrapuri
[23/01/24, 6:45:31 PM] khushi e.c: College:- Technocrat Institute of Technology
Name :-	ADITYA KUMAR JHA
Contact :-	7970802136		 visiting date :- will think  indrapuri
[23/01/24, 6:48:20 PM] anchal e.c: 4th year
	Computer Science & Engineering
	Sagar Institute of Research & Technology	
RIDDHI GROVER	9589999704	
Date _24 jan
[23/01/24, 6:55:05 PM] Hafsa.: Name of Student: Koushal Silawat 
College name: TIT
Contact no: 9131421281
Branch: EC
Year: 3rd Year 
Expected Date of Visit: Will come in starting Feb
[23/01/24, 6:56:06 PM] Hafsa.: Name of Student: Harsh Chhatwani
College name: OIST
Contact no: 9827825265
Branch: CS/AI/ML
Year: 2nd Year 
Expected Date of Visit: Will come after exam
[23/01/24, 7:00:00 PM] khushi e.c: College name :- Technocrat Institute of Technology
Name :-	AMAN KUMAR	 contact :- 7856062531		   Expected date to visit :-will think in ndrapuri
[23/01/24, 7:16:15 PM] ~ Deepali coding: 167	Computer Science & Engineering-Data Science	Oriental College of Technology	SHIVAM TIWARI	9770868739	ringing 	will come Sunday / this week
[23/01/24, 7:17:19 PM] ~ Deepali coding: Computer Science & Engineering	Lakshmi Narain College of Technology Excellence	AMAN MAHRA	6264322382	ringing 	will come after some time
[24/01/24, 11:31:05 AM] Harsh sir tl: Good  morning Coding Thinker, Bhopal se harsh  baat kar raha hoon. Coding Thinker ek software development aur training institute hai. Main aap se kuch sawaal poochna chahta hoon aapki padhai ke baare mein:
1.	Aap study-wise kya kar rahe hain?
2.	Aap kis branch se hain?
3.	Aap kis college mein hain?
4.	Aap kaunse year mein hain?
Maine aapko coding languages aur placement-oriented courses ke baare mein call kiya tha. Kya aap kuch plan bana rahe hain, jaise ki full-stack web development, data science with Python, aur any other coding courses? Humare institute mein course content, projects, assignments, aur practice tests ke baare mein discuss karenge.
Ek aur important cheez hai non-technical skills, jo companies ke exams ke pehle crack karna padta hai. Iske liye hum CRT (Campus Recruitment Training) course provide karte hain, jisme aptitude, reasoning, verbal, non-verbal, aur soft skills ki classes hoti hain. Ye complimentary service hai aur iske liye koi extra charge nahi hota.
Hamare faculty members experienced IT professionals hain, jo multinational companies jaise Amazon, Google, TCS mein kaam kar chuke hain. Humare institute mein aapko company-oriented training milegi.
Hum aapko assistance bhi provide karte hain. Companies humare institute mein campus drives ke through aati hain, jisse aapko on-campus placement opportunities milte hain. Recent drives mein Webcrop (3.5 LPA), Egnito Technology, aur Encore ne 6.5 LPA se shuruwat ki hai.
Agar aap interested hain, toh aap humare center aakar details discuss kar sakte hain. Humare counsellors aur faculties aapko behtar tarah guide karenge. Aapko registration ke liye koi extra fees nahi deni hogi. Aap bata sakte hain ki aap Bhopal mein kahan rehte hain, taki hum aapko best tareeke se help kar sake.
Dhanyavaad, [Your Name] Coding Thinker, Bhopal
[24/01/24, 11:33:01 AM] Harsh sir tl: Certainly! Here's a refined version:

"Team, we'll be utilizing a similar pitch with a few minor tweaks. The rest of the details remain familiar to all of you.
[24/01/24, 11:35:33 AM] Harsh sir tl: If you come across any updates, please feel free to bring them to my attention for discussion. Additionally, please use your name in our communication. Thank you.
[24/01/24, 12:20:03 PM] Hafsa.: Name of Student: Masuque Ali
College name: REC
Contact no: 6205677242
Branch: CSR
Expected Date of Visit: 30 Jan
[24/01/24, 1:19:52 PM] anchal e.c: 4th year
Computer Science & Engineering	
Sagar Institute of Research & Technology
	PRIYANSH CHOUKSEY	
8878402600	
Date _will think
[24/01/24, 1:27:15 PM] kp sir: 👍
[24/01/24, 1:35:29 PM] suman coding: 4 year
Technocrats institute of technology & Science
Name - Jiyaul Haque
M.No. - 7764959901
Date - will think
[24/01/24, 1:36:46 PM] khushi e.c: Technocrat Institute of Technology	
Name:- BHAGVAN	 contact no:- 9993396050	
 Expected date of :- 	after 20 Feb in m.p nagar
[24/01/24, 1:47:13 PM] ~ Deepali coding: Computer Science & Engineering-Data Science	Oriental College of Technology	PREETAM AHIRWAR	7089791604	will come 30 January indrapuri
[24/01/24, 1:49:17 PM] Lalita Sahu: Name of Student:- payal sahu
College name: NRI
Contact no: 9179540256
Year: 3rd
Expected Date of Visit: 10feb
[24/01/24, 1:54:09 PM] ~ Deepali coding: Will come today with friend Syed ali
[24/01/24, 1:55:25 PM] kp sir: Mp nagar ya indrapuri
[24/01/24, 1:55:39 PM] ~ Deepali coding: Mp nagar sir
[24/01/24, 1:55:56 PM] kasim k: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
SHAHEED ANVAR ANSARI	
8269884282	
coming 24jan
[24/01/24, 1:56:50 PM] kp sir: Pls mentioned the branch where he will visit
[24/01/24, 1:57:06 PM] kasim k: chetak bridge
[24/01/24, 1:57:53 PM] Hafsa.: Coming today Chetak Bridge ‎<This message was edited>
[24/01/24, 3:10:05 PM] kasim k: + khushi coming today indrpuri
[24/01/24, 3:12:12 PM] Harsh sir tl: "Team,

I hope this message finds you well. As you know, our coding institute is dedicated to providing top-notch education with a guarantee of 100% placement assistance. We offer a diverse range of courses designed to not only enhance skills but also ensure successful placements for our students.

I'd like to discuss the best strategy for promoting our institute and conveying the value of our courses to potential students. Let's focus on highlighting the key aspects:

Placement Assistance: Emphasize our commitment to securing placements for our students. This sets us apart from other institutes and is a significant factor that potential students consider.

Course Variety: Showcase the variety of courses we offer. Explain how each course is tailored to equip students with the skills that are in high demand in the industry.

Success Stories: Share success stories of our past students who have not only completed the courses successfully but have also secured desirable placements. Real-world examples can be powerful motivators.

Industry-Relevant Content: Highlight that our courses are designed in collaboration with industry experts, ensuring that our students are learning the latest technologies and industry best practices.

Engagement with Employers: Mention any partnerships or collaborations we have with employers. This adds credibility to our placement assistance program.

Let's brainstorm on creative ways to communicate these points, whether through social media, targeted emails, or other channels. I encourage everyone to share ideas and work collaboratively to boost enrollment and continue to make a positive impact on our students' lives.

Thank you for your dedication and hard work.

Best regards,
[HARSH VARDHAN SEN ]"
[24/01/24, 3:13:39 PM] ~ Deepali coding: Will come today indrapuri With ravi
[24/01/24, 3:15:28 PM] ~ Deepali coding: Will come 26 - 27 January
[24/01/24, 3:18:28 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	ABHISHEK KUSHWAHA	7489390042
3rd year
	will come 27 jan
chetak
[24/01/24, 3:27:25 PM] Lalita Sahu: Name of Student:- Dhananjay kumar
College name: IES
Contact no: 7367071572
Year: 3rd
Expected Date of Visit: 27jan
[24/01/24, 3:28:14 PM] ~ Deepali coding: Will come 25 January with friend nitin
[24/01/24, 3:36:35 PM] ~ Deepali coding: Name of Student:- Shruti Shrivastava
Branch : ec
College name: Oriental 
Contact no: 8269031915
Year: 4th year
Expected Date of Visit: 25 January chetak bridge
[24/01/24, 3:36:49 PM] Hafsa.: Name of Student: Mohammad Nadim 
College name: SIRT
Contact no: 8102506790
Branch: EE
Expected Date of Visit: 6 Feb
[24/01/24, 3:42:07 PM] anchal e.c: 3rd year
Computer Science & Engineering	
Technocrats Institute of Technology - Computer Science and Engineering	
PRADUMNA BAMRELE	
8103928524
Date_	will come feb
[24/01/24, 3:59:38 PM] khushi e.c: College 		:- Technocrats Institute of Technology [Excellence]	 
Name :- PRINCE KEWAT
Contact no:-9926901776		
Expected date :- will come in Indra puri    26  Jan
[24/01/24, 4:02:12 PM] ~ Chauhan Shilpa: Rahul Mishra+ 
7225857847
College - IS( CS)
Visit date -25 feb ke baad with friends
[24/01/24, 4:10:48 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	ANIL	
9301224043	
3rd year
will come 28 jan 
chetak
[24/01/24, 4:27:11 PM] annu❤️: Technocrats Institute of Technology & Science	
S. SNEHA	
8817146086	
Will Come Python 	
inform himself 
4th year
[24/01/24, 5:10:22 PM] ~ Chauhan Shilpa: Name-MOHD AYAZ ANSARI
College -Oriental College of Technology
Contact no:-		9926148156
Expected date :- will come feb
[24/01/24, 5:15:45 PM] suman coding: Name of Student: ayush jha
College name: TIT
Contact no: 7632026798
Branch: information technology 
Year: 2 year 
Expected Date of Visit: 11  February indrapuri
[24/01/24, 5:23:31 PM] ~ Deepali coding: 302	Computer Science & Engineering	Bansal Institute of Research, Technology & Science	POORVI SAINI	8319143889	will come 2 feb indrapuri
[24/01/24, 5:25:59 PM] ~ Deepali coding: Will come 28 January indrapuri
[24/01/24, 5:29:05 PM] ~ Deepali coding: Will come 6:30 pm indrapuri+ 1 friend mayuresh
[24/01/24, 5:30:32 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[24/01/24, 5:31:10 PM] khushi e.c: Will come 7 pm indrapuri 
+1 freind kundan
[24/01/24, 5:31:30 PM] ~ Chauhan Shilpa: Name:-NAVIN PATEL
College -Oriental College of Technology
Contact no:-		9179786603
Expected date :- 26 se 28 January ( mp nagar)
[24/01/24, 5:59:31 PM] kasim k: 3rd year
Mechanical Engineering	
Patel College of Science & Technology	
SHALENDRA KUMAR SAHU	7509110165	
29 Jan
chetak bridge
[24/01/24, 6:17:49 PM] Hafsa.: Name of Student: Om Singh
College name: OIST
Contact no: 7999416126
Branch: CS/AI/ML
Year: 2nd year 
Expected Date of Visit: 25 Jan
[24/01/24, 6:20:43 PM] Lalita Sahu: Name of Student:- rasid jamal
College name: IES
Contact no: 7070528759
Year: 3rd
Expected Date of Visit: will come feb
[24/01/24, 6:27:28 PM] suman coding: Name of Student: Prashant Chaudhary 
College name: TIT
Contact no: 9359324146
Branch: computer science & engineering 
Expected Date of Visit: 18  February indrapuri
[24/01/24, 6:28:16 PM] annu❤️: Sagar Institute of Science & Technology & Research	
ABHINAV PRATAP SINGH	
6268443531	
Will Come FSD	
5 February
4th Year
[24/01/24, 6:29:02 PM] arpana e.c: Name of Student: Deepak 
College name: LNCt 
Contact no:8252186202
Branch: computer science & engineering 
Expected Date of Visit:  25 jan indrapuri
[24/01/24, 6:29:57 PM] khushi e.c: Branch :- 	Mechanical Engineering	Girdhar Siksha Evam Samaj Kalyan Samiti Group of Inst. 
Name :- 	DURGESH YADAV	
 Contact number:- 8827383325		 Expected  visit date :-  will think    (m. p nagar )
[24/01/24, 6:30:54 PM] Neha mam e.c: @919131608639 sir aaj kuch enquiry pahunchi kya Indripuri inhone likhi to bahut hai
[24/01/24, 6:48:13 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	NIKHIL KHANGAR
3rd year	6268421580	
will think 27 jan
chetak
[24/01/24, 7:00:01 PM] Hafsa.: Name of Student: Akshay Deshmukh 
College name: OIST
Contact no: 8305370755
Branch: CS/AI/ML
Year: 2nd year 
Expected Date of Visit: Will come after exam in Feb
[24/01/24, 7:22:38 PM] ~ Chauhan Shilpa: Mp nagar ki location send kar dijiye
[24/01/24, 7:24:32 PM] anchal e.c: ‎Location: https://maps.google.com/?q=23.233191,77.440689
[24/01/24, 7:24:49 PM] kasim k: mp nagar , chetak bridge kasturba nagar near hero showroom, lalwani complex, coding thinker
[24/01/24, 7:25:30 PM] ~ Chauhan Shilpa: Name of Student: IQRA KHAN
College name: Scope College of Engineering
Contact no: 9691627767
Branch: Computer Science & Engineering
Year: 4th year 
Expected Date of Visit: 29 January
[24/01/24, 7:25:43 PM] ~ Chauhan Shilpa: Thanku sir
[24/01/24, 7:25:51 PM] ~ Chauhan Shilpa: Thanku mam
[24/01/24, 7:31:27 PM] annu❤️: Computer Science & Engineering	
SAM College of Engineering & Technology	
SHIVA DUBEY	
6264118267	
Will Come for friend	
In February 
4th Year
[24/01/24, 11:25:05 PM] kp sir: Haan 10 enquiry aai hai total
[25/01/24, 11:41:55 AM] Harsh sir tl: Good morning team,

I hope you are all doing well. As a team, we are well aware of our targets, and it is crucial that we achieve them. Let's stay focused and work with our full strength to reach our goals.

Thank you,
[ HARSH VARDHAN SEN ]
[25/01/24, 12:57:06 PM] ~ Chauhan Shilpa: Name of Student: KRISHNA GAHLOT
College name: Scope College of Engineering
Contact no: 9691627767
Branch: Computer Science & Engineering
Year: 4th year 
Expected Date of Visit: 10 February ke baad
[25/01/24, 1:02:12 PM] Lalita Sahu: Name of Student: Lakhan lal
College name:Bhopal institude of teachology bangrasia
Contact no: 7000082527
Branch:-Electrical & Electronics Engineering
Year: 4th year 
Expected Date of Visit: 26jan
[25/01/24, 1:17:27 PM] Hafsa.: Name of Student: Khushi Parihar 
College name: OIST
Contact no: 8319635761
Branch: CS/AI/ML
Year: 2nd year 
Expected Date of Visit: Will come after exam in Feb
[25/01/24, 1:25:22 PM] anchal e.c: 4th year 
	Computer Science & Engineering
	Technocrats Institute of Technology & Science	
MD SOHAIL ALAM	8578084975
Date	-25 jan will come indrapuri
[25/01/24, 2:50:15 PM] ~ Deepali coding: Computer Science & Engineering	Trinity Institute of Technology & Research	SHIFA NAAZ	9301932649 	after 30 interested indrapuri
[25/01/24, 3:21:44 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	RAJEEV KUSHWAH
	6260601008
3rd year
	will think 28 jan
chetak
[25/01/24, 3:27:32 PM] ~ Deepali coding: Computer Science & Engineering	NRI Institute of Research & Technology	SHUBHAM SINGH	9301549512	will come 28 January for( revisit		)		indrapuri
[25/01/24, 3:35:17 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	RAJENDRA AHIRWAR
	8461836729	
1st year
will come 27 jan
chetak
[25/01/24, 3:38:45 PM] khushi e.c: Branch :- Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:- Technocrat Institute of Technology
Name:- 	TAIYABA QUMER	
Contact:- 8969656975		 Expected date:- after 21 Feb  ( indrapuri)
[25/01/24, 3:41:48 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	RASHMI ATHIYA
	7389887772	
2nd year
will think after exam 18 feb
chetak
[25/01/24, 3:49:01 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology	
VISHAL KUMAR	7739302475	
Will Come 	Inform himself
4th year
[25/01/24, 4:55:03 PM] ~ Chauhan Shilpa: Name of Student: SHIVAM PARASTE
College name: Surabhi College of Engineering & Technology
Contact no: 8959098519
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: Will come in Feb
[25/01/24, 5:28:04 PM] kasim k: 4th year
Computer Science & Engineering	
Lakshmi Narain College of Technology	
HARSHAL PATEL	
7089474857	
27 Jan ( indrpuri )
[25/01/24, 5:48:13 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology	
NARENDRA SINGH YADAV	
9926305277	15 Group 
26-27 January
4th year
[25/01/24, 6:00:28 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology
RISHI RAJ SONI	
9926305277 
Will Come with Narendra
26-27 January
4th year
[25/01/24, 6:11:08 PM] Lalita Sahu: Name of Student:Deepika prajapati
College name:Technocrats Institute of Technology â€“ Advance
Contact no: 7566719090
Branch:-
Year: 4th year 
Expected Date of Visit: 29jan
[25/01/24, 6:25:38 PM] Harsh sir tl: ‎This message was deleted.
[25/01/24, 6:25:56 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology	
SUHAIL AHMAD ANSARI
7089571072	
Will Come 	27 January
4th Year
[25/01/24, 6:27:55 PM] Hafsa.: Name of Student: Raghav Dubey
College name: OIST
Contact no: 6261408835
Branch: CS/AI/ML
Year: 2nd year 
Expected Date of Visit: 15 Feb ‎<This message was edited>
[25/01/24, 6:39:29 PM] Harsh sir tl: ‎This message was deleted.
[25/01/24, 6:47:48 PM] Harsh sir tl: Hello, everyone! I am thrilled to announce that Coding Thinker is organizing an in-house competition to enhance your skills and assess your knowledge. We have exciting gifts for you, and the test will be tailored to your batch's courses. Participants will be required to create web pages, answer multiple-choice questions (MCQs), and take a pen-and-paper test. Prepare for a challenging and rewarding experience!

The competition is scheduled for this upcoming Saturday, January 27, 2024. The exact timing will be shared with you very soon, by tomorrow. Additionally, I'd like to highlight that this competition is mandatory, and it has been designed in a way that will aid you in your placements and future endeavors with upcoming companies.

Best of luck to all participants! If you have any further questions or require additional information, please feel free to reach out
[25/01/24, 8:39:59 PM] Harsh sir tl: Hello Durga,

I hope this message finds you well. We discussed your role in a meeting held this evening and reached a decision. Starting from tomorrow, your work location will be relocated from Coding Thinker Indrapuri to the Coding Thinkers branch in MP Nagar. Please be prepared to embark on this journey with us and strive to achieve your targets in the new location.

Best regards,
[HARSH VARDHAN SEN ]
[25/01/24, 9:02:34 PM] kasim k: 4th year 
Computer Science & Engineering	
Lakshmi Narain College of Technology	
LOVKESH HIMTHANI	
9425974170	
sehore sunday 28 jan
‎[25/01/24, 11:30:58 PM] Harsh sir tl: Coding Thinker Post4.jpg ‎document omitted
[25/01/24, 11:31:25 PM] Harsh sir tl: Kindly update it on your WhatsApp status
[26/01/24, 7:49:52 AM] anup kumar ct: ‎Neha mam e.c removed anup kumar ct
[26/01/24, 7:49:58 AM] naresh e.c: ‎Neha mam e.c removed naresh e.c
[26/01/24, 10:04:08 AM] Harsh sir tl: Good morning team,

Yesterday, I thoroughly reviewed all the sheets you uploaded, and I noticed a deviation in the way responses were coming compared to our usual standards. Let's collaborate to address this issue and work towards improving the quality of our output.

Moreover, Lalita and Suman, it has been a month since you joined our institute, and responses seem to be lacking. Please communicate any challenges you're facing so we can provide assistance. I encourage you to set and pursue your goals, and we're here to support you.

Let's strive for better results together.

Best regards,
[HARSH VARDHAN SEN]
[26/01/24, 11:30:25 AM] khushi e.c: Thankyou so much  sir
[26/01/24, 12:35:46 PM] annu❤️: Electronics & Communication Engineering	
Girdhar Siksha Evam Samaj Kalyan Samiti Group of Inst.	
SANJAY RAI	8120963270	
Will think 	inform himself Bhanu pratap 
4th year
[26/01/24, 1:06:27 PM] khushi e.c: Name of Student: Anubhav Pandey 
College name: TIT
Contact no : 9179448064
Expected Date of Visit : Will come today  26Jan (indrapuri) 3 pm
[26/01/24, 1:09:18 PM] khushi e.c: Will come today (indrapuri) after 7 pm
[26/01/24, 1:19:26 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	RISHABH SAHU
	9302889428
3rd year
	will come 28 jan
chetak
[26/01/24, 1:29:06 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	ROHIT SAHU
	6265262027	
3rd year
will come 28 jan
[26/01/24, 1:29:15 PM] arpana e.c: inderpuri
[26/01/24, 1:37:22 PM] ~ Chauhan Shilpa: Name of Student: ABHISHEK KUMAR
College name: Vidhyapeeth Institute of Science & Technology
Contact no: 9123126649
Branch: Mechanical Engineering
Year: 4th year 
Expected Date of Visit: 28 January visit ( Indore)
[26/01/24, 1:44:35 PM] khushi e.c: Branch :- 		Artificial Intelligence and Data Science	
College:- Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
Year:- 3rd year 
Name :- ANKITA RAJPUT	 contact number:- 7724010440			
Expected date:- after 1feb  m.p nagar
[26/01/24, 1:47:33 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	SATISH MALVIYA
	8103378100
3rd year
	will come 28 jan
chetak
[26/01/24, 3:05:13 PM] Hafsa.: Name of Student: Divyansh Singh
College name: TIT
Contact no: 8115571858
Branch: CS/AI/ML
Year: 2nd year 
Expected Date of Visit: Will come in Feb
[26/01/24, 3:13:41 PM] Lalita Sahu: Name of Student: mohommad nizamudeen
College name: TIT
Contact no: 9792940583
Branch: 
Year: 4th year 
Expected Date of Visit: 2feb
[26/01/24, 3:17:50 PM] ~ Deepali coding: ‎This message was deleted.
[26/01/24, 3:18:12 PM] ~ Deepali coding: Name of Student sapna Chauhan 
College name: SIRT
Contact no: 6265311391
Branch: ec
Year: 3 Rd year 
Expected Date of Visit: 30 January
[26/01/24, 3:25:21 PM] khushi e.c: Branch :;- Artificial Intelligence and Data Science 
College:- 	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	 Name :- MD ARHAN MANSOORI	
Contact:- 6281003819
Expected date:- 30 Jan m.p nagar
[26/01/24, 3:25:58 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	ROZY KHAN	9644373426
3rd year
	will come 27 jan
mp nagar
[26/01/24, 3:30:09 PM] ~ Deepali coding: Name of Student Shubham Singh 
College name: SIRT
Contact no: 9174317328
Branch: ec
Year: 3 Rd year 
Expected Date of Visit: 1 feb indrapuri
[26/01/24, 3:31:50 PM] Hafsa.: Name of Student: Deepak Lodha
College name: BIRT
Contact no: 8602287271
Year: 2nd year 
Expected Date of Visit: Will come after exam
[26/01/24, 3:34:05 PM] anchal e.c: Artificial Intelligence and Machine Learning	
Sagar Institute of Research & Technology	
ASHUTOSH SHRIVAS	
8827393823	
Date _after 16 February ‎<This message was edited>
[26/01/24, 3:35:33 PM] annu❤️: Computer Science & Information Technology
Sagar Institute of Research & Technology
SONAL MORE
9174687196	
Will Come Java 	
After exam 	20 February
2nd Year
[26/01/24, 3:52:50 PM] khushi e.c: Branch ;- 	Artificial Intelligence and Data Science	
College:- Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	 Name :- PRIYANSHU	 
contact number:- 7247422191	
Expected date :- 		after 8 Feb indrapuri
[26/01/24, 4:11:09 PM] Lalita Sahu: Name of Student: harshita pandey
College name: TIT
Contact no: 7697224992
Branch: cs
Year: 4th year 
Expected Date of Visit: 27 jan
[26/01/24, 4:15:10 PM] Lalita Sahu: Name of Student: annan hasan
College name: sagar institude
Contact no: 7772976228

Year: 4th year 
Expected Date of Visit: 26 jan
[26/01/24, 4:20:04 PM] khushi e.c: Will come after  18 Feb with 2 freinds nageshwar Soni and sahid
[26/01/24, 4:27:15 PM] suman coding: Name of Student: fulchand sirsam
College name: technocrats institute of technology and science 
Contact no: 9301074180
Expected Date of Visit: 26 February
[26/01/24, 4:27:27 PM] khushi e.c: With freind kashyap
[26/01/24, 4:49:35 PM] arpana e.c: 1.MD IRSHAD
2. ANAND CHOUHAN
3. LEELA DHAR 
4.AAYUSH SHIVHAR
VNS. college
 will come 28 jan 
Mo nagar
[26/01/24, 4:58:23 PM] ~ Chauhan Shilpa: Name of Student: ARBIND KUMAR PAL
College name: Vidhyapeeth Institute of Science & Technology
Contact no: 8103720391
Branch: Mechanical Engineering
Year: 4th year 
Expected Date of Visit: will think
[26/01/24, 5:48:50 PM] anchal e.c: Name of Student: Rajendra ahirwar 
College name: Bansal 
Contact no: 7000977338
Branch: CS
Year: 2nd year 
Expected Date of Visit: after exam 8 Feb
[26/01/24, 5:49:47 PM] khushi e.c: Name of Student: Atishay 
College name: Bansal 
Contact no: 7000977338
Branch: Civil
Year: 2nd year 
Expected Date of Visit:  will think
[26/01/24, 5:51:17 PM] anchal e.c: Name of Student: Vivek Patel 
College name: Bansal 
Contact no: 7999742522
Branch: CS
Year: 2nd year 
Expected Date of Visit: will think
[26/01/24, 5:58:58 PM] khushi e.c: Branch :- Artificial Intelligence and Data Science	
College:-Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
Name:- 	YASH DHAKAD
	Contact number:-7223860594	
Expected date :-		after 15 Feb
[26/01/24, 6:15:33 PM] khushi e.c: Branch :- 	Artificial Intelligence and Data Science	
College:- Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
Name:- YOGESH KHAPARIYE
Contact:- 	8839521606		
Expected date :- 	 will think
‎[26/01/24, 7:09:42 PM] kasim k: IMG_5772.HEIC ‎document omitted
‎[26/01/24, 7:09:42 PM] kasim k: IMG_5769.mov ‎document omitted
‎[26/01/24, 7:09:42 PM] kasim k: IMG_5767.HEIC ‎document omitted
‎[26/01/24, 7:09:42 PM] kasim k: IMG_5770.mov ‎document omitted
‎[26/01/24, 7:09:42 PM] kasim k: IMG_5768.HEIC ‎document omitted
‎[26/01/24, 7:09:42 PM] kasim k: IMG_5771.HEIC ‎document omitted
[27/01/24, 12:36:14 PM] khushi e.c: Will come today after 1 pm in (m.p nagar)
[27/01/24, 12:59:33 PM] Harsh sir tl: Subject: Urgent: Join Google Meet Immediately

Hello Team,

I hope this message finds you well. Urgently, I need each of you to join the virtual meeting at the following link: https://meet.google.com/jsw-phma-ejgon.

Your prompt participation is crucial, and I appreciate your immediate attention to this matter.

Best regards,

[ HARSH VARDHAN SEN ]
[ BDA ]
[27/01/24, 1:02:26 PM] Harsh sir tl: https://meet.google.com/jsw-phma-ejg
[27/01/24, 1:06:17 PM] arpana e.c: Bansal Institute of Science & Technology
	AAYUSHI MISHRA
	9119870671	
3rd year
	will think  28 jan
Mp nagar
[27/01/24, 1:36:08 PM] ~ Chauhan Shilpa: Name of Student: SHUBHAM KUMAR
College name: Lakshmi Narain College of Technology & Science
Contact no: 6205750452
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: 10 February (indrapuri)
[27/01/24, 1:37:04 PM] ~ Deepali coding: ‎This message was deleted.
[27/01/24, 1:39:01 PM] suman coding: Name of student: Kunal kalbande
College : name: oriental 
Contact no: 8359001485
Branch: computer science & engineering 
Year: 3 year 
Expected Date of Visit: 27  January indrapuri ( 6:00 pm)
[27/01/24, 1:58:01 PM] khushi e.c: Branch :- Artificial Intelligence and Data Science	
College :- Corporate Institute of Science & Technology	
Name:- ARSHAD AHMED
Contact:- 	9981833805		
Expected date :- 	 29 indrapuri
[27/01/24, 2:00:24 PM] khushi e.c: ‎This message was deleted.
[27/01/24, 3:04:44 PM] Hafsa.: Name of Student: Jatin Verma 
College name: SAM
Contact no: 8770270904
Year: 3rd year 
Expected Date of Visit: Will come in 1-2 days
[27/01/24, 3:18:30 PM] kasim k: 3rd year
Computer Science & Engineering	
Oriental College of Technology
NIHIR VERMA	
7999382002	 
try to visit 30jan
indrpuri
[27/01/24, 3:37:03 PM] ~ Deepali coding: 3RD	Computer Science & Engineering	VNS Group of Institutions	MD ARSHAD ALAM	7004628367	will come feb end
[27/01/24, 3:37:49 PM] ~ Deepali coding: FINAL 	MCA	Oriental Institute of Science & Technology	ABHISHEK KUMAR JHA	9162502255		will come 8-10 feb
[27/01/24, 3:41:34 PM] anchal e.c: 3rd year
Computer Science & Engineering	Technocrat Institute of Technology	PRANJAL SHARMA	9425477055	
Date_	after 10 feb will think
[27/01/24, 3:47:09 PM] khushi e.c: Name of Student:  Awinash Kumar Singh + Aryan Raj 
College name: jnct
Contact no:-+91 91420 19313
Year: 3rd year 
Expected Date of Visit: Will come  28 Jan  ( indrapuri )
[27/01/24, 4:11:23 PM] ~ Deepali coding: FINAL 	MCA	Technocrats Institute of Technology [Excellence]	PRANAY	9617504820 will come feb mid
[27/01/24, 4:16:17 PM] khushi e.c: Branch :- 	Artificial Intelligence and Data Science	
College:- Corporate Institute of Science & Technology	
Name :- GOVIND PATEL
Contact:-	7024295572		
Expected date :- 	1 Feb
[27/01/24, 4:19:47 PM] arpana e.c: Bansal Institute of Science & Technology	
AMAN DUBEY
	8305549202	
3rd  year
	will come 7 feb
mp nagar
[27/01/24, 4:20:09 PM] Lalita Sahu: Name of Student:  SUNEEL SONI
College name: Technocrat Institute of Technology
Contact no:-8770944940
Branch:- Information Technology
Year: 3rd year 
Expected Date of Visit: Will come  30 Jan  ( indrapuri )
[27/01/24, 4:21:11 PM] ~ Chauhan Shilpa: Name of Student: SNEHA SHARMA
College name: Lakshmi Narain College of Technology & Science
Contact no: 9335202762
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: will call February'
[27/01/24, 4:26:07 PM] annu❤️: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence
SOURABH GOUR
9893206451 
Will Come 	5 February	Chetak With brother 
3rd year
[27/01/24, 4:27:08 PM] anchal e.c: 3rd year
	Computer Science & Engineering	Technocrat Institute of Technology	PRANJAL HASWANI	7828858308		
Date _fsd  28 ind
[27/01/24, 4:27:25 PM] arpana e.c: Bansal Institute of Science & Technology
ANKIT MEENA
	8770453728	
3rd year
	will come 28 jan 
mp nagar
[27/01/24, 4:32:55 PM] Lalita Sahu: Name of Student: Rajendra thakur
College:-Sagar Institute of Research & Technology Excellence
Contact no:-9131998145
Branch:- computer science
Year: 3rd year 
Expected Date of Visit: 5feb mpnagar
[27/01/24, 4:33:25 PM] Hafsa.: Name of Student: Mohammad Irfan Alam 
College name: SAM
Contact no: 8294323713
Year: 3rd year 
Expected Date of Visit: Will come next week
[27/01/24, 4:50:15 PM] Lalita Sahu: Name of Student: sanjay singh
College:-Sagar Institute of Research & Technology Excellence
Contact no:-7489022687
Branch:- computer science
Year: 3rd year 
Expected Date of Visit: 31 jan indrapuri
[27/01/24, 5:06:13 PM] suman coding: Name of student: virendra verma
College name: Sagar institute of science & technology 
Contact no: 7489974102
Branch: computer science & engineering 
Year: 3 year 
Expected Date of Visit: 27  February
[27/01/24, 5:13:07 PM] ~ Deepali coding: 3RD	Computer Science & Engineering	Oriental College of Technology	SNEHA GUPTA	9343944598	indrapuri 	full stack 		will come 13 feb
[27/01/24, 5:26:31 PM] khushi e.c: Name of student:   Aman kumar +2 freinds Ajeet and Suman 
College name: tit  institute of science & technology 
Contact no: +91 78560 62531
Branch: computer science & engineering 
Year: 3 year 
Expected Date :- today 7 pm indrapuri
[27/01/24, 5:30:58 PM] khushi e.c: Will come today after 7pm  + kashyap
[27/01/24, 5:45:45 PM] Hafsa.: Name of Student : Ritik Kirar
College name: SAM
Contact no: 9131285286
Year: 3rd year 
Branch: CSE
Expected Date of Visit: 28 Jan
[27/01/24, 5:57:12 PM] annu❤️: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence	
VIVEK KUMAR YADAV
9065019441	
Will Come 	In February 
3rd year
[27/01/24, 6:09:06 PM] khushi e.c: Branch:-	Artificial Intelligence and Data Science
College:-	Corporate Institute of Science & Technology	SHAIJAL 
Name:-VISHWAKARMA
Contact:-	7067658554		
Expected date:-	after 5 Feb
[27/01/24, 6:11:40 PM] khushi e.c: Branch :-	Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:-Technocrats Institute of Technology [Excellence]
Name:- 	SAHIL GUPTA
Contact:-	9098286061			
Expected date:-after 2 Feb indrapuri
[27/01/24, 6:28:10 PM] ~ Chauhan Shilpa: Name of Student: VAISHNAVI NEMA
College name: Lakshmi Narain College of Technology & Science
Contact no: 7224096580
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: 28 January mp nagar (evening time) ‎<This message was edited>
[27/01/24, 6:53:13 PM] khushi e.c: Will come after 2 days
[27/01/24, 6:53:46 PM] kp sir: Deepali ke language main 2 registration hue hai indrapuri main
[27/01/24, 6:53:58 PM] ~ Deepali coding: Okh sir 👍🏻
[27/01/24, 6:54:27 PM] kp sir: Poore course main convert karna Hai, Data Science main
[27/01/24, 6:54:45 PM] ~ Deepali coding: Sir ho jayega thode din me
[27/01/24, 6:54:55 PM] ~ Deepali coding: Interested hai dono pure course ke liye
[27/01/24, 7:05:50 PM] ~ Chauhan Shilpa: Name of Student: VIJAY BHOYAR
College name: Lakshmi Narain College of Technology & Science
Contact no: 6269571549
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit:   8 Feb
‎[28/01/24, 12:28:54 AM] Neha mam e.c: IMG_4873.MP4 ‎document omitted
[28/01/24, 4:03:35 AM] Harsh sir tl: Hello team,

I want to express my sincere appreciation to each member. I recognize the hard work you're putting in, and I'm confident that together we'll achieve our targets remarkably. Thank you so much, team.

Best regards,
[HARSH VARDHAN]
[28/01/24, 4:03:54 AM] Harsh sir tl: Anchal, Mahi, and Deepali are kindly requested to visit the Indrapuri branch. Thank you. ‎<This message was edited>
[28/01/24, 12:38:00 PM] arpana e.c: coming today inderpuri ..at evening
[28/01/24, 12:39:58 PM] Harsh sir tl: Team kitni der lagegi
[28/01/24, 12:43:23 PM] arpana e.c: Bansal Institute of Science & Technology
	DHRUV SAHU	9302917691 
3rd year
	will think to come  after 31 jan
Mp nagar
[28/01/24, 12:44:06 PM] arpana e.c: we are in office ..in mp nagar
[28/01/24, 1:02:59 PM] kasim k: 10 min sir  nikal gye yaha se
[28/01/24, 1:03:18 PM] Neha mam e.c: Aaj kissi ke prospect nahi ban rahe hai kya
[28/01/24, 1:04:09 PM] Neha mam e.c: Konse data par kaaam kar rahe ho
[28/01/24, 1:04:25 PM] kasim k: 3rd year
[28/01/24, 1:04:46 PM] ~ Chauhan Shilpa: 3rd year par mam
[28/01/24, 1:05:13 PM] Neha mam e.c: Aaj koi prospect nahi bhej raha hai aaj ban nahi rahe kya
[28/01/24, 1:05:23 PM] ~ Chauhan Shilpa: Electrical & Electronics Engineering
[28/01/24, 1:05:35 PM] ~ Chauhan Shilpa: Ka data hai
[28/01/24, 1:05:54 PM] ~ Chauhan Shilpa: Not interested ja rahe hai call
[28/01/24, 1:06:11 PM] arpana e.c: not anwser  jaa rhe h abhi
[28/01/24, 1:15:16 PM] Lalita Sahu: Name of Student: vijay sharma
College:-Sagar Institute of Research & Technology Excellence
Contact no:7354178073
Branch:- computer science
Year: 3rd year 
Expected Date of Visit: will think
[28/01/24, 1:39:08 PM] annu❤️: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence
ANU JHA	
8840003726	
Will Come DSP
20 February
3rd year
[28/01/24, 1:45:38 PM] ~ Deepali coding: 3RD	Computer Science & Engineering	Technocrats Institute of Technology - Computer Science and Engineering	ANIRUDH BADKUR	7987325854		will come next week
[28/01/24, 1:47:08 PM] anchal e.c: Coming today chetak
[28/01/24, 1:49:58 PM] anchal e.c: Will come indrapuri today
[28/01/24, 2:03:50 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
UJJWAL RAI	
9570580514	
Date_	not confirm date to visit
[28/01/24, 2:52:05 PM] Harsh sir tl: Team, have you all returned to the office after lunch?
[28/01/24, 3:05:09 PM] arpana e.c: Bansal Institute of Science & Technology	DURGESH
 RAGHUWANSHI	9131789397	
3rd year
will come 4 feb
mp nagar
[28/01/24, 3:09:44 PM] kasim k: yes sir
[28/01/24, 3:26:34 PM] ~ Deepali coding: 3RD	Computer Science & Engineering	Technocrats Institute of Technology - Computer Science and Engineering	DHARMENDER SINGH	6397208339	mp nagar 	will come 2 feb
[28/01/24, 3:30:15 PM] annu❤️: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence
SATYAJIT ROY
6296441797	
Will Come CRT	
20 February
3rd year
[28/01/24, 3:32:08 PM] ~ Deepali coding: 3RD	Electronics & Communication Engineering	Technocrat Institute of Technology	ABHISHEK KUMAR	8340185618	Indrapuri			will come 28 January
[28/01/24, 3:43:12 PM] kasim k: 3rd year
Computer Science & Engineering	
Bansal Institute of Research & Technology	
KHUSHI CHOURASIA	
6266041214	
30 Jan
[28/01/24, 4:02:57 PM] arpana e.c: Bansal Institute of Science & Technology	
NAINA BISWAS
	6267742289	
3rd year
will come  31 jan
inderpuri
[28/01/24, 4:13:13 PM] arpana e.c: Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
ADYA PIPERSANIYA
	7224036096	
3rd year
will come 30 jan
Inderpuri
[28/01/24, 4:27:19 PM] arpana e.c: Patel College of Science & Technology
	SANJEET KUMAR
	9297616440	
3rd year
	will think
[28/01/24, 4:31:34 PM] Neha mam e.c: @919303330545 @916260753147 next Sunday tak aap dono ko admission karna nahi to Monday se nahi aana hai aapko
[28/01/24, 5:26:16 PM] annu❤️: Computer Science & Engineering	
Radha Raman Institute of Technology & Science
RAJ PRAKASH CHOUDHARY
9679385644	
Will Come DSA	
18 February
3rd year
[28/01/24, 5:31:53 PM] ~ Deepali coding: 3RD	Electronics & Communication Engineering	Lakshmi Narain College of Technology	ABHISHEK SAHU	8461801896	will come feb first week for revisit indrapuri
[28/01/24, 5:32:19 PM] ~ Chauhan Shilpa: Name of Student: KUNAL KALBANDE
College name: Oriental College of Technology
Contact no: 8359001485
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit:   February last
[28/01/24, 5:40:45 PM] kasim k: 3rd year
Computer Science & Engineering	
Bansal Institute of Research & Technology	
RAJENDRA SAHU	
6260976841	
feb 13
[28/01/24, 5:45:48 PM] ~ Deepali coding: 4TH	Computer Science & Engineering	NRI Institute of Information Science & Technology	NIKIL VISHWAKARMA		9302069187 will come mid Feb
[28/01/24, 5:51:55 PM] kasim k: 3rd year
Computer Science & Engineering	
Bansal Institute of Research & Technology	
RANGNATH SINGH	
7489301366	
9feb indrpuri
[28/01/24, 6:06:52 PM] annu❤️: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	JAI PARKASH
8083362206	
Will Come DSP	
20 February
3rd Year
[28/01/24, 6:13:23 PM] suman coding: Name of Student: mahima majumdar 
College name: SAM 
Contact no: 9794173572
Branch: artificial intelligence and data science 
Year: 3ed year 
Expected Date of Visit: will think
[28/01/24, 6:14:41 PM] Neha mam e.c: Morning se aap ek hi prospect bana pai ho
[28/01/24, 6:20:17 PM] ~ Deepali coding: 3RD	Computer Science & Engineering	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	ASHISH KATARE	9329105988will come 2 feb
[28/01/24, 6:21:35 PM] suman coding: Name of Student: devender 
College name: SAM 
Contact no: 8959381468
Branch: electrical and electronics engineering 
Year: 3ed year 
Expected Date of Visit: will think
[28/01/24, 6:24:55 PM] kasim k: ‎You deleted this message.
[28/01/24, 6:25:02 PM] kasim k: ‎You deleted this message.
[28/01/24, 6:25:30 PM] kasim k: 3rd year
Computer Science & Engineering	
Bansal Institute of Research & Technology	
ROSHAN SHINDE	
9302002950
1feb
 (chetak bridge)
[28/01/24, 6:25:51 PM] anchal e.c: With 3 frds
[28/01/24, 6:31:33 PM] arpana e.c: Patel College of Science & Technology
	SUJEET BAMHORE	8817234063	
2nd year
	will come 4 feb
mp nagar
[28/01/24, 6:32:25 PM] anchal e.c: Artificial Intelligence and Data Science	Corporate Institute of Science & Technology	
NIKHIL PATEL
	9301872962			
Not confirm date to visit
[28/01/24, 6:40:32 PM] ~ Deepali coding: ‎This message was deleted.
[28/01/24, 6:40:54 PM] ~ Deepali coding: 3RD	Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	GAUTAM VERMA	7247427512 will come 		Feb 5
[28/01/24, 6:49:16 PM] suman coding: Name of Student: akash meena
College name: SAM 
Contact no: 6262881427
Branch: artificial intelligence and data science 
Year: 3ed year 
Expected Date of Visit: 30 January indrapuri
[28/01/24, 6:50:59 PM] arpana e.c: Patel College of Science & Technology
	SUYASH KUMAR
	8986382660	
3rd year
	will come 10 feb
mp nagar
[28/01/24, 7:06:46 PM] suman coding: Name of Student: ankul vishwakarma 
College name: SAM 
Contact no: 9327208948
Branch: artificial intelligence and data science 
Year: 3ed year 
Expected Date of Visit: 16 February indrapuri
[28/01/24, 7:09:16 PM] ~ Chauhan Shilpa: Name of Student: PANKAJ KUMAR
College name: Surabhi College of Engineering & Technology
Contact no: 7470613560
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: 8 feb
[28/01/24, 7:12:53 PM] ~ Chauhan Shilpa: Name of Student: LADE DEVENDRA NANDKISHOR
College name: Surabhi College of Engineering & Technology
Contact no: 7499865897
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: 25 feb ‎<This message was edited>
[28/01/24, 7:16:14 PM] ~ Chauhan Shilpa: Name of Student: SUNNY KUMAR
College name: Technocrats Institute of Technology - Computer Science and Engineering
Contact no: 6204100773
Branch: Computer Science & Engineering
Year: 3ed year 
Expected Date of Visit: will think
[28/01/24, 7:35:15 PM] kp sir: Note : sabhi caller Dhyanesh Rakhee apan ko placement cell pitch karnaa hai additional support main but *Training* *placement* officers ka name *disclose* nahi karnaa , Aur nahi kisi *trainer* ke *naam* *pitch* *karnaa* hai remember this point .
Harsh Sir pls take care of that
[28/01/24, 7:36:31 PM] kp sir: Kal data analytics ki class 6.45PM par announce Karni Hai agar koi aapse poochtaa hai toh
[28/01/24, 7:43:06 PM] kp sir: Tomorrow class timing will of Java +DSA fsd2,3,4 wallo ki class 12PM PAR ANNOUNCE HAI ,AGAR KOI STUDENTS POCHTAA HAI
[28/01/24, 8:01:41 PM] annu❤️: Ok sir
[28/01/24, 9:52:11 PM] Harsh sir tl: Good evening team,

I hope you're all doing well. I want to express my appreciation for the hard work each of you is putting in. Special kudos to Suman – your performance has notably improved after the review meeting. You all are amazing, keep up the hard work. Together, we will achieve great exposure, and our institute will continue to grow.

Best regards,
[HARSH VARDHAN]
[28/01/24, 9:53:13 PM] kp sir: 👍👍
[29/01/24, 10:57:38 AM] kasim k: MCA
Bansal Institute of Research & Technology	
shivam thakre
9522178737
coming today
 (chetak bridge)
[29/01/24, 11:01:42 AM] Harsh sir tl: Very well done kasim keep grinding like this
[29/01/24, 12:08:21 PM] Lalita Sahu: Name of Student: Priyanshu bhagat
College name: Technocrat Institute of Technology
Contact no: 7079707930
Branch: information technology
Year: 3ed year 
Expected Date of Visit: 1feb
[29/01/24, 12:34:31 PM] ~ Deepali coding: Name of Student: Ranjana
College name: VNS
Contact no: 9826077093
Branch: cs
Year: 4 th year
Expected Date of Visit: 1feb
[29/01/24, 12:34:52 PM] Neha mam e.c: Tum aayi ho kya
[29/01/24, 12:35:05 PM] ~ Deepali coding: Yes mam
[29/01/24, 12:35:16 PM] ~ Deepali coding: Mujhe kal kam hai kal off lungi me
[29/01/24, 12:39:02 PM] khushi e.c: Name of Student:  Amit dhakad 
College name: corporate college 
Contact no: 9770614708
Branch: AI-DS
Year: 3rd year
Expected Date of Visit:  30 Jan ( m.p nagar )
[29/01/24, 12:46:58 PM] Lalita Sahu: Name of Student: Riteek doble
College name: Technocrat Institute of Technology
Contact no: 8103941424
Branch: information technology
Year: 3rd year 
Expected Date of Visit: 4feb
[29/01/24, 12:48:11 PM] Hafsa.: Name of Student : Anil Rathore 
College name: SIRT 
Contact no: 8959463595
Year: 3rd year 
Branch: CSE
Expected Date of Visit: 30 Jan ( Indrapuri ) ‎<This message was edited>
[29/01/24, 12:48:50 PM] ~ Chauhan Shilpa: Name of Student: HRITIK SAINI
College name: SAM College of Engineering & Technology
Contact no: 7724045783
Branch: Artificial Intelligence and Data Science
Year: 3ed year 
Expected Date of Visit: 31 January (indrapuri)
[29/01/24, 12:51:48 PM] khushi e.c: Branch :- 		Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:- Technocrats Institute of Technology [Excellence]	
Name:-SIDDHARTH KARAN	
Contact number:- 7692939637		
Expected date :- 	will think
[29/01/24, 12:52:41 PM] Harsh sir tl: Good work team keep working hard
[29/01/24, 12:53:40 PM] kasim k: 3rd year
Computer Science & Engineering	
SAM College of Engineering & Technology	
CHETAN CHOUDHARY	8815069845	
6Feb
[29/01/24, 1:02:50 PM] ~ Chauhan Shilpa: Name of Student: DIVAKAR SINGH
College name: SAM College of Engineering & Technology
Contact no: 6260816705
Branch: Artificial Intelligence and Data Science
Year: 3ed year 
Expected Date of Visit: will think ( data analytics)
[29/01/24, 1:09:59 PM] khushi e.c: Branch:- 		Artificial Intelligence and Data Science
College:- 	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
Name:- 	SAGAR
Contact:-	6265966375	
Expected date :- 		will think
[29/01/24, 1:19:55 PM] annu❤️: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence
MOHAMMAD AMAN
7354287363
Will Come After 22 February
3rd Year
[29/01/24, 1:31:52 PM] khushi e.c: Branch:- Computer Science & Engineering-Artificial Intelligence and Machine Learning	 
College:- Technocrats Institute of Technology [Excellence]	
Name :- SHUBHAM SINGH	
Contact:- 6261552949	
Expected date:- 		after 12 Feb
[29/01/24, 1:39:59 PM] khushi e.c: Will come today indrapuri in 20 minutes
[29/01/24, 2:03:44 PM] ~ Chauhan Shilpa: Visit done 👍
[29/01/24, 2:08:24 PM] Neha mam e.c: 2nd ko aapne yaha campus aa raha hai
[29/01/24, 2:11:04 PM] khushi e.c: Ok mam
[29/01/24, 3:08:03 PM] Lalita Sahu: Name of Student: tarun kumar 
College name: Technocrat Institute of Technology
Contact no: 9754228305
Branch: information technology
Year: 3rd year 
Expected Date of Visit: 30jan
(CRT)
[29/01/24, 3:26:00 PM] kp sir: Stuti data science main kiskaa admission tha
[29/01/24, 3:28:36 PM] Neha mam e.c: Kya hua
[29/01/24, 3:28:38 PM] annu❤️: Mera tha sir
[29/01/24, 3:29:13 PM] kp sir: Kuch nahi maam ,Ek kaam tha
[29/01/24, 3:29:18 PM] kp sir: Ok
[29/01/24, 3:32:10 PM] kp sir: Anushree give me the number in my WhatsUp
[29/01/24, 3:33:38 PM] annu❤️: Ok sir
[29/01/24, 4:05:13 PM] ‎You: ‎You pinned a message
[29/01/24, 4:43:59 PM] ~ Deepali coding: Electrical & Electronics Engineering	Technocrat Institute of Technology	MD SHAHID ANWAR	9162053789	 	will come 31 January indrapuri
[29/01/24, 4:52:07 PM] Lalita Sahu: Name of Student: Anurag asati
College name: Technocrat Institute of Technology
Contact no: 7024789497
Branch: Computer Science & Engineering-Artificial Intelligence and Machine Learning
Year: 3rd year 
Expected Date of Visit: 5feb
[29/01/24, 5:10:38 PM] arpana e.c: coming today withinh 10mnt
[29/01/24, 5:12:07 PM] arpana e.c: mp nagar
[29/01/24, 5:42:49 PM] annu❤️: Computer Science & Engineering	
SAM College of Engineering & Technology
PARMANANAD DAS
9128252272	
Will Come CRT	6 February

Computer Science & Engineering	
VNS Group of Institutions	
SUDAMA AHIRWAR	
8461873234	
Will Come FSD 6 February
[29/01/24, 6:01:28 PM] Lalita Sahu: Name of Student: shubham pandey
College name: Technocrat Institute of Technology
Contact no: 7970955502
Branch: information technology
Year: 3rd year 
Expected Date of Visit: will think 11feb(crt)
[29/01/24, 6:17:11 PM] Hafsa.: Name :- Ajay singh lodhi 
Number: - 8817717164
College: - SIRT
Branch :-AI/DS
Expected date of visit: - After exam in Feb
[29/01/24, 6:34:29 PM] Hafsa.: Name: Sameet Arya
Number: 9171623785
College: UIT
Expected date of Visit: 31 Jan
[29/01/24, 7:00:35 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Trinity Institute of Technology & Research
 Name:- 	NILESH DASHRIYA	
Contact:- 9174950761		m.p nagar 3 Jan
[29/01/24, 7:15:00 PM] annu❤️: Electronics & Communication Engineering	
Sagar Institute of Science Technology & Engineering	
UDAY KUMAR IRPACHI	
9131596106	
Will come Java
20 February
Old prospect
[29/01/24, 7:28:46 PM] Neha mam e.c: @916260753147 Kya scene hai aapka
[29/01/24, 7:30:10 PM] Lalita Sahu: Mem me  mere side se kosis kr rhi hu
[29/01/24, 7:30:31 PM] Neha mam e.c: Aapki koshish dikh nahi rahi
[29/01/24, 7:30:52 PM] Lalita Sahu: I know maam
[29/01/24, 7:31:27 PM] Neha mam e.c: To bina admission ke baar baar ye kehane se me koshish kar rahi hu kaam kon chalega
[29/01/24, 7:31:34 PM] Lalita Sahu: Me efforts lga rhi hu but.
[29/01/24, 7:31:53 PM] Neha mam e.c: Me kissi ko aapke efforts nahi dikh rahe
[29/01/24, 7:32:18 PM] Neha mam e.c: Same baat naye naye words me kehane se kaam nahi chalta hai
[29/01/24, 7:32:41 PM] khushi e.c: Branch :-Computer Science & Engineering
College:- 	Trinity Institute of Technology & Research	
Name:- PRIYANKA BALHORE	
Contact,:- 8319700317	
Expected date :- 	2 Feb indrapuri
[30/01/24, 12:05:57 PM] Harsh sir tl: Team meeting in 5 minutes
[30/01/24, 12:10:44 PM] Harsh sir tl: Only indrapuri team will join
[30/01/24, 12:10:47 PM] Harsh sir tl: Harsh vardhan sen has invited you to join a video meeting on Google Meet.

Join the meeting: https://meet.google.com/soz-ocys-vkq
[30/01/24, 12:47:35 PM] khushi e.c: Branch :- Computer Science & Engineering
College:-
	Trinity Institute of Technology & Research
Name:-	SURENDRA DANGI	
Contact:-6261373050	
Expected date:- 	3 Feb   indrapuri
[30/01/24, 12:58:53 PM] arpana e.c: Patel College of Science & Technology
	TEENA
	8450067085	
3rd year
	will come 3 feb
Mp nagar
[30/01/24, 1:08:04 PM] arpana e.c: try to come today after  6 pm
[30/01/24, 1:11:11 PM] suman coding: Name of Student: hritik saini 
College name: SAM
Contact no: 7724045783
Branch: artificial intelligence and data science 
Year: 3rd year 
Expected Date of Visit: 30 January indrapuri 8 pm
[30/01/24, 1:29:37 PM] suman coding: Name of Student: kavita raikwar
College name: JNCT
Contact no: 6260509655
Branch: artificial intelligence and data science 
Year: 3rd year 
Expected Date of Visit: 3 February MP Nagar
[30/01/24, 1:31:27 PM] anchal e.c: 4th year 
Electrical & Electronics Engineering	Bhopal Institute of Technology, Bangrasia	
ABHISHEK TRIPATHI	
9109858061
Date_	will think
[30/01/24, 1:44:11 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
Name:-	SHOBHIT SHRIVASTAVA
Contact:-	9691654319
Expected date		2 Feb m.p nagar
[30/01/24, 1:44:59 PM] arpana e.c: Name :- Ridhima dubey 
Number: - 7067459831
College: - radha raman 
Branch :- cs e
Expected date of visit: - after exam 12 feb
[30/01/24, 1:45:51 PM] Lalita Sahu: Name of Student: SHIVAM kumar
College name: Technocrat Institute of Technology
Contact no: 7061355187
Branch: information technology
Year: 3rd year 
Expected Date of Visit:13feb(crt)
[30/01/24, 1:51:21 PM] arpana e.c: Name :- vishal 
Number: - 9625330997
College :- radha raman 
Branch :- cs 
2nd year 
Expected date of visit :- After exam 18 feb
[30/01/24, 1:55:06 PM] ~ Chauhan Shilpa: Name of Student: ANKIT CHOURASIYA
College name: SAM College of Engineering & Technology
Contact no: 8103814749
Branch: Artificial Intelligence and Data Science
Year: 3rd year 
Expected Date of Visit: February first week
[30/01/24, 1:56:56 PM] Hafsa.: Name :- Jagdeesh Malviya 
Number: - 8878691622
College: - Trinity College 
Branch :-CSE
Year: 3rd Yr
Expected date of visit: - Will contact if plan
[30/01/24, 3:08:51 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology	
SANJOG PAGARE	7024350956	
Will Come FSD	2 February
3rd Year
[30/01/24, 3:29:48 PM] suman coding: Name of Student: Ankit mewada 
College name: JNCT
Contact no: 8817458645
Branch: artificial intelligence and data machine learning 
Year: 3rd year 
Expected Date of Visit: will think
[30/01/24, 3:40:48 PM] khushi e.c: Name of Student: Sachin vishwakarma 
College name: corporate college 
Contact no: 9098174286
Branch: artificial intelligence and data  science 
Year: 3rd year 
Expected Date of Visit: 30 Jan m.p nagar
[30/01/24, 4:03:52 PM] Lalita Sahu: Name of Student: PRARTHANA VISHWAKARMA
College name: IES college
Contact no: 9340891415
Year: 3rd year 
Expected Date of Visit:will think mid feb
[30/01/24, 4:20:00 PM] khushi e.c: +2 friends Farhan Khan and Vivek Kushwaha 6 pm  (m.p nagar )
[30/01/24, 4:24:00 PM] khushi e.c: Will come today 7:30 pm (indrapuri)
[30/01/24, 4:30:17 PM] ~ Chauhan Shilpa: Name of Student: KISHAN VISHWAKARMA
College name: Lakshmi Narain College of Technology & Science
Contact no: 8085421529
Branch: Electronics & Communication Engineering
Year: 3ed year 
Expected Date of Visit: 5 February (indrapuri)
[30/01/24, 4:41:10 PM] khushi e.c: Branch :- Computer Science & Engineering 
College:-	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
Name:-	SOURABH KUSHWAHA
Contact:-	9907165439		
Expected date :- ,will think (m.p nagar )
[30/01/24, 5:38:25 PM] khushi e.c: Branch :-Computer Science & Engineering	
College:-Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
 Name :- 	TARUN TEKAM
Contact,:- 	9754309127		
Expected date. :- 2 Feb. m.p nagar
[30/01/24, 5:42:05 PM] khushi e.c: Branch:- Computer Science & Engineering	
College:-Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name :- VIPIN KUSHWAH
Contact:-	6265880793	
Expected date :-	Feb 2
[30/01/24, 5:45:10 PM] ~ Chauhan Shilpa: Name of Student: Aman sanidhya 
Contact no: 8770930203
Branch: aiml 
Year: mca
Expected Date of Visit: March
[30/01/24, 5:54:50 PM] khushi e.c: Branch :- Computer Science & Engineering	 
College:-Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name :-VIVEK GOUR
Contact number:-	6265863698		
Expected date:-31 Jan m.p nagar
[30/01/24, 5:56:59 PM] Lalita Sahu: Name of Student: SOURABH YADAV
College name: Vaishnavi Inst. of Tech. & Science
Contact no: 7067607945
Year: 3rd year 
Expected Date of Visit:22feb
[30/01/24, 6:09:29 PM] khushi e.c: Will come tomorrow 1 pm
[30/01/24, 6:16:19 PM] Lalita Sahu: ‎This message was deleted.
[30/01/24, 6:17:00 PM] Lalita Sahu: Name of Student: SHAMIKSHA
College name: Technocrat Institute of Technology
Contact no: 9129351971
Branch: information technology
Year: 3rd year 
Expected Date of Visit:feb5
[30/01/24, 6:40:19 PM] ~ Chauhan Shilpa: Name of Student: rishabh Gupta 
Contact no: 7581863455
Expected Date of Visit: today visit indrapuri
[30/01/24, 6:47:24 PM] Lalita Sahu: Name of Student:MAHIMA
College name: Bansal collage
Contact no: 7987519751
Year: 2ndyear 
Expected Date of Visit:not a confirm date 
(Refrence number)
[30/01/24, 6:50:11 PM] Neha mam e.c: Tumpar konsa reference aa gya
[30/01/24, 6:50:13 PM] Neha mam e.c: Hai
[30/01/24, 6:51:14 PM] Lalita Sahu: Mam student ka khud call aaya tha wo bol rhi ki number  kisi ne number diya h
[30/01/24, 6:52:07 PM] arpana e.c: Patel College of Science & Technology
	UPENDRA KUMAR
 SAHU	7047817912
will come 4 feb
mp nagar
[30/01/24, 6:54:54 PM] ~ Chauhan Shilpa: Name of Student: ayush tank 
Contact no: 8959491481
College:- jawaharlal nehru college
Expected Date of Visit: 5 February ke baad
[30/01/24, 7:02:04 PM] Neha mam e.c: Ok
[30/01/24, 7:04:13 PM] ~ Chauhan Shilpa: Name of Student: ateet toppo
Contact no: 8819092838
College:- sirt(MBA)
Expected Date of Visit: 10  February
[30/01/24, 7:07:31 PM] Hafsa.: Name :- Ankush Kumar 
Number: - 8252597656
College: - Millennium College 
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - 6 Feb
[30/01/24, 7:10:28 PM] kasim k: Electronics & Communication Engineering	
Sha-Shib College of Technology	
ABHISHEK ROY CHOUDHURY
7488907024
3feb
[30/01/24, 7:11:15 PM] kasim k: EC	
Patel College of Science & Technology,Bhopal	
ABHISHEK SINGH	
9131890800
10feb
[30/01/24, 7:13:07 PM] kasim k: IES
BE
SANJEEV KUMAR	
6202934623
7feb
[30/01/24, 11:06:01 PM] kp sir: Data science ke saare bachoo ko call hogye drive ke liye bhopal and Gwalior donoo ko .
[30/01/24, 11:07:59 PM] kp sir: @Harsh  in morning prepare a list those are coming for drive as per call status of particular caller ,so that we will identify ,how many students appear from data science branch from bhopal and Gwalior also
[31/01/24, 12:28:27 PM] ~ Deepali coding: Name :- Krishna Ahirwar 
Number: - 9285155809
College: - vns
Branch :-CS
Year: 3 Rd 
Expected date of visit: - 1 Feb
[31/01/24, 12:39:15 PM] khushi e.c: Branch:- Information Technology	
College:- Technocrat Institute of Technology
Name :- 	PRATEEK PANDEY	
Contact:- 6267369788
Expected:- 	m.p nagar 5 pm
[31/01/24, 12:56:06 PM] Hafsa.: Will go Indrapuri today
[31/01/24, 1:45:06 PM] suman coding: Name :- krutika goyal
Number: - 7999526011
College: - LNCT 
Branch :-CSE 
Expected date of visit: - will think
[31/01/24, 1:52:06 PM] Hafsa.: Name :- Mohammad Mohsin Afroz 
Number: - 9262769165
College: - Millennium College 
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - Will come next week ‎<This message was edited>
[31/01/24, 2:47:06 PM] ~ Chauhan Shilpa: Varsha -9522012676
 Meena- 8349567450
College: - Bansal college of engineering
Branch :-CSE
Year: 3rd Yr
Expected date of visit: - Java batch join karna hai mp nagar me
[31/01/24, 3:16:16 PM] ~ Deepali coding: 3RD	Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrats Institute of Technology [Excellence]	MAYUR DAHAKE	7089937905	will come 31 January indrapuri
[31/01/24, 3:28:31 PM] annu❤️: Computer Science & Engineering	
Radharaman Engineering College
SHUBHAM CHAKRAWARTI	7067982985	
Will think DSA
inform himself 
3rd Year
[31/01/24, 3:36:42 PM] Hafsa.: Name :- Abdul Rehman 
Number: - 8319425125
College: - Millennium College 
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - Will contact after exam
[31/01/24, 3:51:32 PM] ~ Deepali coding: PO	EX	[0132]Radha Raman Institute of Technology & Science,Bhopal	TUFAIL ALAM	8404837654	will come after 5 feb
[31/01/24, 3:54:49 PM] Lalita Sahu: Student name:-Rohit choudhary
Branch:-Computer Science & Engineering	
Collage:-IES's College of Technology
Contact:-7086176080
Year:-3rd year
	Expected date of visit:-4Feb
[31/01/24, 3:59:57 PM] Hafsa.: Name :- Anwir Akhtar 
Number: - 7870026241
College: - Millennium College 
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - Will come after 13 Feb
[31/01/24, 4:07:16 PM] Lalita Sahu: Student name:-Rohit verma
Branch:-Computer Science & Engineering	
Collage:-IES's College of Technology
Contact:-7828654809
Year:-3rd year
	Expected date of visit:- will think
[31/01/24, 4:12:51 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Technocrat Institute of Technology
Name :- 	FURQAN MAJEED	
Contact:- 8815574289
Expected date :- 	1feb 5 pm indrapuri
[31/01/24, 4:24:23 PM] Hafsa.: Name : - Mohammad Owais 
Number: - 7007928336
College: - Millennium College 
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - Will come after exam
[31/01/24, 4:33:18 PM] anchal e.c: Electrical & Electronics Engineering	Sagar Institute of Research & Technology	
SACHIN SAHU	
9993412721	
Date_	fsd will come after exam
[31/01/24, 4:34:25 PM] anchal e.c: Electrical & Electronics Engineering	Sagar Institute of Research & Technology	
ZAKIR HUSSAIN
	8002156428		
Date _after exam will confirm
[31/01/24, 5:09:12 PM] ~ Chauhan Shilpa: Name :- MOHIT RAI
Number: - 9301080124
College: - Oriental College of Technology 
Branch :-Computer Science & Engineering
Year: 3ed Yr
Expected date of visit: - Will come next week (indrapuri)
[31/01/24, 5:19:01 PM] Lalita Sahu: Will come tomorrow 4pm M.P.nagr
[31/01/24, 5:21:42 PM] khushi e.c: Branch :-Information Technology
College:-	Technocrat Institute of Technology
Name:-	AMIT DHAKAD
Contact:- 	9098706876
Expected date :- 	4 Feb m.p nagar
[31/01/24, 5:27:51 PM] annu❤️: Computer Science & Engineering	
Radharaman Engineering College
TANU KACHER
6264732197	
Will Come 	20 February
3rd year
[31/01/24, 5:58:01 PM] khushi e.c: Branch:- Information Technology
Colg :-	Technocrat Institute of Technology	
Name:-DHEERAJ THAKRE
Contact:-	8839386967
Expected date :- 	5 Feb
[31/01/24, 6:20:42 PM] arpana e.c: Name of student suman singh
9109153184
passout 
will come 1 feb 
mp nagar
[31/01/24, 6:26:53 PM] Lalita Sahu: Student name:-shivkant
Branch:-Computer Science & Engineering	
Collage:-IES's College of Technology
Contact:-9835369947
Year:-3rd year
	Expected date of visit:- 4feb
[31/01/24, 6:56:28 PM] Hafsa.: Name : -  Shubh Vishwakarma 
Number: - 8817827273
College: - BIRTS
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - Will come after exam
[31/01/24, 9:30:45 PM] Lalita Sahu: Student name:-Anish kumar
Contact:- 9708188798
Collage:- TIT collage
Branch :- B. Tech
Year:- 3rd year
Expeted date :-will come 1feb
[01/02/24, 11:27:31 AM] Harsh sir tl: Hey team, I'm currently at the Indrapuri branch. I'll be at the MP Nagar branch around 12:30. See you there!
[01/02/24, 11:32:06 AM] Hafsa.: Okh Sir
[01/02/24, 11:32:18 AM] Harsh sir tl: Team, I'll be assigning 10 numbers each to some of you shortly. Reach out to these students from Gwalior and update them about our placement drive on 2nd and 4th of Feb. Thanks!
[01/02/24, 11:40:19 AM] Harsh sir tl: Team, if you've received the contact details for Gwalior students, please start reaching out to update them about the upcoming placement drive on 2nd and 4th of Feb. Thanks for your prompt action!
[01/02/24, 11:45:52 AM] Lalita Sahu: Will come today mp nagar
[01/02/24, 12:15:05 PM] Lalita Sahu: Name :- Tannu kumari
Number: - 9973622429
College: -IES collage
Branch :-CS
Year: 3 Rd 
Expected date of visit: - 4 Feb
[01/02/24, 12:42:22 PM] Lalita Sahu: Coming today 5pm indrapuri
[01/02/24, 1:01:30 PM] Lalita Sahu: Name :- SURAJ kumar with one frnd
Number: - 829235507
College: -IES collage
Branch :-CS
Year: 3 Rd 
Expected date of visit: - 3,4 Feb
‎[01/02/24, 1:59:13 PM] Harsh sir tl: ‎image omitted
‎[01/02/24, 1:59:14 PM] Harsh sir tl: ‎image omitted
[01/02/24, 2:00:44 PM] kp sir: ‎This message was deleted.
[01/02/24, 2:00:45 PM] Harsh sir tl: Team, kindly upload these statuses on WhatsApp and Instagram. Thank you for your cooperation!
[01/02/24, 3:04:57 PM] anchal e.c: 2 feb ko Friday h sir
‎[01/02/24, 3:16:32 PM] anchal e.c: ‎image omitted
[01/02/24, 4:14:47 PM] Hafsa.: Name : -  Shailav Patel 
Number: - 9302837592
College: - BIRTS
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - Will try on 4 Feb
[01/02/24, 4:42:20 PM] Lalita Sahu: Will come indrapuri in 20minit  with 2frnd
[01/02/24, 5:10:08 PM] anchal e.c: Name_	sunny Kumar 	
Number _8708083441
College _TIT
Branch _ cs
Date_ 	3 February ‎<This message was edited>
[01/02/24, 5:12:36 PM] Lalita Sahu: 501	Electrical & Electronics Engineering	ADARSH PAL	Sagar Institute of Research & Technology	7000816884	 	will think
[01/02/24, 5:12:49 PM] Lalita Sahu: Electrical & Electronics Engineering	SHIVAM RAGHUWANSHI	Sagar Institute of Research & Technology	9098965237
	will come 4feb
[01/02/24, 5:45:09 PM] Harsh sir tl: 📅 Exciting News! 🚀 Coding Thinker is hosting a Placement Drive on Feb 2nd & Feb 4th, 2024! 🌐✨ Students, gear up for incredible opportunities. Others, explore our institution for top-notch education and placement support in Technical companies. Enroll now for a bright future! 🎓💼 #CodingThinker #PlacementDrive #TechOpportunities
[01/02/24, 5:46:52 PM] Harsh sir tl: Team, let's spread the word! 🚀 Coding Thinker is hosting a Placement Drive on Feb 2nd & Feb 4th, 2024. 🌐✨ Please upload this announcement on our Instagram, Facebook, and WhatsApp channels. Let's make it a success! 📢🎓
[01/02/24, 6:24:30 PM] Hafsa.: Name : -  Ankit Lodhi 
Number: - 9893294762
College: - BIST
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - Will come after exam
[01/02/24, 6:36:04 PM] Harsh sir tl: Team, starting tomorrow, please ensure you come dressed in the proper outfit. Additionally, wear the T-shirts provided by the institute . Thank you for your cooperation!
[01/02/24, 6:40:20 PM] ~ Chauhan Shilpa: Name : -  Farhan Khan 
Number: - 9589707074
College: - tit
Branch :-cs ds
Year: 1st Yr
Expected date of visit: - 2 Feb (mp nagar)
[02/02/24, 1:06:09 PM] ~ Chauhan Shilpa: Name : -  prince sahu and  Vinita Singh 
Number: - 9753561983
College: - lnct 
Year: 2nd Yr
Expected date of visit: - 3 Feb (mp nagar)
[02/02/24, 2:50:27 PM] Harsh sir tl: http://18.246.243.246/assessment
[02/02/24, 3:03:25 PM] arpana e.c: Lakshmi Narain College of Technology
	RISHIKA PURVIYA
	9302442949	
3rd year
	will come after 10feb
mp nagar
[02/02/24, 3:10:20 PM] Harsh sir tl: http://54.218.159.190/assessment/
[02/02/24, 3:42:35 PM] suman coding: Name : -  aniket kushwah 
Number: - 8349864660
College: - Sagar 
Branch :- electronic & communication engineering 
Expected date of visit: - 4 February
[02/02/24, 3:57:53 PM] suman coding: Name : -  Ashutosh Pandey 
Number: - 9793828338
College: - LNCT  
Expected date of visit: - coming today
[02/02/24, 3:58:13 PM] suman coding: Indrapuri
[02/02/24, 5:25:01 PM] arpana e.c: Lakshmi Narain College of Technology
	SAKET CHOURASIYA
	7879057774
3rd year
will come 3 feb 
mp nagar
[02/02/24, 5:52:12 PM] suman coding: Name : -  harsha
Number: - 9753873158
College: - Sagar 
Branch :- electronic & communication engineering 
Expected date of visit: - will think
[02/02/24, 6:43:04 PM] ~ Chauhan Shilpa: Name : -  NIKHIL
Number: - 9993817082
College: - Oriental College of Technology
Branch :-Computer Science & Engineering
Year: 3ed Yr
Expected date of visit: - 4 Feb (mp nagar or indrapuri)
[02/02/24, 7:45:50 PM] kp sir: Harsh photo share kardooo aaj ki
[03/02/24, 12:30:24 PM] arpana e.c: coming  today mp nagar
[03/02/24, 12:43:37 PM] suman coding: Name : -  Arjun Prajapati 
Number: - 7987280398
College: - SAGE
Expected date of visit: - coming today mp nagar
[03/02/24, 12:49:38 PM] Neha mam e.c: Iska kya hua
[03/02/24, 12:53:15 PM] Lalita Sahu: Ye fsd k liye interested h
[03/02/24, 12:53:17 PM] Lalita Sahu: ‎This message was deleted.
[03/02/24, 12:55:07 PM] Lalita Sahu: Abhi 2bje k bad follow ups lege mam
[03/02/24, 12:55:18 PM] Neha mam e.c: To admission karvao
[03/02/24, 12:55:26 PM] Lalita Sahu: Yes maam
[03/02/24, 12:56:09 PM] Neha mam e.c: Aabhi  Saturday Sunday hai to aap karo registration
[03/02/24, 12:56:44 PM] Lalita Sahu: Ok mam
[03/02/24, 12:57:13 PM] khushi e.c: Ok mam
[03/02/24, 12:58:05 PM] Neha mam e.c: Durga aapko bhi registration karvana hai Sunday tak
[03/02/24, 12:58:29 PM] khushi e.c: Ok mam
[03/02/24, 1:06:22 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:- 	NRI Institute of Information Science & Technology
Name :- 	MUKHTAR BAIG
Contact:- 	8871014050
Expected date:-		will. think m.p Nagar
[03/02/24, 1:09:23 PM] khushi e.c: ‎This message was deleted.
[03/02/24, 1:10:19 PM] khushi e.c: ‎This message was deleted.
[03/02/24, 1:42:00 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:- 	NRI Institute of Information Science & Technology	
Name :- SANDEEP KUMAR KORI
Contact:- 	7692959293
Expected date :- 		will think after 1 week
[03/02/24, 3:07:06 PM] ~ Deepali coding: Will come 8 feb with friend Abhishek kumar gupta
[03/02/24, 3:13:13 PM] arpana e.c: name of student Yash chhalotre
9770449788
3rd year
will come 3 feb 
mp nagar
[03/02/24, 3:22:47 PM] Hafsa.: ‎‎Hafsa. changed their phone number to a new number. ‎Tap to message or add the new number.
[03/02/24, 3:23:37 PM] arpana e.c: coming today mp nagar
[03/02/24, 3:33:39 PM] suman coding: Name of Student: rajguru sharma
College name: LNCT 
Contact no: 7987388485
Branch: artificial intelligence and machine learning 
Expected Date of Visit: coming today indrapuri
[03/02/24, 3:35:44 PM] Lalita Sahu: ‎This message was deleted.
[03/02/24, 3:38:38 PM] Lalita Sahu: Name of Student: kapil
College name: Ies college
Contact no: 9098904581
Branch: eletrical &eletronics engineering
Expected Date of Visit: 10feb(crt)
[03/02/24, 3:52:39 PM] khushi e.c: Branch:- Electrical & Electronics Engineering	
College:-Technocrats Institute of Technology & Science	 
Name :-  BALIRAM KUMAR	
Contact:- 8603929240	
Expected date:-	after 13 Feb indrapuri
[03/02/24, 4:03:34 PM] Lalita Sahu: Name of Student: PRAMOD KUMAR VISHWAKARMA	
College name: Ies college
Contact no: 9074271006
Branch: eletrical &eletronics engineering
Expected Date of Visit: 15feb mpnagar
[03/02/24, 4:07:58 PM] khushi e.c: Branch:-Electrical & Electronics Engineering	
College:-Technocrats Institute of Technology & Science
Name :- 	HIMANSHU SEN
Contact:- 	9516027639	
Expected date. :- 	will come today indrapuri
[03/02/24, 4:24:30 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:- 	Technocrats Institute of Technology & Science	
Name:- PRANSHU JAISWAL	
Contact:- 8989288741
	expected	date :- will think 8feb indrapuri
[03/02/24, 4:29:46 PM] khushi e.c: Will come today (indrapuri)+ himanshu Gupta
[03/02/24, 4:30:54 PM] Lalita Sahu: Name of Student: AFSAL ansari
College name: Ies college
Contact no: 9931559235
Branch: eletrical &eletronics engineering
Expected Date of Visit: 12feb
[03/02/24, 4:38:29 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:-	Technocrats Institute of Technology & Science	
Name:- PRASHANT SAHU 
contact	:-9406776354		
Expected date:-4 Feb
[03/02/24, 5:35:18 PM] suman coding: Name of Student: Priya 
College name: Bhopal institute of technology and science 
Contact no: 6362439938
Branch: electronic and communication & engineer 
Expected Date of Visit: will think
[03/02/24, 5:48:27 PM] ~ Hafsa , Coding Thinker: Name : -  Ibrar Ahmed 
Number: - 6006198274
College: - OIST
Branch :-CSE
Year: 2nd Yr
Expected date of visit: - Will come after 12 Feb
[03/02/24, 6:06:45 PM] ~ Deepali coding: ‎This message was deleted.
[03/02/24, 6:11:14 PM] suman coding: Name : -  Azam Khan 
Number: - 7999429849
College: - scope college of engineering 
Branch :-CSE
Expected date of visit: - March MP Nagar
[03/02/24, 6:22:54 PM] ~ Deepali coding: Will come tomorrow Chetak with mayank and Vishal also
[03/02/24, 6:27:21 PM] arpana e.c: name of student muskan patel 
MCA running 
Mansarover college
9009962337
will come .feb 12
Mp nagar
[03/02/24, 6:27:54 PM] arpana e.c: will come tomarrow .
mp nagar
[04/02/24, 11:52:26 AM] khushi e.c: Electrical & Electronics Engineering
College:- 	Technocrat Institute of Technology
Name :- 	SATYADEV KEWAT
Contact:- 	8815234106		
Expected date:- will think
[04/02/24, 12:04:29 PM] suman coding: Name : -  ranjan sahni
Number : - 9060642312
College : - scope college of engineering 
Branch :-CSE
year :- 4 year 
Expected date of visit :-5 February MP Nagar with friend
[04/02/24, 12:11:12 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	
College:- Technocrat Institute of Technology
Name :- 	SHAMIM ALAM
Contact:-	9939333513	
	expected  date:- willt think indrapuri
[04/02/24, 12:13:43 PM] Lalita Sahu: Branch:-Electronics & Communication Engineering	
 College:- Girdhar Siksha Evam Samaj Kalyan Samiti Group of Inst.	
Name:-PRIYESH SHRIVASTAVA	
Contact:- 8305995174	
expected date:-will think
[04/02/24, 12:21:46 PM] suman coding: Name : -  Aditya lavanshi 
Number : - 6266302249
College : - scope college 
Expected date of visit :- coming today MP Nagar
[04/02/24, 12:35:20 PM] Lalita Sahu: Branch:- Electronics & Communication Engineering
College:-	Girdhar Siksha Evam Samaj Kalyan Samiti Group of Inst.	
Student name:-UJJAWAL MANEKAR	
Contact:-6262517079	
Expected date:- will think  indore
[04/02/24, 12:48:34 PM] Lalita Sahu: Electronics & Communication Engineering
Collage:-	Girdhar Siksha Evam Samaj Kalyan Samiti Group of Inst.	
Name:-NARESH KUMAR JATAV	
Contact:-7415777164	
Expected date:-Feb 5
[04/02/24, 1:21:23 PM] ~ Hafsa , Coding Thinker: Will go Indrapuri today
[04/02/24, 2:25:54 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[04/02/24, 2:26:27 PM] ~ Chauhan Shilpa: Name : -  prince sahu and  Vinita Singh , Bhavya 
Number: - 9753561983
College: - lnct 
Year: 2nd Yr
Expected date of visit: -  (mp nagar) will come today
[04/02/24, 2:41:02 PM] suman coding: Coming today indrapuri
[04/02/24, 3:07:55 PM] Lalita Sahu: Branch:-Electrical Engineering	
Collage:-NRI Institute of Research & Technology	
Name:- ANKIT CHARAN
Contact:-	7803888819	
Expected date :-11feb indore
[04/02/24, 3:38:25 PM] ~ Chauhan Shilpa: Name : -  MANOHAR AHIRWAR
Number: -7869723191
College: - SAM College of Engineering & Technology
Year: 3ed Yr
Expected date of visit: - 12 February ke baad
[04/02/24, 3:39:31 PM] khushi e.c: Branch Computer Science & Engineering	
IES's College of Technology
Name:- 	MOHIT KUMAR SINGH
Contact:- 	7903381018		
Expected date:- will come today  indrapuri
[04/02/24, 4:11:45 PM] khushi e.c: Branch :-Computer Science & Engineering
Colg :-	IES's College of Technology
Name :- 	MOKHTAR ALAM
Contact:- 	6200295507	 
Expected date :- 	will think
[04/02/24, 4:21:29 PM] khushi e.c: Branch :- Computer Science & Engineering
Colg :-	IES's College of Technology
Name:- 	MUNNA KUMAR
Contact:- 	7091167155	
Expected date :- 	after holi
[04/02/24, 4:34:32 PM] suman coding: Name : -  Ankit rathor
Number : - 9752839851
College : - Trinity institute of technology 
Branch :- electrical & electronics engineering 
year :- 4 year 
Expected date of visit :- 7 February indrapuri
[04/02/24, 4:47:22 PM] Lalita Sahu: Branch:-Electrical Engineering
College:-	NRI Institute of Research & Technology	
Name:-KULDEEP KATARE	
Contact:-7024674562	
Exepted date:-will think (crt )
[04/02/24, 5:17:34 PM] khushi e.c: Branch :- Computer Science & Engineering
College:-	Patel College of Science & Technology	
Name:-SATYAM KUMAR
Contact:-	9693756696	
Expected date::-	1 March
[04/02/24, 5:31:25 PM] khushi e.c: Branch :- Computer Science & Engineering
College:-	Patel College of Science & Technology
Name:- 	SUDHIR KUMAR	
Contact:- 7070958308
Expected date :- 		after 25 Feb
[04/02/24, 6:26:59 PM] khushi e.c: Will come today indrapuri+ himashu  Gupta
[04/02/24, 11:46:15 PM] kp sir: Today placement drive over , special thanks to all team of Harsh ,and especially Mr. Harsh who did your job very sincerely and your team also done good job .
Behalf of management I would like to thanks all sales hero .
🙏🙏🙏🙏🙏
[05/02/24, 12:27:37 PM] Lalita Sahu: Electrical Engineering	NRI Institute of Research & Technology	PAWAN KUMAR MANDEKAR	9340698900	will come11feb
[05/02/24, 1:02:34 PM] annu❤️: Computer Science & Engineering	
Radharaman Engineering College
AYUSHMAN TIWARI
6232568469	
Will Come DSP	15 February
3rd year
[05/02/24, 1:10:52 PM] ~ Chauhan Shilpa: Name : - SARTHAK SHARMA with friends (Arihant Manas)
Number: -7000594675
College: - VNS Group of Institutions
Year: 2nd year 
Expected date of visit: -  10 ya 11 February ( mp nagar) ‎<This message was edited>
[05/02/24, 1:12:10 PM] khushi e.c: Branch:- Computer Science & Engineering	
College:-Patel College of Science & Technology	
Name:-VICKY KUMAR	
Contact:-9852073594	
Expected date:-
	after holi
[05/02/24, 1:16:36 PM] Lalita Sahu: Electrical Engineering	
NRI Institute of Research & Technology	
MD JALAL UDDIN	
7091044274	
20Feb
[05/02/24, 1:21:24 PM] Neha mam e.c: Kya hua iska
[05/02/24, 1:23:41 PM] Lalita Sahu: Mam  student March  ka bol rha h
[05/02/24, 1:24:40 PM] Lalita Sahu: Ye fees bol rha h ki fees jyada h
[05/02/24, 1:25:56 PM] Neha mam e.c: Me itna time to nahi de paungi
[05/02/24, 1:26:43 PM] Lalita Sahu: Ok mam
[05/02/24, 1:28:48 PM] khushi e.c: Branch:-Electronics & Communication Engineering
College:-	Technocrat Institute of Technology
Name:-	HARSHIT SHARMA
Contact:-	8770514353		
Expected date :- 12 Feb
[05/02/24, 1:34:57 PM] Lalita Sahu: Branch:-Electrical Engineering	
Collage:- NRI Institute of Research & Technology	
Name:-VISHAL BINDWARI	
Contact:-7828860196
Expected date:- 	11Feb
[05/02/24, 1:35:36 PM] khushi e.c: Branch:- Electronics & Communication Engineering	
College:-Technocrat Institute of Technology
Name:-	SANJAY TIWARI
Contact:-	8340703488	
Expected date :- 	5feb indrapuri
[05/02/24, 1:39:30 PM] Neha mam e.c: Aap logo ko telesales ke liye appoint kiya hai naki telecaller ke liye aap sale kar hi nahi paa rahi ho
[05/02/24, 1:41:27 PM] Lalita Sahu: Thik h to aap bta dijiye
[05/02/24, 1:50:12 PM] khushi e.c: Branch:- Electronics & Communication Engineering	
College:-Technocrat Institute of Technology
Name:-	GAUTAM KUMAR CHAUDHRY
Contact:-	6299963599	
Expected date :- 	after 15 Feb indrapuri
[05/02/24, 1:56:48 PM] annu❤️: Computer Science & Engineering	
Radharaman Engineering College	
IRFAN ALAM	8083247436	
Will Come Java	
20 February
3rd Year
[05/02/24, 1:59:21 PM] suman coding: Name of Student: lal bahadur saket
College name: vidyapeeth institute of science & technology 
Contact no: 9826919771
Branch: electronic & communication engineer 
Expected Date of Visit: 7 February indrapuri
[05/02/24, 2:04:53 PM] khushi e.c: Branch :- Electronics & Communication Engineering	
College:-Technocrat Institute of Technology
Name:-	PRINCE KUMAR YADAV
Contact:-	7631232919	
Expected date :- 	 6 Feb evening   in m. p nagar
[05/02/24, 2:50:01 PM] Harsh sir tl: Good afternoon team,

I kindly request each of you to review your previous prospects. Please reshare them in our prospects group to avoid any misunderstandings between the team and management.

Thank you,
[HARSH VARDHAN]
[05/02/24, 2:50:21 PM] khushi e.c: Will come today indrapuri
[05/02/24, 2:50:53 PM] kasim k: old jitne v haiii jinhone bola hai ana ka sub krna hai ky ?
[05/02/24, 2:51:09 PM] Harsh sir tl: Hn
[05/02/24, 3:01:56 PM] khushi e.c: Branch :- Electronics & Communication Engineering	
College:-J.N. College of Technology	
Name:-BHARAT SAHU	
Contact:-9713659570		
Expected date:-11 Feb
[05/02/24, 3:11:28 PM] kasim k: coming 5-6  feb
[05/02/24, 3:28:27 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
ANIL MEHRA	8349951803
Will Come 7 February
Old prospect
[05/02/24, 3:37:04 PM] annu❤️: Computer Science & Engineering	
Sagar Institute of Science Technology & Engineering	
INDRAJEET	
9336274796
Will Come In March
Old prospect
[05/02/24, 3:40:45 PM] khushi e.c: Will come today indrapuri
[05/02/24, 3:40:51 PM] Lalita Sahu: ‎This message was deleted.
[05/02/24, 3:41:12 PM] Lalita Sahu: Name:- YUGESH KUMAR contact:- 7368992893 Branch:-Electrical & Electronics Engineering		collageSagar Institute of Research & Technology	
Year:-3rd
Expected date:-11feb
[05/02/24, 3:50:32 PM] kasim k: (old prospect)
Artificial Intelligence and Machine Learning	Sagar Institute of Research & Technology	
ASHVIN SHINGEWAD	
7724964916	
10feb 
After exam
[05/02/24, 4:05:28 PM] Lalita Sahu: Branch:-Mechanical Engineering
Collage	Technocrats Institute of Technology [Excellence]	MD
Name:-ARIZ KHAN	
Contact:-7355248724	
Expected date12Feb
[05/02/24, 4:20:22 PM] annu❤️: Computer Science & Engineering	
Vidhyapeeth Institute of Science & Technology
PAWAN PATEL	
9123114196	
After exam 15 Feb 
Old prospect
[05/02/24, 4:29:51 PM] khushi e.c: Branch:-Electrical & Electronics Engineering	
College:-Millennium Institute of Technology & Science
Name:-	FAKRUZZAMA
Contact:-	7870955456	
Expected date:-	 will think in March
[05/02/24, 5:05:15 PM] annu❤️: Computer Science & Engineering	
Vidhyapeeth Institute of Science & Technology	
JAVED AKHTER	NA
6203256838
Next semester 
Old prospect
[05/02/24, 5:10:10 PM] annu❤️: Vidhyapeeth Institute of Science & Technology
VINEET PANCHESHWAR	
6268923703	
15 February
Old prospect
[05/02/24, 5:18:20 PM] suman coding: Name of Student: shubham Patel 
College name: Sagar institute of science & technology 
Contact no: 6261396286
Branch: electrical & electronic engineer 
Expected Date of Visit: 7 February indrapuri
[05/02/24, 5:20:33 PM] annu❤️: Computer Science & Engineering	
Vidhyapeeth Institute of Science & Technology
DEEPU KUMAR MAHTO		
9110074313	
In March 
Old prospect
[05/02/24, 5:23:55 PM] kasim k: Computer Science & Engineering	
All Saints' College of Technology	
IRSHAD ANSARI	
9264406199	
2march
 old prospect
[05/02/24, 5:24:05 PM] arpana e.c: SAM College of Engineering & Technology
	YOGENDRA SARATHE
	6265307839
old propect 
3rd year
will think march
[05/02/24, 5:25:38 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[05/02/24, 5:26:41 PM] ~ Chauhan Shilpa: Durga mam apki ye visit aai thi followup ap kal dena same day par follow up nahi dena hai
[05/02/24, 5:27:06 PM] ~ Chauhan Shilpa: Ek friend bhi sath me tha
[05/02/24, 5:27:20 PM] khushi e.c: Ok mam
[05/02/24, 5:31:01 PM] arpana e.c: Radha Raman Institute of Technology & Science	
OM SURYAWANSHI	8770628758
old prospect
will think
[05/02/24, 5:33:08 PM] arpana e.c: Radha Raman Institute of Technology & Science	
BHARTI HUMNEKAR
	9144829862
old prospect
will come in april
[05/02/24, 5:50:16 PM] arpana e.c: Corporate Institute of Science & Technology
	MD IFTAKHAR ALAM
	7004988529
4th year 
old prospect
will come in April
[05/02/24, 5:50:19 PM] annu❤️: Computer Science & Engineering	
Bansal Institute of Science & Technology
NAMAN GUPTA	NA
6260069038	
In March
Old prospect
[05/02/24, 5:50:21 PM] suman coding: Name of Student: himanshu pawar 
College name: Sagar institute of science & technology 
Contact no: 6262523548
Branch: electrical & electronic engineer 
Expected Date of Visit: 9 February MP Nagar
[05/02/24, 5:54:25 PM] annu❤️: Computer Science & Engineering	
Bansal Institute of Science & Technology	
VIKAS DHAKAD	
6265371875	
In April 
Old prospect
[05/02/24, 5:55:40 PM] arpana e.c: Technocrat Institute of Technology	
SAKSHI RAUT
	6265335909
old prospect
will come 20 feb
[05/02/24, 5:57:20 PM] kasim k: (old prospect)
aids	
sirt	ajay singh lodhi	
8817717164		
try to come 6 feb/
after exam
[05/02/24, 5:57:33 PM] Lalita Sahu: Mechanical Engineering
	Technocrats Institute of Technology [Excellence]
	PRADEEP KUMAR MARAVI
	6266448669	
will think CRT
[05/02/24, 6:02:42 PM] annu❤️: Computer Science & Engineering	
Bansal Institute of Science & Technology	
SHIVAM KUMAR	NA
9758802344	
In March 
Old prospect
[05/02/24, 6:03:57 PM] arpana e.c: Bhopal Institute of Technology & Science, Bangrasia
	REETA
	7879403594
old prospect
will come 5 march 
after exam
[05/02/24, 6:07:05 PM] arpana e.c: Lakshmi Narain College of Technology
	TUSHAR BISEN
	7999068020
old prospect 
will think
[05/02/24, 6:07:40 PM] Lalita Sahu: Branch:-Mechanical Engineering
Collage:-	Technocrats Institute of Technology [Excellence]	
name:- PRAFUL KASDEKAR
Contact:-	9171027182	
will come first week in march
[05/02/24, 6:11:18 PM] annu❤️: Computer Science & Engineering	
Bansal Institute of Science & Technology
RIYA INDRAPAL PATLE
9343791533	
20 February
Old prospect
[05/02/24, 6:18:35 PM] kasim k: (old prospect)
2ND		
Shubham chouhan	8600270560		
After  22 feb  chetak bridge
[05/02/24, 6:24:50 PM] annu❤️: Computer Science & Engineering	
Oriental College of Technology	
DIVYANSHU KUMAR MAURYA		
8815262631	
10 February
Old prospect
[05/02/24, 6:27:10 PM] arpana e.c: Radha Raman Institute of Technology & Science	
MD SHAHBAZ
	8298423174
old prospect
will come after march
[05/02/24, 6:36:32 PM] annu❤️: Computer Science & Engineering	
Oriental College of Technology
ADITYA CHANDRA	
8405876247	
After exam In March 
Old prospect
[05/02/24, 6:40:49 PM] kasim k: Computer Science & Engineering	
NRI Institute of Information Science & Technology	
AARYAN GARDE	
9301330510			
20Feb
(old prospect)
[05/02/24, 6:43:13 PM] arpana e.c: Lakshmi Narain College of Technology Excellence
	SAURAV KUMAR
	9708817643
3rd year
old prospect
will come 11 feb
[05/02/24, 6:43:17 PM] khushi e.c: Branch :-Computer Science & Engineering	
College:-Patel College of Science & Technology	
Name:-KHAN WASIM AKRAM
Contact:-	9326628747		 
Expected date:-after 13 Feb
[05/02/24, 6:56:42 PM] kasim k: Computer Science & Engineering	
Bansal Institute of Research & Technology	
SAGAR MISHRA	
9993679315			
10feb indrpuri
 (old prospect)
[05/02/24, 6:58:09 PM] kasim k: + friends data analytics
[05/02/24, 6:58:20 PM] annu❤️: Computer Science & Engineering	
Sagar Institute of Science Technology & Engineering	
SATENDRA KUSHWAHA
6264847948	
18 February with friend
Old prospect
[05/02/24, 7:02:54 PM] Neha mam e.c: Pls sabhi Aapne friend ke naam mention kariye
[05/02/24, 7:30:06 PM] Neha mam e.c: Kissi par data science or data analytic ka student ho MP nagar ke liye to kal 2 baje class hai
[05/02/24, 8:05:30 PM] kp sir: Kuch bachhe enquiry kiye the arpanaa Kal aakar ek baar dekhlenaa enquiry form
[05/02/24, 8:28:32 PM] arpana e.c: hnn sir
[05/02/24, 9:40:01 PM] anchal e.c: Branch :-Computer Science 
College:- millenium
Name:-priyanshu 
Contact:-	9708766702 
Expected date:-8Feb
[05/02/24, 10:30:09 PM] ~ Deepali coding: Branch :-Computer Science
College:- Lnct
Name:-piyush solanki
Contact:- +91 91655 36804
Expected date:-6 feb
[05/02/24, 10:52:43 PM] Neha mam e.c: @919424704675 @916263594069 aaj ghar baithakar kaam kar rahi ho kya
[05/02/24, 11:30:43 PM] anchal e.c: Yes ma'am
[06/02/24, 12:12:48 PM] annu❤️: Computer Science & Engineering	
Bansal Institute of Science & Technology	
AKSHAT LOVANSHI	
7440910307	
In February 
Old prospect
[06/02/24, 12:12:56 PM] ~ Deepali coding: Branch :-Computer Science
College:- tit passout 
Name:-Rupali
Contact:-  95165 01323
Expected date:-7 feb
[06/02/24, 12:16:09 PM] annu❤️: Computer Science & Engineering	
Bansal Institute of Science & Technology
BOBY YADAV	
9340173798	
In March 
Old prospect
[06/02/24, 12:16:43 PM] arpana e.c: Bhopal Institute of Technology & Science, Bangrasia
	RAJKUMAR
	7697422166
old prospect
already visited 
come for adimison 12 feb
[06/02/24, 12:28:02 PM] arpana e.c: Shri Ram College of Technology
	DEEKSHA BOPCHE
	9301320875
Already visited
come for revist  8feb
old prospect
[06/02/24, 12:34:09 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
HARIOM TRIPATHI	
9302682283	
12 Feb
chetak bridge
(old prospect)
[06/02/24, 12:34:09 PM] arpana e.c: Surabhi College of Engineering & Technology	
AKASH DOHARE
	9165671327
Old prospect
Already visted 
Come for revist
[06/02/24, 12:34:30 PM] annu❤️: Computer Science & Engineering	
Oriental College of Technology
PRINCE DWIVEDI	
7024389122
In March Cc++
Old prospect
[06/02/24, 12:38:05 PM] anchal e.c: Electrical & Electronics Engineering	Sagar Institute of Research & Technology
	HARSH BASEDIYA	
9993564088	
Date _1 march will come ‎<This message was edited>
[06/02/24, 12:40:30 PM] Lalita Sahu: Will come today mpnagar
[06/02/24, 12:41:03 PM] arpana e.c: Lakshmi Narain College of Technology Excellence	
RACHIT TIWARI
3Rd year
	7354672172
Old prospect
Will come today 
Inderpuri
[06/02/24, 12:41:47 PM] ~ Hafsa , Coding Thinker: Name of Student: Shivam Kachchi + friends ( Gaurav,Satyam, Rajkumar )
College name: TIT
Contact no: 9770081523
Branch: EC
Year: 2nd Yr old prospect 
Expected Date of Visit: After 13 Feb ‎<This message was edited>
[06/02/24, 12:43:31 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
ASHOK AHIRWAR	
9770930874
11 Feb (chetak ) old prospect
[06/02/24, 12:44:06 PM] ~ Hafsa , Coding Thinker: Name of Student: Ankur Gangwani 
College name: LNCT
Contact no: 7000433838
Branch: CS
Year: 2nd Yr old prospect 
Expected Date of Visit: After exam (14 Feb ) ‎<This message was edited>
[06/02/24, 12:44:07 PM] Lalita Sahu: Will come today indrapuri
[06/02/24, 12:45:32 PM] khushi e.c: Branch :-Electrical & Electronics Engineering
College:-	Millennium Institute of Technology & Science
Name:-	SUNIDHI VINOD VISHWAKARMA
Contact:-	8669130694	
Expected date :-	will think
[06/02/24, 12:48:27 PM] arpana e.c: Oriental College of Technology
	LAL SINGH
	8269356696
3rd Year
Old Prospect
will come 8 Feb
[06/02/24, 12:52:53 PM] khushi e.c: Branch :-Electronics & Communication Engineering
College:-	Technocrat Institute of Technology
Name :-	GOURAV KUMAR
Contact:-	7667444505	
Expected date :-	after 20 Feb m.p Nagar
[06/02/24, 12:55:14 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	AYUSH KUMAR GUPTA	
7485055300
Date _		after	12	feb will come
Old prospect ‎<This message was edited>
[06/02/24, 12:56:45 PM] annu❤️: Computer Science & Engineering	
Sagar Institute of Science Technology & Engineering	
DILIP KUMAR	
7909086049
Already Admission will Come with friends In March 
Old prospect
[06/02/24, 1:01:01 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Lakshmi Narain College of Technology & Science	
ARSHITA RAI	
7987495026		
Date _	after exam 15 feb
Old prospects
[06/02/24, 1:04:17 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
ABHISHEK MEENA	
9981351626	
15Feb
(old prospect)
[06/02/24, 1:04:42 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Data Science	Technocrat Institute of Technology	
ANUPAM DWIVEDI	
7879431924	
Date_	will come march		
Old prospect
[06/02/24, 1:11:39 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Data Science	Technocrat Institute of Technology	
ASHISH SAHU	
8085766413		
Date _after exam will come 
Old prospect
[06/02/24, 1:15:30 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	TANYA CHAURASIA	9039612573
Visit date - will come after 8 feb
[06/02/24, 1:15:54 PM] anchal e.c: Information Technology	Oriental Institute of Science & Technology	
SAKSHI PARDHI	
7440500495		
Date_ after exam will think			
Old prospect
[06/02/24, 1:16:47 PM] ~ Hafsa , Coding Thinker: Name of Student: Shivraj Tiwari 
College name: LNCT
Contact no: 7987457276
Branch: AI/DS
Year: 2nd Yr old prospect 
Expected Date of Visit: 9 Feb
[06/02/24, 1:17:36 PM] annu❤️: Computer Science & Engineering	
Scope College of Engineering	
ABHILASHA DUBEY		8962451989	
10 February
Old prospect
[06/02/24, 1:17:56 PM] ~ Chauhan Shilpa: Name : -  SHUBHAM KEWAT
Number: - 6260806067
College: - Radha Raman Institute of Technology & Science
Branch :- Computer Science & Engineering
Year: 3ed Yr
Expected date of visit: - Will come after 15 February (old prospect) ‎<This message was edited>
[06/02/24, 1:18:07 PM] ~ Hafsa , Coding Thinker: Name of Student: Nayan Brijpuria
College name: LNCT
Contact no: 7999857524
Branch: CS/AI/ML
Year: 2nd Yr old prospect 
Expected Date of Visit: After 16 Feb
[06/02/24, 1:19:39 PM] ~ Deepali coding: Computer Science & Engineering	Radharaman Engineering College	PRASHANT SAGAR	7307662237	
Visit date will come 9 feb with (friend group)
[06/02/24, 1:21:06 PM] annu❤️: Computer Science & Engineering	
Scope College of Engineering	
RAMAKANT SAHU	
8871087598	
15 February
Old prospect
[06/02/24, 1:24:00 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence	Technocrat Institute of Technology	RAJENDRA RAJPUT	
8962996982	
Date _will come after exam 	 
Old prospect
[06/02/24, 1:24:55 PM] arpana e.c: Technocrats Institute of Technology [Excellence]	
RAHUL PRAJAPTI
	7024155704
3rd year
old prospect
will come after march
[06/02/24, 1:26:37 PM] ~ Chauhan Shilpa: Name : -  SACHIN VERMA
Number: - 7415731797
College: - Technocrats Institute of Technology & Science
Branch :-Computer Science & Engineering
Year: 3ed Yr
Expected date of visit: - Will come after 10 February( old prospect) ‎<This message was edited>
[06/02/24, 1:28:28 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	SUDHANSHU SHEKHAR	6206292270	visit date : after 15 feb indrapuri
[06/02/24, 1:32:55 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	
ABHISHEK GUPTA	
9304613765	
Date _20,21 feb will come 
Old prospect ‎<This message was edited>
[06/02/24, 1:35:07 PM] khushi e.c: ‎This message was deleted.
[06/02/24, 1:37:54 PM] khushi e.c: Branch :-Computer Science & Engineering
College:-	Bansal Institute of Research & Technology
Name:-	SHIVANI LODHI	contact:-9752829851
Expected date :- 		after 15 Feb
[06/02/24, 1:41:37 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	GURUDATT KUMAR GAUTAM	7250732106	 	visit date after 15 feb
[06/02/24, 1:45:28 PM] annu❤️: Computer Science & Engineering	
Oriental College of Technology
RAJ THAKRE	
7583003335	
18 February
Old prospect
[06/02/24, 1:46:08 PM] annu❤️: Computer Science & Engineering	
Sagar Institute of Science Technology & Engineering	
HIMANSHU SHIVHARE	
7999290891	
In March 
Old prospect
[06/02/24, 1:46:51 PM] ~ Chauhan Shilpa: Name : -  KAUSHAL KUMAR
Number: - 8340753566
College: - Scope College of Engineering
Branch :-Computer Science & Engineering
Year: 3ed Yr
Expected date of visit: - Will think ( old prospect)
[06/02/24, 1:54:46 PM] annu❤️: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
WASI HAIDER	
9798674832	
In March 
Old prospect
[06/02/24, 1:56:13 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	
MD IZAAN AHMAD	
7209452658	
Date _after exam 17 Feb will come 			
Old prospect
[06/02/24, 2:18:19 PM] Lalita Sahu: Maam ye visit aai h kya confirm kr diye student ko follow up k liye call kiya tha to bol rha h ki visit krliya
[06/02/24, 2:19:06 PM] Neha mam e.c: Kargya visit
[06/02/24, 2:19:12 PM] Lalita Sahu: Ok maam
[06/02/24, 2:39:37 PM] anchal e.c: Name_	sunny Kumar 	
Number _8708083441
College _TIT
Branch _ cs
Date_ 	1 March
Old prospect
[06/02/24, 2:42:49 PM] aman ct: ‎Neha mam e.c added aman ct
[06/02/24, 2:45:13 PM] ~ Deepali coding: Will come 14 with 3 friends Ariz khan Ashish and azaad
[06/02/24, 2:56:25 PM] khushi e.c: Coming today
[06/02/24, 2:59:47 PM] annu❤️: Computer Science & Engineering-Data Science	
IES College of Technology	
SHIVAM SAHU	
6267738513	
20 February
Old prospect
[06/02/24, 3:01:59 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	SHAIKH AAMIR	6267112564	will come after 14 feb
[06/02/24, 3:07:29 PM] annu❤️: Computer Science & Bussiness System	
IES College of Technology	
HARSH PANDEY		9199668058	
In March 
Old prospect
[06/02/24, 3:09:25 PM] aman ct: ‎Neha mam e.c removed aman ct
[06/02/24, 3:14:05 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
SHEKHAR DAHARWAL	
8435244150	
Date _march will come 
Old prospect
[06/02/24, 3:20:37 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science
	RAJEEV SINGH
	7488554105	
Date -after exam will come 
Old prospect
[06/02/24, 3:21:11 PM] annu❤️: Computer Science & Engineering-Data Science	
IES College of Technology	
KANHAIYA KUMAR CHAURSIYA	
9060706664	
In March 
Old prospect
[06/02/24, 3:31:02 PM] anchal e.c: Electrical & Electronics Engineering	Sagar Institute of Research & Technology	ZAKIR HUSSAIN	8002156428
Date_	20 feb will come 
Old prospect
[06/02/24, 3:46:25 PM] ~ Memuna Coding Thinker: ‎Neha mam e.c added ~ Memuna Coding Thinker
[06/02/24, 3:46:04 PM] annu❤️: Computer Science & Engineering-Data Science	
IES College of Technology
SHIVAM TIWARI
7209523830	
20 February
Old prospect
[06/02/24, 3:48:53 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	
SACHIN RAJPOOT	
6260317991
Date_	16 Feb indrapuri			
Old prospect
[06/02/24, 3:52:26 PM] kasim k: ‎You deleted this message.
[06/02/24, 3:53:12 PM] kasim k: (old prospect)
Computer Science & Engineering	
SAM College of Engineering & Technology	
CHETAN CHOUDHARY	8815069845	
16feb
[06/02/24, 3:53:17 PM] annu❤️: Computer Science & Engineering-Data Science	
Oriental College of Technology
YUSRA SIDDIQUI
8305128150
In March DSA 
Old prospect
[06/02/24, 3:57:11 PM] annu❤️: Information Technology
Oriental College of Technology
RISHI CHOURASIY
9301750526	
Indrapuri 	In March Cc++
Old prospect
[06/02/24, 3:59:41 PM] arpana e.c: Technocrats Institute of Technology [Excellence]
	PANKAJ SAHU
	9171449865
Already visited
come for revist feb end
[06/02/24, 3:59:53 PM] khushi e.c: Branch-:Electrical & Electronics Engineering
College:-	Bansal Institute of Research & Technology
Name:-	ABHISHEK
Contact:-	7610640386	
Expected date :-	will think
[06/02/24, 4:00:46 PM] annu❤️: Information Technology
Oriental College of Technology	
VINEET SARATHE
8319754015		
20 February
Old prospect
[06/02/24, 4:02:20 PM] annu❤️: IES College of Technology
PRABHAT KUMAR	
9262523489	
16 February
Old prospect
[06/02/24, 4:03:00 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Research & Technology	
SATISH KUMAR	
6267378639
	Date _20,22 feb Ds	January
 old prospect ‎<This message was edited>
[06/02/24, 4:12:09 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:-	Bansal Institute of Research & Technology
Name:-	ARTI
Contact:-	7692021955
Expected date :-		will think
[06/02/24, 4:16:19 PM] kasim k: ‎You deleted this message.
[06/02/24, 4:16:37 PM] kasim k: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence	
MAHAK RAGHUWANSHI	9302057341		 
after exam feb 12
(old prospect )
[06/02/24, 4:18:04 PM] kasim k: (old prospect)
Computer Science & Engineering	
J.N. College of Technology	
AYUSH CHOUDHARY	 
9691255508	
feb 10 after exam
[06/02/24, 4:18:08 PM] kasim k: Electronics & Communication Engineering	
IES College of Technology	NITISH KUMAR	
6203749531	 
feb 20 after exam
(old prospect)
[06/02/24, 4:22:54 PM] ~ Hafsa , Coding Thinker: Name of Student: Ritesh Mewada
College name: BIST 
Contact no: 9303926442
Branch: CSE
Year: 1st Yr old prospect 
Expected Date of Visit: After 16 Feb
[06/02/24, 4:28:58 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	
College:-Bansal Institute of Research & Technology	
Name:-HARSH KUSHWAHA
Contact:-	9685543756		
Expected date after 19 Feb
[06/02/24, 4:31:25 PM] anchal e.c: Information Technology	Oriental Institute of Science & Technology
	KANISHQ RAGHUWANSHI	
6265963407	
Date _second week of March 	indrapuri 	
Old prospect ‎<This message was edited>
[06/02/24, 4:37:37 PM] anchal e.c: Information Technology	Technocrat Institute of Technology	
HARSH PRAKASH
	8789791626	
Date _will come march		
Old prospect
[06/02/24, 5:11:04 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	 PANKAJ BAIRAGI	
9522437225	
feb 20	
old prospect
[06/02/24, 5:15:25 PM] arpana e.c: Oriental College of Technology
	ALOK VISHWAKARMA
	9407582236
3rd year
old prospect
Will come today  
mp nagar
[06/02/24, 5:16:09 PM] kasim k: old prospect
Computer Science & Engineering	
J.N. College of Technology	
UMASHANKAR AHIRWAR	
8085145152	
after exam 22feb
[06/02/24, 5:17:33 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
GAURAV DAHIYA	
8319866542	
march 1week
(old prospect)
[06/02/24, 5:19:17 PM] annu❤️: Artificial Intelligence and Machine Learning	
J.N. College of Technology
SOMNATH NISHAD	
8103898620	
In March 
Old prospect
[06/02/24, 5:19:59 PM] ~ Deepali coding: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	ATUL AYUSH	9471999399	will come for revisit 9 feb indrapuri ( with friend sumit)
[06/02/24, 5:21:53 PM] annu❤️: Artificial Intelligence and Machine Learning	
J.N. College of Technology	
SAURABH KUMAR DWIVEDI	
7509809897	
20 February
Old prospect
[06/02/24, 5:22:54 PM] ~ Hafsa , Coding Thinker: Name of Student: Nitish Kumar 
College name: TIT
Contact no: 7494034024
Branch: CS/AI/ML
Year: 1st Yr old prospect 
Expected Date of Visit: After 20 Feb
[06/02/24, 5:24:16 PM] kasim k: (old prospect)
IES	
BE	
PRADEEP NIGAM	
8305729451	
c,c++
march batch
[06/02/24, 5:25:48 PM] annu❤️: Artificial Intelligence and Machine Learning	
J.N. College of Technology	NAMAN CHAURASIYA
8858562796	
15 February
Old prospect
[06/02/24, 5:31:04 PM] ~ Deepali coding: Electronics & Communication Engineering	Lakshmi Narain College of Technology	SURYMANI KUMAR	9693297428	will come 16 feb indrapuri
[06/02/24, 5:31:48 PM] kasim k: btec
2021  
Arti	
9691296114	
1 year java	will think	
10march
[06/02/24, 5:31:54 PM] ~ Hafsa , Coding Thinker: Name of Student: Utkarsh Tamrakar 
College name: TIT
Contact no: 7746099515
Branch: CS/AI/ML
Year: 1st Yr old prospect 
Expected Date of Visit: After 20 Feb
[06/02/24, 5:34:15 PM] arpana e.c: IES's College of Technology
	ABHISHEK KUMAR SINGH
	6200506319
Old prospect
Will come April 3
[06/02/24, 5:39:19 PM] ~ Deepali coding: ‎This message was deleted.
[06/02/24, 5:39:36 PM] annu❤️: Computer Science & Engineering	
Sagar Institute of Science Technology & Engineering	
ROHIT BAMNE	
Will come After exam
7879390759	
In March 
Old prospect
[06/02/24, 5:40:12 PM] ~ Deepali coding: 27	Computer Science & Engineering-Data Science	Oriental College of Technology	ASHI SHRIVASTAVA	6260572116
Visit date: 16 feb chetak
[06/02/24, 5:41:55 PM] annu❤️: Computer Science & Engineering-Data Science	
Oriental College of Technology
PRADEEP KUMAR SAHU	
6265386521 
18 February
Old prospect
[06/02/24, 5:42:35 PM] arpana e.c: IES's College of Technology
	GOURAV YADAV
	8319663425
3rd year
old prospect
 will come 7 feb
[06/02/24, 5:44:43 PM] anchal e.c: Electrical & Electronics Engineering	Radha Raman Institute of Technology & Science	
PREETAM RAJ	
7667174032	
Date _after 15 feb will come 
mp nagar 	
Old prospect
[06/02/24, 5:47:11 PM] annu❤️: Computer Science & Engineering-Data Science	
Oriental College of Technology	
UTKARSH SHRIVASTAVA	
7566273632	
20 February
Old prospect
[06/02/24, 5:47:41 PM] annu❤️: Artificial Intelligence and Machine Learning	
J.N. College of Technology	
PRATHVI RAJ YADAV	
7000920710	
In March
Old prospect
[06/02/24, 5:51:24 PM] anchal e.c: Electrical & Electronics Engineering	Oriental Institute of Science & Technology
	GOUTAM SAHU
	9424698881	 
Date _after 16 feb 
indrapuri 	 	
Old prospect ‎<This message was edited>
[06/02/24, 6:00:07 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
SANJAY KUMAR
	6287844845	
Date _after 15 February
Old prospect
[06/02/24, 6:01:17 PM] anchal e.c: Electrical & Electronics Engineering	Sagar Institute of Research & Technology	
MAHFUZ ALAM
	8210573876	
Date_	after exam
Old prospect
[06/02/24, 6:01:34 PM] kasim k: Lnct 
sanskar
9109291533
+ prince ,vinita + 1
7 feb chetak bridge
[06/02/24, 6:02:04 PM] annu❤️: Artificial Intelligence and Machine Learning	
J.N. College of Technology	
AASTHA KUMARI SINGH	
9798534163	
In March 
Old prospect
[06/02/24, 6:02:18 PM] anchal e.c: Electrical & Electronics Engineering	Sagar Institute of Research & Technology	
SHIVAM KUMAR
	9065673471	
	Date _after exam
Old prospect
[06/02/24, 6:06:11 PM] annu❤️: Artificial Intelligence and Machine Learning	
J.N. College of Technology
	BHARGAVI CHOUDHARY	
9749993967	
16 February
Old prospect
[06/02/24, 6:06:49 PM] anchal e.c: Electrical & Electronics Engineering	Sagar Institute of Research & Technology	
MANISH KUMAR
	7870651752
Date_	will come 10 March 	fsd 					
Old prospect
[06/02/24, 6:09:53 PM] anchal e.c: Electrical & Electronics Engineering	
Sagar Institute of Research & Technology	
RAHUL ANURAGI
	8109126618	
Date _8,9 feb will come 
Old prospect
[06/02/24, 6:10:47 PM] khushi e.c: Branch :- Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Lakshmi Narain College of Technology & Science	
Name:-ABHISHEK LODHI
Contact:-	8770413417
Expected date 		will think
[06/02/24, 6:11:35 PM] ~ Deepali coding: Information Technology	Oriental College of Technology	VILASH PATIL	7247614032	after 8 feb indrapuri
[06/02/24, 6:20:54 PM] khushi e.c: Branch :-Electrical & Electronics Engineering	
College:-Bansal College of Engineering
Name:-	SANTOSH KUMAR
Contact:-	7354333114	,7999091577	
 Expected date:-will come  9 Feb
[06/02/24, 6:24:24 PM] ~ Deepali coding: Information Technology	Oriental College of Technology	SATYAM VISHWAKARMA	9754729123	 will come 16 feb
[06/02/24, 6:29:43 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	VAIBHAV DESHMUKH	6263016398	will come after 12 feb
[06/02/24, 6:32:33 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	SATYAM RAHUL	8853579874	will come after 12 fev
[06/02/24, 6:36:20 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	
MD SHAHID ALI
	8709758469	
Date _after exam Will come 
Old prospect
[06/02/24, 6:39:21 PM] anchal e.c: Electronics & Communication Engineering	Lakshmi Narain College of Technology
	TANISHKA BEHERA	
9039813204	
Date _ after exam
Old prospect
[06/02/24, 6:41:18 PM] ~ Hafsa , Coding Thinker: Name of Student: Manas Kumar
College name: TIT
Contact no: 9693104628
Branch: CS/AI/ML
Year: 1st Yr old prospect 
Expected Date of Visit: After 16 Feb
[06/02/24, 6:45:15 PM] ~ Deepali coding: 34	Computer Science & Engineering-Data Science	Oriental College of Technology	NIKESH PATEL	6264821937	will  come 11 feb indrapuri
[06/02/24, 6:45:22 PM] anchal e.c: Computer Science & Engineering	Oriental College of Technology
	BADAL SINGH	
9179787632	
Date _9 feb will come 	old prospect
[06/02/24, 6:45:23 PM] annu❤️: Information Technology
Technocrat Institute of Technology	
HARSH KUMAR	NA	6207734782	
20 February
Old prospect
[06/02/24, 6:50:49 PM] anchal e.c: Electronics & Communication Engineering	Lakshmi Narain College of Technology	
RAMAN PANDIT	7222936532	
Date _after exam 
Old prospect
[06/02/24, 6:51:20 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Data Science	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	SONU KUSHWAH	6232377368	will come march
[06/02/24, 6:51:29 PM] annu❤️: Information Technology
Technocrat Institute of Technology	
AKSHAT SINGH RAGHUWANSHI	
6263580724	
In March 
Old prospect
[06/02/24, 6:56:42 PM] anchal e.c: Electronics & Communication Engineering	Sagar Institute of Research & Technology
 POORVA VISHWAKARMA	
9981508159	
after exam will come ‎<This message was edited>
[06/02/24, 6:59:35 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
MUSKAN SINGH	
7307970318	 
22feb
( old prospect)
[06/02/24, 7:03:12 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Oriental Institute of Science & Technology	CHANDRA PRAKASH PASWAN	8103777579		will come	16 feb chetak
[06/02/24, 7:04:50 PM] anchal e.c: Electronics & Communication Engineering	Sagar Institute of Research & Technology	
MOHD IBAD KHAN	
6265533886	
will come 7,8 feb
[06/02/24, 7:06:56 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Data Science	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	TANISH PATIDAR	9171386066	will come after 16 feb
[06/02/24, 7:08:24 PM] kasim k: ‎You deleted this message.
[06/02/24, 7:09:39 PM] anchal e.c: Electronics & Communication Engineering	Sagar Institute of Research & Technology	
NISHANK DIXIT
	8839809059	
 after exam
[06/02/24, 7:10:11 PM] annu❤️: Computer Science & Bussiness System
Oriental Institute of Science & Technology	SAMRIDHI		
6201677818	
11 February
Old prospect
[06/02/24, 7:10:25 PM] kasim k: Artificial Intelligence and Data Science	
J.N. College of Technology	
PRERNA DESHMUKH	
8225974597	
13 feb + devki +1
chetak bridge
[06/02/24, 7:12:22 PM] arpana e.c: Vaishnavi Inst. of Tech. & Science
	ANKIT KEER
	9098555023
Old prospect
will come after 10 feb
[06/02/24, 7:14:16 PM] kasim k: 2/6/2024	Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
VISHAL KUMAR SINGH	
9939166764	
24 Feb
(old prospect)
[06/02/24, 7:17:36 PM] anchal e.c: Computer Science & Engineering	Bansal College of Engineering	
ROHAN KEER	
8319416315	
Date -after exam fsd
[07/02/24, 11:55:28 AM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
MAHEK ZAHEER	
9131844658	
1march
[07/02/24, 12:00:26 PM] ~ Memuna Coding Thinker: Computer science &
 Engineering
All Saint's College of technology
Inam Khan
8839053109
12 Feb
[07/02/24, 12:02:35 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
AVNISH MISHRA	
9219789114	
29 jan nehru nagar 
chetak bridge 
(old prospect)
[07/02/24, 12:06:46 PM] annu❤️: Artificial Intelligence and Machine Learning	
J.N. College of Technology
PRASHANT KUMAR	
6204769164	
15 February With Friends Parv , Mahesh + 2 
Old prospect
[07/02/24, 12:07:54 PM] anchal e.c: Electronics & Communication Engineering	Lakshmi Narain College of Technology
	VIVEK KUMAR MISHRA	
9113132535
	 after 12 feb
[07/02/24, 12:13:17 PM] kasim k: Computer Science & Engineering	
Vaishnavi Inst. of Tech. & Science	
MANOJ KUMAR DAHARE	
9302982064	
march batch 
(old prospect)
[07/02/24, 12:14:12 PM] annu❤️: Computer Science & Engineering-Data Science	
Technocrat Institute of Technology	
VINAY SOLANKI	
9109429283	
In March 
Old prospect
[07/02/24, 12:16:08 PM] arpana e.c: Millennium Institute of Technology
	KRANTI BELWANSHI
	8120644270
2nd year
Old prospect 
Will come 27 feb
[07/02/24, 12:18:10 PM] kasim k: Computer Science & Engineering	
Vaishnavi Inst. of Tech. & Science	
HIMANSHI MALVIYA	
7869507357		
15March
(old prospect)
[07/02/24, 12:19:37 PM] khushi e.c: Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Lakshmi Narain College of Technology & Science	
Name::-KAUSHAL LADIYA
Contact:-	8770385447		
Expected date:- will think 2  Days indrapuri
[07/02/24, 12:22:20 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]
	FAHAD ALI	
7033178536	 
after exam will come
[07/02/24, 12:23:02 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Research, Technology & Science	
NIRANJAN KUMAR	
7492928753	
after exam
[07/02/24, 12:23:24 PM] ~ Deepali coding: Branch :-Ec
Name:-	shaheen
Contact:-8109732125
 Expected date:-will come  10 Feb with friend Ruksar
[07/02/24, 12:24:39 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Research, Technology & Science
	PRACHI GAUTAM	6268579012	
after exam
[07/02/24, 12:25:19 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Research, Technology & Science	
SURENDRA LODHI	9301003419	
after 12 feb fsd
[07/02/24, 12:25:59 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Research, Technology & Science	
AMAN SINGH RATHOUR	
7880268112	
10 feb
[07/02/24, 12:26:41 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Research, Technology & Science
	PRIYANSHU GOSWAMI	
6264664290
	after exam
[07/02/24, 12:30:15 PM] arpana e.c: J.N. College of Technology
	KHUSHBU SAHU
	9301314192
2nd year
Old prospect
will come 12 feb
[07/02/24, 12:33:15 PM] ~ Hafsa , Coding Thinker: Name of Student: Sonam Tiwari 
College name: NRI
Contact no: 9302292406
Branch: CS
Year: 1st Yr old prospect 
Expected Date of Visit: After 12 Feb
[07/02/24, 12:33:18 PM] kasim k: Oriental College of Technology	
TOMENDRA PAWAR	
8719887568	
after exam	 feb end
(old prospect)
[07/02/24, 12:34:14 PM] khushi e.c: Will come today + freind puplesh
[07/02/24, 12:35:38 PM] ~ Memuna Coding Thinker: Name of Student: Priya Sahu
College name: TIT
Contact no: 8717922553
Branch: CS
Expected Date of Visit: Next week
[07/02/24, 12:35:39 PM] ~ Deepali coding: Computer Science & Engineering	Radharaman Engineering College	MD EHTESHAM ANSARI	6201463513	willl come 12 feb chetak
[07/02/24, 12:40:12 PM] arpana e.c: J.N. College of Technology
	RADHIKA RAI
	7440928509
2 Nd year
Old prosPect
Will come 14 feb
[07/02/24, 12:40:53 PM] arpana e.c: Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
	RAHUL KUMAR
 BHAGAT
	7779919830
2nd year
Old prospect
Will come 16 feb
[07/02/24, 12:41:11 PM] ~ Deepali coding: Computer Science & Engineering	Radharaman Engineering College	ZAKIR HUSSAIN	7739678028	will come chetak not not confirmed date
[07/02/24, 12:44:10 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	JITENDRA CHOUDHARY	9399088027	 	after exam
[07/02/24, 12:44:15 PM] arpana e.c: Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
SUMIT AHIRWAR
	9131895387
Old prospect
Will come 2 march
[07/02/24, 12:45:10 PM] khushi e.c: Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Lakshmi Narain College of Technology & Science	
Name:-MUSKAN SAHU
Contact:-	7470779968		
Expected date:-will think
[07/02/24, 12:47:23 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science
	ROHIT KUMAR
	9110079736
	12 feb will come
[07/02/24, 12:48:01 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
RAVI RANJAN	
9113714591	
after exam
[07/02/24, 12:48:37 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
ARYAN GUPTA
	7379957166	
after exam
[07/02/24, 12:49:09 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
AJAY GOUR	
9644029231
	after exam 15 feb
[07/02/24, 12:49:41 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
AMIT KUMAR CHAKRAWARTI	
8349208722	
20 Feb
[07/02/24, 12:50:22 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
VINAY KUMAR AHIRWAR	
8959339982		
after exam Febuary
[07/02/24, 12:50:24 PM] annu❤️: Computer Science & Engineering-Data Science	
Technocrat Institute of Technology
AMIT KUMAR MEENA
Chetak 	9754914323	
In March 
Old prospect
[07/02/24, 12:54:27 PM] annu❤️: Computer Science & Engineering-Data Science	
Technocrat Institute of Technology	
MOHD OSAID Khan 
9343563282	
20 February
Old prospect
[07/02/24, 12:54:42 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
MOHAMMAD KAIF NAZIR	
9301561570	 
after exam
[07/02/24, 12:54:42 PM] ~ Hafsa , Coding Thinker: Name of Student: Ankit Kumar 
College name: BGI
Contact no: 8252170844
Branch: CS
Year: 2nd Yr old prospect 
Expected Date of Visit: After 17 Feb
[07/02/24, 1:00:59 PM] khushi e.c: Branch :-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Lakshmi Narain College of Technology & Science	
Name:-PARTH SONI
Contact:-	9826456622	
  Expected date :- 	10 Feb in m.p  nagar
[07/02/24, 1:04:27 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Oriental Institute of Science & Technology	PRANSHU GUPTA	9301389556	will come after holi
[07/02/24, 1:07:01 PM] ~ Memuna Coding Thinker: Name of Student: Saquib Siddiqui 
College name: All Saint's College 
Contact no: 8871451213
Branch: CS
Expected Date of Visit: 8 Feb
[07/02/24, 1:07:58 PM] khushi e.c: Branch :-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Lakshmi Narain College of Technology & Science
Name:-	PRANJAL JAIN
Contact:-	7879956660		
Expected date:-will think
[07/02/24, 1:11:15 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]
SHIVTAR KUMAR	
Chetak 	9981890358	
In March 
Old prospect
[07/02/24, 1:13:02 PM] ~ Deepali coding: Computer Science & Information Technology	Sagar Institute of Research & Technology	ABHISHEK KUMAR YADAV	8521366717	will come march indrapuri
[07/02/24, 1:13:23 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]
NISHCHAY GAUTAM
Indrapuri 	9329308168
In March 
Old prospect
[07/02/24, 1:14:02 PM] arpana e.c: Technocrats Institute of Technology [Excellence]
	SANJANA TIWARI
	9301460596
Old prospect
 will come 9 feb
[07/02/24, 1:14:35 PM] ~ Memuna Coding Thinker: Name of Student: khushi Chouksey 
College name: Sagar
Contact no: 9302753103
Branch: CS
Expected Date of Visit: will come after 1 week
[07/02/24, 1:18:06 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Data Science	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	SANDEEP PRAJAPATI	9165803693		will come 16 feb			chetak
[07/02/24, 1:18:52 PM] arpana e.c: Technocrats Institute of Technology [Excellence]
	KUSHAGRA SAHU
	6261466521
old prospect
will come 16 feb
[07/02/24, 1:21:03 PM] Neha mam e.c: Data science and data analytic me MP nagar ke liye kissi par student hai join ke liye
[07/02/24, 1:22:36 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	ROUNAK ZAMIL	
9534970908	
13 February
Old prospect
[07/02/24, 1:23:03 PM] Neha mam e.c: Ye batao
[07/02/24, 1:23:26 PM] kasim k: aj ayega ek
[07/02/24, 1:23:48 PM] Neha mam e.c: Admission batao
[07/02/24, 1:26:16 PM] Neha mam e.c: Sabji ko answer dena hai naki deen karke chupchap rehana hai
[07/02/24, 1:27:07 PM] Neha mam e.c: Sabhi *
[07/02/24, 1:27:56 PM] kasim k: aj ana wala tha ab kl ayaga mam  data science ka  aut 2 fsd ke hai aj ana wale haiii sham tk cnfrm karenge
[07/02/24, 1:29:23 PM] arpana e.c: Technocrats Institute of Technology [Excellence]
	SOURABH
	6265703550
Old prospect
will come  after 15 feb
[07/02/24, 1:33:07 PM] khushi e.c: Mam ek registration aane. Ka bol rahe hai
[07/02/24, 1:33:27 PM] khushi e.c: Ds ka hai. Evening tak
[07/02/24, 1:33:35 PM] khushi e.c: Aayenge
[07/02/24, 1:37:23 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	SHANI CHOUREY	
9575452725	
15 February
Old prospect
[07/02/24, 1:41:38 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
AMAN CHOUDHARY		7898402150	
15 February
Old prospect
[07/02/24, 1:45:48 PM] ~ Memuna Coding Thinker: Name of Student: Ayazul Haque
College name: All Saint's 
Contact no: 7491902274
Branch: EC
Expected Date of Visit: will come last Feb
[07/02/24, 1:48:39 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	
GAYATRI SAHU
	8303258714	
15 march ‎<This message was edited>
[07/02/24, 1:49:39 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	
HARSHITA JAISWAL	
8959069403
	15 feb will come
[07/02/24, 1:50:18 PM] anchal e.c: 4 August	Computer Science & Engineering	Patel College of Science & Technology	
MOSHARRAF ALAM	
9771944231	
will think after exam
[07/02/24, 1:50:54 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
ANKUJ MATRE	7
692821435	
after exam will come
[07/02/24, 1:51:29 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
MUKUL KUMAR
	7488361413	
after exam will come
[07/02/24, 1:52:16 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
SHIVAM KUMAR ASHISH
	7903819844	
march will come
[07/02/24, 1:52:46 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
MD NAHID RAJA
	9572611323
	march will come
[07/02/24, 1:53:16 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science
	RAUSHAN KUMAR SINGH
	8340282407	
will come march
[07/02/24, 1:53:50 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
MD KAIF	
9129818936	
march will come
[07/02/24, 1:54:31 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science
	AYUSH RUSIYA
	9301729541	
march
[07/02/24, 1:55:02 PM] anchal e.c: Computer Science & Engineering	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
ABHAY MISHRA
	6267850184	
will come march
[07/02/24, 1:55:29 PM] anchal e.c: Computer Science & Engineering	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
HIMANSHU DUBEY	
7909909902	
will come march
[07/02/24, 1:55:57 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
RUCHITA POTPHODE	
8305741640
	after 15 feb
[07/02/24, 1:58:31 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
ROHIT KUMAR	
9118559155	
march
[07/02/24, 2:11:53 PM] arpana e.c: Technocrats Institute of Technology [Excellence]
	BRAJKISHOR YADAV
	9285276946
Old prospect
will come 11feb
[07/02/24, 2:58:04 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
YOGESH SEN	
9303391712	
20 February
Old prospect
[07/02/24, 3:03:04 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology & Science
HEMANT KUSHWAHA		8269105703	
15 February
Old prospect
[07/02/24, 3:05:55 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology & Science
ADITYA MEHRA	NA
7389047491	
In March 
Old prospect
[07/02/24, 3:08:11 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Data Science	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	MONU KUSHWAH	6265035718	will come 1 March with Abhishek
[07/02/24, 3:11:06 PM] kasim k: Computer Science & Engineering	
All Saints' College of Technology	
AHMED SARDAR	
7389596503	
march end 
(old prospect)
[07/02/24, 3:21:00 PM] ~ Deepali coding: Computer Science & Engineering	Bansal Institute of Research, Technology & Science	SHEKHAR SEN	8770930541	will come 14 feb indrapuri
[07/02/24, 3:27:36 PM] arpana e.c: Technocrat Institute of Technology
	ABHISHEK KUMAR
	7739056659
old propect
will come 20 march
[07/02/24, 3:28:35 PM] ~ Deepali coding: Computer Science & Engineering	Millennium Institute of Technology & Science	AMARESH VISHWAKARMA	8468048287	will come march mid
[07/02/24, 3:30:13 PM] ~ Hafsa , Coding Thinker: Name of Student: Omprakash Verma 
College name: Bansal College 
Contact no: 8305038398
Year: 1st Yr 
Expected Date of Visit: Will come in March
[07/02/24, 3:32:41 PM] ~ Deepali coding: Electronics & Communication Engineering	VNS Group of Institutions	SHUBHAM AGRAWAL	7000205327 will come feb end
[07/02/24, 3:34:32 PM] arpana e.c: Technocrat Institute of Technology
	AMIT KUMAR
	9334695610
Old prospect
will come 20 feb
[07/02/24, 3:37:04 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Oriental Institute of Science & Technology
ADITYA SAHU	
9301460346	
In March 
Old prospect
[07/02/24, 3:44:59 PM] khushi e.c: Branch :-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Lakshmi Narain College of Technology & Science	
Name :-SHIVANSH RAWAT
Contact:-	7697009114	
Expected date :-	will think
[07/02/24, 3:49:33 PM] annu❤️: Electronics & Communication Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
SHANI KUMAR PATEL	
8120013499	
10 February
Old prospect
[07/02/24, 3:50:02 PM] arpana e.c: Technocrats Institute of Technology [Excellence]
	ABHISHEK DUBEY
	8349369757
Already visited
come for revist 16feb
[07/02/24, 3:51:10 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
RUPESH KESHARWANI	
7241169472
	after exam
[07/02/24, 3:51:41 PM] anchal e.c: Information Technology	Bansal Institute of Science & Technology
	NIDA NAAZ	
8817083575	
after exam
[07/02/24, 3:52:13 PM] anchal e.c: Information Technology	Bansal Institute of Science & Technology	
SOURABH CHIDAR	
9713353106	
after 15 feb
[07/02/24, 3:52:21 PM] annu❤️: Electronics & Communication Engineering	
Sagar Institute of Science Technology & Engineering	
SHIVAM SHARMA	
7275007501	
In March 
Old prospect
[07/02/24, 3:52:22 PM] ~ Hafsa , Coding Thinker: Name of Student: Kumar Gaurav
College name: LNCT
Contact no: 6200359473
Year: 2nd Year
Expected Date of Visit: Will come after 14 Feb
[07/02/24, 3:52:44 PM] anchal e.c: Computer Science & Engineering	Bansal College of Engineering
	VISHAL SINGH RAJPUT	
6260034532	
will think after exam
[07/02/24, 3:53:14 PM] anchal e.c: Computer Science & Engineering	Bansal College of Engineering	
SAHIL PURI	
9302070377	
after exam will come
[07/02/24, 3:54:01 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence	Technocrat Institute of Technology	
ADARSH VERMA
	9630330977	
18 19 feb
[07/02/24, 3:54:27 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	
PRINCE SINGH
	9973353565	
after exam will come
[07/02/24, 3:55:00 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence	Technocrat Institute of Technology	
ANANT DUBEY	
9669729283
	march will come
[07/02/24, 3:55:41 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence	Technocrat Institute of Technology	
ANSHUL PAWAR
	8085396635	
20 Feb
[07/02/24, 3:55:54 PM] ~ Deepali coding: Computer Science & Engineering	Radharaman Engineering College	ANIL YADAV	8210140091	visit will come 17 feb
[07/02/24, 3:56:46 PM] annu❤️: Electronics & Communication Engineering	
Sagar Institute of Science Technology & Engineering	
UDAY KUMAR IRPACHI	
9131596106	
In March 
Old prospect
[07/02/24, 3:56:48 PM] arpana e.c: with 2 frinds ..anirudh
[07/02/24, 3:57:13 PM] arpana e.c: ‎This message was deleted.
[07/02/24, 3:57:45 PM] arpana e.c: VNS Group of Institutions
	ARPIT PANDEY
	7722933362
Already visited
come for revist 17 feb 
with frind abhay
[07/02/24, 4:01:04 PM] khushi e.c: Branch :-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Lakshmi Narain College of Technology & Science
Name:-	SRISHTI
Contact:-	7992344110	
Expected date :-	will think
[07/02/24, 4:05:22 PM] arpana e.c: Millennium Institute of Technology & Science	
HIMANSHU VEER
	9399315136
Already visited
come for Admision april
[07/02/24, 4:14:42 PM] arpana e.c: Technocrat Institute of Technology
	SAURABH PATHAK
	9179740448
Already visited
come for admision feb end
[07/02/24, 4:18:00 PM] arpana e.c: Technocrat Institute of Technology
	SHAURYAM RAJ
	8409767886
Old prospect
will come 20 feb
[07/02/24, 4:24:30 PM] khushi e.c: Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:-Lakshmi Narain College of Technology & Science	
Name:-SURYAPRATAP SINGH UMATH
Contact:-	8319832780		
Expected date:-after 30 Feb  indrapuri
[07/02/24, 4:27:15 PM] ~ Hafsa , Coding Thinker: Name of Student: Piyush Sen 
College name: Hamidia
Contact no: 7898462204
Branch: BCA old prospect 
Expected Date of Visit: Will come in 2-3 days
[07/02/24, 4:37:06 PM] ~ Hafsa , Coding Thinker: Name of Student: Shivam Saket
College name: Bansal 
Contact no: 8237840770
Branch: CS old prospect 
Year: 1st Yr
Expected Date of Visit: Will come after 20 Feb
[07/02/24, 4:40:02 PM] kp sir: Aaj kisi ka prospects aane wala hai indrapuri
[07/02/24, 4:42:35 PM] Lalita Sahu: Sir enquriy pad par call kr  rhi hu  isliye
[07/02/24, 5:21:36 PM] kp sir: Team aaplog 
Indrapuri and mp nagar main Batches kabse announce karrahe hoo apni pitch main .
Data science and FSD dono ke
[07/02/24, 5:22:01 PM] ~ Deepali coding: Sir 10 hi bol rhe hai abhi hum
[07/02/24, 5:22:14 PM] ~ Deepali coding: But students after 12-15 tk hi aane ka bol rhe hai
[07/02/24, 5:26:59 PM] arpana e.c: students after 12 feb ka bol rhe
[07/02/24, 5:27:38 PM] Neha mam e.c: Sir Indripuri and MP nagar individually baat kar rahe hai
[07/02/24, 5:32:50 PM] Lalita Sahu: Sir 10feb ka bta rhe h
[07/02/24, 5:32:55 PM] kp sir: Haan maam ,muje yeah Janna hai ki Indrapuri main bacche Kab ka bolrahe hain
[07/02/24, 5:33:12 PM] kp sir: Kitne hai Jo aarahe hain
[07/02/24, 5:33:48 PM] annu❤️: Electronics & Communication Engineering	
Oriental Institute of Science & Technology	
AYUSH KUMAR
8252885896	
In March 
Old prospect
[07/02/24, 5:34:20 PM] Lalita Sahu: 6student h jo 10feb ka bol rhe or kuch students h jo 15to 20feb ka bol rhe h
[07/02/24, 5:35:54 PM] kp sir: Kon se course main 
FSD waale yaa Data science main
[07/02/24, 5:36:34 PM] annu❤️: Electronics & Communication Engineering	
Oriental Institute of Science & Technology
ANKIT SAHU
8982945057	
Indrapuri 	20 February
Old prospect
[07/02/24, 5:36:36 PM] Lalita Sahu: Fsd k jyada students h sir
[07/02/24, 5:36:59 PM] kp sir: Sabhi se input chaiye mujee ki indrapuri main kon kon se course main prospect hai Jo admission lene ka Feb main
[07/02/24, 5:37:17 PM] kp sir: Ok
[07/02/24, 5:37:20 PM] Lalita Sahu: Ok sir
[07/02/24, 5:42:10 PM] ~ Hafsa , Coding Thinker: Name of Student: Ajay Patel 
College name: Hamidia 
Contact no: 8839041680
Branch: BCA old prospect 
Expected Date of Visit: Will come after 16 Feb
[07/02/24, 5:53:12 PM] arpana e.c: Technocrat Institute of Technology
	MOHAMMAD SHOAIB
	7879955909
Old prospect
will come 10 feb with 2 frind ..aniket and rituraj
Inderpuri
[07/02/24, 5:57:40 PM] kp sir: Harshit khatarkar ka kya feedback hai durgaa ,visited hai yeah
[07/02/24, 5:58:45 PM] kp sir: Vijay meethe and Krishna Mahajan ka kya feedback hai Shilpa maam ,visited hai
[07/02/24, 5:59:22 PM] kp sir: MD. Aksh ka bhi Shilpa maam
[07/02/24, 6:00:00 PM] arpana e.c: Technocrat Institute of Technology
	RAUSHAN KUMAR
	9102442914
old prospect
will come 18 feb
Inderpuri
[07/02/24, 6:00:19 PM] khushi e.c: Sir 2 minutes
[07/02/24, 6:01:52 PM] ~ Deepali coding: Computer Science & Engineering	Radharaman Engineering College	SHUBHAM KUMAR	9262637273	will come 10 Feb chetak
[07/02/24, 6:05:56 PM] kp sir: OK Bata doo
[07/02/24, 6:18:20 PM] ~ Deepali coding: Computer Science & Engineering	Lakshmi Narain College of Technology & Science	PRAKASH RAJ	6205148339	will come 8 feb indrapuri
[07/02/24, 6:37:38 PM] ~ Deepali coding: Computer Science & Engineering	Lakshmi Narain College of Technology & Science	PARV CHOUDHARY	6268932423	will come march indrapuri
[07/02/24, 6:56:16 PM] ~ Hafsa , Coding Thinker: Name of Student: Aman Kumar Singh 
College name: OIST
Contact no: 7669652458
Branch: CS
Year: 2nd Year 
Expected Date of Visit: Will come after practicals
[07/02/24, 7:00:05 PM] annu❤️: Electronics & Communication Engineering	
NRI Institute of Information Science & Technology	
SUSHMITA SEN
7722952366		
In March 
Old prospect
[07/02/24, 7:02:20 PM] annu❤️: Electronics & Communication Engineering	
NRI Institute of Information Science & Technology	
SHIVAM KUMAR
6200140427	
In March 
Old prospect
[07/02/24, 7:03:46 PM] kasim k: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
KALYANI DESHBHARTAR	
7000482947	
march batch
[07/02/24, 7:03:58 PM] kasim k: Artificial Intelligence and Machine Learning	
Sagar Institute of Research & Technology	
PAWAN VISHWAKARMA	9770876521	
march batch
[07/02/24, 7:04:17 PM] kasim k: Artificial Intelligence and Machine Learning	
Sagar Institute of Research & Technology	
SOURABH PATEL	
6261115870	
march plan
[07/02/24, 7:04:31 PM] kasim k: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
ARVIND SEN	
6264067910	
27Feb
[07/02/24, 7:04:42 PM] kasim k: Computer Science & Engineering	
Lakshmi Narain College of Technology	
HARISH BAGHEL	
6260574215	
19 Feb
[07/02/24, 7:04:53 PM] kasim k: Artificial Intelligence and Data Science	
J.N. College of Technology	
AYUSH KUMAR DUBEY	9522342772	
25Feb
[07/02/24, 7:05:04 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
HARSHRAJ SINGH CHOUHAN
9589586748	
18 feb after exam
[07/02/24, 7:05:15 PM] kasim k: Artificial Intelligence and Data Science	
J.N. College of Technology	
RITIKA NIGAM	
6267250326	.
13feb
[07/02/24, 7:05:25 PM] kasim k: Artificial Intelligence and Machine Learning	
J.N. College of Technology	
WASIM AKHTAR	
8294659146	
17 feb machine learning
[07/02/24, 7:05:27 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	
College:-Surabhi College of Engineering & Technology	
Name:-ANURAG TIWARI
Contact:-	9340920892
Expected date:-		 9 Feb  m.p nagar
[07/02/24, 7:05:29 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence	Technocrat Institute of Technology
	SONU NAYAK
	8120165149	
march will come
[07/02/24, 7:05:36 PM] kasim k: Information Technology	
Oriental Institute of Science & Technology	
MD OWAIS ALAM	
9798085581	
20Feb
[07/02/24, 7:05:44 PM] kasim k: Electrical & Electronics Engineering	
J.N. College of Technology	
SAKSHI KUNWAR RATHOD	
9754233628	
march batch
[07/02/24, 7:05:46 PM] kasim k: Electrical & Electronics Engineering	
J.N. College of Technology	
CHANDAN KUMAR	
7488628557	
already visited plan in  feb end  batch
[07/02/24, 7:06:09 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence	Technocrat Institute of Technology	
DEEPANSHU KHOUSHI	
7723094938	
will think
[07/02/24, 7:06:51 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence	Technocrat Institute of Technology	
HARSHIT FARKARE	
7724916729	
18 feb will come
[07/02/24, 7:07:06 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
RAJAT KUMAR	
9557608718		
after 20  feb
[07/02/24, 7:07:18 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence	Technocrat Institute of Technology	
PANKAJ KUMAR YADAV	
9616236977	
17 feb will come
[07/02/24, 7:07:46 PM] anchal e.c: Information Technology	Technocrat Institute of Technology	
RAMLAKHAN MALVIYA	
9399464718	
after exam
[07/02/24, 7:08:12 PM] anchal e.c: Information Technology	Technocrat Institute of Technology
	ABHAY PRATAP SINGH	
8319756509	
April will come 		fsd
[07/02/24, 7:08:39 PM] anchal e.c: Information Technology	Technocrat Institute of Technology
	AMAN KUMAR SINGH
	6201960003
	15 feb mp nagar
[07/02/24, 7:10:09 PM] anchal e.c: Information Technology	Technocrat Institute of Technology	
AALEKH MINAREY
	8103499703	
after exam 15 feb
[07/02/24, 7:11:31 PM] anchal e.c: Computer Science & Bussiness System	Oriental Institute of Science & Technology	
AKANKSHA VERMA	
9516346996	
8,9 feb
[07/02/24, 7:12:03 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Data Science	Technocrat Institute of Technology
	ABHYANSHU BENDE	
9755723930	
will come March
[07/02/24, 7:12:33 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Data Science	Technocrat Institute of Technology	
DEVANSH RAGHUWANSHI	
7389639732	
will come after exam
[07/02/24, 7:12:55 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	ARVIND NAGPURE	8085919210	will come 12 feb chetak bridge
[07/02/24, 7:13:01 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Data Science	Technocrat Institute of Technology	
RISHIRAJ RAGHUWANSHI
	9691872062	
after exam will come
[07/02/24, 7:13:32 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Lakshmi Narain College of Technology	
DIKSHANT BAIRAGI	
9039384652	
march will come
[07/02/24, 7:14:03 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	
HARSH RAJ SINGH	
9471473020	
after exam will come
[07/02/24, 7:14:34 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	
DEEPAK DHAKAD
	9669606687
	16 feb
[07/02/24, 7:15:04 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	
RISHAV KUMAR YADAV	
8517081425	
10 11 Feb
[07/02/24, 7:16:15 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
VEDANT CHOURASIYA-	
6266505656		
plan after exam		
13Feb
[07/02/24, 7:17:16 PM] anchal e.c: Computer Science & Engineering	Lakshmi Narain College of Technology & Science	
RAHUL MATHANKER	
7898042398	
8 feb
[07/02/24, 7:17:33 PM] anchal e.c: Computer Science & Engineering	Bansal College of Engineering	
ROHAN KEER	
8319416315	
after exam
[07/02/24, 7:17:59 PM] anchal e.c: Electronics & Communication Engineering	Sagar Institute of Research & Technology	
NISHANK DIXIT
	8839809059	
 after exam
[07/02/24, 7:18:30 PM] anchal e.c: Electronics & Communication Engineering	Sagar Institute of Research & Technology	
MOHD IBAD KHAN	
6265533886
	will come 7,8 feb
[07/02/24, 7:19:22 PM] anchal e.c: Electronics & Communication Engineering	Sagar Institute of Research & Technology	
POORVA VISHWAKARMA
	9981508159	
after exam will come
[07/02/24, 7:20:01 PM] anchal e.c: Electronics & Communication Engineering	Lakshmi Narain College of Technology
	RAMAN PANDIT	
7222936532	
after exam
[07/02/24, 7:21:31 PM] kasim k: J.N. College of Technology	
NIKHIL SINGH	
9670996264	
after exam 14feb
[07/02/24, 7:21:40 PM] kasim k: J.N. College of Technology	
ASHUTOSH GUPTA	
8305707631	
after exam 18 feb
[07/02/24, 7:21:50 PM] kasim k: J.N. College of Technology	
ADITYA KUMAR CHOUDHARY
	6206748201	
after exam 28feb
[07/02/24, 7:21:53 PM] kasim k: J.N. College of Technology	
DEEPAK MANDLOI	
6261942839	
after exam ⭐️ 19 feb
[07/02/24, 7:23:37 PM] arpana e.c: Bansal College of Engineering
	DEEPESH KUMAR
	8305970611
old prospect
will come 5 march
[07/02/24, 7:27:50 PM] arpana e.c: Bhopal Institute of Technology, Bangrasia	
ANKIT KUMAR
	9336854050
old prospect
will come after 20 feb
[07/02/24, 9:09:02 PM] khushi e.c: ‎This message was deleted.
[07/02/24, 9:09:07 PM] khushi e.c: ‎This message was deleted.
[07/02/24, 9:10:07 PM] khushi e.c: Harshit katnakar ko ek baar or inquiry chaiye
[07/02/24, 9:10:36 PM] khushi e.c: Sir M.p Nagar mein
[07/02/24, 10:51:53 PM] kp sir: OK toh bulalooo
[07/02/24, 10:54:22 PM] khushi e.c: ‎This message was deleted.
[07/02/24, 10:54:47 PM] khushi e.c: Ji sir 9 Feb ko ayenge
[08/02/24, 11:45:11 AM] Harsh sir tl: Good morning team,

I trust you're all well. Let's start today with a shared commitment to focus on our work and achieve targets for the institute. Your hard work hasn't gone unnoticed, and I believe in each one of you. Don't let your potential go untapped; together, let's elevate and grow. Our collective efforts will pave the way for success. Here's to a day of dedication and achievement.

Regards,
[HARSH VARDHAN]
[08/02/24, 12:02:40 PM] annu❤️: Computer Science & Engineering	
Bansal Institute of Research & Technology
DEEPAK THAKUR
9301446704	
Indrapuri 	In March 
Old prospect
[08/02/24, 12:15:51 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology	
ABHISHEK RANJAN
7091633234	
Will come Python 	
10 February
Old prospect
[08/02/24, 12:33:13 PM] anchal e.c: Electrical Engineering	Sagar Institute of Science Technology & Engineering	
RAMGOPAL PRAJAPATI	
9302479341	
10 feb c,c+
[08/02/24, 12:33:56 PM] khushi e.c: Branch :-Electrical & Electronics Engineering	
College:-Surabhi College of Engineering & Technology	

Name:-KHUSHAL GAYDHANE
Contact:-	9755992082		
Expected date:-after 13 Feb  (m. p nagar)
[08/02/24, 12:38:36 PM] ~ Deepali coding: Electrical & Electronics Engineering	Sagar Institute of Research & Technology	SHIVENDRA PANDEY	7697612508	will come 13 feb indrapuri (+ friends)
[08/02/24, 12:39:51 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology	
AKASH PATEL	7049695103
Will Come 13 January For admission 
Old prospect
[08/02/24, 12:39:54 PM] khushi e.c: Branch :-Electrical & Electronics Engineering
College:-	Surabhi College of Engineering & Technology
Name:-	MONOO PRAJAPATI
Contact:-	9617933064		
Expected date:-after 1 week
[08/02/24, 12:51:08 PM] ~ Hafsa , Coding Thinker: Will come on 9 Feb
[08/02/24, 12:57:11 PM] ~ Deepali coding: Electronics & Communication Engineering	Technocrats Institute of Technology [Excellence]	HEMANT GURJAR	6261845435	will come after 12 feb indrapuri with friend( Sanjay)
[08/02/24, 1:00:54 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology
MANISH KUMAR MALVIYA	
9171165793	
Will come C++ DSA
15 February
Old prospect
[08/02/24, 1:04:04 PM] kasim k: name :- saloni pal
number - 6264824329
date -18 feb 
revisit plan in indrpuri 
(already visited)
[08/02/24, 1:05:34 PM] annu❤️: Computer Science & Engineering	
Millennium Institute of Technology & Science
AAYUSH VERMA	6266191974	 
Will Come	With friends 
15 February Call back
Old prospect
[08/02/24, 1:16:34 PM] ~ Deepali coding: 4TH	Electronics Communication	University institute of technology,RGPV Bhopal	ANUJ KUSHWAHA	8770234882	will come after 16 feb
[08/02/24, 1:25:16 PM] annu❤️: Computer Science & Engineering	
Millennium Institute of Technology & Science
ANKIT KUMAR
8210288392	
Will come 	8 February
With friends
Old prospect
[08/02/24, 1:33:40 PM] ~ Memuna Coding Thinker: Name of Student: Sameem Muhammad 
College name: Surabhi clg
Contact no: 7905466182
Branch: CS
Expected Date of Visit: After 15 Feb
[08/02/24, 1:59:32 PM] annu❤️: Will come 9 Feb with friend
[08/02/24, 2:51:57 PM] annu❤️: Computer Science & Engineering	
Millennium Institute of Technology & Science	
RASHID HUSAIN
9264487623	 	
25 February
Old prospect
[08/02/24, 3:06:29 PM] ~ Memuna Coding Thinker: Name of Student: MD Kaif
College name: Surabhi clg
Contact no: 7572016639
Branch: CS
Expected Date of Visit: After 12 Feb
[08/02/24, 3:12:27 PM] kasim k: Name :- Yash 
Number - 81209 26832
 coming today chetak bridge revisit
[08/02/24, 3:19:47 PM] annu❤️: Computer Science & Engineering	
Technocrats Institute of Technology - Computer Science and Engineering
KIRTI TIWARI	8959117058	
After Holi 
Old prospect
[08/02/24, 3:21:46 PM] annu❤️: Computer Science & Engineering	
Technocrats Institute of Technology - Computer Science and Engineering	
MD ALI UDDIN
8809255929
In March
Old prospect
[08/02/24, 3:24:48 PM] ~ Deepali coding: 3RD	Computer Science & Engineering	Technocrats Institute of Technology - Computer Science and Engineering	ARUN	7225077157 will come march
[08/02/24, 3:31:29 PM] anchal e.c: Will come today
[08/02/24, 3:39:10 PM] anchal e.c: Computer Science & Engineering	Patel College of Science & Technology	
vishal Yadav 	
9508952958	
18 19 feb
[08/02/24, 3:42:20 PM] annu❤️: Computer Science & Engineering	
Technocrats Institute of Technology - Computer Science and Engineering	
PRABHAT PRABHANJAN
8051422360	
Will come  	In March 
Old prospect
[08/02/24, 3:43:02 PM] anchal e.c: Electronics & Communication Engineering	Lakshmi Narain College of Technology	
SUMIT MISHRA	8957260953	
after exam 17 18 Feb
[08/02/24, 3:58:12 PM] khushi e.c: Branch:-Electrical & Electronics Engineering	
College:-Millennium Institute of Technology & Science	
Name:-SHASHI RAJ
Contact:-	9525536512		
Expected date:-after 5 March
[08/02/24, 3:59:30 PM] annu❤️: Computer Science & Engineering	
Technocrats Institute of Technology - Computer Science and Engineering	
RANJEET BHANSAR
9179255738	
Will come 12 February with sourabh
Indrapuri 
Old prospect
[08/02/24, 4:01:45 PM] khushi e.c: Branch:-Electrical & Electronics Engineering
College:-	Millennium Institute of Technology & Science	
Name:-YUSUF ALI
Contact::	7004718913		
Expected date:-will think after 25 Feb
[08/02/24, 4:10:06 PM] annu❤️: Abhishek Malviya - 9753883622 
Will Come 15 February
Indrapuri 
Old prospect
[08/02/24, 4:12:50 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	
SAKET KUMAR	
7461940168	
17feb ‎<This message was edited>
[08/02/24, 4:14:07 PM] ~ Hafsa , Coding Thinker: Name of Student: Sagar Sen 
College name: Corporate College 
Contact no: 9361599247
Branch: CS
Year: 2nd Yr old prospect 
Expected Date of Visit: 11 Feb ( Indrapuri ) ‎<This message was edited>
[08/02/24, 4:15:06 PM] kp sir: 11 jan toh nikal gyai
[08/02/24, 4:16:34 PM] kp sir: 13 jan Kab
[08/02/24, 4:16:59 PM] annu❤️: 13 February
[08/02/24, 4:18:11 PM] kp sir: Aaj aarahi hai kya
[08/02/24, 4:18:28 PM] kp sir: Aaj Kab tak aarahi hai
[08/02/24, 4:19:10 PM] kp sir: Yeah aaj aarahi hai yaa Kal
[08/02/24, 4:19:12 PM] anchal e.c: ‎This message was deleted.
[08/02/24, 4:20:06 PM] anchal e.c: Evening me aega
[08/02/24, 4:22:39 PM] kasim k: + gaurav  + 3 friends
[08/02/24, 4:24:52 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
LEENA KESHNIYA	
9343216398	
end of feb
[08/02/24, 4:30:30 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
ASHISH AHIRWAR	
6268401268	
march will come
[08/02/24, 5:06:15 PM] kasim k: adarsh
[08/02/24, 5:13:24 PM] Neha mam e.c: Kasim 4 aa gye
[08/02/24, 5:14:35 PM] kasim k: nhi mam cl nahi utaya avi
[08/02/24, 5:14:47 PM] Neha mam e.c: Are
[08/02/24, 5:14:58 PM] Neha mam e.c: Karo registration aaj sab
[08/02/24, 5:25:01 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
VISHAL SALLAM
	7489132682	
9,10 feb 
mp nagar
[08/02/24, 5:27:37 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	MOHAMMAD TAHA KHAN	8767256075	will come next week indrapuri
[08/02/24, 5:29:33 PM] ~ Hafsa , Coding Thinker: Name of Student: Gautam Patel
College name: OIST
Contact no: 9334565057
Branch: CS
Year: 2nd Year 
Expected Date of Visit: 11 Feb
[08/02/24, 5:34:18 PM] kasim k: 367	Computer Science & Engineering	
Technocrat Institute of Technology	
ABHISHEK PATEL	
8349348081		
after exam	12feb indrpuri
[08/02/24, 5:36:06 PM] annu❤️: Hitendra kushwaha - 8815361171
Will Come FSD 
13 February
Already visited
[08/02/24, 5:39:45 PM] annu❤️: Neha vishwakarma - 7828185941
Will Come with Somya , Tanya , Anushree 
Already visited 
13 February
Old prospect
[08/02/24, 5:42:34 PM] arpana e.c: Lakshmi Narain College of Technology
	DEEPESH MEHTA
	8236044148
will come 27 feb
[08/02/24, 5:42:39 PM] kp sir: Yeah bhi lightened jaaye ki kaha join karenge Mp nagar ya indrapuri main
[08/02/24, 5:43:19 PM] annu❤️: Okk sir
[08/02/24, 5:45:24 PM] kp sir: Sabhi log yeah jaaror add kartee jaaye jo prospects banrahe hai ki wo kaha join karenge ya visit karenge Mp nagar ya indrapuri
[08/02/24, 5:53:18 PM] Harsh sir tl: Lalita ekk bhi prospect nai bana abhi tk ?
[08/02/24, 5:56:42 PM] Lalita Sahu: Sir 2 hi procpect bne sham ko ek sath update krugi call kr rhi hu
[08/02/24, 5:58:41 PM] Harsh sir tl: Team, good day! Kindly share updates promptly to keep everyone in the loop. Your swift responses will help us stay aligned and make informed decisions. Let's keep the communication flowing for seamless collaboration. Thanks!
[08/02/24, 5:59:33 PM] anchal e.c: Computer Science & Engineering	Patel College of Science & Technology	
ANKIT KUMAR	
9262346367	
after exam will come
[08/02/24, 6:00:19 PM] arpana e.c: Lakshmi Narain College of Technology
	HANUMAN KUSHWAHA
	9165015631
2nd year
will come 1 mRch
 mp nagar
[08/02/24, 6:02:10 PM] kasim k: Artificial Intelligence and Machine Learning	
J.N. College of Technology	
PRANAV ASATI	
9691384141	
july plan after 7 semester (indrpuri)
[08/02/24, 6:08:30 PM] anchal e.c: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
ANUJ KUMAR SINGH	
6207305710	
18 19 feb 
mp nagar
[08/02/24, 6:10:24 PM] arpana e.c: VNS Group of Institutions
	PANKAJ VISHWAKARMA
	8319709213
2nd year
will come after 20 feb
mp nagar
[08/02/24, 6:17:24 PM] arpana e.c: VNS Group of Institutions
	SUNNY KUMAR
	9334817261
will come 16 feb
mp nagar
[08/02/24, 6:20:53 PM] ~ Deepali coding: Will come 13 feb chetak + friend tejasswi
[08/02/24, 6:24:47 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
ROHAN RAJ	
7764097757	
13,14 feb 	
Indrapuri
[08/02/24, 6:25:45 PM] arpana e.c: VNS Group of Institutions
	DEVRAJ MARAN
	7470575047
will come after exam 
mp nagar
[08/02/24, 6:30:03 PM] kasim k: Computer Science & Engineering	
Corporate Institute of Science & Technology	
ABHIRAJ CHOUHAN	
9755494110				
13Feb
[08/02/24, 6:35:28 PM] khushi e.c: Branch :-Electrical & Electronics Engineering
College:-	Bansal College of Engineering
Name:-	RINKESH PORTE
Contact:-	8269845870		
Expected date:-after 13 Feb
[08/02/24, 6:52:09 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science
	NANDLAL RATHOD	
9691621954	
20 feb 
 mp nagar
[08/02/24, 6:57:19 PM] anchal e.c: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
ASHWINI KUMAR SINGH	
9006631843
	after exam will come
[08/02/24, 7:19:11 PM] anchal e.c: Computer Science & Engineering	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
SHAHNAWAZ ALAM	8092225760	
after 20 feb
 mp nagar
[09/02/24, 12:10:21 PM] ~ Chauhan Shilpa: Will come today mp nagar 1 pm
[09/02/24, 12:22:24 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
ANIL MEHRA	
8349951803
Will Come Today
Chetak
Old prospect
[09/02/24, 12:22:31 PM] annu❤️: With friend
[09/02/24, 12:31:32 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Oriental Institute of Science & Technology	MONU TYAGI	7746046864	will come march start
[09/02/24, 12:34:06 PM] Neha mam e.c: @916260753147 status lagate samme thode check kar liya karo laga kya rahi ho
[09/02/24, 12:34:46 PM] anchal e.c: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
PRASENDRA LODHI	
8602559282	
will come March 
 mp nagar
[09/02/24, 12:43:24 PM] anchal e.c: Computer Science & Engineering	
Radha Raman Institute of Technology & Science
	MAAZ USMANI	7324886683	
will come March 
mp nagar
[09/02/24, 12:49:50 PM] Neha mam e.c: @917489380471 tum log status lagte samme bilkul  check bhi nahi karte kya
[09/02/24, 12:51:08 PM] khushi e.c: Sorry mam
[09/02/24, 1:14:21 PM] anchal e.c: Information Technology	Bansal Institute of Science & Technology
	AMAN SINGH DANGI	
7389070820
	10 Feb fsd 
mp nagar
[09/02/24, 1:17:13 PM] ~ Deepali coding: Computer Science & Engineering	Sagar Institute of Research & Technology Excellence	DEV RAJPUT	7489763650	will come 20 feb + friends
[09/02/24, 1:18:11 PM] annu❤️: Computer Science & Engineering	
Mittal Institute of Technology
ASHISH KUMAR PATEL	6261872569	
Call back 	In March 
Old prospect
[09/02/24, 1:27:52 PM] Lalita Sahu: Computer Science & Engineering	
IES's College of Technology	
SONU KUMAR DUBEY	
9835944870	
Will think (CRT	)
[09/02/24, 1:34:19 PM] anchal e.c: Electrical & Electronics Engineering	
Bansal Institute of Research & Technology
	ANJALI SINGH
	6261964793
 will think
[09/02/24, 1:36:03 PM] ~ Deepali coding: Computer Science & Engineering	Sagar Institute of Research & Technology Excellence	PRINCE TRIPATHI	9770631393	will come march end																				with 4 friends chetak
[09/02/24, 1:48:26 PM] ~ Deepali coding: Computer Science & Engineering	Sagar Institute of Research & Technology Excellence	PRAFULL BISEN	9753358952	will come 18 feb chetak
[09/02/24, 2:38:57 PM] Neha mam e.c: @918085394718 jo with friend likh raha hai usko accept nahi karenge apan data utana hi hai sabke pass pahuch chuka hai data 1-1 baar name mention karna compulsory hai jisko samasya hai to aap uska koi prospect nahi likhi
[09/02/24, 2:39:32 PM] Neha mam e.c: Kitni baar bole chuke hai with friend nahi chalega to bhi baar baar likha jata hai
[09/02/24, 2:41:03 PM] Neha mam e.c: @918085394718 iss Sunday Indripuri ki student ka test plan kar lo
[09/02/24, 2:41:19 PM] Neha mam e.c: Data science and full stack dono
[09/02/24, 2:41:50 PM] Harsh sir tl: For sure mam
[09/02/24, 2:42:07 PM] Harsh sir tl: Ok mam
[09/02/24, 2:45:07 PM] Harsh sir tl: Team, kindly note that for each prospect, include the names of all individuals accompanying them. Without this information, we won't consider them as part of your prospects. Your cooperation in providing complete details is appreciated
[09/02/24, 3:07:37 PM] ~ Deepali coding: Electronics & Communication Engineering	Bansal Institute of Research & Technology	RANJNA KASHYAP	6260955264	will come 17 feb indrapuri
[09/02/24, 3:25:48 PM] ~ Deepali coding: Computer Science & Engineering-Data Science	Oriental College of Technology	VIVEK PATEL	8462926853	will come 17 Feb
[09/02/24, 3:27:57 PM] khushi e.c: Branch :-Computer Science & Engineering	
College:-Sagar Institute of Research & Technology
Name :-	DEEPAK MEHTA
Contact:-	7873468788	
Expected date :-	will think
[09/02/24, 3:30:58 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology
NITESH KUMAR MEENA
7067152640 
Will come Java 
Call back 11 February 
Old prospect
[09/02/24, 3:33:23 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Oriental Institute of Science & Technology	HARI SAHU	9329403626	will come march start with atharv and ashish
[09/02/24, 3:34:10 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Data Science	
Technocrat Institute of Technology
MOHAMMAD AKRAM ALI
8358909946	
Will come 	15 February
Old prospect
[09/02/24, 3:36:34 PM] annu❤️: Computer Science & Engineering	
Patel College of Science & Technology	
AMIT KUMAR VARMA
9131103924	
Will come 	11 February
Old prospect
[09/02/24, 3:39:46 PM] annu❤️: Computer Science & Engineering	
Patel College of Science & Technology	
KIRTAN KOUSHAL
9301015825	
Will come 	In March
Old prospect
[09/02/24, 3:44:24 PM] annu❤️: ‎This message was deleted.
[09/02/24, 3:45:00 PM] ~ Chauhan Shilpa: Name :- Yuvraj
Number: - 8709966170
College: - lnct
Branch :-Computer Science & Engineering
Year: 2nd Yr
Expected date of visit: - 15 February indrapuri
[09/02/24, 3:45:16 PM] annu❤️: Computer Science & Engineering	
Trinity Institute of Technology & Research	
ANSARI MOHD SAAD MOHAMMAD FAIYAZ
9156577091	
 In March
[09/02/24, 3:54:25 PM] khushi e.c: Branch :-		Computer Science & Engineering	
College:-Bhopal Institute of Technology & Science, Bangrasia
Name :-	KARTIKEY DUBEY
Contact:-	9956919494			
Expected date:-will think
[09/02/24, 3:55:48 PM] annu❤️: Electronics & Communication Engineering	
Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
TANIYA SAHU
7089808949	
Will come 	In March 
Old prospect
[09/02/24, 4:14:53 PM] khushi e.c: Branch		Computer Science & Engineering	
College:-Bhopal Institute of Technology & Science, Bangrasia
Name:-
	LAVKESH KUMAR
Contact :-	9294627678	
Expected date :-		after 25 March
[09/02/24, 4:16:44 PM] ~ Chauhan Shilpa: Name of Student: Ashraf 
College name: Trinity 
Contact no: 9431037664
Branch: CSE
Year: 1ST
Expected Date of Visit: 20 February
[09/02/24, 4:29:05 PM] khushi e.c: Branch :-Computer Science & Engineering	
College:-Bhopal Institute of Technology & Science, Bangrasia
Name :-	MD KITABUDDIN
Contact:-	9065489148		
Expected date:-	after 25 April
[09/02/24, 4:43:31 PM] kasim k: Computer Science & Engineering-Data Science	
Oriental College of Technology
PARTH KOTWE	
7879264554		
will think indrpuri	
11Feb
[09/02/24, 5:11:28 PM] anchal e.c: Computer Science & Engineering
	Technocrats Institute of Technology & Science	
AMAN PATLE	9691718077				
Will come after exam
[09/02/24, 5:20:07 PM] kasim k: Computer Science & Engineering	
Rajeev Gandhi Proudyogiki 
Mahavidylaya	
ANDEEP KUMAR	
9302547355		
15Feb
[09/02/24, 5:26:28 PM] annu❤️: Computer Science & Engineering	
Lakshmi Narain College of Technology & Science
OJAS ARYA	
6260779505
Will come 	In March 
Old prospect
[09/02/24, 5:41:53 PM] Neha mam e.c: Yeah toh hai hi nahi
[09/02/24, 5:41:54 PM] Neha mam e.c: Yahaa enquiry pad par
[09/02/24, 5:41:54 PM] Neha mam e.c: Visited
[09/02/24, 5:42:06 PM] Neha mam e.c: Neha vishwakarma - 7828185941
Will Come with Somya , Tanya , Anushree 
Already visited 
13 February
Old prospect
[09/02/24, 5:42:22 PM] Neha mam e.c: Kp sir ne bhi bola hai ki ye nahi aayi
[09/02/24, 5:42:55 PM] annu❤️: Ayi hai sir apne friend ke saath
[09/02/24, 5:43:05 PM] Neha mam e.c: To aapne colleague ko sahi mana karo student jhooth bole sakte hai
[09/02/24, 5:43:43 PM] Neha mam e.c: Abh baar baar student se confirm mat karo
[09/02/24, 5:43:52 PM] Neha mam e.c: Kharab ho jayega prospect
[09/02/24, 5:44:21 PM] Neha mam e.c: Chode do registration karaiega tab admitte card manga lena
[09/02/24, 5:45:56 PM] kp sir: Mujhe toh enquiry pad main nahi dikhaa, prospect jan main aaya toh ek baar isi group main tag karoo ki konsa prospect daala hai 4 jan ke phale
[09/02/24, 5:46:07 PM] kp sir: Kewal Luv aayaa hai aapka
[09/02/24, 5:46:38 PM] kp sir: Baaki mujee koi bhi nahi dikhee hai enquiry pad main
[09/02/24, 5:47:29 PM] anchal e.c: Artificial Intelligence and Data Science	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
PIYUSH	
6267166338	
11 Feb will come
Indrapuri
[09/02/24, 5:47:36 PM] annu❤️: Theek hai mam
[09/02/24, 5:48:08 PM] Neha mam e.c: Ur enquiry Abhi aapki dikhi nahi hai pad me
[09/02/24, 5:55:51 PM] ~ Deepali coding: Information Technology	Oriental College of Technology	AARTI DHURVE	9340416715	will come next week indrapuri
[09/02/24, 5:59:54 PM] anchal e.c: Computer Science & Engineering	VNS Group of Institutions	
PRINCE RAI	
7067529559
	will think
[09/02/24, 6:03:22 PM] ~ Deepali coding: Will come Sunday with utkarsh Gupta and abhay gupta
[09/02/24, 6:05:12 PM] khushi e.c: Branch:-Computer Science & Engineering	
College:-Bhopal Institute of Technology & Science, Bangrasia
Name :-	VIKASH BHARTI
Contact:-	6232141105			
Expected date:-will think
[09/02/24, 6:10:04 PM] ~ Chauhan Shilpa: Ragistration done hafsa mam
[09/02/24, 6:13:17 PM] kp sir: 👍
[09/02/24, 6:14:28 PM] ~ Chauhan Shilpa: Ragistration done 👍 ( 5 February)
[09/02/24, 6:20:12 PM] ~ Hafsa , Coding Thinker: Thank You Madam
[09/02/24, 6:22:30 PM] ~ Deepali coding: Information Technology	Oriental Institute of Science & Technology	SHIVANK SHUKLA	7489356159	will come 17 feb indrapuri
[09/02/24, 6:43:42 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	RUDRA PRATAP SINGH BAGHEL	9977381399	will come after 17 feb  indrapuri
[09/02/24, 6:44:24 PM] anchal e.c: Computer Science & Engineering	
VNS Group of Institutions	
RISHABH TRIPATHI	
8429633843
	12 feb 
 indrapuri
[09/02/24, 6:53:10 PM] anchal e.c: Computer Science & Engineering	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
	BALVEER KAUL
	9893983996	
10 feb 		
Indrapuri
[09/02/24, 6:57:09 PM] anchal e.c: Computer Science & Engineering	Radha Raman Institute of Technology & Science	
MURTUJA ANSARI
	9523118876	
will come March
[09/02/24, 7:02:51 PM] anchal e.c: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
SATISH SINGH	
9343676864	
16 feb will come 
Mp nagar
[09/02/24, 7:06:56 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
SHALANI KUMARI	
8102180439	
10 feb 
indrapuri
[09/02/24, 7:17:02 PM] anchal e.c: Computer Science & Engineering
	Vaishnavi Inst. of Tech. & Science
	GOURAV	
7748052551	
after 15 march
[09/02/24, 7:20:52 PM] anchal e.c: Computer Science & Engineering	
Scope College of Engineering	
KASHISH SONI	
9340894917
	will think
[10/02/24, 12:05:41 PM] ~ Deepali coding: Branch :-		Computer Science & Engineering	
College:tit
Name :-	Nayab and sumit
Contact:-	7489181083	
visit date 10 feb
[10/02/24, 12:07:03 PM] anchal e.c: Computer Science & Engineering	
Scope College of Engineering	
RAJ KUMAR SHAH	
7828870233	
march
[10/02/24, 12:18:27 PM] ~ Hafsa , Coding Thinker: Will come today with friends
Name nhi bata rahe friends ka  
( MP Nagar ) ‎<This message was edited>
[10/02/24, 12:19:24 PM] anchal e.c: Information Technology	Oriental Institute of Science & Technology
	ANKIT TRIPATHI	
9696674754	
  will think
[10/02/24, 12:50:52 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	ALIM BAIG	7566188709	will come after 20 feb chetak
[10/02/24, 12:59:28 PM] ~ Deepali coding: Name of Student: Shailesh patel, Abhishek patel, Akshat sharma
College name: tit
Contact no: 9755775926
Branch: CSE
Year: 2nd 
Expected Date of Visit: 15 feb
[10/02/24, 1:05:31 PM] ~ Memuna Coding Thinker: Name of Student: Rekha Kushram
College name: Surabhi clg
Contact no: 8815761846
Branch: CS
Expected Date of Visit: 11  Feb
[10/02/24, 1:12:19 PM] ~ Hafsa , Coding Thinker: ‎This message was deleted.
[10/02/24, 1:12:57 PM] ~ Hafsa , Coding Thinker: Name of Student: Huzaifa Imam + friends ( Uday & Abhay) 
College name: OIST
Contact no: 9334452193
Branch: CS/AI/ML
Expected Date of Visit: 12 Feb
[10/02/24, 1:14:11 PM] arpana e.c: Millennium Institute of Technology & Science
	RAJANI BELWANSHI
	6266319321
will come after 16 feb
old prospect
[10/02/24, 1:23:55 PM] ~ Deepali coding: Computer Science & Engineering	Lakshmi Narain College of Technology Excellence	VIPUL KUMAR	9693484459	will come 10 feb indrapuri evening
[10/02/24, 1:29:52 PM] kasim k: 2nd year
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	 
RAKESH KUMAR MANDAL	
7634041917	
20 feb chetak gautam nagar
[10/02/24, 1:36:30 PM] khushi e.c: College:-Sagar Institute of Research & Technology
Name:-	ABHINAY KUMAR PATEL
Contact:-	9584692671		
Expected date:- for brother 	  after 20 Feb
[10/02/24, 1:42:31 PM] ~ Memuna Coding Thinker: Name of Student: Akash Verma 
College name: Sagar clg
Contact no: 9770333893
Branch: CS
Expected Date of Visit: 14 Feb
[10/02/24, 1:51:46 PM] khushi e.c: Branch:-	Electrical & Electronics Engineering	
College:-Sagar Institute of Research & Technology	
Name:-ANISH KUMAR MISHRA
Contact:-	8305280902	
Expected date :-	will think in March
[10/02/24, 2:31:27 PM] kasim k: 2nd year
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
ABHAY RAJ SINGH	
7372867517	
after 20 feb nehru nagar
[10/02/24, 2:33:49 PM] arpana e.c: nehru nagar
[10/02/24, 2:34:28 PM] kasim k: aree mtlb nehru nagar mai rehta haiii  wo copy ho gya
[10/02/24, 2:49:02 PM] ~ Deepali coding: Electrical & Electronics Engineering	NRI Institute of Information Science & Technology	MONU BHURIYA	7828033543	will come 11 feb chetak
[10/02/24, 3:01:23 PM] annu❤️: Computer Science & Engineering	
Technocrat Institute of Technology
PRATYUSH VISHWAKARMA
7987318950	
Will Come DSP	 
12 February
[10/02/24, 3:05:59 PM] ~ Deepali coding: Technocrats Institute of Technology [Excellence]	MD. NEHAL KHAN		will come 13 feb indrapuri 	8294154975
[10/02/24, 3:14:12 PM] Neha mam e.c: ‎This message was deleted.
‎[10/02/24, 3:14:13 PM] Neha mam e.c: ‎image omitted
‎[10/02/24, 3:14:43 PM] Neha mam e.c: ‎image omitted
[10/02/24, 3:17:59 PM] Harsh sir tl: Dear Team,

Hope this message finds you well. Please drop a message on my number. Additionally, I will share-some contact numbers; prioritize making calls to them.

Thank you
[10/02/24, 3:21:25 PM] ~ Hafsa , Coding Thinker: Name of Student: Abdul Rafey Khan 
College name: TIT
Contact no: 8827370039
Branch: CS/AI/ML
Expected Date of Visit: 11 Feb
[10/02/24, 3:23:09 PM] khushi e.c: ‎This message was deleted.
[10/02/24, 3:25:39 PM] khushi e.c: Branch:-Electrical & Electronics Engineering 
college:-	Sagar Institute of Research & Technology
Name :-	AMIT VISHWAKARMA + himanshu kashyap
Contact:-	8461830080
Expected date :-		will think
[10/02/24, 3:40:49 PM] ~ Chauhan Shilpa: Name :- MANISH
Number: - 7440505136
College: - Trinity Institute of Technology & Research
Branch :-Electrical & Electronics Engineering
Year: 3 ed Yr
Expected date of visit: - 20 February (mp nagar)
[10/02/24, 3:46:28 PM] annu❤️: Rajesh Sahu - 8305958029
Will Come indrapuri
11 February
[10/02/24, 3:48:14 PM] ~ Memuna Coding Thinker: Vivek -- 6264977107
Will come 12 Feb mp nagar
[10/02/24, 4:01:14 PM] annu❤️: Bhola shau - 8889879176
Will Come 16 February
[10/02/24, 4:02:37 PM] Harsh sir tl: Sandeep Ahirwar has already visited. If anyone has information on his please inform me.
‎[10/02/24, 4:04:22 PM] Neha mam e.c: Coding Thinker Post 1.2.mp4 ‎document omitted
[10/02/24, 4:09:08 PM] ~ Hafsa , Coding Thinker: Name of Student: Mohammad Shadab 
College name: BITS
Contact no: 7631150971
Branch: CS
Year: 3rd Yr
Expected Date of Visit: After 20 Feb
[10/02/24, 4:10:50 PM] annu❤️: Surjeet Kumar Yadav - 6205466882
IES college
3rd year 
Chetak 16 February
[10/02/24, 4:11:10 PM] khushi e.c: Branch:-Electrical & Electronics Engineering	
College:-Sagar Institute of Research & Technology	
Name:-MOHAMMAD ISHAN KHAN
Contact:-	7223822703	
Expected date:-	will think
[10/02/24, 4:20:31 PM] khushi e.c: Branch :-Electrical & Electronics Engineering	
College:-Sagar Institute of Research & Technology	
Name :-GULFAM ALAM	
Contact:-9572636605		
Expected date:-will come today indrapuri
[10/02/24, 4:22:42 PM] annu❤️: Sanat lodhi - 7694931881
Will Come DSA
Chetak 20 February
[10/02/24, 4:23:35 PM] ~ Hafsa , Coding Thinker: Name of Student: Mohammad Sarim 
College name: Corporate College 
Contact no: 9565444065
Branch: CS
Year: 2nd Yr
Expected Date of Visit: After 15 Feb
[10/02/24, 4:49:39 PM] ~ Deepali coding: Will come 11 feb with Prashant
[10/02/24, 4:51:25 PM] kasim k: aryan 	
tit /2nd year/cs	
9977791944	
12feb evening
[10/02/24, 5:01:33 PM] khushi e.c: Name:- Rohit thakur 
Branch :- cs&e
College:-BITS
Year :- 3rd 
Contact:- 7909322992
 Expected date :- 17  Feb m.p nagar
[10/02/24, 5:03:54 PM] anchal e.c: Computer Science & Engineering-Data Science	Technocrat Institute of Technology
	ROHIT KUMAR SHARMA	
6203095190	
	after 12 feb will come 
Indrapuri
[10/02/24, 5:17:20 PM] Lalita Sahu: Name:- Ankush patel
Number:- 7747998646
Branch :- cs
College:-LNCT
Year :- 2nd year
 Expected date :- 18feb(indrapuri)
[10/02/24, 5:24:48 PM] ~ Hafsa , Coding Thinker: Name of Student: Prasoon Parihar + Nikhil Singh 
College name: JNCT
Contact no: 7067837586
Branch: CS
Year: 2nd Yr
Expected Date of Visit: 11 Feb (Indrapuri) ‎<This message was edited>
[10/02/24, 5:40:09 PM] ~ Deepali coding: ‎This message was deleted.
[10/02/24, 5:40:31 PM] anchal e.c: Will come today mp nagar registration
[10/02/24, 5:43:16 PM] Lalita Sahu: Name:- Rohan tayde
Number:- 9516727404
Branch :- AIML
College:-LNCT
Year :- 2nd year
 Expected date :-will think (indrapuri)
[10/02/24, 5:52:00 PM] arpana e.c: name of student- Arjun 
6264482012
bansal college
 2nd year 
will come  after 20 feb

Name of student- Ajeet shukla
9340757097
oriental college
2nd year
will come 2 March

Name of student- Rahul ahirwar
8109398074
sagar college 
2nd year
will come After 15 feb


Name of student- Sanjay 9589567070
sagar college 
2nd year
will come 15feb

Name of student- shaban 9981491609
oriental college 
2nd year
will come after 15 feb

Name of student Nishant sharma
9302690175
Sirt college
2nd year
 will come 12 feb  with friend Hardik
[10/02/24, 5:57:34 PM] arpana e.c: Millennium Institute of Technology & Science	
ABHISHEK DUBEY
	9506666223
3dr year
old prospect
will come after 21 feb
[10/02/24, 6:02:57 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	 college:- Sagar Institute of Research & Technology
Name :- 	RANJAN KUMAR

	 Contact:-7645008607		
Expected date:-will think
[10/02/24, 6:03:50 PM] arpana e.c: Bansal Institute of Research, Technology & Science	
SAURABH SHUKLA
	7307560660
3rd year
old prospect
Will come feb end
[10/02/24, 6:07:56 PM] ~ Deepali coding: 65	Electronics & Communication Engineering	IES College of Technology	SATYAM KUMAR CHANDRAVANSHEE	7250060706	will come 12 feb chetak
[10/02/24, 6:09:39 PM] khushi e.c: Branch :- Computer Science & Engineering
College:-	NRI Institute of Information Science & Technology	
Name:-SHITAL PATLE	
Contact:-6267066817
Expected date:-	 11 Feb indrapuri
[10/02/24, 6:09:59 PM] ~ Deepali coding: Will come today indrapuri with abhijay
[10/02/24, 6:11:10 PM] khushi e.c: + Mohit ramnaresh
[10/02/24, 6:13:45 PM] ~ Chauhan Shilpa: Name :- Satyam Kumar , Yuvraj, Ankur
Number: - 9835902443
College: - lnct
Branch :- cs
Year: 2nd Yr
Expected date of visit: - 16 February ( indrapuri)
[10/02/24, 6:13:47 PM] annu❤️: Computer Science & Engineering	
Corporate Institute of Science & Technology
AKASH RANJAN	8409001048	
In March 
3rd year
[10/02/24, 6:14:45 PM] arpana e.c: Bansal Institute of Research, Technology & Science
	ANKITA PATEL
	6264002214
2nd year
old prospect
Will come 12 feb
[10/02/24, 6:18:02 PM] Lalita Sahu: Name:- suhani lodhi
Number:- 6269113920
Branch :- CS
College:-LNCT
Year :- 2nd year
 Expected date :-after 18feb (indrapuri)
[10/02/24, 6:25:23 PM] khushi e.c: + Aryan ,faiz
[10/02/24, 6:28:30 PM] arpana e.c: Oriental Institute of Science & Technology	
VIKAS AHIRWAR
	8989717870
2nd year
old prospect
Will come march
[10/02/24, 6:41:36 PM] Lalita Sahu: Name:- Swastika nanda
Number:- 7067035861
Branch :- AIML
College:-NRI
Year :- 2nd year
 Expected date :-after 14feb
[10/02/24, 6:45:22 PM] Lalita Sahu: Name:- Aagman tiwari
Number:- 7909370564
Branch :- CS
College:-LNCT
Year :- 2nd year
 Expected date :-13, 14feb
[10/02/24, 6:52:37 PM] arpana e.c: Technocrats Institute of Technology [Excellence]
	VISHAL AHIRWAR
	8357807920
2nd year
old prospect
will think april
[10/02/24, 6:55:27 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	GAUTAM KUMAR
	9142848772
old propect
2nd year
will come after 20feb
[11/02/24, 11:45:24 AM] Lalita Sahu: Mam me aaj thoda sa let aaugi
[11/02/24, 11:50:05 AM] Neha mam e.c: Off le lo aap
[11/02/24, 12:01:42 PM] Lalita Sahu: Ok mAm
[11/02/24, 12:02:12 PM] anchal e.c: IES college
Computer science
3rd year
NAme - sonali
8210775021
Will come 12 feb ‎<This message was edited>
[11/02/24, 12:08:53 PM] khushi e.c: Will come today
[11/02/24, 12:27:32 PM] khushi e.c: Branch:-		Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Lakshmi Narain College of Technology
Name:-	ANAY KUMAR VYAS
Contact:-	9179101196		
Expected date :-	11 Feb indrapuri
[11/02/24, 12:54:34 PM] khushi e.c: + chiku singhawa
[11/02/24, 1:07:51 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	INTAKHAB ALAM	9472796063		will come 12 feb							indrapuri
[11/02/24, 1:11:13 PM] ~ Hafsa , Coding Thinker: Name of Student: Sanjana Vishwakarma 
College name: NRI 
Contact no: 6263187219
Branch: CS
Year: 2nd Yr
Expected Date of Visit:  After 17 Feb (Indrapuri)
[11/02/24, 1:22:33 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	ANURAG MISHRA
	6268975864
Old prospect
will come march
[11/02/24, 1:23:03 PM] arpana e.c: Bhopal Institute of Technology, Bangrasia	
TEJESH BOPCHE
	8269872298
Old propect
will come march
[11/02/24, 1:26:21 PM] ~ Deepali coding: Will come 13 feb indrapuri
[11/02/24, 1:35:41 PM] arpana e.c: Lakshmi Narain College of Technology
	RAKESH SAHU
	7024943290O
old propect
Will come 25 feb
[11/02/24, 1:37:55 PM] arpana e.c: Lakshmi Narain College of Technology
	KARTIK RAJPUT
	7489891095
old propect
will come after 25 feb
[11/02/24, 1:42:08 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering	college:-Sagar Institute of Research & Technology
Name:-	PARAS DABDE	
Contact:-9301853516	
 Expected date:-	will think after 16 Feb
[11/02/24, 1:47:55 PM] arpana e.c: Lakshmi Narain College of Technology
	HIMANSHU SHARMA
	9340398797
old propect
will come 28 feb
[11/02/24, 1:50:09 PM] arpana e.c: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
	PANKAJ KUMAR MISHRA
	7667353158
old propect
will come after 20 feb
[11/02/24, 1:54:07 PM] arpana e.c: Lakshmi Narain College of Technology
	RAJU MEWADA
	9131505693
old propect
 Will come 15 feb
[11/02/24, 1:54:17 PM] khushi e.c: Branch:-	Electrical & Electronics Engineering
College::	Sagar Institute of Research & Technology	
Name :-RAHUL KUMAR SAKET +Deepak Sharma
Contact:-	7247430669	
Expected date :-	12 Feb indrapuri
[11/02/24, 2:29:08 PM] arpana e.c: Name of Student Abhay postar
Oriental college 
Aiml branch
3rd year
will come 13 feb 
mp nagar
[11/02/24, 2:55:51 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering
College:-	Sagar Institute of Research & Technology	
Name:-PRIYANSHI GUPTA	
Contact:- 7224998590	
Expected date :-	will think
[11/02/24, 2:57:27 PM] ~ Chauhan Shilpa: Name :- sammad ali 
Number: - 8298598809
College: - patel college 
Branch :- cs
Year: 3ed year
Will come tomorrow for registration already visited
[11/02/24, 2:57:29 PM] annu❤️: With friends  Nimesh , sushant 18 February
[11/02/24, 3:01:46 PM] khushi e.c: Branch :+	Electrical & Electronics Engineering
College:-	Sagar Institute of Research & Technology
Name :-	SHAUKAT ANSARI
Contact:-	6207955320
Expected date. :-		will think after 23 Feb
[11/02/24, 3:05:05 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology	
SHIV KUMAR RAJAK	
9302408433
Will Come 21 February
Old prospect
[11/02/24, 3:17:35 PM] ~ Deepali coding: Branch:-	Cs AIML
College::	TIT
Name : Anjali 
Contact:-	7909508231
Expected date :-	13 feb indrapuri
[11/02/24, 3:18:35 PM] annu❤️: Computer Science & Bussiness System	
IES College of Technology	
SHIVA SINGH	
9931073032
Will Come c++ , DSA 
Old prospect already visited
[11/02/24, 3:28:39 PM] annu❤️: Mausi ke Ali - 6205677242
Will Come FSD After 20 February 
Already visited
Old prospect
[11/02/24, 3:28:43 PM] suman coding: Name:- Rohit pali
Number:- 9770142112
Branch :- CSE
College:- original 
 Expected date :-after 17 feb with friend (mp nagar)
[11/02/24, 3:34:40 PM] kasim k: rohit	
tit/2nd year/3rdsam/cs	 
7024074564	
after 17feb
[11/02/24, 3:39:49 PM] ~ Deepali coding: Branch:-	Cs 
College::	TIT
Name : Tanu
Contact:-	8817579567
Already visited 
Old prospect
[11/02/24, 3:40:23 PM] Neha mam e.c: Konsi tanu
[11/02/24, 3:42:44 PM] ~ Deepali coding: Mam abhi 3-4 din phale hi visit kiya hai
[11/02/24, 3:42:56 PM] Neha mam e.c: Pura naam kya hai
[11/02/24, 3:43:32 PM] ~ Deepali coding: Mam mere pass tanu hi likha hai bss
[11/02/24, 3:45:59 PM] suman coding: Name:- Aarya Gupta 
Number:- 9993257605
Branch :- CSE
College:- original 
 Expected date :-after 19 feb  (mp nagar)
[11/02/24, 3:47:56 PM] suman coding: Name:- yuvraj singh kushwaha 
Number:- 7389729041
Branch :- CSE
College:- original 
 Expected date :-after 18 feb with friend (indrapuri)
[11/02/24, 3:52:14 PM] khushi e.c: Name :- Abhishek Kumar
College :- Bmct
Branch :- cs 
Year 3rd 
Contact 7491035920
 Expected date:- after 9 March
[11/02/24, 3:56:19 PM] khushi e.c: Name :- Anshu Kumar 
College:- IES college
Branch :- cs 
Contact 9771807711
Expected date:- after. ,19 Feb
[11/02/24, 3:59:20 PM] suman coding: Name:- komal wankhede 
Number:- 7987957280
Branch :- CSE
College:- original 
 Expected date :- 25 feb
[11/02/24, 4:07:52 PM] khushi e.c: Branch :- 	Electrical & Electronics Engineering	
College:-Sagar Institute of Research & Technology	
Name :-RAM KOURAV
Contact:-	6265760566	
Expected date :-	after 20 Feb
[11/02/24, 4:30:59 PM] khushi e.c: Name :- vikash sahare. 
College:- Bits
Branch:- cs
Number:-6262344828
Expected date:-will think
[11/02/24, 4:31:16 PM] ~ Hafsa , Coding Thinker: Name of Student: Samarjeet Dhakad 
College name: TIT
Contact no: 6265483600
Branch: CS
Year: 2nd Yr
Expected Date of Visit:  11 Feb (Indrapuri)
[11/02/24, 4:34:06 PM] anchal e.c: Information Technology	Bansal Institute of Science & Technology	
SHASHANK BAGENIYA	
9981465046
	13 feb fsd
Indrapuri
[11/02/24, 5:12:59 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering	
College:-Sagar Institute of Research & Technology	
Name :-ANURAG SHUKLA	
Contact:-7488266520	
Expected date:-	will think after 1 week
[11/02/24, 5:13:07 PM] Neha mam e.c: @team harsh sir ne tum logo kal interested kuch no diye honge unme se kisko kitne no Mille the ur Kitne student interested hai course ke liye
[11/02/24, 5:13:40 PM] arpana e.c: total - 10 number
intr - 7
[11/02/24, 5:13:58 PM] Neha mam e.c: Badiya kab aane ka bole rahe hai
[11/02/24, 5:14:11 PM] arpana e.c: after exam
[11/02/24, 5:14:17 PM] arpana e.c: zyda 2nd year ke the mre
[11/02/24, 5:14:20 PM] annu❤️: Total - 10 
Interested - 5
[11/02/24, 5:14:23 PM] khushi e.c: Total 10 hai 
Interested:- 3 
And will think  :- 2
[11/02/24, 5:14:34 PM] ~ Memuna Coding Thinker: Total 10 
Interested 2
[11/02/24, 5:14:39 PM] Neha mam e.c: Data 2nd year ka ho hai
[11/02/24, 5:14:47 PM] ~ Hafsa , Coding Thinker: Total- 10
Interested - 4
[11/02/24, 5:14:50 PM] arpana e.c: hnn
[11/02/24, 5:14:58 PM] Neha mam e.c: Bahut kaam nikla
[11/02/24, 5:15:07 PM] Neha mam e.c: Sabko call proper ho gya
[11/02/24, 5:15:10 PM] khushi e.c: 19 Feb and 
9 March 
Tak ayenge
[11/02/24, 5:15:18 PM] Neha mam e.c: Tumhara bhi
[11/02/24, 5:15:19 PM] ~ Memuna Coding Thinker: Yes 4 call recieve nhi kr rhe
[11/02/24, 5:15:36 PM] Neha mam e.c: Acha
[11/02/24, 5:15:44 PM] khushi e.c: Mam 4 students ne call nhi receive kiye hai
[11/02/24, 5:15:52 PM] Neha mam e.c: Phir lagakar check kiya
[11/02/24, 5:16:00 PM] khushi e.c: Ji mam 3 baar
[11/02/24, 5:16:08 PM] ~ Memuna Coding Thinker: Morning m kra tha abhi fir kr rhe
[11/02/24, 5:17:06 PM] kasim k: 2 :-intrested 
3 not  intrested 
5 not ans
[11/02/24, 5:17:08 PM] Neha mam e.c: @919424704675 @916263551348 @916263594069  tum logo ko bhi milla hoga
[11/02/24, 5:17:24 PM] Neha mam e.c: Bahut badiya
[11/02/24, 5:18:07 PM] ~ Deepali coding: Yes mam
[11/02/24, 5:18:20 PM] Neha mam e.c: Kya scene hai
[11/02/24, 5:25:45 PM] ~ Memuna Coding Thinker: Manesh Kumar
8207430095
Will come after 15 Feb mp nagar
[11/02/24, 5:27:46 PM] ~ Deepali coding: Mam 2 prospect Bane hai
[11/02/24, 5:27:56 PM] ~ Deepali coding: Baki kuch na or decline hai
[11/02/24, 5:28:03 PM] ~ Deepali coding: Na wale ko kar rhe hai ek bar or
[11/02/24, 5:29:11 PM] ~ Deepali coding: Branch:-	cs
College:-Lnct
Name:-Anamika 
Contact:-	9302765082	
Expected date :- will come 17 feb
[11/02/24, 5:31:17 PM] Neha mam e.c: @919424704675 @916263551348 aapka kya hai
[11/02/24, 5:31:46 PM] ~ Memuna Coding Thinker: Sharad Kumar
8817961109
Will come after 16 Feb mp nagar
[11/02/24, 5:32:36 PM] Neha mam e.c: @916263594069 student aa gye udhar test ke liye
[11/02/24, 5:32:50 PM] ~ Deepali coding: Yes nam
[11/02/24, 5:32:56 PM] ~ Deepali coding: Mam
[11/02/24, 5:33:00 PM] Neha mam e.c: Kitne
[11/02/24, 5:33:04 PM] ~ Hafsa , Coding Thinker: Name of Student: Nadir Niyaz
College name: OIST
Contact no: 6267352057
Branch: CS/AI/ML
Year: 2nd Yr
Expected Date of Visit:  After 15 Feb
[11/02/24, 5:33:15 PM] khushi e.c: Branch:- Electrical & Electronics Engineering
College:-	Sagar Institute of Research & Technology	
Name::MD REYAJ
Contact:-	8434969380		
Expected date:-  will think
[11/02/24, 5:35:44 PM] anchal e.c: 2 prospect h
[11/02/24, 5:36:18 PM] ~ Deepali coding: 16
[11/02/24, 5:37:34 PM] ~ Deepali coding: Branch:-	cs
College:-Lnct
Name:-uday and abhay
Contact:-	9140573231
Expected date :- will come 18 feb indrapuri
[11/02/24, 5:38:12 PM] Neha mam e.c: Bad
[11/02/24, 5:38:15 PM] Neha mam e.c: Bas
[11/02/24, 5:38:20 PM] ~ Deepali coding: Yes mam
[11/02/24, 5:39:23 PM] Neha mam e.c: @918085394718 test ka compulsory karna padega
[11/02/24, 5:40:41 PM] anchal e.c: Abdul samad
9934371891
12 feb
Indrapuri
[11/02/24, 5:48:40 PM] ~ Chauhan Shilpa: Name of Student: Ankit with friends Chetan aur Rohit
College name: jnct
Contact no: 8718001456
Branch: aisa / cs
Year: 2nd Yr
Expected Date of Visit:   12  Feb indrapuri
[11/02/24, 6:00:20 PM] anchal e.c: Alok Gupta
6207765130
Sagar college
CS
2nd year
Will come April
[11/02/24, 6:02:28 PM] arpana e.c: Name of student Himanshu
7999323159
Oriental college 
will come 13 feb 
Inderapuri
[11/02/24, 6:10:15 PM] kasim k: Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
SAUD ANSARI	
7667961227	
13April
[11/02/24, 6:14:33 PM] khushi e.c: Branch :-Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:- Technocrat Institute of Technology
Name:-	PRINCE KUMAR
Contact:-	7781839926	
Expected date :-	12 Feb indrapuri
[11/02/24, 6:16:07 PM] arpana e.c: name of studrnt  Arslaan khan 6269943154
Oriental college
will come 13 feb
with frinds .Uzair, shokir ahmed,Yuvraj singh, Safwan 
Mp nagar
[11/02/24, 6:18:41 PM] kasim k: Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
POOJA SHRIVASTAVA	
8962938569	
march 1 week
( indrpuri)
[11/02/24, 6:19:16 PM] annu❤️: Harlan - 8827039582
Will Come 17 February
Indrapuri
[11/02/24, 6:27:02 PM] khushi e.c: Branch:-Electrical & Electronics Engineering	
College:-Sagar Institute of Research & Technology	
Name:-ASHISH KUMAR MISHRA
Contact:-	9693584802		
Expected date:-after 15 Feb
[11/02/24, 6:35:57 PM] ~ Hafsa , Coding Thinker: ‎This message was deleted.
[11/02/24, 6:39:36 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering	
College:-Sagar Institute of Research & Technology
Name:-	ARUN DHONDI
Contact :-8085453941	
Expected date :-	will think
[11/02/24, 6:43:14 PM] kasim k: Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
KHUSHBU PUSHPTODE	 6266431500	
March 26
2nd year chetak bridge
[11/02/24, 6:46:00 PM] ~ Chauhan Shilpa: Name of Student: puspraj 
College name: lnct
Contact no: 7067603990
Branch: aiml / cse
Year: 2nd Yr
Expected Date of Visit:   after 10 March
[11/02/24, 6:46:09 PM] anchal e.c: AIDS
Technocrats Institute of Technology [Excellence]	
Amrutha Mohandas 
8085747592
2nd yr
Will come 20 Feb
[11/02/24, 6:51:53 PM] ~ Hafsa , Coding Thinker: Name of Student: Nishant Kumar 
College name: TIT
Contact no: 8292966947
Branch: CS/AI/ML
Year: 2nd Yr
Expected Date of Visit:  After 13 Feb
[11/02/24, 7:02:54 PM] ~ Deepali coding: Name of Student: Dhanu
College name: LNCT
Contact no: 8757750131
Branch: cs
Year: 2nd Yr
Expected Date of Visit:  will come 12 feb. Indrapuri
[11/02/24, 7:07:18 PM] ~ Deepali coding: Name of Student: yogesh sahu
College name: TIT
Contact no: 9691223326
Branch: cs
Year: 2nd year
Expected Date of Visit:  will come after 15 feb
[11/02/24, 7:11:32 PM] anchal e.c: CS
Technocrats Institute of Technology [Excellence]	
Ritik sahu
8878003625
3rd yr
Will come 22 Feb
[12/02/24, 12:27:56 PM] annu❤️: MD Kamran Khan 
8303300892
All saints college
Will Come in March 
New Batch
[12/02/24, 12:32:32 PM] kasim k: chandrakant 	
sirt/2nd /	
9801172234	
12feb indrpuri
[12/02/24, 12:32:53 PM] ~ Memuna Coding Thinker: Brajesh Singh
6266829269
12 Feb Indripuri
[12/02/24, 12:35:00 PM] annu❤️: Bhavishya Rajput
6268682881
Will Come Python
Indrapuri
With friend Abhinav
[12/02/24, 12:35:22 PM] ~ Memuna Coding Thinker: +Sandeep
[12/02/24, 12:37:51 PM] ~ Hafsa , Coding Thinker: Name of Student: Shruti 
College name: Oriental College 
Contact no: 8358970082
Branch: EC
Expected Date of Visit: 13 Feb
[12/02/24, 12:43:19 PM] ~ Memuna Coding Thinker: Sandeep Sahu with friends ( Shubham Singh & Shubham yadav)
9752733788
Will come after 10 March
[12/02/24, 1:28:41 PM] arpana e.c: Bansal Institute of Research & Technology
	HARISHANKAR	9301730166	
2nd year
will come after 16 feb
[12/02/24, 1:36:13 PM] ~ Memuna Coding Thinker: Name of Student: Ashu Namdev 
College name: Trinity College 
Contact no: 9039589448
Branch: CSE
Expected Date of Visit: after 17 feb
[12/02/24, 1:42:17 PM] ~ Hafsa , Coding Thinker: Name of Student: Bhupendra Dangi
College name: LNCT
Contact no: 9589519377
Branch: CS
Year: 3rd
Expected Date of Visit: 19 Feb
[12/02/24, 1:55:06 PM] arpana e.c: will come 14 feb
[12/02/24, 2:00:41 PM] ~ Hafsa , Coding Thinker: Name of Student: Rupendra Satpute
College name: TIT
Contact no: 6266871344
Branch: CS
Year: 2nd 
Expected Date of Visit: Will come in March
[12/02/24, 2:49:18 PM] ~ Deepali coding: Name of Student: Manish kumar
College name: NRI 
Contact no: 7546088229
Branch: ec
Year: 3rd year
Expected Date of Visit: Will come 18Feb
[12/02/24, 3:15:54 PM] ~ Memuna Coding Thinker: Hariom
9755793952
Will come 17 Feb
[12/02/24, 3:36:29 PM] ~ Chauhan Shilpa: Name of Student: gourav Verma 
College name: rgpv 
Contact no: 7000965078 
Branch: cs
Year: 3ed Yr
Expected Date of Visit:   12 February indrapuri ‎<This message was edited>
[12/02/24, 3:46:41 PM] ~ Hafsa , Coding Thinker: Name of Student: Tikaram
College name: Bansal 
Contact no: 7806040468
Branch: ME
Year: 3rd Yr
Expected Date of Visit: After 20 Feb
[12/02/24, 3:49:10 PM] ~ Memuna Coding Thinker: Sumit 
7070180724
Bansal clg 
Will come after 17 Feb
[12/02/24, 3:52:09 PM] suman coding: Name of Student: Ankit rathor 
College name: Trinity institute of technology 
Contact no: 9752839851
Branch: electrical & electronic engineer 
Expected Date of Visit: coming today (indrapuri)
[12/02/24, 4:00:21 PM] anchal e.c: Name of Student: Anil 
College name: SIRT
Contact no: 9301685441
Branch: Ex AIDS 
Expected Date of Visit: After 15 Feb
[12/02/24, 4:08:43 PM] anchal e.c: Name of Student: Surender
College name: SIRT
Contact no: 6268510237
Branch: ME
Expected Date of Visit: After 15 Feb
[12/02/24, 5:21:58 PM] annu❤️: Computer Science & Engineering	
Corporate Institute of Science & Technology	
ANAND OSWAL
8966988493	
In March 
FSD Indrapuri
[12/02/24, 5:22:49 PM] anchal e.c: Will come today
[12/02/24, 5:23:39 PM] anchal e.c: Will come today
[12/02/24, 5:26:13 PM] ~ Memuna Coding Thinker: Nitesh & Nitin
9406558405
Will come 13 Feb
[12/02/24, 5:30:28 PM] ~ Hafsa , Coding Thinker: Name of Student: Rajeev Ranjan + Deepak Dhakad
College name: TIT
Contact no: 9128658896
Branch: CS/AI/ML
Year: 2nd Yr
Expected Date of Visit: 15 Feb
[12/02/24, 5:30:51 PM] annu❤️: Computer Science & Engineering-Data Science	
Trinity Institute of Technology & Research	
RAVI DANGI
8463021808	
Ankit Dangi 
9301714257	
In March 
2nd year
[12/02/24, 5:44:11 PM] arpana e.c: ‎This message was deleted.
[12/02/24, 5:44:25 PM] arpana e.c: Name of student kritij gupta 
9993534384
sam collge
3rd year
will come 15 feb
mp nagar
[12/02/24, 5:51:55 PM] ~ Hafsa , Coding Thinker: Name of Student: Mohit Patil 
College name: TIT
Contact no: 9302223633
Branch: CS/AI/ML
Year: 2nd Yr
Expected Date of Visit: 15 Feb
[12/02/24, 5:53:34 PM] ~ Memuna Coding Thinker: Student name : Shivam Yadav
Contact no : 8957332055
Will come after 17 Feb
[12/02/24, 5:53:36 PM] annu❤️: Computer Science & Engineering-Data Science	
Trinity Institute of Technology & Research	
LIKESH ADEY
9098549968	
17 February	Cc++ 
Chetak 
2nd year
[12/02/24, 6:14:38 PM] kasim k: Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
SHREYA SINGH
8709447105	
25feb dsp indrpuri
[12/02/24, 6:24:12 PM] Harsh sir tl: Happy Birthday, Anchal! May your day be incredibly special. Wishing you all the joy and success in the world. Take a pledge to set unexpected targets this February, and I believe you'll achieve great things. Cheers to another fantastic year ahead!@919424704675
[12/02/24, 6:27:02 PM] annu❤️: Shivam Patel 
9685425468
In March
[12/02/24, 6:31:38 PM] ~ Mahi: ‎Neha mam e.c added ~ Mahi
[12/02/24, 6:32:28 PM] arpana e.c: ‎Neha mam e.c removed arpana e.c
[12/02/24, 6:32:44 PM] anchal e.c: Thnku soo much sir 😊
[12/02/24, 6:33:48 PM] Neha mam e.c: Happy birthday anchal💐🎈🎂
[12/02/24, 6:34:07 PM] anchal e.c: Thnku ma'am 😊
[12/02/24, 6:46:53 PM] arpana e.c: ‎Neha mam e.c added arpana e.c
[12/02/24, 6:53:30 PM] ~ Hafsa , Coding Thinker: Going today ( Indrapuri )
[12/02/24, 6:56:35 PM] arpana e.c: name of student nitish kumar
8269298915
IES college  
3rd year
will come today 
inderpuri
[12/02/24, 7:01:36 PM] ~ Deepali coding: name of student Abhishek lodha
8839958565
Bansal 
3rd year
will come 13feb indrapuri
[12/02/24, 8:30:14 PM] ~ Chauhan Shilpa: Name - shubham dhadse
College - TIT 
Mob - 88178 94135
Branch - CS
Expected date of Visit:- 14 February (indrapuri)
[12/02/24, 8:35:07 PM] kasim k: Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
ABHI SHARMA	
8827320833	
15/16feb indrpuri
[13/02/24, 12:38:36 PM] ~ Deepali coding: name of student Sukhveer 
8109136346
Bansal 
3rd year
will come after 20
[13/02/24, 12:46:05 PM] Lalita Sahu: Student name:-SHREYA PATIL	
Contact:-7869087060	
 Collage:-Technocrats Institute of Technology & Science
MCA
Expacted date :-Will think
[13/02/24, 12:47:57 PM] kp sir: Aak FSD ka batch hai MP nagar main 
TEAM KITNE LOG AARAHE HAIN 
INDIVIDUALLY GROUP MAIN DAALOO
[13/02/24, 12:48:16 PM] kp sir: 25 aaj baithane hai aaplogo koo
[13/02/24, 1:01:45 PM] ~ Deepali coding: name of student Manish sha
3 Rd year 
Bansal 
3rd year
will come march start
[13/02/24, 1:04:53 PM] kp sir: Iskee kuch hai kya aasar 
Kitnee kitnee aarahe hain sabhi ke . Kal tak toh update Kar hi liya hogaa naa itne mere aarahe hain itnee mere
[13/02/24, 1:05:24 PM] kasim k: 2
[13/02/24, 1:05:28 PM] kasim k: fsd
[13/02/24, 1:05:56 PM] ~ Chauhan Shilpa: Sir ek abhi subha ho gaya hai ek or saam tak ho jayega
[13/02/24, 1:06:33 PM] kp sir: 👍
[13/02/24, 1:06:35 PM] arpana e.c: aj ke liye ni h sir ..15 tk ho jyga 1
[13/02/24, 1:06:39 PM] ~ Hafsa , Coding Thinker: Sir aj k nhi h
[13/02/24, 1:06:49 PM] ~ Hafsa , Coding Thinker: 17 k bad bol rhe
[13/02/24, 1:07:10 PM] ~ Hafsa , Coding Thinker: Ek 2 revisit krne ka bol rahe
[13/02/24, 1:11:02 PM] anchal e.c: With friend neelam will come today registration
[13/02/24, 1:12:13 PM] annu❤️: 2 are hai sir FSD
[13/02/24, 1:14:13 PM] Neha mam e.c: @916263594069 @917489380471 @916260753147 aapka
[13/02/24, 1:14:31 PM] ~ Deepali coding: Mam fsd ka nhi hai
[13/02/24, 1:14:35 PM] ~ Deepali coding: Data science ka aayega aaj
[13/02/24, 1:14:42 PM] ~ Deepali coding: Admission lene
[13/02/24, 1:14:43 PM] Neha mam e.c: Acha bhejo
[13/02/24, 1:14:52 PM] ~ Deepali coding: Ji mam
[13/02/24, 1:14:54 PM] Neha mam e.c: Kya name hai
[13/02/24, 1:15:11 PM] ~ Deepali coding: Abhishek bansal ka
[13/02/24, 1:15:40 PM] ~ Deepali coding: Indrapuri aayega mam ds pythan ke liye
[13/02/24, 1:15:51 PM] Neha mam e.c: Ok
[13/02/24, 1:19:19 PM] anchal e.c: Will come today mp nagar
[13/02/24, 1:30:25 PM] ~ Deepali coding: name of student Ariz khan with two friends azard and ashish
2 nd year 
Radha raman
2 nd year
Will come registration 17 feb
[13/02/24, 1:40:52 PM] khushi e.c: Mam  admission  abhi nhi hai 
  Visit hai
[13/02/24, 1:48:37 PM] arpana e.c: ‎This message was deleted.
[13/02/24, 1:50:27 PM] ~ Deepali coding: 624	Computer Science & Engineering	All Saints' College of Technology	TAVREZ ALAM	9507156178	will come march start mp nagar
[13/02/24, 1:50:43 PM] arpana e.c: ‎This message was deleted.
[13/02/24, 1:51:56 PM] arpana e.c: ‎This message was deleted.
[13/02/24, 1:53:10 PM] arpana e.c: will come today with sister kriti mp nagar
[13/02/24, 2:22:40 PM] kasim k: Name :- Labish + indori singh 
Number - +91 6261-410090
old visit 
chetak 29 feb with pankaj + rahil + 1 friends
[13/02/24, 3:03:04 PM] annu❤️: Computer Science & Engineering-Data Science	
Trinity Institute of Technology & Research	
GAURAV RAHANGDALE
9301599608	
In March 
2nd Year
[13/02/24, 3:03:15 PM] ~ Deepali coding: 51	Artificial Intelligence and Data Science	J.N. College of Technology	DEEPAK KUMAR	8271418996		will come 17 feb
[13/02/24, 3:07:20 PM] Lalita Sahu: Computer Science & Engineering	
Bansal Institute of Science & Technology	
  ROHIT KUSHWAHA
	7987467463	
18Feb mp nagar
[13/02/24, 3:09:46 PM] ~ Deepali coding: Will come with juhi indrapuri
[13/02/24, 3:20:00 PM] ~ Hafsa , Coding Thinker: Will come after practicals
[13/02/24, 3:28:18 PM] ~ Hafsa , Coding Thinker: Will come on 16 Feb with friend Vishal
[13/02/24, 3:50:41 PM] ~ Hafsa , Coding Thinker: Name of Student: Lalit Bhalavi
College name: Trinity 
Contact no : 6263906242
Branch: CS
Year: 3rd Yr
Expected Date of Visit : 13 Feb
[13/02/24, 3:56:38 PM] Lalita Sahu: Student name:-anshul vishvkrma
Contact:-	8871783944
Branch:-                                  Information Technology
 Collage:- Bansal Institute of Science & Technology
Year:- 2nd year
Expected date :-14, 15feb indrapuri
[13/02/24, 3:57:47 PM] anchal e.c: Computer Science & Engineering	
Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
AMAAN MOHAMMAD KHAN	
6263800875		
Will come after 20 feb
[13/02/24, 3:58:22 PM] anchal e.c: Electrical & Electronics Engineering	Sagar Institute of Research & Technology	
SACHIN SAHU
	9993412721
	will think
[13/02/24, 4:10:51 PM] anchal e.c: 3rd year 
CS
Radha Raman Institute of Technology & Science
	Atul soni 
Number _7694030743
Date _ after 15 Feb
[13/02/24, 4:21:31 PM] anchal e.c: Student name:-Gautam ahirwar 
Contact:-	7489793204
Branch:- CS
 Collage:- Bansal Institute of Science & Technology
Year:- 3rd year
Expected date :- 15 feb
[13/02/24, 4:23:50 PM] ~ Deepali coding: name of student: sarthak
2 nd year 
LNCT
2 nd 
Will come 14 feb
[13/02/24, 4:33:04 PM] ~ Deepali coding: name of student: Aman choudhary 
Year: 2nd 
College: OIST
BRANCH cs
Will come 20 feb mp nagar
[13/02/24, 4:50:13 PM] ~ Chauhan Shilpa: Name - Isha 
College - jnct 
Mob - 8269993753
Branch - aiml
Expected date of Visit:- 24 February  mp nagar
[13/02/24, 5:29:12 PM] ~ Deepali coding: ‎This message was deleted.
[13/02/24, 5:29:30 PM] ~ Deepali coding: 71	Electronics & Communication Engineering	IES College of Technology	MD KAIF	7070916003 will come 18 feb
[13/02/24, 5:33:37 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering
College:-	Oriental Institute of Science & Technology	
Name:-PRATEEK SINGH BAGHEL
Contact:-	6264682756		
Expected date:-will think
[13/02/24, 5:36:32 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]
ASHUTOSH CHOUBEY
6263085925	
Python Chetak 	
In March 
2nd year
[13/02/24, 5:38:35 PM] kasim k: Computer Science & Engineering	
Bansal College of Engineering
MADHVI SAHU	
6267742725	
march end
[13/02/24, 5:42:15 PM] khushi e.c: Branch :-Electrical & Electronics Engineering
College:-	Oriental Institute of Science & Technology
Name:-	AVINASH KUMAR.
Contact:-	9263753453
Expected date:-		will think
[13/02/24, 5:45:55 PM] anchal e.c: Student name:- prachi 
Contact:-	9685639066
Branch:- CS
 Collage:- Bansal Institute of Science & Technology
Year:- 3rd year
Expected date :- 20 feb
With friend pallavi
[13/02/24, 5:51:59 PM] Neha mam e.c: Anchal aa rahi hai na ye
[13/02/24, 5:52:10 PM] Neha mam e.c: Enquiry kaha li hai inhone
[13/02/24, 5:55:04 PM] anchal e.c: Enquiry nai li h
[13/02/24, 5:55:22 PM] anchal e.c: Ma'am apne jo number diye the
[13/02/24, 5:55:28 PM] anchal e.c: Wahi h
[13/02/24, 5:55:50 PM] Lalita Sahu: Student name:-Rashmi patel
Contact:-	7974175970
 Collage:- scope collage
Year:- MCA
Expected date :-after 20feb
[13/02/24, 5:56:13 PM] anchal e.c: Call recieve nai kr rhi abhi morning me bola tha usne aane ka registration ke liye
[13/02/24, 5:58:10 PM] khushi e.c: Branch:-	Electrical & Electronics Engineering	
College::Oriental Institute of Science & Technology	
Name:-RITIK CHAUDHARY
Contact:-	9109246166	
Expected date :-	21feb indrapuri
[13/02/24, 6:05:13 PM] khushi e.c: Branch :-Electrical & Electronics Engineering
College:-	Oriental Institute of Science & Technology
Name:-	SHAHIL ALI
Contact:- 	6200214854		
Expected date :- 18 Feb
[13/02/24, 6:08:14 PM] ~ Deepali coding: Branch :-cs aiml
College lnct
Name:-	Himanshu Gautam 
Contact:- 	7974495114	
Expected date :- 1 march
[13/02/24, 6:09:29 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
SHEJAL DHADSE
9098020761	
Python 	In March 
2nd year
[13/02/24, 6:12:16 PM] kasim k: Computer Science & Engineering-Artificial 
Intelligence and Data Science
Technocrat Institute of 
Technology	
AMISH PRATAP SINGH	7857027273	
march first week indrpuri
[13/02/24, 6:14:02 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering	
College:-Oriental Institute of Science & Technology
Name:-	HARIOM
Contact:-	6260641221		
Expected date:-16 feb  indrapuri
[13/02/24, 6:21:43 PM] ~ Deepali coding: Branch :-	CS
YEAR 2nd 
College:-TIT
Name:-	Ashu Tiwari 
Contact:-	6260051676
Expected date:-20 feb
[13/02/24, 6:23:01 PM] kp sir: Kab aarahe hain Anchal yeah log kitne baje
[13/02/24, 6:23:21 PM] kp sir: Visit aai aapki
[13/02/24, 6:23:48 PM] kp sir: Aapka pahuch rahaa hai kya 1 aur admission
[13/02/24, 6:24:31 PM] ~ Hafsa , Coding Thinker: After 18 bola h Sir unhone
[13/02/24, 6:24:33 PM] kp sir: Kitne baje aayenge ,aaj ka hi batch join karrahe hai naa
[13/02/24, 6:25:16 PM] ~ Chauhan Shilpa: Ji sir raste me hai abhi call aya tha
[13/02/24, 6:25:46 PM] anchal e.c: Sir 5:30 bola tha ab call nahi utha rhi
[13/02/24, 6:28:11 PM] kp sir: Achha ,kisi ka bhi nahi
[13/02/24, 6:34:56 PM] kp sir: @Harsh team se poocha hai Appne aaj ke admission ka status , jo batch start Kiya hai
[13/02/24, 6:38:03 PM] kasim k: Computer Science & Engineering-Artificial Intelligence and Data Science	
Technocrat Institute of Technology	
ASHUTOSH KUSHWAHA	
9329592036	
16feb indrpuri ⭐️
[13/02/24, 6:39:23 PM] anchal e.c: Computer Science & Engineering
	Bansal Institute of Research & Technology
	RAVENDRA KUMAR KUSHWAHA
	9302732278
Date_	 will come 15 feb 
indrapuri
[13/02/24, 6:40:58 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:-	Oriental Institute of Science & Technology	
Name:-VISHAL KUMAR	
Contact:-8294715553	
Expected date :-	after 25 March 	indrapuri
[13/02/24, 6:42:21 PM] Lalita Sahu: MCA
Scope College of Engineering
	VIJAY KOLHE
	8109625271	
   will think
[13/02/24, 6:50:00 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
KHUSHI SAGAR	
8305207065
Python Chetak 	
20 February
2nd Year
[13/02/24, 7:12:10 PM] khushi e.c: Branch :-Electrical & Electronics Engineering
College:-	Oriental Institute of Science & Technology
Name :-	ANANT KUMAR SHAH
Contact:-	9109379030	
Expected date :- 	after 18 Feb Indra puri
[14/02/24, 12:06:18 PM] ~ Hafsa , Coding Thinker: Name of Student: Prakhar Mishra
College name: SIRT 
Contact no : 8349158497
Branch: CS/IT
Year: 2nd Yr
Expected Date of Visit : Will come in March
[14/02/24, 12:38:28 PM] ~ Deepali coding: Name of Student: Roushan kumar 
College name: Tit
Contact no : 8757750131
Branch: CS/IT
Year: 2nd Yr
Expected Date of Visit : Will come 14 feb indrapuri with friend Anuj
[14/02/24, 1:04:35 PM] kp sir: Kasim idhar aao cabin main
[14/02/24, 1:06:30 PM] anchal e.c: ‎This message was deleted.
[14/02/24, 1:08:57 PM] Lalita Sahu: Name - jeeshab patel
College - Scope collage
Mob - 9340946637
MCA
Expected date:- 8march
[14/02/24, 1:14:01 PM] suman coding: Name of Student: sakshi malviya 
College name: bansal college 
Contact no : 8959245584
Year: 2nd Yr
Expected Date of Visit : Will think ( March )
[14/02/24, 1:20:43 PM] kp sir: Memuna aap cabin main aaiyee
[14/02/24, 1:23:37 PM] kp sir: Aparna aap aayee
[14/02/24, 1:30:59 PM] Lalita Sahu: ‎This message was deleted.
[14/02/24, 1:31:49 PM] Lalita Sahu: Name:-	ABHISHEK DUBEY
Contact:-	8602042201	
College:- scope college
MCA
Expected date:- 17 Feb
[14/02/24, 1:35:37 PM] kp sir: Hafsa cabin main aaye
[14/02/24, 1:47:36 PM] khushi e.c: Branch :- 		Computer Science & Engineering
College:-	Radha Raman Institute of Technology & Science
Name:-	FIROZ ANSARI
Contact:-	7482943462
 Expected date:-after March
[14/02/24, 2:48:12 PM] Lalita Sahu: Will come today evening indrapuri
[14/02/24, 2:57:31 PM] ~ Deepali coding: Vaishnavi Inst. of Tech. & Science	RAJU OHARIYA	 								8103563245 will come after March
[14/02/24, 3:22:39 PM] ~ Deepali coding: Branch :- 		Computer Science & Engineering
College:-	Madhyanchal professional university
Name:-	kasif qamar 
Contact:-	 75648 21577
 Expected date:- feb end
Reference by Ariz khan 
Ariz already visited
[14/02/24, 3:23:22 PM] khushi e.c: College:-			Lakshmi Narain College of Technology & Science	
Name :-ARYA KANADE
Contact::	7879386788	
Expected date:-will think
[14/02/24, 3:29:35 PM] ~ Deepali coding: Branch :- 		CS aiml
College:- TIT
Name:-Gaurav Chauhan 
Contact:-	 6266409162
 Expected date:- will come today
[14/02/24, 3:32:01 PM] kp sir: Indrapuri batch main aaj kitne admission aarahe hain
[14/02/24, 3:37:41 PM] arpana e.c: Bansal Institute of Research & Technology
	ASHISH DHAKAR
	9981428665
	will come after 20 feb
Mp nagar
[14/02/24, 3:39:27 PM] kasim k: visit hai sir admission 16 ke baad ka bol rahe hai kuch aur kuch practical ke bd 22 around
[14/02/24, 3:40:00 PM] annu❤️: Meri bhi visit hh pr chetak pr hi
[14/02/24, 3:43:08 PM] annu❤️: Information Technology
Technocrat Institute of Technology
KANHAIYA KUMAR
7033933975
In March 
2nd Year
[14/02/24, 3:48:04 PM] arpana e.c: Bansal Institute of Research & Technology
	PRACHI LODHI
	8871366394: 	
2nd year
will come after 16 feb
Inderpuri
[14/02/24, 3:50:59 PM] suman coding: Name of Student : Mohammad kaif
College name: LNCT 
Contact no : 7783819420
Year: 2nd Yr
Expected Date of Visit : 15 February indrapuri
[14/02/24, 3:51:54 PM] khushi e.c: Branch :-Electrical Engineering
College:-	Vaishnavi Inst. of Tech. & Science	
Name:-NEMCHAND HANVAT	
Contact:-7509550923
Expected date:- 	after 22 Feb
[14/02/24, 3:52:27 PM] suman coding: Name of Studen : jayant Singh 
College name: LNCT 
Contact no : 9669382420
Expected Date of Visit : will think
[14/02/24, 3:53:33 PM] kasim k: ayush 		
7974508581	 
20 feb indrpuri
[14/02/24, 3:54:14 PM] arpana e.c: Bansal Institute of Research & Technology
	KHUSHI PRAJAPATI
	8817957206	
2nd year
will think after exam
mp nagar
[14/02/24, 4:07:40 PM] arpana e.c: Name of student Rony singh
6204700778
IES college. 
will come today Inderpuri
[14/02/24, 4:17:07 PM] ~ Deepali coding: Isne visit kar liya
[14/02/24, 4:17:26 PM] arpana e.c: ohk
[14/02/24, 4:21:51 PM] arpana e.c: will come 15 feb inderpuri
[14/02/24, 4:22:56 PM] khushi e.c: Branch :-Electrical Engineering
College:-	Vaishnavi Inst. of Tech. & Science 
name:- 	SANJAY KUMAR BAIGA 
Contact:-	8349090522 
Expected date:- will think
[14/02/24, 4:29:14 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering	
College:-Bhopal Institute of Technology, Bangrasia	
Name:-DEEPAK
Contact:-	8871775906	 
Expected date:-will think
[14/02/24, 4:36:59 PM] ~ Chauhan Shilpa: Name - rajeesh Dubey 
College - sirt
Mob - 9644441177
Branch - cs
Expected date of Visit:- March
[14/02/24, 4:51:53 PM] ~ Chauhan Shilpa: Name - Bahadur Singh 
College - rgpv 
Mob - 8969321889
Branch - cs
Expected date of Visit:- will think
[14/02/24, 4:55:24 PM] kp sir: Shilpa maam kitne baithenge aaaj new admission indrapuri main
[14/02/24, 5:01:12 PM] Lalita Sahu: BranchComputer Science & Engineering	
College:-IES's College of Technology
 Name:-SHAHROZ ANWAR KHAN
Number:-	7368876343	
Year:- 3rd 
Expected date:- will think
[14/02/24, 5:14:31 PM] ~ Deepali coding: Will come tomorrow Chetak bridge with friend ayush
[14/02/24, 5:17:57 PM] ~ Deepali coding: Will come 20 feb with Ajay and Rabindra indrapuri
[14/02/24, 5:23:55 PM] ~ Chauhan Shilpa: Sir aj 2 the par ek student ki tabiyat kharab ho gayi hai ‎<This message was edited>
[14/02/24, 5:24:07 PM] ~ Chauhan Shilpa: Or ek call receive nahi kar raha
[14/02/24, 5:26:08 PM] Neha mam e.c: 1 Deepali  ka to aa raha hai
[14/02/24, 5:29:41 PM] arpana e.c: Bansal Institute of Science & Technology	
ANISH KURMI
	8103393066	
will think 20feb
mp nagar
[14/02/24, 5:30:59 PM] khushi e.c: Branch :-Artificial Intelligence and Data Science	
College::Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
Name:-	EASHAN TIWARI
Contact:-	7999825250	
Expected date :-15 Feb m.p nagar
[14/02/24, 5:35:35 PM] annu❤️: Information Technology
Technocrat Institute of Technology
SAURAV KUMAR JHA
9693769318	
Try to visit on 18 February Or In March 
Cc++, Java 
2nd year
[14/02/24, 5:38:39 PM] suman coding: Name of Studen : Akshay gattiyani
Contact no : 7879325953
Expected Date of Visit : 15 February MP Nagar
[14/02/24, 5:42:11 PM] kasim k: ‎You deleted this message.
[14/02/24, 5:43:37 PM] anchal e.c: Information Technology	Bansal Institute of Science & Technology	
PRIYANKA	
8817355074	
after exam will think 	
indrapuri
[14/02/24, 5:44:50 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Lakshmi Narain College of Technology	
AAMIR KHAN	
8827251924	
after 20 feb
[14/02/24, 5:46:39 PM] arpana e.c: Bansal Institute of Science & Technology
	SARITA
	8450044012
2nd year
	will come 18 feb
mp nagar
[14/02/24, 5:48:37 PM] ~ Hafsa , Coding Thinker: Name of Student: Dhananjay
College name: SIRT 
Contact no : 9425642003
Branch: CS
Expected Date of Visit : 17 Feb
[14/02/24, 5:49:01 PM] khushi e.c: Branch:-Artificial Intelligence and Data Science
College::-	Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.
Name:-	KESHAV SEN
Contact:-	7869465232
   Expected date :-	 after 25 Feb
[14/02/24, 5:50:46 PM] annu❤️: Information Technology
Technocrat Institute of Technology
SAHIL RATHORE
9302851137	
In March 
2nd year
[14/02/24, 6:05:30 PM] khushi e.c: Branch :- 	Artificial Intelligence and Data Science
College:-	Corporate Institute of Science & Technology
Name:-	ARSHAD QURESHI
Contact:-	6263361076	
Expected date:-	will think
[14/02/24, 6:06:48 PM] ~ Hafsa , Coding Thinker: Name of Student: Amit Kumar 
College name: SIRT 
Contact no : 7319865270
Branch: CS
Expected Date of Visit : 14 Feb (Indrapuri)
[14/02/24, 6:24:44 PM] khushi e.c: Branch :-	Artificial Intelligence and Data Science
College:-	Corporate Institute of Science & Technology
Name:-	VIKASH AGRAWAL
Contact:-	9301288182
Expected date:-	will think
[14/02/24, 6:26:25 PM] anchal e.c: Cs
Technocrat Institute of Technology
Nitesh Kumar 
7061711913
After 20 feb 
Indrapuri ‎<This message was edited>
[14/02/24, 6:32:03 PM] annu❤️: Will Come 16 February with Priyanshi and Devshri indrapuri
[14/02/24, 6:33:27 PM] khushi e.c: Branch :- 	Computer Science & Engineering-Artificial Intelligence and Machine Learning	
 College:-Technocrats Institute of Technology [Excellence]
Name :-	SAURAV PRAKASH	
Contact::8434623037	
Expected date:- after 19 Feb
[14/02/24, 6:34:00 PM] kasim k: Computer Science & Engineering	
Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
ABHISHEK KUMAR	
8434646744	
after exam	after 28 feb
[14/02/24, 6:44:11 PM] khushi e.c: Branch :6	Electrical & Electronics Engineering
College :- 	Oriental Institute of Science & Technology
Name:-	MD TAUSEEF
Contact:-	9199411807		
Expected date:-after 25 Feb
[14/02/24, 8:18:13 PM] ~ Chauhan Shilpa: Visit done
[14/02/24, 9:59:44 PM] ~ Hafsa , Coding Thinker: Thank you mam
[15/02/24, 12:49:26 AM] kasim k: name :- kamlesh 
number :- 9009378516 
(data science  chetak today )
[15/02/24, 12:50:22 AM] kp sir: 1 baje
[15/02/24, 12:50:35 AM] kp sir: Kasim
[15/02/24, 1:46:24 AM] kasim k: han sir just cl ayaa tha
[15/02/24, 12:29:23 PM] ~ Hafsa , Coding Thinker: Name of Student: Ritik Tiwari
College name: Trinity College 
Contact no : 7408111990
Branch: CS
Expected Date of Visit : 18 Feb
[15/02/24, 12:34:42 PM] Neha mam e.c: Aaj sab chutti par chale gye
[15/02/24, 12:34:49 PM] Neha mam e.c: Kuch hai kya aaj
[15/02/24, 12:51:10 PM] khushi e.c: Branch :-Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:-Lakshmi Narain College of Technology & Science	
Name:-MUDIT SINGH THAKUR,+2.  Nakul raghuwanshi and kaushal 
Contact:-	6269580322	

Expected date :-	16 Feb m.p nagar
[15/02/24, 12:52:06 PM] ~ Memuna Coding Thinker: Name of Student: Veerendra kushwaha 
College name: Trinity College 
Contact no : 8435647151
Expected Date of Visit : 18 Feb
[15/02/24, 1:04:34 PM] ~ Memuna Coding Thinker: Will come today ( Indripuri )
[15/02/24, 1:33:28 PM] khushi e.c: Will come today with 3 freinds   Amit , Anurag, Rahul
[15/02/24, 1:33:47 PM] khushi e.c: Indrapuri
[15/02/24, 1:54:14 PM] khushi e.c: Branch :-Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:-Technocrats Institute of Technology [Excellence]
Name:-	SHREYA CHAURASIA	
Contact:-6232290500	
Expected date:-	will think
[15/02/24, 1:59:59 PM] ~ Memuna Coding Thinker: Name of Student: Vivek Kumar saket 
Contact no : 8319182606
Expected Date of Visit : after 17 Feb
[15/02/24, 2:05:21 PM] suman coding: ‎kp sir removed suman coding
[15/02/24, 3:01:30 PM] ~ Hafsa , Coding Thinker: Will come at evening
[15/02/24, 3:12:02 PM] ~ Hafsa , Coding Thinker: Will come with friend Vivek Kumar after 17 Feb
[15/02/24, 3:12:52 PM] ~ Memuna Coding Thinker: Name of Student: Aman prajapati 
Contact no : 8085211497
Expected Date of Visit : 18 Feb
[15/02/24, 3:20:18 PM] ~ Chauhan Shilpa: Name - SANJAY KUMAR
College - Radharaman Engineering College
Mob - 9608631007
Branch - cs 
Expected date of Visit:- 29  February  mp nagar
[15/02/24, 3:27:06 PM] Lalita Sahu: Name - Sujal jain
College - Oriental Institute of Science & Technology
Mob - 8435332963
Branch - aiml
Expected date of Visit:- 18feb
[15/02/24, 3:53:49 PM] ~ Chauhan Shilpa: Name - ANJALI SAHU
College - Sagar Institute of Research & Technology
Mob -6263690161
Branch - 
Expected date Computer Science & Engineering Visit:- 18 February  indrapuri
[15/02/24, 3:54:06 PM] Lalita Sahu: Branch CS, aiml
College:- Oriental Institute of Science & Technology
Name :-	SYED SHOAIB ALI
Number :- 	8815998314	
Expected date :-24Feb (indrapuri)
[15/02/24, 3:56:54 PM] ~ Hafsa , Coding Thinker: Will come on 18 Feb
[15/02/24, 4:07:57 PM] ~ Memuna Coding Thinker: Name of Student: Sourabh Chadar
Contact no : 8815792224
Expected Date of Visit : 18 Feb
[15/02/24, 4:43:50 PM] ~ Memuna Coding Thinker: Name of Student: Abhishek prajapati + friend ( Krishna)
Contact no : 8319115952
Expected Date of Visit : 16 Feb
[15/02/24, 4:58:47 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:- Lakshmi Narain College of Technology	
Name:-ADITYA PRATAP SINGH	
Number:- 9589303667	
Expected date :-7March
[15/02/24, 5:17:37 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering
College:-	Oriental Institute of Science & Technology	
Name:-BAJRANGI KUMAR
	 Contact:-8092396331	
Expected date:-after  1 March 			( m.p nagar )
[15/02/24, 5:28:29 PM] khushi e.c: Branch :-Electrical & Electronics Engineering
College:-	Oriental Institute of Science & Technology
Name:-	KAUSHAL KUMAR
Contact;-	9262821399	
Expected date :-	will think in April
[15/02/24, 5:36:16 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	
Class :-Oriental Institute of Science & Technology
Name:-	AAZAM ANSARI	
Contact:- 8962639496
Expected date :- 		16 Feb m.p nagar
[15/02/24, 5:47:03 PM] ~ Hafsa , Coding Thinker: Name of Student: Vineet Kushwaha
College name: Radharaman College 
Contact no : 8839003275
Branch: CS
Expected Date of Visit : Will come in March
[15/02/24, 6:12:20 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	
College:-Radha Raman Institute of Technology & Science
Name:-	AMARJEET BAITHA
Contact:-	9973228227		
Expected date:-will think in April
[15/02/24, 6:27:37 PM] Lalita Sahu: Branch:-	Computer Science & Engineering	
College :-Lakshmi Narain College of Technology
Name :-	MANJAS DAHATE
Number:-	6267644275	
Expected:- after 25feb
[15/02/24, 6:30:21 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:- 	Radha Raman Institute of Technology & Science
Name:-	DHIRAJ SINGH
Contact:-	8405062897		
Expected date:-19 Feb m.p nagar
[15/02/24, 6:55:33 PM] kasim k: shivani agarwal 
coming today 
+91 6261-628073
[15/02/24, 7:05:46 PM] ~ Chauhan Shilpa: Visit done
[15/02/24, 7:06:53 PM] ~ Chauhan Shilpa: Visit done
[15/02/24, 7:08:49 PM] ~ Memuna Coding Thinker: Ok mam Thank you
[15/02/24, 7:18:55 PM] ~ Chauhan Shilpa: Visit done
[15/02/24, 7:20:16 PM] khushi e.c: Will come 18 Feb
[15/02/24, 7:20:58 PM] ~ Deepali coding: ‎This message was deleted.
[15/02/24, 8:40:53 PM] khushi e.c: Sir awinash Kumar Singh  registration   ke liye  aaye. The kya
‎[15/02/24, 11:47:10 PM] Neha mam e.c: IMG_5526.MP4 ‎document omitted
[15/02/24, 11:48:04 PM] kp sir: Pls make this as a status
[15/02/24, 11:48:46 PM] khushi e.c: Ji sir
[15/02/24, 11:50:02 PM] kp sir: @Harsh sir Kal aakar sabsee phalee data accumulate karnaa hai jaisaa Maine aapko batayaa tha . 
Main saam ko aaungaaa poora check karenge apan phir ,caller ko properly 2 year ka data allot karnaa . Kal any how aap phale yeah waala kaam priority par karlenaa .
[16/02/24, 11:30:01 AM] khushi e.c: Will  come today  + sahil ( m.p nagar)
[16/02/24, 1:14:29 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-Lakshmi Narain College of Technology	
Name:-SANJU KATARIYA	
Number:-8965827364
Expected date:-	18Feb
[16/02/24, 1:16:38 PM] ~ Deepali coding: Year 3 Rd 
College:-tit
Name:-Amit Kumar 
Number:-9136750319
Expected date:-	22 feb
[16/02/24, 1:39:33 PM] ~ Deepali coding: ‎This message was deleted.
[16/02/24, 1:40:02 PM] ~ Deepali coding: Will come today for revisit (Anuj Rameshwar and nitish)
[16/02/24, 3:53:10 PM] arpana e.c: coming today inderpuri
[16/02/24, 4:06:51 PM] arpana e.c: Bansal Institute of Research & Technology
	ABHISHEK RAJAK
	7898018281
2nd year
will come 17 feb
mp nagar
[16/02/24, 4:07:56 PM] Harsh sir tl: ‎This message was deleted.
[16/02/24, 4:08:47 PM] ~ Memuna Coding Thinker: Name of Student: Aryan Dubey 
College name: Trinity clg 
Contact no : 8827406637
Expected Date of Visit : Will come in March
[16/02/24, 4:12:20 PM] ~ Chauhan Shilpa: Name of Student: PIYUSH CHAURIHA , divesh
College name: Technocrat Institute of Technology
Contact no: 9340996297 
Branch: cs
Year: 3ed Yr
Expected Date of Visit:   16 February indrapuri
[16/02/24, 4:17:45 PM] ~ Chauhan Shilpa: Name of Student: MUSKAN PANDEL
College name: Technocrat Institute of Technology
Contact no: 8770806460
Branch: cs
Year: 3ed Yr
Expected Date of Visit:   28  February indrapuri
[16/02/24, 4:25:56 PM] ~ Memuna Coding Thinker: Name of Student: Sumanth Kumar
College name: Sagar clg 
Contact no : 9718265960
Expected Date of Visit : Will come in March
[16/02/24, 4:28:37 PM] ~ Chauhan Shilpa: Name of Student: SHREYANSH
College name: Sagar Institute of Research & Technology Excellence
Contact no: 9838626936
Branch: cs
Year: 3ed Yr
Expected Date of Visit:   5 March February indrapuri
[16/02/24, 4:31:38 PM] arpana e.c: Name of student Roshan kumar
9523129378
sistec college 
1st year
will come 20 feb
mp nagar
[16/02/24, 4:33:36 PM] anchal e.c: Computer Science & Bussiness System	
IES College of Technology
MOHIT PARMAR
	9131797927	
25 feb
[16/02/24, 4:42:27 PM] khushi e.c: Branch :-	Electrical & Electronics Engineering
College:-	Oriental Institute of Science & Technology
Name :-	SANDIP KUMAR	
Contact '-:-6205507283	
Expected date :-	after   March
[16/02/24, 5:16:12 PM] annu❤️: Information Technology
Technocrat Institute of Technology
TAZKEER KHAN
7571828898	
In March 
2nd year
[16/02/24, 5:17:17 PM] Neha mam e.c: Aaj pehale prospect bana hai tumhara
[16/02/24, 5:18:48 PM] annu❤️: Hnn mam 2 nd year pr ni kr rhi thi aaj last exam tha unka
[16/02/24, 5:18:57 PM] annu❤️: Call back aur not answered hi ja rhe the
[16/02/24, 5:23:15 PM] ~ Chauhan Shilpa: Visit done
[16/02/24, 5:27:34 PM] arpana e.c: Oriental College of Technology
	SANDEEP KUMAR
	7322815406
2nd year
will come 17 feb
mp nagar
[16/02/24, 5:27:40 PM] annu❤️: Computer Science & Engineering-Data Science	
Oriental Institute of Science & Technology
ARPIT CHOURASIYA
8223991983	
25 February
2nd year
[16/02/24, 5:38:40 PM] Lalita Sahu: Branch:-Computer Science & Engineering
College:-	VNS Group of Institutions
Name:-	RAJ KUMAR GUPTA	
Number:-6387566379	
Expected date :-first week in march(mpnagar)
[16/02/24, 5:42:06 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Science & Technology	

HARSHWARDHAN AHIRWAR	
8349176414
	25 feb  
indrapuri
[16/02/24, 5:49:07 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-VNS Group of Institutions
Name:-	NIDHI VERMA
Number:-	9039128842	
Expected date:-will think march
[16/02/24, 5:57:19 PM] arpana e.c: Oriental College of Technology
	ADARSH KUMAR PANDEY
	9507892201	
2nd year
will think 17 feb
mp nagar
[16/02/24, 6:00:32 PM] Lalita Sahu: Branch :-Computer Science & Engineering
College:-	VNS Group of Institutions	
Name:-KUNAL WAGH
Number:-	7987460534
Expected date:-	18feb mpnagar
[16/02/24, 6:11:57 PM] anchal e.c: Computer Science & Engineering	Oriental College of Technology
	SIDDHARTH MISHRA	
8602404871	
will come march
[16/02/24, 6:13:54 PM] khushi e.c: Branch :-Electrical & Electronics Engineering	
College:-Radha Raman Institute of Technology & Science
Name,:-	RAJESH KUMAR KUSHWAHA	
Contact:-7610313189
Expected date :-		will think
[16/02/24, 6:15:49 PM] Lalita Sahu: Branch:-	Computer Science & Engineering	
College:-VNS Group of Institutions	
Name :- ATUL KUMAR MAHULE	with rahul 
Number:- 7489542549
Expected date :-	8March
[16/02/24, 6:23:28 PM] ~ Chauhan Shilpa: Name of Student:-ELARAM
College name: SAM College of Engineering & Technology
Contact no: 6266831005
Branch: Electrical & Electronics Engineering
Year: 3ed Yr
Expected Date of Visit:  2 March February indrapuri
[16/02/24, 6:30:30 PM] Lalita Sahu: Branch:-	Computer Science & Engineering	
College:-VNS Group of Institutions	
Name:-HARSH VISHWAKARMA	
Number:-7354135230
Expected date:-	25February
[16/02/24, 6:39:45 PM] annu❤️: Beekesh Ahirwar - 9691047530
In March
FSD
[16/02/24, 6:40:05 PM] ~ Chauhan Shilpa: Name of Student:-SANTOSH KUMAR SAKET, vikas 
College name: Bhopal Institute of Technology & Science, Bangrasia
Contact no: 8823814873
Branch: Computer Science & Engineering
Year: 3ed Yr
Expected Date of Visit:  29 February ndrapuri ‎<This message was edited>
[16/02/24, 6:42:05 PM] ~ Memuna Coding Thinker: Name of Student: Khushi parmal 
College name:  Vaishnavi clg 
Contact no : 8370028969
Expected Date of Visit : 18 feb
[16/02/24, 6:43:38 PM] Lalita Sahu: Branch:-Computer Science & Engineering
College:-	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name:-MANSI KUMARI
Number:-	7857987883
Expected date:- will think 	(indrapuri)
[16/02/24, 6:47:12 PM] ~ Chauhan Shilpa: Name of Student:- NAIM KHAN 
College name:- Bhopal Institute of Technology & Science, Bangrasia
Contact no: -9977177885
Branch: -Computer Science & Engineering
Year: 3ed Yr
Expected Date of Visit:  25 March
[16/02/24, 6:53:41 PM] ~ Deepali coding: Will come 18 feb chetak with Vishal and dilip
[16/02/24, 6:54:29 PM] kasim k: Computer Science & Engineering 
â€“ 
Artificial Intelligence	Technocrat Institute of Technology	
PRITAM KUMAR	9006248209	
after march 15
[16/02/24, 6:54:29 PM] kasim k: Computer Science & Engineering â€“ Artificial Intelligence	
Technocrat Institute of Technology	
ATUL PAL	
6261805520	
march end
[16/02/24, 6:54:29 PM] kasim k: Computer Science & Engineering	
Bansal College of Engineering	MADHVI SAHU	
6267742725	
march end
[16/02/24, 6:55:48 PM] kasim k: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
SHAILENDRA KUMAR	
7678611078	
after 20 will think
[16/02/24, 6:57:19 PM] Neha mam e.c: @918085394718 sir Tuesday tak MP nagar ka Fsd ka batch full karo
[16/02/24, 6:57:45 PM] Neha mam e.c: Baki Indripuri and MP nagar data science ka bhi
[16/02/24, 7:01:44 PM] arpana e.c: Computer Science & Engineering-Data Science	Oriental College of Technology	
VIVEK KUMAR GUPTA
	9131798545	
2nd year
 will come 17 feb
indrapuri
[16/02/24, 7:02:35 PM] anchal e.c: Computer Science & Engineering	
Bansal Institute of Research & Technology	
MRITUNJAY RAJAK	
8085964756
	17 feb 
 Indrapuri
[16/02/24, 7:05:15 PM] ~ Deepali coding: 265	Computer Science & Engineering	J.N. College of Technology	PRABAL SONI	8878449170	will come 1 March mp nagar
[16/02/24, 7:06:52 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
 Name:-SAALIM KHAN
Number:-	8109300837	
Expected date:- not confirmed date(m.p.nagar)
[16/02/24, 7:08:29 PM] ~ Deepali coding: 266	Computer Science & Engineering	J.N. College of Technology	RAUSHAN KUMAR	9608133297	come after Holi indrapuri
[16/02/24, 7:09:06 PM] ~ Chauhan Shilpa: Name of Student:- RAHUL KUMAR
College name:- Corporate Institute of Science & Technology
Contact no: -6201261631
Branch: -Computer Science & Engineering
Year: 3ed Yr
Expected Date of Visit:  25 February
[16/02/24, 7:12:11 PM] arpana e.c: Oriental Institute of Science & Technology
	HARSH BHARGAVA
	6261212506	
will come 2 march
indrapuri
[16/02/24, 7:12:49 PM] annu❤️: Information Technology
Technocrat Institute of Technology	
SUDHANSHU KUMAR JHA
6203196024
12 March 
2nd year
[16/02/24, 7:15:59 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Research & Technology	
ANKIT YADAV	
9835919373	
will come march Java
[16/02/24, 7:17:23 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
Name:-	AKSHAT PANDAY
Number:-	9303200955	
Expected date:-will think march
[16/02/24, 7:17:29 PM] ~ Deepali coding: 269	Computer Science & Engineering	J.N. College of Technology	GAURAV PARDHI	9301847388	come after holi
[16/02/24, 7:19:52 PM] Lalita Sahu: Branch:-	Computer Science & Engineering
College:-	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name:-HARI OM
Number:-	7828358046	
Expected date:-26Feb
[16/02/24, 7:20:07 PM] khushi e.c: Branch :-	Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Technocrat Institute of Technology
Name:-	ALOK KUMAR
Contact:-	6209809540		
Expected date :- after 	10 March
[16/02/24, 7:25:44 PM] anchal e.c: Computer Science & Engineering	
Bansal Institute of Science & Technology	
VISHAL SAHU
	9174715281	
28 feb
[16/02/24, 7:29:30 PM] arpana e.c: Oriental Institute of Science & Technology
	KHUSH PALIWAL
	8889206290	
will. come march 2
m nagar
[16/02/24, 7:38:42 PM] ~ Chauhan Shilpa: Visit done 👍
[16/02/24, 7:39:44 PM] ~ Chauhan Shilpa: Visit done
[16/02/24, 8:19:19 PM] ~ Chauhan Shilpa: Name of Student:-  DEVENDRA KURWE
College name:- Radharaman Engineering College 
Contact no: 7869062707
Branch: -Computer Science & Engineering
Year: 3ed Yr
Expected Date of Visit:  21 February( mp nagar)
[17/02/24, 12:43:17 PM] anchal e.c: Cs
Technocrat Institute of Technology
Nitesh Kumar 
7061711913
After 1 march
With friend mohit Singh 
Indrapuri
[17/02/24, 12:45:13 PM] Lalita Sahu: Branch:-Computer Science & Engineering
College:-	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name:-SHIVA	
Number:-9302121776
Expected date:-	after 5march
[17/02/24, 1:00:54 PM] Lalita Sahu: Branch:-Computer Science & Engineering
College:-	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name:-MURLI PATIDAR
Number:-	7852830690
Expected date:-	1March indrapuri
[17/02/24, 1:09:37 PM] annu❤️: Computer Science & Engineering-Data Science
Oriental Institute of Science & Technology
YUVRAJ SINGH KUSHWAH	
7389729041	
28 February	
Cc++ indrapuri 
2nd year
[17/02/24, 1:13:29 PM] ~ Hafsa , Coding Thinker: Name of Student: Anubhav Samele 
College name: SIRT
Contact no : 9131105694
Branch: AIML old prospect 
Expected Date of Visit : Will come in 2-3 days
[17/02/24, 1:13:38 PM] arpana e.c: ‎This message was deleted.
[17/02/24, 1:15:41 PM] ~ Hafsa , Coding Thinker: Will come today with Saloni ‎<This message was edited>
[17/02/24, 1:16:19 PM] arpana e.c: coming today frind sumit
[17/02/24, 1:19:15 PM] ~ Memuna Coding Thinker: Name of Student: Kuldeep Sen 
College name: Vaishnavi clg 
Contact no : 8962943670
Branch: AIML 
Expected Date of Visit : Will come in March
[17/02/24, 1:21:49 PM] ~ Deepali coding: 272	Computer Science & Engineering	J.N. College of Technology	AMIT CHAUHAN	9752650652	will come 5 march indrapuri
[17/02/24, 1:23:19 PM] annu❤️: Computer Science & Engineering-Data Science	
Oriental Institute of Science & Technology
PRIYANSHU KACHNARIYA
7987168985	
Cc++ , DSA	Will come in 6th semester 
2 nd year
[17/02/24, 1:23:27 PM] khushi e.c: Branch :--	Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Technocrats Institute of Technology [Excellence]	
Name:- YASH AWADHIYA	
Contact:-7224809142		
Expected date ::	 after 3 March indrapuri
[17/02/24, 1:30:16 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
Name:-	TANWIR ALAM	number:-6200478057
Expected date:-	25Feb
[17/02/24, 1:33:16 PM] ~ Hafsa , Coding Thinker: Name of Student: Aniket Jethani 
College name: TIT
Contact no : 8103910626
Branch: CS/DS old prospect 
Expected Date of Visit : Will come in March
[17/02/24, 1:33:49 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Data Science	Technocrat Institute of Technology	
ASHISH SAHU
	8085766413	
17 feb
With friend abheet and udit
indrapuri
[17/02/24, 1:33:51 PM] khushi e.c: Branch :- 	Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:- Technocrats Institute of Technology [Excellence]	
Name :- RAMAN THAKUR	
Contact:-  8305446593		
Expected date:-	20 Feb indrapuri
[17/02/24, 1:34:10 PM] ~ Memuna Coding Thinker: Name of Student: Monark Bhoyar
College name: Vaishnavi clg 
Contact no : 6268016595
Branch: AIML 
Expected Date of Visit : Will come in March
[17/02/24, 1:39:24 PM] ~ Hafsa , Coding Thinker: Name of Student: Harprit 
College name: Patel College 
Contact no : 9425642003
Branch: CS
Expected Date of Visit : Will come in March
[17/02/24, 1:41:03 PM] Lalita Sahu: Branch:- Computer Science & Engineering 
College:-	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name:-AMAN VERMA
Number:-	9302584839	
Expected date:-19Feb (indrapuri)
‎[17/02/24, 1:43:02 PM] kp sir: 12-6.jpg ‎document omitted
[17/02/24, 1:44:25 PM] ~ Deepali coding: Branch:- Computer science 
College:-Radha raman
Year - 2 nd 
Name:-satya prakash 
Number:-	 95692 95507
Expected date:-will come 17 feb chetak with friends( Atik , Ankush , Anshu )
[17/02/24, 1:44:39 PM] kp sir: Jinsse  baat horahi hai Jo baat main positive response derahe hain unko 
Placement ke video , Placement poster , testimonial video share karnaa hai sabhi caller ko
‎[17/02/24, 1:45:08 PM] kp sir: ‎video omitted
[17/02/24, 1:45:14 PM] ~ Deepali coding: Oky sir
[17/02/24, 1:45:20 PM] kp sir: Yeah testimonials video hai
‎[17/02/24, 1:45:53 PM] kp sir: ‎image omitted
[17/02/24, 1:46:22 PM] kp sir: Yeah poster send karnaa hai    
Jinsee bhi aapki baat horahi hai
[17/02/24, 1:47:48 PM] khushi e.c: Branch :- Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:- 	Technocrats Institute of Technology [Excellence]	
Name :- AYUSH SAHU
Contact:- 	7024364718	
Expected date:- Feb 26 in indrapuri
‎[17/02/24, 1:48:07 PM] kp sir: ‎video omitted
[17/02/24, 1:48:13 PM] kp sir: Yeah Wali video bhejnaa hai
[17/02/24, 1:50:05 PM] arpana e.c: ohk sir
[17/02/24, 1:53:12 PM] anchal e.c: Will come today
[17/02/24, 1:56:12 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
RAVI DHAKAD	
9302377129	
10March
[17/02/24, 1:57:15 PM] kasim k: Computer Science & Engineering	
Radharaman Engineering College	
NIYAZUL HAQUE	
7325093302	
after 10 march
[17/02/24, 1:58:06 PM] kasim k: Oriental College of Technology
RAJ YADAV	
9770970068	
19Feb
[17/02/24, 1:58:34 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
NIKHIL SINGH	
9670996264	
after exam	+
Prassung singh parihar 
1march
[17/02/24, 1:59:48 PM] khushi e.c: ‎This message was deleted.
[17/02/24, 2:01:11 PM] khushi e.c: Branch :- 	Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College :- Technocrats Institute of Technology [Excellence]	
Name. :- ROUSHAN KUMAR + rameshwar  verma 
Contact:- 	8757750131		
 Expected date:-  	17 Feb indrapuri
[17/02/24, 3:07:47 PM] ~ Memuna Coding Thinker: Name of Student: Srajal Bisen 
College name: Vaishnavi clg 
Contact no : 7489621838
Branch: AIML 
Expected Date of Visit : Will come in March
[17/02/24, 3:12:52 PM] khushi e.c: Branch :- Computer Science & Engineering-Artificial Intelligence and Machine Learning
 college :: 	Technocrats Institute of Technology [Excellence]	
Name :- MANOJ KUMAR VAISHYA
Contact :- 	810310130 
Expected date :- will think
[17/02/24, 3:13:53 PM] ~ Deepali coding: ‎This message was deleted.
[17/02/24, 3:14:28 PM] ~ Deepali coding: Will come 20 feb with one friend devshree
[17/02/24, 3:15:21 PM] Harsh sir tl: Dear Team, Kindly ensure the completion of the assigned task by tomorrow, as I plan to allocate new data for the second year. Thank you.
[17/02/24, 3:27:25 PM] Lalita Sahu: Branch:-	Computer Science & Engineering	
College:-Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name:-SHIVANG SINGH
	Name:-9109073701
Expected date:-will think
[17/02/24, 3:30:09 PM] khushi e.c: Branch :- Electronics & Communication Engineering	
College :- Technocrats Institute of Technology [Excellence]
Name :- 	ROUNAK KUMAR
Contact:- 	6202760531		 Expected date:- will think
[17/02/24, 3:38:16 PM] khushi e.c: Branch:- 	Electronics & Communication Engineering	
College :-  Technocrats Institute of Technology [Excellence]	
Name. :- NAZIA KHAN	
Contact :- 7415098376	
Expected date:-  18 Feb indrapuri
[17/02/24, 3:48:09 PM] arpana e.c: coming today
[17/02/24, 3:55:44 PM] ~ Memuna Coding Thinker: Name of Student: Shivkumar Sahu
College name: Vaishnavi clg 
Contact no : 9584520491
Branch: AIML 
Expected Date of Visit : Will come 28 Feb
[17/02/24, 4:16:04 PM] ~ Hafsa , Coding Thinker: Will come on 20 Feb
[17/02/24, 4:17:07 PM] ~ Hafsa , Coding Thinker: 20 Feb
[17/02/24, 4:25:58 PM] kasim k: SHIVKUMAR LILHARE	9144177125	
OIST	
19 feb indrpuri
[17/02/24, 4:31:04 PM] annu❤️: MOHAMMED SALMAN
9131940541	
Oriental Institute of Science & Technology	
In March 	DSP 
4th year
[17/02/24, 4:33:11 PM] arpana e.c: coming today 
mp nagar
[17/02/24, 4:44:59 PM] khushi e.c: Name :- Satish Rana 
Contact:- 7748842772
College :- Sagar 
Year  :- 1 st year 
Expected date:- will think
[17/02/24, 4:46:53 PM] khushi e.c: Name :- Anurag Namdev
Contact:- 9669721727
College:- Sagar institute
Branch:-  cs
Year 1st
Expected date:- will think
[17/02/24, 5:14:55 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrats Institute of Technology [Excellence]	
HARSHJEET PARIHAR
	7415615455	
20 feb 
 mp nagar ‎<This message was edited>
[17/02/24, 5:15:19 PM] kasim k: Name - Lavkush
Number - 091654 62263
Collge - Oist 
26 feb
[17/02/24, 5:22:52 PM] ~ Memuna Coding Thinker: Name of Student: Vishal Kumar 
College name: Sagar clg 
Contact no : 9643282670
Branch: CS
Expected Date of Visit : Will come 10 March
[17/02/24, 5:27:00 PM] ~ Hafsa , Coding Thinker: Name of Student: Sachin Kumar 
College name: REC
Contact no : 7856073525
Branch: CS
Expected Date of Visit : Will come in March
[17/02/24, 5:27:53 PM] ~ Deepali coding: Name of Student: Ujjwal 
College name: TIT
Contact no : 8873604456
Branch: CS
Expected Date of Visit : Will come  20 feb for revisit with 3 friends ( prabhat Sonu Anuj)
[17/02/24, 5:33:58 PM] khushi e.c: College:; Trinity Institute of Technology & Research
Name :- 	ANAND YADAV
Contact:- 	9792101225		 
Expected Date:: 	will think
[17/02/24, 5:34:26 PM] annu❤️: ABHISHEK KUMAR JHA
9162502255	
Oriental Institute of Science & Technology	
25 February	
Call back 
4th year
[17/02/24, 5:37:10 PM] ~ Memuna Coding Thinker: Name of Student: Shivanshu Gautam
College name: Sagar clg 
Contact no : 8305132194
Branch: CS
Expected Date of Visit : Will come 10 March
[17/02/24, 5:38:01 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Technocrats Institute of Technology & Science	
Name:-DHEERAJ PATEL
Number:-	7869983072	
Expected date :-March (m.p.nagar)
[17/02/24, 5:44:35 PM] annu❤️: SHIVANSHU GUPTA
7869279986	
Oriental Institute of Science & Technology
25 February	
Indrapuri 
4th year
[17/02/24, 5:46:02 PM] annu❤️: Already old prospect hai mam yeh mera admission ke liye ayega March main
[17/02/24, 5:46:38 PM] Lalita Sahu: But ye mere pass data me h
[17/02/24, 5:46:44 PM] Lalita Sahu: 2nd year
[17/02/24, 5:47:03 PM] annu❤️: Already visited hai pr yeh bta rhi hu apko isliye
[17/02/24, 5:47:08 PM] ~ Hafsa , Coding Thinker: Name of Student: Mohit Rahangdale 
College name: REC
Contact no : 9302770758
Branch: CS
Expected Date of Visit : Will come next week
[17/02/24, 5:47:10 PM] ~ Memuna Coding Thinker: Name of Student: Shivam Singh 
College name: Sagar clg 
Contact no : 8120965156
Branch: CS
Expected Date of Visit : Will come 5 March
[17/02/24, 5:47:12 PM] Lalita Sahu: Ha to kya hua
[17/02/24, 5:47:40 PM] Lalita Sahu: Mene to call kiya
[17/02/24, 5:48:21 PM] Lalita Sahu: Mere pass data me aaya h
[17/02/24, 5:48:55 PM] Lalita Sahu: Or mera bhi prospect bna h apka group me bhi nai dala hai
[17/02/24, 5:49:07 PM] annu❤️: Already visited hh wo purana
[17/02/24, 5:49:13 PM] annu❤️: Bhut plhe ka
[17/02/24, 5:49:36 PM] Lalita Sahu: Abhi mene call kiya h
[17/02/24, 5:52:14 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:-Technocrats Institute of Technology & Science
Name:-	NEHA KHANDAGLE
Number:-	9340924339	
Expected date:-23Feb
[17/02/24, 5:55:58 PM] Harsh sir tl: Attention, everyone. Please be advised that this group is exclusively for sharing your prospects and not for discussing personal issues. Kindly refrain from engaging in such discussions to maintain the intended purpose of this group. Thank you for your cooperation.
[17/02/24, 5:56:09 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrats Institute of Technology [Excellence]	
ANANYA GUPTA	
7974326719	
Will think
[17/02/24, 5:56:52 PM] ~ Deepali coding: Oky sir 👍🏻
[17/02/24, 6:04:19 PM] ~ Hafsa , Coding Thinker: Name of Student: Ankita Golait
College name: LNCT
Contact no : 9301365615
Branch: CS
Expected Date of Visit : Will come for admission in FSD
‎[17/02/24, 6:11:06 PM] Harsh sir tl: ‎image omitted
[17/02/24, 6:11:41 PM] Harsh sir tl: Team you all are requested to upload this on your status and stories
[17/02/24, 6:12:38 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning
	Technocrats Institute of Technology [Excellence]
	ANIKET KUMAR YADAV	
6263826989	
march fsd 
indrapuri
[17/02/24, 6:16:12 PM] Lalita Sahu: Branch:-Computer Science & Engineering
	College:-Technocrats Institute of Technology [Excellence]	
Name:-DEEPAK GOSWAMI	
Number:-7974012758	
Expected date:-28Feb
[17/02/24, 6:17:23 PM] khushi e.c: ‎This message was deleted.
[17/02/24, 6:18:56 PM] khushi e.c: Branch :- Electronics & Communication Engineering	
College:- Trinity Institute of Technology & Research	
Name :- ABHISHEK YADAV
Contact :- 	9198122543		
Expected date:- 	will think in June
[17/02/24, 6:19:48 PM] arpana e.c: Oriental College of Technology
	PIYUSH TRIPATHI
	9752869573
	will come 18 feb
mp nagar
[17/02/24, 6:22:46 PM] khushi e.c: Branch:- Electronics & Communication Engineering
College:: -	Trinity Institute of Technology & Research
Name :- 	REETI KUSHWAH
Contact:- 	9713494440		 
Expected date::- 	after March
[17/02/24, 6:24:08 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
SHIWANK SINGH BAGRI
	9343231055	
will come march 
Indrapuri
[17/02/24, 6:25:33 PM] kasim k: ANKIT CHAUHAN	
8251922263
	OIST	
march 1 week
[17/02/24, 6:25:39 PM] kasim k: chetak
[17/02/24, 6:30:51 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Technocrats Institute of Technology & Science	
Name:-NIDHI CHOUHAN
Number:-	8982990944	
Expected date:- will think
[17/02/24, 6:33:06 PM] khushi e.c: Branch ;:- 	Electronics & Communication Engineering	
College:- Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name :- RAJEEV AHIRWAR	
Contact:-9340563942		
Expected date:- 	after 6 months
[17/02/24, 6:39:56 PM] arpana e.c: Oriental College of Technology
	YASHPAL AHIRWAR
	9555508319
will come 20 feb
indrapuri
[17/02/24, 6:40:59 PM] Lalita Sahu: Branch:-Computer Science & Engineering
College:-	Bansal Institute of Science & Technology
Name:-	SHIVAM PATEL
Number:-	8770722840
Expected date :-	18 feb (mpnagar)
[17/02/24, 6:42:54 PM] Harsh sir tl: Team, please ensure that we give our 100%. Half of February has passed, and we haven't received the expected response yet. Keep working hard.
[17/02/24, 6:44:37 PM] khushi e.c: Branch :- Electronics & Communication Engineering	
College :- Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	
Name. :- LAVKUSH PRAJAPATI
Contact :- 	7225042014		
Expected date :- 	after 26 Feb
[17/02/24, 6:46:24 PM] ~ Hafsa , Coding Thinker: Name of Student: Akrati Nema 
College name: TIT
Contact no : 7746006150
Branch: CS/AI/ML
Expected Date of Visit : Will come in March
[17/02/24, 6:50:15 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-Technocrats Institute of Technology [Excellence]	
 Name:-ASHIF KHAN
Number:-	6265004582	
Expected date:-18Feb (indrapuri)
[17/02/24, 6:50:25 PM] anchal e.c: CS+AIML	
Bansal 	
VIPUL KUMAR
	7369849156
 will come march 
	indrapuri
[17/02/24, 6:54:44 PM] anchal e.c: CS+AIML
	Bansal 	
VIKRAM SINGH CHANDEL	
9301248401		
25 feb
Indraprastha
[17/02/24, 6:56:26 PM] ~ Deepali coding: Branch:-Computer Science 
College: NRI
 Name:-kripanand 
Number:-	7354522152
Expected date:-26Feb (indrapuri)
[17/02/24, 7:00:23 PM] khushi e.c: Branch :; -	Electronics & Communication Engineering	
College:; -Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
Name :- 	GIRRAJ DHAKAD
Contact :- 	7692801827		
Expected date:-   after 26 Feb
[17/02/24, 7:00:51 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:- Bansal Institute of Science & Technology
Name:-	AMAN SINGH	
Number:-9516503774/ 9479324274
Expected date :-	after 24feb
[17/02/24, 7:01:09 PM] ~ Deepali coding: Branch:-Computer Science 
College: NRI
 Name:-Tilak sahu
Number:-	7000623239
Expected date:-20Feb (indrapuri) with brother ( satyam)
[17/02/24, 7:02:13 PM] Lalita Sahu: With aman +soud
[17/02/24, 7:02:16 PM] ~ Memuna Coding Thinker: Name of Student: Riya Gupta 
College name: TIT clg 
Contact no : 8817275273
Branch: CS
Expected Date of Visit : Will come in March
[17/02/24, 7:06:47 PM] ~ Deepali coding: Name of Student: Vishal Pandey 
College name: NRI 
Contact no : 9142557707
Branch: CS
Expected Date of Visit : Will come 25 feb indrapuri
[17/02/24, 7:13:10 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-Bansal Institute of Science & Technology
Name:-	RAHUL RAGHUWANSHi
Number:-9399748015	
Expected date:-22Feb (indrapuri)
[17/02/24, 7:27:00 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-Bansal Institute of Science & Technology	
Name:-MD AQUIBE JAWED
Number:-	9470533075
Expected date:-	Feb 25 (indrapuri)
[18/02/24, 11:59:48 AM] anchal e.c: Computer Science & Engineering	
Vidhyapeeth Institute of Science & Technology	
SUDHANSHU KUMAR	
7545840902	
Date _	12 March
[18/02/24, 12:01:15 PM] ~ Hafsa , Coding Thinker: Name of Student: Saif Ahmad
College name: REC
Contact no : 7388462124
Branch: CS
Expected Date of Visit : Will come in March
[18/02/24, 12:06:41 PM] anchal e.c: Computer Science & Engineering	Bansal Institute of Science & Technology	
ASHISH PRAJAPATI	8085108460	
	22 feb fsd
 indrapuri
[18/02/24, 12:11:43 PM] annu❤️: ARCHANA KUMARI
7470947432	
Oriental Institute of Science & Technology	
25 February	
Indrapuri 
4th year
[18/02/24, 12:15:19 PM] ~ Memuna Coding Thinker: Name of Student: Jayram  Taran 
College name: Sagar clg 
Contact no : 7509053553
Branch: CS
Expected Date of Visit : Will come in March
[18/02/24, 12:24:43 PM] annu❤️: Will come today with sitra Mp nagar
[18/02/24, 12:26:45 PM] ~ Hafsa , Coding Thinker: Name of Student: Sanjeev Raj with friends but not confirming their names 
College name: REC
Contact no : 9525450138
Branch: CS
Expected Date of Visit : 18 Feb ( Indrapuri )
[18/02/24, 12:33:53 PM] kasim k: Name - Aniket Vishwakarma
number -9575455736

coming today (chetak bridge )
[18/02/24, 12:34:50 PM] arpana e.c: ‎kp sir added arpana e.c
[18/02/24, 12:35:57 PM] ~ Mahi: coming today with avjeet singj pradun sing
[18/02/24, 1:00:38 PM] Lalita Sahu: Computer Science & Engineering
	Bansal Institute of Science & Technolog
	ANKIT KUMAR SINGH
	8918876671	
will think
[18/02/24, 1:00:53 PM] anchal e.c: Will come today
[18/02/24, 1:05:30 PM] anchal e.c: Computer Science & Engineering-Data Science	
Technocrat Institute of Technology
	ZAID MIRZA	
6307272004	
will come March
[18/02/24, 1:13:14 PM] ~ Hafsa , Coding Thinker: Will come on 19 Feb with Vishal Dev
[18/02/24, 1:19:10 PM] ~ Deepali coding: 2ND	Computer Science & Engineering-Data Science	Technocrat Institute of Technology	PAVAN CHOUDHARY	8878160829		will come mid March indrapuri
[18/02/24, 1:23:01 PM] anchal e.c: Computer Science & Engineering-Data Science	IES College of Technology	MAUSAM AMKARE	
8226044215	
	 End of February 		
With friend Mithun,suraj, monu
[18/02/24, 1:28:02 PM] annu❤️: Will Come today with Sunil Kumar indrapuri
[18/02/24, 1:29:21 PM] ~ Memuna Coding Thinker: Name of Student: Manal Thakur 
College name: LNCT  
Contact no : 8319422071
Expected Date of Visit : 20 Feb
[18/02/24, 1:31:26 PM] anchal e.c: Computer Science & Engineering	
Oriental College of Technology
	ABHISHEK PARMAR	
9926421695	
22 Feb
[18/02/24, 1:45:10 PM] Lalita Sahu: Computer Science & Engineering
	Lakshmi Narain College of Technology
	DEVENDRA PANWAR
	9926806770 3March
[18/02/24, 1:49:55 PM] ~ Hafsa , Coding Thinker: Will come on 19 Feb
[18/02/24, 1:56:46 PM] Lalita Sahu: Computer Science & Engineering	
Lakshmi Narain College of Technology	
NIKHIL WADHWANI	
6232721978	22Feb(m.p.nagar)
[18/02/24, 2:58:09 PM] ~ Deepali coding: 2ND	Artificial Intelligence and Data Science	Lakshmi Narain College of Technology	YASH DHOTE	7440730401		will come 28 feb indrapuri
‎[18/02/24, 3:01:20 PM] kp sir: ‎audio omitted
[18/02/24, 3:02:02 PM] ~ Memuna Coding Thinker: Name of Student: Payal Kshirsagar 
College name: TIT
Contact no : 6264908601
Expected Date of Visit : will come in March
[18/02/24, 3:10:13 PM] annu❤️: MUSKAN CHANDIL
8319076561	
Oriental Institute of Science & Technology
25 February	
Indrapuri 
4th year
[18/02/24, 3:13:57 PM] kasim k: will come for registration march new batch  + rohit ,chetan,harsh,sachin +1
[18/02/24, 3:25:24 PM] ~ Mahi: VNS Group of Institutions	
DEVRAJ MARAN
	7470575047
will come 19 feb 
with frind kunal
mp nagar
[18/02/24, 3:28:18 PM] ~ Hafsa , Coding Thinker: Name of Student: Rakhi Tembhare
College name: OIST
Contact no: 6267535633
Branch: CS/AI/ML
Year: 2nd Year 
Expected Date of Visit: Will come in March
[18/02/24, 3:39:48 PM] ~ Memuna Coding Thinker: Name of Student: Gaurav Khemchandani
College name: LNCT 
Contact no : 846291808
Expected Date of Visit : 21 Feb
[18/02/24, 3:40:01 PM] ~ Hafsa , Coding Thinker: Name of Student: Mohammad Shaban 
College name: OIST
Contact no: 9981491609
Branch: CS/AI/ML
Year: 2nd Year 
Expected Date of Visit: Will come next week
[18/02/24, 3:54:16 PM] ~ Memuna Coding Thinker: Name of Student: Gaurav Pancheshwar
College name: LNCT 
Contact no: 9406767732
Year: 2nd Year 
Expected Date of Visit: Will come 2 March
[18/02/24, 3:57:42 PM] ~ Hafsa , Coding Thinker: 19 Feb
[18/02/24, 4:00:10 PM] annu❤️: AYUSH JAIN
7415448619	
Oriental Institute of Science & Technology	
In March 	
Cc++ , Data analytics 
4th year
[18/02/24, 4:02:01 PM] kasim k: Information Technology	
Oriental Institute of Science & Technology	
VIDIT YADAV	
7084989823	
coming today indrpuri +sahil ku jha
[18/02/24, 4:03:50 PM] ~ Hafsa , Coding Thinker: Name of Student: Anvesh Singh 
College name: OIST
Contact no: 8319695680
Branch: CS/AI/ML
Year: 2nd Year 
Expected Date of Visit: 23 Feb
[18/02/24, 4:04:14 PM] ~ Chauhan Shilpa: Name of Student: satyendra Kumar 
College name: radha raman
Contact no: 8859069624
Branch: CS
Year: 3nd Year 
Expected Date of Visit: Will come in March
[18/02/24, 4:28:17 PM] ~ Hafsa , Coding Thinker: Name of Student: Ankit Lodhi
College name: BIST
Contact no: 9893294762
Branch: CS
Year: 2nd Year 
Expected Date of Visit: 22-23 Feb
[18/02/24, 4:41:22 PM] ~ Chauhan Shilpa: Name of Student:  KAMAL SINGH
College name: IASSCOM Fortune Institute of Technology
Contact no: 7415952855
Branch: CS
Year: 2nd Year 
Expected Date of Visit: Will come in March
[18/02/24, 5:39:57 PM] annu❤️: UJJAVAL MISHRA
7898425683	
Oriental Institute of Science & Technology	
15 March	Call back 
4th year
[18/02/24, 5:53:57 PM] Lalita Sahu: Computer Science & Engineering	
Lakshmi Narain College of Technology
	TANISHKA JAIN
	9340069759
	will think
[18/02/24, 6:00:45 PM] ~ Hafsa , Coding Thinker: Name of Student: Shreya Gajbhiye
College name: BIRTS
Contact no: 9174456516
Branch: CS
Year: 2nd Year 
Expected Date of Visit: Will come in March
[18/02/24, 6:02:19 PM] annu❤️: MD tabish - 7050133946
Will Come today
Indrapuri
[18/02/24, 6:04:32 PM] Lalita Sahu: Computer Science & Engineering	
Lakshmi Narain College of Technology
	DEEVYANSHU TIWARI
	9399561228	27Feb
[18/02/24, 6:04:44 PM] annu❤️: All saints
CSE branch 
4th year
[18/02/24, 6:07:45 PM] annu❤️: Computer Science & Engineering	
Technocrat Institute of Technology
MANU BADONIYA
8109056509	
19 February indrapuri
[18/02/24, 6:11:19 PM] ~ Deepali coding: Will come 19 feb indrapuri with arpit
[18/02/24, 6:15:16 PM] ~ Hafsa , Coding Thinker: Name of Student: MD Niyaz Ahmad 
College name: Millennium College 
Contact no: 6200495384
Branch: CS
Year: 2nd Year 
Expected Date of Visit: Will come till 10 March
[18/02/24, 6:17:07 PM] ~ Mahi: Sagar Institute of Science & Technology, Pipalner Gandhi
 Nagar Bhopal.	
TANYA RAWAT
	9770233024
3rd year
will come 26 feb with frind adit pareek
 mp nagar
[18/02/24, 6:23:59 PM] ~ Hafsa , Coding Thinker: Name of Student: Sugandh Kumar
College name: Vidyapeeth College 
Contact no: 7643821219
Branch: EE
Year: 2nd Year 
Expected Date of Visit: 25 Feb
[18/02/24, 6:25:05 PM] kasim k: Artificial Intelligence and Data Science	
Sagar Institute of Research & Technology Excellence	
ASHWANI KUMAR	
7352440366		
after samester exam  30 feb
[18/02/24, 6:29:47 PM] kasim k: 8	Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology & Science	
DAYANAND SURVE	
8602338135	
21 February
[18/02/24, 6:31:07 PM] kasim k: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology & Science	
HARSH SAHU	
7999905430	
march end
[18/02/24, 6:34:17 PM] kasim k: Computer Science & Engineering	
Scope College of Engineering
BHAVNA JHA	
8827194796	
9March
[18/02/24, 6:37:07 PM] kasim k: 1Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
AFSAR ALI	
9508719523	
27 February
[18/02/24, 6:38:22 PM] ~ Hafsa , Coding Thinker: Name of Student: Ravishankar Yadav 
College name: VNS
Contact no: 6264008465
Branch: EE
Year: 2nd Year 
Expected Date of Visit: Will come in March
[18/02/24, 6:41:10 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	ANAND DWIVEDI	
7007455992	
intrested will think march 1 week
(old prospects)
[18/02/24, 6:42:24 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
ABHISHEK KUMAR	
6207992871	
10march + gaurav kumar
[18/02/24, 6:42:34 PM] ~ Memuna Coding Thinker: Name of Student: Kuldeep Bhil
Contact no: 7724827643
Expected Date of Visit: Will come in March
[18/02/24, 6:43:39 PM] anchal e.c: 558	Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrats Institute of Technology [Excellence]	
KHUSHI VERMA
	9399075571	 	
19feb 
 mp nagar
[18/02/24, 6:45:36 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	AYUSH CHITRANSHI	
7389802405	
after 10 march
[18/02/24, 6:52:22 PM] ~ Hafsa , Coding Thinker: Name of Student: Syed Arham Ali
College name: Millennium College 
Contact no: 7000857757
Branch: CS 
Year: 2nd Year 
Expected Date of Visit: 25 Feb
[18/02/24, 6:53:59 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	DAULAT GWALA	
6260564017	
27feb after practical
[18/02/24, 6:57:28 PM] ~ Memuna Coding Thinker: Name of Student: Swaraj Sanodiya
College name: Vaishnavi College 
Contact no: 9755114034
Branch: AIML
Expected Date of Visit: 20 Feb
[18/02/24, 6:58:53 PM] kasim k: Computer Science & Engineering	
Radharaman Engineering College	
VISHAL KUMAR CHAUHAN	9301383028	
march batch
[18/02/24, 7:00:04 PM] kp sir: Arpana  Maine aapko MCA ka data diya hai 1 hour main uspar call karlooo aap
[18/02/24, 7:04:46 PM] kasim k: Artificial Intelligence and Machine Learning	
Sagar Institute of Research & Technology	
GAURAV PATEL	
7723860240	
aditya + rajendra 
march 1
[18/02/24, 7:04:55 PM] anchal e.c: VANDANA RATHORE	
MCA
9630149721
	will think
[18/02/24, 7:08:56 PM] kasim k: Artificial Intelligence and Machine Learning	
Sagar Institute of Research & Technology	

JATIN VISHWAKARMA	8966074302	
will cnfrm tomorrow 19 feb
[18/02/24, 7:10:06 PM] kasim k: Electronics & Communication Engineering	
Oriental College of Technology
ANIKET SHARAN	
8340184331	
after 1 march
[18/02/24, 7:15:52 PM] kasim k: Computer Science & Engineering-Artificial Intelligence and Machine Learning	

Oriental Institute of Science & Technology	
MANGESH RAUT	
9098289502	
29feb indrpuri
[18/02/24, 7:16:02 PM] ~ Chauhan Shilpa: Name of Student:  Nitesh Kumar 
College name: tit
Contact no: 7254896588
Branch: CS
Year: 3ed Year 
Expected Date of Visit: already visited come 20 Feb for registration
[18/02/24, 7:19:55 PM] kasim k: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Oriental Institute of Science & Technology	
MOHD ZAHID KHAN	8840921438	
after eid (laptop issu)
[18/02/24, 7:21:26 PM] annu❤️: Name of students -  Piyush Raj
Mobile no - 7061693311
College - Oriental
Branch - EC
 indrapuri 
 Patel nagar 
Will Come 19 February
[18/02/24, 7:31:15 PM] annu❤️: JNCT 
Madhu Prasad 
8817420779
Will Come Chetak
With Prashant Kumar 
19 February
[18/02/24, 7:36:52 PM] kasim k: Computer Science & Engineering	
Scope College of Engineering
RAHUL DEY	
7488783514	
15March
[18/02/24, 7:45:32 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[18/02/24, 8:08:52 PM] ~ Chauhan Shilpa: Name of Student:  ayush 
College name: oist
Contact no: 6260126558
Year: 1 St year (MCA)
Expected Date of Visit: 20 February
[18/02/24, 8:09:25 PM] ~ Chauhan Shilpa: Name of Student:  mak khan
College name: Sam 
Contact no: 889891995
Branch: CS
Year: 1 St year (mtech)
Expected Date of Visit: will come March
[18/02/24, 8:15:47 PM] ~ Chauhan Shilpa: Name of Student:  Saket Chauhan
College name: lnct
Contact no: 9608879525
Year: 1 St year (mca)
Expected Date of Visit: will come 20 March
[18/02/24, 8:22:11 PM] ~ Chauhan Shilpa: Name of Student:  adity 
College name: jnct 
Contact no: 9123249866
Year: 2nd (cs)
Expected Date of Visit: after 15 March
[18/02/24, 8:42:28 PM] ~ Chauhan Shilpa: Name of Student:  md.sajjid 
College name :- IES
Contact no: 9006602386
Year: 2nd (cs)
Expected Date of Visit: will come April
[19/02/24, 12:08:09 PM] ~ Chauhan Shilpa: Name of Student:  Manish Kumar 
College name: tit
Contact no: 6202564378 ,6206407108
Year: 2nd (cs)
Expected Date of Visit: after 25 March( mp nagar) ‎<This message was edited>
[19/02/24, 12:10:20 PM] kasim k: ‎You deleted this message.
[19/02/24, 12:10:50 PM] kasim k: Artificial Intelligence and Data Science	

J.N. College of Technology	
ASHUTOSH KUMAR SINGH	
6202555803	
1April(indrpuri)
[19/02/24, 12:11:35 PM] kasim k: Computer Science & Engineering	
Oriental College of Technology	SAKSHAM SEN	
9755157438	
12March
[19/02/24, 12:14:14 PM] ~ Hafsa , Coding Thinker: Name of Student: Akash Giri
College name: OIST 
Contact no: 7970174252
Branch: CS 
Year: 2nd Year 
Expected Date of Visit: 23 Feb
[19/02/24, 12:16:46 PM] ~ Memuna Coding Thinker: Will come Today with Harsh
[19/02/24, 12:29:04 PM] khushi e.c: Will come today with owaish ( indrapuri)
[19/02/24, 12:31:37 PM] ~ Mahi: ANSHU SHUKLA	6394478059	
TIT	 MCA
will come 21 feb
mp nagar
[19/02/24, 12:37:55 PM] ~ Chauhan Shilpa: Name of Student:  ankita golait  
College name: lnct 
Contact no: -9301365615
Year: 2nd (cs)
Expected Date of Visit: 19 February ( mp nagar)
[19/02/24, 12:43:13 PM] kasim k: ‎You deleted this message.
[19/02/24, 12:45:14 PM] kasim k: Artificial Intelligence and Data Science	
J.N. College of Technology	
DEEPAK SINGH TOMAR	
8103295702	

nirmal -6204834971
ashutosh- 6202555803
gurvendra -8092107316
ajay kewat-6264076066
will come for   revisit/registration.

after 17 march
[19/02/24, 12:45:30 PM] ~ Memuna Coding Thinker: Will come today with Sachin
[19/02/24, 12:53:13 PM] annu❤️: Will Come 21 February 
With sourabh and Ramakant
[19/02/24, 12:54:32 PM] ~ Chauhan Shilpa: Name of Student:- Ajay 
College name: sagar 
Contact no: -7896869948
Year: 2nd (cse)
Expected Date of Visit: 2 April
[19/02/24, 1:01:16 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
MRITUNJAY KUMAR	
7479466834	
25 Feb
[19/02/24, 1:01:47 PM] kasim k: + shivam kumar
[19/02/24, 1:02:45 PM] kasim k: Electronics & Communication Engineering	
IES College of Technology	
MANISH KUMAR BAITHA	
9334772769	
10Mar
[19/02/24, 1:02:55 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Technocrats Institute of Technology & Science	
Name:-deependra sahu
Number:-	8103733188
Expected date:- will think
[19/02/24, 1:02:55 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:-	Technocrats Institute of Technology & Science	
Name:-ritik sahu
Number:-	8878003625
Expected date:- 22feb
[19/02/24, 1:03:05 PM] annu❤️: Will Come today with MD Aram , Chetak
[19/02/24, 1:03:36 PM] kasim k: ‎You deleted this message.
[19/02/24, 1:04:16 PM] kasim k: Electronics & Communication Engineering	
IES College of Technology	
ABHISHEK KUMAR	
9835512118	
3march indrpuri
+ritik , sagar
[19/02/24, 1:04:52 PM] ~ Memuna Coding Thinker: Name of Student: Meghanath Enwati
College name: Vaishnavi College 
Contact no: 8103595629
Branch: AIML
Expected Date of Visit: 26 Feb
[19/02/24, 1:04:55 PM] kasim k: 1Electronics & Communication Engineering	
IES College of Technology	RAJA BABU	
8102548135	
24Feb + ayush gaur
[19/02/24, 1:08:19 PM] kasim k: Electronics & Communication Engineering	
IES College of Technology	MD SARFARAJ ANSARI	9708811255	Mar 7
[19/02/24, 1:13:57 PM] ~ Mahi: PRIYA GOKHE
	6265474441	
TIT	 MCA
will come 20 feb
indrapuri
[19/02/24, 1:14:45 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Data Science
College:-	Technocrat Institute of Technology	
Name:-SHUBHANSHU PATERIYA	
Number:-7869681260	
Expected date:-.19feb indrapuri
[19/02/24, 1:15:05 PM] ~ Chauhan Shilpa: Name of Student:- Rajan Kumar sharma
College name:- IES
Contact no: -9153439219
Year: 2nd (cs)
Expected Date of Visit: 22 February ‎<This message was edited>
[19/02/24, 1:15:09 PM] kasim k: Electronics & Communication Engineering	
IES College of Technology	
SHIVAM TIWARI	
7632040635	 
2March mp nagar  c,c++
[19/02/24, 1:31:30 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Data Science
College:-	Technocrat Institute of Technology	
Name:-AVADHESH KUMAR YADAV	
Number:-9507951878
Expected date:-	will think
[19/02/24, 1:41:52 PM] Lalita Sahu: Branch:-Computer Science & Engineering	
College:-Lakshmi Narain College of Technology & Science
Name:-DAKSH UPADHYAY
	Number:-8827023279
Expected date:- 3March
[19/02/24, 1:50:52 PM] ~ Chauhan Shilpa: Name of Student:- Ankit Gupta 
College name:- tit
Contact no: - 9713965883
Year: 1 year (cs)
Expected Date of Visit: 2 April
[19/02/24, 1:51:42 PM] kasim k: ‎You deleted this message.
[19/02/24, 1:52:01 PM] kasim k: Artificial Intelligence and Data Science	
J.N. College of Technology	MD SAHIL
7779953452		
visited on crnter 12/13 dec
come for registration 17 march
[19/02/24, 1:53:23 PM] ~ Mahi: ‎This message was deleted.
[19/02/24, 1:53:47 PM] ~ Mahi: coming today 
mp nagar Frind kunal
[19/02/24, 1:54:32 PM] ~ Mahi: J.N. College of Technology	
RADHIKA RAI
	7440928509
will come today 19 feb
with frind roshni
indrapuri
[19/02/24, 1:55:05 PM] ~ Chauhan Shilpa: Name of Student:- prakharam  with friends Nikesh of Sanskar
College name:- lnct 
Contact no: - 8709623564
Year: mca 2nd sem 
Expected Date of Visit:  10 March ‎<This message was edited>
[19/02/24, 1:58:22 PM] Lalita Sahu: Will come today after 3pm
[19/02/24, 2:22:31 PM] ~ Mahi: RITESH SAHU	8602534866	
TIT	 mca
will come 20 feb
indrapuri
[19/02/24, 3:03:13 PM] ~ Hafsa , Coding Thinker: Name of Student: Ramdayal Ahirwar 
College name: TIT
Contact no : 8103377678
Branch: CS/AI/ML
Expected Date of Visit : Will come in March
[19/02/24, 3:14:26 PM] annu❤️: Will Come indrapuri for registration
23 February
[19/02/24, 3:15:45 PM] ~ Memuna Coding Thinker: Name of Student: Yatharth Singh 
College name: Sagar College 
Contact no: 8726554518
Branch: CS
Expected Date of Visit: 2 March
[19/02/24, 3:46:10 PM] Lalita Sahu: Branch:-	Computer Science & Engineering	
College:-Lakshmi Narain College of Technology & Science	
Name:-RITIK RAI
Number:-	6265177903
Expected date:-	will come 27feb
[19/02/24, 3:52:05 PM] khushi e.c: Name :- Ravindra Kumar
Contact:- 9285583776
 Expected date:- will think
[19/02/24, 4:04:17 PM] khushi e.c: Name :- Chetan suryawanshi
Contact:- 958428220
College:- jnct
[19/02/24, 4:06:00 PM] ~ Memuna Coding Thinker: Name of Student: Prateek Patel 
College name: Sagar clg 
Contact no: 9630412427
Branch: CS
Expected Date of Visit: 1 March
[19/02/24, 4:24:30 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	
College:-Bansal Institute of Research & Technology	
Name:-HARSH KUSHWAHA
Contact:-	9685543756		
Expected date after 19 Feb 
 + Abhishek
[19/02/24, 4:24:45 PM] khushi e.c: M.p nagar
[19/02/24, 4:27:00 PM] khushi e.c: + Amit, Anurag  , Rahul
[19/02/24, 4:34:01 PM] Lalita Sahu: Branch:-CS
College:-LNCT	
Name:-yash
Number:-	6268961574
Expected date:-	will come 27feb
[19/02/24, 5:06:45 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Data Science
College:-	Technocrat Institute of Technology	
Name:-AYUSH PANDEY
Number:-	8603811940
	Expected date:- 25Feb
[19/02/24, 5:14:09 PM] kasim k: SHARAD KUMAR YADAV	6264791488	
OIST	
cnfrm tomorrow
[19/02/24, 5:15:15 PM] ~ Memuna Coding Thinker: Name of Student: Shubham yadav 
College name: Sagar clg 
Contact no: 9691396622
Branch: CS
Expected Date of Visit: In  March
[19/02/24, 5:33:29 PM] Lalita Sahu: Branch:-Computer Science & Engineering-Data Science
College:-	Technocrat Institute of Technology
Name  	ABHISHEK YADAV	
Number:-7903433142	
Expected date :- 20feb
[19/02/24, 5:34:38 PM] ~ Mahi: SOURABH DUBEY
	8109102009	
TIT MCA
will come 21 feb
indrapuri
[19/02/24, 5:36:54 PM] kasim k: KUNAL YADAV	
7222985993	
OIST	
coming tomorrow 20 feb
[19/02/24, 5:37:02 PM] kasim k: ROSHNI CHOUKSEY	8085394808	
OIST	
10March
mca
[19/02/24, 5:42:35 PM] ~ Mahi: NIDHI PRIYA	7488782318
	TIT	 MCA
will think march end
[19/02/24, 5:49:19 PM] annu❤️: MANISH VISHWAKARMA
9111576217	
Oriental Institute of Science & Technology	
1 March	
4th year
[19/02/24, 6:00:15 PM] ~ Hafsa , Coding Thinker: Name of Student: Naval Kishor 
College name: Millennium 
Contact no : 7828244739
Branch: CS
Expected Date of Visit : Will come in March
[19/02/24, 6:05:47 PM] ~ Mahi: VISHAL RAIKWAR	8269373481	
TIT MCA
	will think  25 feb
indrapuri
[19/02/24, 6:14:41 PM] khushi e.c: Branch :- 	Electrical & Electronics Engineering	
College;- Oriental Institute of Science & Technology
Name :- 	GAURAV KUMAR	
Contact:- 8862985706		  
Expected date :- 	after 5 March
[19/02/24, 6:25:52 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	 
College:- Sagar Institute of Research & Technology
Name :- 	RIZWAN ALAM	
Contact:- 7493892619	
Expected date:- after 2 March
[19/02/24, 6:31:58 PM] khushi e.c: Branch :- 	Electronics & Communication Engineering	
College :- J.N. College of Technology
Name :- 	PAYAL MEHRA	
Contact :- 8871412883
 Expected date :- 5 March
[19/02/24, 6:47:30 PM] kasim k: SAGAR RAGHUWANSHI	7999716065	
OIST	
mca
coming tomorrow 20feb
‎[19/02/24, 7:00:09 PM] kp sir: ‎image omitted
[19/02/24, 7:00:44 PM] kp sir: Note karloo sabhi log , sabhi log active Rahe, sabko Pata rahaa hai
[19/02/24, 9:11:48 PM] khushi e.c: Name of Student: vikash sahare 
College name: Bits college of bhopal
 Year :- 3rd 
Contact no : +91 6262 344 828
Branch: CSE
Expected Date of Visit : Will come in March
[19/02/24, 9:29:58 PM] ~ Chauhan Shilpa: Mam c,c++ ke Pankaj sar Ki class 3:00 p.m. to 5:30 p.m. tak hai indrapuri mein TTS mein
[19/02/24, 9:32:11 PM] kp sir: Haan ,sabhi aarahe hain hariom ko chorrkar
[19/02/24, 9:34:35 PM] Neha mam e.c: Daily kar sakte hai kya
[19/02/24, 10:31:01 PM] kp sir: I think sabhi caller status lagakar rakhe ,video wala ya placement post walaa .Roj bachooo ko hit karnaa chaiyeee
[19/02/24, 11:23:15 PM] Harsh sir tl: @916260753147 aapko mana kiya tha na jitna data roka hai uspr kaam na krne keliye ?
[19/02/24, 11:25:08 PM] Harsh sir tl: You people are expected to listen whatever i am saying ab aapke 4 prospects ke chakkar m data upr neeche hoga very unprofessional aap sabko bola tha fir bhi uspr kaam krne lage the
[19/02/24, 11:28:21 PM] kp sir: Harsh sir aap data hi hata dooo . Aur abb jo aap allot kare proper usi par kaam karwaiye aap .
Koi bhi instructor TL ke through aapko dire jaarahe hain it means ki wo management ke hi instructions hai so aapklogo ko uskoo seriously lenaa hai .
[19/02/24, 11:29:14 PM] kp sir: @Harsh sir aapne jo data aagyaa aapke pass ,prospect ke baad abb aap wahi data regular basis par allot kare
[19/02/24, 11:29:32 PM] Harsh sir tl: For sure sir
[19/02/24, 11:32:35 PM] Harsh sir tl: Starting tomorrow, the team will be working on data, and I'll be providing assistance. Please integrate the data that I supply, and I'll expect daily updates from each team member. Is this clear to everyone?
[19/02/24, 11:33:20 PM] kp sir: 👍👍
[19/02/24, 11:40:30 PM] ~ Hafsa , Coding Thinker: Yes sir
[19/02/24, 11:40:49 PM] khushi e.c: Ji sir
[20/02/24, 11:57:56 AM] anchal e.c: Name _ sahil
College _ TIT
Branch _ CS
7903473899
Will come 5 March
[20/02/24, 12:18:25 PM] anchal e.c: Will come today
[20/02/24, 12:24:06 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Corporate Institute of Science & Technology	
Name :- RISHIKA DUBEY
Contact:- 	9993972275	
 Expected date :- 	21 feb  indrapuri
[20/02/24, 12:41:21 PM] khushi e.c: Branch :-  B.Tech	Computer Science & Engineering
College;:- 	Corporate Institute of Science & Technology
Name :- 	ZAFRUL ISLAM SHAMSI
Contact:-	7542834733		
Expected date:- will think
[20/02/24, 12:55:14 PM] annu❤️: B.Tech	
Computer Science & Engineering	
All Saints' College of Technology	AHSAN ALI	
8294230577	
25 March
2nd year
[20/02/24, 12:55:38 PM] Lalita Sahu: Computer Science & Engineering
	Lakshmi Narain College of Technology
	AYUSH KUMAR	
9570771064	
will come 26feb
[20/02/24, 12:55:55 PM] anchal e.c: Will come today
[20/02/24, 1:11:19 PM] ~ Hafsa , Coding Thinker: Name of Student: Imran Ahmad
College name: All Saint's 
Contact no : 7250816173
Branch: CS
Expected Date of Visit : Will come in March
[20/02/24, 1:13:30 PM] ~ Memuna Coding Thinker: Name of Student: Vishal Kumar 
College name: IES 
Contact no : 7295997202
Branch: CS
Expected Date of Visit : 21 Feb
[20/02/24, 1:17:03 PM] anchal e.c: Electronics & Communication Engineering	Lakshmi Narain College of Technology	
VIVEK KUMAR MISHRA	
9113132535	 
Will come 1 march 
indrapuri 
	 with frd ankit himanshu
[20/02/24, 1:32:14 PM] khushi e.c: Branch :- Computer Science & Engineering	
College;:- Corporate Institute of Science & Technology
Name :- 	PRASHANT AWADHIYA	
Contact:- 6262087434	
Expected date :- 	will think
[20/02/24, 1:36:46 PM] ~ Memuna Coding Thinker: Name of Student: Aarif Hussain 
College name: IES 
Contact no : 7491899196
Branch: CS
Expected Date of Visit : 4 March
[20/02/24, 1:38:00 PM] annu❤️: Will Come tomorrow for registration Chetak + Neeraj
[20/02/24, 1:38:24 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College :- 	Corporate Institute of Science & Technology
Name :; 	MOHAMMAD SAHIL ANSARI	
Contact:- 9628471644	
Expected date :- 	 will think
[20/02/24, 1:40:00 PM] ~ Hafsa , Coding Thinker: Will go Indrapuri at evening with Vivek
[20/02/24, 1:45:54 PM] khushi e.c: Branch :- Computer Science & Engineering	
College ;- Corporate Institute of Science & Technology	
Branch :- ABU HANZALA	
Contact:- 7779832221	
Expected date ,:- 	after 1 month
[20/02/24, 2:04:05 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:- 	Corporate Institute of Science & Technology
Name :- 	PREM PRAKASH GAUTAM
Contact :- 	6386345696	
Expected date :- 	8 March indrapuri
[20/02/24, 2:54:51 PM] khushi e.c: Branch :- Computer Science & Engineering
College:-	Corporate Institute of Science & Technology	
Name. :- MD RASHID NADEEM	
Contact:- 8235133431		
Expected date :- will think
[20/02/24, 3:02:50 PM] annu❤️: B.Tech	
Computer Science & Engineering	
All Saints' College of Technology
MD SHAHAB SANOWAR
6206528557	
In April 
2nd Year
[20/02/24, 3:03:48 PM] khushi e.c: Branch :-  Computer Science & Engineering	
College :- Corporate Institute of Science & Technology	
Name :- FAIJ ALAM
Contact:- 	7392969189		
Expected date:- after 5 March
[20/02/24, 3:05:33 PM] ~ Memuna Coding Thinker: Name of Student: Snehanshu Kumar Jha with Ravi & Aditya 
College name: IES 
Contact no : 8235910817
Branch: CS
Expected Date of Visit : 26 Feb
[20/02/24, 3:09:06 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Corporate Institute of Science & Technology
Name :- 	MOHD SARIM
Contact:- 	9565444065
Expected date :- 		after 2 month
[20/02/24, 3:12:44 PM] annu❤️: B.Tech	
Computer Science & Engineering	
All Saints' College of Technology	
MD QUASID ANWAR
7480037300	
In March 
3rd Year
[20/02/24, 3:15:43 PM] annu❤️: B.Tech
Computer Science & Engineering	
All Saints' College of Technology
MD AFTAB ANWER
7765982305	
1 March
2nd Year
[20/02/24, 3:17:56 PM] kasim k: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
MADHUSUDAN MEWADA	
7222952148	
will think	
march batch
[20/02/24, 3:21:27 PM] Lalita Sahu: Computer Science & Engineering
	Lakshmi Narain College of Technology & Science	HARSH KUMAR
	6200205881	2March
[20/02/24, 3:37:22 PM] ~ Mahi: Bhopal Institute of Technology & Science, Bangrasia
	SHRESHTH RAI
	7518615173
	will come 2 march
mp nagar
[20/02/24, 3:54:44 PM] ~ Deepali coding: 2ND	Computer Science & Engineering-Artificial Intelligence and Machine Learning	NRI Institute of Information Science & Technology	ANKUSH RAJ	6206493738		will come march
[20/02/24, 3:56:48 PM] khushi e.c: Branch :- Computer Science & Engineering
College:-	IES College of Technology
Name. :- 	DEEPAK KUMAR	
 Contact:- 7564869417	
Expected date :- 	will think
[20/02/24, 3:59:48 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
IES College of Technology
	ISHWAR CHANDRA PATEL	
9399896413
	not confirmed date
[20/02/24, 4:04:11 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	IES College of Technology	
Name ,:- AYUSH SAINI	
Contact:- 9669227525	
Expected date :- 	after 2 month
[20/02/24, 4:09:14 PM] ~ Hafsa , Coding Thinker: Name of Student: Shahanshah 
College name: All Saint's 
Contact no : 6306185667
Branch: CS
Expected Date of Visit : Will come after Holi
[20/02/24, 4:12:52 PM] ~ Memuna Coding Thinker: Name of Student: Pulkitam Shrivastava
College name: IES 
Contact no : 8085518288
Branch: CS
Expected Date of Visit : 28 Feb
[20/02/24, 4:16:26 PM] Lalita Sahu: Name :-adarsh raj +akshay+avinash
Number:-8409907047
Branch:-	Computer Science & Engineering
College:-	IES College of Technology	
Expected date:-5March
[20/02/24, 4:16:55 PM] khushi e.c: Branch :- Computer Science & Engineering 
College:- 	IES College of Technology 
Name:- 	LOVELY KUMARI	
Contact:- 9958624794	
Expected date :- 	after April
[20/02/24, 4:20:41 PM] annu❤️: B.Tech	
Computer Science & Engineering
All Saints' College of Technology
Ashish 
9666139428
2nd Year
[20/02/24, 4:22:21 PM] kasim k: Computer Science & Engineering	
Patel College of Science & Technology	
ADITYA KUMAR SHARMA	
8434225748	
after exam c,c++ 	
20march
[20/02/24, 4:22:56 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
College:-IES College of Technology
Name:-	ABHISHEK KUMAR
Number:-	9304598275	
Expected date:-will come 2march
[20/02/24, 4:27:42 PM] khushi e.c: Branch :- Computer Science & Engineering
College,:- 	IES College of Technology
Name :- 	MOHAMMAD EKHLAQUDDIN
Contact:- 	9693736547	
Expected date ,:- 	after 27 Feb
[20/02/24, 4:33:13 PM] Lalita Sahu: B.Tech	Computer Science & Engineering
	IES College of Technology	
AYUSH KUMAR
	9798588911	
will think
[20/02/24, 4:45:51 PM] ~ Mahi: Corporate Institute of Science & Technology
	RAMKARAN YADAV
	7354183548	
will come 10 march
indrapuri
[20/02/24, 4:46:17 PM] khushi e.c: Branch :-Computer Science & Engineering	
College:- IES College of Technology	
Name  :- JASWIN JOY PATRICK
Contact:- 	7987437038
Expected date :- 	29 Feb
[20/02/24, 4:46:39 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	All Saints' College of Technology	AHIL RAZA	9507741938	will come march Chetak
[20/02/24, 5:03:10 PM] anchal e.c: B.Tech	Computer Science & Engineering	Bhopal Institute of Technology & Science, Bangrasia	
SONAM MANDAL	
7879558407	
 	march will come
[20/02/24, 5:05:50 PM] annu❤️: Will Come With sneha ,  21 February
[20/02/24, 5:11:21 PM] ~ Deepali coding: 2ND	Artificial Intelligence and Data Science	Lakshmi Narain College of Technology	TANU GOUR	9754608266		will come 28 feb indrapuri
[20/02/24, 5:14:55 PM] ~ Deepali coding: Branch :-Computer Science
College:- vns
Name  :- mahak 
Contact:- 7610662866
Expected date :- 	20 feb
[20/02/24, 5:15:27 PM] kp sir: Indrapuri main enquiry aai kya
[20/02/24, 5:15:52 PM] ~ Deepali coding: Haa sir ek aai thu
[20/02/24, 5:16:23 PM] khushi e.c: Branch :- Computer Science & Engineering	 college:- IES College of Technology
	 Name :- MD ARISH	 +2 freinds  Fahad , samiullah
Contact:- 6201360029	
Expected date :- 	after  2 March
[20/02/24, 5:19:47 PM] ~ Deepali coding: With friend yasmin
[20/02/24, 5:38:13 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrats Institute of Technology [Excellence]	
CHANDAN TALE	
9302303463	
will come March
	indrapuri
[20/02/24, 5:42:52 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
College:-IES College of Technology
Name:-	AARTI SHARMA
Number:-	9522686855	
Expected date:- 2march(mpnagar)
[20/02/24, 5:42:59 PM] ~ Mahi: Corporate Institute of Science & Technology
	MANISH RAJBHAR
	6268730107
	will come april
[20/02/24, 5:43:50 PM] kasim k: AMIT SEN
	6267118388	
OIST	 
mca
will try to come tomorrow
[20/02/24, 5:44:11 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology
	AMRITESH KUMAR DWIVEDI	
7389103803	
	first week of march
[20/02/24, 5:50:22 PM] ~ Mahi: Corporate Institute of Science & Technology
	PHOOL KUMARI
	9798399887	
will think  After holi
[20/02/24, 5:52:50 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:: IES College of Technology
Name ,:: -	ASHISH RANJAN YADAV
Contact:- 	9285547320		
Expected date:- after 6 March
[20/02/24, 5:55:48 PM] ~ Mahi: Corporate Institute of Science & Technology	
MD SUFIYAN	9113783520
	will come 1.week of march
indrapuri
[20/02/24, 6:00:56 PM] ~ Mahi: Corporate Institute of Science & Technology
	SUSHIL KUMAR
	9060456790	
will come feb end
mp nagar
‎[20/02/24, 6:01:39 PM] Harsh sir tl: ‎audio omitted
[20/02/24, 6:01:45 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	
AYUSHI SHEKHAR SHARMA	
9589418807	
will come march
[20/02/24, 6:04:26 PM] ~ Hafsa , Coding Thinker: Name of Student: Priya Yadav
College name: JNCT
Contact no : 7723932215
Branch: CS
Expected Date of Visit : Will come in March
[20/02/24, 6:05:58 PM] ~ Mahi: Corporate Institute of Science & Technology	
MD HARIS ANWER
	9546213860	
will think after eid
[20/02/24, 6:06:08 PM] ~ Hafsa , Coding Thinker: Okh Sir
[20/02/24, 6:06:28 PM] khushi e.c: Branch :- Computer Science & Engineering	
College :- IES College of Technology 
Name :- 	AMAR KUMAR
Contact:- 	7091869732	
Expected date :-  	 after  22 Feb  M.p Nagar
[20/02/24, 6:10:31 PM] ~ Mahi: Corporate Institute of Science & Technology
	ANSHIKA PATEL
	6268905974	
will think  march mid
[20/02/24, 6:13:53 PM] ~ Hafsa , Coding Thinker: Name of Student: Rupesh Kumar 
College name: JNCT
Contact no : 7079500772
Branch: CS
Expected Date of Visit : Will come after 10 March
[20/02/24, 6:16:52 PM] ~ Hafsa , Coding Thinker: Will come tomorrow with Amit and Atul
[20/02/24, 6:19:05 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
 College :- 	IES College of Technology
Name :- 	BIRENDRA PRATAP SINGH
Contact :- 	7070375324		
Expected date:- will think
[20/02/24, 6:20:02 PM] ~ Mahi: Corporate Institute of Science & Technology
	MOHAMMAD SADIK
	9934680627	
will think march end
[20/02/24, 6:22:01 PM] ~ Hafsa , Coding Thinker: Name of Student: Harsh Chauhan 
College name: JNCT
Contact no : 9336761627
Branch: CS
Expected Date of Visit : Will come in March ‎<This message was edited>
[20/02/24, 6:25:36 PM] ~ Memuna Coding Thinker: Name of Student: Shahid Afridi 
College name: IES 
Contact no : 9693155440
Branch: CS
Expected Date of Visit : 5 March
[20/02/24, 6:41:07 PM] ~ Hafsa , Coding Thinker: With Rajneesh
[20/02/24, 6:50:57 PM] kasim k: B.Tech	Computer Science & Engineering	
J.N. College of Technology	PRINCE MISHRA	
9691988352	
march 1 week
[20/02/24, 7:04:15 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
MANSI JOTHE	
7909720884	
21/22 feb
[20/02/24, 7:17:38 PM] ~ Deepali coding: Name of Student: Deepak kumar
College name: TIT
Contact no :  7974012758
Branch: CS
Expected Date of Visit :feb end with friend ( Siddharth)
[20/02/24, 7:21:20 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
IES College of Technology	
ATUL KUMAR	
8051438324
	will think
[20/02/24, 7:22:39 PM] anchal e.c: Name of Student: Pramanand Das 
College name: SAM
Contact no: 9128252272
Branch: CSE
Year: 3RD
Expected Date of Visit: will come march
[20/02/24, 7:26:59 PM] anchal e.c: Name :- harsh morya
Number: - 7225902702 
Colleges:-  tit
Branch :- cseaiml
Expected date of visit: - will come march
[20/02/24, 7:28:25 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:- 	IES College of Technology
Name :-	PANDIT VISHNU GUPT SHARMA
Contact:- 	9608728325		
Expected date:-21 Feb
[21/02/24, 11:56:23 AM] ~ Deepali coding: Branch :- B.Tech	Computer Science & Engineering
College:- 	sort 
Name :-	yugal bharat
Contact:- 	‪ 7354141826
Expected date: come march
[21/02/24, 12:01:56 PM] khushi e.c: Branch :: B.Tech	Computer Science & Engineering
College:- 	IES College of Technology	
Name :- MANISH KUMAR YADAV
Contact:- 	9015035318	
 Expected date :- 	 after 9 March  m.p nagar
[21/02/24, 1:13:59 PM] khushi e.c: + Manish Kumar
[21/02/24, 2:12:09 PM] ~ Hafsa , Coding Thinker: Name of Student: MD Shahnawaz
College name: All Saint's 
Contact no : 6299783798
Branch: CS
Expected Date of Visit : 27 Feb
[21/02/24, 2:34:27 PM] khushi e.c: + Sunil  Kumar  will come today indrapuri
[21/02/24, 3:01:34 PM] ~ Deepali coding: 2ND	Computer Science & Engineering	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	DEEPIKA KHATARKAR	9302331611		will come 5 march Chetak
[21/02/24, 4:17:53 PM] ~ Memuna Coding Thinker: Name of Student: Ranjan Kumar Sharma 
College name: IES
Contact no : 9153439219
Branch: CS
Expected Date of Visit : 10 March
[21/02/24, 4:50:35 PM] ~ Chauhan Shilpa: Will come today with friend vikrant indrapuri
[21/02/24, 5:08:47 PM] ~ Chauhan Shilpa: Name :- Rohan rajak 
Number: - 9589894295
Colleges:-  tit
Branch :- cs
Expected date of visit: - will come march first week
[21/02/24, 5:10:43 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology - Computer Science and Engineering
	YUNUS KHAN	
9630501300		
will come march
[21/02/24, 5:21:03 PM] ~ Deepali coding: Name :- Rahul
Number: - 7520135270
Colleges:-  tit
Branch :- cs
Expected date of visit: - will come march 5
[21/02/24, 5:50:31 PM] ~ Deepali coding: 2ND	Information Technology	Oriental Institute of Science & Technology	ANKIT LODHI	8103211926		will come march start
[21/02/24, 5:52:36 PM] annu❤️: Already Admission hai yeh meri
[21/02/24, 5:56:49 PM] ~ Deepali coding: Mene usko alag course pitch Kiya hai aapki admission hai to aap baat karo na fsd ke liye
[21/02/24, 6:11:46 PM] annu❤️: Pata hai mujhe uske project bache hue hai complete ho jyange phir usse Java Krna hai
[22/02/24, 12:23:51 PM] ~ Memuna Coding Thinker: Name of Student: Nikita 
Contact no : 7489809570
Expected Date of Visit : 26 feb
[22/02/24, 12:38:39 PM] ~ Hafsa , Coding Thinker: Will come today with Adarsh Sharma
‎[22/02/24, 12:42:02 PM] Neha mam e.c: ‎image omitted
‎[22/02/24, 12:42:03 PM] Neha mam e.c: ‎image omitted
‎[22/02/24, 12:42:03 PM] Neha mam e.c: ‎image omitted
‎[22/02/24, 12:42:04 PM] Neha mam e.c: ‎image omitted
‎[22/02/24, 12:42:04 PM] Neha mam e.c: ‎image omitted
‎[22/02/24, 12:42:04 PM] Neha mam e.c: ‎video omitted
[22/02/24, 12:42:41 PM] Neha mam e.c: make as a status
[22/02/24, 12:58:43 PM] ~ Memuna Coding Thinker: Name of Student: Vandana+ frend 
Contact no : 9630149721
Expected Date of Visit : 23 feb
[22/02/24, 1:02:30 PM] kasim k: Computer Science & Engineering	
Radharaman Engineering College	
ANKUSH KUMAR SHUKLA	
9572437452
 will come for registration 
24 feb (old visit )
[22/02/24, 1:11:03 PM] ~ Deepali coding: 2ND	Computer Science & Engineering	Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL	PANKAJ GOUR	9399098205		will come march chetak
[22/02/24, 1:19:29 PM] ~ Deepali coding: 2ND	Artificial Intelligence and Data Science	Corporate Institute of Science & Technology	HIMANSHU	9528068416	mp nagar 	will come after 8 March
[22/02/24, 1:32:34 PM] kp sir: Anchal Gautam se baat karloo ki wo class lene kabse aayegaa .aaj 22 FEB hai
[22/02/24, 1:55:01 PM] kp sir: Kaise bharogee 24FEB waale batch .saare prospects tumhare March main jaarahe hain , *Harsh* sir Apan *FEB* ki *salary* *nahi* denge kya team ko
[22/02/24, 1:56:02 PM] Harsh sir tl: Sir krte hai
[22/02/24, 1:56:06 PM] Harsh sir tl: Fill
[22/02/24, 1:56:15 PM] anchal e.c: Sir wo 26feb se aane ka bol rha h ‎<This message was edited>
[22/02/24, 2:54:37 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
IES College of Technology	
VIVEK PANDEY
	9755924460
	will think
[22/02/24, 2:55:35 PM] kasim k: Computer Science & Engineering	
Radharaman Engineering College	
SACHIN KUMAR	
9798956650
10march
[22/02/24, 3:00:07 PM] kasim k: ‎You deleted this message.
[22/02/24, 3:00:43 PM] kasim k: Computer Science & Engineering	
Corporate Institute of Science & Technology	
KAPIL KUMAR LODHI	
8305783601
2march
[22/02/24, 3:00:49 PM] ~ Memuna Coding Thinker: Name of Student: MD Kashif 
College name: IES
Contact no : 7979867194
Branch: CS
Expected Date of Visit : 4 March
[22/02/24, 3:02:35 PM] kasim k: Oriental College of Technology	PALAK UPADHYAY	
8303168052
26feb
‎[22/02/24, 3:04:11 PM] Neha mam e.c: ‎image omitted
‎[22/02/24, 3:04:53 PM] Neha mam e.c: ‎image omitted
[22/02/24, 3:05:11 PM] kasim k: 24ka bola hai mam baki deepali se shyd aj kaa instalmnt  ki bt krne ayyge
[22/02/24, 3:05:22 PM] kasim k: march batch mai plan karega
[22/02/24, 3:05:53 PM] Neha mam e.c: Kon hai tumhara
[22/02/24, 3:06:20 PM] kasim k: ankush
[22/02/24, 3:08:17 PM] ~ Deepali coding: Mam Fees me thoda issue hai inhe aaj fr se baat karne aane ka bol rhe hai
[22/02/24, 3:08:34 PM] Neha mam e.c: Kaha aa rahe hai
[22/02/24, 3:08:41 PM] Neha mam e.c: Kya issue hai
[22/02/24, 3:08:46 PM] ~ Deepali coding: Mam yahi aayenge indrapuri
[22/02/24, 3:09:22 PM] ~ Deepali coding: Installment me karna hai but thoda kam ho Jaye aisa bol rhe hai kp sir ne enquiry li thi to bol rhe hai ki yahi aakar sir se baat kar lete hai
[22/02/24, 3:09:35 PM] ~ Deepali coding: 4 hai total
[22/02/24, 3:09:56 PM] Neha mam e.c: Aaj bulao
[22/02/24, 3:10:07 PM] Neha mam e.c: Ur convert karna hai unko
[22/02/24, 3:10:14 PM] ~ Deepali coding: Aaj ka hi bola hai mam aane ka
[22/02/24, 3:10:17 PM] ~ Deepali coding: 5 pm pr
[22/02/24, 3:10:21 PM] Neha mam e.c: Ok
[22/02/24, 3:10:25 PM] ~ Deepali coding: Ji
[22/02/24, 3:11:05 PM] kasim k: ‎You deleted this message.
[22/02/24, 3:13:35 PM] kp sir: Jo prospects hai format main usi ke according daloo prospects
[22/02/24, 3:13:40 PM] ~ Hafsa , Coding Thinker: Name of Student: Vinay Kumar Yadav 
College name: IES
Contact no : 9102655199
Branch: CS
Expected Date of Visit : Will come in March
[22/02/24, 3:15:24 PM] kasim k: ‎You deleted this message.
[22/02/24, 3:15:37 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- IES College of Technology
Name :- 	MANISH RAJ
Expected date:- will think
Contact:- 	6299215410
[22/02/24, 3:15:52 PM] kasim k: Name of Student: Sanjeev kumar 
College name: IES
Contact no : 6202934623
Branch: EC
Expected Date of Visit : 23feb indrpuri + rahul aryan
[22/02/24, 3:21:55 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	IES College of Technology	
Name. :: AMAN KUMAR	
Contact:- 9905348255		
Expected date:- 27 March
[22/02/24, 3:24:22 PM] ~ Memuna Coding Thinker: Name of Student: Durgesh Kumar 
College name: Corporate institute of science and technology 
Contact no : 6299200116
Branch: CS
Expected Date of Visit : Will come in 4 March
[22/02/24, 3:26:14 PM] ~ Hafsa , Coding Thinker: Name of Student: Arpit Singh Parihar 
College name: IES
Contact no : 8770549760
Branch: CS
Expected Date of Visit : Will come in March ‎<This message was edited>
[22/02/24, 3:32:17 PM] khushi e.c: Branch :- Computer Science & Engineering
 College :- IES College of Technology	 
Name. :- ANKIT SINGH	
Contact:- 7209136212	
Expected date:- 	23feb m.p nagar
‎[22/02/24, 3:37:59 PM] Neha mam e.c: ‎image omitted
[22/02/24, 3:38:03 PM] Neha mam e.c: Iska kya hai
[22/02/24, 3:40:24 PM] kasim k: 19 tk cnfrm krna ka bola tha mam ab call receive nahi kr rahi
[22/02/24, 3:40:48 PM] Neha mam e.c: Kisi ur se lagvao
[22/02/24, 3:41:06 PM] kasim k: ji mam
[22/02/24, 3:41:49 PM] kp sir: Harsh sir se karwaa baat
[22/02/24, 3:42:32 PM] kasim k: harsh sir kh raha abhi phone nahi uthaegi
[22/02/24, 3:48:45 PM] ~ Hafsa , Coding Thinker: Name of Student: Sudarshan  Singh 
College name: IES
Contact no : 8826659884
Branch: CS
Expected Date of Visit : 28 Feb
[22/02/24, 3:55:39 PM] ~ Memuna Coding Thinker: Name of Student: Balesh Lodhi & Balik lodhi 
College name : Corporate institute of science and technology 
Contact no : 7415986461
Branch: CS
Expected Date of Visit : 26 Feb
[22/02/24, 3:56:09 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:; 	IES College of Technology	
Name :- ASHWIN JADHAV contact:- 	6266725522		
Expected date:: after 14 March
[22/02/24, 3:59:10 PM] Lalita Sahu: Name of Student: Chand kumar
College name: IEs
Contact no :9798496870 	Branch: cs
Expected Date of Visit : after 15march
[22/02/24, 4:00:25 PM] anchal e.c: Information Technology	
Bansal Institute of Science & Technology	
AMAN SINGH DANGI	
7389070820	
26 Feb				
With friend rupesh, Sulabh ‎<This message was edited>
[22/02/24, 4:02:02 PM] khushi e.c: + Anand Kumar
[22/02/24, 4:07:22 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Sagar Institute of Research & Technology	
BHUMI GARG
	7879434091	
will come march
[22/02/24, 4:16:52 PM] kasim k: B.Tech	
Computer Science & Engineering	
J.N. College of Technology	
ABHISHEK KANKHARE	
9755992067	
march end (  chetak)
[22/02/24, 4:17:28 PM] Harsh sir tl: Team march nai abhi chahiye hai admissions
[22/02/24, 4:18:45 PM] khushi e.c: Branch. :- Computer Science & Engineering
College:- 	IES College of Technology
Name :- 	SUBHASH KUMAR PATEL
Contact:- 	9516401137	
Expected date:- 8 March
[22/02/24, 4:22:00 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Sagar Institute of Research & Technology	ILMA	
9669244106		
will come march
[22/02/24, 4:25:50 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	IES College of Technology	 
Name :: VIVEK KUMAR	
Contact :- 9155453579	
Expected date :- 	5march m.p nagar
[22/02/24, 4:28:56 PM] annu❤️: Nitin Suman 
9074061042
LNCT
Will Come python
In March
Indore Branch
[22/02/24, 4:34:28 PM] khushi e.c: Branch :- Computer Science & Engineering
 College:- IES College of Technology	
Name :- ADITYA RAJ
Contact:- 	9546084671	
Expected date :- 	April
[22/02/24, 4:40:34 PM] khushi e.c: Branch :- Computer Science & Engineering
College :- 	IES College of Technology name. :- 	ASHISH RAJ	
Contact:- 9905419508		
Expected date:- april
[22/02/24, 4:40:59 PM] ~ Hafsa , Coding Thinker: Name of Student: MD Kaif
College name: IES
Contact no : 9508062699
Branch: CS
Expected Date of Visit : Will come in March
[22/02/24, 4:47:49 PM] Lalita Sahu: Name of Student: piyanshika
College name : IES college
Contact no : 9955365161
Branch: CS
Expected Date of Visit :  not confirmed date(m.p.nagar)
[22/02/24, 4:50:14 PM] annu❤️: Will Come today with Abhishek Chetak
[22/02/24, 4:54:04 PM] annu❤️: Will Come today indrapuri with Abhishek
[22/02/24, 5:16:53 PM] ~ Hafsa , Coding Thinker: Name of Student: Kumar Abhishek 
College name: IES
Contact no : 7367955221
Branch: CS
Expected Date of Visit : Will come after Holi
[22/02/24, 5:19:23 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- IES College of Technology
Name ;:- 	ASHWANI KUMAR TIWARI
Contact:- 	7571070460	
Expected date :; 	will think
[22/02/24, 5:21:05 PM] kasim k: Computer Science & Engineering	
IES College of Technology	
VIVEK KUMAR GAUTAM	
8827750980	
23 feb chetak
[22/02/24, 5:25:07 PM] ~ Memuna Coding Thinker: Name of Student: Sitesh Kumar Singh 
College name: Corporate institute of science and technology 
Contact no : 9939101400
Branch: CS
Expected Date of Visit : Will come in March
[22/02/24, 5:29:40 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Technocrat Institute of Technology	SATYAM KUMAR	7632007198	will come 10 match indrapuri
[22/02/24, 5:33:03 PM] annu❤️: Will Come today indrapuri
[22/02/24, 5:35:21 PM] ~ Memuna Coding Thinker: Name of Student: Udit Tripathi 
College name: Corporate institute of science and technology 
Contact no : 6265244276
Branch: CS
Expected Date of Visit : Will come in 5 March
[22/02/24, 5:35:49 PM] annu❤️: Will Come on 10 March with Sudhir
[22/02/24, 5:35:55 PM] khushi e.c: Branch :; - Computer Science & Engineering	
College ;:- IES College of Technology
Name :- 	MANISH KUMAR	
Contact:- 9508969882		
Expected date:-  after April
[22/02/24, 5:50:47 PM] kasim k: B.Tech	Computer Science & Engineering	
IES College of Technology	
ABDUR REHMAN	
8873874275	
23 feb chetak
[22/02/24, 5:51:16 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Technocrat Institute of Technology	RUDRANSH BUDHOLIA	7879732641	will come 1 march
[22/02/24, 5:51:51 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
College:-IES College of Technology
Name:-	PRAMOD PATEL
Number:-	6263588550
Expected date:-	will come 23feb
[22/02/24, 5:52:21 PM] khushi e.c: Branch ;- Computer Science & Engineering	
College :- IES College of Technology	
Name. :: MD SHAHJAD
Contact:- 	8877750408	
Expected date :- 	 3  March  m.p nagar
[22/02/24, 5:54:56 PM] ~ Hafsa , Coding Thinker: Name of Student: MD Saif Ali
College name: IES
Contact no : 9508107544
Branch: CS
Expected Date of Visit : Will come in mid March
[22/02/24, 6:00:50 PM] khushi e.c: Branch ;-: Computer Science & Engineering
College:- 	IES College of Technology	
Name. :- ANSHU KUMAR	
Contact:- 9905145008		
Expected date :- 25 Feb m.p nagar
[22/02/24, 6:04:27 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Sagar Institute of Research & Technology	
SAKSHI NARWARE	
9399243208	
not confirm date to visit 		
Indrapuri
[22/02/24, 6:09:54 PM] Lalita Sahu: B.Tech	Computer Science & Engineering
College:-	IES College of Technology
Name:-	AISHWARY SHAH
Number:-	6265733454	
 Expected date:- 26feb m.p.nagar
[22/02/24, 6:13:03 PM] kasim k: Name - ayushi pandey
collge - bansal cs ( mandideep)
number- 9302894233
expected date - 26feb (chetak )
[22/02/24, 6:14:15 PM] annu❤️: JNCT
Rishi Kumar Meena 
7869188168
Will Come 25 March
With Arun Meena
[22/02/24, 6:15:19 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Technocrat Institute of Technology	YUVRAJ KUMAR SINGH	6205339802	will come next month
[22/02/24, 6:18:02 PM] kasim k: Computer Science & Engineering	
Scope College of Engineering
CHANDAN DUTTA	
9693412055
10march
[22/02/24, 6:19:56 PM] annu❤️: Coming today indrapuri
[22/02/24, 6:32:29 PM] ~ Hafsa , Coding Thinker: Name of Student: Siddhant Sahu 
College name: IES
Contact no : 8435831380
Branch: CS
Expected Date of Visit : Will come in March
[22/02/24, 6:33:04 PM] ~ Hafsa , Coding Thinker: Name of Student: Swet Prakash 
College name: IES
Contact no : 8435831380
Branch: CS
Expected Date of Visit : 24 Feb ( Indrapuri )
[22/02/24, 6:41:59 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Technocrat Institute of Technology	SUMAYYA NAGMA	8229035200	will come 25 feb indrapuri
[22/02/24, 6:51:21 PM] Harsh sir tl: Team, it's time to demonstrate that we are the best! Let's work together to boost our organization's sales and showcase our capabilities. We've got this!
[22/02/24, 6:55:11 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
College:-IES College of Technology
Name:-	VIJAY KUMAR MANDAL	
Number:-7488678887
Expected date:- 24Feb
[22/02/24, 6:56:53 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Technocrat Institute of Technology	ADITYA RAJ	9263605950	come after holi  indrapuri
[22/02/24, 7:04:40 PM] ~ Memuna Coding Thinker: Name of Student: Abhishek Verma 
College name: TIT 
Contact no : 7000904259
Expected Date of Visit : In March
[22/02/24, 7:09:08 PM] anchal e.c: Will come today
[22/02/24, 7:09:15 PM] kasim k: Name - Aasmeen Khatun
number -081206 55983
collge - Sirt
 expected date of visit - 27 march indrpuri
[22/02/24, 7:09:27 PM] Neha mam e.c: Kaha par
[22/02/24, 7:09:43 PM] anchal e.c: Indrapuri
[22/02/24, 7:09:48 PM] Neha mam e.c: Ok
[22/02/24, 7:16:16 PM] annu❤️: FINAL 
MCA
Technocrats Institute of Technology [Excellence]
AMBESH RAJPUT	9981308137 	
23 February
Chetak
[22/02/24, 7:21:16 PM] kasim k: Name - faizan ahmed
number -8521590779
college- ies 
Expected date of visit - 
5march (chetak)
[22/02/24, 7:31:11 PM] ~ Hafsa , Coding Thinker: Summary of daily report
*DATE* - 22. 02. 2024

1. Name of caller - Hafsa

2 . How many of dial call -   61 + follow ups 

3 . How many no of connected call - 43

4 . For which course How many no of student shows interest to visit center- 4

5 . How many interested in  course - 7

 6 . Expected revenue per day
[23/02/24, 12:06:04 PM] khushi e.c: Name ::    Sunil 
Contact:- +91 79748 87351
With  Gaurav 
Course :- fsd
[23/02/24, 12:07:00 PM] ~ Hafsa , Coding Thinker: Name of Student: Faisal Imam
College name: IES
Contact no : 9060508527
Branch: CS
Expected Date of Visit : Will come in March
[23/02/24, 12:21:32 PM] ~ Hafsa , Coding Thinker: Name of Student: Aanya Sinha
College name: IES
Contact no : 6299009373
Branch: CS
Expected Date of Visit : 24 Feb
[23/02/24, 12:21:36 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Sagar Institute of Research & Technology	
PRIYANSH KATRE
	7000563429		
1 march java
[23/02/24, 12:33:48 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Sagar Institute of Research & Technology
	SHIVANI SAHU	6261074095		
will come march
[23/02/24, 12:40:45 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Sagar Institute of Research & Technology	
SHIVANSH SINGH	
6268749259	 
	will think
[23/02/24, 12:47:27 PM] kasim k: Name of Student: Rishabh 
College name: sirts
Contact no : 9827014372
Branch: ec
Expected Date of Visit : 25 sunday (chetak)
[23/02/24, 12:48:06 PM] kp sir: Kisi ka data science ka admission ho indrapuri main toh uskoo bulaa loo
[23/02/24, 12:48:23 PM] kp sir: Aaj backup hai
[23/02/24, 12:48:41 PM] ~ Deepali coding: Oky sir
[23/02/24, 12:50:55 PM] annu❤️: B.Tech	
Computer Science & Engineering	
J.N. College of Technolog
RAHUL KUMAR
8539882998	
25 March	Indrapuri 
2nd Year
[23/02/24, 1:10:11 PM] ~ Chauhan Shilpa: Name of Student: shiv Kumar 
College name: vaishnavi 
Contact no : 7692013715
Branch: aiml
Year:- 2 nd 
Expected Date of Visit : Will come in March ‎<This message was edited>
[23/02/24, 1:18:27 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Technocrat Institute of Technology	DEEP CHAUHAN	7000776749	will come march
[23/02/24, 1:18:35 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
College:-Technocrat Institute of Technology	
 Name :-YASHNESH NANDAN	number:-8651407421
	 Expected date:- 26Feb
[23/02/24, 1:23:11 PM] kasim k: sir kitne bja haiii
[23/02/24, 1:23:19 PM] kasim k: class backup
[23/02/24, 1:24:40 PM] ~ Deepali coding: 3 bje
[23/02/24, 1:24:45 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Technocrat Institute of Technology	ANJALI KUMARI	7439595181	will come 25 mp nagar
[23/02/24, 1:39:51 PM] Lalita Sahu: B.Tech	Computer Science & Engineering
	Technocrat Institute of Technology
	MANISH KUMAR
	6206407108	
will think
[23/02/24, 1:40:21 PM] kasim k: Name - khushi
Number -8109013218
branch - cs
visit date - 24 feb (indrpuri fsd)
[23/02/24, 1:44:40 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:: 	IES College of Technology	
Name :- INZAMAMUL HAQUE
Contact:- 	7070536545		 
Expected  :- after 1 week
‎[23/02/24, 2:42:16 PM] Neha mam e.c: IMG_5769.MP4 ‎document omitted
[23/02/24, 2:42:29 PM] Neha mam e.c: Make as a status
[23/02/24, 2:42:34 PM] ~ Deepali coding: Ok mam
[23/02/24, 3:08:44 PM] ~ Deepali coding: ‎This message was deleted.
[23/02/24, 3:09:27 PM] ~ Deepali coding: Computer Science & Engineering	Technocrats Institute of Technology & Science	ASAD KHAN	7805925580	come march
[23/02/24, 3:09:52 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- IES College of Technology
Name :- 	ANAND KUMAR
Contact:- 	9709515978		
Expected date:- 23 Feb m.p nagar
[23/02/24, 3:11:57 PM] khushi e.c: + Ankit
[23/02/24, 3:14:47 PM] kp sir: Yeah Anand and Ankit alag hai kya
[23/02/24, 3:15:54 PM] anchal e.c: Branch _ computer science
College _ TIT
Name _ vishal
Contact _70005 15658
Will come 26 feb
Indrapuri
[23/02/24, 3:15:59 PM] kp sir: Jo aaj yeah prospect Daalaa ,main judge karlerahaa huun ki yeah dono same hai
[23/02/24, 3:17:04 PM] ~ Hafsa , Coding Thinker: Name of Student: Indar Kumar
College name: JNCT
Contact no : 9576434569
Branch: CS
Expected Date of Visit : Will come after Holi
[23/02/24, 3:17:07 PM] kp sir: Aur apan call karke baat karrahe hain students se aur apan confirm nahi karpaarahe hain .
Aise kaise hoga kaam jab kuud hi yaad nahi ki Kisee baat hui phale
[23/02/24, 3:17:54 PM] khushi e.c: Sir freind hai Ankit
[23/02/24, 3:32:38 PM] kp sir: Madam main yeah bolrahaa huun ki yeah prospect aap phale bhi daalchukee hoo naa ,jaraa dhyan se dekheee
[23/02/24, 3:37:51 PM] khushi e.c: Ok sir
[23/02/24, 3:42:49 PM] khushi e.c: Sir group me show    nhi ho raha hai isliye dala hai dubara
[23/02/24, 3:42:57 PM] khushi e.c: Aaj aa rahe hain isliye
[23/02/24, 4:05:25 PM] anchal e.c: College _SIRt
Branch _AIML
7294834709	
ashif	
	26 feb 
indrapuri
[23/02/24, 4:22:30 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- IES College of Technology	
Name :- ASHISH SINGH	
Contact:- 8815379027	
Expected date :- 	24 Feb indrapuri
[23/02/24, 4:46:16 PM] anchal e.c: Will come day revisit with friend Izam
[23/02/24, 4:46:56 PM] annu❤️: B.Tech	
Computer Science & Engineering	
J.N. College of Technology	
SUHANI PATIDAR
6269559067	
5 March
2nd Year
[23/02/24, 4:52:26 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	IES College of Technology
Name :- 	BRINAL KUMAR SINGH
Contact:- 	8603895610	
Expected date:- 	will think in indrapuri
[23/02/24, 5:22:10 PM] ~ Chauhan Shilpa: Name of Student: Aishwarya 
College name: lnct
Contact no : 9279247097
Year:- 2 nd 
Expected Date of Visit : Will come in March
[23/02/24, 5:27:54 PM] ~ Chauhan Shilpa: Name of Student: ayush tripathi 
College name: lnct (cs) 
Contact no : 9302472853
Year:- 2 nd 
Expected Date of Visit : Will come in March last
[23/02/24, 5:33:03 PM] ~ Hafsa , Coding Thinker: Name of Student: Aastha Menhdole 
College name: NRI 
Contact no : 7828957831
Branch: CS
Expected Date of Visit : Will come in March
[23/02/24, 5:33:10 PM] Lalita Sahu: B.Tech	Computer Science & Engineering	
College:- Technocrat Institute of Technology
Name:-	LAHER CHOUKSEY
Number:-	7225958083	
Expected date:-will think
[23/02/24, 5:36:00 PM] khushi e.c: Branch ;+ :- Computer Science & Engineering	
College:-  IES College of Technology	
Name :- DEEPAK KUMAR PRASAD
Contact:- 	9113319446	
Expected date :- 	25 Feb
[23/02/24, 5:39:29 PM] ~ Chauhan Shilpa: Name of Student: harshit Vishwakarma 
College name: oist
Contact no : 9753967235
Year:- 2 nd 
Expected Date of Visit : 29 February
[23/02/24, 5:54:22 PM] ~ Hafsa , Coding Thinker: Name of Student: Sachin Rai
College name: NRI 
Contact no : 7610444346
Branch: CS
Expected Date of Visit : 26 Feb
[23/02/24, 5:56:55 PM] khushi e.c: Branch :- Computer Science & Engineering	 college :-IES College of Technology	
Name. :- AZAD ANSARI	
Contact:- 8298467293		
Expected date :- 	24 Feb m.p nagar
[23/02/24, 6:52:53 PM] annu❤️: ‎This message was deleted.
[23/02/24, 6:53:23 PM] kasim k: B.Tech	Computer Science & Engineering	
J.N. College of Technology	
NAGENDRA PRATAP SINGH	9302707157	
march batch
[23/02/24, 6:53:26 PM] kasim k: chetak
[23/02/24, 6:53:52 PM] annu❤️: B.Tech	
Computer Science & Engineering	
J.N. College of Technology
RAMNARAYAN DANGI	6264575169	
1 March
2nd year
[23/02/24, 6:55:32 PM] khushi e.c: Branch :- Computer Science & Engineering
 College:- 	IES College of Technology
Name :- 	SANKET SHRIVASTAVA
 Contact :- 	8989886620		
Expected date :- 	after 2 March
[23/02/24, 7:00:05 PM] Neha mam e.c: 24/ Feb Fsd Indripuri ke liye Kitne student hai sabhi ke pass
[23/02/24, 7:03:39 PM] ~ Deepali coding: Mere 3 hai mam
[23/02/24, 7:04:14 PM] kasim k: 2mam
[23/02/24, 7:04:49 PM] anchal e.c: 1 hai ma'am
[23/02/24, 7:05:17 PM] Neha mam e.c: Kal 4 the
[23/02/24, 7:05:27 PM] ~ Chauhan Shilpa: 2 hai ham
[23/02/24, 7:05:31 PM] ~ Deepali coding: Mam usme se ek kasim sir ka hai
[23/02/24, 7:05:35 PM] ~ Deepali coding: Ankush
[23/02/24, 7:05:37 PM] ~ Deepali coding: Ussi me se
[23/02/24, 7:07:05 PM] Neha mam e.c: Anchal 1 hi
[23/02/24, 7:07:14 PM] Neha mam e.c: Anchal kaise chalega
[23/02/24, 7:07:23 PM] Neha mam e.c: Sirf 2
[23/02/24, 7:07:34 PM] Neha mam e.c: Sirf 2
[23/02/24, 7:07:37 PM] ~ Hafsa , Coding Thinker: 2 hai madam 
Wo Monday ko aaenge
[23/02/24, 7:08:58 PM] anchal e.c: Ma'am 2 or hai but wo confirm nahi bta rhe kb ae gai
[23/02/24, 7:10:17 PM] ~ Chauhan Shilpa: Mam ek already Kara Diya hai is batch me
[23/02/24, 7:11:38 PM] ~ Chauhan Shilpa: Or student hai
[23/02/24, 7:24:23 PM] ~ Hafsa , Coding Thinker: Name of Student: Abhishekh Kumar 
College name: JNCT 
Contact no : 7610444346
Branch: CS
Expected Date of Visit : Will come in mid March
Aapka kuch nahi hai kya
[23/02/24, 7:31:05 PM] annu❤️: Mam 3 hai but wo March shift ho gyi hai
[23/02/24, 7:32:20 PM] ~ Memuna Coding Thinker: Mam mere visits h admissions nhi
[23/02/24, 7:33:18 PM] Neha mam e.c: Kab hai visit 20-22 days hogye aapko visit kuch bhi nahi hai aapki
[23/02/24, 7:35:46 PM] ~ Memuna Coding Thinker: Mam ane k bolte h phr call recieve nhi krte
[23/02/24, 7:36:22 PM] Neha mam e.c: To aise kaise chal payega
[23/02/24, 7:48:12 PM] kasim k: Name - Nishi
Number - 7509834647
branch - it 
coming 24 feb indrpuri
[23/02/24, 7:49:03 PM] kasim k: Name - Yogita
Number - 9179150447
collge - Bansal 
coming 24 feb (chetak )
[23/02/24, 7:49:48 PM] ~ Chauhan Shilpa: Name of Student: Paras Trivedi, Sanskar Tiwari, Prithvi Singh, Abhishek Trivedi, Tushar Singh, Rohit Kumar
College name: Oriental
Contact no : 8871901563
Branch: cs
Year:- 2 nd (cs)
Expected Date of Visit : 25 February
[23/02/24, 7:51:22 PM] kasim k: ‎You deleted this message.
[24/02/24, 11:37:07 AM] kp sir: Gautam ko call karloo Anchal ki kabsee karegaa class
[24/02/24, 11:39:00 AM] Neha mam e.c: Kp 4-5 student ur line up hai saath me 26-27 me karte hai
[24/02/24, 11:39:23 AM] Neha mam e.c: Indripuri ka backup complete ho gya kya
[24/02/24, 11:41:54 AM] kp sir: Nahi abhi dusri class hai
[24/02/24, 11:42:25 AM] kp sir: Maam aaj laga late hain phir 26 ko karengee ,
[24/02/24, 11:44:04 AM] anchal e.c: Sir 26 se aega wo
[24/02/24, 12:16:23 PM] kp sir: 2.30 PM se backup hai indrapuri main aaj Data science ka
[24/02/24, 12:16:54 PM] ~ Hafsa , Coding Thinker: Name of Student: Prince Kumar 
College name: JNCT 
Contact no : 9525580059
Branch: CS
Expected Date of Visit : Will come after 10 March
[24/02/24, 12:29:23 PM] annu❤️: Laksha Pardhi 
8819034897
Will Come 
Chetak
1 March FSD
[24/02/24, 1:05:00 PM] anchal e.c: B.Tech	Computer Science & Engineering-Internet of Things and Cyber Security Including Block Chain Technology
	Lakshmi Narain College of Technology	
SAQUIR ALI	
6203061035	 
	after 2 march
[24/02/24, 1:06:16 PM] ~ Memuna Coding Thinker: Name of Student: Adarsh Singh 
College name: LNCT 
Contact no : 9329944319
Branch: CS
Expected Date of Visit : Will come 15 March
[24/02/24, 1:15:21 PM] ~ Hafsa , Coding Thinker: Will go Indrapuri today
[24/02/24, 1:27:07 PM] anchal e.c: B.Tech	Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology	
PRASHANT BHOURGADE
	6263690082				
Will come 28 feb	
With friend sandesh 
Indrapuri ‎<This message was edited>
[24/02/24, 1:27:37 PM] ~ Hafsa , Coding Thinker: Will go Indrapuri today with friends
Amit and Shiv
[24/02/24, 1:47:07 PM] ~ Chauhan Shilpa: Name of Student: KAMINI MEHRA
College name: Bansal College of Engineering
Contact no : 6266629258
Branch: Computer Science & Engineering
Expected Date of Visit : Will come 5 March
[24/02/24, 1:58:24 PM] ~ Chauhan Shilpa: Name of Student: HAZIQUE MUJTABA
College name: Sha-Shib College of Technology
Contact no : 9060914929
Branch: Computer Science & Engineering
Expected Date of Visit : Will come 25 February (mp nagar)
[24/02/24, 2:03:24 PM] ~ Memuna Coding Thinker: Name of Student: Arnavya Shrivastav 
College name: LNCT 
Contact no : 8959935139
Branch: CS
Expected Date of Visit : 26 Feb
[24/02/24, 2:03:43 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrat Institute of Technology	
RITIGYA CHARAN
9142417515	
26 February	
Indrapuri 
2nd year
[24/02/24, 2:16:11 PM] kasim k: B.Tech
Mechanical Engineering	
J.N. College of Technology	
VARUN JATAV	
8269842214	
15March
[24/02/24, 2:54:32 PM] ~ Memuna Coding Thinker: Name of Student: Shivam  Ahirwar 
College name: LNCT 
Contact no : 9302484473
Branch: CS
Expected Date of Visit : 5 March
[24/02/24, 3:04:59 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	IES College of Technology	
Name :- AKRITI KUMARI
Contact:- 	7320920764	
Expected date:- will think
[24/02/24, 3:16:20 PM] ~ Memuna Coding Thinker: Name of Student: Sourav pal
College name: LNCT 
Contact no : 9301637229
Branch: CS
Expected Date of Visit : 5 March
[24/02/24, 3:24:40 PM] anchal e.c: B.Tech	Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology	RAUNAK NIGAM	6260717144	
9406888722	
Will think
Indrapuri
[24/02/24, 3:30:57 PM] ~ Memuna Coding Thinker: Name of Student: Lakshya Shukla + Khushi Katare 
College name: LNCT 
Contact no : 6261997683
Branch: CS
Expected Date of Visit : 5 March
[24/02/24, 3:43:14 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research, Technology & Science
Name :- 	BHOOPENDRA VISHWAKARMA
Contact:- 	6267838130	
Expected date ,:- 	after 5 March in
[24/02/24, 3:51:04 PM] khushi e.c: Branch :- B.Tech	Mechanical  Engineering	
College:- Bansal Institute of Research, Technology & Science
Name :- 	PRITAM WADIWA
Contact	:- 9516401163
Expected date :- 28 Feb m.p nagar
[24/02/24, 3:58:28 PM] khushi e.c: Branch :- B.Tech	Mechanical Engineering	
College,:- Bansal Institute of Research, Technology & Science
Name :- 	SHIVENDRA TIWARI
Contact:-:	9589156487
Expected date :- 	5 March
[24/02/24, 4:14:39 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrat Institute of Technology	
HARIOM PATEL
7879422718	
12 March	Indrapuri 
2nd Year
[24/02/24, 4:21:18 PM] ~ Deepali coding: ‎This message was deleted.
[24/02/24, 4:26:25 PM] ~ Deepali coding: Will come today mp nagar
[24/02/24, 4:29:54 PM] khushi e.c: With freind Rohit , vikash and prakash
[24/02/24, 4:32:36 PM] annu❤️: Name :- Vishal 
Number: - 9625330997
College :- radha raman 
Branch :- cs 
2nd year 
Expected date of visit :- 25 March
[24/02/24, 4:33:27 PM] khushi e.c: With  freind abdur
[24/02/24, 4:40:49 PM] ~ Memuna Coding Thinker: Name of Student: Arjit Gupta 
College name: LNCT 
Contact no : 6265022474
Branch: CS
Expected Date of Visit : 1 March
[24/02/24, 4:44:42 PM] kasim k: Name :- Vishal 
Number: - 8319511167
College :- tit
Branch :- it  
Expected date of visit :- 24feb
[24/02/24, 5:11:59 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:; - Bansal Institute of Research, Technology & Science
Name. :- 	HIMANSHU KALBHOR
 Contact:- 	9691181018	
Expected:- 	2 March indrapuri
[24/02/24, 5:46:12 PM] ~ Chauhan Shilpa: Name of Student: Abhinav Gupta 
College name: lnct
Contact no : 9109687967
Branch: CS
Expected Date of Visit :  25 February
[24/02/24, 5:54:08 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Bansal Institute of Research, Technology & Science
Name :- 	KHUSHI YADAV
Contact:- 	9343113880
Expected date :- 		3 March indrapuri
[24/02/24, 6:02:56 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research, Technology & Science
Name:- 	PRADEEP RAHANGDALE
Contact:- 	9131302329	
Expected date :- 	after 2 March  m.p nagar
[24/02/24, 6:05:49 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:- 	Bansal Institute of Research, Technology & Science	
Name :- HARIOM CHANDRAVANSHI
Contact:- 	9009025798		
Expected date:; 11March
[24/02/24, 6:27:52 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrat Institute of Technology	
SUJAL ADLAK
8817012702	
1 April
Java + DSA Chetak
2nd Year
[24/02/24, 6:30:04 PM] ~ Memuna Coding Thinker: Name of Student: Pratigya Singh 
College name: LNCT 
Contact no : 8319291980
Branch: CS
Expected Date of Visit : 25 Feb
[24/02/24, 6:31:56 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	ADARSH SONI	7388763699	will come after holi indrapuri
[24/02/24, 6:37:55 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Bansal Institute of Research, Technology & Science
Name :: -	SANDEEP KUMAR
Contact:- 	8581095425		
 Expected date:- 12 March m.p Nagar
[24/02/24, 6:41:48 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	MOHAMMAD HASNAIN	7389299870	will come 4-5 march indrapuri
[24/02/24, 6:43:41 PM] kp sir: @ Harsh sir Kal. 
Truba college 
JNCT 
SISTECH GHANDHINAGAR 
JANAA HAI .

DATA AAAJ HI  KAL KA ALLOT KARDENAA
[24/02/24, 6:44:11 PM] Harsh sir tl: Jii sir
[24/02/24, 6:48:04 PM] Neha mam e.c: Kal Sunday hai kp sir
[24/02/24, 6:52:11 PM] kp sir: Haan maam yeah log admission 15 bolte hain baithenge class main   aur 8 aate hain . 
Toh damag kaam karnaa bsnd kardiyaaa inloogg ko lag hi nahi rahaa hai ki batch 29 tak batch full karnaa hai .
[24/02/24, 6:52:36 PM] khushi e.c: Branch ;- B.Tech	Computer Science & Engineering
College:- 	Bansal Institute of Research, Technology & Science	
Name. :; RACHIT TRIPATHI
Contact:: 	8305321550	
Expected date :- 	3 march  m.p nagar
[24/02/24, 6:53:51 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research, Technology & Science
Name :- 	SHASHANK SEWAIWAR
Contact;:-	7898478368		
Expected date:- 7 March indrapuri
[24/02/24, 7:03:00 PM] anchal e.c: Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
MD MEHRAB HASAN	
7546016548	
with friend shiv Kumar, Faisal 
25 feb
Mp nagar
[24/02/24, 7:18:56 PM] anchal e.c: Computer Science & Bussiness System	
Oriental Institute of Science & Technology
	AYUSH RAJPOOT	
9329652252	
will think
[24/02/24, 7:26:08 PM] ~ Hafsa , Coding Thinker: Name of Student: Harsh Malviya 
College name: OIST
Contact no : 9525580059
Branch: CS/AI/ML
Expected Date of Visit : Will come in mid March
[24/02/24, 9:20:04 PM] Lalita Sahu: ‎Neha mam e.c removed Lalita Sahu
[25/02/24, 11:54:11 AM] Harsh sir tl: Aaj jis jis ki visits hai make sure they are coming
[25/02/24, 11:57:14 AM] anchal e.c: Name of Student: Dhananjay neware 
College name: TIT
Contact no : 9285351855
Branch: AIML
Expected Date of Visit : 25 feb
With friend sourabh 
Mp nagar
[25/02/24, 12:06:51 PM] kp sir: Data science ka backup new students ka aaaj Sunday 5.30PM par hai indrapuri main
[25/02/24, 12:11:28 PM] ~ Deepali coding: Oky sir
[25/02/24, 12:27:53 PM] anchal e.c: Computer Science & Engineering â€“ Artificial Intelligence
	Technocrat Institute of Technology	
ADITYA KUMAR YADAV	
7004426813	
Will come march
[25/02/24, 12:32:25 PM] anchal e.c: Will come today
[25/02/24, 12:52:36 PM] ~ Hafsa , Coding Thinker: Will go Indrapuri today with Pintu Kumar
[25/02/24, 12:55:51 PM] kp sir: Data science ya FSD
[25/02/24, 12:56:02 PM] kp sir: Data science ya FSD
[25/02/24, 1:22:47 PM] ~ Hafsa , Coding Thinker: FSD 
Visit h Sir
[25/02/24, 1:28:46 PM] anchal e.c: Fsd
[25/02/24, 1:34:48 PM] ~ Memuna Coding Thinker: Name of Student: Manish 
College name: Bansal CLG 
Contact no : 9301972652
Branch: ME
Expected Date of Visit : 26 Feb
[25/02/24, 2:03:15 PM] anchal e.c: Computer Science & Engineering	Patel College of Science & Technology	
vishal Yadav 	
9508952958	
26feb with friend rahul, sonu
Indrapuri
[25/02/24, 2:14:35 PM] khushi e.c: Will come after holi
[25/02/24, 2:14:36 PM] khushi e.c: ‎This message was deleted.
[25/02/24, 2:17:13 PM] khushi e.c: Will come with freind Abhishek 
m.p nagar
[25/02/24, 2:22:14 PM] Neha mam e.c: @918085394718 ek saath sabhi ko chutti de di kya
[25/02/24, 2:22:25 PM] Harsh sir tl: Nai mam
[25/02/24, 2:22:36 PM] Neha mam e.c: To kon kon aaya hai MP nagar me
[25/02/24, 2:22:54 PM] Harsh sir tl: Kasim anushree or durga ne off liya hai
[25/02/24, 2:23:03 PM] Harsh sir tl: Aaj arpana aane wali thi but aai nai
[25/02/24, 2:23:09 PM] Neha mam e.c: Arpana to already off hai na sir
[25/02/24, 2:23:23 PM] Neha mam e.c: 4 days ka bole ke gyi thi
[25/02/24, 2:23:30 PM] Harsh sir tl: Aaj wapas aane wali thi is basis pr mene unko dedi thi
[25/02/24, 2:24:21 PM] Neha mam e.c: Deepali ne ek student ko bheja tha vo direct class me chala gya usse koi office me nahi milla tha
[25/02/24, 2:24:59 PM] Harsh sir tl: Nai mam milliye the usse memuna ne baat ki thi or rupesh sir ne hafsa inquiry lerai thii
[25/02/24, 2:26:11 PM] ~ Hafsa , Coding Thinker: Registration Kara Raha h mam 
Wo aa gya
[25/02/24, 2:26:24 PM] ~ Deepali coding: Ok mam
[25/02/24, 2:27:13 PM] Neha mam e.c: Already kal enquiry lekar gya hai
[25/02/24, 2:27:25 PM] Neha mam e.c: Uper se usko niche vapis kiya hai
[25/02/24, 2:27:33 PM] Neha mam e.c: Rupesh sir se bole kar
[25/02/24, 2:29:18 PM] ~ Hafsa , Coding Thinker: Yes mam 
Mai thi nhi isiliye dekh nhi pai nhi to rok leti use
[25/02/24, 3:12:32 PM] ~ Chauhan Shilpa: Name of Student: RASHI NAGAR
College name: Scope College of Engineering
Contact no : 7489496027
Branch: Computer Science & Engineering
Expected Date of Visit :  29 February
[25/02/24, 3:28:26 PM] ~ Memuna Coding Thinker: Name of Student: Purnima kakde
College name: TIT
Contact no : 8817726981
Branch: CD
Expected Date of Visit : 10 March
[25/02/24, 3:41:22 PM] ~ Hafsa , Coding Thinker: Name of Student: Akshita Dawande
College name: OIST
Contact no :  9644001944
Branch: CS/AI/ML
Expected Date of Visit : Will come in March
[25/02/24, 3:46:43 PM] ~ Chauhan Shilpa: Name of Student: SHIBU KUMAR SINGH
College name:-Oriental Institute of Science & Technology
Contact no :  7765896596
Branch:Computer Science & Engineering-Data Science
Expected Date of Visit :  will come in March last
[25/02/24, 3:59:00 PM] ~ Chauhan Shilpa: Name of Student:- PRINCE KUMAR
College name:-Technocrat Institute of Technology
Contact no :  6200350439
Branch:-Information Technology
Expected Date of Visit :  will come in March
[25/02/24, 5:25:29 PM] ~ Memuna Coding Thinker: Name of Student: Abhishek Gupta 
College name: TIT
Contact no : 9935659424
Branch: Cs
Expected Date of Visit : 2 March
[25/02/24, 5:59:37 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	VINAMRA KHARE	9685694156	will come 2-3 march with harsh Gupta indrapuri
[25/02/24, 6:09:03 PM] anchal e.c: Information Technology	Bansal Institute of Science & Technology	
ANJALI CHIDAR	
8871331029	
will think
[25/02/24, 6:30:16 PM] anchal e.c: Computer Science & Engineering	Technocrats Institute of Technology & Science	
AJAY KUMAR RAJAK
	7987961356	
10 march 
Indrapuri
[25/02/24, 6:30:32 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	ABHISHEK KUMAR DUBEY	6200968218	will come 5 march indrapuri
[25/02/24, 6:37:53 PM] anchal e.c: Name - kaluram malviya 
Number - 9301363126
Visit Date - 1 March
With friend nirmala 
indrapuri
[25/02/24, 6:38:06 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	PRAJJVAL PAWAR	8770393212	will come 2 March indrapuri
[25/02/24, 6:40:03 PM] ~ Chauhan Shilpa: Name of Student:- SANJAY SINGH
College name:-Technocrat Institute of Technology
Contact no :  9770468180
Branch:-Information Technology
Expected Date of Visit :  will come in 10 March
[25/02/24, 6:41:48 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[25/02/24, 6:42:36 PM] ~ Memuna Coding Thinker: Name of Student: Faiz Siddiqui 
College name: TIT
Contact no : 7235999079
Branch: Cs
Expected Date of Visit : 8 March
[25/02/24, 6:47:14 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	ARADHYA PANDEY	7772984509	will come 5 march indrapuri
[25/02/24, 6:54:19 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	UTKARSH DONGRE	7828441610	come 2-3 march indrapuri
[25/02/24, 8:08:03 PM] ~ Chauhan Shilpa: Name of Student:- DEEPANSHU MAHESHWARI
College name:-Bansal College of Engineering
Contact no :  7354988076
Branch:-Computer Science & Engineering
Expected Date of Visit :  will come in 27 February (mp nagar)
[25/02/24, 8:19:29 PM] ~ Chauhan Shilpa: Name of Student:- VISHWAJEET PANDEY
College name:-Scope College of Engineering
Contact no :  9696737683
Branch:-Computer Science & Engineering
Expected Date of Visit :  will come in 6 March (mp nagar)
[25/02/24, 8:25:47 PM] ~ Chauhan Shilpa: Name of Student:- ARUN KUMAR SHARMA
College name:-Scope College of Engineering
Contact no :  8602870138
Branch:-Computer Science & Engineering
Expected Date of Visit :  will come in 8 March (mp nagar)
[25/02/24, 8:49:24 PM] ~ Chauhan Shilpa: Name of Student:- SAGAR SINGH
College name:-Technocrat Institute of Technology
Contact no :  6200625789
Branch:-Information Technology
Expected Date of Visit :  will come in 12 March
[26/02/24, 12:15:25 PM] ~ Mahi: coming today  inderpuri
[26/02/24, 12:20:56 PM] annu❤️: Amritesh Dwivedi 
7389103803
TIT 
AIML Branch 
2nd Year 
Will Come 25 March
[26/02/24, 12:40:58 PM] annu❤️: Prabhanshu Kamal Pandey
9302576485
Oriental College
Will Come 15 March 
With Aditya Sharma
[26/02/24, 12:43:13 PM] annu❤️: Electronics & Communication Engineering	
Oriental College of Technology	
ASHUTOSH KUMAR
6204891148
10 March
[26/02/24, 12:50:17 PM] annu❤️: Will Come 27 February 
Indrapuri
[26/02/24, 12:51:43 PM] anchal e.c: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	
PIYUSH JHADE
	8770800776		
27 feb indrapuri
[26/02/24, 12:58:22 PM] ~ Mahi: coming today 
in9derapuri
[26/02/24, 1:02:35 PM] ~ Chauhan Shilpa: Name of Student:- GAGAN KUSHWAHA
College name:-Bansal College of Engineering
Contact no : -7694853584
Branch:-Computer Science & Engineering
Expected Date of Visit :  will come in  March
[26/02/24, 1:05:45 PM] ~ Mahi: SONAM KUMARI	7986659419	
TIT	 MCA
will come april
[26/02/24, 1:06:36 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Sagar Institute of Research & Technology	
KRITYENDRA PATEL
	9685390040	
Will come 5 March
Indrapuri
[26/02/24, 1:13:17 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	HRITIK THAKUR	9479487100	come 2 March chetak
[26/02/24, 1:16:41 PM] ~ Chauhan Shilpa: Name of Student:- SUDHANSHU RANJAN
College name:-Technocrat Institute of Technology
Contact no : -8789470762
Branch:- Information Technology
Expected Date of Visit :  will come in  March ‎<This message was edited>
[26/02/24, 1:19:43 PM] annu❤️: Suryansh Raghuwanshi 
9893813717
Bansal College
10 March
2nd Year
[26/02/24, 1:20:40 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	AANCHAL KURMWANSHI	8305453291	come 27 feb indrapuri
[26/02/24, 1:26:52 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Bansal Institute of Research, Technology & Science
Name. :- 	RAJA PAL
Contact:- 	7722969650	
Expected date:- 	4 March indrapuri
[26/02/24, 1:26:53 PM] annu❤️: Name of Student: Amit
College name: TIT
Contact no: 9128793926
Branch: CSE
Year: 3RD
Expected Date of Visit:  1 March 
Web development
[26/02/24, 1:28:30 PM] anchal e.c: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	
RESHAV SHARMA
	9074716400	
 will think 	
Mp nagar
[26/02/24, 1:29:45 PM] kasim k: ‎You deleted this message.
[26/02/24, 1:32:03 PM] kasim k: Computer Science & Engineering	
Bansal Institute of Research, 
Technology & Science	
YUVRAJ NAMDEV
7880256747		
march 1week
[26/02/24, 1:36:27 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Bansal Institute of Research, Technology & Science
Name :; 	SEJAL	
Contact:- 8815962954		
Expected date:; after 5  March  f
[26/02/24, 1:59:52 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	MOHAMMAD DANISH	9113422826	will come today Evening indrapuri
[26/02/24, 3:57:25 PM] khushi e.c: Muskan 
9685001954
[26/02/24, 4:17:24 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:: Bansal Institute of Research & Technology	
Name :- VIKAS LODHI
Contact:- 	9302309827	
Expected date:-	after 5 March indrapuri
[26/02/24, 4:29:40 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:: 	Bansal Institute of Research & Technology
Name :- 	AMAR SINGH LODHI
Contact:- 	9755575307		
Expected date:- 1 march indrapuri
[26/02/24, 4:33:58 PM] khushi e.c: ‎This message was deleted.
[26/02/24, 4:36:13 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research & Technology	
Name :- SHWETA DWIVEDI	
Contact:- 8959481393
Expected date :- 		 will think
[26/02/24, 5:01:05 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Sagar Institute of Research & Technology	
PANKAJ BAHADUR SHAHI	
6232280019		
27 feb fsd 
indrapuri
[26/02/24, 5:21:58 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Bansal Institute of Research & Technology
Name :- 	GAKARE HARSH NARESH
Contact:- 	7499725914	
Expected date :- 	will think after March
[26/02/24, 5:22:55 PM] ~ Mahi: coming today with freind aditya pareek ‎<This message was edited>
[26/02/24, 5:26:19 PM] anchal e.c: B.Tech	Computer Science & Engineering	Sagar Institute of Research & Technology	
NITYA TIWARI
	9111802817		
Will think march 
Indrapuri
[26/02/24, 5:36:20 PM] anchal e.c: B.Tech	Computer Science & Engineering-Artificial Intelligence and Machine Learning
	IES College of Technology	
MD SAJID	
6202884652	
 	will come march 		
Mp nagar
[26/02/24, 5:41:08 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Bansal College of Engineering	NIKITA MEENA	8319233065	will come 27 feb with aarti and ayushi chetak
[26/02/24, 5:41:50 PM] ~ Mahi: Lakshmi Narain College of Technology Excellence
	RACHIT TIWARI
	7354672172
will come today  with frinds priyanshu shivam  yash
Inderapuri
[26/02/24, 5:45:25 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research & Technology	
Name. :- ANMOL DWIVEDI
Contact:- 	6266809868	
Expected	 date :- will think after March
[26/02/24, 5:45:55 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research & Technology
Name :- 	HARSH MISHRA
Contact:- 	8085294929	
Expected date :- 	after 15 March
[26/02/24, 5:57:58 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:- 	Bansal Institute of Research & Technology
Name :: 	VIKAS KUMAR JAISWAL
Contact:- 	8966882353	
Expected date :- 	3 march indrapuri
[26/02/24, 6:00:57 PM] kp sir: Khushi nahi aai hai kasim
[26/02/24, 6:01:31 PM] ~ Mahi: Lakshmi Narain College of Technology
	KARTIK RAJPUT
	748989109
will come today with frind Elijha 
inderpuri
[26/02/24, 6:08:10 PM] kasim k: sir call
kaat dia
[26/02/24, 6:09:35 PM] kp sir: Ku usi ka phone aaya tha naa 
Phir ku kaat diyaa
[26/02/24, 6:09:49 PM] ~ Mahi: Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
	RAHUL KUMAR BHAGAT	
7779919830
will come 2 march
with frinds Deepak ,Roshni,Rohit
Inderapuri
[26/02/24, 6:10:02 PM] kasim k: pta nahi sirrr 3 number se lga chuka kaat hi rahi haii abhi tau
[26/02/24, 6:10:22 PM] kp sir: ALIJHA TOH ENROLLED HAI SAYAD
[26/02/24, 6:10:31 PM] kp sir: Ok
[26/02/24, 6:11:37 PM] ~ Mahi: Elijha bola h usne baki aynge to dekh lena ap sir .konsi elijha h .
[26/02/24, 6:11:41 PM] kp sir: Lanka hai LNCT CS -DS branch ka check karloo ek baar
[26/02/24, 6:21:52 PM] annu❤️: Ravi Dangi 
9131609045
With friend Sanjeev Dwivedi
26 February
Indrapuri
[26/02/24, 6:29:22 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Bansal College of Engineering	VARSH RAJVARDHAN SINGH RAJPUT	7828458395	will come 29 feb chetak
[26/02/24, 6:41:30 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Bansal Institute of Research & Technology	
Name ;:- GOURAV THAKUR
Contact:- 	8839252782
Expected date :- 		    29 Feb indrapuri
[26/02/24, 6:46:53 PM] anchal e.c: B.Tech	Computer Science & Engineering-Artificial Intelligence and Machine Learning
	IES College of Technology	
PRAVEEN KUMAR YADAV	6206698995		
	8 march 
with friend upendra manidhar, Shashi
[26/02/24, 6:51:29 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research & Technology	
Name. ;:- DEEPAK
Contact:- 	6264587430	
Expected date :- 	2 march m.p nagar
[26/02/24, 6:53:50 PM] annu❤️: Yogesh Rai
7049874636
Will Come indrapuri
27 February
[26/02/24, 6:57:59 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal College of Engineering
	DISHA	
7024715261	
will come march
[26/02/24, 6:58:02 PM] ~ Deepali coding: B.Tech	Artificial Intelligence and Data Science	J.N. College of Technology	ROHIT MALVIYA	7354725841	will come 1 march
[26/02/24, 7:02:44 PM] ~ Deepali coding: B.Tech	Artificial Intelligence and Data Science	J.N. College of Technology	HARSH KUSHWAHA	9993805812	will come march first week
‎[26/02/24, 7:04:36 PM] Neha mam e.c: ‎image omitted
[26/02/24, 7:05:06 PM] Neha mam e.c: @916260034224 @919244005782 @916263551348  issi me kal fee leni hai
[26/02/24, 7:05:13 PM] ~ Deepali coding: Okay mam
[26/02/24, 7:05:17 PM] Neha mam e.c: Dhyan rakhe sab
[26/02/24, 7:05:23 PM] ~ Deepali coding: Ji mam
[26/02/24, 7:06:49 PM] ~ Chauhan Shilpa: Ji mam
[26/02/24, 7:07:33 PM] ~ Mahi: Lakshmi Narain College of Technology	
SINGH ABHISHEK RAMTA
	9022242361	
will come 1 .march with frinds
indrapuri ‎<This message was edited>
[26/02/24, 7:08:08 PM] ~ Mahi: ok mam
[26/02/24, 7:22:09 PM] ~ Mahi: Lakshmi Narain College of Technology	
VEDANT RAI	9407094220	
will come 2 march
indrapuri
[27/02/24, 12:21:57 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research & Technology	
Name :- DEEKSHA JHARIYA
Contact:- 	8450835413	
Expected date :- 	7  March
[27/02/24, 1:04:02 PM] ~ Mahi: Technocrats Institute of Technology [Excellence]
	ABHISHEK DUBEY
	8349369757
old prospect 
already visited 
will come for admision after 10 march
[27/02/24, 1:25:12 PM] kp sir: Harsh sir kahaa hooo aap
[27/02/24, 1:25:14 PM] kp sir: Abhi
[27/02/24, 1:26:42 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:- 	Bansal Institute of Research & Technology	
Name :- SHIVAM SHARMA	
Contact:: 9302036507	
Expected date:- 
	after holi
[27/02/24, 1:37:11 PM] annu❤️: Ritika Verma 
9589119420
LNCT College 
Will Come after 15 March
[27/02/24, 1:38:37 PM] annu❤️: Sarthak Mishra 
9977762820
Sagar College
CS Branch
Will Come today
27 February
[27/02/24, 1:41:12 PM] ~ Chauhan Shilpa: Name of Student:- SHREYANSH KUMAR
College name:-Technocrat Institute of Technology
Contact no : -8581875518
Branch:- Computer Science & Engineering
Expected Date of Visit :  will come in 16 March
[27/02/24, 2:56:00 PM] khushi e.c: Name :- Bittu Singh
Contact :; 8579875495
[27/02/24, 3:28:15 PM] ~ Hafsa , Coding Thinker: Name of Student: Aryan Baghel
College name: OIST
Contact no :  6265510247
Branch: CS/AI/ML
Expected Date of Visit : Will come in March ‎<This message was edited>
[27/02/24, 3:33:30 PM] ~ Memuna Coding Thinker: Name of Student: Sidharth Patel 
College name: TIT
Contact no : 8109209990
Branch: Cs
Expected Date of Visit : 15 March
[27/02/24, 3:37:00 PM] khushi e.c: Branch :; Electrical & Electronics Engineering
College:- 	Bansal Institute of Research & Technology	
Contact:- ANIL AHIRWAR
Name :: 	9399645771
Expected date :- 		15 March m.p Nagar
[27/02/24, 3:40:29 PM] ~ Mahi: Technocrat Institute of Technology	
SAURABH PATHAK	9179740448
already visited
will come for admision 29 feb
mp nagar
[27/02/24, 3:44:43 PM] khushi e.c: Branch :- Mechanical Engineering
College:- 	Bansal Institute of Research & Technology
Name :- 	SACHIN KUSHWAH
Contact:- 	8223018162
Expected date :- 	4 March indrapuri
[27/02/24, 4:21:46 PM] khushi e.c: Branch ;- B.Tech	Computer Science & Engineering	
College:- Bansal Institute of Research & Technology
Name :- 	JAY KUMAR PATEL
Contact:- 	8817694857	
Expected date :- 	6 March indrapuri
[27/02/24, 4:23:24 PM] khushi e.c: Branch :- Civil Engineering	
College:- Bansal Institute of Research & Technology	 
Name :- PARVATI KAHAR	
Contact :- 9302807605	
Expected date :- 	28 Feb Indra puri
[27/02/24, 4:47:58 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrat Institute of Technology	
ABHISHEK KUMAR	
9770585422	
1 March 
2nd Year
[27/02/24, 4:49:12 PM] ~ Mahi: Lakshmi Narain College of Technology & Science	HARSH JAIN
	9893776620	
will think
[27/02/24, 4:55:43 PM] ~ Memuna Coding Thinker: Name of Student: Harsh Namdeo
College name: TIT
Contact no : 9009893485
Branch: Cs
Expected Date of Visit : 1 March
[27/02/24, 4:58:20 PM] khushi e.c: Branch ;:- Computer Science & Engineering	
College:: -Bansal Institute of Research & Technology
Name :- 	ANAMIKA
 JAIN	
Contact:- 9301042290
Expected date :- 		5 March
[27/02/24, 5:01:07 PM] ~ Hafsa , Coding Thinker: Name of Student: Krishnanand Choudhary with Harshit Sharma 
College name: OIST
Contact no :  6265510247
Branch: CS/AI/ML
Expected Date of Visit : 3 March
[27/02/24, 5:06:11 PM] ~ Mahi: Bansal College of Engineering
	ANSHUL DHAKAR+1 frind
	8305709039	
will come 28 feb 
Mp nagar
[27/02/24, 5:16:23 PM] ~ Mahi: Lakshmi Narain College of Technology & Science
	JANVI MANDLOI
	8462911504	
will think
indrapuri
[27/02/24, 5:25:17 PM] ~ Memuna Coding Thinker: Name of Student: Mohd Niyaj Haider 
College name: TIT
Contact no : 9098862764
Branch: Cs
Expected Date of Visit : 29 Feb
[27/02/24, 5:30:40 PM] ~ Chauhan Shilpa: Name of Student:  YASH KUMAR PAL
College name: Technocrat Institute of Technology
Contact no :  9993533638
Branch: Computer Science & Engineering
Expected Date of Visit : 5  March
[27/02/24, 5:30:56 PM] khushi e.c: Branch :- Computer Science & Engineering
College;- 	Bansal Institute of Research, Technology & Science
Name ;- 	ALTAF KHAN
Contact:- 	7879142450		
Expected date :- 	15 March indrapuri
[27/02/24, 5:38:57 PM] kasim k: ‎You deleted this message.
[27/02/24, 5:39:26 PM] kasim k: ‎You deleted this message.
[27/02/24, 5:40:49 PM] kasim k: Name - ayushi pandey
number- 9302894233
collge - bansal collge mandideep
coming today +nikita+aarti
(indrpuri coming today)
[27/02/24, 5:49:23 PM] annu❤️: Shobhit 
8319615177
Will Come indrapuri
10 March 
Data science course
[27/02/24, 6:06:28 PM] ~ Chauhan Shilpa: Name of Student:  ARPIT GUPTA
College name: Technocrat Institute of Technology
Contact no :  7000289922
Branch: Computer Science & Engineering
Expected Date of Visit : 12  March
[27/02/24, 6:22:20 PM] ~ Chauhan Shilpa: Name of Student:-RAJ BAHADUR AHIRWAR
College name: Technocrat Institute of Technology
Contact no : -9755390922 
Branch: Computer Science & Engineering
Expected Date of Visit : will come in March
[27/02/24, 6:27:58 PM] Neha mam e.c: @917489380471 vo 2 admission ka kya hua
[27/02/24, 6:28:12 PM] Neha mam e.c: Kiske kitne admission hai iss month ke
[27/02/24, 6:28:37 PM] khushi e.c: Mam aaj unke bhaiya nhi aaye hai  shaam Tak aa jayenge ya fir kal confirm hai
[27/02/24, 6:28:50 PM] Neha mam e.c: @916264088400 aapki visit nahi hai kya kar rahi ho aap
[27/02/24, 6:29:06 PM] khushi e.c: Unke bhaiya ko bhi karna hai
[27/02/24, 6:29:32 PM] Neha mam e.c: Maam aap dekh lo roz roz tarakene se kaam nahi chal payega
[27/02/24, 6:29:53 PM] Neha mam e.c: Jisko bhi karna hai Mujhe admission se matlab hai
[27/02/24, 6:30:19 PM] Neha mam e.c: Iska answer sabko dena hai
[27/02/24, 6:32:46 PM] ~ Deepali coding: 7 Admission hai mam mere
[27/02/24, 6:33:15 PM] Neha mam e.c: Deepali 2 din ur bache hai kuch admission hai kya aapke
[27/02/24, 6:33:43 PM] ~ Deepali coding: Mam admission hai but sare 3-4 March ka bol rhe hai ab
[27/02/24, 6:34:43 PM] Neha mam e.c: Acha
[27/02/24, 6:34:50 PM] ~ Chauhan Shilpa: Mam 6 admission hai hamare
[27/02/24, 6:35:05 PM] ~ Deepali coding: Ji mam
[27/02/24, 6:35:15 PM] Neha mam e.c: Ur koi line up hai 2 days me
[27/02/24, 6:35:29 PM] ~ Chauhan Shilpa: Mam hai
[27/02/24, 6:35:43 PM] Neha mam e.c: Kab ke Shilpa maam
[27/02/24, 6:36:12 PM] ~ Chauhan Shilpa: Mam aj he ane Wale the par aye nahi Pani ke karan
[27/02/24, 6:36:35 PM] Neha mam e.c: Acha
[27/02/24, 6:36:49 PM] ~ Chauhan Shilpa: Or abhi visit aa rahi hai bo abhi interested hai
[27/02/24, 6:37:02 PM] Neha mam e.c: Acha
[27/02/24, 6:37:06 PM] ~ Chauhan Shilpa: Ji mam
[27/02/24, 6:37:22 PM] ~ Chauhan Shilpa: Akansha mishra 
Varsha sarathe
[27/02/24, 6:37:36 PM] kasim k: 6 admission
[27/02/24, 6:37:39 PM] ~ Chauhan Shilpa: Ye dono mp nagar ayengi 1 ko ragistration ke liye
[27/02/24, 6:37:42 PM] Neha mam e.c: @918085394718 25-30 admission se kuch nahi hone vala
[27/02/24, 6:38:10 PM] Neha mam e.c: @918085394718 aapne kya strategy bana rakhi hai kal mujhe aap batayega
[27/02/24, 6:38:52 PM] Neha mam e.c: 10 log ki team di hai unse sirf 25 admission karvaye hai to chalana bada mushkil hai
[27/02/24, 6:41:36 PM] Neha mam e.c: Answer dene me sabhi ko koi dikkat hai kya
[27/02/24, 6:42:00 PM] ~ Mahi: mre 3 admision total
[27/02/24, 6:42:06 PM] ~ Mahi: 2 lineup h
[27/02/24, 6:42:18 PM] Neha mam e.c: Kab tak
[27/02/24, 6:42:20 PM] ~ Mahi: baki jo h march ke
[27/02/24, 6:42:24 PM] ~ Mahi: feb me
[27/02/24, 6:42:36 PM] Neha mam e.c: 2 days hi bache hai
[27/02/24, 6:42:41 PM] ~ Mahi: hn mam
[27/02/24, 6:42:44 PM] ~ Hafsa , Coding Thinker: 4 admission
[27/02/24, 6:46:46 PM] Neha mam e.c: Sabne bata diya kya
[27/02/24, 6:47:12 PM] annu❤️: Mere 2 hai 29 ko
[27/02/24, 6:47:38 PM] Neha mam e.c: Ur kuch nahi hue kya aapke
[27/02/24, 6:48:10 PM] annu❤️: Hue hai mam 1
[27/02/24, 6:48:31 PM] ~ Memuna Coding Thinker: Mere admission nhi h
[27/02/24, 6:49:08 PM] Neha mam e.c: Aapki enquiry nahi ho to admission kaha se honge vo to uper likha hai
[27/02/24, 6:49:35 PM] Neha mam e.c: Anushree kar kya rahi ho
[27/02/24, 6:51:11 PM] Neha mam e.c: @916267544143 @919424704675 aapka kuch nahi hai to bole rahe nahi ho
[27/02/24, 6:51:22 PM] annu❤️: Mam 5 the mere pr batch shift krte krte wo March chale gye
[27/02/24, 6:51:41 PM] kasim k: ???
[27/02/24, 6:52:00 PM] Neha mam e.c: 1 hi baar to shift hua tha batch
[27/02/24, 7:01:53 PM] kasim k: kp sir indrpuri mai hai kyy ??
[27/02/24, 7:04:00 PM] Neha mam e.c: Ha
[27/02/24, 7:07:15 PM] Neha mam e.c: Memuna sabhi callers ki enquiry aa rahi hai bas aapka excuse hi chal raha hai ki student bahar hai
[27/02/24, 7:07:34 PM] Neha mam e.c: Bina registration to mushkil hoga mere liye
[27/02/24, 7:16:38 PM] khushi e.c: Branch ;- Computer Science & Engineering	
College;; :- Bansal Institute of Research, Technology & Science
Name :- 	NEHA RAJAK + salma khatoon
Contact:- 	9303612424		
Expected date:- 	28 feb Indra puri
[27/02/24, 7:45:24 PM] ~ Deepali coding: Branch ;- Computer Science & Engineering	
College;; :- tit
Name :- 	mayur
Contact:- 	6367848204
Expected date:- 	28 feb Indra puri with friend keshav
[28/02/24, 12:03:52 PM] ~ Deepali coding: Branch ;-me
Name :- 	imran raza
Contact:- 	9123240447
Expected date:- 	28 feb Indra puri old prospect
[28/02/24, 12:17:36 PM] ~ Mahi: coming today inderapuri
[28/02/24, 12:53:13 PM] khushi e.c: K.p Sir. Indrapuri  mein Inquiry aa  rahi hai aap waha par ho kya
[28/02/24, 12:53:46 PM] kp sir: Kitne baje
[28/02/24, 12:53:58 PM] kp sir: Main oist main huun abhi pahucha huu
[28/02/24, 12:54:07 PM] kp sir: Usko 2 baje bulaa loo
[28/02/24, 12:54:25 PM] khushi e.c: Nikal gai hai sir
[28/02/24, 12:59:53 PM] ~ Mahi: coming today +1 frind
mp nagar
[28/02/24, 2:09:19 PM] kp sir: Aai nahi hai abhi tak
[28/02/24, 2:10:53 PM] khushi e.c: Sir unse bol diya tha late ana or ab phone nhi utha rahe hai
[28/02/24, 2:11:16 PM] kp sir: 🙏
[28/02/24, 2:14:05 PM] kp sir: Yeah toh subha visit par aane walaa tha phone aaya tha iskaa . 
Ek teacher hai unka phone aaya tha
[28/02/24, 2:15:06 PM] ~ Deepali coding: Sir mera old prospect tha
[28/02/24, 2:15:07 PM] ~ Deepali coding: Ye
[28/02/24, 2:15:09 PM] kp sir: Call karloo iskoo Visit par aana tha aaaj
[28/02/24, 2:19:43 PM] kp sir: Sabhi ke saath same hoga Deepali maam , bahut se logo ka Maine considered nahi Kiya hai . Uahi considered karrahe hain jo old prospect main Dale hain visit ke phale
[28/02/24, 2:20:00 PM] ~ Deepali coding: Ok sir
[28/02/24, 2:48:56 PM] khushi e.c: Branch :- Mechanical Engineering
College:- 	Bansal Institute of Research, Technology & Science
Name:- 	CHANDRA PRATAP BUNDELA
Contact:- 	7974885252		
Expected date. :- 	6 March indrapuri
[28/02/24, 3:09:37 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research, Technology & Science
Name :: -	SUBHASH YADAV
Contact:- 	9179768579	
Expected date:; 	4 March m.p nagar
[28/02/24, 3:14:04 PM] ~ Hafsa , Coding Thinker: Will come on 4 Mar with friends ( Anshul+Devesh + Rishabh)
[28/02/24, 3:14:46 PM] kp sir: Tumhare 
Anurag ke saath wale aanrahe the parso abhi tak nahi aayeee unkaa kya
[28/02/24, 3:15:13 PM] kp sir: Hariom bhi tha sayad
[28/02/24, 3:15:41 PM] ~ Hafsa , Coding Thinker: Yes Sir 
Us din confirmation Dene bad usne call nhi uthaya
[28/02/24, 3:16:13 PM] ~ Hafsa , Coding Thinker: Maine class ka bhi bata diya tha msg ka reply bhi nhi de Raha
[28/02/24, 3:28:21 PM] khushi e.c: B.Tech	Computer Science & Engineering
College:- 	Bansal Institute of Research & Technology
Name :- 	ARUN RAIKWAR
Contact:: 	8889587585	
Expected date :: 	will think in Indra puri c+++
[28/02/24, 3:54:08 PM] ~ Hafsa , Coding Thinker: Name of Student: Ramakant Patil
College name: TIT
Contact no :  9691446260
Branch: CSE
Expected Date of Visit : Will come in mid March
[28/02/24, 4:26:07 PM] Neha mam e.c: Rishabh Pawar kissi ka admission hai kya
[28/02/24, 4:33:20 PM] khushi e.c: Branch:- Computer Science & Engineering
College:-	Bansal Institute of Research, Technology & Science
Name:-	NITEEN DIGARSE
Contact,:- 	6263606661		
Expected date:- 1 march indrapuri
[28/02/24, 4:44:35 PM] ~ Mahi: coming today 
indrapuri
[28/02/24, 4:46:02 PM] ~ Deepali coding: Number 6267848204
[28/02/24, 5:58:16 PM] anchal e.c: B.Tech	Computer Science & Bussiness System	IES College of Technology	
MD DILKASH AALAM	
6201331718	
Will come March
[28/02/24, 6:01:34 PM] ~ Deepali coding: B.Tech	Electronics & Communication Engineering	J.N. College of Technology	VIVEK CHOUHAN	6268293829	come 5 march chetak
[28/02/24, 6:08:17 PM] ~ Hafsa , Coding Thinker: Going Indrapuri with Anil
[28/02/24, 6:11:45 PM] annu❤️: Stuti gupta 
Friend 
Suhani katare 
Devki Gupta
[28/02/24, 6:25:51 PM] ~ Deepali coding: B.Tech	Artificial Intelligence and Machine Learning	J.N. College of Technology	ALOK RAJ	6204084479	come 4 March indrapuri
[28/02/24, 6:33:17 PM] ~ Mahi: Lakshmi Narain College of Technology & Science
	AYUSHI GUPTA
	8090283348	
will think after 5 march
[28/02/24, 6:36:46 PM] ~ Hafsa , Coding Thinker: Name of Student: Anirudh 
College name: LNCT
Branch: AI/ML
Expected Date of Visit : 29 Feb
[28/02/24, 6:44:52 PM] ~ Deepali coding: B.Tech	Artificial Intelligence and Machine Learning	J.N. College of Technology	RAHUL TIWARI	8770319796	will come 5 march indrapuri
[28/02/24, 6:55:01 PM] anchal e.c: B.Tech	Computer Science & Engineering-Artificial Intelligence and Machine Learning	IES College of Technology	
SAKSHI YADAV	934088322
first week of march 
Indrapuri
[28/02/24, 7:00:18 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research, Technology & Science
Name :- 	MANGAL PANDEY
Contact,:- 	7987211793	
Expected date:- 2 March m.p nagar
[28/02/24, 7:06:00 PM] khushi e.c: + Akash Pandey
[28/02/24, 7:11:25 PM] ~ Hafsa , Coding Thinker: Name of Student: Lakshya Asthana
College name: OIST
Contact no :  9301723862
Branch: CS/DS
Expected Date of Visit : 4 Mar ‎<This message was edited>
[28/02/24, 7:39:39 PM] ~ Mahi: with frind rudransh
[28/02/24, 9:10:30 PM] annu❤️: Kl batayengi wo
[29/02/24, 12:13:10 PM] ~ Deepali coding: B.Tech	Electronics & Communication Engineering	J.N. College of Technology	HARSH KUMAR	7667991923	will come after 15 march
[29/02/24, 12:21:47 PM] ~ Hafsa , Coding Thinker: Name of Student: Mohit Raut
College name: SIRTE
Contact no :  7974679889
Branch: CSE
Expected Date of Visit : After 10 March
[29/02/24, 12:22:38 PM] Neha mam e.c: @916264088400 aapke koi prospect nahi ban rahe hai kya
[29/02/24, 12:22:54 PM] Neha mam e.c: Na hi aap sale summary daalti ho
[29/02/24, 12:46:52 PM] ~ Deepali coding: B.Tech	Artificial Intelligence and Machine Learning	J.N. College of Technology	SUBHAN KHAN	8002788911	will come 7 March indrapuri
[29/02/24, 1:04:43 PM] ~ Deepali coding: B.Tech	Artificial Intelligence and Machine Learning	J.N. College of Technology	SAQUIB MAHFUZ	6202229454	wil come mid march	Indrapuri
[29/02/24, 1:27:51 PM] ~ Chauhan Shilpa: Name of Student:  vinit Kumar 
College name: Oriental 
Contact no :  9575729514
Branch: Cs (aiml)
Expected Date of Visit : 29  February ( indrapuri)
[29/02/24, 1:36:22 PM] ~ Hafsa , Coding Thinker: Name of Student: Yogesh Vishwakarma 
College name: SIRTE
Contact no :  8103080652
Branch: CSE
Expected Date of Visit : 4 March
[29/02/24, 1:49:11 PM] anchal e.c: B.Tech	Electronics & Communication Engineering	IES College of Technology	DINESH KUMAR
	7370071531		
15 march 
With friend amit yogesh
[29/02/24, 1:51:33 PM] ~ Hafsa , Coding Thinker: Name of Student: Abhishek Kasrade
College name: SIRTE
Contact no :  9584413697
Branch: CSE
Expected Date of Visit : Will come after Holi
[29/02/24, 2:54:20 PM] ~ Deepali coding: B.Tech	Artificial Intelligence and Machine Learning	J.N. College of Technology	VIKKI MAURYA	8528071061	will come 1 march indrapuri
[29/02/24, 3:05:51 PM] ~ Mahi: Trinity Institute of Technology & Research
	SHIVAM PATEL
	8770439099	
will come 8 march indore
[29/02/24, 3:12:27 PM] anchal e.c: Name - Aryan
Number _ 9262812488
Will come 29 feb
[29/02/24, 3:22:02 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	ADITYA DWIVEDI	8815834992	will come after 11 march indrapuri
[29/02/24, 3:50:47 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	NIKHIL MEWADA	8269425160	will come after 15 march
[29/02/24, 4:00:24 PM] anchal e.c: B.Tech	Computer Science & Engineering-Data Science
	IES College of Technology	
SUMAN VERMA
	7492080760			
will think 
 indrapuri
[29/02/24, 4:01:43 PM] ~ Mahi: Lakshmi Narain College of Technology & Science
	BASU TOMAR
	8349116672	
will come 6 march
indrapuri
[29/02/24, 4:08:25 PM] ~ Mahi: Lakshmi Narain College of Technology & Science
	HARSHVARDHAN
 DHUWARE	9691497396	
will come 1 march with. frind gourav
mp nagar
[29/02/24, 4:20:33 PM] ~ Hafsa , Coding Thinker: Name of Student: Bhupendra Kumar Vishwakarma 
College name: SIRTE
Contact no :  7470842860
Branch: CSE
Expected Date of Visit : Will come in March
[29/02/24, 4:27:36 PM] ~ Mahi: Lakshmi Narain College of Technology & Science
	AKASH TIWARI
	9340415106	
will come april
[29/02/24, 5:20:23 PM] Harsh sir tl: @919424704675 iska kya hua ??
[29/02/24, 5:20:54 PM] Harsh sir tl: @916263551348 mam iska kya hua ??
[29/02/24, 5:21:32 PM] Harsh sir tl: Team make sure your visit comes
[29/02/24, 5:22:31 PM] anchal e.c: Evening me
[29/02/24, 5:22:33 PM] anchal e.c: Aega
[29/02/24, 5:22:44 PM] anchal e.c: Indrapuri
[29/02/24, 5:23:26 PM] Harsh sir tl: @916263594069 iska kya hua ?
[29/02/24, 5:23:54 PM] ~ Deepali coding: March 4 ka bol rha
[29/02/24, 5:23:55 PM] ~ Hafsa , Coding Thinker: Name of Student: Astha Raypuria
College name: SIRTE
Contact no :  6260489830
Branch: CSE
Expected Date of Visit : 3 Mar
[29/02/24, 5:29:50 PM] anchal e.c: Sir a gai ye inquiry
[29/02/24, 5:29:52 PM] anchal e.c: Abhi
[29/02/24, 5:30:05 PM] anchal e.c: Visit done
[29/02/24, 5:38:49 PM] Harsh sir tl: Ok
[29/02/24, 6:04:07 PM] ~ Chauhan Shilpa: Sir just abhi call aya hai kl ane ka bol raha hai
[29/02/24, 6:05:07 PM] Harsh sir tl: Ok
[29/02/24, 6:44:58 PM] anchal e.c: B.Tech	Computer Science & Engineering	Trinity Institute of Technology & Research	
PALLAVI RANA
	7909919120		
will think
[29/02/24, 7:38:12 PM] anchal e.c: Name _ pradeep
College _ bansal
Branch _ CS
Number _ 9131302329
Will come 8 march
With friend Shashank ‎<This message was edited>
[01/03/24, 1:03:31 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	SUDHIR KUMAR	9142900659	will come after holi indrapuri
[01/03/24, 1:04:57 PM] Harsh sir tl: Team aaj ke liye around 30 visits plan ki hai sbne to make sure aap sabse follow up le
[01/03/24, 1:07:32 PM] kp sir: Admission bhi karayee sabhi 
K p sir ko birthday wishes main
[01/03/24, 1:09:18 PM] kp sir: Only one
[01/03/24, 1:16:23 PM] ~ Chauhan Shilpa: Name of Student: ritik Meena 
College name: vaishnavi
Contact no :  6265189911
Branch: ai 
Expected Date of Visit : 8  march ( indrapuri)
[01/03/24, 1:18:10 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	PRIYA PATEL	9399755628	will come 3 March indrapuri
[01/03/24, 1:18:42 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Bansal Institute of Research & Technology	
Name ;- DIVYANSH MALVIYA	
Contact:; 6265702772		 	
Expected date :-  2 March indrapuri
[01/03/24, 1:25:44 PM] kp sir: Chaloo kasim ,Deepali, Shilpa 
Ke aaj admission ke through muje wishes milrahi hai .
🙏🙏
Baaki log nahi karnaa chatee hain
[01/03/24, 1:43:21 PM] ~ Mahi: name of student Nitis kumar
8269298915
IES College 
3rd year
will come After holi 
Inderapuri
[01/03/24, 1:51:28 PM] ~ Mahi: Trinity Institute of Technology & Research
	PRABHAT YADAV
	6307173549	
will come 16 march
Indrapuri
[01/03/24, 1:53:57 PM] ~ Hafsa , Coding Thinker: Name of Student: Aman Lakhuja 
College name: LNCT
Contact no :  6260489830
Branch: CSE old prospect 
Expected Date of Visit : 3 Mar
[01/03/24, 2:01:57 PM] ~ Mahi: Trinity Institute of Technology & Research
	SACHIN SAHU
	9669108435	
will come 8 march
Mp nagar
[01/03/24, 2:05:11 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	YUGANT NATH	7471199126	will come 10 march
[01/03/24, 3:03:59 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	POOJA SAHU	9630105360	will come 5 march indrapuri
[01/03/24, 3:15:35 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrat Institute of Technology	
PIYUSH KUMAR SINGH
6207239039	
27 March	
Indrapuri 
2nd Year
[01/03/24, 3:20:24 PM] kp sir: Kaha hai 30 visit main toh indrapuri main hi hoon
[01/03/24, 3:51:32 PM] ~ Chauhan Shilpa: Name of Student:  SHUBHAM KUMAR
College name: NRI Institute of Information Science & Technology
Contact no :  8652520389
Branch: Computer Science & Engineering
Expected Date of Visit : 23 march ( indrapuri)
[01/03/24, 4:08:09 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrat Institute of Technology	
KAHAF
7987494069	
5 March	Indrapuri 
2nd Year
[01/03/24, 4:08:22 PM] kasim k: ‎You deleted this message.
[01/03/24, 4:16:35 PM] ~ Chauhan Shilpa: Name of Student:-AMRESH KUMAR SINGH
College name: Patel College of Science & Technology
Contact no : 6201125905
Branch: Computer Science & Engineering
Expected Date of Visit : 3 march ( indrapuri)
[01/03/24, 4:21:13 PM] annu❤️: Harsh Tripathi 9669170812
Will Come 12 March
Indrapuri
[01/03/24, 4:21:49 PM] ~ Hafsa , Coding Thinker: Name of Student: Atul Sen 
College name: Bansal
Contact no :  7879749778
Branch: CSE  
Expected Date of Visit : Will come in mid March
[01/03/24, 4:30:14 PM] ~ Hafsa , Coding Thinker: Name of Student: Taha Shameem
College name: TIT
Contact no :  7380855899
Branch: CSE  
Expected Date of Visit : 3 March
[01/03/24, 4:40:40 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	NEHA PRASAD	7000442868	will come 7 march
[01/03/24, 5:45:20 PM] ~ Mahi: Trinity Institute of Technology & Research
	AMAN RAJBHAR
	8287115860
	will come after 15 march
indrapuri
[01/03/24, 5:51:43 PM] khushi e.c: Branch :- Computer Science & Engineering
College:: 	NRI Institute of Information Science & Technology
Name ,:; 	KANAK GUPTA	
Contact:; 9229260199	
Expected date ,:- 	will think in indrapuri
[01/03/24, 6:01:42 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- NRI Institute of Information Science & Technology	
Name. :- RAKHI SHARMA	
Contact:- 9113408424	
Expected date :- 	 5 March indrapuri
[01/03/24, 6:04:49 PM] annu❤️: Will Come indrapuri with Anurag , On 2 March
[01/03/24, 6:07:29 PM] ~ Mahi: Trinity Institute of Technology & Researc	MD RAJ	
6205779706	
will come 2 march
witj frind saif
Indrapuri
[01/03/24, 6:14:25 PM] ~ Deepali coding: Will come today with hasmat ullah and ahemad
[01/03/24, 6:26:26 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	NRI Institute of Information Science & Technology	
Name :; BHARTI BOPCHE	
Contact:- 9343305894	 will think  after 	7 March
[01/03/24, 6:26:45 PM] ~ Chauhan Shilpa: Name of Student:-NILESH KUMAR
College name: Patel College of Science & Technology
Contact no :-8404960507
Branch: Computer Science & Engineering
Expected Date of Visit : 13 march ( indrapuri)
[01/03/24, 6:36:48 PM] khushi e.c: Branch ;:- Computer Science & Engineering	
College:: NRI Institute of Information Science & Technology	
Name ;- SACHIN CHAUDHARY
Contact:- 	8450880014		
Expected date:- 9march indrapuri
[01/03/24, 6:41:23 PM] ~ Mahi: Trinity Institute of Technology & Researcs	VIKRAM AHIRWAR
	8103748715	
will come 3 march
mp nagar
[01/03/24, 6:41:45 PM] ~ Hafsa , Coding Thinker: Name of Student: Nirbhay Singh Parihar + Pramay
College name: TIT
Contact no :  8602472757
Branch: CSE  
Expected Date of Visit :  6 March
[01/03/24, 6:46:33 PM] khushi e.c: Branch :+ Computer Science & Engineering	
College:; NRI Institute of Information Science & Technology	
Name :- PRATEEK SINGH	 +Aman 
Contact:: 7879805230	
Expected date :- 	2.march Indra puri
[01/03/24, 6:52:14 PM] ~ Mahi: Trinity Institute of Technology & Research
	AMIT SAHU
	9691623612	
will come 4 march
mp nagar
[01/03/24, 6:52:56 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	NRI Institute of Information Science & Technology
	Name :- NIKHIL GUPTA
Contact:- 	9827524565
Contact:- 		will think
[01/03/24, 6:56:00 PM] ~ Mahi: Trinity Institute of Technology & Research
	VISHAL AMARGHADE
	9516065043	
will come 3 march
mp nagar
[01/03/24, 6:58:01 PM] ~ Hafsa , Coding Thinker: Name of Student: Ritesh Kumar
College name: TIT
Contact no :  9453990076
Branch: CSE  
Expected Date of Visit : Will come after 10 March
[01/03/24, 6:58:59 PM] annu❤️: B.Tech	
Computer Science & Engineering
Technocrat Institute of Technology	
SUBHAM SIDHARTH
9334799192	
9 March	Java 
2nd Year
[01/03/24, 7:03:35 PM] ~ Mahi: Trinity Institute of Technology & Research
	BHAVESH PATHE
	7354457952
	will come 3 march
mp nagar
[01/03/24, 7:07:56 PM] ~ Mahi: Trinity Institute of Technology & Research
	ABHASH KUMAR
	6204893932
	will come after 5 march
mp nagar
[01/03/24, 7:11:24 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
J.N. College of Technology
	ALISHA SHAIKH	
9752747470	
4march chetak
[01/03/24, 7:11:39 PM] kasim k: Artificial Intelligence and Machine Learning	
J.N. College of Technology	
RAMJEE YADAV	
9580770622	
will think
[01/03/24, 7:12:13 PM] kasim k: B.Tech	
Artificial Intelligence and Machine 
Learning	
J.N. College of Technology	SOHEL KHAN	
9630893816	
2 march indpuri
[01/03/24, 7:12:15 PM] kasim k: B.Tech	Electronics & Communication Engineering	
Bansal College of Engineering
	PAYAL GOUR	
9301260947	
5march  indpuri
[01/03/24, 7:18:44 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
J.N. College of Technology	
MD IRSAD ALI	
7546908871	
10 March
[01/03/24, 7:19:46 PM] ~ Hafsa , Coding Thinker: Name of Student: Harsh Namdeo + Pradumn+ Saloni
College name: TIT
Contact no : 9009893485
Branch: CS
Expected Date of Visit : 2
 March ( Indrapuri )
[01/03/24, 7:52:40 PM] ~ Mahi: Trinity Institute of Technology & Research
	SHIVAM PATEL
	9301681945	
will think
[02/03/24, 12:06:32 PM] ~ Hafsa , Coding Thinker: Name of Student: Anupam Vishwakarma 
College name: SIRTE
Contact no : 7898945097
Branch: CS
Expected Date of Visit : 6 March
[02/03/24, 12:52:09 PM] khushi e.c: B.Tech	Computer Science & Engineering
College:; 	NRI Institute of Information Science & Technology
Name :- 	MOHAMMAD NAWAZ
Contact:; -	7061595148		
Expected date:- will think after 20 March
[02/03/24, 12:58:13 PM] annu❤️: B.Tech	
Computer Science & Engineering
Technocrat Institute of Technology	
MRITUNJAY SHRIVASTAVA
7771950865	
15 March	Java 
2nd Year
[02/03/24, 1:08:53 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- NRI Institute of Information Science & Technology	
Name :- TANUSHKA BHAGAT
Contact:- 	8871933918	
Expected date :- 	after 13 March
[02/03/24, 1:16:11 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:- 	NRI Institute of Information Science & Technology
Name :- 	SUJEET KUMAR MAHTO
Contact:- 	7050871855	
Expected date :- 	after holi c,c++
[02/03/24, 1:24:10 PM] ~ Hafsa , Coding Thinker: Will come at evening with friends
Name nhi bataya
[02/03/24, 1:31:00 PM] ~ Mahi: NRI Institute of Information Science & Technology	
JEEVESH SHUKLA	
8602837208	
will come after 8 march
mp nagar
[02/03/24, 1:32:31 PM] khushi e.c: College:- NRI Institute of Information Science & Technology
Name:- 	MAYURI DAMAHE
Contact:- 	6266545283	
Expected date :- 	after 10 March
[02/03/24, 1:39:33 PM] annu❤️: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology & Science
DHEERAJ PATEL	
7869983072
Will Come 3 March 
For registration
Indrapuri
[02/03/24, 1:58:41 PM] ~ Mahi: coming today 
mp nagar
[02/03/24, 2:37:47 PM] ~ Chauhan Shilpa: Name of Student:- SAKSHAM SAHU
College name:-Technocrat Institute of Technology
Contact no :-7007510320
Branch:- Computer Science & Engineering
Expected Date of Visit : 15 march ( indrapuri)
[02/03/24, 2:49:32 PM] ~ Chauhan Shilpa: Name of Student:- SOURABH SAHU
College name:-Technocrat Institute of Technology
Contact no :- 6263197558
Branch:- Computer Science & Engineering
Expected Date of Visit : 25 march ( indrapuri)
[02/03/24, 3:31:16 PM] annu❤️: Coming today with Rahul chetak
[02/03/24, 3:31:50 PM] ~ Hafsa , Coding Thinker: Name of Student:  Utkarsh Kumar 
College name: LNCT
Contact no : 7648962453
Branch: EE
Expected Date of Visit : 3 March
[02/03/24, 3:42:15 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- NRI Institute of Research & Technology
Name. :- 	JATIN KUMAR BAMAN
Contact;- 	9993061721		
Expected date:- will think
[02/03/24, 4:03:25 PM] khushi e.c: Branch ;:- B.Tech	Computer Science & Engineering
College:- 	NRI Institute of Information Science & Technology
Name :- 	AKASH KUMAR	 + Raj lodhi 
Contact:; 9685481358	
Expected date :- 	  will think indrapuri ‎<This message was edited>
[02/03/24, 5:10:55 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:: NRI Institute of Information Science & Technology	
Name :- RAHUL PATLE	
Contact:- 8966054708		
Expected date :- 20 March indrapuri
[02/03/24, 5:21:59 PM] ~ Hafsa , Coding Thinker: Name of Student:  Pranjal Shukla 
College name: LNCT
Contact no : 7440986727
Branch: CSE
Expected Date of Visit : 4 March
[02/03/24, 5:31:37 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- NRI Institute of Information Science & Technology
Name :- 	VIVEK KUMAR
Contact:- 	9142457610	
Expected date :- 	will think indrapuri
[02/03/24, 5:37:33 PM] kasim k: B.Tech	
Electronics & Communication Engineering	
J.N. College of Technology	
SUNIL KUMAR	
8210075162	
5 March
[02/03/24, 5:49:02 PM] annu❤️: B.Tech	
Computer Science & Engineering
Technocrats Institute of Technology & Science
ANKIT DANGI	8962775853	
4 March with Amit , Vishal Kumar 
Indrapuri 
2nd Year
[02/03/24, 5:56:12 PM] ~ Mahi: Bansal Institute of Science & Technology
	GOURAV RATHORE
	8839258389
	will come 3 march
mp nagar
[02/03/24, 6:02:17 PM] ~ Mahi: Bansal Institute of Science & Technology
	SATYAM PATEL
	7024811383	
will come 21 march
indrapuri
[02/03/24, 6:05:12 PM] khushi e.c: Branch :- Computer Science & Engineering-Cyber Security
 College :- Sagar Institute of Research & Technology
Name. :- 	ANSHUMAN SINGH
Contact:- 	7648812794		
Expected date:- after 7 March m.p nagar
[02/03/24, 6:08:16 PM] ~ Mahi: Bansal Institute of Science & Technology
	KIRTI RAJPUT
	6261483179	
will think end march
[02/03/24, 6:46:59 PM] ~ Mahi: NRI Institute of Research & Technology
	ANAND KUMAR UIKEY
	9893960527	
will come 3 march
mp nagar
[02/03/24, 6:56:05 PM] khushi e.c: Branch :- B.Tech	Electrical & Electronics Engineering
College:- 	Sagar Institute of Research & Technology
Name :- 	SHIVAM SAKET + Brijesh saket 
Contact:- 	9993670996	
Expected date ;- 	3/11/2024 indrapuri ‎<This message was edited>
[02/03/24, 6:58:34 PM] kasim k: B.Tech	
Artificial Intelligence and Data Science	
J.N. College of Technology	
PALAK RICHHARIYA	
9039482663	
will cnfrm after 2 days
[02/03/24, 6:58:46 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
J.N. College of Technology	
DEVENDRA VISHWAKARMA	
7999780124	
16 March
[02/03/24, 6:59:14 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
J.N. College of Technology	
SHIVANCHAL PANDEY	
6268348442	
11 March
[02/03/24, 7:21:22 PM] ~ Mahi: NRI Institute of Research & Technology
	SUNEEL KUSHWAHA
	7509252460	
will come after 20 march
with frind abhay and nikku
mp nagar
[03/03/24, 12:20:33 PM] ~ Hafsa , Coding Thinker: Will come on 4 Mar
[03/03/24, 12:32:51 PM] ~ Hafsa , Coding Thinker: Name of Student:  Lavi Pawar
College name: LNCT
Contact no : 7447021159
Branch: AI/DS 
Expected Date of Visit : 6 March
[03/03/24, 1:08:39 PM] ~ Hafsa , Coding Thinker: 8 Mar
[03/03/24, 1:10:57 PM] ~ Hafsa , Coding Thinker: Will go Indrapuri
[03/03/24, 1:40:32 PM] ~ Hafsa , Coding Thinker: On 5 March with Afaan , Shabaan , Zahid
[03/03/24, 2:06:05 PM] ~ Hafsa , Coding Thinker: Will go Indrapuri with Rohit
[03/03/24, 2:50:17 PM] ~ Chauhan Shilpa: Name of Student:  Sandeep 
College name: Bansal 
Contact no : 7447021159
Branch: mca
Expected Date of Visit : 5 March
[03/03/24, 3:09:01 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrat Institute of Technology	
SURENDRA SINGH LODHA	7999301018	
	will think
[03/03/24, 3:26:00 PM] ~ Mahi: will come today with frinds yashant shivam 
mp nagar
[03/03/24, 3:41:37 PM] annu❤️: Information Technology
Technocrat Institute of Technology	
AKSHAT SINGH RAGHUWANSHI	
6263580724
15 March
Chetak
[03/03/24, 3:43:29 PM] annu❤️: Coming today chetak
[03/03/24, 4:01:35 PM] annu❤️: Will Come 15 March with Aman and Gourav
[03/03/24, 4:38:04 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- NRI Institute of Information Science & Technology
Name :- 	MOHIT SANODIYA
Contact:- 	6267351569	
Expected date :- 	will think after.  10 March
[03/03/24, 4:39:03 PM] khushi e.c: College:- Computer Science & Engineering	
Branch :- NRI Institute of Information Science & Technology	
Name :- SUBHASH KUMAR
Contact:- 	7489990355	
Expected date. :- 	will think  after 15 March indrapuri
[03/03/24, 4:51:14 PM] khushi e.c: Branch :- Civil Engineering	
College:- Sagar Institute of Research & Technology	
Name :- RAJVEER RAO	
Contact,:- 9713844320	
Expected date :- 	4 March indrapuri
[03/03/24, 4:52:06 PM] ~ Hafsa , Coding Thinker: Will come on 4 March with Abhimanyu , Brijesh and one more friend
[03/03/24, 5:08:05 PM] khushi e.c: Branch :- Electrical & Electronics Engineering	
College:- Sagar Institute of Research & Technology
Name :- 	KANCHAN KUSHWAHA
Contact:- 	8839064472		
Expected date:- will think
[03/03/24, 5:32:14 PM] khushi e.c: Branch :- B.Tech	Artificial Intelligence and Machine Learning	
College:- Sagar Institute of Research & Technology
Name :- 	HIMANSHU GUPTA	
Contact:- 7067437827	
Expected date :- 	april
‎[03/03/24, 5:39:06 PM] Neha mam e.c: IMG_6242.MP4 ‎document omitted
[03/03/24, 5:56:48 PM] ~ Hafsa , Coding Thinker: Name of Student: Devesh Bodkhe
College name: SIRT
Contact no : 7470529435
Branch: CSE
Expected Date of Visit : 6 March
[03/03/24, 5:57:56 PM] khushi e.c: Branch :- Computer Science & Engineering-Cyber Security
College:- 	Sagar Institute of Research & Technology	
Name :- ABAAN ISHAQ	
Contact:- 9977998575		
Expected date;-  8 April
[03/03/24, 6:00:51 PM] ~ Mahi: Bansal Institute of Science & Technology
	TUSHAR TANDEKAR
	6261396410	
will think
[03/03/24, 6:04:47 PM] kasim k: Information Technology	
Oriental College of Technology
BHOOMIKA UGHADE	
7999548025	
will think date not cnfrm
[03/03/24, 6:10:30 PM] ~ Mahi: Bansal Institute of Science & Technology
	VIKAS SINGH
	9984683089	
will think 4 march
mp nagar
[03/03/24, 6:21:22 PM] ~ Mahi: Bansal Institute of Science & Technology
	DEVANSHU PANDEY
	8085962292	
will come 11 march
with frind Akash gourav and Anupam
mp nagar
[03/03/24, 6:29:33 PM] ~ Mahi: Bansal Institute of Science & Technology
	ARYAN SHAKYA
	6265796658
	will think 6 march
mp nagar
[03/03/24, 6:50:27 PM] ~ Mahi: ‎This message was deleted.
[03/03/24, 6:53:32 PM] ~ Hafsa , Coding Thinker: Name of Student: Piyush Panthi
College name: LNCT
Contact no : 9630790684
Branch: AI/DS
Expected Date of Visit : Will come after Holi
‎[03/03/24, 7:06:04 PM] kp sir: ‎audio omitted
[03/03/24, 7:07:29 PM] ~ Hafsa , Coding Thinker: Name of Student: Ashish Kumar 
College name: LNCT
Contact no : 8825125559
Branch: AI/DS
Expected Date of Visit : 5 March
[03/03/24, 7:09:19 PM] kp sir: Rachit Tiwari jo visit aai hai unkoo call mat karnaa aab jiski bhi visit hoo woo , unka number hi hatadoo , ki dubara galti se nahi koi call lagadee 
LNCT ke the .
Aise hi Durga ki visit thi LNCT ki aaya tha 3-4 din phale but koi response nahi tha sun hi nahi raha tha
[03/03/24, 7:10:05 PM] ~ Mahi: Bansal Institute of Science & Technology
	ANJALI SINGROLI
	7879309250
will come after 6 march with frind Akansha mishra
indrapuri
[03/03/24, 7:10:06 PM] Harsh sir tl: Ill delete these 2 contacts
[03/03/24, 7:19:31 PM] khushi e.c: Branch :- Computer Science & Engineering-Cyber Security	
College:- Sagar Institute of Research & Technology	
Name :- SUDHANSHU KUMAR
Contact;- 	9065817344		 
Expected date 10 March indrapuri
[03/03/24, 7:20:11 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Trinity Institute of Technology & Research
DEEPAK KUMAR SAKET
9179318873	
10 March	
Chetak , Indrapuri
2nd Year
[03/03/24, 7:38:13 PM] kasim k: B.Tech	
Information Technology	
Oriental College of Technology
SANSKAR KOLARE	
7024870591	
12 March
[03/03/24, 7:38:42 PM] kasim k: B.Tech
Computer Science & Engineering-Cyber Security	
Oriental College of Technology
NAVEEN KUMBHARE	
9111348904	
8March
[03/03/24, 7:41:54 PM] ~ Mahi: Bansal Institute of Science & Technology
	KASHISH PRIYA
	9304502162	
will come 11 march
mp nagar
[03/03/24, 7:53:24 PM] kp sir: Deepali uska kya hua online registration ka uit walaa jo karraha tha
[03/03/24, 8:17:36 PM] ~ Deepali coding: Sir bol rhe hai ki 5 ko aakar hi karte hai
[03/03/24, 8:17:52 PM] ~ Deepali coding: 2 friend or hai uske to bol rhe hai samne aakar hi kar leneg mam
[03/03/24, 8:20:55 PM] kp sir: OK Haan 2 OIST ke CS-BS ke hain
[03/03/24, 8:21:48 PM] ~ Deepali coding: Ji sir
[03/03/24, 8:26:08 PM] ~ Deepali coding: Name - Rahul 
College-LNCT
YEAR - 3
Branch -cs 
Reference Balram
Come 6 march
[04/03/24, 12:17:58 PM] ~ Mahi: will come today  indrapuri
[04/03/24, 12:25:36 PM] khushi e.c: Branch :- Mechanical Engineering
College:- 	Sagar Institute of Research & Technology
Name :- 	HEMANT KEER
Contact:- 	7067831675	
Expected date:- 	will think   m.p nagar
[04/03/24, 1:41:17 PM] kasim k: Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
ANKIT KUMAR	
8271087743		
6 March ( indrpuri )
[04/03/24, 1:42:54 PM] khushi e.c: Branch :- Civil Engineering
College:- 	Oriental Institute of Science & Technology	
Name :- SOM PATEL
Contact:- 	8269329218		 
Expected date:- after 10 March
[04/03/24, 1:46:37 PM] ~ Hafsa , Coding Thinker: Name of Student: Mohammad Niyaj Haider with Tofeeq and Naiyar Azam
College name: TIT
Contact no : 9098862764
Branch: CS
Expected Date of Visit : 4 March
[04/03/24, 1:48:18 PM] khushi e.c: Branch :-Civil Engineering
College:- 	Sagar Institute of Research & Technology	
Name :- TILESH KALPURE
Contact:- 	9986205413	
Expected date :- 	will think after 3 months
[04/03/24, 1:58:05 PM] kasim k: Computer Science & Engineering	
Patel College of Science & Technology	
SHIVENDRA KUMAR TIWARI	
9109478219	
after 25 march
[04/03/24, 3:12:48 PM] ~ Hafsa , Coding Thinker: Name of Student: Sajal 
College name: BITS
Contact: 7898404836
Branch: CS
Expected Date of Visit : 5 March
[04/03/24, 3:32:47 PM] ~ Mahi: name of student Ankesh pandey
9117179946
Tit collge Cse branch
2nd year 
will come After holi .
[04/03/24, 3:45:45 PM] khushi e.c: Will come today m.p nagar with priyansh
[04/03/24, 3:46:56 PM] khushi e.c: Will come today indrapuri with Dinesh and  Tika ram
[04/03/24, 3:52:03 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:- 	Bansal College of Engineering	
Name :- VISHAL YADAV	
Contact:- 8305486977		
Expected date:- 7 March indrapuri
[04/03/24, 4:00:29 PM] khushi e.c: Branch :- Electrical & Electronics Engineering
College:- 	Oriental Institute of Science & Technology
Name :- 	SUMIT PAL
Contact:- 	7000722572		
Expected date:- after 11 March indrapuri
[04/03/24, 4:08:03 PM] ~ Mahi: Name of student Anand vishwakarma
8959250093
TiT college
will come 5 march
mp nagar
[04/03/24, 4:08:04 PM] khushi e.c: Branch :- B.Tech	Mechanical Engineering
College:- 	Sagar Institute of Research & Technology
Name :- 	SAMEER MANUA
Contact:- 	8305440846		 
Expected date:- 5 March m.p nagar
[04/03/24, 4:08:55 PM] ~ Hafsa , Coding Thinker: Will go Indrapuri today
[04/03/24, 4:41:53 PM] ~ Hafsa , Coding Thinker: Name of Student: Abhishek Lodhi
College name: SIRTE
Contact: 8889595689
Branch: CSE
Expected Date of Visit : 5 March ( Indrapuri )
[04/03/24, 5:14:21 PM] ~ Deepali coding: Name of Student: isha 
College name: Lnct
Contact:  7000788849
Branch: CSE
Expected Date of Visit : 15  March ( Indrapuri
[04/03/24, 5:19:24 PM] khushi e.c: Branch :- Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College :- Oriental Institute of Science & Technology	
Name :- NANDINI KAWALE
Contact:- 	8770071869		
Expected date:- June
[04/03/24, 5:30:06 PM] ~ Mahi: Bansal Institute of Science & Technology
	NITIN SINGH DANGI
	9302456375
	will come 7 march
mp nagar
[04/03/24, 5:51:35 PM] ~ Mahi: Bansal Institute of Science & Technology
	AMIT KUMAR SINGH
	8603087891	
will think 10 march
mp nagar
[04/03/24, 5:58:13 PM] khushi e.c: Branch :: - Computer Science & Engineering	
College:- Oriental Institute of Science & Technology	
Name:- TAPESH CHAVLE
Contact:- 	6263442911		
Expected date:- 10 March indrapuri
[04/03/24, 6:03:52 PM] ~ Chauhan Shilpa: Name - Tanishq 
Number - 9399890491
Visit date - will come Last march (mp nagar office)
[04/03/24, 6:04:45 PM] ~ Mahi: Bansal Institute of Science & Technology
	YASH GHODKI
	6261513702	
will come 5 march
indrapuri
[04/03/24, 6:13:45 PM] ~ Mahi: Bansal Institute of Science & Technology
	ABHISHEK DHAKAD
	9584327874
	will think 5 march 
with frinds pankaj nagar ayush raj
indrapuri
[04/03/24, 6:26:43 PM] ~ Chauhan Shilpa: Name of Student: Govind 
College name: Bansal 
Contact no: 8815771050
Branch: AIML
Year: 1ST
Expected Date of Visit:  will come April
[04/03/24, 6:27:20 PM] ~ Mahi: Bansal Institute of Science & Technology
	KAVITA GOSWAMI
	9691713158	
will think 11 march 
mp nagar
[04/03/24, 6:57:26 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	IES College of Technology
Name :- 	AMIT PRAKASH
Contact:- 	9117492187			
Expected date:- 6 march  indrapuri
[04/03/24, 7:05:23 PM] khushi e.c: Branch :- Computer Science & Engineering
College;- 	IES College of Technology
Name ;- 	UDAY KSHEERSAGAR
Contact:- 	8269366987	
Expected date:- 10 March m.p nagar
[04/03/24, 10:00:36 PM] ~ Deepali coding: Branch :- Computer Science & Engineering
College;- 	truba
Name ;- Sanjeet nagar
Contact:- 	7354230232
Expected date:- 6March m.p nagar
[04/03/24, 10:04:18 PM] Neha mam e.c: abhi aapan ko konse college me response mill raha hai
[04/03/24, 10:17:36 PM] Neha mam e.c: Koi ajeeb question puche liya kya
[04/03/24, 10:33:11 PM] kasim k: ‎You deleted this message.
[04/03/24, 10:35:55 PM] Neha mam e.c: Office me bole raha tha ki oriental me response nahi mill raha vo syreyans jaa raha hai
[04/03/24, 10:37:23 PM] kasim k: han mai orirntal ka hi bol raha 
 tha
[04/03/24, 10:42:51 PM] Neha mam e.c: Me aapse puche rahi hu ki konse college me acha response mill raha hai
[04/03/24, 10:52:11 PM] kasim k: Oriental College of Technology
[04/03/24, 10:53:13 PM] kp sir: Aaj toh 3 registration hue hai OiST ke response ku nahi aarahaa kon si branch ka calling karrahe hoo
[04/03/24, 10:53:36 PM] Neha mam e.c: Kasim simple question puche rahi hu kis college me aapna feedback acha hai
[04/03/24, 10:53:39 PM] kasim k: mix hai me , It , civil
[04/03/24, 10:53:53 PM] kp sir: Iskaa achha response hai yaa nahi
[04/03/24, 10:54:26 PM] Neha mam e.c: @918085394718 tumne kon se caller ko konsa college assign kiya hai
[04/03/24, 10:54:36 PM] Neha mam e.c: 2nd year me
[04/03/24, 10:54:45 PM] Neha mam e.c: And 3rd year me
[04/03/24, 10:54:57 PM] Neha mam e.c: 1st year also
[04/03/24, 10:55:21 PM] kasim k: mere mai ni nikal raha lg bhg sub sheryansh mai join hai krna nahi  hai call kt rahe
[04/03/24, 10:55:35 PM] kp sir: @Harsh sir sayad time nahi milrhaa hai data proper Dene ka ki phale bhi bolaa huun ki sabse phale acche college , main CS , IT DS Aiml denaa hai apan CE ,ME allot karrahe hain randomly
[04/03/24, 10:56:06 PM] kasim k: cs v hai sir usme
[04/03/24, 10:56:21 PM] Neha mam e.c: ??
‎[04/03/24, 10:56:33 PM] kp sir: ‎audio omitted
[04/03/24, 10:58:00 PM] kasim k: ni sir maine sirf  Oriental College of Technology ispe hi calling ki haiii
[04/03/24, 10:58:34 PM] kasim k: tau wo sunn v nahi rahe proper aur sunn rahe the end mai will think mai ja rahe
[04/03/24, 10:59:47 PM] kp sir: Achha thik hai 
Kal main 2 baje office aaungaa , Abb data main allot karungaa sabhi ko 2 year and 1 year .
Harsh aap Kal se college visit aur workshop par focus karooo aur muje Data Bata denaa ki kya allot Kiya hai wo marked hogaa
[04/03/24, 11:00:05 PM] kp sir: OCT PAR CALALING ROK DOO ABB
[04/03/24, 11:00:44 PM] kp sir: Parso se workshop lagrahi hai waha Aman sir ki ,uske baad karnaa OCT par CS main calling
[04/03/24, 11:01:42 PM] kasim k: ok sirr
[04/03/24, 11:03:52 PM] Neha mam e.c: 6 March tak tumne mujhe 11-12 registration ka projection diya hai Anushree
[04/03/24, 11:04:28 PM] Neha mam e.c: Ye karna hai parso tak
[05/03/24, 12:03:24 AM] kp sir: @Team ,new batch Data science ka indrapuri main start horahaa hai 9 Tarik se toh iskoo bhi dhyan rskhnaa jo students bolrahe hain unkoo Bata sakte hain indrapuri jo join karnaa chatee hain .
[05/03/24, 8:13:16 AM] Harsh sir tl: Cs it or Ai Ds ka hi allot kiya hai
[05/03/24, 8:13:30 AM] Harsh sir tl: 1-2 1-2 number hi h beech m
[05/03/24, 8:14:07 AM] Harsh sir tl: M sirf CS IT Ai ds pr hi focus krraha hun
[05/03/24, 8:14:29 AM] Harsh sir tl: Civil ke to wo bhi clear bolkr ke bataya hai
[05/03/24, 8:15:16 AM] Harsh sir tl: 60-60 70 number deraha hun to 2-3 number civil wagera ke h to i don’t think tht is such an big issue
[05/03/24, 8:17:28 AM] Harsh sir tl: Sirf TIT LNCT SIRT SIRT E , sistec , JNCT , NRI, bansal or corporate ka data hi allot kiya hun
[05/03/24, 11:13:50 AM] kp sir: Ok
[05/03/24, 11:46:52 AM] ~ Hafsa , Coding Thinker: Name of Student: Anjali Kushwaha with Pooja 
College name: Bansal 
Contact no: 9285548893
Branch: Civil
Expected Date of Visit:  6 March
[05/03/24, 11:56:21 AM] ~ Chauhan Shilpa: Name of Student: Sneha Jaiswal 
College name: lnct
Contact no: 9109616550
Branch: cse
Expected Date of Visit:  8 March
[05/03/24, 12:04:12 PM] ~ Chauhan Shilpa: Name of Student: Nikhil Nigam
College name: tIt
Contact no: 9669634783
Branch: cse
Expected Date of Visit:  8 March
[05/03/24, 12:10:50 PM] ~ Mahi: Name of Student Shalini bisane
6260321713
NRI College
will come 5 march 
mp nagar
[05/03/24, 12:40:16 PM] anchal e.c: Manesh Kumar
8207430095
Will come after 10 march
mp nagar
[05/03/24, 12:46:52 PM] ~ Hafsa , Coding Thinker: Name of Student: Abhishek Thakur with Akash, Satendra and more friends 
College name : TIT
Contact no: 9798898338
Branch: EE
Expected Date of Visit:  5 March
[05/03/24, 12:50:50 PM] ~ Mahi: Name of student  Ankit shurkiwal
7693964204
Sirt College
will think
[05/03/24, 12:51:25 PM] annu❤️: Coming today with Vinayak, devashree
[05/03/24, 1:35:41 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	RAVIKANT SEN	8878315526	will come after holi
[05/03/24, 1:38:40 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	VINAY BISEN	7354216958	come 10 march indrapuri
‎[05/03/24, 1:44:10 PM] Neha mam e.c: ‎image omitted
[05/03/24, 1:46:39 PM] ~ Chauhan Shilpa: Name of Student: satyam 
College name: tIt
Contact no: 7828391659
Branch: cse
Expected Date of Visit:  12 March ‎<This message was edited>
[05/03/24, 2:49:28 PM] annu❤️: Suhani friend coming today indrapuri
Paras
[05/03/24, 3:10:48 PM] kasim k: will come with friends zahid , afaan,huzaifa, 
will come today( mp nagar )
 @916260034224
[05/03/24, 3:27:10 PM] ~ Deepali coding: Name mithlesh
College bansal
Year 2 year
Branch cs
Number. 95756769041
Already visited
Will come for registration 7 march
[05/03/24, 3:47:46 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	IES College of Technology	
VIJAY SHAKTI TIWARI	
9608575311	 
will think
[05/03/24, 4:00:06 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Trinity Institute of Technology & Research	
SUDHA KUMARI	7439983750		
After 15 march
[05/03/24, 4:30:51 PM] ~ Mahi: will go today indrapuri
[05/03/24, 5:00:58 PM] ~ Chauhan Shilpa: Name of Student: VAIDIK TAMRAKAR ( sparsh Sandeep)
College name: Sagar Institute of Research & Technology 
Contact no: 9826484300
Branch: Computer Science & Engineering
Expected Date of Visit:  5  March
[05/03/24, 5:21:18 PM] Harsh sir tl: @916263551348 mam yeah kitne baje visit kiya tha aapne abhi update kiya hai we won’t be able to consider this
[05/03/24, 5:34:45 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal College of Engineering
ARYAN
7806072555	
7/8 march will think
(chetak bridge)
[05/03/24, 5:45:19 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Trinity Institute of Technology & Research
GYANAM SRIVASTAVA
9135134302	
Python 	In April 
2nd Year
[05/03/24, 5:45:26 PM] ~ Mahi: will come  today mp nagar
[05/03/24, 5:47:47 PM] ~ Hafsa , Coding Thinker: Name of Student: Sahil Ahmad 
College name : Bansal 
Contact no: 8962281950
Branch: CS
Expected Date of Visit:  6 March
[05/03/24, 5:49:13 PM] Harsh sir tl: @916263551348Shilpa mam kindly add all your old prospects in group so that no misunderstanding happens every one has done the task which i have assigned only you are remaining kindly do this by the end of 06-03-2024
[05/03/24, 5:53:40 PM] khushi e.c: Branch :- Computer Science & Engineering-Cyber Security	
College:- Lakshmi Narain College of Technology & Science	
Name :- AMAN RAJ
Contact:- 	8757510300	
Expected date :- 	12 March indrapuri
[05/03/24, 6:05:47 PM] khushi e.c: Computer Science & Engineering	NRI Institute of Information Science & Technology	DHRUV PRATAP SINGH	9179660790		will think after 14 March
[05/03/24, 6:12:31 PM] kp sir: @Harsh sir Mere saamne call aaya  tha Shilpa ke pass main wahi baitha tha , vadik wale students aur wo saamne muje Bolkar bhi gye hain ki maam se baat hoti thi meri , Enquiry ke time 30 min enquiry toh Maine li hai unki
[05/03/24, 6:13:25 PM] kp sir: Jab main yaha baitha huun means kuch galat nahi hoga don't worry
[05/03/24, 6:18:58 PM] kasim k: Priyanka Gautam 	8989903603		
Institute for Excellence in Higher Education 	
2025	
before 12 march ( chetak )
[05/03/24, 6:21:13 PM] ~ Mahi: Monika
9009318672
Institute for Excellence in Higher Education 	
2025	
will come in april
mp nagar
[05/03/24, 6:22:59 PM] khushi e.c: Branch Computer Science & Engineering-Cyber Security
College:- 	Lakshmi Narain College of Technology & Science	
Name. :- AGRIMA JAIN
Contact:- 	6386296690		
Expected date:-  will think indrapuri
[05/03/24, 6:23:03 PM] ~ Chauhan Shilpa: Will come today with Anup mishra
[05/03/24, 6:29:45 PM] annu❤️: ‎This message was deleted.
[05/03/24, 6:35:11 PM] ~ Deepali coding: Name Akshay pal
College excellence
Brach cs
Number 88278 44882
Will come 9 March indrapuri
[05/03/24, 6:42:32 PM] annu❤️: Anshita Jain
7440498722
Will think
Institute for excellence in higher education
[05/03/24, 6:44:47 PM] ~ Deepali coding: Abhinav sharma
Excellence
Cs
7470415399
Come 7 march indrapuri
[05/03/24, 6:46:09 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering-Artificial Intelligence and Machine Learning	
College:- Lakshmi Narain College of Technology & Science
Name:- 	ADARSH KOURAV	
Contact:- 6267309046
Expected date ;- 		12 March
[05/03/24, 6:54:01 PM] khushi e.c: Branch :- Computer Science & Engineering-Cyber Security	
College:- Lakshmi Narain College of Technology & Science
Name :- 	RASHI STHAPAK	
Contact:- 8982416188	
Expected date :- 	will think after holi m.p nagar
[05/03/24, 6:55:45 PM] ~ Hafsa , Coding Thinker: Name - Palak Lalwani
College-LNCT
Branch - CS/AI/ML 
Reference Nayan
Will Come on 6 march
[05/03/24, 7:25:35 PM] khushi e.c: Branch :- Computer Science & Engineering-Cyber Security	
College:- Lakshmi Narain College of Technology & Science
Name :- 	RAJAT KAWRE + 1 freind 
Contact;:- 	8319803870	

Expected date:- 9 March indrapuri ‎<This message was edited>
[05/03/24, 7:40:18 PM] ~ Mahi: NRI Institute of Research & Technology
	SAKSHI DUBEY
	6263227301
	will come 7 march
mp nagar
[05/03/24, 10:40:37 PM] kp sir: Harsh 
Bansal aur kis college se response milrahA tha
[05/03/24, 10:48:13 PM] Harsh sir tl: Tit
[05/03/24, 10:48:27 PM] Harsh sir tl: Inke prospects bnrahe the
[05/03/24, 10:48:49 PM] Harsh sir tl: Baaki colleges ke compare m inka response better tha
[06/03/24, 12:33:07 PM] annu❤️: Will Come today with imrat singh
[06/03/24, 12:35:01 PM] ~ Deepali coding: Will come today with neeraj
[06/03/24, 12:37:51 PM] khushi e.c: Branch :- Information Technology	Oriental 
College:- Institute of Science & Technology
Name :- 	AAKANSH RATHORE
Contact:- 	8109929620		
expected date :-   11. March
[06/03/24, 12:51:04 PM] ~ Mahi: will come today 
mp nagar
[06/03/24, 1:10:47 PM] ~ Deepali coding: Branch :- CS
College:- JNCT
Name :- 	Deepesh 
Contact:- 	8640083505
expected date :-  20 March
[06/03/24, 1:21:28 PM] ~ Mahi: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal
.	MOHAMMAD ZIYA ANSARI
	7879859713
3rd year
will come 9 march
indrapuri
[06/03/24, 1:29:54 PM] ~ Mahi: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal.	
JYOTI GOSWAMI	
9340011154	
3rd year
	will come 10 march
mp nagar
[06/03/24, 2:03:27 PM] kasim k: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology & Science	
MAHIMA KAUSHIK	
9406927730	
8March⭐️
(chetak )
[06/03/24, 3:08:58 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology
HARSH MOURYA
7225902702	
11 March	
indrapuri 
2nd Year
[06/03/24, 3:18:03 PM] ~ Hafsa , Coding Thinker: Name of Student: Jay Gupta 
College name : LNCT
Contact no: 8962407471
Branch: AI/ML
Expected Date of Visit:  Will come after 15 Mar
[06/03/24, 3:21:44 PM] khushi e.c: ‎This message was deleted.
[06/03/24, 3:26:00 PM] khushi e.c: Branch :- Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:- 	Lakshmi Narain College of Technology & Science	 
Name :- ASHISH CHINCHE
Contact:-	9302178992	
Expected date :- 	after 11 March m m.p Naga
[06/03/24, 3:43:36 PM] anchal e.c: Information Technology	Bansal Institute of Science & Technology	
VAIBHAV YADAV	7049538376		
Will come
Indrapuri
[06/03/24, 4:07:09 PM] annu❤️: Will Come today indrapuri
[06/03/24, 4:12:58 PM] ~ Deepali coding: Come today with Nirmal Meena
[06/03/24, 4:26:20 PM] khushi e.c: With freind Sachin and Rohit
[06/03/24, 4:33:45 PM] ~ Chauhan Shilpa: Name of Student: SAMIM HUSAIN(Junaid Ahmed aur Sanjay Kumar)
College name : Radharaman Engineering College
Contact no: 9939833793
Branch: Computer Science & Engineering
Expected Date of Visit:  Will come after 12 March (mp nagar)
[06/03/24, 4:52:28 PM] ~ Chauhan Shilpa: Name of Student: ROHIT VERMA
College name : Radharaman Engineering College
Contact no: 7415709112
Branch: Computer Science & Engineering
Expected Date of Visit:  Will come after 15 March (mp nagar)
[06/03/24, 5:56:32 PM] anchal e.c: Manju- 9755948829
College   - IES 
Will come end of March
Shagun _ 9691895924
Will come after exam
Varun- 7440286718
College _ oriental
Will come 8 march 
Shivani - 9770848140
Will think
[06/03/24, 6:10:37 PM] annu❤️: Reference - Abhishek will come after 10 March
[06/03/24, 6:21:46 PM] khushi e.c: Branch ;-  Computer Science & Engineering-Cyber Security
College: 	Lakshmi Narain College of Technology & Science
Name :- 	SATYAM RAGHUWANSHI
Contact:- 	8989436912	
Expected date :- 	10  March
[06/03/24, 6:24:05 PM] ~ Mahi: Name Of student Abhishek Dhadak
7879885141
NRI College
 will think after 10 march
Indrapuri
[06/03/24, 6:38:18 PM] ~ Hafsa , Coding Thinker: Coming with Mehek Verma 
Chetak
[06/03/24, 7:28:07 PM] anchal e.c: B.Tech	Computer Science & Engineering	Bansal College of Engineering	
CHITRANSH MEHRA
	8085476434	
After 15 march
[06/03/24, 8:38:24 PM] khushi e.c: With bhavesh will come on  8 March
[07/03/24, 12:14:14 PM] anchal e.c: Sumit Mishra -89572 60953
With friend shivang,vaidanshi, vadshalya
Will come today
Indrapuri
[07/03/24, 12:35:36 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	JAVED ALAM		7763828695	come after holi
[07/03/24, 12:39:34 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	NRI Institute of Information Science & Technology	SONU KUMAR		7987386398	will come 20 march
[07/03/24, 12:50:59 PM] khushi e.c: Computer Science & Engineering
College:- 	Lakshmi Narain College of Technology Excellence
Name ;:- 	UTKARSH GAUTAM
Contact:- 	7310581526
Expected date:- 9 March indrapuri
[07/03/24, 12:57:32 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Trinity Institute of Technology & Research	
AMAN KUMAR PANIKA	9399862732	
	11 march fsd
 indrapuri
[07/03/24, 1:16:52 PM] khushi e.c: Branch :- Computer Science & Engineering-Data Science
College:- 	Lakshmi Narain College of Technology Excellence
Name. :- 	SATYAM JAISWAL	
Contact:- 7067180147		
Expected date :- ,9 March m.p nagar
[07/03/24, 1:32:31 PM] khushi e.c: Branch :- Computer Science & Engineering-Data Science	
College:- Lakshmi Narain College of Technology Excellence
Name :- 	KAPIL MEWADA	
Contact:- 6260068660
Expected date :- 		7march  m.p nagar
[07/03/24, 1:36:35 PM] ~ Mahi: NRI Institute of Research & Technology
	SAMEK WASNIK
	9691467967
will think after eid
[07/03/24, 1:43:07 PM] ~ Mahi: NRI Institute of Research & Technology
	SHIKHA BISEN
	9302835599
	will come 20 march
indrapuri
[07/03/24, 1:49:53 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology	
SUNNY KUMAR MAHATO	
8271068927	
In April 	Cc++ 
2nd Year
[07/03/24, 1:57:59 PM] anchal e.c: College -tit
CS 
name- 	rafik khan 	
8120165530		
	after 15 march
Mp nagar
[07/03/24, 2:05:09 PM] anchal e.c: pankaj kushwah 
	7223017603	
With friend Dharmendra Nikhil
Will come 11march
Indrapuri ‎<This message was edited>
[07/03/24, 2:57:48 PM] ~ Deepali coding: Name - Deepanshu
College - Bansal
Branch- cs
Number ‪ 7354988076
Come 7 feb chetak
[07/03/24, 2:58:39 PM] Neha mam e.c: Chalo tumne kuch Chetak ke liye to nikale
[07/03/24, 2:59:04 PM] ~ Deepali coding: Mam chetak pr kal bhi admission hua
[07/03/24, 2:59:09 PM] ~ Deepali coding: Kal bhi ek aa jayega
[07/03/24, 2:59:14 PM] ~ Deepali coding: Nikita bhi wahi Hui hai
[07/03/24, 2:59:17 PM] Neha mam e.c: Balram laya tha uska kya hua
[07/03/24, 2:59:59 PM] ~ Deepali coding: Mam Wednesday aayega Rahul admission ke liye
[07/03/24, 3:01:32 PM] Neha mam e.c: Kal ke baad new Fsd-B Tuesday, Thursday, Sunday ho jayega
[07/03/24, 3:01:59 PM] Neha mam e.c: Data science monday,Wednesday,Friday
[07/03/24, 3:02:18 PM] ~ Deepali coding: Oky mam
[07/03/24, 3:03:21 PM] Neha mam e.c: Kal par Friday rehagi phir Sunday
[07/03/24, 3:24:09 PM] ~ Deepali coding: Uske baat Tuesday shift ho jayega
[07/03/24, 3:25:52 PM] Neha mam e.c: Friday 
Sunday 
Tuesday 
Thursday 
Sunday 
/
/
/
[07/03/24, 3:25:58 PM] Neha mam e.c: Samajh aa gya
[07/03/24, 3:26:09 PM] ~ Deepali coding: Yes mam
[07/03/24, 3:27:10 PM] Neha mam e.c: Ok
[07/03/24, 3:27:24 PM] Neha mam e.c: Schedule bhej dete hai confuse nahi ho
[07/03/24, 3:28:23 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Trinity Institute of Technology & Research	
Name. :- RAJ KUMAR THAKUR	
Contact:; 9301985442	
Expected date :- 	will think m.p nagar
[07/03/24, 3:40:43 PM] annu❤️: Deepika 
9302331611
Will Come chetak
8 March
With vidhi
[07/03/24, 4:11:51 PM] ~ Deepali coding: Ye mene phale hi dal diya hai
[07/03/24, 4:12:58 PM] annu❤️: Wo already meri admission hai to dalne kaa mtlb ni
[07/03/24, 4:13:19 PM] ~ Deepali coding: But fsd ke liye mene phale pitch kiya
[07/03/24, 4:13:47 PM] annu❤️: Already baat hui hai usse jb admission hh aap claim ni kr skte plhe hi clear kr diya tha yeh aur
[07/03/24, 4:14:22 PM] ~ Deepali coding: Me to karugi kyoki mene pitch kiya hai
[07/03/24, 4:14:55 PM] annu❤️: Krte rho to jb wo admission hai to dekh lange ok
[07/03/24, 4:15:03 PM] ~ Deepali coding: Haa
[07/03/24, 4:15:27 PM] ~ Deepali coding: Karwa lo fr
[07/03/24, 4:18:18 PM] Neha mam e.c: Ladai nahi karni hai apan ko
[07/03/24, 4:18:29 PM] ~ Deepali coding: Yes mam
[07/03/24, 4:18:50 PM] Neha mam e.c: Group par behaas mat kiya karo
[07/03/24, 4:19:44 PM] Neha mam e.c: Dono kp sir ko aapni call list ur kaise kisne bulaya ye sab likhva do
[07/03/24, 4:20:31 PM] kp sir: Admission hojane dooo apan karlenge anushree ,Deepali verify 
Don't worry
[07/03/24, 4:20:56 PM] Neha mam e.c: Bacho jaise ladai nahi kiya karo
[07/03/24, 4:22:38 PM] anchal e.c: Branch _ cs
College _  sagar institute
Name _ lokesh
Number _62651 88482
Will come 25 March
Mp nagar
[07/03/24, 4:30:07 PM] ~ Chauhan Shilpa: Name of Student:-AMAN KHAN
College name :-Technocrat Institute of Technology
Contact no:-7839092040
Branch: Computer Science & Engineering
Expected Date of Visit:  after Ramzan
[07/03/24, 4:30:26 PM] ~ Hafsa , Coding Thinker: Name of Student:  Nitish Sonpure
College name: OIST
Contact no : 8120367785
Branch: CS/DS 
Expected Date of Visit : Will come in April
[07/03/24, 4:31:00 PM] khushi e.c: Will come after 13 March with freind Shivam and mukhtar
[07/03/24, 4:37:45 PM] kasim k: Name of Student:  Rupesh kumar
College name: jnct
Contact no : 7079500772
Branch: CS 
Expected Date of Visit : 15march ( chetak )
[07/03/24, 5:28:57 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Trinity Institute of Technology & Research	RAJ KUMAR THAKUR	
9301985442	
	will think
[07/03/24, 5:37:48 PM] kasim k: Name of Student:  Jahid alam
College name: All saints 
Contact no : 7033637235
Branch: CS 
Expected Date of Visit : after eid
[07/03/24, 5:44:50 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Trinity Institute of Technology & Research	
MOHIT RAGHUVANSHI	
8982565916	
	8,9 march 
 indrapuri
[07/03/24, 5:58:50 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrat Institute of Technology	
BIPESH KUMAR YADAV
8404822627	
In April 
2nd Year
[07/03/24, 5:59:56 PM] ~ Hafsa , Coding Thinker: Name of Student: Dhruv Rawat 
College name: OIST
Contact no : 9755442837
Branch: CS/AI/ML
Expected Date of Visit : 11  March
[07/03/24, 6:05:47 PM] khushi e.c: Branch :: Computer Science & Engineering
College:- 	Trinity Institute of Technology & Research	
Name :: SACHIN RAJBHAR	
Contact :- 8840339181		
Expected date :- 14 March Indra puri
[07/03/24, 6:06:47 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Trinity Institute of Technology & Research	
RAVI PRAKASH YADAV	9450637416	
	after holi 
indrapuri
[07/03/24, 6:21:37 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Trinity Institute of Technology & Research
	ROCHAK TIWARI	7987387001		
9,10 March 
Indrapuri
[07/03/24, 6:24:00 PM] annu❤️: B.Tech	
Computer Science & Engineering
Radharaman Engineering College	
PAWAN KUMAR SINGH
9334738080	
After Holi 	
2nd Year
[07/03/24, 6:28:45 PM] khushi e.c: Branch :-B.Tech	Computer Science & Engineering
College:- 	Vaishnavi Inst. of Tech. & Science	
Name :- SHUBHAM KOL
Contact:- 	8103401059		
Expected date:- after holi
[07/03/24, 6:34:21 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Radharaman Engineering College	
SHALWI KUMARI
6204842035	
After Holi 
2nd Year
[07/03/24, 6:56:25 PM] ~ Deepali coding: ‎This message was deleted.
[07/03/24, 7:01:38 PM] ~ Deepali coding: Will come 8 March 
Alok
Ruchi
Neha
[07/03/24, 7:12:53 PM] khushi e.c: Branch:: B.Tech	Computer Science & Engineering
College:- 	Vaishnavi Inst. of Tech. & Science
Name. :- 	PAYAL DARVEKAR
Contact:- 	9340602926		
Expected date 12  March
[07/03/24, 7:14:33 PM] kasim k: B.Tech	
Computer Science & Engineering-Cyber Security	
Lakshmi Narain College of Technology & Science	
ABHASH CHOUDHARY	
9039944958	
8March
[07/03/24, 7:14:57 PM] annu❤️: Will Come with adarsh 8 March indrapuri
[07/03/24, 7:23:57 PM] ~ Mahi: NRI Institute of Research & Technology
	ABHISHEK	
7987103310	
will come after holi
[07/03/24, 7:51:26 PM] ~ Chauhan Shilpa: Visit done
[07/03/24, 7:54:43 PM] ~ Chauhan Shilpa: Visit done
[07/03/24, 8:12:18 PM] ~ Chauhan Shilpa: Name of Student:-SURBHI DUBEY  and  Poornima
College name :-Technocrat Institute of Technology
Contact no:-9755357521
Branch: Computer Science & Engineering
Expected Date of Visit:  will come 18 March (mp nagar)
[07/03/24, 8:20:54 PM] ~ Chauhan Shilpa: Name of Student:-KRUTI LOKHANDE
College name :-Technocrat Institute of Technology
Contact no:-8871204905
Branch: Computer Science & Engineering
Expected Date of Visit:  will come 13 March
[07/03/24, 8:40:39 PM] ~ Chauhan Shilpa: Name of Student:-SATYAM BISEN
College name :-Technocrat Institute of Technology
Contact no:-7879227241
Branch: Computer Science & Engineering
Expected Date of Visit:  will come 20 March (mp nagar)
[08/03/24, 12:34:59 PM] Harsh sir tl: Visit done
[08/03/24, 12:36:42 PM] Harsh sir tl: Visit done admitted in our institute
[08/03/24, 12:38:01 PM] Harsh sir tl: Hafsa :- Rameshwar 9369311782 
admission done
[08/03/24, 12:38:38 PM] Harsh sir tl: Anuj visited
[08/03/24, 12:39:35 PM] Harsh sir tl: Visit done
[08/03/24, 12:42:38 PM] kasim k: @918085394718
[08/03/24, 12:43:18 PM] Harsh sir tl: Visit done with rohit 
@916267544143
[08/03/24, 12:43:27 PM] Harsh sir tl: Chetan visit done @916263551348
[08/03/24, 12:46:02 PM] Harsh sir tl: Visit done
[08/03/24, 12:46:37 PM] Harsh sir tl: Visit done
[08/03/24, 12:51:57 PM] Harsh sir tl: Visit done with astitva shrivastava
[08/03/24, 12:53:22 PM] Harsh sir tl: Visit done will be counted as direct
[08/03/24, 12:53:47 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Radharaman Engineering College	
PRINCE KUMAR
9798250567	
After Holi 
2nd Year
[08/03/24, 12:55:06 PM] Harsh sir tl: Visit done
[08/03/24, 12:56:55 PM] ~ Deepali coding: @918085394718
[08/03/24, 12:57:01 PM] Harsh sir tl: Visit done
[08/03/24, 12:57:32 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Bansal College of Engineering
Name :- 	ROHIT PATEL
Contact:- 	7999850515	
Expected date:- 13 March indrapuri
[08/03/24, 12:59:31 PM] Harsh sir tl: Visit done
[08/03/24, 1:00:02 PM] Harsh sir tl: Visit done
[08/03/24, 1:00:26 PM] Harsh sir tl: Visit done
[08/03/24, 1:00:28 PM] khushi e.c: Name:- Ritivik Kumar 
Contact :- 8409275326
College:- sirt 
Branch :- CSE 
Year 2nd
[08/03/24, 1:00:53 PM] Harsh sir tl: Visit done
[08/03/24, 1:01:54 PM] Harsh sir tl: Visit done admission done
[08/03/24, 1:02:35 PM] Harsh sir tl: Visit done
[08/03/24, 1:03:34 PM] Harsh sir tl: Visit done
[08/03/24, 1:05:20 PM] Harsh sir tl: Visit done
[08/03/24, 1:06:10 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Lakshmi Narain College of Technology Excellence
	RAJ CHAWDA	
6264039327	
	9 march will come
 indrapuri
[08/03/24, 1:07:23 PM] Harsh sir tl: Visit done
[08/03/24, 1:08:28 PM] Harsh sir tl: Visit done
[08/03/24, 1:10:26 PM] Harsh sir tl: Visit done with parth gupta
[08/03/24, 1:11:20 PM] ~ Mahi: NRI Institute of Research & Technology
	SURAJ KOURAV
	8103615599
	will think arpil 1st week
[08/03/24, 1:11:44 PM] Harsh sir tl: Visit done
[08/03/24, 1:15:03 PM] Harsh sir tl: Visit done admission done
[08/03/24, 1:15:57 PM] Neha mam e.c: Inn sabke admission ho gye
[08/03/24, 1:17:12 PM] Harsh sir tl: 3 admission 
Paras trivedi 
Prathvi singh 
Adish jain
[08/03/24, 1:18:04 PM] Harsh sir tl: Visit done
[08/03/24, 1:19:14 PM] annu❤️: B.Tech	
Computer Science & Engineering
Radharaman Engineering College	
ROHIT KUMAR
7368830842	
After Holi 
Will Come for admission
2nd Year
[08/03/24, 1:19:28 PM] ~ Chauhan Shilpa: Mam abhi 3 huye hai or ane Wale h
[08/03/24, 1:20:10 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Lakshmi Narain College of Technology Excellence	
MOHAMMED ABDUL AZEEZ
	9301233280		will think 
 indrapuri
[08/03/24, 1:20:39 PM] Harsh sir tl: Visit done 1 admission 
Vaidik
[08/03/24, 1:21:15 PM] Harsh sir tl: Visit done
[08/03/24, 1:26:35 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Radharaman Engineering College	
ASHUTOSH
9752854706	
20 March	Indrapuri 
2nd Year
[08/03/24, 1:38:12 PM] khushi e.c: Branch :- Civil Engineering
College:- 	Bansal College of Engineering
Name :- 	SUMESH	
Contact:- 8815858478		
Expected date:- 	will come 13 March  m.p nagar
[08/03/24, 1:51:09 PM] ~ Deepali coding: @918085394718
[08/03/24, 1:51:15 PM] Harsh sir tl: Visit done
[08/03/24, 1:52:20 PM] ~ Deepali coding: @918085394718
[08/03/24, 1:52:24 PM] Harsh sir tl: Visit done
[08/03/24, 1:53:51 PM] ~ Deepali coding: @918085394718
[08/03/24, 1:54:06 PM] Harsh sir tl: Visit done
[08/03/24, 1:57:16 PM] ~ Deepali coding: @918085394718
[08/03/24, 1:57:25 PM] Harsh sir tl: Visit done
[08/03/24, 1:58:06 PM] ~ Deepali coding: @918085394718
[08/03/24, 1:58:12 PM] Harsh sir tl: Visit done
[08/03/24, 2:00:30 PM] ~ Deepali coding: @918085394718
[08/03/24, 2:00:35 PM] Harsh sir tl: Joined
[08/03/24, 2:01:15 PM] ~ Deepali coding: @918085394718
[08/03/24, 2:01:37 PM] Harsh sir tl: Only lav kumar visited
[08/03/24, 2:02:10 PM] ~ Deepali coding: @918085394718
[08/03/24, 2:02:23 PM] Harsh sir tl: Joined
[08/03/24, 2:02:50 PM] ~ Deepali coding: @918085394718
[08/03/24, 2:02:58 PM] Harsh sir tl: Visit done
[08/03/24, 2:05:13 PM] Harsh sir tl: Joined
[08/03/24, 2:05:42 PM] ~ Deepali coding: @918085394718
[08/03/24, 2:06:00 PM] Harsh sir tl: Joined
[08/03/24, 2:08:14 PM] Harsh sir tl: Visit done
[08/03/24, 2:09:04 PM] ~ Deepali coding: @918085394718
[08/03/24, 2:09:11 PM] Harsh sir tl: Visit done
[08/03/24, 2:10:27 PM] Harsh sir tl: Visit done
[08/03/24, 2:10:51 PM] Harsh sir tl: Visit done
[08/03/24, 2:11:52 PM] Harsh sir tl: Visit done
[08/03/24, 2:13:08 PM] Harsh sir tl: Joined
[08/03/24, 3:29:25 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Trinity Institute of Technology & Research	
Name :- PALLAVI RANA
Contact:- 	7909919120		
Expected date:- 17  March Indrapuri
[08/03/24, 3:32:51 PM] anchal e.c: Ye mera pehele hi prospect dala h
[08/03/24, 3:41:59 PM] kp sir: Haan data same hogya 
Harsh sir dekhloo data lunch ke baad
[08/03/24, 3:54:45 PM] Harsh sir tl: 2-4 repeat the bss
[08/03/24, 3:54:49 PM] Harsh sir tl: Krdiya h sort
[08/03/24, 4:06:07 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Technocrats Institute of Technology [Excellence]	
HARSHJEET PARIHAR
	7415615455	
9 March with friend Khushi 
 mp nagar
[08/03/24, 5:06:00 PM] khushi e.c: Branch :- B.Tech	Artificial Intelligence and Data Science	
College:- Corporate Institute of Science & Technology	
Name :& SAQUIB KHAN
Contact:- 	7587929124		
Expected date:- 15 march
[08/03/24, 5:07:50 PM] Harsh sir tl: Visit done
[08/03/24, 5:09:03 PM] Harsh sir tl: Visit done
[08/03/24, 5:09:22 PM] Harsh sir tl: Visit done
[08/03/24, 5:21:16 PM] khushi e.c: Branch :- B.Tech	Artificial Intelligence and Data Science	
College:- Corporate Institute of Science & Technology	
Name ;:- AYUSH SAHU	
Contact :- 9039844419		
Expected date:- 16  March
[08/03/24, 5:42:19 PM] khushi e.c: Branch ::- Computer Science & Bussiness System
College:- 	IES College of Technology
Name. ;- 	RAHUL KUMAR
Contact:- 	9135342494	
Expected date :: 	18march  m.p nagar
[08/03/24, 6:16:47 PM] khushi e.c: Branch ;- Computer Science & Engineering-Artificial Intelligence and Machine Learning
College:- 	IES College of Technology
Name :- 	MANIDHAR YADAV
Contact:- 	9031239709		
Expected date:- 13 March m.p nagar
[08/03/24, 6:39:55 PM] ~ Mahi: NRI Institute of Research & Technology
	ARADHANA VERMA
	7804827939	
will think april
[08/03/24, 6:41:32 PM] kasim k: B.Tech	Computer Science & Engineering	
Bansal Institute of Science & Technology	
NEELESH PATEL	
7724072662	
will think 11 march
[08/03/24, 6:42:02 PM] kasim k: B.Tech	Computer Science & Engineering	
Bansal Institute of Science & Technology	
FATEH BAHADUR SINGH	
7024795674	
9march ⭐️(chetak)
[08/03/24, 6:58:16 PM] ~ Deepali coding: Name Amit kumar
Number ‪ 97526 50652‬
College Lnct
Year 2 nd 
Will come 15 march
[09/03/24, 9:34:04 AM] ~ Deepali coding: Will come tomorrow for registration ( Sangeet )
[09/03/24, 12:13:46 PM] khushi e.c: B.Tech	Computer Science & Engineering-Data Science	IES College of Technology	HIMANSHU KUMAR GIRI	9113704308		ds   m.p nagar   11 March
[09/03/24, 12:49:33 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Vaishnavi Inst. of Tech. & Science
Name :- 	SHUBHAM PANCHE
Contact;:- 	9981783350	
Expected date :-  	will come after holi
[09/03/24, 12:51:26 PM] ~ Deepali coding: 2ND	Computer Science & Engineering	Bhopal Institute of Technology, Bangrasia	RAVISHANKAR BISEN	8224095351	 	will come April
[09/03/24, 1:12:48 PM] khushi e.c: Branch :-  Artificial Intelligence and Data Science
College:- Corporate Institute of Science & Technology
Name :- 	ABHAY PATEL
Contact:-	9713804316	. expected date 	5 April m.p nagar
[09/03/24, 1:19:07 PM] anchal e.c: Syed sharik raza - 7992406408
Will come 9,10 March
Indrapuri
[09/03/24, 1:30:29 PM] anchal e.c: Shubham
9174317328
Will think
Indrapuri
[09/03/24, 1:52:47 PM] khushi e.c: Branch :- Computer Science & Engineering-Cyber Security
College:- 	IES College of Technology	
Name. :- HIMANI
Contact:- 	7024890197		
Expected date:- will think m.p.nagar
[09/03/24, 1:56:06 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Radharaman Engineering College	
KUNDAN KUMAR YADAV	
8252176135	
Will think 
2nd Year
[09/03/24, 2:59:35 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Radharaman Engineering College	
MAYANK SEN
7999693203	
26 March
2nd Year
[09/03/24, 3:02:54 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal Institute of Science & Technology	
ASHOK RAJAK	
9171134634	
will think 12
[09/03/24, 3:03:21 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal Institute of Science & Technology	
ROHIT KURMI	
8305457553	
12 March
[09/03/24, 3:04:00 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal Institute of Science & Technology	
SURYANSH PORANIK	
8982660651	
will think enroll in sharma
[09/03/24, 3:08:53 PM] Neha mam e.c: To aapne paas kyun likha hai
[09/03/24, 3:09:25 PM] kasim k: wha se c,c++ kr raha hai mam isliye  is mnth course complete ho jyega  tau askte haiiu
[09/03/24, 3:15:19 PM] ~ Mahi: NRI Institute of Research & Technology
	SUMIT CHOUHAN
	7489169006	
will think after holi with frind sourab
[09/03/24, 3:24:33 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Bansal Institute of Research, Technology & Science	AKASH KUMAR SINGH		8602548159	will come 10 march chetak
[09/03/24, 3:46:54 PM] kp sir: Already visited
[09/03/24, 3:47:05 PM] kp sir: Already visited
[09/03/24, 3:53:56 PM] ~ Hafsa , Coding Thinker: Name of Student: Jagdeesh Malviya 
College name: Trinity 
Contact no : 8878691622
Branch: CS
Expected Date of Visit : Will contact in April
[09/03/24, 3:56:16 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering-Data Science	
College:- IES College of Technology	
Branch :- ABHAY KUMAR
Contact:- 	9142590077
Expected date :- 	after holi
[09/03/24, 4:02:05 PM] ~ Mahi: IES College of Technology	
DIPESH KUMAR MISHRA
	7481000910	
will come 10 march
chetak
[09/03/24, 4:09:19 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal Institute of Science & Technology	
RITESH KUMAR SHAH	6268031098	
17March
[09/03/24, 4:41:00 PM] Harsh sir tl: @919244985834 aapne aaj off liya tha na ?
[09/03/24, 4:41:27 PM] ~ Mahi: no sir
[09/03/24, 4:42:09 PM] Harsh sir tl: Kitne baje aaye aap?
[09/03/24, 4:42:20 PM] ~ Mahi: 2.30 pm
[09/03/24, 4:42:29 PM] ~ Mahi: half day  me
[09/03/24, 4:42:49 PM] Harsh sir tl: Mene half day mana kiya tha full off count krunga m isko
[09/03/24, 4:45:23 PM] ~ Mahi: and agr kisi ko half ka kam ho to sir urgent me to kya kre..
[09/03/24, 4:45:49 PM] Harsh sir tl: No more discussion mene aapko full day off boldiya tha
[09/03/24, 5:01:30 PM] ~ Chauhan Shilpa: Name of Student: VISHAL PAWAR (Aniket Aman Anuj)
College name: Technocrat Institute of Technology
Contact no : 
Branch: Computer Science & Engineering9340865298
Expected Date of Visit : Will last March
[09/03/24, 5:19:27 PM] ~ Hafsa , Coding Thinker: Will come on 10 March with Shubham and Uday
[09/03/24, 5:20:24 PM] kasim k: Computer Science & Engineering	
J.N. College of Technology	
DIVYANSH VISHWAKARMA	
9399696544
12 march
[09/03/24, 5:34:47 PM] khushi e.c: ‎This message was deleted.
[09/03/24, 5:36:10 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:- 	Mittal Institute of Technology	
Name :- REHNUMA KHAN	
Contact:-9302534789	
Expected date 	 after holi
[09/03/24, 5:57:43 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Bansal Institute of Research & Technology
	VIKASH SINGH
	9109464860
	13 march 
indrapuri
[09/03/24, 6:02:55 PM] ~ Mahi: IES College of Technology	
SUNNY SINGH
	6202120109	
will come 10 march
chetak
[09/03/24, 6:13:35 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Bansal Institute of Research & Technology	
OM KUMAR BEN
	9340774207
	not confirm date to visit 
Indrapuri
[09/03/24, 6:14:21 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:: Mittal Institute of Technology
Name. ::  ;- 	VIKASH GOUR
Contact:- 	6260409950		
Expected date:- 13 March  m.p nagar
[09/03/24, 6:30:20 PM] kasim k: B.Tech	Computer Science & Engineering	
Bansal Institute of Science & Technology	
SONU JATAV	
7247351564	
10march  
 with ajay chaudhary
[09/03/24, 6:31:31 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering
College:: 	Mittal Institute of Technology
Name. :- 	NITIN THAKUR	
Contact:- 9770477745	
Expected date :- 	  19 March
[09/03/24, 6:40:17 PM] ~ Hafsa , Coding Thinker: Name of Student: Vishnu Sharma 
College name: IES
Contact no : 8435831380
Branch: CS/DS
Expected Date of Visit : 10 March
[09/03/24, 6:45:51 PM] ~ Hafsa , Coding Thinker: Harsh Sir mera data phir same ho gya Arpana se
[09/03/24, 6:52:21 PM] khushi e.c: Branch :- Computer Science & Engineering	
Branch :- Mittal Institute of Technology
Name :- 	ABHISHEK TIWARI
Contact:- 	9981451050
Expected date :- 		12 march indrapuri ‎<This message was edited>
[09/03/24, 6:53:01 PM] annu❤️: B.Tech
Information Technology
Bansal Institute of Science & Technology
PRAPTI AHIRWAR
8962681217	
13 March	indrapuri 
2nd Year
[09/03/24, 7:06:22 PM] kasim k: B.Tech	
Computer Science & Engineering	
J.N. College of Technology	SAKSHI GUPTA	
7566129869	
 + shidhant
 16march
[09/03/24, 7:13:47 PM] annu❤️: B.Tech	
Information Technology
Bansal Institute of Science & Technology
PALLAVI PATEL
8602814590	
11 March	
Indrapuri 
2nd Year
[09/03/24, 8:30:41 PM] Neha mam e.c: Already visited 26 jan
[09/03/24, 8:33:28 PM] Neha mam e.c: Already visited on 26/jan
[10/03/24, 12:00:43 PM] ~ Mahi: will come today with frind preety 
chetak
[10/03/24, 12:06:03 PM] ~ Mahi: Computer Science & Engineering-Artificial Intelligence and Machine Learning	IES College of Technology
	AMAAD MALIK
	9015035357
	will think after eid
[10/03/24, 12:33:01 PM] ~ Hafsa , Coding Thinker: Name of Student: Rishi Vaidya
College name: IES
Contact no : 8871652941
Branch: CS/Cyber Security 
Expected Date of Visit : 11 March ( Indrapuri )
[10/03/24, 12:39:09 PM] khushi e.c: Branch :-  Computer Science & Engineering
College:- Oriental Institute of Science & Technology
Name :- 	YASHWINEE BISEN
Contact:- 	8319266401		
Expected date::   after 15 March
[10/03/24, 1:00:15 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal Institute of Research & Technology	
DEEPAK AHIRWAR	7697406730	
will think 
indrapuri
[10/03/24, 1:15:10 PM] annu❤️: B.Tech	
Artificial Intelligence and Data Science	Lakshmi Narain College of Technology	
ESHITA PANDIT
9630196011	
11 March	Chetak 
2nd Year
[10/03/24, 1:38:07 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal Institute of Research & Technology	
PRINCE CHOURASIYA	
9399305971
	20 March 
will come indrapuri
[10/03/24, 1:39:23 PM] kasim k: B.Tech	
Computer Science & Engineering	
J.N. College of Technology	
HARIRAM PRAJAPATI	
8305156359	
12March (indrpuri)
[10/03/24, 1:50:32 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Bansal Institute of Research & Technology	
ATUL SANODIYA
	7000802383	
13 march
 mp nagar
[10/03/24, 1:50:37 PM] ~ Hafsa , Coding Thinker: Name of Student: Abhishek Kumar
College name: IES
Contact no : 6206032280
Branch: CS/Cyber Security 
Expected Date of Visit : Will come after Holi
[10/03/24, 2:27:19 PM] kasim k: B.Tech	
Electronics & Communication Engineering	
J.N. College of Technology	ANJALI CHOUHAN	
8103106835	
17 March
[10/03/24, 2:58:53 PM] khushi e.c: Branch Computer Science & Engineering	
College:- Mittal Institute of Technology
Name ;- 	PRIYA THAKUR
Contact:- 	7489243934		
Expected date:- after holi  m.p Nagae
[10/03/24, 3:00:26 PM] khushi e.c: Name :- Computer Science & Engineering	
College:- Mittal Institute of Technology
Branch :- 	NISHANT SAHU
Contact:- 	7771881962	
Expected date :- 	13march indrapuri
[10/03/24, 3:02:08 PM] khushi e.c: Computer Science & Engineering	Mittal Institute of Technology	MANOJ	8171229652		12 march  m.p nagar   fsd
[10/03/24, 3:04:44 PM] ~ Mahi: ‎This message was deleted.
[10/03/24, 3:05:07 PM] ~ Mahi: will come today chetak
[10/03/24, 3:06:04 PM] ~ Mahi: will come today 
indrapuri
[10/03/24, 3:18:51 PM] ~ Mahi: IES College of Technology	
RAMAN KUMAR	7781840542	
will come  13 march
chetak
[10/03/24, 3:24:12 PM] ~ Hafsa , Coding Thinker: Will come today Chetak with Alka Mandal
[10/03/24, 3:25:42 PM] khushi e.c: Branch:- Computer Science & Engineering	
College:- Mittal Institute of Technology
Name :- 	RITIK RATHORE
Contact:- 	6266439696		
Expected date:- 13 March   m.p nagar
[10/03/24, 3:58:06 PM] anchal e.c: ‎This message was deleted.
[10/03/24, 3:58:36 PM] ~ Deepali coding: Will come today indrapuri with Roushan
[10/03/24, 4:00:25 PM] ~ Mahi: IES College of Technology
	ANKIT KUMAR	7209645255	
will come arpril 5
chetak
[10/03/24, 4:08:59 PM] anchal e.c: Will come today indrapuri
[10/03/24, 5:37:50 PM] kasim k: ‎You deleted this message.
[10/03/24, 5:38:02 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
J.N. College of Technology	
PRAVESH AHIRWAR	
6263297473	
12 march will think
[10/03/24, 5:41:47 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
J.N. College of Technology	
RAJ KUMAR SINGH	
7061388078	
13march indrpuri
[10/03/24, 6:04:08 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
J.N. College of Technology	
SHASHANK KUMAR NAMDEO
9981325976	
13march chetak
[10/03/24, 6:17:51 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
J.N. College of Technology	
PARV BALDUA	
7470825895	
16March
[10/03/24, 6:34:00 PM] khushi e.c: Branch :- Computer Science & Engineering	
College:- Mittal Institute of Technology
Name. ;:- 	ROHIT PACHLANIYA with friends shami , darshan, Ali 
Contact:- 	7047700844	
Expected:- 	 15 march indrapuri
[10/03/24, 6:39:31 PM] annu❤️: B.Tech	
Computer Science & Engineering-Internet of Things and Cyber Security Including Block Chain Technology
Lakshmi Narain College of Technology	
SHIVAM KUMAR
7728081784	
11 March	
Indrapuri 
2nd Year
[10/03/24, 6:46:27 PM] annu❤️: B.Tech	
Computer Science & Engineering-Internet of Things and Cyber Security Including Block Chain Technology
Lakshmi Narain College of Technology	
VISHAL DANGI
9589344506	
Will think 
2nd Year
[10/03/24, 6:48:46 PM] khushi e.c: Branch :- Computer Science & Engineering
College:- 	Mittal Institute of Technology
Name :- 	GAURAV SINGH
Contact :- 	6388583992		
Expected date :- after April
[10/03/24, 6:59:25 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal Institute of Research & Technology
	AKHILESH TIWARI	
9179892381	
12,13, march fsd ⭐
mp nagar
[10/03/24, 7:14:53 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal Institute of Research & Technology	
RAMPAL LODHI
	9754506577	
will think 
indrapuri
[10/03/24, 7:21:57 PM] kasim k: B.Tech	
Artificial Intelligence and Data Science	
J.N. College of Technology	
RIYA SONARE	
8827273500	
 23march
[10/03/24, 7:22:39 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal Institute of Research & Technology	
KULDEEP SINGH
	8103035397	
will think
[10/03/24, 7:22:48 PM] annu❤️: B.Tech	
Artificial Intelligence and Data Science	
Lakshmi Narain College of Technology	
UTKARSH KUSHWAHA
7415958370	
20 March
2nd Year
[10/03/24, 8:36:20 PM] ~ Chauhan Shilpa: Name of Student: GUNJAN RAVINDRA WADASKAR
College name: Technocrat Institute of Technology
Contact no : 9301812318
Branch: Computer Science & Engineering
Expected Date of Visit : Will come 15 march
[11/03/24, 12:14:25 PM] ~ Hafsa , Coding Thinker: Name of Student: Sadhana Jatav
College name: VNS
Contact no : 6264054551
Branch: CS
Expected Date of Visit : Will come in April
[11/03/24, 1:13:37 PM] ~ Deepali coding: B.Tech	Computer Science & Engineering	Bansal Institute of Research, Technology & Science	KARAN MALVIYA		9301652288	will come march end
[11/03/24, 1:32:46 PM] ~ Hafsa , Coding Thinker: Name of Student: Patle Shubham Chainlal
College name: VNS
Contact no : 8849897587
Branch: CS
Expected Date of Visit : Will come after Holi
[11/03/24, 3:05:00 PM] Neha mam e.c: @918085394718 data time par diya karo caller faltu time pass karte rehate hai
[11/03/24, 3:11:57 PM] ~ Mahi: NRI Institute of Research & Technology
	SANJEEV BANSHI
	8818982170	
	will think
[11/03/24, 3:33:45 PM] ~ Mahi: NRI Institute of Research & Technology
	SHITESVARI DHURWE
	6260799149	
	will come after holi
[11/03/24, 4:13:19 PM] annu❤️: B.Tech	
Artificial Intelligence and Data Science	
Lakshmi Narain College of Technology	
AKSHITA GUPTA
7879784375	
1 April
2nd Year
[11/03/24, 4:21:07 PM] annu❤️: B.Tech	
Computer Science & Engineering-Internet of Things and Cyber Security Including Block Chain Technology
Lakshmi Narain College of Technology	
AYUSH PATEL
6232872550	
Will think 
2nd Year
[11/03/24, 5:25:25 PM] ~ Hafsa , Coding Thinker: Name of Student: Sheikh Kaifuddin
College name: SIRT 
Contact no : 7024651116
Branch: CS
Expected Date of Visit : Will come after Eid
[11/03/24, 5:31:24 PM] ~ Mahi: Bansal Institute of Science & Technology
	ANUJ KUMAR
	6204659969	
will come after 20 march
chetak
[11/03/24, 5:31:37 PM] Harsh sir tl: Mam sbke pass allotted hai already
[11/03/24, 5:36:03 PM] anchal e.c: College - LNCT
Name - Yash Meena
Will come 12 march
Mp nagar
[11/03/24, 5:41:05 PM] ~ Mahi: Bansal Institute of Science & Technology
	ABHISHEK PATEl
	8815582576	
will come 15 march
[11/03/24, 6:00:07 PM] annu❤️: Will Come with Vijendra and Vivek today
[11/03/24, 6:29:30 PM] annu❤️: B.Tech	
Artificial Intelligence and Data Science	
Lakshmi Narain College of Technology
MEGHENDRA SINGH THAKUR	
7509122323	
29 March	Indrapuri 
2nd Year
[11/03/24, 6:52:46 PM] anchal e.c: Will come today indrapuri
[11/03/24, 7:04:26 PM] ~ Hafsa , Coding Thinker: Name of Student: Roshan Rajput 
College name: SIRTE
Contact no : 7610533820
Branch: CS
Expected Date of Visit : Will come in April
[11/03/24, 7:22:10 PM] anchal e.c: With friend samarjeet
[11/03/24, 7:56:02 PM] ~ Hafsa , Coding Thinker: Going Indrapuri with Sachin
[12/03/24, 12:39:36 PM] ~ Chauhan Shilpa: Name of Student: Tushar Singh, 
College name: Oriental
Contact no : 7080080229
Branch: cs
Year:- 2 nd (cs)
Expected Date of Visit :  will come today
[12/03/24, 1:13:20 PM] ~ Mahi: Lakshmi Narain College of Technology	
MADHUR SAHU
	8085499460	
will come 15 march
indrapuri ‎<This message was edited>
[12/03/24, 1:31:42 PM] ~ Hafsa , Coding Thinker: Name of Student: Ritesh Kumar 
College name: TIT
Contact no : 9453990076
Branch: CS
Expected Date of Visit : 14 March
[12/03/24, 1:52:05 PM] ~ Deepali coding: Name Yash jain
College soit rgpv 
Branch cs
Number ‪62673 08824‬
Visit date 13 March chetak( reference by yugal)
[12/03/24, 1:52:35 PM] Neha mam e.c: Yugal aapka prospect hai kya
[12/03/24, 1:52:42 PM] ~ Deepali coding: Yes mam
[12/03/24, 1:52:49 PM] Neha mam e.c: Kaise
[12/03/24, 1:53:03 PM] Neha mam e.c: Soit ka to data hi nahi hai mere pass
[12/03/24, 1:53:06 PM] ~ Deepali coding: Reference Mila tha mam group me 21 feb se hi dala hai mene
[12/03/24, 1:53:29 PM] Neha mam e.c: Kisse se reference milla tha
[12/03/24, 1:53:44 PM] Neha mam e.c: Yugal ka kisse reference milla tha
[12/03/24, 1:56:02 PM] ~ Deepali coding: ‎This message was deleted.
[12/03/24, 1:56:31 PM] Neha mam e.c: Kya dekhu isko
[12/03/24, 1:56:57 PM] ~ Deepali coding: Ye dala hai mam 21 ko
‎[12/03/24, 2:17:34 PM] Neha mam e.c: IMG_6483.MP4 ‎document omitted
‎[12/03/24, 2:21:47 PM] Neha mam e.c: IMG_6484.MP4 ‎document omitted
[12/03/24, 2:21:54 PM] Neha mam e.c: Ye post karna
[12/03/24, 2:32:08 PM] kasim k: Name of Student: abhishek lodhi
College name: lnct
Contact no : 09074613383
Branch: cs
Expected Date of Visit :  13march chetak
+ priyanka
[12/03/24, 2:33:46 PM] Neha mam e.c: Set on your status
[12/03/24, 2:52:24 PM] kp sir: Chetak aur MP nagar
[12/03/24, 3:09:32 PM] ~ Deepali coding: Mp nagar nhi sir indrapuri
[12/03/24, 3:09:38 PM] ~ Deepali coding: Aayenge
[12/03/24, 3:09:58 PM] ~ Deepali coding: Already visited hai
[12/03/24, 3:13:12 PM] kp sir: Kon se course main aarahe hain registration ke liye
[12/03/24, 3:13:56 PM] kp sir: 4PM PAR FSD KA BACKUP RAKHAA HSI AAJ ,FSD MAIN HAIN KYA
[12/03/24, 3:44:48 PM] ~ Hafsa , Coding Thinker: Name of Student: Utsav Shukla
College name: LNCT
Contact no : 7509847122
Branch: CS
Expected Date of Visit : Come after 20 March
[12/03/24, 3:45:29 PM] ~ Hafsa , Coding Thinker: Will come in April
[12/03/24, 4:05:09 PM] ~ Hafsa , Coding Thinker: Will come with Muskan Chourasia
[12/03/24, 4:27:57 PM] ~ Chauhan Shilpa: With Shikhar Gupta
[12/03/24, 4:37:53 PM] ~ Mahi: will come today inderpuri
[12/03/24, 5:49:52 PM] ~ Hafsa , Coding Thinker: Name of Student: Saurabh Sharma
College name: NRI
Contact no : 6263876668
Branch: CS
Expected Date of Visit : Come after Holi
[12/03/24, 6:00:19 PM] anchal e.c: Computer Science & Engineering-Data Science
	IES College of Technology	
RAHUL KUMAR YADAV	
9031798745		
	April
[12/03/24, 6:17:40 PM] ~ Mahi: Trinity Institute of Technology & Research
	RAHUL BANKER
	8878082371	
will come 13 march
with frind Ritesh,and Harsh
Indrapuri
[12/03/24, 6:32:07 PM] ~ Mahi: Trinity Institute of Technology & Research
	VISHAL SAINI
	8305726934	
	will come 17 mrch
indrapuri
[12/03/24, 6:59:15 PM] anchal e.c: Information Technology	Oriental Institute of Science & Technology
	SAKSHI WANI	
8982200566	
Will think 
 indrapuri
[12/03/24, 7:45:08 PM] ~ Chauhan Shilpa: Name of Student: Manish 
College name: lnct
Contact no : 6204668118
Expected Date of Visit :  will come 13 March
[13/03/24, 1:01:36 PM] Harsh sir tl: Subha se ekk bhi prospects nai bane kisi ke bhii
[13/03/24, 1:02:53 PM] Harsh sir tl: Msgs krrahe ho team apne prospects ko ??
[13/03/24, 1:04:44 PM] anchal e.c: Yes sir
[13/03/24, 1:13:22 PM] ~ Mahi: yes
[13/03/24, 1:13:36 PM] ~ Mahi: calls to ni  uth rhe to msg kr rhe h
[13/03/24, 1:14:07 PM] khushi e.c: Yes sir
[13/03/24, 1:35:17 PM] ~ Mahi: Oriental Institute of Science & Technology
	JAYESH VIJAY VARGIAYA	
8305661178	
3rd year
	will come 17 march
chetak ‎<This message was edited>
[13/03/24, 1:57:31 PM] khushi e.c: Branch :- Computer Science & Engineering
College:-	Bhopal Institute of Technology & Science, Bangrasia
Name :- 	MAYANK SINGH
Contact:- 	9754792944	
Year:- 3rd
Expected date:- will think after holi indore
[13/03/24, 2:03:25 PM] ~ Mahi: Technocrats Institute of Technology & Science
	RATNESH KUMAR PATEL
	9752390331	
3rd year
will come  13 march
 chetak
[13/03/24, 3:20:07 PM] ~ Chauhan Shilpa: Name of Student:-VIVEK GIRHARE
College name: Oriental College of Technology
Contact no :-8269469429
Branch:-Information Technology
Expected Date of Visit :  will come 29 March
[13/03/24, 3:31:57 PM] ~ Chauhan Shilpa: Name of Student:-MD NASAR ALAM
College name: Slagar Institute of Research & Technology Excellence
Contact no 6202870354
Branch:-Computer Science & Engineering
Expected Date of Visit :  after Ramzan
[13/03/24, 3:44:00 PM] ~ Deepali coding: Computer Science & Engineering	Oriental Institute of Science & Technology	AYUSH MISHRA		7773013059	will come 14 March indrapuri
[13/03/24, 3:58:15 PM] khushi e.c: Branch :- Artificial Intelligence and Data Science
College:- 	Corporate Institute of Science & Technology	
Name :- BHARTI WAGDRE	
Contact:- 7970115030	 
Expected date:-  	after holi m p nagar
[13/03/24, 5:12:21 PM] ~ Mahi: NRI Institute of Information Science & Technology	
ASHISH AHIRWAR	7000031178	
will come 17 march
[13/03/24, 5:21:16 PM] ~ Chauhan Shilpa: Name of Student:-AYUSHI SARATHEY
College name: Slagar Institute of Research & Technology Excellence
Contact no:-9109270562
Branch:-Computer Science & Engineering
Expected Date of Visit :  will come 15 march
[13/03/24, 5:21:42 PM] Harsh sir tl: @916260034224 @919424704675 @916263594069 aaj jo highlighted data allot kiya hai kindly make sure you work on that
[13/03/24, 5:22:12 PM] ~ Mahi: yes sir
[13/03/24, 5:22:43 PM] ~ Deepali coding: Yes sir
[13/03/24, 5:29:26 PM] ~ Mahi: NRI Institute of Information Science & Technology	
SURAJ KUMAR KEWAT
	7974479337	
will come march end
[13/03/24, 5:32:12 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Lakshmi Narain College of Technology Excellence
	KAJAL MEENA	
9479796726	
will think
[13/03/24, 5:32:28 PM] anchal e.c: Yes sir
[13/03/24, 5:32:52 PM] Neha mam e.c: Aaj kal koi prospect ban nahi rahe hai team
[13/03/24, 5:33:17 PM] Neha mam e.c: Aise sote sote kaam karonge to kaise chalega
[13/03/24, 5:33:36 PM] Neha mam e.c: Samajh hi nahi aa raha aap lo ka kaam
[13/03/24, 5:38:35 PM] ~ Mahi: will come 17 march with frinds amit, anurag and  vishal 
inderpuri
[13/03/24, 5:39:24 PM] khushi e.c: Branch :- Electronics & Communication Engineering	
College:- Technocrat Institute of Technology
Name :- 	RAVINDRA KUMAR
Contact:- 	9572233410		
Expected date:- 
  16 March m.p Nagar
[13/03/24, 5:41:27 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Lakshmi Narain College of Technology Excellence
	HEMANT RAJ	
9135607497	
13 march  indrapuri
[13/03/24, 5:42:48 PM] ~ Deepali coding: B.Tech	Information Technology	NRI Institute of Information Science & Technology	SUMAN KUMARI		8319152148	will come indrapuri
[13/03/24, 6:00:27 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Lakshmi Narain College of Technology Excellence	
TAISON YADAV	9151330359	
after holi 
Indrapuri
[13/03/24, 6:08:36 PM] anchal e.c: B.Tech	Computer Science & Engineering-Artificial Intelligence and Machine Learning
	NRI Institute of Information Science & Technology	
SATAKSHI VAIDHY
	7987940465	
after holi 
 indrapuri
[13/03/24, 6:10:28 PM] ~ Mahi: NRI Institute of Information Science & Technology	
ANKIT KUMAR YADAV
	7415157283
	will come 18 march
Indrapuri
[13/03/24, 6:13:29 PM] khushi e.c: Branch :- Electronics & Communication Engineering	
College:- Technocrat Institute of Technology
Name :- 	RUPESH KUMAR
Contact:- 	6202217625	
Expected date :- 	15march indrapuri
[13/03/24, 6:23:42 PM] ~ Mahi: NRI Institute of Information Science & Technology
	VISHAL NAMDEV
	7970041292	
will come 17 march 
indrapuri
[13/03/24, 6:26:06 PM] anchal e.c: B.Tech	Cyber Security	
NRI Institute of Research & Technology	
JAYANT CHOUKIKAR
	7000722575
	17 March 
indrapuri
[13/03/24, 6:32:08 PM] ~ Chauhan Shilpa: Name of Student:-GAUTAM KUMAR
College name:-Technocrat Institute of Technology
Contact no:-6206414620
Branch:-Electronics & Communication Engineering
Expected Date of Visit :  will come April
[13/03/24, 6:32:40 PM] anchal e.c: B.Tech	Cyber Security
	NRI Institute of Research & Technology	
UDAY NAGAR	
8815514579	
	will think
[13/03/24, 6:33:28 PM] khushi e.c: Computer Science & Engineering	
College:;Vaishnavi Inst. of Tech. & Science
Name :- 	DIVYANSHU KUSHWAHA
Contact:- 	9685499314
Expected date:- 	17March
[13/03/24, 6:46:35 PM] Neha mam e.c: @919424704675 @916263594069 @916263551348 koi enquiry aayi kya
[13/03/24, 6:46:52 PM] ~ Deepali coding: Yes mam
[13/03/24, 6:47:04 PM] Neha mam e.c: Kitni
[13/03/24, 6:47:13 PM] ~ Deepali coding: 4
[13/03/24, 6:47:20 PM] Neha mam e.c: Abhi hai
[13/03/24, 6:47:29 PM] Neha mam e.c: Konse college
[13/03/24, 6:47:30 PM] ~ Mahi: NRI Institute of Information Science & Technology	
MANISH KUMAR TIWARI
	9589563405	
will think 18 march
indrapuri
[13/03/24, 6:51:57 PM] anchal e.c: B.Tech	Information Technology
	NRI Institute of Information Science & Technology
	ROSHANI DUBEY
	8269415709	
	will think ⭐
[13/03/24, 6:59:48 PM] ~ Deepali coding: Oist
[13/03/24, 7:02:26 PM] Neha mam e.c: Iska answer to diya nahi
[13/03/24, 7:08:05 PM] khushi e.c: Computer Science & Engineering-Internet of Things and Cyber Security Including Block Chain Technology
College:- 	Lakshmi Narain College of Technology
Name :- 	MOHAMMAD LUQMAN
Contact:- 	7223813123	
Expected date :- 	after ramzan
[13/03/24, 7:51:18 PM] ~ Chauhan Shilpa: Visit done
[13/03/24, 7:52:49 PM] ~ Mahi: Ok mam Thankyou
[13/03/24, 7:53:15 PM] ~ Chauhan Shilpa: Visit done
[13/03/24, 7:55:36 PM] ~ Chauhan Shilpa: Visit done
[13/03/24, 8:00:06 PM] ~ Hafsa , Coding Thinker: Thank you
‎[14/03/24, 11:23:52 AM] Neha mam e.c: IMG_6527.MP4 ‎document omitted
[14/03/24, 11:38:29 AM] Neha mam e.c: Set as a status
[14/03/24, 11:38:43 AM] anchal e.c: Yes ma'am
[14/03/24, 11:40:58 AM] khushi e.c: Yes mam
[14/03/24, 12:29:22 PM] anchal e.c: Bansal group of institute
AMIT SAKET	
9343592947	
17 March
[14/03/24, 12:43:01 PM] ~ Deepali coding: Name of Student: Devesh
College name: NRI 
Contact no: 9343761857
Branch: CSE
Year: 3rd Year 
Expected Date of Visit:  Will come 16 march chetak
[14/03/24, 12:51:03 PM] anchal e.c: Name of Student: subhra Pandey 
College name: sam girls college 
Contact no:9142011980
Branch: CSE

Expected Date of Visit:  Will come mp nagar
[14/03/24, 1:21:03 PM] Harsh sir tl: When ?
[14/03/24, 1:31:38 PM] anchal e.c: Date nahi btai
[14/03/24, 1:31:57 PM] Harsh sir tl: Ok
[14/03/24, 1:50:02 PM] ~ Chauhan Shilpa: Name of Student:-VIJAY PATEL
College name: Patel College of Science & Technology
Contact no: 9451323699
Branch:Computer Science & Engineering
Expected Date of Visit:  5 April
[14/03/24, 1:56:54 PM] ~ Chauhan Shilpa: Name of Student:-MONESH SAHU
College name: Technocrats Institute of Technology [Excellence]
Contact no: 8959711090
Branch:Computer Science & Engineering
Expected Date of Visit:  25 March
[14/03/24, 1:57:34 PM] Neha mam e.c: Holi vale din aayega
[14/03/24, 2:03:10 PM] annu❤️: B.Tech	
Computer Science & Engineering	
J.N. College of Technology
MRITYUNJAY RAM
7739496085	
After Holi 
2nd Year
[14/03/24, 2:54:32 PM] ~ Chauhan Shilpa: Mam student ne March last bola tha
[14/03/24, 2:55:28 PM] annu❤️: B.Tech	
Computer Science & Engineering	
J.N. College of Technology
RINKI KUMARI
7667706826	
15 March	
Indrapuri 
2nd Year
[14/03/24, 3:17:15 PM] khushi e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Lakshmi Narain College of Technology & Science	DEVANSH UPADHYAY	9584459780
Expected date will think
[14/03/24, 3:33:48 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrat Institute of Technology	
AMAN ANAND
7869142475	
14 March	
Indrapuri 
2nd Year
[14/03/24, 3:49:48 PM] annu❤️: Filter lga hh
[14/03/24, 3:49:55 PM] annu❤️: Check kro aap
[14/03/24, 3:50:13 PM] Harsh sir tl: Mera mtlb h itne saare
[14/03/24, 3:50:25 PM] Harsh sir tl: Not answered inko
[14/03/24, 3:50:36 PM] Harsh sir tl: Sham ko hi lagana abhi bhi not answered m hi jarahe hena
[14/03/24, 3:50:37 PM] annu❤️: Hnnn filter main sare hi ate hh
[14/03/24, 3:50:57 PM] annu❤️: Ok
[14/03/24, 4:57:31 PM] anchal e.c: Shubham kumar yadav	
Oriental institute of science and technology	IT	
6202203806	
Software engineer	
will come 16,17 march 
indrapuri ‎<This message was edited>
[14/03/24, 5:05:49 PM] anchal e.c: Sarthik SIngh Thakur
	Oriental Institute of Science and Technology	IT
	9165240649
	Web Developer	
Will think
[14/03/24, 5:39:05 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Data Science	
Technocrat Institute of Technology	
RAJA BABU
6202081037	
15 March	
Indrapuri 
2nd Year
[14/03/24, 5:40:39 PM] kasim k: Isha dutt	
Oriental institute of science and technology 	
IT	
7000788849	
Web developer 	
1april chetak
[14/03/24, 5:51:31 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Data Science	
Technocrat Institute of Technology	
HIMANSHU CHAUDHARY
9340072905	
Will think 	After Holi 
2nd Year
[14/03/24, 5:54:05 PM] ~ Mahi: will come  17 march.  with  frinds. anuj ,arjun,kapil,Ayush
Indrapuri
[14/03/24, 6:22:02 PM] khushi e.c: Branch :: Information Technology
College:- 	Technocrat Institute of Technology
Name :- 	SUDHANSHU KUMAR JHA
Contact:- 	6203196024		
Expected date:- after holi  indrapuri
[14/03/24, 6:29:37 PM] annu❤️: B.Tech	
Computer Science & Engineering â€“ Artificial Intelligence	
Technocrat Institute of Technology	
KASHISH SINGH
9302272700	
After Holi 
2nd Year
[14/03/24, 6:36:45 PM] ~ Mahi: NRI Institute of Information Science & Technology	
ABHISHEK KUMAR
 MISHRA	
9752188261	
	will come after holi
[14/03/24, 6:37:29 PM] khushi e.c: B.Tech	Computer Science & Engineering-Artificial Intelligence and Data Science
College:- 	Technocrat Institute of Technology
Name :- 	AMIT KHAIR
Contact:- 	8224919671		 
Expected date:-  after holi  m.p nagar
[14/03/24, 6:38:02 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Data Science	
Technocrat Institute of Technology	
AKHIL SONI
7987210614	
22 March	
Indrapuri 
2nd Year
[14/03/24, 6:38:47 PM] Harsh sir tl: @916263594069prospects nai bnrahe kya aaj ?
[14/03/24, 6:39:16 PM] ~ Deepali coding: Sir iss time calling nhi ho pati yaha
[14/03/24, 6:41:10 PM] Harsh sir tl: Can you be more specific with reason
[14/03/24, 6:43:54 PM] ~ Mahi: NRI Institute of Information Science & Technology	
SAKSHAM DWIVEDI
	7415289297	
	will come after holi
[14/03/24, 6:46:49 PM] khushi e.c: Computer Science & Engineering-Artificial Intelligence and Data Science	
College:- Technocrat Institute of Technology
Name:- 	LOKESH RAGHUWANSHI
Contact:- 	7440840443		
Expected date :- 19 March indrapuri
[14/03/24, 6:51:21 PM] kp sir: Harsh sir 1-2 din LNCT KA MAT DOO DATA WAHA TECH FEST CHALRAHA SAYAD , DUSRE TIT KA AI ML AUR BRANCH KA DEDDOO 1-2 DIN
[14/03/24, 6:51:48 PM] Harsh sir tl: Ok sir
[14/03/24, 6:58:37 PM] ~ Mahi: IES College of Technology
	SHIVAM YADAV
	9305460284	
	will think
[14/03/24, 7:02:38 PM] khushi e.c: Branch ;- B.Tech	Computer   :: Science & Engineering-Artificial Intelligence and Data Science	
College:- Technocrat Institute of Technology
Name ;: 	SHARADDHA TAWAR
Contact:- 	9329129478		 
Expected date:- 17 March Indrapuri
[14/03/24, 7:14:31 PM] kasim k: B.Tech
Artificial Intelligence and Data Science	
Lakshmi Narain College of Technology	
AVIRAL DUBEY	
7477096630	
15march chetak
[15/03/24, 1:13:44 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrat Institute of Technology
UTKARSH SINGH BHADAURIYA
9171994938	
After this semester 
Indrapuri 
2nd Year
[15/03/24, 1:23:06 PM] anchal e.c: Computer Science & Engineering	
Technocrats Institute of Technology & Science	
SATYAPRAKASH MEENA
	8871297703	
will think
[15/03/24, 1:25:08 PM] khushi e.c: Branch :- Computer Science & Engineering-Artificial Intelligence and Data Science
College:- 	Technocrat Institute of Technology
Name :- 	AKASH KUMAR GUPTA
Contact:- 	7898608546		
Expected date:- 17 March Indrapuri
[15/03/24, 2:56:30 PM] khushi e.c: Branch :-  Computer Science & Engineering-Artificial Intelligence and Data Science	
College:: :- Technocrat Institute of Technology
Name :- 	MUBASSHERA RIZVI
Contact:- 	9074239321	
 Expected date ,:- 	17 March Indra puri
[15/03/24, 3:30:18 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrats Institute of Technology & Science
RITESH KUMAR YADAV
6295569165	
1 April
2nd Year
[15/03/24, 3:32:18 PM] anchal e.c: Information 
Technology	Bansal Institute of Science & Technology	
RAGHURAJ SINGH	
9575626773
will think
[15/03/24, 3:44:27 PM] annu❤️: B.Tech	
Computer Science & Engineering
Technocrats Institute of Technology & Science
ABHISHEK KUMAR SINGH	
6204584496	
7389738418
15 March	 with Anurag 
Indrapuri 
2nd Year
[15/03/24, 3:47:14 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Data Science	
Technocrat Institute of Technology	
ABHYANSHU BENDE	
9755723930	
20.march will come 
mp nagar
[15/03/24, 4:22:12 PM] kasim k: B.Tech	Computer Science & Engineering	
Lakshmi Narain College of Technology	
DHANANJAY SINGH KANWAR 8815327663	
Sunday 17 March
[15/03/24, 4:22:32 PM] kasim k: B.Tech	
Computer Science & Information Technology	
Sagar Institute of Research & Technology	
ROHIT KUMAR YADAV	8051643108	
16march indrpuri
[15/03/24, 4:45:11 PM] ~ Deepali coding: Computer Science & Engineering	Technocrats Institute of Technology [Excellence]	GULSHAN KUMAR	9508157265	come 5 april
[15/03/24, 4:54:25 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
Sagar Institute of Research & Technology	
MOHIT	
9340700626	 
may batch
[15/03/24, 4:56:17 PM] khushi e.c: Branch :- B.Tech	Computer Science & Engineering-Data Science
College:- 	Technocrat Institute of Technology
Name :- 	JAYDEEP LODHI
Contact:- 	7828484941		
Expected date:- after holi
[15/03/24, 5:45:37 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	
Sagar Institute of Research & Technology	
MALAY JAIN	
6232155888	
pytn dsa will think
[15/03/24, 5:42:46 PM] ~ Deepali coding: Computer Science & Engineering	Radharaman Engineering College	VISHAL	9625330997	will come 16 march
[15/03/24, 6:43:46 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Radha Raman Institute of Technology & Science	
RUPESH KUMAR	9334965103
	after holi 
indrapuri
[15/03/24, 7:32:49 PM] kasim k: B.Tech
Computer Science & Engineering-Cyber Security	
Sagar Institute of Research & Technology	
KHUMANSHU BUDHOLIYA	
8435793621	
17March
[16/03/24, 11:46:54 AM] kasim k: Branch :- B.Tech	CS
Collge- Bansal
Name :- 	Kuldeep
Contact:- 8103035397
Expected date:- 20march
[16/03/24, 1:14:35 PM] ~ Mahi: will come 17 march with frinds shiva,shub,shivam
chetak
[16/03/24, 1:41:07 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence	
AYUSHI SINGH
9691603407	
Will think 
2nd Year
[16/03/24, 1:44:43 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence
DEEPAK KUMAR KUSHWAHA
7805960449	
After Holi 
2nd Year
[16/03/24, 2:55:07 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence	
GULAM GOUS
6232659032	
After Eid 
2nd Year
[16/03/24, 3:00:35 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence	
RASHI YADAV
7049891881	
18 March	Chetak 
2nd Year
[16/03/24, 3:09:55 PM] ~ Mahi: Trinity Institute of Technology & Research
	GAURAV VERMA
	9263066822	
will think
[16/03/24, 3:17:05 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence
ANUPAM VISHWAKARMA
7898945097	
Will think Call back himself 
2nd Year
[16/03/24, 3:47:58 PM] ~ Mahi: Sagar Institute of Science & Technology, Pipalner Gandhi Nagar Bhopal
.	VISHAKHA SHARMA
3rd year
	7224011931
	will think 17 march
chetak
[16/03/24, 4:27:45 PM] ~ Hafsa , Coding Thinker: Will come on 18 March ( Indrapuri )
[16/03/24, 5:34:29 PM] anchal e.c: Computer Science & Engineering-Artificial Intelligence and Machine Learning	
IES College of Technology
	FAHEEM ANSARI
	9525020369				
After 30 march
[16/03/24, 5:41:39 PM] kasim k: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Technocrats Institute of Technology [Excellence]	
YOGESH SAHU	
9691223326	
25march +tanishq
[16/03/24, 5:47:33 PM] ~ Mahi: Trinity Institute of Technology & Research
	MD SAIF ALI KHAN
	8789636189	
after eid
[16/03/24, 5:54:53 PM] kasim k: B.Tech
Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
SUDHIR	
7447097453	
5April
[16/03/24, 5:57:23 PM] ~ Mahi: Trinity Institute of Technology & Research
	RAJA BABU AHIRWAR
	9329418238	
will come  20 march
chetak
[16/03/24, 6:14:55 PM] kasim k: B.Tech	
Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]	
AKASH KUSHWAHA	
9589416182	
indprui 20 march (c,c++)
[16/03/24, 6:19:20 PM] ~ Mahi: Bansal Institute of Science & Technology
	ANKIT KUMAR SINGH
	8918876671	
	will think after 20 march
indrapuri
[16/03/24, 6:36:39 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Radha Raman Institute of Technology & Science
	PRATIKSHA PAL
	6267187782
	will think
[16/03/24, 6:44:58 PM] ~ Deepali coding: Computer Science & Engineering-Artificial Intelligence and Machine Learning	Oriental Institute of Science & Technology	SONIKA RAI	9303949090 come 20 march
[16/03/24, 6:59:22 PM] anchal e.c: B.Tech	Computer Science & Engineering	Radha Raman Institute of Technology & Science	
AYUSH BISEN	
9294714406	
April will come
[16/03/24, 7:03:20 PM] ~ Deepali coding: Will come today indrapuri
[16/03/24, 7:09:39 PM] ~ Mahi: Bansal Institute of Science & Technology
	SHUBHAM PATHAK
	8602457304	
	will come today 16 march
indrapuri
[16/03/24, 7:14:43 PM] kasim k: B.Tech	
Artificial Intelligence and Machine Learning	Sagar Institute of Research & Technology	
VIVEK RAMANLAL LILHARE	9075658131	
28 March
[16/03/24, 8:59:30 PM] Neha mam e.c: Durga kal se aap reception par seating hai 
Arpana aap piche hi caller vali  jagah hi kaam karna
[16/03/24, 9:08:03 PM] ~ Mahi: yes mam
[17/03/24, 1:02:12 PM] kasim k: Artificial Intelligence and Machine Learning	Sagar Institute of Research & Technology	
HARIOM SONI	
9302423440	
 25march
[17/03/24, 1:14:11 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal Institute of Research & Technology	
ANIL KUMAR KUSHWAHA	6265988190	
	26 march 
jabalpur
[17/03/24, 1:33:19 PM] Neha mam e.c: @919424704675 @916263594069 @916263551348 konse data par calling kar rahe ho
[17/03/24, 1:33:46 PM] anchal e.c: 2nd year bansal
[17/03/24, 1:33:59 PM] Neha mam e.c: Branch
[17/03/24, 1:34:26 PM] anchal e.c: Cs
[17/03/24, 1:34:40 PM] ~ Deepali coding: Bansal cs 2 year pr mam
[17/03/24, 1:34:46 PM] Neha mam e.c: Kya response Bansal cs
[17/03/24, 1:34:54 PM] anchal e.c: Not answering
[17/03/24, 1:34:56 PM] Neha mam e.c: Dono same kar rahe ho
[17/03/24, 1:34:57 PM] anchal e.c: Jyda h
[17/03/24, 1:35:03 PM] Neha mam e.c: Acha
[17/03/24, 1:35:14 PM] ~ Deepali coding: Mam data bansal ka or Radha raman ka hi hai
[17/03/24, 1:35:16 PM] ~ Deepali coding: Abhi
[17/03/24, 1:35:25 PM] Neha mam e.c: Kitne din se Bansal kar rahe ho
[17/03/24, 1:35:29 PM] ~ Deepali coding: Radha raman pr response nhi hai isley bansal kar rhe hai
[17/03/24, 1:35:32 PM] anchal e.c: Aaj hi
[17/03/24, 1:35:33 PM] ~ Chauhan Shilpa: Mam lnct 2 nd yr Electronics
[17/03/24, 1:35:34 PM] anchal e.c: Diya h
[17/03/24, 1:35:36 PM] anchal e.c: Bansal
[17/03/24, 1:35:45 PM] Neha mam e.c: Iske pehale
[17/03/24, 1:35:50 PM] anchal e.c: Kl parso radha raman
[17/03/24, 1:35:51 PM] ~ Deepali coding: LNCT cs
[17/03/24, 1:35:55 PM] anchal e.c: Use pehele LNCT
[17/03/24, 1:36:07 PM] Neha mam e.c: LNCT me bhi response nahi hai
[17/03/24, 1:36:25 PM] Neha mam e.c: Cs and electronics
[17/03/24, 1:36:27 PM] Neha mam e.c: Me
[17/03/24, 1:36:31 PM] anchal e.c: Ma'am sab not interested
[17/03/24, 1:36:34 PM] anchal e.c: Me h
[17/03/24, 1:36:37 PM] Neha mam e.c: Acha
[17/03/24, 1:36:50 PM] Neha mam e.c: Ur uske pehale konsa kar rahe the
[17/03/24, 1:37:08 PM] anchal e.c: Meri sheet lnct hi dete h
[17/03/24, 1:37:12 PM] anchal e.c: Sir jyda
[17/03/24, 1:37:21 PM] Neha mam e.c: Acha
[17/03/24, 1:37:35 PM] Neha mam e.c: LNCT not interested chal raha hai
[17/03/24, 1:37:36 PM] Neha mam e.c: Ok
[17/03/24, 1:37:44 PM] Neha mam e.c: Radharaman bhi same
[17/03/24, 1:37:53 PM] Neha mam e.c: Bansal bhi same
[17/03/24, 1:38:10 PM] anchal e.c: Bansal aaj hi mila h
[17/03/24, 1:38:18 PM] anchal e.c: Pure call nahi kiye abhi
[17/03/24, 1:38:20 PM] Neha mam e.c: Shilpa maam aapka Kya response hai
[17/03/24, 1:38:29 PM] Neha mam e.c: Ok
[17/03/24, 1:38:37 PM] Neha mam e.c: Mostly not answering hai
[17/03/24, 1:39:00 PM] anchal e.c: Ek bar or call krugi ma'am us pr jo not answering h
[17/03/24, 1:39:02 PM] ~ Chauhan Shilpa: Mam electric par call kar rahe hain to Abhi usmein to interested nahin hai student
[17/03/24, 1:39:14 PM] Neha mam e.c: Acha
[17/03/24, 1:39:20 PM] ~ Chauhan Shilpa: Ji mam
[17/03/24, 1:39:25 PM] Neha mam e.c: Not interested hi hai aapka bhi
[17/03/24, 1:39:44 PM] ~ Chauhan Shilpa: Ji mam
[17/03/24, 1:41:15 PM] kasim k: ban raha hai prospect baki abhi followups le raha hu
[17/03/24, 1:41:34 PM] annu❤️: Ban rahe hai mam prospect Sagar pr bhi Bane hai mere
[17/03/24, 1:43:39 PM] ~ Ravi Gupta: ‎Neha mam e.c added ~ Ravi Gupta
[17/03/24, 1:44:10 PM] Neha mam e.c: Kasim tumhe kon konsa college mila hai
[17/03/24, 1:44:19 PM] Neha mam e.c: Anushree tumhe
[17/03/24, 1:44:40 PM] ~ Ravi Gupta: 1st year main kya response hai
[17/03/24, 1:44:49 PM] Neha mam e.c: 1 year me response aa raha hai
[17/03/24, 1:44:52 PM] kasim k: College - Sagar Institute of Research & Technology
branch - Computer Science & Engineering-Cyber Security,
CsIT,
Aiml
[17/03/24, 1:45:31 PM] Neha mam e.c: Arpana aapse bhi pucha hai
[17/03/24, 1:45:34 PM] annu❤️: 1st year ka data hi nahi hai
[17/03/24, 1:45:38 PM] ~ Mahi: data ni h  wo
[17/03/24, 1:45:55 PM] kasim k: data hi nahi sir abhi 2 nd year ka hi mil raha
[17/03/24, 1:45:58 PM] Neha mam e.c: To konsa data hai
[17/03/24, 1:46:03 PM] ~ Mahi: morning sw aj ke followups liye h mbne
[17/03/24, 1:46:03 PM] annu❤️: 2nd Year
[17/03/24, 1:46:05 PM] annu❤️: Hai
[17/03/24, 1:46:10 PM] kasim k: 2nd year 3,4sam
[17/03/24, 1:46:18 PM] ~ Mahi: abhi sir se data liya tit ka uspr call kr rhi
[17/03/24, 1:46:22 PM] Neha mam e.c: Overall baat ho rahi hai
[17/03/24, 1:47:08 PM] Neha mam e.c: 2nd year mill raha hai jo student 3/4 semester hai
[17/03/24, 1:47:22 PM] kasim k: yes mam
[17/03/24, 1:47:29 PM] Neha mam e.c: Ok
[17/03/24, 1:47:38 PM] ~ Ravi Gupta: Kya response hai
[17/03/24, 1:47:38 PM] anchal e.c: Mere pass h wo glt ho gya tha data anurag se to us pr call krne ke liye mna kr diya tha
[17/03/24, 1:48:00 PM] Neha mam e.c: Iss data ko apan kitni baar call kiya hai
[17/03/24, 1:48:13 PM] annu❤️: 3-4 baar mam
[17/03/24, 1:48:14 PM] kasim k: 3/4 baar mam
[17/03/24, 1:48:51 PM] ~ Mahi: 2 bar
[17/03/24, 1:48:59 PM] Neha mam e.c: Matlab
[17/03/24, 1:49:11 PM] Neha mam e.c: 2 baar kab
[17/03/24, 1:49:17 PM] Neha mam e.c: Kab
[17/03/24, 1:49:29 PM] Neha mam e.c: Kab
[17/03/24, 1:49:55 PM] ~ Mahi: phle kiya feb me or ab not anwser pr
[17/03/24, 1:50:14 PM] Neha mam e.c: Iske pehale bhi kiya tha last year
[17/03/24, 1:50:17 PM] kasim k: mam ek baar auguest mai 
aur ek br usk phel kia tha fit digital market vghre pe cyber v pitch kiya shyd us data pe
 firrr jb sheet shuffle hui tau  fir se  kia
[17/03/24, 1:50:24 PM] kasim k: han mam kiya tha
[17/03/24, 1:50:39 PM] Neha mam e.c: Data sayad mene Sep me kharida hai
[17/03/24, 1:51:05 PM] kasim k: mere mai hi 2 br sheet bani hui hai  ek auguest 1 year aur ek 1year c,c++
[17/03/24, 1:51:40 PM] Neha mam e.c: Matlab kaisi
[17/03/24, 1:58:53 PM] Harsh sir tl: Bansal or JNCT ?? 
CSE KE OR AIML KE milakr 191 jo h wo bhi to bataiye
[17/03/24, 1:59:14 PM] Harsh sir tl: Baaki sb log jitna allot h kon kon se colleges ka diya tha wo bataiye
[17/03/24, 2:00:09 PM] Harsh sir tl: Such as @916260034224arpana
IES NRI or trinity LNCT 
Bansal ese mam ko pura update karo
[17/03/24, 2:02:18 PM] Neha mam e.c: Kp sir apan 2 year ka data kab purchase kiya tha
[17/03/24, 2:05:43 PM] ~ Chauhan Shilpa: Name of Student:-RAUNAK KUMAR
College name: Lakshmi Narain College of Technology
Contact no: 8969486995
Branch: Electronics & Communication Engineering
Expected Date of Visit:  10 April
[17/03/24, 2:07:30 PM] Harsh sir tl: KP sir stated that he would allocate the data for the first year, so I refrained from accessing it. ‎<This message was edited>
[17/03/24, 2:09:30 PM] kp sir: 1 year allot abhi kardungaa toh phir usmee bolenge ki 1 year ka hai language main jaarahe hain , placement batch nain nahi aur phir is Data par bhi aaplog yahi bologogee ki Kai baar call hogyaa is par .so 2 year data se hi output nikalee
[17/03/24, 2:10:30 PM] Harsh sir tl: Totally understandable working on it
[17/03/24, 2:11:45 PM] kp sir: August- sep main aaya tha maam
[17/03/24, 2:12:26 PM] Neha mam e.c: To apan ne kitni baar inse iss data par call karvaya hai
[17/03/24, 2:13:39 PM] kp sir: 2-3  baar hogya hai lagbhag .
1 time jab 2 sem main data tha 
Phir 3 sem 
Aur abb 4 sem main aagye hain bachhe
[17/03/24, 2:15:30 PM] Neha mam e.c: Kasim kahe raha hai ki pehale cyber ke liye ragda phir digital marketing phir full stack and Ds ur ek baar laguage pitch kiya hoga
[17/03/24, 2:15:55 PM] kasim k: digital marketing tau kia cyber ka cnfrm nhi mam
[17/03/24, 2:16:09 PM] Neha mam e.c: Cyber kiya hoga
[17/03/24, 2:16:18 PM] kasim k: han mam ho skte haiii
[17/03/24, 2:17:45 PM] kp sir: Digital marketing par toh non-technical data par karayaatha is par kahaa karayaa
[17/03/24, 2:18:42 PM] kasim k: sir dono per hi hua tha yeh course dono k lie tha na  baki 3/4 br tau norml hi calling ki java pytn c,c++ ki
[17/03/24, 2:20:04 PM] kp sir: Achha itne caller the ki 10 day ki calling main 12000data par sab ne cyber par calling karli Aur digital marketing par 1 week calling kaari toh uspar bhi 12000 data par calling phir se hogyai . Gajab ki calling speed hai sabhi ki Matlab
[17/03/24, 2:20:40 PM] kp sir: Kasim cyber ka bolrahe hoo 
Speed fast hogi matlab
[17/03/24, 2:20:53 PM] kasim k: cyboer tau 2 log hi kr rhe the ne  kajal aur bharat .
pure data ka ni kh raha mai
[17/03/24, 2:21:22 PM] kp sir: Mujee toh nahi lagtaa ki 12000 par digital marketing pitch Kiya hoo Aur cyber
[17/03/24, 2:21:27 PM] kp sir: Haan
[17/03/24, 2:21:29 PM] kasim k: mere
mai 2 sheet bani hui haiii 3 sheet hai mere pass 1 year ki
hii agr maina ki tau sub ne hi kia hogi
[17/03/24, 2:21:54 PM] kp sir: Jaroori nahi hai naa ki sabne Kiya hooo
[17/03/24, 2:22:15 PM] kasim k: han sir jaruri tau nahin hai
[17/03/24, 2:23:03 PM] kp sir: 12000 data par calling 1 baar full flash karne main itnaa time lagtaa hai . 
Apan ne DIGITAL MARKETING ,CYBER SABKE LIYEE SABHI KO PITCH KARDIYAA
[17/03/24, 2:26:28 PM] Neha mam e.c: Nahi overall apan ye baat isliye kar rahe jab inse apan kuch puche rahe hai admission regarding to ye log answer ye dete hai data not answering hai not interested hai coding thinker sune kar call cut ho rahe hai prospect ban nahi rahe hai 60 ki calling kar rahe hai to 1-2 badi mushkil se ban rahe hai to kya karna chaiye apan ko
[17/03/24, 2:38:22 PM] kp sir: Harsh sir 3 year wale data par bhi same response hai kya ,unko call karwaloo CRT ke liye wolog kya bolrahe hain . Abhi aptitude bhi start horaha hai apnaa agar kuch banrahe hootoh bula loo .
Kisi ek ko dear dekhoo data response Pata karoo
[17/03/24, 2:38:44 PM] kp sir: 3 year ka
[17/03/24, 2:39:35 PM] kp sir: 2025 passout data par kisi ek caller ko dekar dekhooo
[17/03/24, 2:40:25 PM] Harsh sir tl: Sir wolog ka response thoda better h
[17/03/24, 2:41:40 PM] Harsh sir tl: Team you already have allot of data from 3 year kindly start your calling on that and submit the response ill go through that once again
[17/03/24, 2:42:19 PM] Neha mam e.c: Mere hisaab se nahi hoga time barbaad hi hoga
[17/03/24, 2:42:26 PM] Neha mam e.c: Par check kar lo
[17/03/24, 2:50:29 PM] kp sir: Aaj saam tak check karloo kya response hai .
[17/03/24, 2:57:41 PM] kasim k: Computer Science & Engineering	
3year 
Oriental College of Technology
SUDEEP MISHRA	
7999778565	
24-25march
[17/03/24, 2:58:06 PM] kasim k: sir CRT ka batch kb se start ho raha haiii
‎[17/03/24, 3:07:35 PM] Neha mam e.c: ‎image omitted
[17/03/24, 3:20:45 PM] ~ Hafsa , Coding Thinker: Will come on 19 March with Muskan Chourasia
[17/03/24, 3:36:18 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]
ABHINAV NAYAK
9179382633	
In April 
2nd Year
[17/03/24, 3:38:33 PM] ~ Mahi: will come today chetak
[17/03/24, 3:58:49 PM] ~ Mahi: Technocrat Institute of Technology
	GAUTAM KUMAR
	7050585503
	will come 18 march
indrapuri
[17/03/24, 4:23:27 PM] Neha mam e.c: Anushree harshit ka kya hai
[17/03/24, 4:30:47 PM] annu❤️: Bolra tha mam aa rha hu
[17/03/24, 4:42:57 PM] Neha mam e.c: Aaya nahi hai sayad
[17/03/24, 5:20:34 PM] ~ Mahi: with frind laxmi
[17/03/24, 5:26:16 PM] Harsh sir tl: @919424704675 @916263551348 @916263594069 are we done enquiry pad if it is done kindly update me with your 3rd year data
[17/03/24, 5:26:33 PM] ~ Deepali coding: Sir 3 year hi kar rhi hu abhi
[17/03/24, 5:26:56 PM] ~ Deepali coding: Nhi aa rha koi response coding course sun kar cut kar rhe hai yaa fr not interested bol rhe hai
[17/03/24, 5:27:08 PM] Harsh sir tl: response kesa araha hai ?
[17/03/24, 5:27:45 PM] ~ Deepali coding: Nhi aa rha hai kuch bhi
[17/03/24, 5:27:59 PM] Harsh sir tl: ok then its already 5:30 you are suggested to start your calling on 2nd year
[17/03/24, 5:28:07 PM] ~ Deepali coding: Oky
[17/03/24, 5:28:09 PM] anchal e.c: Ok sir
‎[17/03/24, 5:28:35 PM] Neha mam e.c: IMG_6606.MP4 ‎document omitted
[17/03/24, 5:28:59 PM] Neha mam e.c: Set as a status
[17/03/24, 5:41:32 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Technocrats Institute of Technology [Excellence]
ASTHA PATAIRIYA
9098415261	
18 March	
Indrapuri 
2nd Year
[17/03/24, 5:44:21 PM] kasim k: B.Tech	
Computer Science & Engineering-Cyber Security	
Sagar Institute of Research & Technology	
AKASH RAWAT	
8962445280	
18march
 +himanshu badhoriya	
indrpur
[17/03/24, 5:54:47 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal College of Engineering
	RITIK CHOUHAN	
8103728519
	will think
[17/03/24, 6:06:20 PM] ~ Chauhan Shilpa: Name of Student:-PRANAV MAITY
College name:-J.N. College of Technology
Contact no:-7649055227
Branch:-Artificial Intelligence and Machine Learning
Expected Date of Visit:-  15 April
[17/03/24, 6:07:25 PM] ~ Mahi: Technocrat Institute of Technology
	PRINCE KUMAR
	8092103166	
will come after holi
[17/03/24, 6:13:18 PM] ~ Chauhan Shilpa: Name of Student:-MANISH YADAV
College name:-J.N. College of Technology
Contact no:-7987501096
Branch:-Artificial Intelligence and Machine Learning
Expected Date of Visit:-  28 March (mp nagar)
[17/03/24, 6:16:52 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal College of Engineering	
ARJUN	
6232658706	
will think  with frds
[17/03/24, 6:50:03 PM] ~ Chauhan Shilpa: Name of Student:-SOURABH VISHWAKARMA
College name:-Bansal College of Engineering
Contact no:-8964087020
Branch:-Computer Science & Engineering
Expected Date of Visit:-  after holi (mp nagar)
[17/03/24, 6:56:50 PM] ~ Chauhan Shilpa: Name of Student:-AYUSH DAMLE
College name:-Bansal College of Engineering
Contact no:-9713521979
Branch:-Computer Science & Engineering
Expected Date of Visit:- 4 April (mp nagar)
[17/03/24, 7:13:36 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Bansal College of Engineering	
MEGHA KADAM	
9770796225	
will come April ⭐
 indrapuri 
With friend sherya disha
[17/03/24, 7:44:48 PM] kp sir: Kasim ,tomendra ko Jada call mat karnaa Holi ke baad ka bola hai isnee
[17/03/24, 7:47:10 PM] kasim k: han sir thik hai
[18/03/24, 12:20:23 PM] Harsh sir tl: Team you all are suggested to shoot msgs and videos of placed students on there WhatsApp
[18/03/24, 12:21:12 PM] Harsh sir tl: And try to focus on 3 year and 4 year till 4 pm after that we will focus on 2nd year
[18/03/24, 12:23:22 PM] Harsh sir tl: Try to pitch them CRT and brief them about placements
[18/03/24, 1:57:53 PM] annu❤️: Electrical Engineering
Sagar Institute of Science Technology & Engineering	
MANVI BISEN
7724860976	
CRT 1 April 	
Indrapuri 
3rd Year
[18/03/24, 3:23:45 PM] Harsh sir tl: Team aaj se jiske pass LNCT ka data hai wo start krdena calling after 4:00 pm
[18/03/24, 3:27:16 PM] ~ Deepali coding: 8085174960
Name Vishal
Year 2
Come 21 March
[18/03/24, 4:26:44 PM] kasim k: B.Tech	
Computer Science & Information Technology	
Sagar Institute of Research & Technology	
AMISHA KUMARI	9472839609	
april 1 week
[18/03/24, 5:23:12 PM] anchal e.c: Electrical & Electronics Engineering	
Oriental Institute of Science & Technology	
GOVIND DHAKAD
	8349077155	    
Will come April
[18/03/24, 5:25:27 PM] ~ Mahi: Technocrat Institute of Technology
	GAURAV SHUKLA
	8871737358
	will come 24 march
chetak
[18/03/24, 5:32:53 PM] ~ Mahi: Technocrat Institute of Technology
	DHEERAJ WANJARE
	8629930167
	will come 28 march
chetak
[18/03/24, 5:44:13 PM] kasim k: B.Tech	
Computer Science & Information Technology	
Sagar Institute of Research & Technology	
YOGIRAJ SINGH AHIRWAR	9617217504	
after holi + vishal khuswaha
[18/03/24, 5:54:14 PM] kasim k: B.Tech	
Computer Science & Engineering-Cyber Security	Sagar Institute of Research & Technology	
SHREEMAYA DONGRE	9303044126	
 5 april
[18/03/24, 5:56:54 PM] ~ Mahi: Sagar Institute of Research & Technology
	ACHAL
	6268283132	
will come 20 mach
indrapuri
[18/03/24, 5:58:27 PM] Harsh sir tl: Team, could you please provide me with a brief overview of today's response on second year?
[18/03/24, 5:58:49 PM] Harsh sir tl: and 3rd-4tth year
[18/03/24, 6:07:22 PM] ~ Mahi: 4th year no response
[18/03/24, 6:07:50 PM] ~ Mahi: 2nd year we work on that .
[18/03/24, 6:08:14 PM] annu❤️: 3rd Year no response
[18/03/24, 6:09:04 PM] Harsh sir tl: No response nahi sunna hai mujhe i need brief overview kya response hai kya bolrahe h bacche
[18/03/24, 6:11:16 PM] anchal e.c: 3rd year no response
[18/03/24, 6:12:20 PM] anchal e.c: Joined other institute
Online Joined h
Not interested
[18/03/24, 6:30:33 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Bansal College of Engineering
	PAYAL CHOUDHARY	
8629909008	
April will come
 indrapuri
[18/03/24, 6:41:28 PM] ~ Mahi: Sagar Institute of Research & Technology
	PRERNA SAHU
	7067219929	
will come after holi  29 march
chetak
[18/03/24, 6:43:32 PM] ~ Chauhan Shilpa: Name of Student:-RISHABH TIKARIYA
College name:-Bansal College of Engineering
Contact no:-6268786191
Branch:-Computer Science & Engineering
Expected Date of Visit:- after holi (mp nagar)
[18/03/24, 6:58:44 PM] ~ Mahi: Sagar Institute of Research & Technology
	SANATAN SAHARIYA
	9752143412
	will come 21 march
[18/03/24, 7:05:07 PM] ~ Chauhan Shilpa: Name of Student:-REENA KUSHWAHA
College name:-Bansal College of Engineering
Contact no:-7828586133
Branch:-Computer Science & Engineering
Expected Date of Visit:- 27 march
[18/03/24, 7:06:42 PM] annu❤️: B.Tech	
Computer Science & Engineering	
Lakshmi Narain College of Technology	
ANIKET AGRAWAL
8109210483	
15 April
2nd Year
[18/03/24, 7:12:44 PM] annu❤️: B.Tech	
Computer Science & Engineering-Internet of Things and Cyber Security Including Block Chain Technology
Lakshmi Narain College of Technology	
PIYUSH MISHRA
6205902852	
After Holi 	
chetak 
2nd Year
[18/03/24, 7:30:36 PM] kasim k: B.Tech
Artificial Intelligence and Machine Learning	Sagar Institute of Research & Technology	
AYUSH PATWA	
9302617229	
19March
[18/03/24, 7:41:44 PM] kp sir: 4 year data par kisne calling ki thi aaj TIT PAR
[18/03/24, 8:00:21 PM] kp sir: Iskaa koi jawab nahi milaa
[18/03/24, 8:00:44 PM] kasim k: maina nhi kii
[18/03/24, 8:01:22 PM] kp sir: 5 admission hue hain jisnee bhi ki hoo batadeee abhi .
[18/03/24, 8:07:23 PM] annu❤️: Maine bhi 3rd Year pr kiya hai sir
[18/03/24, 8:09:50 PM] ~ Chauhan Shilpa: Name of Student:-MAHENDRA
College name:-Bansal College of Engineering
Contact no:-9302874338
Branch:-Computer Science & Engineering
Expected Date of Visit:- 5 April
[18/03/24, 8:22:30 PM] ~ Chauhan Shilpa: Name of Student:-SHIVAM GOUR
College name:-Bansal College of Engineering
Contact no:-7489343262
Branch:-Computer Science & Engineering
Expected Date of Visit:- 23 March
[18/03/24, 9:14:25 PM] anchal e.c: Call to nai kiye pr all year ke prospects pr msg dale the
[18/03/24, 10:15:40 PM] ~ Chauhan Shilpa: Sir kl call kiye the aj nhi old prospect par
[18/03/24, 11:30:23 PM] khushi e.c: ‎Harsh sir tl removed khushi e.c
[19/03/24, 10:58:21 AM] Harsh sir tl: Team, setbacks happen, but remember, we've got this. Reflect on what works, make adjustments, and celebrate every win, big or small. I believe in each of you. Don't lose hope. Management stands with you. Let's keep achieving success together.
[19/03/24, 1:07:25 PM] Harsh sir tl: Team aren’t you calling??
[19/03/24, 1:08:58 PM] Harsh sir tl: In day time i have already advised you to call on 4th year and 3rd year try to pitch them CRT
[19/03/24, 1:09:58 PM] Harsh sir tl: Aap logo ke hisaab se response nai araha tha but yesterday only we got 5 admission from final year so keep grinding your work
‎[19/03/24, 1:57:51 PM] Harsh sir tl: ‎audio omitted
[19/03/24, 2:04:38 PM] ~ Deepali coding: Name of Student:-sahil 
College name:-Ies college 
Contact no:9669758211
Branch:-Computer Science & Engineering
Expected Date of Visit:- come today 19 march chetak
[19/03/24, 2:05:33 PM] ~ Deepali coding: 3 rd year
[19/03/24, 2:45:37 PM] ~ Chauhan Shilpa: Name of Student:-ankit rathore 
College name:-tit
Contact no:- 9111913483
Branch:- electrical
Expected Date of Visit:- come today 19 indrapuri
[19/03/24, 3:38:21 PM] annu❤️: 442	
Computer Science & Engineering	
Lakshmi Narain College of Technology & Science
ANSHIKA GUPTA
6306230710	
Indrapuri 	
15 April
4th year
[19/03/24, 4:50:31 PM] ~ Mahi: coming todat with amit yash
[19/03/24, 5:18:35 PM] kp sir: @team I have alloted a data to you pls call them also
[19/03/24, 5:19:23 PM] Neha mam e.c: Aap logo ka break ka time change ho gya hai kya
[19/03/24, 5:19:33 PM] Neha mam e.c: Ya kaam karne ka maan nahi hai
[19/03/24, 5:19:55 PM] Neha mam e.c: Jab dekho jab time pass karte ho
[19/03/24, 5:20:00 PM] kp sir: Sabhi log apni grail I'd mere number par send kardeee
[19/03/24, 5:20:09 PM] anchal e.c: Ma'am me to call kr rhi hu jabalpur ke data pr
[19/03/24, 5:20:37 PM] Neha mam e.c: Aap log 5:17 ko bahar se aao
[19/03/24, 5:20:38 PM] Neha mam e.c: Hai
[19/03/24, 5:20:48 PM] Neha mam e.c: Phir kuch log baat karne lage
[19/03/24, 5:23:03 PM] kp sir: Gmail I'd bhejoo mujheee apni apnii
[19/03/24, 5:23:26 PM] annu❤️: B.Tech	
Computer Science & Engineering-Cyber Security
Lakshmi Narain College of Technology & Science
PRANJUL TIWARI
6264448231	
After Holi 
2nd Year
[19/03/24, 5:23:35 PM] annu❤️: Ok sir
[19/03/24, 5:28:39 PM] kp sir: Allotted pls check it is fresh data, we want proper response
[19/03/24, 5:41:32 PM] kp sir: Arpana Anchal allotted
[19/03/24, 5:47:28 PM] ~ Mahi: ADITI SINGH
	Technocrats Institute of Technology & Science
	9098557971
MCA
1st year
	will come 24 march
indrapuri
[19/03/24, 5:50:18 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
PRALAY SINGH NEWRE	8982035826	
3April
[19/03/24, 5:50:40 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	SURAJ KUMAR	
7739947288	
24march c,c++
[19/03/24, 5:50:54 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
JAI PARKASH	
8083362206	1april + vishal
[19/03/24, 5:52:28 PM] kp sir: Shilpa allotted
[19/03/24, 5:52:43 PM] ~ Chauhan Shilpa: Thankyou sir
[19/03/24, 5:59:01 PM] annu❤️: AAKASH YADUWANSHI
Lakshmi Narain College of Technology
9770509928	
Python 	
Before Holi
[19/03/24, 6:07:41 PM] annu❤️: ABHAY KATRE	
Lakshmi Narain College of Technology
9109715429	
FSD	 Will Come 
Inform himself 
1st Year MCA
[19/03/24, 6:11:14 PM] ~ Mahi: DEVESH KUMAR	Technocrats Institute of Technology & Science
	8543957626
	Fsd	MCA 1st year
will think April end
[19/03/24, 6:18:00 PM] annu❤️: ABHINAV SHARMA
Lakshmi Narain College of Technology
7869469460	
Cc++	
In April 
1st Year
[19/03/24, 6:18:24 PM] ~ Mahi: IMRAN KHAN
	Technocrats Institute of Technology & Science
	6265409033	
MCA 1st yaer
Fsd
	will think after eid
[19/03/24, 6:18:32 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
KOMAL SINGH BAGHEL	8982952112	
april 1week
[19/03/24, 6:21:54 PM] annu❤️: ABHINAV TIWARI
Lakshmi Narain College of Technology
9302313510	
FSD	
7 April
1st Year MCA
[19/03/24, 6:29:00 PM] annu❤️: Indrapuri
[19/03/24, 6:29:58 PM] ~ Mahi: ANKIT GAVATIYA
	Technocrats Institute of Technology & Science
	7879133607	
Fsd
 MCA 1st year
	will come 21 march
[19/03/24, 6:30:50 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
RAUSHAN KUMAR	
7061294673	
29 March
[19/03/24, 6:41:41 PM] annu❤️: ADARSH SAHU	
Lakshmi Narain College of Technology
9098595554	
FSD + Python 	
23 March
Indrapuri
1 Year MCA
[19/03/24, 6:45:19 PM] ~ Chauhan Shilpa: Name of Student:-SONAM
College name:-Bansal College of Engineering
Contact no:-9685299584
Branch:-Computer Science & Engineering
Expected Date of Visit:- will think
[19/03/24, 6:54:49 PM] ~ Mahi: KUMAR SATYAM
	Technocrats Institute of Technology & Science
	8541984707
Fsd MCA 1st year
	will come 20 mrch
chetak
[19/03/24, 7:02:28 PM] annu❤️: AKASH UPADHYAY
Lakshmi Narain College of Technology
7909676759	
FSD	
In April 
1 Year MCA
[19/03/24, 7:04:31 PM] ~ Chauhan Shilpa: Name of Student:-VIVEK KUMAR SHAH
College name:-Lakshmi Narain College of Technology
Contact no:-9174111170
Branch:-Computer Science & Engineering-Artificial Intelligence and Machine Learning
Expected Date of Visit:- will come 10 April
[19/03/24, 7:19:50 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
SAKSHI KANERIYA	
9826648764
	27 March (chetak)
[19/03/24, 7:28:18 PM] ~ Mahi: NEHA PARWEEN
	Technocrats Institute of Technology & Science
	9113433704	
fsd		 MCA 1st year
will come april end
[20/03/24, 12:43:43 PM] annu❤️: B.Tech	
Computer Science & Engineering-Cyber Security	
Lakshmi Narain College of Technology & Science
SHASHANK PRABHAT
8210349515	
Will think 	Java 
2nd Year
[20/03/24, 1:54:18 PM] annu❤️: Coming today indrapuri
[20/03/24, 2:26:40 PM] kp sir: MCA KA DATA PAR HOGYAI KYA CALLING
[20/03/24, 2:39:20 PM] Neha mam e.c: Kissike prospect nahi ban rahe kya
[20/03/24, 2:41:27 PM] kp sir: Anchal Jabalpur par karrahi hooo .
[20/03/24, 2:53:33 PM] anchal e.c: Hn sir
[20/03/24, 2:53:53 PM] anchal e.c: Evening me MCA data pr calling krugi
[20/03/24, 2:58:22 PM] annu❤️: Electrical & Electronics
Engineering	Lakshmi Narain College of Technology	
SARTHAK GUPTA
7898660847	
In April 
Indrapuri
4th Year
[20/03/24, 3:52:03 PM] ~ Mahi: ni sir baki h abhi
[20/03/24, 3:52:49 PM] ~ Mahi: morning me kiye to not anwser hue eveing me krunge unko
[20/03/24, 3:53:13 PM] ~ Mahi: Oriental Institute of Science & Technology
	KHUSHI SHUKLA
	9109459424
3rd year
		will come 24 march.
chetak
[20/03/24, 3:57:30 PM] ~ Mahi: Oriental Institute of Science & Technology
	MANAS MITRA
	9630784785	
3rd year 
CRT
	will think after holi
[20/03/24, 4:01:37 PM] annu❤️: Mechanical Engineering
Technocrats Institute of Technology [Excellence]
ANKIT SINGH RAJPOOT
8770520056	
Java , Python
Inform himself In April 
	indrapuri 
4th Year
[20/03/24, 4:14:54 PM] ~ Mahi: Oriental Institute of Science & Technology
	PRASHANT DHAKAD
	9479955178	
CRt 
3rd year
	will come 21 march 
chetak
[20/03/24, 4:39:47 PM] kp sir: Sabko data dediyaa hai pls check
[20/03/24, 4:41:59 PM] ~ Chauhan Shilpa: Name of Student:-PRADEEP KUMAR YADAV
College name:-IES's College of Technology
Contact no:-7061731954
Branch:-Electrical & Electronics Engineering
Expected Date of Visit:- will come 12 April
[20/03/24, 5:03:29 PM] anchal e.c: MCA
RAVI	
Technocrats Institute of Technology [Excellence]	
8435910170
will come 23 march ‎<This message was edited>
[20/03/24, 5:10:13 PM] ~ Chauhan Shilpa: Name of Student:-CHANDAN KUMAR YAJEE
College name:-NRI Institute of Information Science & Technology
Contact no:-7370057723
Expected Date of Visit:- will come 24 march
[20/03/24, 5:17:31 PM] annu❤️: AMAR KUMAR SAHU
Lakshmi Narain College of Technology
9516359887	
FSD + Python 
Indrapuri 	
With friend Adarsh Sahu 
1st Year MCA
[20/03/24, 5:26:56 PM] ~ Mahi: ABHINAV SINGH
	Technocrats Institute of Technology [Excellence]	7869708127	
MCA 1st year
will come 24march
[20/03/24, 5:36:12 PM] ~ Deepali coding: 1	ARAVIND KUMAR GUPTA	Technocrats Institute of Technology [Excellence]	7509066316 come after holi
[20/03/24, 5:44:22 PM] annu❤️: SAURAV KUMAR
Technocrats Institute of Technology & Science
6207841176	
Indrapuri 	
24 March
1st Year MCA
[20/03/24, 5:48:13 PM] annu❤️: SHEETAL MALVIYA
Technocrats Institute of Technology & Science
7470665783	
Web development 
Chetak 	
Inform himself 
1st Year MCA
[20/03/24, 5:56:36 PM] ~ Mahi: AKANKSHA SINGH
	Technocrats Institute of Technology [Excellence]
	7999756647	
FSd		
MCA 1st year
will come 21 march with frind Aditya dhurway
chetak ‎<This message was edited>
[20/03/24, 6:06:44 PM] anchal e.c: MCA
SAMEER HUMANE
	Technocrats Institute of Technology [Excellence]
	9179520172	
10 April indrapuri ‎<This message was edited>
[20/03/24, 6:12:30 PM] ~ Deepali coding: 10	BHUMIKA NAMDEV	Technocrats Institute of Technology [Excellence]	9893360047 come after holi chetak
[20/03/24, 6:13:36 PM] ~ Mahi: AKSHAY SHARMA
	Technocrats Institute of Technology [Excellence]	
7067202710	
fsd ds		
after holi
[20/03/24, 6:25:04 PM] annu❤️: TANYA SINGH
Technocrats Institute of Technology & Science
9399473442	
SQL	
Chetak
After Holi 
1st Year MCA
[20/03/24, 6:34:59 PM] kp sir: Tumhare kam ku nikal Rahe prospects
[20/03/24, 6:35:49 PM] ~ Deepali coding: Sir mca pr start kiya hai call karna
[20/03/24, 6:36:16 PM] ~ Deepali coding: Uss pr ban rhe hai abhi
[20/03/24, 6:39:46 PM] annu❤️: VIKAS SHARMA
Technocrats Institute of Technology & Science
6264145386	
Chetak 	
After Holi 
1st Year MCA
[20/03/24, 6:46:45 PM] ~ Deepali coding: 17	GAJENDRA LODHI	Technocrats Institute of Technology [Excellence]	7772808253		come after holi chetak
[20/03/24, 6:48:05 PM] ~ Chauhan Shilpa: YASH PATHAK	NRI Institute of Information Science & Technology	7869110073
Will come April first week ‎<This message was edited>
[20/03/24, 6:57:45 PM] anchal e.c: CS
TIT college
Suraj ahirwar
8643000681
Will 27 march ⭐
With 4 friend 
Indrapuri ‎<This message was edited>
[20/03/24, 6:59:34 PM] anchal e.c: MCA
SHIVAM AMRUTE
	Technocrats Institute of Technology [Excellence]	
8982657485		
	after holi 
	indrapuri ‎<This message was edited>
[20/03/24, 7:04:30 PM] ~ Deepali coding: 26	JITENDRA GADEKAR	Technocrats Institute of Technology [Excellence]	8965864851 		come 22 march indrapuri
[20/03/24, 7:14:48 PM] ~ Deepali coding: 25	ICHCHHA KHARE	Technocrats Institute of Technology [Excellence]	9302149866		come 3 April indrapuri
[20/03/24, 7:20:46 PM] ~ Deepali coding: Name vidhi meena
College bansal
Year MBA student
Number 9893512603
Come 21 March chetak
[20/03/24, 7:31:18 PM] ~ Mahi: Sagar Institute of Research & Technology
	AMAN MANDAL
	6202234585
	will think april
‎[21/03/24, 11:29:16 AM] Neha mam e.c: IMG_6670.MP4 ‎document omitted
[21/03/24, 11:29:22 AM] Neha mam e.c: Set as a status
[21/03/24, 12:38:10 PM] ~ Chauhan Shilpa: Name of Student:-VIVEK YADAV
College name:-NRI Institute of Information Science & Technology
Contact no:-8218778532
Expected Date of Visit:- will think
[21/03/24, 12:58:58 PM] ~ Mahi: Truba Institute of Engg. & Information Technology, GANDHI NAGAR, BHOPAL
	ADITI PATHAK
	8103708028
3rd year
	will come 23 march
chetak
‎[21/03/24, 1:21:58 PM] Harsh sir tl: ‎audio omitted
[21/03/24, 2:43:27 PM] kp sir: Indeapuri team calling start hogyai MCA par yaa nahi
[21/03/24, 2:45:31 PM] kp sir: Arpana data allotted
‎[21/03/24, 2:46:25 PM] Neha mam e.c: IMG_6680.MP4 ‎document omitted
[21/03/24, 2:49:01 PM] ~ Mahi: ok sir
[21/03/24, 2:49:33 PM] ~ Mahi: Patel College of Science & Technology	
SANJEET KUMAR	
9297616443
3rd year
	will think april 1st
 week
[21/03/24, 2:53:35 PM] kp sir: Kasim mca data shared
[21/03/24, 2:56:27 PM] kasim k: ok sir
[21/03/24, 3:03:59 PM] ~ Chauhan Shilpa: Ho gai hai sir
[21/03/24, 3:04:26 PM] anchal e.c: Yes sir
[21/03/24, 3:10:53 PM] ~ Mahi: Patel College of Science & Technology
	SOHAIL KHAN	
7281975797	
3rd year
will come after eid
chetak
[21/03/24, 3:12:23 PM] anchal e.c: MCA
	SHOEB AHMED QURESHI	
Technocrats Institute of Technology [Excellence]	
8770741316	
	after Eid will come
 mp nagar ‎<This message was edited>
[21/03/24, 3:25:30 PM] ~ Deepali coding: Computer Science & Engineering	Oriental College of Technology	ANURAG KHARE		8817987185	will come after holi
[21/03/24, 3:31:36 PM] ~ Chauhan Shilpa: Name of Student:-DIWAN SINGH KUSHWAH
College name:-NRI Institute of Information Science & Technology
Contact no:-9009166292
Expected Date of Visit:- after holi
[21/03/24, 3:36:27 PM] anchal e.c: MCA
SUJAY SAHU	
Technocrats Institute of Technology [Excellence]	
9303573260	
		will think
[21/03/24, 4:33:18 PM] kasim k: ‎You deleted this message.
[21/03/24, 4:33:57 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	ANSH KUMAR	
8528700599
april 1 week
[21/03/24, 4:34:45 PM] kasim k: ‎You deleted this message.
[21/03/24, 4:35:02 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	SEEMA KEWTE	
8871255325	
5  april
[21/03/24, 4:57:58 PM] ~ Deepali coding: 27	JYOTI SHUKARWARE	Technocrats Institute of Technology [Excellence]	7610650351		come after holi
[21/03/24, 5:04:10 PM] anchal e.c: MCA
	TUSHAR
	Technocrats Institute of Technology [Excellence]
	8103352035
		29 March ⭐ indrapuri
[21/03/24, 5:11:03 PM] annu❤️: AKANSHA TRIPATHI	
NRI Institute of Information Science & Technology	
6265309913	
FSD 	
After Holi 	
indrapuri 
1st Year MCA
[21/03/24, 5:14:11 PM] ~ Mahi: NEERAJ PRAJAPATI	NRI
 Institute of Information Science & Technology
	9171855941
	fsd		 
MCA 1st year
will think march end
chetak
[21/03/24, 5:20:25 PM] ~ Mahi: NIKHIL SHUKLA	
NRI Institute of Information Science & Technology
	9162315931
	fsd		 MCA
will think after april
[21/03/24, 5:25:58 PM] anchal e.c: MCA
	VAISHAL
I	Technocrats Institute of Technology [Excellence]
	8815739208	
	will think
[21/03/24, 5:28:08 PM] ~ Chauhan Shilpa: Name of Student:-ravi pawar 
College name:-NRI Institute of Information Science & Technology
Contact no:-7987318515
Expected Date of Visit:- April first week
[21/03/24, 5:38:22 PM] anchal e.c: MCA
	VIJAY DUBEY
	Technocrats Institute of Technology [Excellence]	
9179337506	
	after holi
 indrapuri
[21/03/24, 5:40:56 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	BABLU KUMAR	
8825138188	
after holi  29 march
[21/03/24, 5:44:24 PM] annu❤️: ANCHAL YADAV	
NRI Institute of Information Science & Technology	
7237094491	
DSA	
Will think 
1st Year MCA
[21/03/24, 5:48:26 PM] ~ Mahi: PARAS AWASTHI	
NRI Institute of Information Science & Technology
	7999775006	
Fsd
MCA
Fsd		will come 22march
chetak
[21/03/24, 6:00:06 PM] anchal e.c: MCA
	VIKASH KUMAR GUPTA	Technocrats Institute of Technology [Excellence]	
9798515891	
	first week of April ⭐
 Indrapuri ‎<This message was edited>
[21/03/24, 6:01:06 PM] annu❤️: ANURAG LODHI	NRI
Institute of Information Science & Technology
8349524031	
CRT 	
20 April
1st Year MCA
[21/03/24, 6:05:25 PM] kasim k: ANAND	
Sagar Institute of Research & Technology	
7869687038	
2nd april
[21/03/24, 6:05:55 PM] kasim k: 7649050949
alternative number
[21/03/24, 6:13:31 PM] annu❤️: ARPAN TAKLODEY	
NRI Institute of Information Science & Technology	
8989664432	
Will Come 	
In April 
1st Year MCA
[21/03/24, 6:23:46 PM] ~ Chauhan Shilpa: Name of Student:-UJJAWAL SHUKLA 
College name:-NRI Institute of Information Science & Technology
Contact no:-7047811705
Expected Date of Visit:- 5 April
[21/03/24, 6:43:36 PM] ~ Mahi: PHOOL KUMAR
	NRI Institute of Information Science & Technology	
8651532640
	ds		 MCA
will think end mRch
[21/03/24, 7:06:25 PM] ~ Deepali coding: ‎This message was deleted.
[21/03/24, 7:06:40 PM] ~ Deepali coding: 53	RAHUL YADAV	Technocrats Institute of Technology [Excellence]	7879127173	web development 	will think
[21/03/24, 7:07:24 PM] ~ Deepali coding: 50	PRIYANSHU SINGH	Technocrats Institute of Technology [Excellence]	9351015350		come after holi
[21/03/24, 7:17:28 PM] ~ Chauhan Shilpa: Name of Student:- SITA SONI
College name:-NRI Institute of Information Science & Technology
Contact no:-7999951282
Expected Date of Visit:- 23 March
[21/03/24, 7:22:23 PM] kasim k: AMAN KUMAR	
Sagar Institute of Research & Technology	
7480850085	
april 1week
[22/03/24, 12:30:01 PM] ~ Chauhan Shilpa: Name of Student:- KHILESHVAR SABLE
College name:-NRI Institute of Information Science & Technology
Contact no:-8819840795
Expected Date of Visit:- 5 April
[22/03/24, 12:31:36 PM] ~ Mahi: Sagar Institute of Research & Technology
	ABHIMANYU KUMAR
	9304341861	
will think
[22/03/24, 12:34:00 PM] anchal e.c: Electrical & Electronics Engineering
	Sagar Institute of Research & Technology	
SACHIN SAHU
	9993412721
	will think
[22/03/24, 12:50:34 PM] kasim k: Name - devyanshu 
Number - 7224088970
college- JnCT
Will come for registration - april before batch + ashu
[22/03/24, 12:51:26 PM] ~ Deepali coding: Name - Monika 
Branch cs
Year final year
College - NRI
Number 7489990197
Visit date - come after holi
[22/03/24, 1:41:48 PM] ~ Chauhan Shilpa: Name of Student:- KINJAL PATEL
College name:-NRI Institute of Information Science & Technology
Contact no:-7828058578
Expected Date of Visit:- after holi
[22/03/24, 1:42:46 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Radha Raman Institute of Technology & Science
	AVNISH KUMAR
	6206775298	
After holi will come
[22/03/24, 3:46:09 PM] kp sir: Jinka data finish hogya hai wo 2 year par call karle apne , aakar deta huun main 4.30PM tak
[22/03/24, 4:57:33 PM] kasim k: B.Tech	Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
RUPESH KUMAR	
7321861307	
april 1 week data science
[22/03/24, 5:14:37 PM] annu❤️: B.Tech	
Artificial Intelligence and Data Science
Lakshmi Narain College of Technology	
ADITYA JAIN	9406550008	
In April 	
Chetak 
2nd Year
[22/03/24, 5:15:43 PM] ~ Mahi: PRIYANSHU THAKUR
	NRI Institute of Information Science & Technology
	7999896649
	FSd		
MCA
will think after holi
[22/03/24, 5:19:06 PM] annu❤️: B.Tech	
Artificial Intelligence and Data Science	Lakshmi Narain College of Technology
GAURAV GUPTA	6266140078	
Inform himself 	
DSA
2nd Year
[22/03/24, 5:29:25 PM] ~ Deepali coding: 7	AYUSH THAKUR	Technocrats Institute of Technology [Excellence]	8718950708	will come 2 April indrapuri
[22/03/24, 5:31:20 PM] anchal e.c: MCA 
	VINAY NANDA
	Technocrats Institute of Technology [Excellence]	
9575640565
	will think
[22/03/24, 5:33:32 PM] kp sir: Deepali alloted
[22/03/24, 5:36:18 PM] kasim k: ADARSH MISHRA	
Sagar Institute of Research & Technology	
7999308687
	2April
[22/03/24, 5:42:49 PM] annu❤️: B.Tech	
Computer Science & Engineering-Internet of Things and Cyber Security Including Block Chain Technology
Lakshmi Narain College of Technology	
ABHAY PAROUHA
9302942815	
1 April
Chetak 
2nd Year
[22/03/24, 5:43:31 PM] kp sir: Anushree data mca allotted
[22/03/24, 5:44:13 PM] ~ Chauhan Shilpa: Name of Student:- MD MAHTAB
College name:-NRI Institute of Information Science & Technology
Contact no:-8405896068
Expected Date of Visit:- after Eid
[22/03/24, 5:48:14 PM] kp sir: Anchal data allotted
[22/03/24, 5:48:48 PM] ~ Deepali coding: 35	MUNNA	Technocrats Institute of Technology [Excellence]	7440862067	come after holi 27 march
[22/03/24, 5:52:49 PM] annu❤️: 82	
LOKESH SHIVNANI
Sagar Institute of Research & Technology
7440673873	
DSP 
In April 
1st Year MCA
[22/03/24, 5:57:16 PM] annu❤️: 83	
LUCKY PATEL	
Sagar Institute of Research & Technology	7879702313	
Web -D	
10 April
1st Year MCA
[22/03/24, 5:57:50 PM] kp sir: Deepali call nahi horahe kya
[22/03/24, 5:58:53 PM] ~ Deepali coding: Sir me ringing pr kar rhi phale
[22/03/24, 5:59:02 PM] ~ Deepali coding: Fr new pr karugi
[22/03/24, 5:59:39 PM] anchal e.c: SHASHANK SHRIVASTAVA
	Sagar Institute of Research & Technology
	6264338229	
 		April will come
MCA
[22/03/24, 6:09:49 PM] anchal e.c: SHITAL KUMARI
	Sagar Institute of Research & Technology
	6201174727	
	Not confirm date to visit 
MCA
[22/03/24, 6:10:28 PM] ~ Mahi: RAHUL NEKYA	
NRI Institute of Information Science & Technology
	8871882934		
MCA
	will think
[22/03/24, 6:17:28 PM] ~ Mahi: RAO DEVANSH KOURAV
	NRI Institute of Information Science & Technology	
8305384034
MCA
	fsd ds	
	will come 2 april
Chetak
[22/03/24, 6:21:51 PM] ~ Chauhan Shilpa: Name of Student:- DIMPLE
College name:-Oriental Institute of Science & Technology
Contact no:-9301039335
Expected Date of Visit:- 31 march
[22/03/24, 6:32:46 PM] annu❤️: 91	
MOHD AMAN	
Sagar Institute of Research & Technology
9984473128	
Web - D	
After Holi 
1st Year MCA
[22/03/24, 6:37:46 PM] ~ Deepali coding: 7	ASHISH KUTAR	Sagar Institute of Research & Technology	7389836349		come after holi chetak
[22/03/24, 6:52:43 PM] annu❤️: 94	
NEERAJ TYAGI	
Sagar Institute of Research & Technology
6261293367	
Web - D 	
5 April	
Indrapuri 
1st Year MCA
[22/03/24, 6:55:44 PM] ~ Mahi: SAKSHI GUPTA
	NRI Institute of Information Science & Technology	
9131077232	
Fsd	
	will come 30 mrch
chetak
[22/03/24, 6:55:59 PM] ~ Deepali coding: 13	AYUSHI SONI	Sagar Institute of Research & Technology	7470335275		come 31 march
[22/03/24, 6:59:44 PM] ~ Mahi: Sagar Institute of Research & Technology
	MUSKAN ROHE
	9424509934	
will come after may 
chetak
[23/03/24, 2:03:39 PM] Harsh sir tl: Team whats happening subha se calling nai horahi h Yaa response nai araha hai ???
[23/03/24, 2:56:46 PM] annu❤️: Computer Science & Engineering	
IES's College of Technology	
SHIVAM RAI
7273056420	
CRT Batch 
Indrapuri 
After Holi 
4th Year
[23/03/24, 3:37:01 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology	
KETAN KUMAR VISHWAKARMA
9174123100	
Will think 
Inform himself 
2nd Year
[23/03/24, 3:50:51 PM] Harsh sir tl: @916263594069 @919424704675  aap off pr hai aapne kisko inform kiya tha ???
[23/03/24, 4:24:05 PM] ~ Chauhan Shilpa: Name of Student:- HARISH SAHU
College name:-Oriental Institute of Science & Technology
Contact no:-8463824904
Expected Date of Visit:- 3 April mp nagar
[23/03/24, 4:39:39 PM] ~ Chauhan Shilpa: Name of Student:- DIPU KUMAR OJHA
College name:-Oriental Institute of Science & Technology
Contact no:-9761576891
Expected Date of Visit:- will come 28 March
[23/03/24, 4:47:40 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal College of Engineering
	SAKSHI AHIRWAR	
9301836614	
27-28march
[23/03/24, 4:48:05 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal College of Engineering ARZOO ODE	
8962367255	
will think obdullaganj
[23/03/24, 5:01:15 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal College of Engineering
RACHNA UPADHYAY	
8817819070	
29 March
[23/03/24, 5:52:15 PM] ~ Chauhan Shilpa: Name of Student:- PRAYANSH JAIN
College name:-Oriental Institute of Science & Technology
Contact no:-7869843789
Expected Date of Visit:- after holi
[23/03/24, 5:58:17 PM] kp sir: Anushree alloted
[23/03/24, 5:59:15 PM] annu❤️: Okk sir
[23/03/24, 6:01:28 PM] ~ Chauhan Shilpa: Name of Student:-PRAJWAL BHOYTE
College name:-Oriental Institute of Science & Technology
Contact no:-9691558499
Expected Date of Visit:- 1 April
[23/03/24, 6:32:57 PM] kasim k: 58	ANISHA KOURAV	
Lakshmi Narain College of Technology	
9691275023	
april 1week
[23/03/24, 6:39:36 PM] annu❤️: 117
RITIK KUMAR SAHU
Oriental Institute of Science & Technology
8434391370	
DSA 	
18 April
1st Year MCA
[23/03/24, 6:39:37 PM] annu❤️: 120	
RIYA RAJ	
Oriental Institute of Science & Technology
6200899483	
Web - D	
Will think 
1st Year MCA
[23/03/24, 6:48:44 PM] annu❤️: 122	
ROHIT YADAV	
Oriental Institute of Science & Technology
8418018966	
FSD	
In April 	
Indrapuri 
1st Year MCA
[23/03/24, 6:54:46 PM] annu❤️: 123	
RUCHI JAWARIYA
Oriental Institute of Science & Technology
8269756487	
DSP	
Will think 
1st Year MCA
[23/03/24, 7:01:08 PM] ~ Chauhan Shilpa: Name of Student:-POOJA KUMARI
College name:-Oriental Institute of Science & Technology
Contact no:-7781022852
Expected Date of Visit:- will think
[23/03/24, 7:09:19 PM] ~ Chauhan Shilpa: Name of Student:-PIYUSH RANJAN
College name:-Oriental Institute of Science & Technology
Contact no:-9693547801
Expected Date of Visit:- will come 12 April
[23/03/24, 7:11:45 PM] kasim k: ANJANA KUMARI SINGH	
Lakshmi Narain College of Technology	
8972704357	
6/7april
[23/03/24, 7:21:01 PM] ~ Chauhan Shilpa: Name of Student:-PARAS RAGHUWANSHI
College name:-Oriental Institute of Science & Technology
Contact no:-8871636527
Expected Date of Visit:- 7 April
[24/03/24, 12:32:53 PM] Harsh sir tl: Kesa response hai team aaj ka ???
[24/03/24, 12:45:41 PM] Harsh sir tl: @919424704675 @916263594069 @916260034224 @919244985834either my message is not visible to you or you are taking it very lightly …. ‎<This message was edited>
[24/03/24, 12:46:26 PM] ~ Mahi: Sagar Institute of Research & Technology
	SUYASH SHUKLA
	9993069654	
will think after holi
[24/03/24, 12:47:24 PM] ~ Mahi: kuch calls uth rhe h kuch nii
[24/03/24, 12:47:34 PM] Harsh sir tl: Ok
[24/03/24, 12:48:38 PM] Harsh sir tl: Rest of you aap logo ko personally puchna padega ?
[24/03/24, 12:49:16 PM] anchal e.c: Not answering me h or kuch ne mna kiya h
[24/03/24, 12:49:22 PM] anchal e.c: Prospect nai bne abhi
[24/03/24, 12:49:31 PM] Harsh sir tl: Ok
[24/03/24, 12:53:48 PM] ~ Mahi: Sagar Institute of Research & Technology
	LALIT VISHWAKARMA
	7223975510	
will think april 15
[24/03/24, 12:56:41 PM] anchal e.c: SHUBHAM KUMAR	Sagar 
Institute of Research & Technology
	9661253409
	not confirm date to visit
[24/03/24, 2:58:10 PM] anchal e.c: SHUBHAM MEENA
	Sagar Institute of Research & Technology
	7879972119
		after 1 April indrapuri
[24/03/24, 3:14:33 PM] ~ Mahi: SANSKAR SAHU
	NRI Institute of Information Science & Technology
	9981431916	
fsd		
MCA
will think higly intr not cnfirm date to visit
[24/03/24, 3:27:07 PM] ~ Deepali coding: 24	DIVYA JAIN	Sagar Institute of Research & Technology	7354676405	will come April first week
[24/03/24, 3:30:50 PM] ~ Mahi: SHIVAM KUMAR
	NRI Institute of Information Science & Technology
	8210671205
	Fsd	
MCA
	will come 27 march
indrapuri
[24/03/24, 4:01:36 PM] ~ Chauhan Shilpa: Name of Student:-KAUSHAL KUMAR
College name:-Scope College of Engineering
Branch :-Computer Science & Engineering
Contact no:-8340753566
Expected Date of Visit:- will think
[24/03/24, 5:10:43 PM] ~ Chauhan Shilpa: Name of Student:-HARSHIT SINGH SISODIYA
College name:-Oriental Institute of Science & Technology
Contact no:-9098426144
Expected Date of Visit:- 2 April ‎<This message was edited>
[24/03/24, 5:15:43 PM] ~ Chauhan Shilpa: Name of Student:-HIMANSHU GURJAR
College name:-Oriental Institute of Science & Technology
Contact no:-7694831604
Expected Date of Visit:- 7 April
[27/03/24, 12:24:51 PM] annu❤️: 130	
SANJAY VISHWAKARMA
Oriental Institute of Science & Technology
9981702721	
Indrapuri 	
7 April
2nd Year
[27/03/24, 12:34:18 PM] anchal e.c: Name of Student: Aniket
College name: Oriental 
Contact no: 9407869995
Branch: EC
Year: PO
Expected Date of Visit: will call
[27/03/24, 12:34:33 PM] ~ Mahi: AKANKSHA SINGH
	Oriental Institute of Science & Technology
	9589327197
	Ds		
MCA
will come 2 april
chetak
[27/03/24, 12:36:36 PM] ~ Deepali coding: Name of Student: Faraz
College name: Trinity 
Contact no:  9406548714
Branch: cs data science 
Year: 2
Expected Date of Visit: will come after 15 April
[27/03/24, 12:43:11 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[27/03/24, 12:52:30 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[27/03/24, 1:02:44 PM] ~ Mahi: NRI Institute of Information Science & Technology
	ANURAG KUSHWAHA
	9098294793	
will come 31 march
Indrapuri
[27/03/24, 1:10:41 PM] annu❤️: 131	
SANSKAR KURMI	
Oriental Institute of Science & Technology	8819930095	
FSD
In April 
2nd Year
[27/03/24, 1:14:40 PM] ~ Mahi: AMAN KUSHWAHA
	Oriental Institute of Science & Technology
	8269743745	
Fsd,Ds		
will come 28 mrch
indrapuri
[27/03/24, 1:47:02 PM] anchal e.c: Name of Student: Priyanshu 
College name: SIRT
Contact no: 9399108535
Branch: CSE
Year: 3RD
Expected Date of Visit: will come April
[27/03/24, 2:59:23 PM] anchal e.c: Name of Student: Vishal Pandey with friends+3
College name: TIT
Contact no: 9140001769
Branch: IT
Year: 2ND
Expected Date of Visit:  15 April
[27/03/24, 3:01:24 PM] ~ Deepali coding: Computer Science & Engineering	Technocrats Institute of Technology - Computer Science and Engineering	DHARMENDER SINGH	6397208339	mp nagar come 10 april
[27/03/24, 3:45:24 PM] annu❤️: 147	
SHIVAM KUMAR TIWARI
Oriental Institute of Science & Technology
6261629406	
Indrapuri 	
2 April
2nd Year MCA
[27/03/24, 4:14:57 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[27/03/24, 4:26:16 PM] ~ Chauhan Shilpa: ‎This message was deleted.
[27/03/24, 4:49:03 PM] ~ Chauhan Shilpa: Name of Student:-Ishita Vishwakarma
College name:-jnct 
Branch :-Computer Science & Engineering
Contact no:- 9329212441
Expected Date of Visit:- 15 April
[27/03/24, 5:09:48 PM] anchal e.c: CS
TIT college
Suraj ahirwar
8643000681
Will 27 march ⭐
With Ram Vishal Suraj sahu
Indrapuri
[27/03/24, 5:48:53 PM] ~ Chauhan Shilpa: Name of Student:-DIKSHA PAWAR
College name:-Lakshmi Narain College of Technology
Contact no:-9770772342
Expected Date of Visit:- April first week
[27/03/24, 5:49:42 PM] ~ Chauhan Shilpa: Name of Student:-NITIN SEN
College name:-Oriental Institute of Science & Technology
Branch :-Computer Science & Engineering
Contact no:-7879048141
Expected Date of Visit:- 31 march
[27/03/24, 5:50:14 PM] ~ Chauhan Shilpa: Name of Student:-LOKESH VERMA
College name:-Oriental Institute of Science & Technology
Branch :-Computer Science & Engineering
Contact no:-9098923370
Expected Date of Visit:- 2 April
[27/03/24, 5:51:04 PM] ~ Chauhan Shilpa: Name of Student:-JANVI CHOUHAN with (Anjali Aman) 
College name:-Oriental Institute of Science & Technology
Branch :-Computer Science & Engineering
Contact no:-6264742309
Expected Date of Visit:- 30 march (Chetak)
[27/03/24, 5:51:40 PM] ~ Chauhan Shilpa: Name of Student:-JAIDEEP MISHRA
College name:-Oriental Institute of Science & Technology
Branch :-Computer Science & Engineering
Contact no:-7804070703
Expected Date of Visit:- will think
[27/03/24, 6:00:16 PM] annu❤️: 150	
SHREYA JAIN	
Oriental Institute of Science & Technology
8989711301		
9 April
2nd Year MCA
[27/03/24, 6:38:55 PM] anchal e.c: VARTIKA BINJOLIY
A	Sagar Institute of Research & 
Technology
	9752139332	
	not confirm date to visit
[27/03/24, 6:48:38 PM] ~ Deepali coding: 34	ISHIKA SHARMA	Sagar Institute of Research & Technology	6269348821		will come 5 april indrapuri
[27/03/24, 6:49:57 PM] annu❤️: 9826964448 
Anil 
2 April 
Cc++
[27/03/24, 7:14:05 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
RITU KUMARI RAI	
7321820191	
april 1 week c,c++  (indrpuri)
[27/03/24, 7:14:22 PM] kasim k: B.Tech	
Computer Science & Engineering	
Radha Raman Institute of Technology & Science	
NABI SARWAR
	8541046691	
after eid
[27/03/24, 7:16:35 PM] kasim k: Computer Science & Engineering	
Technocrats Institute of Technology & Science	
BRIJENDRA KUSHWAHA	8962721878
9april
[27/03/24, 7:17:30 PM] kasim k: Computer Science & Engineering	
Patel College of Science & Technology	
UZAIR ALI KHAN	
7905256489
17 april
[27/03/24, 7:50:10 PM] Neha mam e.c: Aap logo ke abhi bhi visit ur registration ka kya scene hai
[27/03/24, 8:23:00 PM] Neha mam e.c: @918085394718 sabki kaam ki mujhe list chaiye ki april me kya scene hai sabka jaise ye log incentive ka baar baar ek dusre se din baar yehi puchte rehate hai ki madam se pucho kab release karenge to aapka kaam hai ki mujhe complete report de ki april ke kya registration ka projection hai mene faltu baithaakar bhi bahut logo ko salary di hai mujhe abh kaam chaiye
[27/03/24, 8:23:03 PM] Neha mam e.c: Sabhi se
[27/03/24, 8:24:34 PM] Harsh sir tl: Definitely mam by tomorrow’s eve ill submit there responses and projections for upcoming months
[27/03/24, 8:27:00 PM] Neha mam e.c: Incentive ke karan ye log kaam nahi kar paa rahe to bhi clear Karen to apan bhi team dekhna suru karen
[27/03/24, 8:27:32 PM] Harsh sir tl: For sure mam
[27/03/24, 8:28:09 PM] Neha mam e.c: ‎This message was deleted.
[28/03/24, 1:29:36 PM] ~ Mahi: AMAN SINHA
	Oriental Institute of Science & Technology	
9117594062
	fsd		
MCA
will come 4 april
[28/03/24, 1:32:38 PM] ~ Mahi: will come todat with frinds
indrapuri
[28/03/24, 1:52:08 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal College of 
Engineering	
SURYANSH RAGHUWANSHI	9893813717	
1 April ( indrpur)
[28/03/24, 1:58:17 PM] ~ Deepali coding: Come with 2 friends Saad nd Shoaib after 15 april
[28/03/24, 2:33:45 PM] Harsh sir tl: Team as discussed yesterday ill be needing everyone’s responses for april and upcoming months in my personal DM before 4:00 pm
[28/03/24, 2:37:08 PM] anchal e.c: Ok
[28/03/24, 2:37:10 PM] anchal e.c: Sir
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology
KRISHNAKANT WAGHMARE
9685967279	
2 April	
Chetak 
FSD
2nd Year
[28/03/24, 4:15:58 PM] Harsh sir tl: Your name
Student Name: 
Admission month : [Admission Date]
Course/ Language : [Insert course /Language ]
[28/03/24, 4:16:26 PM] Harsh sir tl: Use this format and share it in my personal DM
[28/03/24, 4:25:49 PM] annu❤️: B.Tech	
Computer Science & Engineering-Internet of Things and Cyber Security Including Block Chain Technology
Lakshmi Narain College of Technology
RISHIKESH NAMDEV
9755900273	
Will think 	
Chetak 
2nd Year
[28/03/24, 4:27:59 PM] ~ Chauhan Shilpa: Name of Student:-DIVYA RAJ
College name:-Lakshmi Narain College of Technology
Contact no:-8409910112
Expected Date of Visit:- 31 march
[28/03/24, 4:52:21 PM] ~ Chauhan Shilpa: Name of Student:-DIVYANSHU KADVE
College name:-Lakshmi Narain College of Technology
Contact no:-9174196387
Expected Date of Visit:- 1 April
[28/03/24, 4:56:14 PM] anchal e.c: AJAY PAWA
R	Oriental Institute of Science & Technology
	7898674162	
MCA
		5 April
	Mp nagar
[28/03/24, 4:57:37 PM] ~ Deepali coding: 37	KHUSHBOO	Sagar Institute of Research & Technology	7489601738		will think
[28/03/24, 4:58:00 PM] ~ Deepali coding: 38	KHUSHI SAHU	Sagar Institute of Research & Technology	9752131259		will think
[28/03/24, 5:01:03 PM] anchal e.c: ‎This message was deleted.
[28/03/24, 5:02:21 PM] anchal e.c: RAMESHWAR DAYAL RAO	
Sagar Institute of Research & Technology	8085509825	
MCA		
	will think
[28/03/24, 5:03:57 PM] ~ Deepali coding: 39	KHUSHI TAMRKAR	Sagar Institute of Research & Technology	7470998209 will come 5 april
[28/03/24, 5:05:04 PM] ~ Chauhan Shilpa: Name of Student:-DIVYANSH VISHWAKARMA
College name:-Lakshmi Narain College of Technology
Contact no:-7987339290
Expected Date of Visit:- 10 April
[28/03/24, 5:05:52 PM] kasim k: B.Tech	
Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence	
KUNAL	8839180522	
2april indrpuri
[28/03/24, 5:15:53 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology
PRIYANSHU SONI
9755877953	
Inform himself 	
FSD 
2nd Year
[28/03/24, 5:17:17 PM] anchal e.c: 84	AFAZAL ANSAR
I	Oriental Institute of Science & Technology
	7352476271
			MCA		
Will come 3 April with friend deepak,dipesh,sneha, Anjali
Indrapuri
[28/03/24, 5:22:16 PM] ~ Mahi: AMIT KUMAR	
Oriental Institute of Science & Technology
	9608099465
	wd with python
MCA
	will think before 31 mrch
[28/03/24, 5:31:11 PM] anchal e.c: 83	ADINA SHOAI
B	Oriental Institute of Science & Technology
McA
	7909826876
	not confirm date to visit 
Indrapuri
[28/03/24, 5:32:46 PM] ~ Mahi: ANIKET RICHHARIYA
	Oriental Institute of Science & Technology
	8463845754		
Ds
MCA
	will think 31 mrch
[28/03/24, 5:44:23 PM] ~ Mahi: ANKIT MISHRA
	Oriental Institute of Science & Technology
	9630646531	
fsd		
mCA
will come 31 mrch
[28/03/24, 5:47:59 PM] ~ Deepali coding: 72	NIRMAL DWIVEDI	Oriental Institute of Science & Technology	8815061036		come 1 april mp nagar				+2 friends
[28/03/24, 5:48:08 PM] annu❤️: B.Tech	
Computer Science & Engineering-Artificial Intelligence and Machine Learning	
Lakshmi Narain College of Technology
HIMANSHU KUMAR SINGH	
6287388720	
4 April	 Cc++
Indrapuri 
2nd Year
[28/03/24, 5:48:24 PM] kasim k: ANKIT KUMAR
	Lakshmi Narain College of Technology	
9110905404	
6 April(indrpuri)
[28/03/24, 5:53:45 PM] ~ Mahi: ANKIT PATIDAR	
Oriental Institute of Science & Technolog	9826855085
	Fsd
MCA
will come 2 april
chetak
[28/03/24, 5:55:58 PM] kasim k: ANKIT KUMAR JHA	
Lakshmi Narain College of Technology	
6206601056	
2april indrpuri
[28/03/24, 5:58:38 PM] ~ Chauhan Shilpa: Name of Student:-GOURAV MALVIYA
College name:-Lakshmi Narain College of Technology
Contact no :-8817532393
Expected Date of Visit:- date not confirmed
[28/03/24, 6:02:47 PM] annu❤️: KANCHAN KUMARI
Lakshmi Narain College of Technology
7050010897	
FSD 	
31 March	
Indrapuri 
2nd Year MCA
[28/03/24, 6:06:24 PM] ~ Mahi: ASHUTOSH SADH
	Oriental Institute of Science & Technology
	7000890324
	FSd
		will think 5 april
[28/03/24, 6:11:41 PM] annu❤️: KANISHKA MISHRA
Lakshmi Narain College of Technology
6264585059	
DSP	
In April 	
Indrapuri 
2nd Year MCA
[28/03/24, 6:15:49 PM] ~ Mahi: ATUL KUMAR YADAV
	Oriental Institute of Science & Technology
	8518013623			
will think after 20 april
[28/03/24, 6:19:58 PM] annu❤️: KARAN SEN	
Lakshmi Narain College of Technology
7828308898	
FSD 	
4 April	
Indrapuri 
2nd Year MCA
[28/03/24, 6:23:13 PM] ~ Mahi: AVANEESH TYAGI
	Oriental Institute of Science & Technology
	6264938117
	Ds		
will come 5 april
indrapuri
[28/03/24, 6:23:28 PM] anchal e.c: AARADHYA TIWARI	Oriental Institute of Science & Technology
	8269815819	
MCA
	29 ,31 march 
indrapuri
[28/03/24, 6:27:28 PM] Neha mam e.c: ‎This message was deleted.
[28/03/24, 6:27:38 PM] Neha mam e.c: New batch
[28/03/24, 6:28:16 PM] Neha mam e.c: Indripuri Fsd 7-8:30pm MWF—-3 april
Mp nagar data science 7-8:30 TTS. 6 April
[28/03/24, 6:28:44 PM] Neha mam e.c: Mp nagar Fsd 
Indripuri data science 
C,c++ kal batati hu
[28/03/24, 6:31:57 PM] ~ Deepali coding: Oky mam
[28/03/24, 6:32:15 PM] ~ Deepali coding: 59	MUSKAN GUPTA	Oriental Institute of Science & Technology	8871630971	come 5 april indrapuri
[28/03/24, 6:55:34 PM] annu❤️: KIRTI	
Lakshmi Narain College of Technology
79873119163	
Java 	
2 April
2nd Year MCA
[28/03/24, 7:20:02 PM] kasim k: APEKSHA YADAV	
Lakshmi Narain College of Technology	
7067623159	
31 March(indrpuri)
[28/03/24, 7:24:32 PM] annu❤️: LAXMI PATEL	
Lakshmi Narain College of Technology
8815421206	
Web - D 	
In April 	
Chetak 
2nd Year MCA
[28/03/24, 7:32:35 PM] annu❤️: MAHAK GUPTA	
Lakshmi Narain College of Technology
9302711964	
FSD 	
Inform himself 	
Indrapuri 
2nd Year MCA
[28/03/24, 7:33:23 PM] ~ Chauhan Shilpa: Name of Student:-HARDIK NAMDEV
College name:-Lakshmi Narain College of Technology
Contact no :-8827210631
Expected Date of Visit:- date not confirmed
[29/03/24, 12:27:02 PM] ~ Mahi: will come today 
chetak
[29/03/24, 1:03:25 PM] annu❤️: Ok sir
[29/03/24, 1:04:40 PM] Harsh sir tl: Team jis jis ke not answering wale students bache hue h 3-4 year ke aap din m unpr calls krte ??
[29/03/24, 1:21:43 PM] ~ Chauhan Shilpa: Name of Student:-NIKHIL TRIVEDI
College name:-Oriental College of Technology
Branch :-Computer Science & Engineering
Contact no :-9669883343
Year:- 3rd year
Expected Date of Visit:- 7 April
[29/03/24, 1:41:55 PM] anchal e.c: Will come today mp nagar evening
[29/03/24, 4:04:07 PM] ~ Chauhan Shilpa: Name of Student:-SANJANA RAJPUT
College name:-Oriental College of Technology
Branch :-Computer Science & Engineering
Contact no :-9131918558
Year:- 3rd year
Expected Date of Visit:- 3 April
[29/03/24, 4:07:27 PM] annu❤️: Artificial Intelligence and Data Science	
SAM College of Engineering & Technology
SUNIL PATEL
7067944874	
DSA	
8 April
3rd Year
[29/03/24, 4:33:07 PM] anchal e.c: ABHINAY SON
I	Oriental Institute of Science & Technology
	8602125883	
	will come 31 march
 with frd hari or harsh indrapuri
[29/03/24, 5:01:49 PM] ~ Chauhan Shilpa: Name of Student:-Amrish
College name:-Patel College
Branch :-Computer Science & Engineering
Contact no :-6201125905
Year:- 3rd year
Expected Date of Visit:- 31 march ‎<This message was edited>
[29/03/24, 5:24:47 PM] anchal e.c: Kritika
 	OIST	
IT
	8817006385	
	Not confirm date to visit
Mp nagar
[29/03/24, 5:33:11 PM] kp sir: Anchal data allotted
[29/03/24, 5:33:23 PM] kp sir: Anushree data alloted
[29/03/24, 5:37:15 PM] annu❤️: Okk sir
[29/03/24, 5:37:36 PM] annu❤️: 189	
MANMOHAN SINGH DANGI	
Lakshmi Narain College of Technology
7440285212	
Indrapuri 	
Will think 
2nd Year MCA
[29/03/24, 5:44:59 PM] anchal e.c: Ok sir
[29/03/24, 6:02:50 PM] annu❤️: 196	
MEENAKSHI CHADOKAR
Lakshmi Narain College of Technology
7909341784	
Cc++ 	
6 April	
Chetak 
2nd Year MCA
[29/03/24, 6:03:34 PM] kp sir: Sab ke pass data hai
[29/03/24, 6:03:52 PM] kp sir: Shilpa and Deepali aapko bhi dediyaa gya hai
[29/03/24, 6:04:45 PM] ~ Chauhan Shilpa: Ji sir
[29/03/24, 6:24:32 PM] kasim k: Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence	
RUDHRA SONI	
8103054579	
6 april indrpuri
[29/03/24, 6:25:04 PM] kasim k: B.Tech	
Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence	
SACHIN PANDEY	
6267488234	
4April
[29/03/24, 6:25:15 PM] annu❤️: 203	
MONIKA SAHU	
Lakshmi Narain College of Technology
9425420495	
Indrapuri 	
7 April
2nd Year MCA
[29/03/24, 6:25:26 PM] kasim k: B.Tech	 
Computer Science & Engineering	
Sagar Institute of Research & Technology Excellence	
PAYAL PRAJAPATI
	9709502102	
april 1 week
[29/03/24, 6:26:27 PM] ~ Deepali coding: 106	RITESH KUMAR	Lakshmi Narain College of Technology	7319824712		come after 5 april
[29/03/24, 6:40:48 PM] annu❤️: 206	
MUSKAN KHARE
Lakshmi Narain College of Technology
9770513076	
FSD
Inform himself 
2nd Year MCA
‎[30/03/24, 1:39:06 PM] Harsh sir tl: ‎image omitted
[30/03/24, 2:12:00 PM] Neha mam e.c: @918085394718 aaj koi phn nahi utha raha hoga
[30/03/24, 2:12:13 PM] Neha mam e.c: Kya kuch kaam ho raha hai
[30/03/24, 2:14:52 PM] Harsh sir tl: Mam team tried calling but nobody is responding everyone is busy in playing holi
[30/03/24, 2:26:11 PM] kp sir: MCA ke data par call karke dekhooo ek baar
[30/03/24, 2:26:41 PM] anchal e.c: PRACHI BATHAM
	Lakshmi Narain College of Technology
	9407569573	
	mp nagar 
	6 April
[30/03/24, 2:27:11 PM] Neha mam e.c: Abh banene lage prospect
[30/03/24, 2:28:44 PM] Harsh sir tl: mam mca pr badi mushkil se 1-1 ban rahe hai rest calls are being declined or not answering
[30/03/24, 2:38:18 PM] kasim k: ABHISHEK KUMAR SINGH	Sagar Institute of Research & Technology	
9752029233			
coming today chetak
[30/03/24, 2:39:47 PM] ~ Mahi: SHREYASH MISHRA
	Oriental Institute of Science & Technology
	7310082009
	Fsd	
	will think not cnfirm date
[30/03/24, 2:45:35 PM] ~ Deepali coding: 123	SACHIN MEENA	Lakshmi Narain College of Technology	7489231823		will come 1 april indrapuri
[30/03/24, 2:54:34 PM] ~ Deepali coding: 125	SAGAR SHARMA	Lakshmi Narain College of Technology	7869279083		will come but date not confirmed
[30/03/24, 3:06:52 PM] Neha mam e.c: +919301836614sakshi Bansal Mandeep 
Visit tomorrow or day after tomorrow
[30/03/24, 3:27:20 PM] ~ Deepali coding: 127	SAKSHAM GUPTA	Lakshmi Narain College of Technology	9691552294		will come 2 April indrapuri
[30/03/24, 3:35:43 PM] ~ Mahi: DEEPESH SAHU	O
riental Institute of Science & Technology
	7898303075
	Fsd		
will think  not cnfirm date to visit
[30/03/24, 3:42:44 PM] ~ Mahi: SIMRAN VERMA
	Oriental Institute of Science & Technology
	9669751012
	fsd	
	will think Intrested
[30/03/24, 3:50:27 PM] ~ Mahi: SNEHA SINGH	
Oriental Institute of Science & Technology
	8102497553			
will think april 5
[30/03/24, 3:51:27 PM] ~ Deepali coding: AASHI VISHWAKARMA	Bansal Institute of Science & Technology	8463896155		come 3 April chetak
[30/03/24, 3:57:43 PM] annu❤️: Artificial Intelligence and Machine Learning	
J.N. College of Technology	
DEV PRATAP SINGH
8009666132	
DSA	
8 April
[30/03/24, 3:59:32 PM] ~ Mahi: SONALI	
Oriental Institute of Science & Technology
	7803868166
	fsd		
will. come 5 april
chetak
[30/03/24, 4:18:01 PM] anchal e.c: PRANESH SHUKlA
	Lakshmi Narain College of Technology
	8878690410	
 	after 4 April
[30/03/24, 4:18:02 PM] anchal e.c: PRAVIN
	Lakshmi Narain College of Technology	7999656536	
	not confirm date of visit
[30/03/24, 4:25:49 PM] ~ Deepali coding: ARUN	Bansal Institute of Science & Technology	9685156429		will come 5 april chetak
[30/03/24, 4:28:44 PM] anchal e.c: PRATYAKSH KHARE	
Lakshmi Narain College of Technology
	9827747980	
 	5 April
[30/03/24, 4:43:15 PM] ~ Mahi: SURAJ KUSHWAHA
	Oriental Institute of Science & Technology	7247015638
	fsd
		will come after 5 april
[30/03/24, 4:52:28 PM] ~ Chauhan Shilpa: SAJID AHMAD	Patel College of Science & Technology	9852052904			after Eid (15 April )
[30/03/24, 5:01:23 PM] ~ Chauhan Shilpa: RITIK PANDAY	Patel College of Science & Technology	9589141464			date not confirmed
[30/03/24, 5:12:16 PM] annu❤️: 210	
NAMITA LILHORE
Lakshmi Narain College of Technology
7898550399	
FSD	
Inform himself 
2nd Year MCA
[30/03/24, 5:20:20 PM] annu❤️: 212	
NANDINI PATEL	
Lakshmi Narain College of Technology
7400815921	
Indrapuri 	
2 April
2nd Year MCA
[30/03/24, 5:41:58 PM] anchal e.c: PURVI TRIPATH
I	Lakshmi Narain College of Technology
	6388544746
 	after 12 April will come
[30/03/24, 5:43:55 PM] ~ Mahi: AKASH KUMAR
	Technocrat Institute of Technology
8210685127
	fsd	
	will think 1. arpil
[30/03/24, 7:52:36 PM] Neha mam e.c: Kasim 1 prospect hi bana
[30/03/24, 8:16:41 PM] kasim k: yes mam qki calls nahi uth rhaa the baki 4 will think mai gya inhone date cnfrm nahi di baki msg dal raha tha tau whatup hi block ho gyaa
[31/03/24, 12:42:09 PM] ~ Mahi: ARCHIT RAI	
Technocrat Institute of Technology
	9305119226	
fsd	
	will think after 10 april
[31/03/24, 1:20:56 PM] ~ Chauhan Shilpa: NAVEEN KUSHWAHA	Patel College of Science & Technology	7477076070			8 April
[31/03/24, 1:37:36 PM] kp sir: Prospects nahi bantahe kya
[31/03/24, 1:37:41 PM] kp sir: Kisi ke
[31/03/24, 1:38:09 PM] kp sir: Deepali ,Anchal
[31/03/24, 1:38:22 PM] ~ Mahi: ni sir
[31/03/24, 1:39:00 PM] kp sir: 2 year and MCA dono par nahi banrahe
[31/03/24, 1:39:24 PM] kp sir: 3 year and final year kisi Data par nahi banrahe
[31/03/24, 1:39:46 PM] ~ Mahi: 2nd year pr ni
[31/03/24, 1:40:07 PM] ~ Mahi: ‎This message was deleted.
[31/03/24, 1:41:59 PM] kasim k: mca ka sir data nahi second yeh per nahi ban rahe  per sunn rahe hai .
[31/03/24, 1:43:51 PM] ~ Deepali coding: Sir me enquiry pad kar rhi hu
[31/03/24, 1:44:04 PM] ~ Deepali coding: 3 April ke batch ke liye
[31/03/24, 1:44:22 PM] anchal e.c: Sir follow up pr km kr rhi hu
[31/03/24, 1:51:36 PM] kp sir: Harsh kon
[31/03/24, 1:54:24 PM] ~ Mahi: harswardhan sir tl humare
[31/03/24, 3:05:34 PM] annu❤️: 225	
NITESH SAXENA	Lakshmi Narain College of Technology
7470848795	
Java 	
27 April
Indrapuri
[31/03/24, 4:44:57 PM] anchal e.c: RAHUL BIL
e	Lakshmi Narain College of Technology
	7610327622
		5 April 
mp nagar
[31/03/24, 5:17:53 PM] ~ Mahi: ARUN SINGH
	Technocrat Institute of Technology	
6261569843
	fsd	
	will come 1 april
[31/03/24, 5:23:03 PM] anchal e.c: RAJ KAURAV	Lakshmi Narain College of Technology	8959608049	ds		will think
[31/03/24, 5:27:01 PM] ~ Mahi: ASHUTOSH TIWARI
	Technocrat Institute of Technology
	7389476280	
		will think after 10april
[31/03/24, 5:31:11 PM] ~ Deepali coding: DEEKSHA	Bansal Institute of Science & Technology	7999681936		will come after 4 april
[31/03/24, 5:31:32 PM] anchal e.c: RAJ PARLT
	Lakshmi Narain College of Technology
	9131956442	
	2 April 
indrapuri
[31/03/24, 5:32:08 PM] ~ Mahi: AYUSH RAJ
	Technocrat Institute of Technology
	9835140108
	fsd	
	will think april end
[31/03/24, 5:39:11 PM] anchal e.c: RAJNISH KUMAR
	Lakshmi Narain College of Technology
	9525964747
		31 March indrapuri
[31/03/24, 5:47:17 PM] ~ Deepali coding: DHEERAJ KUMAR YADAV	Bansal Institute of Science & Technology	9117429988		will think
[31/03/24, 6:28:56 PM] kasim k: B.Tech
Computer Science & Engineering	
Bansal College of Engineering
ABHINAV MISHRA	
9589106617	
6April
[31/03/24, 6:29:18 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal College of Engineering
AKASH BARASIYA	7089353238	
3April
[31/03/24, 6:29:36 PM] kasim k: B.Tech	
Computer Science & Engineering	
Bansal College of Engineering	
SHRADHA RAJPUT	9399079309	
15 April
[31/03/24, 6:53:10 PM] ~ Chauhan Shilpa: HEMLAL KUMAR	Patel College of Science & Technology	7320817939			10 April
[01/04/24, 12:33:46 PM] ~ Mahi: will come today indrapuri
[01/04/24, 1:03:26 PM] anchal e.c: B.Tech	Computer Science & Engineering
	Radha Raman Institute of Technology & Science
	ANKIT GAUTAM	8819957150
	2 April 
mp nagar
[01/04/24, 1:52:52 PM] ~ Mahi: HEMANT KUMAR
	Technocrat Institute of Technology	
7254882238
	fsd		
will come 2 april
[01/04/24, 2:25:04 PM] Neha mam e.c: ‎This message was deleted.
[01/04/24, 2:26:36 PM] Neha mam e.c: 3 April Mwf Fsd new batch Indripuri 7-8:30
6 April TTS data science 
7-8:30  MP nagar
8 April MWF Fsd new batch MP nagar 5:30-7
11 April TTS data science 
Indripuri 7-8:30
[01/04/24, 2:27:27 PM] Neha mam e.c: 11 April vala 5:30-7 rehaga
[01/04/24, 2:40:20 PM] kp sir: Anchal data dediyaa hai
[01/04/24, 2:40:41 PM] anchal e.c: Ok sir
[01/04/24, 2:40:58 PM] ~ Deepali coding: C& c ++
[01/04/24, 2:41:25 PM] Neha mam e.c: C,c++ MP nagar evening tak bata denge
[01/04/24, 2:41:30 PM] ~ Deepali coding: Oky
[01/04/24, 2:41:55 PM] Neha mam e.c: Acha ek bahar board ka ek pic lekar dedo
[01/04/24, 2:42:01 PM] Neha mam e.c: Deepali
[01/04/24, 2:42:13 PM] ~ Deepali coding: Konsa board mam
[01/04/24, 2:42:43 PM] Neha mam e.c: Coding thinker ka jo chai Dutta baar ke uper laga hai
[01/04/24, 2:42:53 PM] ~ Deepali coding: Oky mam
[01/04/24, 3:40:34 PM] anchal e.c: B.Tech	Computer Science & Engineering	
Lakshmi Narain College of Technology Excellence	
TAISON YADAV	9151330359	
With frd Mayank or rishi 
Will come today 
Indrapuri
[01/04/24, 3:42:29 PM] Neha mam e.c: Kitne baje aa rahe hai
[01/04/24, 3:43:01 PM] anchal e.c: Evening
[01/04/24, 3:43:02 PM] anchal e.c: Me
[01/04/24, 4:35:33 PM] ~ Deepali coding: Will come today chetak
(Oist )
[01/04/24, 4:57:56 PM] anchal e.c: Will come today mp nagar evening 7:30pm
[01/04/24, 5:00:07 PM] Neha mam e.c: Indripuri ke enquiry pad ho gya Kay
[01/04/24, 5:00:57 PM] anchal e.c: Nai ma'am thoda bacha h
[01/04/24, 5:00:59 PM] anchal e.c: Kr rhe h
[01/04/24, 5:01:01 PM] anchal e.c: Wahi
[01/04/24, 5:27:35 PM] ~ Chauhan Shilpa: Mam kuch number or bache he
[01/04/24, 5:32:30 PM] anchal e.c: GAYATRI PAKHAL
E	Bansal Institute of Science & Technology
	7999636826
	 not confirm date to visit ‎<This message was edited>
[01/04/24, 5:46:34 PM] anchal e.c: HIMANSHU KUSHWAH
	Bansal Institute of Science & Technology
	6268296889		
	3 April indrapuri
[01/04/24, 5:56:11 PM] anchal e.c: JAYANT VISHWAKARMA	
Bansal Institute of Science & Technology
	7879042144		
DS	will think
[01/04/24, 6:10:18 PM] ~ Deepali coding: Will come 6 april with 4 friends Utkarsh , Aradhya, Abhay, Sankalp 
Mp nagar for registration
[01/04/24, 6:12:31 PM] ~ Chauhan Shilpa: Welcome tomorrow with friend Ayush Jain
[01/04/24, 6:17:20 PM] ~ Deepali coding: Name-Dharmendra Kumar
College Sirt
Brach cs
Year 2 
Number  9301823743
Will come 2 April indrapuri
[01/04/24, 6:17:43 PM] anchal e.c: B.Tech	Artificial Intelligence and Data Science
	Lakshmi Narain College of Technology
	KAPIL RAWAT
	7970158365
	indrapuri 
	3 April
[01/04/24, 6:22:20 PM] ~ Chauhan Shilpa: Welcome tomorrow with friends Lakshmi Sahu
[01/04/24, 6:26:25 PM] anchal e.c: B.Tech	Computer Science & Engineering-Artificial Intelligence and Machine Learning
	Lakshmi Narain College of Technology	SHIVAM KUMAR	9110974903
 indrapuri 
 	4 April ds
[01/04/24, 6:31:48 PM] Neha mam e.c: 7 baje ke liye convenience ho gye kya
[01/04/24, 6:32:36 PM] ~ Deepali coding: Haa mene bola aap 3-4 class lo aap fr dekho kitne bje tk hostel poch rhe ho
[01/04/24, 6:32:53 PM] ~ Deepali coding: 3 students hostel ke hai 9 bje tk pochna rhega unhe
[01/04/24, 6:32:58 PM] Neha mam e.c: Are phir dimag khaenge vo
[01/04/24, 6:32:59 PM] ~ Deepali coding: Hostel
[01/04/24, 6:33:11 PM] ~ Deepali coding: Fr kya karu ab mam koi or time hai kya?
[01/04/24, 6:33:34 PM] Neha mam e.c: 1 option hai mere pass
[01/04/24, 6:33:42 PM] ~ Deepali coding: Ji bataiye
[01/04/24, 6:33:59 PM] ~ Mahi: name - Amna ali 
 98935 62064
college- safia college
will come 12 april 
chetak
[01/04/24, 6:40:44 PM] ~ Chauhan Shilpa: Will come tomorrow mp nagar
[01/04/24, 7:09:11 PM] ~ Chauhan Shilpa: Will come tomorrow mp nagar
[01/04/24, 7:45:15 PM] ~ Chauhan Shilpa: With friends devanshu panthi Ashu Patil
[01/04/24, 9:56:09 PM] Neha mam e.c: Thoda change kiya hai apan ne batch me
6/ April TTS data science. 7-8:30 Indripuri 
10/April MWF data science MP nagar 5:30-7pm
[01/04/24, 9:56:36 PM] Neha mam e.c: Abh to theek hai pls check 
Deepali 
Arpana
[01/04/24, 10:06:54 PM] ~ Mahi: yes mam
‎[01/04/24, 10:48:39 PM] Neha mam e.c: ‎image omitted
‎[01/04/24, 10:48:39 PM] Neha mam e.c: ‎image omitted
‎[01/04/24, 10:48:40 PM] Neha mam e.c: ‎image omitted
‎[01/04/24, 10:48:40 PM] Neha mam e.c: ‎image omitted
[01/04/24, 10:57:35 PM] Neha mam e.c: Set as a status
[02/04/24, 8:41:55 AM] ~ Deepali coding: Yes mam
‎[02/04/24, 10:44:01 AM] Neha mam e.c: ‎image omitted
‎[02/04/24, 10:44:02 AM] Neha mam e.c: ‎image omitted
‎[02/04/24, 10:44:02 AM] Neha mam e.c: ‎image omitted
‎[02/04/24, 10:44:03 AM] Neha mam e.c: ‎image omitted
[02/04/24, 12:10:49 PM] Neha mam e.c: Branch :- B.Tech	CS
Collge- Bansal
Name :- 	Kuldeep
Contact:- 8103035397
Expected date:- 20march
[02/04/24, 12:10:49 PM] Neha mam e.c: ravendra + vikash
[02/04/24, 12:10:50 PM] Neha mam e.c: +ankush
[02/04/24, 12:11:40 PM] ~ Deepali coding: Check kar ke batati hu mam
[02/04/24, 1:27:26 PM] ~ Deepali coding: Will come 10 april chetak for python language already visited
[02/04/24, 3:35:55 PM] ~ Deepali coding: 532	Computer Science & Engineering	Scope College of Engineering	SHIVSHEKHAR PATHAK	come 4 april chetak 		9174232327
[02/04/24, 4:17:27 PM] ~ Deepali coding: Will come today evening indrapuri
[02/04/24, 4:20:28 PM] Neha mam e.c: Kasim ye sab join ho gye kya
[02/04/24, 4:30:25 PM] Neha mam e.c: Inka kya hua
[02/04/24, 4:31:29 PM] ~ Mahi: PRASHANT RA
I	Technocrat Institute of Technology
	7398922086			
will think 12 april

'''




sender_names = [
    'Deepali coding:',
    'anup kumar ct:',
    'anchal e.c:',
    'annu❤️:',
    'naresh e.c:',
    'Hafsa.:',
    'khushi e.c:',
    'Lalita Sahu:',
    'Chauhan Shilpa:',
    'arpana e.c:',
    'Mahi:',
    'kasim k:',
]


# Message starts with [21/03/24, 4:33:57 PM] kasim k: like [{timestamp}]{space}{sender_name} to next few lines of message till next [{timestamp}]{space}{sender_name}

# Extracting messages from the text

messages = []
message_template = {
    'sender': '',
    'message': ''
}

students = []


message = message_template
for line in raw_data.split('\n'):
    if line:
        
        if line[0] == '[':
            messages.append(message)

            # Extract Name, Contact Number, College Name, Branch, Year from message['message']
            data = message['message']
			

            # print(data)
            # print('---------------')
            # print('---------------')
            # print('---------------')


            # data = data[data.index(':') + 1:]



            # if there is contact number present in data, find it using regex
            contact_number = re.findall(r'\d{10}', data)

            if contact_number:

                finished_data = data[data.index(']'):]
                finished_data = finished_data[finished_data.index(':')+2:]

                print(finished_data)
                print('------------------')
                print('------------------')
                print('------------------')
                print('------------------')


                contact_number = contact_number[0]

                # Find Name of the student, Generally it is after "Name :", "Name of Student:", "Name:-"
                name = re.findall(r'Name of Student:-|Name of Student:|Name :|Name:-', data)
                
				

                if name:
                    name = name[0]
                    name_index = data.index(name)
                    name = data[name_index + len(name):].split('\n')[0]
                    name = name.replace('-', '').replace(':', '').replace(';', '').strip()
                else:
                    name = ''

				

                # print(name + ' --- ' + contact_number)

                # college = re.findall(r'College', data)
                # if college:
                #     college = college[0]
                #     college_index = data.index(college)
                #     college = data[college_index + len(college):].split('\n')[0]
                #     college = college.replace('-', '').replace(':', '').replace(';', '').replace('name', '').strip()
                #     # print(college)
                # else:
                #     college = ''

                
                students.append({
                    'name': name,
                    'contact_number': contact_number
                })

		 
            message['message'] = line + '\n'
        else:
            message['message'] += line + '\n'

        # if line[0] == '[':
        #     messages.append(message)
        #     print(message)
        #     print('---------------')
        #     print('---------------')
        #     print('---------------')


        #     message['message'] += line 
        #     message = message_template
        # else:
        #     message['message'] += line 





       


print("Total Students: ", len(students))

