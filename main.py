import sqlite3

conn = sqlite3.connect('moviestable.db')

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE movie (
	movie_name text,
	actor_name text,
	Second_actor_name text,
	year_released int,
	director_name text
	)""")

many_movie = [
			('Shershaah', 'Sidharth Malhotra', 'Kiara Advani', '2021', 'Vishnu Varadhan'),
			('3 Idiots', 'Aamir Khan', 'Madhavan', '2009', 'Rajkumar Hirani'),
			('Kashmir Files', 'Darshan Kumar', 'Pallavi Joshi', '2022', 'Vivek Agnihotri'),
            ('Article 15', 'Ayushman Khurrana', 'Isha Talwar', '2019', 'Anubhav Sinha'),
			('M S Dhoni', 'Sushant Singh Rajput', 'Kiara Advani', '2016', 'Neeraj Pandey'),
		]

cursor.executemany("INSERT INTO movie VALUES (?,?,?,?,?)", many_movie)

cursor.execute("SELECT * FROM movie")

items = cursor.fetchall()

for item in items:
	print(item)


cursor.execute("SELECT * FROM movie WHERE actor_name='Sushant Singh Rajput'")
print("Your search for actor is")
print(cursor.fetchone())

conn.commit()

conn.close()
