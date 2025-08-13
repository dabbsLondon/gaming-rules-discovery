pub mod api;
pub mod parser;
pub mod db;
pub mod models;
pub mod validator;

#[cfg(test)]
mod tests {
    use crate::parser::{units, weapons};

    #[test]
    fn parse_unit_returns_placeholder() {
        let u = units::parse("test");
        assert_eq!(u.name, "placeholder");
    }

    #[test]
    fn parse_weapon_returns_placeholder() {
        let w = weapons::parse("test");
        assert_eq!(w.name, "placeholder");
    }
}
