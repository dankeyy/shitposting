// So here's the thing- you can't invoke proc macro in the same crate you made it, 
// but I refuse to make a cargo project in this repo, 
// so here I split the code to- creation file -> test file -> run

// ---------------------------------------- tmp/src/lib.rs ----------------------------------------

use proc_macro::TokenStream;
use syn::{Token, Ident, LitStr, parse::Parse, parse::ParseStream};


struct LazyStatic {
    structure : Ident,
    attr      : LitStr,
}


impl Parse for LazyStatic {
    fn parse(input: ParseStream) -> Result<Self, syn::Error> {
        let attr: LitStr = input.parse()?;
        input.parse::<Token![,]>()?;
        let structure: Ident = input.parse()?;
        Ok( LazyStatic { attr, structure } )
    }
}


#[proc_macro]
pub fn getattr(body: TokenStream) -> TokenStream {
    let LazyStatic { attr, structure } = syn::parse_macro_input!(body as LazyStatic);
    let attr_ident = Ident::new(&attr.value(), proc_macro2::Span::call_site());

    let res = format!("{}.{}", structure, attr_ident).parse::<TokenStream>().unwrap();

    println!("gottem -> {}", res);
    res
}
      

// ---------------------------------------- tmp/test/poop.rs ----------------------------------------
      
use project::getattr;

#[derive(Debug)]
struct Foo<'a> {
    a: u32,
    b: &'a str,
}

#[test]
fn testitt() {

    let bloop = Foo {a: 1, b: "banana"};

    println!("{:?}", getattr!("a", bloop));
    println!("{:?}", getattr!("b", bloop));
}
             
             
// ---------------------------------------- Run ----------------------------------------

/* 
cargo test -- --nocapture
   Compiling tmp v0.1.0 (/home/dankey/testing/tmp)
gottem -> bloop.a
gottem -> bloop.b
    Finished test [unoptimized + debuginfo] target(s) in 0.26s
     Running unittests src/lib.rs (/home/dankey/testing/tmp/target/debug/deps/tmp-f3d5a93c73fa58b8)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/poop.rs (/home/dankey/testing/tmp/target/debug/deps/poop-14bb0ae1a0508355)

running 1 test
1
"banana"
test testitt ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests tmp

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

*/
