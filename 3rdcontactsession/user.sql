CREATE TABLE "user"(
  id SERIAL PRIMARY KEY ,
  name VARCHAR(100),
  email VARCHAR(255),
  age INT
);

INSERT INTO "user" (name, email, age) VALUES ('Donald', 'donald@fake.email', 27);
INSERT INTO "user" (name, email, age) VALUES ('Jack', 'jack@fake.email', 24);

SELECT * FROM "user";

UPDATE "user" SET age = 21 WHERE name = 'Donald';

DELETE FROM "user" WHERE name = 'Jack';

