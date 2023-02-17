use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::path::{Path, PathBuf};

fn walk_dir(dir_path: &Path, current_dir: Option<&Path>) -> std::io::Result<()> {
    let current_dir = match current_dir {
        Some(dir) => dir.join(dir_path.file_name().unwrap()),
        None => PathBuf::new().join(dir_path),
    };

    for entry in std::fs::read_dir(dir_path)? {
        let entry = entry?;
        if entry.path().is_dir() {
            walk_dir(&entry.path(), Some(&current_dir))?;
        } else if entry.file_name() == "best.lint" {
            let file = File::open(entry.path())?;
            println!("{:?}", entry.path());
            let mut reader = BufReader::new(file);

            // Parse the file content and save the current directory path
            let mut count = 0;
            let mut in_fitness_section = false;
            let mut adj_list: Vec<Vec<u32>> = vec![];
            let mut adj_listss: Vec<Vec<Vec<u32>>> = vec![];
            let mut nodes = 0;
            let mut ind = 0;
            for line_ in reader.lines().enumerate() {
                let line = line_.1.unwrap();
                let mut fitness = 0.0;
                if line.contains("fitness") {
                    let split_fit: Vec<&str> = line.split(' ').collect();
                    if let Ok(f) = split_fit[0].parse::<f32>() {
                        fitness = f;
                    };
                    println!("{}", fitness);
                }
                // println!("{}", &line);
                if line.contains("Graph") {
                    in_fitness_section = true;
                    continue;
                }

                if in_fitness_section && count == 0 {
                    println!("{}", in_fitness_section);
                    // let mut first_line: String = "".to_string();
                    let first_line = line;
                    let split_first = first_line
                        // .expect("stuff")
                        .split(' ')
                        .map(|x| x.parse::<u32>().unwrap())
                        .collect::<Vec<_>>();
                    println!("{:?}", split_first);
                    // adj_list = Vec::<Vec<u32>>::with_capacity(split_first[0] as usize);
                    count += 1;
                    nodes = split_first[0];
                    println!("nodes: {}", nodes);
                    ind = 0;
                    continue;
                }

                if in_fitness_section && count >= 1 {
                    let line: Vec<u32> =
                        line.split(' ').map(|x| x.parse::<u32>().unwrap()).collect();

                    // let idx = line_.0;
                    if !line.is_empty() {
                        let mut tmp: Vec<u32> = Vec::new();
                        adj_list.push(tmp);
                        for numb in &line {
                            adj_list[ind].push(*numb);
                        }
                        ind += 1;
                    }
                    if ind == nodes as usize {
                        in_fitness_section = false;
                        count = 0;
                        println!("list length: {}", adj_list.len());
                        adj_listss.push(adj_list.clone());
                        adj_list.clear();
                    }
                    continue;
                }
                if adj_listss.len() == 30 {
                    // We found all adjacency lists, save the current directory path
                    let output_file = current_dir.join(format!(
                        "{}-output.txt",
                        entry.path().file_stem().unwrap().to_str().unwrap()
                    ));
                    if let Some(parent) = current_dir.parent() {
                        if parent.to_str().unwrap().contains("PM") {
                            println!("Path '{}' contains 'PM'", current_dir.display());
                        } else if parent.to_str().unwrap().contains("ED") {
                            println!("Path '{}' contains 'ED'", current_dir.display());
                        }
                    }
                    println!("{:?}", output_file);
                    let mut output = File::create(output_file)?;
                    for list in &adj_listss {
                        writeln!(output, "{:?}", list)?;
                    }
                    break;
                }
            }
        }
    }

    Ok(())
}

fn main() -> std::io::Result<()> {
    let root_dir_path = Path::new("/home/james/CEC2023");
    walk_dir(root_dir_path, None)
}
