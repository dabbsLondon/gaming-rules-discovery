CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS units (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    raw_ocr TEXT,
    source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS weapons (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    raw_ocr TEXT,
    source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS vehicles (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    raw_ocr TEXT,
    source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS special_rules (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    raw_ocr TEXT,
    source_id INTEGER REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS pending_reviews (
    id SERIAL PRIMARY KEY,
    entity_type TEXT NOT NULL,
    entity_id INTEGER NOT NULL,
    differences JSONB
);

CREATE TABLE IF NOT EXISTS weapon_hosts (
    weapon_id INTEGER REFERENCES weapons(id),
    host_type TEXT NOT NULL,
    host_id INTEGER NOT NULL,
    PRIMARY KEY (weapon_id, host_type, host_id)
);

CREATE TABLE IF NOT EXISTS unit_special_rules (
    unit_id INTEGER REFERENCES units(id),
    special_rule_id INTEGER REFERENCES special_rules(id),
    PRIMARY KEY (unit_id, special_rule_id)
);
