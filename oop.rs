trait AbstractAnimal {
    fn kind(&self)  -> &str { "any generic animol" }
    fn sound(&self) -> &str { "brrr" }
}

trait MakeSound {
    fn speak(&self) {
        println!("kek");
    }
}


struct Animal {}
struct Dog    {}
struct Human  {}
struct Cat    {}


impl<T> MakeSound for T
where T: AbstractAnimal
{
    fn speak(&self) {
        println!("{} goes {}", self.kind(), self.sound());
    }
}

impl MakeSound for Human {}

impl AbstractAnimal for Animal {}

impl AbstractAnimal for Dog {
    fn kind(&self)  -> &str { "dog"  }
    fn sound(&self) -> &str { "woof" }
}

impl AbstractAnimal for Cat {
    fn kind(&self)  -> &str { "cat"  }
    fn sound(&self) -> &str { "meow" }
}


fn main() {
    let dog = Dog {};
    let cat = Cat {};
    let hummus = Human {};
    let animol = Animal {};

    dog.speak();
    cat.speak();
    animol.speak();
    print!("except the stupid human that talks and says ");
    hummus.speak();

    println!("I eat mostly {}s and {}s but ok with {}", cat.kind(), dog.kind(), animol.kind());
}

// output:
// dog goes woof
// cat goes meow
// any generic animol goes brrr
// except the stupid human that talks and says kek
// I eat mostly cats and dogs but ok with any generic animol
