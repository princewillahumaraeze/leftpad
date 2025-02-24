fn leftpad(s: &str, length: usize,  pad: &str){
	if length <= s.len(){
		println!("{s}");
		return 
	}
	let padding  = pad.repeat(length - s.len());
	println!("{}", padding+s);
}

fn main() {
    leftpad("Foo", 5, "*");
}
