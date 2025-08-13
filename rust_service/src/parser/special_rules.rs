use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct SpecialRule {
    pub name: String,
}

pub fn parse(_raw: &str) -> SpecialRule {
    SpecialRule { name: "placeholder".into() }
}
