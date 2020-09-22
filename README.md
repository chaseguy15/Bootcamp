# Bootcamp

This a simple file for finding important resources used during the Autopilot boot camp.

Detailed information on the Autopilot team can be found of the docs and in the boot camp recording videos on our google drive.

## OS
Getting your OS set up is important. If you run a Linux or Mac distribution, you are already set. If you run windows, we will need to get some Linux functionality going on your machine first.

There are a few ways to go about this:

- WSL. This allows you to use Linux features on a windows device. Though sometimes a pain, newer versions of wsl are becoming quite easy to manage. This is recommended for beginners.
- Dual boot. I would recommend dual booting to anyone that wants to familiarize with the full functionality of Linux.

### WSL
If you have Windows version 1903 or greater: [WSL 2](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10)

If you have Windows version 1803 or greater (and don't want an easy to use Linux system): [WSL 1](http://docs.uavaustin.org/guides/installation/getting-started/windows.html)

#### Configuring Kernel

To configure the kernel you will need to edit the bashrc and bash_profile files. These files hold information on your kernel setting. To do this, you will need to get and run nano, a command-line text editor. Run:

```bash
sudo apt update
sudo apt-get install nano
sudo nano ~/.bashrc
```

This will open the .bashrc file within your root directory. We are now going to create an alias to jump to our working UAV directory. This saves us the hassle of moving directories all the time. Inside the file add the line:

```bash
alias uav='cd /c/Users/<your user>/Documents/UAV'
```

This makes it so that anytime you run "uav" in the kernel, bash reads "cd /c/Users/<your user>/Documents/UAV". This is what an alias does, lets you create custom inputs. The main command being used here is "cd" which stands for change directory. This is used to navigate the file system in unix and windows. If you would like, you can customize the directory and alias name from above to be whatever you like, as long as you have a way to quickly access your UAV folder.

You are then going to want to exit, save, and name the file. While still in the nano editor, input:

```bash
ctrl+c
y
enter
```

Please repeat the above process for the .bash_profile file as well, using the same alias if you changed it.

## Git
Git is used for version control and some documentation of the code.

To install Git run :


```bash
sudo apt update
sudo apt-get install curl
sudo apt-get install git-all
```
[UAV Austin Git install page](http://docs.uavaustin.org/guides/installation/git/index.html)

## Python
Python is used for the UGV drop code, and is just a generally good language to
know, especially when learning programming.

To install Python in a Linux kernel, run:

```bash
sudo apt update
sudo apt-get install python3.6
```

For reference on the style of Python, please refer to [the Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## Rust
Rust is the language of Pathfinder and a great way to learn the fundamentals of programming which can often be overlooked with more dynamic languages.

To install Rust, run:

```bash
sudo curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

- ["The Book"](https://doc.rust-lang.org/book/)
- [By example](https://doc.rust-lang.org/stable/rust-by-example/index.html)
- [Rustlings](https://github.com/rust-lang/rustlings/)
- [Standard library](https://doc.rust-lang.org/std/index.html)
- [Rust style guide](https://doc.rust-lang.org/1.0.0/style/style/naming/README.html)

# Structure
The tentative schedule of boot camp is as follows:

- Day 1: Installations and an overview of the team, the code, and our goals.
- Day 2: Programming basics, a look at Python and making code
- Day 3: The UGV drop, algorithms, and early OOP
- Day 4: Pathfinder and jumping off the deep end with Rust
- Day 5: Microservices, networking, and revisiting the stack
- Day 6: Buffer day (Probably needed, covering these topics is very important)
