-- Create document_type enumeration.
CREATE TYPE document_type_enum AS ENUM ('CC', 'CE');

-- Create contacts table.
CREATE TABLE contacts (
	id SERIAL NOT NULL,
	active BOOLEAN NOT NULL DEFAULT true,
	name VARCHAR(100) NOT NULL,
	document_type document_type_enum DEFAULT 'CC',
	document VARCHAR(20) NOT NULL UNIQUE,
	email VARCHAR(50) NOT NULL UNIQUE,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

-- Comment columns of contacts table.
COMMENT ON COLUMN contacts.id IS 'Contact id';
COMMENT ON COLUMN contacts.active IS 'Contact is active';
COMMENT ON COLUMN contacts.name IS 'Contact name';
COMMENT ON COLUMN contacts.document_type IS 'Contact document type';
COMMENT ON COLUMN contacts.document IS 'Contact document number';
COMMENT ON COLUMN contacts.email IS 'Contact email';
COMMENT ON COLUMN contacts.created_at IS 'Contact creation date';
COMMENT ON COLUMN contacts.updated_at IS 'Contact update date';
COMMENT ON TABLE contacts IS 'Contacts table';

-- Create users table.
CREATE TABLE users ( 
	id SERIAL NOT NULL,
	active BOOLEAN NOT NULL DEFAULT true,
	uid UUID NOT NULL,
	username VARCHAR(50) NOT NULL UNIQUE,
	password VARCHAR(100) NOT NULL,
	contact_id INTEGER NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	CONSTRAINT contact_idxfk FOREIGN KEY (contact_id) REFERENCES contacts (id)
);

-- Comment columns of users table.
COMMENT ON COLUMN users.id IS 'User id';
COMMENT ON COLUMN users.active IS 'User is active';
COMMENT ON COLUMN users.uid IS 'User identifier';
COMMENT ON COLUMN users.username IS 'User name';
COMMENT ON COLUMN users.password IS 'User password';
COMMENT ON COLUMN users.contact_id IS 'The related contact';
COMMENT ON COLUMN users.created_at IS 'User creation date';
COMMENT ON COLUMN users.updated_at IS 'User update date';
COMMENT ON TABLE users IS 'Users table';

-- Create some users.
INSERT INTO contacts 
	(name, document, email)
VALUES 
	('Test 1', '10471234578', 'test1@gmail.com'),
	('Test 2', '10471234579', 'test2@gmail.com');

INSERT INTO users 
	(uid, username, password, contact_id)
VALUES 
	('b85a613c-53ed-483a-a09b-a7a64b705702', 'test1', '$2b$12$pAyE.yEER3Vcfvv8vCo4..WKt2xUcdNL6yk.JXP1SiyRn2Ke0s2hG', 1),
	('a9ea6dd7-62a2-4318-be5e-164f948a985f', 'test2', '$2b$12$ZY6AY52WW/dxbPJN.BNOZeOxFoCvM3fFg8LZfMHSPrl5033nfoZMG', 2);

-- Create transactions table.
CREATE TABLE transactions (
	id SERIAL NOT NULL,
	concept VARCHAR(50) NOT NULL,
	amount FLOAT NOT NULL,
	source_user_id INTEGER NOT NULL,
	destination_user_id INTEGER NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	CONSTRAINT source_user_idxfk FOREIGN KEY (source_user_id) REFERENCES users (id),
	CONSTRAINT destination_user_idxfk FOREIGN KEY (destination_user_id) REFERENCES users (id)
);

-- Comment columns of transactions table.
COMMENT ON COLUMN transactions.id IS 'Transaction id';
COMMENT ON COLUMN transactions.concept IS 'Transaction concept';
COMMENT ON COLUMN transactions.amount IS 'Transaction amount';
COMMENT ON COLUMN transactions.source_user_id IS 'The related source user';
COMMENT ON COLUMN transactions.destination_user_id IS 'The related destination user';
COMMENT ON COLUMN transactions.created_at IS 'Transaction creation date';
COMMENT ON COLUMN transactions.updated_at IS 'Transaction update date';
COMMENT ON TABLE transactions IS 'Transactions table';

-- Create some transactions.
INSERT INTO transactions 
	(concept, amount, source_user_id, destination_user_id, created_at, updated_at)
VALUES 
	('Investment 1', 1500000, 1, 2, '2022-01-01 13:00:00', '2022-01-01 13:00:00'),
	('Investment 2', 2000000, 1, 2, '2022-02-01 15:00:00', '2022-02-01 15:00:00'),
	('Investment 3', 3000000, 1, 2, '2022-03-01 22:00:00', '2022-03-01 22:00:00'),
	('Investment 4', 4000000, 1, 2, '2022-04-01 14:00:00', '2022-04-01 14:00:00'),
	('Investment 5', 5500000, 1, 2, '2022-05-01 11:00:00', '2022-05-01 11:00:00'),
	('Investment 6', 6700000, 1, 2, '2022-06-01 13:00:00', '2022-06-01 13:00:00'),
	('Investment 7', 7000000, 1, 2, '2022-07-01 09:00:00', '2022-07-01 09:00:00'),
	('Investment 8', 8500000, 1, 2, '2022-08-01 08:00:00', '2022-08-01 08:00:00'),
	('Investment 1', 1000000, 2, 1, '2022-07-01 15:00:00', '2022-07-01 15:00:00'),
	('Investment 2', 2000000, 2, 1, '2022-08-01 12:00:00', '2022-08-01 12:00:00');
