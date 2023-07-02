/// Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
/// You may assume that each input would have exactly one solution, and you may not use the same element twice.
/// You can return the answer in any order.

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    use std::collections::HashMap;
    let mut r: HashMap<i32, i32> = HashMap::new();
    for i in 0..nums.len() {
        r.insert(nums[i], i as i32);
    }

    for i in 0..nums.len() {
        match r.get(&(target - nums[i])) {
            Some(index) if i as i32 != *index => return vec![i as i32, index.clone()],
            None => {}
            _ => {}
        }
    }
    vec![]
}
}