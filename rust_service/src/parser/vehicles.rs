use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct Vehicle {
    pub name: String,
}

pub fn parse(_raw: &str) -> Vehicle {
    Vehicle { name: "placeholder".into() }
}
