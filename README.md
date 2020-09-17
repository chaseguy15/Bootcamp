# Bootcamp

This a simple file for finding important resources used during the Autopilot boot camp.

Detailed information on the Autopilot team can be found of the docs and in the boot camp recording videos on our google drive.

## OS
Getting your OS set up is important. If you run a Linux or Mac distribution, you are already set. If you run windows, we will need to get some Linux functionality going on your machine first.

There are a few ways to go about this:

- WSL. This allows you to use Linux features on a windows device. Though sometimes a pain, newer versions of wsl are becoming quite easy to manage. This is recommended for beginners.
- Dual boot. I would recommend dual booting to anyone that wants to familiarize with the full functionality of Linux.

### WSL
[wsl 2](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10)
[wsl 1](http://docs.uavaustin.org/guides/installation/getting-started/windows.html)

## Python
Python is used for the UGV drop code, and is just a generally good language to
know, especially when learning programming.

To install Python in a Linux kernel, run:

```shell
sudo apt-get update
sudo apt-get install python3.6
```

## Rust
Rust is the language of Pathfinder and a great way to learn the fundamentals of programming which can often be overlooked with more dynamic languages.

[install](https://www.rust-lang.org/tools/install)

- ["The Book"] (https://doc.rust-lang.org/book/)
- [By example] (https://doc.rust-lang.org/stable/rust-by-example/index.html)
- [Rustlings] (https://github.com/rust-lang/rustlings/)
- [Standard library] (https://doc.rust-lang.org/std/index.html)
- [Rust style guide] (https://doc.rust-lang.org/1.0.0/style/style/naming/README.html)

# Structure
The tentative schedule of boot camp is as follows:

- Day 1: Installations and an overview of the team, the code, and our goals.
- Day 2: Programming basics, a look at Python and making code
- Day 3: The UGV drop, algorithms, and early OOP
- Day 4: Pathfinder and jumping off the deep end with Rust
- Day 5: Microservices, networking, and revisiting the stack
- Day 6: Buffer day (Probably needed, covering these topics is very important)
