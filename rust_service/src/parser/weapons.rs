use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct Weapon {
    pub name: String,
}

pub fn parse(_raw: &str) -> Weapon {
    Weapon { name: "placeholder".into() }
}
