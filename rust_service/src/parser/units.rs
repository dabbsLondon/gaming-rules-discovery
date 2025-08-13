use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct Unit {
    pub name: String,
}

pub fn parse(_raw: &str) -> Unit {
    Unit { name: "placeholder".into() }
}
