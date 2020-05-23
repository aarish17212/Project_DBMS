
import sqlite3
list1 = ['6E 292','6E 943','6E 263','6E 241','6E 458','6E 152','6E 315','6E 342','6E 153','6E 207','6E 206','6E 449','6E 147','6E 377','6E 378','6E 258','6E 210','6E 155','6E 551','6E 173','6E 102','6E 322','6E 138','6E 137','6E 265','6E 141','6E 306','AI 970','AI 971','AI 972','AI 973','AI 974','AI 975','AI 976','AI 977','AI 978','AI 979','AI 980','AI 981','AI 982','AI 983','AI 984','AI 985','AI 986','AI 987','AI 988','AI 989','AI 990','AI 991','AI 992','AI 993','AI 994','AI 995','AI 996','AI 997','AI 998','AI 999','SG 219','SG 220','SG 221','SG 222','SG 223','SG 224','SG 225','SG 226','SG 227','SG 228','SG 229','SG 231','SG 232','SG 233','G8 206','G8 207','G8 208','G8 209','G8 210','G8 211','G8 212','G8 213','G8 214','G8 215','G8 216','G8 217','G8 218','IX 435','IX 436','IX 437','IX 438','IX 439','IX 440','IX 441','IX 442','IX 443','IX 444','UK 877','UK 878','UK 879','UK 880','UK 881','UK 882','UK 883','UK 884','UK 885','UK 886','UK 887','UK 888','UK 889','UK 890','UK 891','UK 892','UK 893','UK 894','UK 895','UK 896','KW 717','KW 718','KW 719','KW 720','KW 721','KW 722','KW 723','KW 724','KW 725','KW 726','OP 124','OP 125','OP 126','OP 127','OP 128','OP 129','OP 130','OP 131','OP 132','OP 133']
connection = sqlite3.connect("database.db")
cur = connection.cursor()

for flight_id in list1:

	sql = ("select capacity from Flight_Information where flight_id=?")
	cur.execute(sql,(flight_id,))
	result = cur.fetchall()
	if(len(result)>0):
		capacity = result[0][0]

		for i in range(1,30):
			to_db = [(flight_id,"2020-5-"+str(i),capacity,)]
			connection.executemany("insert into Flight_seats(flight_id,booking_date,seats) values(?,?,?);",to_db)
			connection.commit()