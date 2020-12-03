CREATE TABLE IF NOT EXISTS 'users' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'username' TEXT NOT NULL,
    'email' TEXT NULL,
    'hash' TEXT NOT NULL,
    'birthday' DATETIME NOT NULL,
    'registered' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS 'records' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    'user_id' INTEGER NOT NULL,
    'name' TEXT NOT NULL,
    'timestamp' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- seeds
INSERT INTO users ('username', 'email', 'hash', 'birthday')
    VALUES ('scchung10', 'chungsumching@gmail.com', '535000$T.qO6MmyAcyTgKvr$xZ060P31YeMjgygAo12paRuz7xrum8GFMT1QN8Ia7uB', '1994-11-06 00:00:00');

INSERT INTO records ('user_id', 'name', 'timestamp')
    VALUES (1, 'Seeing an old friend', '2020-11-03 15:31:06');
INSERT INTO records ('user_id', 'name', 'timestamp')
    VALUES (1, 'Hearing a song that reminds you of your past', '2020-11-03 15:31:06');
INSERT INTO records ('user_id', 'name', 'timestamp')
    VALUES (1, 'A bit of good news for a loved one/friend', '2020-11-04 15:31:06');
INSERT INTO records ('user_id', 'name', 'timestamp')
    VALUES (1, 'Getting a thank you from someone', '2020-11-04 15:31:06');
INSERT INTO records ('user_id', 'name', 'timestamp')
    VALUES (1, 'Eating comfort food', '2020-12-03 15:31:06');
