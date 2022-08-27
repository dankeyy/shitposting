macro_rules! typed {
    ($e:expr, $type:ty) => {

        if let Some(f) = (&$e as &dyn std::any::Any).downcast_ref::<$type>() {
            fn poo(f: $type) {
                println!("{} is {}", f, stringify!($type));
            }

            poo(f.to_owned());
            return;
        }

    };
}


fn kek<T: 'static>(t: T) {
        typed!(t, &str);
        typed!(t, String);
        typed!(t, char);
        typed!(t, f32);
        typed!(t, f64);
        typed!(t, u8);
        typed!(t, u16);
        typed!(t, u32);
        typed!(t, u64);
        typed!(t, usize);
        typed!(t, i8);
        typed!(t, i16);
        typed!(t, i32);
        typed!(t, i64);
        typed!(t, isize);
}


fn main() {
    kek("poo");
    kek(String::from("pee"));
    kek('F');
    kek(1337usize);
    kek(1.618f64);
}

// output:
// poo is &str
// pee is String
// F is char
// 1337 is usize
// 1.618 is f64
