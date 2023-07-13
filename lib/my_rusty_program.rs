use std::{thread, time};

fn main() {
    println!("Hello from the web!");
    thread::sleep(time::Duration::from_millis(2000));
    println!("I am an external program");
    thread::sleep(time::Duration::from_millis(2000));
    println!("cool, right 😎");
    thread::sleep(time::Duration::from_millis(2000));
}
