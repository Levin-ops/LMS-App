from app import app

from models import db, User, Student, Instructor, Course

users = [{
  "id": 1,
  "firstname": "Onida",
  "lastname": "Thieme",
  "email": "othieme0@gizmodo.com",
  "password": "493b75df64246ea3783b4ed7aade2f395a7044e9",
  "usertype": "instructor",
  "photo_url": "https://robohash.org/ideosullam.png?size=50x50&set=set1",

}, {
  "id": 2,
  "firstname": "Augy",
  "lastname": "Brewerton",
  "email": "abrewerton1@freewebs.com",
  "password": "ba80fd8e0372e0e1c8ed18b7e89e7dfe991c441b",
  "usertype": "instructor",
  "photo_url": "https://robohash.org/officiaetcommodi.png?size=50x50&set=set1",
 
}, {
  "id": 3,
  "firstname": "Elicia",
  "lastname": "Novis",
  "email": "enovis2@sfgate.com",
  "password": "a276bf03f1f84fadaa76d6b98b9df467964f0974",
  "usertype": "student",
  "photo_url": "https://robohash.org/adipiscietplaceat.png?size=50x50&set=set1",

}, {
  "id": 4,
  "firstname": "Imojean",
  "lastname": "Perrat",
  "email": "iperrat3@pcworld.com",
  "password": "aee1956052b998db9be07714dbb173b56adf77c4",
  "usertype": "student",
  "photo_url": "https://robohash.org/distinctioautqui.png?size=50x50&set=set1",

}, {
  "id": 5,
  "firstname": "Waverly",
  "lastname": "Lowen",
  "email": "wlowen4@rakuten.co.jp",
  "password": "2f27bcde7a6da8df68b5663485610016785d5fea",
  "usertype": "student",
  "photo_url": "https://robohash.org/idaliquamqui.png?size=50x50&set=set1",

}, {
  "id": 6,
  "firstname": "Herminia",
  "lastname": "Ashlin",
  "email": "hashlin5@discuz.net",
  "password": "3b166f80def50cadca1b37a06cb0d251f3fc9ea1",
  "usertype": "instructor",
  "photo_url": "https://robohash.org/harumenimcum.png?size=50x50&set=set1",

}, {
  "id": 7,
  "firstname": "Sashenka",
  "lastname": "Gorsse",
  "email": "sgorsse6@google.com.br",
  "password": "91b67eed6f046f9615fa3f904c847f50edb5e7dd",
  "usertype": "instructor",
  "photo_url": "https://robohash.org/adipisciassumendaquod.png?size=50x50&set=set1",
 
}, {
  "id": 8,
  "firstname": "Margot",
  "lastname": "Crewes",
  "email": "mcrewes7@census.gov",
  "password": "5a03e19b1367ec75aa3826b724faba1090e97ea3",
  "usertype": "student",
  "photo_url": "https://robohash.org/praesentiumconsectetureligendi.png?size=50x50&set=set1"
}, {
  "id": 9,
  "firstname": "Michaelina",
  "lastname": "Speeks",
  "email": "mspeeks8@geocities.jp",
  "password": "83e338aaabf92111403fda9b57e766f0e34b7572",
  "usertype": "instructor",
  "photo_url": "https://robohash.org/nisilaboriosamdelectus.png?size=50x50&set=set1",
  
}, {
  "id": 10,
  "firstname": "Jeromy",
  "lastname": "Barends",
  "email": "jbarends9@geocities.com",
  "password": "ee8aa721674acedf7354b2d78de5633a54bdbbb5",
  "usertype": "instructor",
  "photo_url": "https://robohash.org/similiquesapientevoluptatem.png?size=50x50&set=set1",
  
}]

