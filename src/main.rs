use std::process::{Command,
                   Output};
use std::io;
use openpty;

struct GameServer {
    stdout_output: Vec<String>,
    stdout_handle: io::Result<()>,
    stdin_handle:  io::Result<()>,
    process:       Command,
}

impl GameServer {
    fn record_input() {

    }

    fn send_input() {

    }

    fn start_server() -> Output {

        let (master, slave, name = openpty::openpty(None, None, None)
            .expect("Creating pty failed");

        Command::new("sh")
            .stdout(slave)
            .spawn()
            .expect("Executing process failed")
    }

    fn record_output() {
    
    }

    fn start_recording_thread() {

    }

    fn start() {

    }
}


fn main() {
    println!("{:?}", start_server());
}
