use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct HarvestRecord {
    pub id: i32,
    pub name: String,
}
