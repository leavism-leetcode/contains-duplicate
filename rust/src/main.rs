use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new();

        for number in &nums {
            if seen.contains(number) {
                return true;
            }
            seen.insert(number);
        }

        false
    }
}
