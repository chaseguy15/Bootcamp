pub struct HorizontalStruct {
    h_field1: f64,
    h_field2: bool,
}

impl HorizontalStruct {
    pub fn new(h_field1: f64, h_field2: bool) -> Self {
        Self {
            h_field1,
            h_field2,
        }
    }

    pub fn printer(&self) -> f64 {
        let f = self.h_field1;
        let bool = self.h_field2;

        if bool == true {
            return f;
        } else {
            return 0.0f64;
        }
    }
}
