CREATE DATABASE friends;

\c friends;

CREATE TABLE person (
    id serial PRIMARY KEY,
    name varchar(50) NOT NULL
);

CREATE TABLE friend (
    person_id integer,
    friend_id integer
);


INSERT INTO person (name) VALUES ('me');
INSERT INTO person (name) VALUES ('my friend');
INSERT INTO person (name) VALUES ('my second friend');

INSERT INTO friend (person_id, friend_id) VALUES (1, 2);
INSERT INTO friend (person_id, friend_id) VALUES (1, 3);

INSERT INTO person (name) VALUES ('first new friend');
INSERT INTO person (name) VALUES ('second new friend');

INSERT INTO friend (person_id, friend_id) VALUES (2, 3);
INSERT INTO friend (person_id, friend_id) VALUES (2, 4);
INSERT INTO friend (person_id, friend_id) VALUES (3, 5);

-- Give a person, return the list of friend’s name
SELECT person.name FROM friend, person WHERE friend.person_id=:my_id AND person.id=friend.friend_id;

-- Give a person, return the list of the friend’s friend, but exclude any direct friends
SELECT person.name
FROM friend as second_level, friend as first_level, person
WHERE first_level.person_id=:my_id
  AND second_level.person_id = first_level.friend_id
  AND second_level.friend_id = person.id
  AND person.id not in (SELECT person.id FROM friend, person WHERE friend.person_id=:my_id AND person.id = friend.friend_id);


SELECT person.name
FROM friend as second_level, friend as first_level, person
WHERE first_level.person_id=:my_id
  AND second_level.person_id = first_level.friend_id
  AND second_level.friend_id = person.id
  AND person.id not in (SELECT person.id FROM friend, person WHERE friend.person_id=:my_id AND person.id = friend.friend_id);