students = [{
  "id": 1,
  "student_fname": "Theresa",
  "student_lname": "Lowten",
  "email": "tlowten0@printfriendly.com",
  "usertype": "student"
}, {
  "id": 2,
  "student_fname": "Emma",
  "student_lname": "Raulin",
  "email": "eraulin1@sourceforge.net",
  "usertype": "student"
}, {
  "id": 3,
  "student_fname": "Byram",
  "student_lname": "Langfield",
  "email": "blangfield2@nsw.gov.au",
  "usertype": "student"
}, {
  "id": 4,
  "student_fname": "Nevin",
  "student_lname": "Martell",
  "email": "nmartell3@google.fr",
  "usertype": "student"
}, {
  "id": 5,
  "student_fname": "Cyrille",
  "student_lname": "Denness",
  "email": "cdenness4@spotify.com",
  "usertype": "student"
}, {
  "id": 6,
  "student_fname": "Dar",
  "student_lname": "Neachell",
  "email": "dneachell5@miitbeian.gov.cn",
  "usertype": "student"
}, {
  "id": 7,
  "student_fname": "Mendy",
  "student_lname": "Berzins",
  "email": "mberzins6@mayoclinic.com",
  "usertype": "student"
}, {
  "id": 8,
  "student_fname": "Maison",
  "student_lname": "Amor",
  "email": "mamor7@hao123.com",
  "usertype": "student"
}, {
  "id": 9,
  "student_fname": "Bert",
  "student_lname": "Towns",
  "email": "btowns8@meetup.com",
  "usertype": "student"
}, {
  "id": 10,
  "student_fname": "Louise",
  "student_lname": "Goodlake",
  "email": "lgoodlake9@eepurl.com",
  "usertype": "student"
}]

instructors = [{
  "id": 1,
  "instructor_fname": "Wally",
  "instructor_lname": "Mebes",
  "bio": "wmebes0@diigo.com",
  "experience": "Saxion Universities ",
  "specialization": "Profound system-worthy middleware",
  "usertype": "instructor"
}, {
  "id": 2,
  "instructor_fname": "Monte",
  "instructor_lname": "Mallen",
  "bio": "mmallen1@creativecommons.org",
  "experience": "Chowan College",
  "specialization": "Decentralized asymmetric infrastructure",
  "usertype": "instructor"
}, {
  "id": 3,
  "instructor_fname": "Benton",
  "instructor_lname": "Dinsale",
  "bio": "bdinsale2@bbb.org",
  "experience": "Tatung Institute of Technology",
  "specialization": "Team-oriented fault-tolerant complexity",
  "usertype": "instructor"
}, {
  "id": 4,
  "instructor_fname": "Aleece",
  "instructor_lname": "Christie",
  "bio": "achristie3@amazonaws.com",
  "experience": "Ishik University",
  "specialization": "Digitized mission-critical service-desk",
  "usertype": "instructor"
}, {
  "id": 5,
  "instructor_fname": "Florette",
  "instructor_lname": "Figger",
  "bio": "ffigger4@mac.com",
  "experience": "Drexel University",
  "specialization": "Distributed cohesive initiative",
  "usertype": "instructor"
}, {
  "id": 6,
  "instructor_fname": "Daniella",
  "instructor_lname": "Hindrich",
  "bio": "dhindrich5@gmpg.org",
  "experience": "School of Banking and Management in Cracow",
  "specialization": "Team-oriented 24/7 standardization",
  "usertype": "instructor"
}, {
  "id": 7,
  "instructor_fname": "Dorene",
  "instructor_lname": "Stanbridge",
  "bio": "dstanbridge6@msn.com",
  "experience": "Chinju National University of Education",
  "specialization": "Universal non-volatile pricing structure",
  "usertype": "instructor"
}, {
  "id": 8,
  "instructor_fname": "Marja",
  "instructor_lname": "Crowest",
  "bio": "mcrowest7@ebay.co.uk",
  "experience": "Universitas Jambi",
  "specialization": "Team-oriented motivating capacity",
  "usertype": "instructor"
}, {
  "id": 9,
  "instructor_fname": "Curran",
  "instructor_lname": "Busch",
  "bio": "cbusch8@moonfruit.com",
  "experience": "University of the East, Coloocan",
  "specialization": "Reduced disintermediate model",
  "usertype": "instructor"
}, {
  "id": 10,
  "instructor_fname": "Harley",
  "instructor_lname": "Sissland",
  "bio": "hsissland9@google.ca",
  "experience": "International University of Fundamental Studies, St. Petersburg",
  "specialization": "Organic fresh-thinking capability",
  "usertype": "instructor"
}]

