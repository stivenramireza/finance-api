CREATE TYPE document_type_enum AS ENUM ('CC', 'CE');

CREATE TABLE contacts (
	id SERIAL NOT NULL,
	name VARCHAR(100) NOT NULL,
	document_type document_type_enum DEFAULT 'CC',
	document VARCHAR(20) NOT NULL,
	email VARCHAR(50) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
);

COMMENT ON COLUMN contacts.id IS 'Contact id';
COMMENT ON COLUMN contacts.name IS 'Contact name';
COMMENT ON COLUMN contacts.document_type IS 'Contact document type';
COMMENT ON COLUMN contacts.document IS 'Contact document number';
COMMENT ON COLUMN contacts.email IS 'Contact email';
COMMENT ON COLUMN contacts.created_at IS 'Contact creation date';
COMMENT ON COLUMN contacts.updated_at IS 'Contact update date';
COMMENT ON TABLE contacts IS 'Contacts table';


CREATE TABLE users ( 
	id UUID NOT NULL,
	contact_id INTEGER NOT NULL,
	password VARCHAR(100) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id),
	CONSTRAINT contact_idxfk FOREIGN KEY (contact_id) REFERENCES contacts (id)
);

COMMENT ON COLUMN users.id IS 'User id';
COMMENT ON COLUMN users.contact_id IS 'The related contact';
COMMENT ON COLUMN users.password IS 'User password';
COMMENT ON COLUMN users.created_at IS 'User creation date';
COMMENT ON COLUMN users.updated_at IS 'User update date';
COMMENT ON COLUMN users.password IS 'User password';
COMMENT ON TABLE users IS 'Users table';
