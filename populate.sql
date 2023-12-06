INSERT INTO Houses (house_name) VALUES
('House Stark'),
('House Arryn'),
('Dothraki'),
('House Lannister'),
('House Clegane'),
('House Vale'); 

INSERT INTO Episodes (episode_id, season, episode) VALUES
(101, 1, 1),
(104, 1, 4),
(105, 1, 5);

INSERT INTO Characters (name, house_name) VALUES
('Ned Stark', 'House Stark'),
('Jon Arryn', 'House Arryn'),
('Lysa Arryn', 'House Arryn'),
('Dothraki man', 'Dothraki'),
('Gregor "the Mountain" Clegane', 'House Lannister'),
('Cleganes horse', 'House Clegane'),
('Stark soldier', 'House Stark'),
('Lannister soldier', 'House Lannister'),
('Will', 'House Stark'),
('Ser Hugh of the Vale', 'House Vale'); 

INSERT INTO Deaths (death_no, location, method, episode_id, killed_name, killer_name) VALUES
(3, 'Winterfell', 'Sword', 101, TRIM('Will'), 'Ned Stark'),
(6, 'Kings Landing', 'Poison', 101, 'Jon Arryn', 'Lysa Arryn'),
(7, 'Pentos', 'Arakh', 101, 'Dothraki man', 'Dothraki man'),
(11, 'Kings Landing', 'Spear', 104, 'Ser Hugh of the Vale', 'Gregor "the Mountain" Clegane'),
(12, 'Kings Landing', 'Sword', 105, 'Cleganes horse', 'Gregor "the Mountain" Clegane'),
(22, 'Kings Landing', 'Spear', 105, 'Stark soldier', 'Lannister soldier'),
(23, 'Kings Landing', 'Spear', 105, 'Stark soldier', 'Lannister soldier');