courses = [{
  "id": 1,
  "title": "Kilo Bravo Quebec Victor Whiskey Juliett Lima Sierra India Zulu Delta Oscar Mike",
  "description": "amet nunc viverra dapibus nulla suscipit ligula in lacus curabitur at ipsum ac",
  "duration": "6 months",
  "instructor_id": 1
}, {
  "id": 2,
  "title": "India Quebec Victor Echo Delta Papa Juliett Sierra Uniform Bravo",
  "description": "amet eleifend pede libero quis orci nullam molestie nibh in lectus pellentesque at nulla suspendisse",
  "duration": "7 months",
  "instructor_id": 2
}, {
  "id": 3,
  "title": "India Tango Bravo Lima November Oscar Kilo Mike Sierra Golf Charlie",
  "description": "nisi volutpat eleifend donec ut dolor morbi vel lectus in quam fringilla",
  "duration": "6 months",
  "instructor_id": 3
}, {
  "id": 4,
  "title": "Papa Romeo Echo Yankee Lima Bravo Mike November Quebec Whiskey Golf Kilo Delta Zulu Victor",
  "description": "sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus etiam vel augue vestibulum rutrum rutrum neque",
  "duration": "6 months",
  "instructor_id": 4
}, {
  "id": 5,
  "title": "November Echo Quebec Juliett Yankee X-ray Romeo Sierra Kilo Oscar Whiskey Foxtrot Uniform India",
  "description": "varius integer ac leo pellentesque ultrices mattis odio donec vitae nisi nam ultrices libero non mattis pulvinar nulla pede",
  "duration": "8 months",
  "instructor_id": 5
}, {
  "id": 6,
  "title": "Victor Sierra Foxtrot Golf Zulu Whiskey Lima Echo Mike Alfa Uniform Juliett",
  "description": "leo odio porttitor id consequat in consequat ut nulla sed accumsan felis",
  "duration": "5 months",
  "instructor_id": 6
}, {
  "id": 7,
  "title": "Foxtrot Charlie Mike Whiskey Oscar X-ray India Kilo Juliett Hotel Yankee Echo",
  "description": "vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum",
  "duration": "6 months",
  "instructor_id": 7
}, {
  "id": 8,
  "title": "Papa Quebec Mike Alfa Yankee Delta Uniform Juliett Foxtrot Kilo X-ray Victor India",
  "description": "pretium iaculis justo in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat",
  "duration": "16 months",
  "instructor_id": 8
}, {
  "id": 9,
  "title": "Oscar Delta Sierra Whiskey Zulu Golf Echo Bravo Victor Alfa Charlie India X-ray Kilo Quebec Romeo Hotel",
  "description": "tellus semper interdum mauris ullamcorper purus sit amet nulla quisque arcu",
  "duration": " 36 months",
  "instructor_id": 9
}, {
  "id": 10,
  "title": "Victor Charlie Uniform November Mike Lima Tango Zulu Juliett Alfa Quebec Delta Kilo Romeo Whiskey Papa X-ray",
  "description": "egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis eget",
  "duration": "76 months",
  "instructor_id": 10
}]

with app.app_context():
    db.session.add_all([User(**user) for user in users])
    db.session.add_all([Student(**student) for student in students])
    db.session.add_all([Instructor(**instructor) for instructor in instructors])
    db.session.add_all([Course(**course) for course in courses])
    db.session.commit()