#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(warnings)]

pub mod backend;
mod horizontal;

use backend::backend_file::Back;
use horizontal::HorizontalStruct;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_this() {
        let horiz = HorizontalStruct::new(4.3f64, true);
        let back = Back::make(3.5f32);
        let ret = horiz.printer();

        assert_eq!(back.field1, 3.5f32);
        assert_eq!(ret, 4.3f64); // assert_eq is used to check values are equal if testing
    }
}
