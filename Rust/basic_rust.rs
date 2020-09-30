// Rust looks a lot different than python, same basic principles

// main function, rust can only run a binary (as opposed to library) with a main
fn main() {
    const THIS_CONSTANT: f32 = 77.2; // constant definition

    // function: requires explicit input and output types
    pub fn this_function(input: f32) -> f32 {
        let mut x = THIS_CONSTANT * input; // mutable variable definition "mutable means it can be changed"
        x = 8.0 * x;
        return x
    }

    let var = this_function(8f32); // immutable variable definition
    println!("{:?}", var); // print statement, a bit more complicated than in python
}
