use crate::parser::units::Unit;

pub fn validate_unit(unit: &Unit) -> bool {
    !unit.name.is_empty()
}
