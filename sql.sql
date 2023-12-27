CREATE TABLE advertisers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    clicks INTEGER,
    views INTEGER
);

INSERT INTO advertisers (name, clicks, views) VALUES
('Advertiser 1', 0, 0),
('Advertiser 2', 0, 0);


CREATE TABLE ads (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255),
    img_url VARCHAR(255),
    link VARCHAR(255),
    clicks INTEGER,
    views INTEGER,
    advertiser_id INTEGER,
    FOREIGN KEY (advertiser_id) REFERENCES advertisers (id)
);


INSERT INTO ads (title, img_url, link, clicks, views, advertiser_id) VALUES
('Ad 1', 'img1.jpg', 'link1', 0, 0, 1),
('Ad 2', 'img2.jpg', 'link2', 0, 0, 1),
('Ad 3', 'img3.jpg', 'link3', 0, 0, 2);



SELECT * FROM advertisers;


SELECT name FROM advertisers;


SELECT ads.*, advertisers.name AS advertiser_name
FROM ads
JOIN advertisers ON ads.advertiser_id = advertisers.id;


SELECT name, SUM(clicks) AS total_clicks
FROM advertisers
GROUP BY name;