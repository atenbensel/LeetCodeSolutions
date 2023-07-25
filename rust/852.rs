impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = arr.len() - 1;

        while left < right {
            let mid = (left + right) / 2;
            if arr[mid] < arr[mid + 1] {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        left as i32
    }
}
