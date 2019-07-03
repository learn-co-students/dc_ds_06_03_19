CREATE TABLE author (
    author_id INT,
    name TEXT,
    country TEXT
);

CREATE TABLE book (
    book_id INT,
    title TEXT,
    pages INT
);

CREATE TABLE book_author (
    author_id INT,
    book_id INT
);

INSERT INTO author
    (author_id, name, country)
VALUES
    (1, 'J.D. Salinger', 'USA'),
    (2, 'F. Scott. Fitzgerald', 'USA'),
    (3, 'Jane Austen', 'UK'),
    (4, 'Scott Hanselman', 'USA'),
    (5, 'Jason N. Gaylord', 'USA'),
    (6, 'Pranav Rastogi', 'India'),
    (7, 'Todd Miranda', 'USA'),
    (8, 'Christian Wenz', 'USA')
;

INSERT INTO book
    (book_id, title, pages)
VALUES
    (1, 'The Catcher in the Rye', 500),
    (2, 'Nine Stories', 600),
    (3, 'Franny and Zooey', 700),
    (4, 'The Great Gatsby', 800),
    (5, 'Tender id the Night', 200),
    (6, 'Pride and Prejudice', 30000),
    (7, 'Professional ASP.NET 4.5 in C# and VB', 3)
;

INSERT INTO book_author
    (book_id, author_id)
VALUES
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (6, 3),
    (7, 4),
    (7, 5),
    (7, 6),
    (7, 7),
    (7, 8)
;
