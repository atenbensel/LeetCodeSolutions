impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut char_set: [bool; 256] = [false; 256];
        
        let mut max_length = 0;
        let mut start = 0;
        
        for (end, c) in s.chars().enumerate() {
            let char_index = c as usize;
            
            while char_set[char_index] {

                let start_char_index = s.chars().nth(start).unwrap() as usize;
                char_set[start_char_index] = false;
                start += 1;
            }
            
            char_set[char_index] = true;
            max_length = max_length.max(end - start + 1);
        }
        
        max_length as i32
    }
}
