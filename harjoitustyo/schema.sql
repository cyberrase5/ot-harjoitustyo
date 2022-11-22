CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	degree_id INTEGER
);

CREATE TABLE courses (
	id SERIAL PRIMARY KEY,
	course_name TEXT,
	ects INTEGER,
	degree_id INTEGER,
	mandatory BOOLEAN
);

CREATE TABLE participants (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users ON DELETE CASCADE,
	course_id INTEGER REFERENCES courses ON DELETE CASCADE,
	grade INTEGER
);
