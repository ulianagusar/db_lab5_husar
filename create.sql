CREATE TABLE Episodes
(
  episode_id INT NOT NULL,
  season INT NOT NULL,
  episode INT NOT NULL,
  PRIMARY KEY (episode_id)
);

CREATE TABLE Houses
(
  house_name CHAR(50) NOT NULL,
  PRIMARY KEY (house_name)
);

CREATE TABLE Characters
(
  name CHAR(50) NOT NULL,
  house_name CHAR(50) NOT NULL,
  PRIMARY KEY (name),
  FOREIGN KEY (house_name) REFERENCES Houses(house_name)
);

CREATE TABLE Deaths
(
  death_no INT NOT NULL,
  location CHAR(50) NOT NULL,
  method CHAR(50) NOT NULL,
  episode_id INT NOT NULL,
  killed_name CHAR(50) NOT NULL,
  killer_name CHAR(50) NOT NULL,
  PRIMARY KEY (death_no),
  FOREIGN KEY (episode_id) REFERENCES Episodes(episode_id),
  FOREIGN KEY (killed_name) REFERENCES Characters(name),
  FOREIGN KEY (killer_name) REFERENCES Characters(name)
);